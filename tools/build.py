"""Build a static clone of macroheadshots.com from the browser capture."""
import base64, hashlib, html, json, os, re, shutil, sys
from urllib.parse import unquote

CAP = sys.argv[1]
OUT = sys.argv[2]
FORM_ID = "F39Doj60gH02JaLUfmFP"

d = json.load(open(CAP))
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(f"{OUT}/assets"); os.makedirs(f"{OUT}/css"); os.makedirs(f"{OUT}/js")

EXT = {"image/webp": "webp", "image/png": "png", "image/jpeg": "jpg", "image/gif": "gif",
       "image/svg+xml": "svg", "image/avif": "avif", "image/x-icon": "ico", "image/vnd.microsoft.icon": "ico",
       "font/woff2": "woff2", "font/woff": "woff", "font/ttf": "ttf", "video/mp4": "mp4"}

# --- assets: write each once (dedupe by content) and map URL -> local path
url_map, by_hash = {}, {}
for url, a in d["assets"].items():
    if "data" not in a:
        continue
    head, b64 = a["data"].split(",", 1)
    raw = base64.b64decode(b64)
    h = hashlib.sha1(raw).hexdigest()[:12]
    if h not in by_hash:
        base = unquote(url.split("?")[0]).rstrip("/").split("/")[-1]
        stem = re.sub(r"[^A-Za-z0-9_-]+", "-", base.rsplit(".", 1)[0])[:40] or "asset"
        ext = EXT.get(a["type"].split(";")[0], base.rsplit(".", 1)[-1].lower())
        name = f"{stem}-{h}.{ext}"
        open(f"{OUT}/assets/{name}", "wb").write(raw)
        by_hash[h] = f"/assets/{name}"
    url_map[url] = by_hash[h]

def localize(text):
    # longest URLs first so proxy URLs win over the inner origin URL they wrap
    for url in sorted(url_map, key=len, reverse=True):
        local = url_map[url]
        for variant in {url, url.replace("&", "&amp;")}:
            text = text.replace(variant, local)
    return text

# --- stylesheets: localize non-Google CSS, keep Google Fonts remote
css_map = {}
for url, body in d["css"].items():
    if "fonts.googleapis.com" in url:
        continue
    name = re.sub(r"[^A-Za-z0-9_.-]+", "-", url.split("?")[0].split("/")[-1])
    open(f"{OUT}/css/{name}", "w").write(localize(body))
    css_map[url] = f"/css/{name}"

FORM_EMBED = (f'<iframe src="https://api.leadconnectorhq.com/widget/form/{FORM_ID}" '
              f'style="width:100%;height:100%;min-height:960px;border:none;border-radius:0px" '
              f'id="inline-{FORM_ID}" data-layout="{{\'id\':\'INLINE\'}}" data-trigger-type="alwaysShow" '
              f'data-activation-type="alwaysActivated" data-deactivation-type="neverDeactivate" '
              f'data-form-id="{FORM_ID}" title="Appointments form"></iframe>'
              f'<script src="https://link.msgsndr.com/js/form_embed.js"></script>')

def replace_form(page):
    """Swap the server-rendered HighLevel form (needs their app JS) for the official embed."""
    m = re.search(r'(<div class="c-form-[^"]*"|<div class="cform-[^"]*")[^>]*>', page)
    if not m:
        return page
    start = m.start()
    # walk to the matching closing div
    depth, i = 0, start
    for t in re.finditer(r"<(/?)div\b[^>]*>", page[start:]):
        depth += -1 if t.group(1) else 1
        if depth == 0:
            i = start + t.end(); break
    return page[:start] + f'<div class="cform-embed">{FORM_EMBED}</div>' + page[i:]

def clean(page):
    page = re.sub(r'<script[^>]*type="module"[^>]*></script>', "", page)
    page = re.sub(r'<link[^>]*(?:as="script"|rel="modulepreload")[^>]*>', "", page)
    page = re.sub(r"<script>window\.__NUXT__=.*?</script>", "", page, flags=re.S)
    page = re.sub(r'<script type="application/json"[^>]*__NUXT_DATA__[^>]*>.*?</script>', "", page, flags=re.S)
    page = re.sub(r'<script[^>]*(?:libphonenumber|intl-tel-input|intlTelInput)[^>]*></script>', "", page)
    page = re.sub(r"<noscript>\s*<iframe[^>]*googletagmanager.*?</noscript>", "", page, flags=re.S)
    page = re.sub(r'<link rel="(?:preconnect|dns-prefetch)"[^>]*>', "", page)
    # stylesheets
    for url, local in css_map.items():
        for v in {url, url.replace("&", "&amp;")}:
            page = page.replace(f'href="{v}"', f'href="{local}"')
    page = re.sub(r'<link rel="preload" as="style" href="https://fonts\.googleapis[^>]*>', "", page)
    page = page.replace('media="print" onload="this.media=\'all\'"', "")
    page = replace_form(page)
    page = localize(page)
    # internal links -> relative
    page = re.sub(r'href="https?://(?:www\.)?macroheadshots\.com/?', 'href="/', page)
    page = page.replace('href="/home"', 'href="/"')
    page = re.sub(r"<!---->|<!--\[-->|<!--\]-->", "", page)
    page = page.replace("</body>", '<script src="/js/site.js" defer></script>\n</body>')
    return page

routes = {"/": "index.html", "/appointments": "appointments.html", "/pricing": "pricing.html"}
for p in d["pages"]:
    if p.startswith("/headshots-in-"):
        routes[p] = p.strip("/") + ".html"

for path, file in routes.items():
    page = clean(d["pages"][path]["html"])
    os.makedirs(os.path.dirname(f"{OUT}/{file}") or OUT, exist_ok=True)
    open(f"{OUT}/{file}", "w").write(page)
    left = sorted(set(re.findall(r"https?://(?:images\.leadconnectorhq|assets\.cdn\.filesafe|storage\.googleapis|firebasestorage)[^\"' )]+", page)))
    print(f"{file}: {len(page)//1024} KB, remote assets left: {len(left)}", left[:3])

print("assets:", len(by_hash), "files")
