"""Check every internal link, asset and #anchor in the built site, using Vercel's cleanUrls/rewrite/redirect rules."""
import json, os, re, sys
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT = sys.argv[1]
cfg = json.load(open(f"{ROOT}/vercel.json"))
redirects = {r["source"]: r["destination"] for r in cfg.get("redirects", [])}

def resolve(path):
    """Return the file Vercel would serve for a path, or None (404)."""
    path = unquote(path)
    if path in redirects:
        return resolve(urlparse(redirects[path]).path)
    m = re.fullmatch(r"/headshots-in-([^/]+)/", path)
    if m:
        path = f"/headshots-in-{m.group(1)}"
    if path == "/":
        cand = ["index.html"]
    elif path.endswith("/"):
        cand = [path.strip("/") + "/index.html", path.strip("/") + ".html"]
    else:
        p = path.lstrip("/")
        cand = [p, p + ".html", p + "/index.html"]
    if path.endswith(".html"):  # cleanUrls redirects /x.html -> /x
        cand = [path.lstrip("/")]
    for c in cand:
        if os.path.isfile(os.path.join(ROOT, c)):
            return c
    return None

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs = []; self.ids = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a: self.ids.add(a["id"])
        for k in ("href", "src", "data-consent-embed"):
            if a.get(k): self.refs.append((tag, k, a[k]))
        if a.get("srcset"):
            for part in a["srcset"].split(","):
                self.refs.append((tag, "srcset", part.strip().split(" ")[0]))

pages = {}
for f in sorted(os.listdir(ROOT)):
    if f.endswith(".html"):
        p = P(); p.feed(open(os.path.join(ROOT, f)).read()); pages[f] = p

problems, external, checked = [], set(), 0
for f, p in pages.items():
    for tag, attr, ref in p.refs:
        if ref.startswith(("tel:", "mailto:", "data:", "blob:", "javascript:")):
            continue
        u = urlparse(ref)
        if u.scheme in ("http", "https"):
            if u.netloc in ("macroheadshots.com", "www.macroheadshots.com"):
                ref = u.path or "/"; u = urlparse(ref)
            else:
                external.add(ref); continue
        if ref.startswith("#"):
            if ref[1:] and ref[1:] not in p.ids:
                problems.append((f, ref, "missing anchor on same page"))
            checked += 1; continue
        target = resolve(u.path or "/")
        checked += 1
        if not target:
            problems.append((f, ref, "404")); continue
        if u.fragment and target.endswith(".html"):
            tp = pages.get(target)
            if tp and u.fragment not in tp.ids:
                problems.append((f, ref, f"missing anchor #{u.fragment} on {target}"))

# CSS url() references
for root, _, files in os.walk(ROOT):
    for fn in files:
        if fn.endswith(".css"):
            css = open(os.path.join(root, fn)).read()
            for ref in re.findall(r"url\(['\"]?([^'\")]+)", css):
                if ref.startswith(("data:", "http", "#")):
                    continue
                checked += 1
                if not resolve(ref if ref.startswith("/") else "/" + os.path.relpath(os.path.join(root, ref), ROOT)):
                    problems.append((fn, ref, "404 (css)"))

# sitemap URLs
sm = open(os.path.join(ROOT, "sitemap.xml")).read()
for loc in re.findall(r"<loc>([^<]+)</loc>", sm):
    checked += 1
    if not resolve(urlparse(loc).path):
        problems.append(("sitemap.xml", loc, "404"))

# original site URLs that must keep working
legacy = ["/", "/home", "/appointments", "/pricing", "/gallery"] + [f"/headshots-in-{t}/" for t in
          ["bloomingdale", "clifton", "haledon", "hawthorne", "little-falls", "milford", "north-haledon", "passaic",
           "paterson", "pompton-lakes", "prospect-park", "ringwood", "totowa", "wanaque", "wayne", "woodland-park"]]
for l in legacy:
    checked += 1
    if not resolve(l):
        problems.append(("legacy URL", l, "404"))

print(f"checked {checked} internal references across {len(pages)} pages")
print("problems:", len(problems))
for x in problems[:50]:
    print("  ", x)
print("external links:", len(external))
for x in sorted(external):
    print("  ", x)
