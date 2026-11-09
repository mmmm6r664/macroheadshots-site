"""Generate the redesigned Macro Headshots site (Shiprocket-style) from the captured content."""
import html, json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from towns import TOWN_INFO

CONTENT, ASSETS_SRC, BRAND, OUT = sys.argv[1:5]
HERE = os.path.dirname(os.path.abspath(__file__))
c = json.load(open(CONTENT))

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(f"{OUT}/assets"); os.makedirs(f"{OUT}/css"); os.makedirs(f"{OUT}/js")
shutil.copy(f"{HERE}/styles.css", f"{OUT}/css/styles.css")
shutil.copy(f"{HERE}/main.js", f"{OUT}/js/main.js")
import hashlib as _h
CSS_V = _h.sha1(open(f"{HERE}/styles.css", "rb").read()).hexdigest()[:10]
JS_V = _h.sha1(open(f"{HERE}/main.js", "rb").read()).hexdigest()[:10]
shutil.copy(f"{BRAND}/logo-dark.png", f"{OUT}/assets/logo-dark.png")
shutil.copy(f"{BRAND}/logo-light.png", f"{OUT}/assets/logo-light.png")
for _l in ("logo-new.svg", "logo-new-dark.svg"): shutil.copy(f"{BRAND}/{_l}", f"{OUT}/assets/{_l}")
shutil.copy(f"{BRAND}/hero-clients.webp", f"{OUT}/assets/hero-clients.webp")
shutil.copy(f"{BRAND}/eras-sample.jpg", f"{OUT}/assets/eras-sample.jpg")
for _d in ("directions-1", "directions-2"): shutil.copy(f"{BRAND}/{_d}.webp", f"{OUT}/assets/{_d}.webp")
ERAS_KB = round(os.path.getsize(f"{BRAND}/eras-sample.jpg") / 1024)

_files = os.listdir(ASSETS_SRC)
def asset(media_id, name):
    """Copy the largest captured version of an image and return its public path."""
    cands = [f for f in _files if f.startswith(media_id)]
    best = max(cands, key=lambda f: os.path.getsize(f"{ASSETS_SRC}/{f}"))
    ext = best.rsplit(".", 1)[-1]
    shutil.copy(f"{ASSETS_SRC}/{best}", f"{OUT}/assets/{name}.{ext}")
    return f"/assets/{name}.{ext}"

IMG = {
    "hero": asset("66fdb1f4e76d596e375401aa", "hero-collage"),
    "g1": asset("66fdb5d9ed66473b3eb3a9ae", "headshot-1"),
    "g2": asset("66fdb5d9f4a520218037f73d", "headshot-2"),
    "g3": asset("66fdb5d99491366d01602453", "headshot-3"),
    "retouch": asset("66fdb7489491364ec060249a", "retouching-before-after"),
    "perk_retouch": asset("66febe6068a53a1b2c16f8e6", "icon-retouching"),
    "perk_reviews": asset("66febe609274d088a96e4564", "icon-reviews"),
    "perk_delivery": asset("66febe601f683282c3aeafa4", "icon-delivery"),
    "perk_backdrops": asset("66febe60b27ab0e9b1cb2ea4", "icon-backdrops"),
}
GAL_DIR = os.path.join(HERE, "..", "gallery")
GALLERY = json.load(open(os.path.join(GAL_DIR, "manifest.json")))
os.makedirs(f"{OUT}/assets/gallery", exist_ok=True)
for _n, *_ in GALLERY:
    shutil.copy(os.path.join(GAL_DIR, _n), f"{OUT}/assets/gallery/{_n}")
IG_DIR = os.path.join(HERE, "..", "instagram")
IG = []
for f in sorted(os.listdir(IG_DIR)):
    shutil.copy(os.path.join(IG_DIR, f), f"{OUT}/assets/{f}")
    IG.append(f"/assets/{f}")

LOGOS = [
    (asset("67f438d613578e181a3a68e5", "client-hudson-county"), "Hudson County, New Jersey"),
    (asset("67f43900694f31187c4d51f0", "client-city-of-hoboken"), "City of Hoboken"),
    (asset("67f4394e694f31580e4d52e3", "client-pelvic-rehabilitation-medicine"), "Pelvic Rehabilitation Medicine"),
    (asset("67f44d2dc4c944d72b702d29", "client-st-joseph-hospital"), "St. Joseph Hospital"),
    (asset("67f43a8635b033163042e6c1", "client-10square-development"), "10Square Development"),
]
map_files = [f for f in _files if f.startswith("map-lhdOqf8lzu")]
MAP = None
if map_files:
    best = max(map_files, key=lambda f: os.path.getsize(f"{ASSETS_SRC}/{f}"))
    shutil.copy(f"{ASSETS_SRC}/{best}", f"{OUT}/assets/studio-map.{best.rsplit('.',1)[-1]}")
    MAP = f"/assets/studio-map.{best.rsplit('.',1)[-1]}"

PHONE, PHONE_TEL = "877-622-4973", "tel:8776224973"
ADDRESS = "195 US-46, Suite 9, Totowa, New Jersey 07512"
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=Macro+Headshots+195+US-46+Totowa+NJ&query_place_id=ChIJBQf90R9ZwokR1-oGndIZRCA"
FB, IG_URL = "https://www.facebook.com/MacroHeadshots", "https://instagram.com/macroheadshots"
FORM_ID = "F39Doj60gH02JaLUfmFP"
REVIEWS = [
    ("Courtney R.", "Great work! They get you in and out quickly and the turnaround for headshots was within 24 hours"),
    ("Vanessa B.", "First time getting professional headshots and I was nervous. The photographer was really helpful. Suggested some amazing poses. Quality Pictures at amazing price"),
    ("Mayra V.", "I had a great experience. It was an easy and straightforward process. I really appreciated hearing recommended photo poses based on industry."),
    ("Vincent B.", "Honestly amazing for the price and time. Quick in and out session with someone who\u2019s clearly experienced and knows what they are doing. If you need something quick and ASAP. This is your guy!"),
    ("Jeannette R.", "Great quality & professional experience taking Headshots. I appreciate the recommendation of poses and the various number of shots provided in my session. Definetly would recommend"),
    ("Cemal K.", "I just got my headshot from here. I was in rush, and they helped me a lot. They have the best price in New Jersey."),
    ("Dawn D.", "Staff is extremely professional and my pictures turned out beautifully. Great service and final results. Highly impressed."),
    ("Manar H.", "The photographer was super friendly and patient. The photos turned out amazing. Highly recommend!"),
    ("Inijah Q.", "Fantastic. The photographer was great. Got the edited pictures within 2 hours. Highly recommended"),
]
PRICES = [("1 Headshot", "$50", "5 minute session", "About 5–10 photos in different poses"),
          ("3 Headshots", "$100", "10–15 minute session", "About 15–20 photos in different poses"),
          ("5 Headshots", "$150", "30 minute session", "About 20–40 photos in different poses"),
          ("10 Headshots", "$250", "1 hour session", "About 40–100 photos in different poses")]
PICKS = [1, 3, 5, 10]

TOWNS = []
for p in c:
    if p.startswith("/headshots-in-"):
        slug = p.strip("/")
        name = slug.replace("headshots-in-", "").replace("-", " ").title()
        TOWNS.append((slug, name))
for _k in TOWN_INFO:
    if f"headshots-in-{_k}" not in [t for t, _ in TOWNS]:
        TOWNS.append((f"headshots-in-{_k}", _k.replace("-", " ").title()))
TOWNS.sort()

# ---------- icons (simple inline line icons) ----------
def icon(name):
    p = {
        "check": '<path d="M20 6 9 17l-5-5"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
        "layers": '<path d="m12 3 9 5-9 5-9-5 9-5Z"/><path d="m3 13 9 5 9-5"/>',
        "sparkle": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
        "timer": '<circle cx="12" cy="13" r="8"/><path d="M12 9v4M9 2h6"/>',
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/>',
        "pin": '<path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12Z"/><circle cx="12" cy="10" r="2.5"/>',
        "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
        "mask": '<path d="M4 5c5 2 11 2 16 0v6a8 8 0 0 1-16 0V5Z"/><path d="M9 10h.01M15 10h.01M9 15c1.7 1.3 4.3 1.3 6 0"/>',
        "wand": '<path d="m15 4 5 5L9 20l-5-5L15 4Z"/><path d="m12 7 5 5"/>',
        "arrow": '<path d="M7 17 17 7M8 7h9v9"/>',
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
        "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M8 3v4M16 3v4M3 10h18"/>',
        "image": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="m21 16-5-5-9 9"/>',
    }[name]
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'

FB_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H8v4h2v8h4v-8h3l1-4h-4V8.5c0-.3.2-.5.5-.5Z"/></svg>'
IG_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>'

e = html.escape

# ---------- shared chrome ----------
SITE = "https://macroheadshots.com"
BUSINESS_LD = {
    "@context": "https://schema.org", "@type": "ProfessionalService", "@id": SITE + "/#business",
    "name": "Macro Headshots", "url": SITE + "/", "telephone": "+1-877-622-4973",
    "image": SITE + "/assets/hero-clients.webp", "logo": SITE + "/assets/icon-512.png",
    "priceRange": "$50 - $250",
    "description": "Professional headshot studio in Totowa, NJ: corporate, acting, residency (ERAS) and personal branding headshots, retouched and delivered within 24 hours.",
    "address": {"@type": "PostalAddress", "streetAddress": "195 US-46, Suite 9", "addressLocality": "Totowa", "addressRegion": "NJ", "postalCode": "07512", "addressCountry": "US"},
    "areaServed": ["New York Metro Area"] + [n + ", NJ" for _, n in TOWNS],
    "sameAs": [FB, IG_URL],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Headshot packages", "itemListElement": [
        {"@type": "Offer", "name": t, "price": a.strip("$"), "priceCurrency": "USD", "description": f"{s}. {sh}. Professional retouching included.", "url": SITE + "/pricing"}
        for t, a, s, sh in PRICES]},
}

def canon(path):
    return SITE + ("/" if path in ("/", "") else path)

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>"

def head(title, desc, path, extra_ld=(), preload=None, robots="index,follow"):
    url = canon(path)
    pre = f'<link rel="preload" as="image" href="{preload}" fetchpriority="high">' if preload else ""
    extra = "".join(ld(x) for x in extra_ld)
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#735ae5">
<meta name="format-detection" content="telephone=yes">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Macro Headshots">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Macro Headshots clients">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}/assets/og-image.jpg">
<meta name="geo.region" content="US-NJ">
<meta name="geo.placename" content="Totowa">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
{pre}
<link rel="stylesheet" href="/css/styles.css?v={CSS_V}">
{ld(BUSINESS_LD)}{extra}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def breadcrumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": canon(pth)} for i, (n, pth) in enumerate(items)]}

def faq_ld(extra=()):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in list(extra) + FAQS]}

SERVICES = [
    ("corporate-headshots", "Corporate Headshots"), ("linkedin-headshots", "LinkedIn Headshots"),
    ("acting-headshots", "Acting Headshots"), ("residency-headshots", "Residency Headshots"),
    ("professional-headshots", "Professional Headshots"), ("executive-headshots", "Executive Headshots"),
    ("team-headshots", "Team Headshots"), ("headshot-retouching", "Headshot Retouching"),
]

def nav(active):
    sub = "".join(f'<a href="/{s}/">{n}</a>' for s, n in SERVICES)
    def link(h, t):
        return f'<a href="{h}"{" class=\"active\"" if active == h else ""}>{t}</a>'
    svc_active = active == "/services" or (active or "").strip("/") in [s for s, _ in SERVICES]
    return f"""<header class="nav" id="nav">
  <div class="nav-inner">
    <a class="nav-logo" href="/" aria-label="Macro Headshots home"><img src="/assets/logo-new.svg" alt="Macro Headshots" width="629" height="240"></a>
    <nav class="nav-links" aria-label="Main">
      <div class="dd"><a href="/services"{" class='active'" if svc_active else ""}>Services</a><div class="dd-menu">{sub}<a href="/services" class="dd-all">All services →</a></div></div>
      {link("/locations", "Locations")}{link("/portfolio", "Portfolio")}{link("/guides", "Guides")}{link("/pricing", "Pricing")}
    </nav>
    <div class="nav-cta">
      <a class="btn btn-outline btn-sm" href="{PHONE_TEL}">Call {PHONE}</a>
      <a class="btn btn-primary btn-sm" href="/appointments">Book Now</a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">{icon('menu')}</button>
    </div>
  </div>
</header>
<main id="main">
"""

def crumbs(items):
    parts = []
    for i, (n, pth) in enumerate(items):
        parts.append(f'<span aria-current="page">{e(n)}</span>' if i == len(items) - 1 else f'<a href="{pth}">{e(n)}</a>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span class="sep">›</span>'.join(parts) + '</nav>'

def footer():
    towns = "".join(f'<li><a href="/{s}/">{n}</a></li>' for s, n in TOWNS)
    return f"""</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <img class="logo" src="/assets/logo-new-dark.svg" alt="Macro Headshots" width="629" height="240" loading="lazy">
        <h2 class="fh">Reach Us At</h2>
        <div class="reach">
          <div>{icon('phone')}<a href="{PHONE_TEL}">{PHONE}</a></div>
          <div>{icon('pin')}<a href="{MAPS_URL}" target="_blank" rel="noopener">Studio: {ADDRESS}</a></div>
        </div>
        <div class="socials"><a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{FB_SVG}</a><a href="{IG_URL}" target="_blank" rel="noopener" aria-label="Instagram">{IG_SVG}</a></div>
      </div>
      <div>
        <h2 class="fh">Services</h2>
        <ul>{"".join(f'<li><a href="/{s}/">{n}</a></li>' for s, n in SERVICES)}<li><a href="/#personal-branding">Personal Branding</a></li></ul>
        <h2 class="fh" style="margin-top:26px">Studio</h2>
        <ul><li><a href="/portfolio">Portfolio &amp; Reviews</a></li><li><a href="/guides">Guides &amp; FAQs</a></li><li><a href="/pricing">Pricing</a></li><li><a href="/appointments">Book an Appointment</a></li></ul>
      </div>
      <div>
        <h2 class="fh"><a href="/locations">Locations</a></h2>
        <ul class="cols2"><li><a href="/locations#studio">Totowa Studio</a></li>{towns}</ul>
      </div>
    </div>
    <div class="footer-bottom"><span>© 2026 Macro Headshots. All rights reserved.</span><span class="legal"><a href="/privacy-policy">Privacy Policy</a><a href="/cookie-policy">Cookie Policy</a><button type="button" class="linklike" data-cookie-settings>Cookie settings</button></span></div>
  </div>
</footer>
<div class="cookie-banner" id="cookie-banner" role="dialog" aria-live="polite" aria-label="Cookie consent" hidden>
  <p><b>We use cookies</b> Essential cookies keep the site and booking form working. With your consent we also load our Instagram feed, which may set their own cookies. <a href="/cookie-policy">Read our cookie policy</a></p>
  <div class="cookie-actions"><button type="button" class="btn btn-outline btn-sm" data-consent="necessary">Necessary only</button><button type="button" class="btn btn-primary btn-sm" data-consent="all">Accept all</button></div>
</div>
<div class="mobile-bar"><a class="btn btn-outline" href="{PHONE_TEL}">Call</a><a class="btn btn-primary" href="/appointments">Book Now</a></div>
<script src="/js/main.js?v={JS_V}" defer></script>
</body>
</html>
"""

BLOBS = '<div class="hero-blobs" aria-hidden="true"><span class="b1"></span><span class="b2"></span><span class="b3"></span><span class="b4"></span></div>'

# ---------- sections ----------
def hero(place, lead, town=False, h1=None, home=False):
    h1 = h1 or f'Headshots near <span class="accent">{e(place)}</span>, NJ'
    why = ""
    if home:
        why = f'''<ul class="why-list">
        <li>{icon('check')}<span><b>Packages from $50</b> · published prices, no surprises</span></li>
        <li>{icon('clock')}<span><b>Retouched &amp; emailed within 24 hours</b></span></li>
        <li>{icon('layers')}<span><b>Unlimited backgrounds</b> · studio backdrops or digital</span></li>
        <li>{icon('wand')}<span><b>Every photo retouched</b> and color graded</span></li>
        <li>{icon('pin')}<span><b>Real studio:</b> 195 US-46, Suite 9, Totowa, NJ</span></li>
      </ul>'''
    return f"""<section class="hero">
  {BLOBS}
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">{icon('pin')} {(e(place) + " clients visit our Totowa studio" if place != "Totowa" else "Our studio is right here in Totowa") if town else "Serving Northern New Jersey &amp; NYC"}</span>
      <h1>{h1}</h1>
      <p class="lead">{e(lead)}</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="/appointments">Book Your Session</a>
        <a class="btn btn-outline" href="/pricing">See Pricing</a>
      </div>
      {why or f'''<div class="chips">
        <span class="chip">{icon('clock')} Retouched in 24 hours</span>
        <span class="chip">{icon('layers')} Unlimited backgrounds</span>
        <span class="chip">{icon('sparkle')} Every photo retouched</span>
      </div>'''}
    </div>
    <div class="hero-visual">
      <img class="collage" src="/assets/hero-clients.webp" alt="Recent Macro Headshots clients: corporate and professional headshots" width="1200" height="940" fetchpriority="high">
      <div class="float-card fc1"><span class="ic ok">{icon('check')}</span><div><b>Retouched &amp; delivered</b><small>within 24 hours</small></div></div>
      <div class="float-card fc2"><span class="ic">{icon('calendar')}</span><div><b>Sessions from $50</b><small>5 minutes to 1 hour</small></div></div>
    </div>
  </div>
</section>
"""

def trust():
    tiles = "".join(f'<div class="logo-tile"><img src="{s}" alt="{e(a)}" loading="lazy"></div>' for s, a in LOGOS)
    return f"""<section class="trust"><div class="wrap trust-inner">
  <h2>Trusted by <b>professionals &amp; organizations</b> across New Jersey</h2>
  <div class="logos">{tiles}</div>
</div></section>
"""

def bullets(items):
    return "<ul>" + "".join(f"<li>{icon('check')}<span>{x}</span></li>" for x in items) + "</ul>"

def services(retouch_text, place=None):
    gph = lambda n, cap: f'<div class="ph"><img src="/assets/gallery/{n}.webp" alt="{cap} headshot by Macro Headshots" loading="lazy"><div class="ph-cap">{cap}<span class="arrow-btn">{icon("arrow")}</span></div></div>'
    ig = lambda i, cap: f'<div class="ph"><img src="{IG[i]}" alt="{cap} headshot by Macro Headshots" loading="lazy"><div class="ph-cap">{cap}<span class="arrow-btn">{icon("arrow")}</span></div></div>'
    return f"""<section class="section" id="services">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What we do</span>
      <h2>Look at the absolute best you have ever looked</h2>
      <p class="lead">{"Corporate, acting and branding headshots for " + e(place) + " clients — shot in our Totowa studio and retouched by experts." if place else "Corporate headshots, acting headshots and more — shot in our Totowa studio and retouched by experts."}</p>
    </div>
    <div class="stack">
      <article class="stack-card">
        <div class="stack-top"><div class="stack-label"><div><span class="stack-num">1/3</span><div class="stack-icon">{icon('briefcase')}</div></div><h3>Corporate<br>headshots</h3></div><a class="btn btn-white btn-sm" href="/appointments">Book now</a></div>
        <div class="stack-body">
          <div class="stack-text"><p>For business professionals who want a polished, confident image for LinkedIn, company websites and team pages.</p>{bullets(['A comfortable, relaxed studio so you feel at ease', 'Unlimited backgrounds — studio backdrops or digital background changes', 'Every photo retouched and delivered within 24 hours'])}</div>
          <div class="stack-media">{gph('headshot-20b','Professional')}{gph('headshot-05a','Corporate')}{gph('headshot-12a','Executive')}</div>
        </div>
      </article>
      <article class="stack-card">
        <div class="stack-top"><div class="stack-label"><div><span class="stack-num">2/3</span><div class="stack-icon">{icon('mask')}</div></div><h3>Acting<br>headshots</h3></div><a class="btn btn-white btn-sm" href="/appointments">Book now</a></div>
        <div class="stack-body">
          <div class="stack-text"><p>For aspiring and working actors who need headshots that truly capture their personality — and get them noticed.</p>{bullets(['Sessions from 5 to 60 minutes', 'Pick your favourite shots from every session', 'Natural-looking retouching on every image'])}</div>
          <div class="stack-media">{ig(1,'Actor')}{ig(2,'Lifestyle')}{ig(0,'Personal brand')}</div>
        </div>
      </article>
      <article class="stack-card">
        <div class="stack-top"><div class="stack-label"><div><span class="stack-num">3/3</span><div class="stack-icon">{icon('wand')}</div></div><h3>Expert<br>retouching</h3></div><a class="btn btn-white btn-sm" href="/pricing">See pricing</a></div>
        <div class="stack-body">
          <div class="stack-text"><p><b>We are the retouching experts.</b></p>{f'<p class="small">{e(retouch_text)}</p>' if retouch_text else ""}{bullets(['Included with every headshot package', 'Background changes done digitally'])}</div>
          <div class="stack-media one"><div class="ph"><img src="{IMG['retouch']}" alt="Before and after headshot retouching" loading="lazy"><div class="ph-cap">Before → After<span class="arrow-btn">{icon('arrow')}</span></div></div></div>
        </div>
      </article>
    </div>
  </div>
</section>
"""

def residency(place=None):
    specs = [("JPG or PNG", "AAMC file type"), ("≤ 150 KB", "AAMC maximum size"), ("Face centered", "AAMC requirement"), ("375 × 525 px", "2.5 × 3.5 in, passport size")]
    spec_html = "".join(f'<div class="spec"><b>{a}</b><small>{b}</small></div>' for a, b in specs)
    return f"""<section class="section" id="residency">
  <div class="wrap">
    <div class="res-band">
      <div class="res-text">
        <span class="eyebrow">{icon('briefcase')} Residency headshots</span>
        <h2>Residency &amp; ERAS headshots for {"medical applicants from " + e(place) if place else "medical applicants"}</h2>
        <p class="lead">Your photo is one of the first things program directors see on your residency application. We photograph you in a polished, business-professional style on a clean backdrop, then deliver a file that meets the AAMC ERAS photo rules alongside your full-resolution, retouched images.</p>
        <div class="specs">{spec_html}</div>
        {bullets(['Quick sessions — the 5-minute package starts at $50', 'Retouched and delivered within 24 hours, in time for application deadlines', 'Your face centered, as AAMC requires, on a plain light backdrop'])}
        <div class="hero-actions"><a class="btn btn-primary" href="/appointments">Book a residency headshot</a><a class="btn btn-outline" href="{PHONE_TEL}">Ask a question</a></div>
      </div>
      <div class="res-visual">
        <div class="eras-card">
          <div class="eras-top"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="eras-title">Application photo</span></div>
          <div class="eras-photo"><span class="dim dim-w">2.5 in</span><span class="dim dim-h">3.5 in</span><img src="/assets/eras-sample.jpg" alt="Example ERAS residency headshot: head and shoulders on a plain light backdrop, 375 by 525 pixels" loading="lazy"></div>
          <div class="eras-meta"><span>eras-photo.jpg · {ERAS_KB} KB</span><span>375 × 525 px</span></div>
        </div>
        <div class="float-card rc1"><span class="ic ok">{icon('check')}</span><div><b>Upload-ready</b><small>Meets AAMC ERAS rules</small></div></div>
        <div class="float-card rc2"><span class="ic">{icon('clock')}</span><div><b>Delivered in 24 hours</b><small>retouched</small></div></div>
      </div>
    </div>
  </div>
</section>
"""

def branding(place=None):
    tiles = [
        (7, "Realtors", "Listings, yard signs and your brokerage or Zillow profile."),
        (2, "Influencers", "A consistent, recognizable look across Instagram, TikTok and YouTube."),
        (10, "Consultants", "LinkedIn, proposals and the About page of your website."),
        (6, "Speakers", "Event programs, speaker one-sheets and press kits."),
        (1, "Content creators", "Thumbnails, channel art and brand media kits."),
    ]
    html_t = "".join(f'<a class="brand-tile" href="/appointments"><img src="{IG[i]}" alt="Personal branding headshot for {t.lower()}" loading="lazy"><div class="bt-body"><div class="bt-head"><h3>{t}</h3><span class="arrow-btn">{icon("arrow")}</span></div><p>{d}</p></div></a>' for i, t, d in tiles)
    return f"""<section class="section soft" id="personal-branding">
  <div class="wrap">
    <div class="section-head head-split"><div><span class="eyebrow">{icon('sparkle')} Personal branding</span><h2>Personal branding headshots{" in " + e(place) if place else ""}</h2></div>
    <p class="lead">When you are the brand, your photo does the introducing. We create headshots with personality for realtors, influencers, consultants, speakers and content creators — images that feel like you and look great everywhere you show up.</p></div>
    <div class="brand-grid">{html_t}</div>
    <div class="brand-foot">
      <div class="chips" style="margin-top:0">
        <span class="chip">{icon('layers')} Unlimited backgrounds</span>
        <span class="chip">{icon('timer')} Longer sessions for more looks</span>
        <span class="chip">{icon('sparkle')} Every photo retouched</span>
      </div>
      <a class="btn btn-primary" href="/appointments">Book a branding session</a>
    </div>
  </div>
</section>
"""

def team_intro():
    return f"""<section class="section" id="team">
  <div class="wrap split">
    <div class="split-media"><img src="/assets/gallery/{GALLERY[0][0]}" alt="A client portrait in the Macro Headshots studio" width="{GALLERY[0][1]}" height="{GALLERY[0][2]}" loading="lazy"></div>
    <div>
      <span class="eyebrow">{icon('image')} Meet the team</span>
      <h2>The photographers behind Macro Headshots</h2>
      <p class="lead" style="margin-top:18px">Our photographers work in one dedicated studio in Totowa, with professional lighting and backdrops set up and ready, so your session starts on time. During the shoot we coach you on posture and expression, then our retouching team edits every image you choose and emails it within 24 hours.</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:22px"><a class="btn btn-primary" href="/appointments">Book a session</a><a class="btn btn-outline" href="/portfolio">See our work</a></div>
    </div>
  </div>
</section>
"""

def strengths(about):
    cards = [
        ("24", "hrs", "Every retouched photo is delivered within 24 hours of your session.", "clock"),
        ("∞", "backgrounds", "Unlimited backgrounds — studio backdrops plus digital background changes.", "layers"),
        ("100", "%", "All pictures are retouched — no extra add-ons to think about.", "sparkle"),
        ("5–60", "min", "Session packages from a quick 5 minutes up to a full hour.", "timer"),
    ]
    html_cards = "".join(f'<div class="stat-card"><div class="big">{b}<small>{s}</small></div><p>{t}</p><span class="ic">{icon(i)}</span></div>' for b, s, t, i in cards)
    return f"""<section class="section soft">
  <div class="wrap">
    <div class="section-head head-split"><div><span class="eyebrow">Why Macro Headshots</span><h2>Our core strengths</h2></div><p class="lead clamp">{e(about)}</p></div>
    <div class="cards4">{html_cards}</div>
  </div>
</section>
"""

def gallery():
    alt = {"studio": "Studio headshot", "location": "On-location headshot", "medical": "Medical professional headshot"}
    fig = lambda x: f'<figure><img src="/assets/gallery/{x[0]}" alt="{alt[x[3]]} by Macro Headshots" width="{x[1]}" height="{x[2]}" loading="lazy" decoding="async"></figure>'
    row1 = [x for x in GALLERY if x[0][-6] == "a"]
    row2 = [x for x in GALLERY if x[0][-6] != "a"]
    r1 = "".join(fig(x) for x in row1); r2 = "".join(fig(x) for x in row2)
    return f"""<section class="section soft" id="gallery">
  <div class="wrap">
    <div class="section-head head-split"><div><span class="eyebrow">{icon('image')} Client gallery</span><h2>Real clients, real results</h2></div>
    <p class="lead">Corporate, personal branding, on-location and medical professional headshots from recent sessions at Macro Headshots. Follow more work on <a href="{IG_URL}" target="_blank" rel="noopener" style="color:var(--brand);font-weight:600">Instagram @macroheadshots</a>.</p></div>
  </div>
  <div class="marquee"><div class="marquee-track">{r1}{r1}</div></div>
  <div class="marquee reverse" style="margin-top:18px"><div class="marquee-track">{r2}{r2}</div></div>
</section>
"""

def retouching(text):
    return f"""<section class="section soft">
  <div class="wrap split">
    <div>
      <span class="eyebrow">{icon('wand')} Retouching</span>
      <h2>We are the retouching experts</h2>
      <p class="lead" style="margin-top:18px">{e(text)}</p>
      <a class="btn btn-primary" href="/appointments">Book a session</a>
    </div>
    <div class="split-media"><img src="{IMG['retouch']}" alt="Before and after retouching" loading="lazy"><div class="ba"><span>Before</span><span>After</span></div></div>
  </div>
</section>
"""

def price_cards(cta="Book this package"):
    out = []
    for i, (tag, amt, sess, shots) in enumerate(PRICES):
        pk = PICKS[i]
        badge = {2: "Most Popular", 3: "Recommended"}.get(i, "")
        out.append(f'<div class="price-card{" feature" if i == 2 else ""}{" has-badge" if badge else ""}">{f'<span class="pc-badge">{badge}</span>' if badge else ""}<span class="tag">{tag}</span><div class="amount">{amt}</div>'
                   f'{bullets([sess, shots, f"You pick your favorite {pk}" if pk > 1 else "You pick your favorite 1", "Retouched, color graded &amp; emailed", "Digital files only"])}'
                   f'<a class="btn {"btn-white" if i == 2 else "btn-primary"}" href="/appointments">{cta}</a></div>')
    return '<div class="price-grid">' + "".join(out) + "</div>"

def how_it_works(soft=False):
    steps = [("calendar", "Book your package", "Choose 1, 3, 5 or 10 headshots and send the booking form, or call us."),
             ("image", "We shoot in different poses", "We take plenty of photos in different poses and expressions during your session."),
             ("check", "You pick your favorites", "Review your photos and select the ones you love — as many as your package includes."),
             ("wand", "Retouched, color graded & emailed", "We edit, retouch and color grade your picks, then email them to you within 24 hours.")]
    st = "".join(f'<div class="hiw-step"><span class="hiw-num">{i+1}</span><span class="ic">{icon(ic)}</span><h3>{t}</h3><p>{d}</p></div>' for i, (ic, t, d) in enumerate(steps))
    rows = "".join(f'<tr><td><b>{t}</b><small>{a}</small></td><td>{s}</td><td>{sh.replace(" in different poses", "")}</td><td><b>{PICKS[i]}</b></td></tr>' for i, (t, a, s, sh) in enumerate(PRICES))
    return f"""<section class="section{' soft' if soft else ''}" id="how-it-works">
  <div class="wrap">
    <div class="section-head head-split"><div><span class="eyebrow">{icon('timer')} How it works</span><h2>How a session works</h2></div>
    <p class="lead">Every package follows the same simple process — the only difference is how long we shoot and how many final headshots you choose.</p></div>
    <div class="hiw-steps">{st}</div>
    <div class="hiw-table"><table>
      <thead><tr><th>Package</th><th>Session length</th><th>Photos we take</th><th>Final headshots you choose</th></tr></thead>
      <tbody>{rows}</tbody></table></div>
    <div class="digital-note">{icon('image')}<p><b>Digital images only.</b> All headshots are delivered as digital files by email — we do not offer printing.</p></div>
  </div>
</section>
"""

def affordability(soft=False):
    rows = [("Price", "$250 median per session in New Jersey¹", "$50 for 1 · $100 for 3 · $150 for 5 · $250 for 10"),
            ("Retouched headshots", "3 or fewer in most packages¹", "1 to 10, you choose the package"),
            ("What $250 gets you", "About one typical NJ session¹", "10 retouched headshots from a 1-hour session"),
            ("Retouching & color grading", "Varies by photographer", "Included on every photo you pick"),
            ("Backgrounds", "Varies by photographer", "Unlimited"),
            ("Delivery", "Varies by photographer", "Emailed within 24 hours")]
    tr = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td class="us">{c}</td></tr>' for a, b, c in rows)
    return f"""<section class="section{' soft' if soft else ''}" id="compare">
  <div class="wrap">
    <div class="section-head head-split"><div><span class="eyebrow">{icon('check')} Affordability</span><h2>How our prices compare</h2></div>
    <p class="lead">A typical New Jersey headshot session costs about $250 and usually includes three or fewer images. At Macro Headshots, $250 gets you ten retouched headshots.</p></div>
    <div class="cmp-table"><table>
      <thead><tr><th></th><th>Typical headshot photographer</th><th class="us">Macro Headshots</th></tr></thead>
      <tbody>{tr}</tbody></table></div>
    <p class="cmp-note">¹ <a href="https://www.headshotpro.com/blog/how-much-does-a-headshot-cost" target="_blank" rel="noopener">HeadshotPro survey of 751 photographer websites</a> (data updated January 2025): New Jersey median session price $250; 66% of packages include 3 or fewer headshots. Nationally, Thumbtack estimates an average of about $304 per headshot session (<a href="https://magichour.ai/blog/how-much-does-a-headshot-cost" target="_blank" rel="noopener">as reported by Magic Hour</a>). Prices vary by photographer.</p>
  </div>
</section>
"""

def pricing_teaser():
    return f"""<section class="section">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Pricing</span><h2>Simple packages, no surprises</h2><p class="lead">Pick the session length that suits you. Every package includes professional retouching.</p></div>
    {price_cards()}
  </div>
</section>
"""

def testimonial(quote):
    return f"""<section class="section">
  <div class="wrap">
    <div class="quote-band">
      <div class="stars">★★★★★</div>
      <h2>“{e(quote)}”</h2>
      <p style="margin-top:14px;color:#e6e1ff">What our clients say about Macro Headshots</p>
      <div class="review-grid">{"".join(f'<figure class="review-card"><div class="r-stars" aria-label="5 out of 5 stars">★★★★★</div><blockquote>{e(t)}</blockquote><figcaption><b>{e(n)}</b><span>Google review</span></figcaption></figure>' for n, t in REVIEWS)}</div>
      <a class="btn btn-white" style="margin-top:26px" href="{MAPS_URL}" target="_blank" rel="noopener">See all reviews on Google</a>
    </div>
  </div>
</section>
"""

def instagram():
    return f"""<section class="section soft">
  <div class="wrap">
    <div class="section-head center"><span class="eyebrow">{IG_SVG.replace('<svg','<svg width="14" height="14"')} @macroheadshots</span><h2>Instagram feed</h2></div>
    <div class="insta" data-consent-embed="https://www.instagram.com/embed.js"><blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/macroheadshots/" data-instgrm-version="13" style="width:100%;max-width:100%"></blockquote>
      <div class="consent-placeholder"><p>The Instagram feed is loaded from Instagram, which may set cookies.</p><button type="button" class="btn btn-primary btn-sm" data-consent="all">Accept cookies &amp; show feed</button> <a class="btn btn-outline btn-sm" href="{IG_URL}" target="_blank" rel="noopener">Open Instagram</a></div></div>
  </div>
</section>
"""

FAQS = None
def faq(extra=()):
    items = []
    for q, a in list(extra) + FAQS:
        parts = [p.strip() for p in re.split(r"(?<=pick \d\.)\s+|(?<=pick 10\.)\s+|(?<=pick 1\.)\s+", a) if p.strip()]
        items.append(f'<details><summary>{e(q)}<span class="plus">+</span></summary><div class="ans">{"".join(f"<p>{e(p)}</p>" for p in parts)}</div></details>')
    items[0] = items[0].replace("<details>", "<details open>", 1)
    return f"""<section class="section" id="faq">
  <div class="wrap faq-grid">
    <div><span class="eyebrow">FAQ</span><h2>Frequently asked questions</h2><p class="lead" style="margin-top:16px">Still have a question? Call us at <a href="{PHONE_TEL}" style="color:var(--brand);font-weight:600">{PHONE}</a>.</p></div>
    <div class="faq">{''.join(items)}</div>
  </div>
</section>
"""

def directions():
    steps = [("/assets/directions-1.webp", "Step 1: drive to the end of the plaza",
              "Go straight along the front of the building, then take a left at the end of the building. There is parking there at the end of the plaza.",
              "Plaza at 195 US-46 in Totowa with an arrow showing the drive along the building and the left turn at the end"),
             ("/assets/directions-2.webp", "Step 2: park and use the office entrance",
              "Park at the end of the plaza. The Macro Headshots office entrance is at the corner of the building. We are on the second floor, Suite 9.",
              "Corner of the building at 195 US-46 with an arrow pointing to the Macro Headshots office entrance")]
    cards = "".join(f'<figure class="dir-card"><img src="{src}" alt="{alt}" width="1200" height="800" loading="lazy" decoding="async"><figcaption><b>{t}</b><span>{d}</span></figcaption></figure>' for src, t, d, alt in steps)
    return f"""<div class="dir-block" id="directions"><h3>Finding our entrance</h3><div class="dir-grid">{cards}</div></div>"""

def contact():
    mp = f'<img src="{MAP}" alt="Map showing Macro Headshots studio in Totowa, NJ" loading="lazy">' if MAP else ""
    return f"""<section class="section soft" id="contact">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Contact</span><h2>Visit the studio</h2></div>
    <div class="contact-grid">
      <div class="contact-card">
        <div class="contact-row"><span class="ic">{icon('phone')}</span><div><small>Call us</small><b><a href="{PHONE_TEL}">{PHONE}</a></b></div></div>
        <div class="contact-row"><span class="ic">{icon('pin')}</span><div><small>Studio address</small><b>{ADDRESS}</b></div></div>
        <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:6px"><a class="btn btn-primary" href="/appointments">Book an appointment</a><a class="btn btn-outline" href="{MAPS_URL}" target="_blank" rel="noopener">Get directions</a></div>
      </div>
      <a class="map-card" href="{MAPS_URL}" target="_blank" rel="noopener" aria-label="Open the studio in Google Maps">{mp}<span class="pin"><b>Macro Headshots</b><br>195 US-46, Totowa, NJ</span></a>
    </div>
    {directions()}
  </div>
</section>
"""

def areas(active=None, town_name=None):
    chips = "".join(f'<a href="/{s}/"{" class=\"active\"" if s == active else ""}>{n}</a>' for s, n in TOWNS)
    return f"""<section class="section" id="locations">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{icon('pin')} Locations</span><h2>{"Serving " + e(town_name) + " and all of North Jersey" if town_name else "Serving North Jersey and the New York Metro Area"}</h2><p class="lead">Our Totowa studio is a short drive from these communities.</p></div>
    <div class="areas">{chips}</div>
  </div>
</section>
"""

def local_section(slug, name):
    t = TOWN_INFO[slug.replace("headshots-in-", "")]
    paras = "".join(f"<p>{e(x)}</p>" for x in t["intro"])
    hl = "".join(f'<span class="chip">{icon("pin")} {e(x)}</span>' for x in t["highlights"])
    names = dict((s.replace("headshots-in-", ""), n) for s, n in TOWNS)
    nb = "".join(f'<a href="/headshots-in-{x}/">Headshots in {names[x]}</a>' for x in t["neighbors"] if x in names and x != slug.replace("headshots-in-", ""))
    return f"""<section class="section" id="local">
  <div class="wrap local-grid">
    <div class="local-text">
      <span class="eyebrow">{icon('pin')} {e(name)}, {t['county']}</span>
      <h2>Headshots for {e(name)} professionals</h2>
      <div class="local-copy">{paras}</div>
      <div class="chips">{hl}</div>
    </div>
    <aside class="local-side">
      <div class="contact-card">
        <h3>Getting to our studio from {e(name)}</h3>
        <p>{e(t['route'])}</p>
        <div class="contact-row"><span class="ic">{icon('pin')}</span><div><small>Studio address</small><b>{ADDRESS}</b></div></div>
        <a class="btn btn-primary btn-sm" href="{MAPS_URL}" target="_blank" rel="noopener">Get directions from {e(name)}</a>
      </div>
      <div class="contact-card nearby"><h3>Nearby areas we serve</h3><div class="areas">{nb}</div></div>
    </aside>
  </div>
</section>
"""

def cta():
    return f"""<section class="section" style="padding-top:0">
  <div class="wrap"><div class="cta-band">
    <div><h2>Ready for the best headshot you have ever had?</h2><p>Book online in a minute, or call us at {PHONE}.</p></div>
    <div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-primary" href="/appointments">Book Now</a><a class="btn btn-white" href="{PHONE_TEL}">Call {PHONE}</a></div>
  </div></div>
</section>
"""

# ---------- pages ----------
def find(page, kind, n=0):
    if page not in c: page = "/"
    found = [it for s in c[page]["sections"] if not s["mobile"] for it in s["items"] if it[0] == kind]
    return found[n] if len(found) > n else None

def first_sentences(text, n=2):
    s = re.split(r"(?<=[.!?])\s+", text)
    return " ".join(s[:n])

def fix(text):
    return (text.replace("Our studio is located As a professional", "As a professional")
                .replace("Proffesional", "Professional"))

from PIL import Image as _PIL
_dims = {}
def _add_dims(m):
    tag, src = m.group(0), m.group(1)
    if " width=" in tag:
        return tag
    if src not in _dims:
        try:
            _dims[src] = _PIL.open(OUT + src).size
        except Exception:
            _dims[src] = None
    d = _dims[src]
    return tag if not d else tag[:-1] + f' width="{d[0]}" height="{d[1]}">'

def write(path, body):
    body = re.sub(r'<img[^>]*?src="(/assets/[^"]+)"[^>]*>', _add_dims, body)
    os.makedirs(os.path.dirname(f"{OUT}/{path}") or OUT, exist_ok=True)
    open(f"{OUT}/{path}", "w").write(body)

FAQS = [
    ("What is the turnaround time?", "We deliver all retouched pictures within 24 hours."),
    ("How many backgrounds can I choose from?", "Unlimited. We shoot on studio backdrops and can change your background digitally to the color you want."),
    ("Are all photos retouched?", "Yes. Every headshot you choose is edited, retouched and color graded."),
    ("How long is a session and how many photos do you take?", "1 headshot ($50): a 5-minute session where we take about 5–10 photos in different poses and you pick 1. 3 headshots ($100): a 10–15 minute session with about 15–20 photos, and you pick 3. 5 headshots ($150): a 30-minute session with about 20–40 photos, and you pick 5. 10 headshots ($250): a 1-hour session with about 40–100 photos, and you pick 10."),
    ("How do I receive my photos? Do you print them?", "Your retouched, color-graded headshots are emailed to you as digital files. All images are digital only — we do not offer printing."),
]

def landing(page, place, active_town=None):
    intro = fix(find(page, "paragraph", 0)[1])
    retouch = fix(find(page, "paragraph", 1)[1])
    town = active_town is not None
    tinfo = TOWN_INFO[active_town.replace("headshots-in-", "")] if town else None
    lead = (tinfo["lead"]
            if town else "We use state-of-the-art equipment and techniques to capture stunning, unique headshots tailored to you — corporate, acting, residency and personal branding.")
    qh = [it[1] for sec in c[page if page in c else "/"]["sections"] for it in sec["items"] if it[0] == "heading" and it[1].strip().startswith('"')][0]
    quote = re.sub(r"\s+", " ", qh.strip().strip('"“” ')).strip()
    quote = re.sub(r"\bIn\b", "in", quote)
    quote = re.sub(r"\s+Period$", ". Period", quote)
    if not quote.endswith("."):
        quote += "."
    meta = dict(c[page if page in c else "/"])
    if town:
        tk = active_town.replace("headshots-in-", "")
        meta["title"] = (f"Headshot Studio in Totowa, NJ | Macro Headshots" if tk == "totowa"
                         else f"Headshots near {place}, NJ | Macro Headshots, Totowa")
        meta["desc"] = tinfo["desc"]
        li_q = (f"Where can I get LinkedIn headshots in Totowa, NJ?" if tk == "totowa"
                else f"Where can I get LinkedIn headshots near {place}, NJ?")
        li_a = (f"At our studio at {ADDRESS}. " if tk == "totowa" else f"{place} clients come to our studio at {ADDRESS}. ") + tinfo["route"] + " A LinkedIn headshot is $50 for a 5-minute session, retouched and emailed within 24 hours."
        tfaq = [(li_q, li_a)] + [(q.replace("877-622-4973", PHONE), a) for q, a in tinfo["faqs"]]
        crumb = [("Home", "/"), ("Locations", "/locations"), (("Headshots in Totowa" if tk == "totowa" else f"Headshots near {place}"), page)]
        svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": f"Professional headshots for {place}, NJ",
                  "serviceType": "Headshot photography", "provider": {"@id": SITE + "/#business"},
                  "areaServed": {"@type": "City", "name": f"{place}, NJ"}, "url": canon(page),
                  "description": tinfo["desc"]}
        h1 = ('Headshot studio in <span class="accent">Totowa</span>, NJ' if tk == "totowa"
              else f'Headshots near <span class="accent">{e(place)}</span>, NJ')
        lead2 = lead + ("" if tk == "totowa" else f" There is no studio in {place}: every session takes place at our Totowa studio.")
        return (head(meta["title"], meta["desc"], page, [faq_ld(tfaq), breadcrumb(crumb), svc_ld], preload="/assets/hero-clients.webp") + nav(None)
                + hero(place, lead2, True, h1).replace('<span class="eyebrow">', crumbs(crumb) + '<span class="eyebrow">', 1) + local_section(active_town, place)
                + services(None, place) + gallery() + pricing_teaser() + how_it_works(True)
                + testimonial(quote) + faq(tfaq) + contact() + areas(active_town, place) + cta() + footer())
    home_title = "Professional Headshots in Totowa, NJ | MacroHeadshots"
    home_desc = "Professional headshots in Totowa, NJ, serving Northern New Jersey and NYC. Corporate, LinkedIn and acting portraits. Packages from $50. Book today."
    home_lead = "Corporate, LinkedIn, acting, residency and personal branding headshots from our Totowa studio, retouched and emailed within 24 hours."
    return (head(home_title, home_desc, "/", [faq_ld()], preload="/assets/hero-clients.webp") + nav("/")
            + hero(place, home_lead, False, 'Professional Headshots in <span class="accent">Totowa, NJ</span>', home=True)
            + trust() + gallery() + testimonial(quote) + services(retouch, None) + residency(None) + branding(None)
            + strengths(intro) + pricing_teaser() + affordability(True) + how_it_works() + faq() + contact() + instagram() + areas(None, None) + cta() + footer())

write("index.html", landing("/", "New York Metro Area"))
for slug, name in TOWNS:
    write(f"{slug}.html", landing(f"/{slug}/", name, slug))

# pricing
perks = [("wand", "Professional Retouching"), ("sparkle", "5-Star Rated on Google"),
         ("clock", "Delivered Within 24 Hours"), ("layers", "Unlimited Backgrounds")]
perk_html = "".join(f'<div class="perk"><span class="perk-ic">{icon(i)}</span><b>{t}</b></div>' for i, t in perks)
m = c["/pricing"]
write("pricing.html", head(m["title"], m["desc"], "/pricing", [faq_ld(), breadcrumb([("Home", "/"), ("Pricing", "/pricing")])]) + nav("/pricing") + f"""
<section class="page-hero">{BLOBS}
  <div class="wrap">{crumbs([("Home", "/"), ("Pricing", "/pricing")])}<span class="eyebrow">Pricing</span><h1>Headshot packages for <span style="color:var(--brand)">every need</span></h1>
  <p class="lead">Straightforward pricing with professional retouching included in every package.</p>
  <div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" href="/appointments">Book Your Session</a><a class="btn btn-outline" href="{PHONE_TEL}">Call {PHONE}</a></div></div>
</section>
<section class="section soft"><div class="wrap">
  <div class="perks">{perk_html}</div>
  {price_cards()}
</div></section>
""" + affordability() + how_it_works(True) + faq() + contact() + cta() + footer())

# appointments
m = c["/appointments"]
mp = f'<img src="{MAP}" alt="Map of the studio" loading="lazy">' if MAP else ""
pk_rows = "".join(f'<li><span><b>{t}</b><small>{s}</small></span><em>{a}</em></li>' for t, a, s, _ in PRICES)
write("appointments.html", head(m["title"], m["desc"], "/appointments", [faq_ld(), breadcrumb([("Home", "/"), ("Appointments", "/appointments")])], preload="/assets/hero-clients.webp") + nav("/appointments") + f"""
<section class="hero appt-hero">{BLOBS}
  <div class="wrap hero-grid">
    <div>
      {crumbs([("Home", "/"), ("Appointments", "/appointments")])}
      <span class="eyebrow">{icon('calendar')} Book online</span>
      <h1>Make an <span class="accent">appointment</span></h1>
      <p class="lead">Choose a date and the headshot package you are interested in, and our team will get back to you. Prefer to talk? Call us at <a href="{PHONE_TEL}" style="color:var(--brand);font-weight:600">{PHONE}</a>.</p>
      <div class="hero-actions"><a class="btn btn-primary" href="#book">Fill in the form</a><a class="btn btn-outline" href="{PHONE_TEL}">Call {PHONE}</a></div>
      <div class="chips">
        <span class="chip">{icon('clock')} Retouched in 24 hours</span>
        <span class="chip">{icon('timer')} Sessions from 5 minutes</span>
        <span class="chip">{icon('pin')} Totowa, NJ studio</span>
      </div>
    </div>
    <div class="hero-visual"><img class="collage" src="/assets/hero-clients.webp" alt="Recent Macro Headshots clients" width="1200" height="940"></div>
  </div>
</section>
<section class="section soft" id="book">
  <div class="wrap">
    <div class="section-head head-split"><div><span class="eyebrow">Request a session</span><h2>Book your headshot session</h2></div><p class="lead">All fields are required. Pick the package you are interested in — you can always change it at the studio.</p></div>
    <div class="book-grid">
      <div class="form-card">
        <iframe src="https://api.leadconnectorhq.com/widget/form/{FORM_ID}" id="inline-{FORM_ID}" data-layout="{{'id':'INLINE'}}" data-trigger-type="alwaysShow" data-trigger-value="" data-activation-type="alwaysActivated" data-activation-value="" data-deactivation-type="neverDeactivate" data-deactivation-value="" data-form-name="Appointments" data-height="1150" data-layout-iframe-id="inline-{FORM_ID}" data-form-id="{FORM_ID}" title="Appointment request form"></iframe>
        <script src="https://link.msgsndr.com/js/form_embed.js"></script>
      </div>
      <aside class="side">
        <div class="contact-card">
          <h3>How it works</h3>
          <ol class="steps"><li>Send the form with your preferred date and package.</li><li>Our team gets back to you to set the time.</li><li>We shoot photos in different poses; you pick your favorites.</li><li>We retouch, color grade and email your digital headshots within 24 hours.</li></ol>
        </div>
        <div class="contact-card">
          <h3>Packages</h3>
          <ul class="pk">{pk_rows}</ul>
          <a class="btn btn-outline btn-sm" href="/pricing">Compare packages</a>
        </div>
        <div class="contact-card">
          <h3>Prefer to talk to us?</h3>
          <div class="contact-row"><span class="ic">{icon('phone')}</span><div><small>Call us</small><b><a href="{PHONE_TEL}">{PHONE}</a></b></div></div>
          <div class="contact-row"><span class="ic">{icon('pin')}</span><div><small>Studio location</small><b>195 US-46, Suite 9, Totowa NJ</b></div></div>
          <a class="map-card" style="min-height:200px" href="{MAPS_URL}" target="_blank" rel="noopener" aria-label="Open the studio in Google Maps">{mp}<span class="pin"><b>Get directions</b></span></a>
        </div>
      </aside>
    </div>
    {directions()}
  </div>
</section>
""" + gallery() + strengths(fix(find("/", "paragraph", 0)[1])) + faq() + cta() + footer())


exec(open(f"{HERE}/ext_pages.py").read())

# ---------- legal pages ----------
UPDATED = "November 9, 2026"
def legal_page(slug, title, desc, h1, body):
    write(f"{slug}.html", head(title, desc, f"/{slug}", [breadcrumb([("Home", "/"), (h1, f"/{slug}")])]) + nav(None) + f"""
<section class="page-hero">{BLOBS}<div class="wrap">{crumbs([("Home", "/"), (h1, f"/{slug}")])}<span class="eyebrow">Legal</span><h1>{h1}</h1><p class="lead">Last updated: {UPDATED}</p></div></section>
<section class="section soft" style="padding-top:56px"><div class="wrap"><article class="prose">{body}</article></div></section>
""" + footer())

legal_page("privacy-policy", "Privacy Policy | Macro Headshots", "How Macro Headshots collects, uses and protects your personal information when you visit our website or book a headshot session.", "Privacy Policy", f"""
<p>This Privacy Policy explains how Macro Headshots ("we", "us", "our"), a professional headshot studio at {ADDRESS}, collects, uses and protects personal information when you visit this website, contact us or book a session.</p>
<h2>Information we collect</h2>
<ul>
<li><b>Information you give us.</b> When you fill in our appointment form we collect your first and last name, phone number, email address, preferred session date, the package you are interested in and your message. If you call us, we may note your name and contact details to arrange your session.</li>
<li><b>Photographs.</b> If you book a session, we take and store the photographs from your session in order to retouch and deliver them to you.</li>
<li><b>Technical information.</b> Like most websites, our hosting provider automatically receives basic technical data such as your IP address, browser type and the pages you request, which is used to deliver and secure the site.</li>
<li><b>Cookies.</b> See our <a href="/cookie-policy">Cookie Policy</a> for details of cookies and similar technologies used on this site.</li>
</ul>
<h2>How we use your information</h2>
<ul>
<li>To respond to your enquiry and schedule, confirm or change your appointment.</li>
<li>To carry out your session, and to retouch and deliver your photographs.</li>
<li>To communicate with you about your booking, including reminders and follow-ups.</li>
<li>To keep our website secure and working properly.</li>
<li>To meet our legal, tax and accounting obligations.</li>
</ul>
<p>We do not sell your personal information.</p>
<h2>Who we share information with</h2>
<p>We share information only with service providers that help us run our business, and only as needed for the purposes above:</p>
<ul>
<li><b>HighLevel / LeadConnector</b>, which provides our appointment form and customer management system.</li>
<li><b>Vercel</b>, which hosts this website.</li>
<li><b>Google Fonts</b>, which serves the fonts used on this site.</li>
<li><b>Instagram (Meta)</b>, which loads only if you accept cookies.</li>
</ul>
<p>We may also disclose information if required by law or to protect our rights, property or safety.</p>
<h2>Photographs and your consent</h2>
<p>Your photographs belong in your hands. We will not use your photographs in our portfolio, website or social media without your permission. If you have given permission and later change your mind, contact us and we will stop using them in new materials.</p>
<h2>How long we keep information</h2>
<p>We keep booking information and session photographs only as long as needed to provide our services and to meet legal and accounting requirements, after which we delete or anonymize it.</p>
<h2>Security</h2>
<p>We use reasonable technical and organizational measures to protect your information, including encrypted (HTTPS) connections to this website. No method of transmission or storage is completely secure, but we work to protect your data.</p>
<h2>Your choices and rights</h2>
<p>You can ask us to access, correct or delete the personal information we hold about you, or to stop sending you messages. Depending on where you live, you may have additional rights under applicable privacy laws. To make a request, call us at <a href="{PHONE_TEL}">{PHONE}</a> or write to us at the address below. We may need to verify your identity before acting on a request.</p>
<h2>Children</h2>
<p>This website is not directed to children under 13, and we do not knowingly collect personal information from them online. Sessions for minors are booked by a parent or guardian.</p>
<h2>Changes to this policy</h2>
<p>We may update this policy from time to time. The "Last updated" date at the top shows when it last changed.</p>
<h2>Contact us</h2>
<p>Macro Headshots<br>{ADDRESS}<br>Phone: <a href="{PHONE_TEL}">{PHONE}</a></p>
""")

legal_page("cookie-policy", "Cookie Policy | Macro Headshots", "Which cookies and similar technologies the Macro Headshots website uses, and how to manage your cookie choices.", "Cookie Policy", f"""
<p>This Cookie Policy explains how the Macro Headshots website uses cookies and similar technologies (such as local storage), and how you can control them. For more about how we handle personal information, see our <a href="/privacy-policy">Privacy Policy</a>.</p>
<h2>What are cookies?</h2>
<p>Cookies are small text files that a website stores on your device. Similar technologies, like local storage, work in a comparable way. They can be set by the website you visit (first-party) or by other services that site uses (third-party).</p>
<h2>Cookies we use</h2>
<div class="table-wrap"><table>
<thead><tr><th>Category</th><th>Provider</th><th>Purpose</th><th>When it is used</th></tr></thead>
<tbody>
<tr><td>Strictly necessary</td><td>Macro Headshots</td><td>Remembers your cookie choice (stored in your browser's local storage as <code>mh-consent</code>).</td><td>Always</td></tr>
<tr><td>Strictly necessary</td><td>HighLevel / LeadConnector</td><td>Runs the appointment form so you can send a booking request.</td><td>When the booking form loads</td></tr>
<tr><td>Third-party content</td><td>Instagram (Meta)</td><td>Displays our Instagram feed.</td><td>Only after you click "Accept all"</td></tr>
</tbody></table></div>
<p>We do not use advertising cookies, and this site does not run analytics or tracking tools.</p>
<h2>Managing your choices</h2>
<p>When you first visit, you can choose <b>Accept all</b> or <b>Necessary only</b>. You can change your choice at any time:</p>
<p><button type="button" class="btn btn-primary btn-sm" data-cookie-settings>Open cookie settings</button></p>
<p>You can also block or delete cookies in your browser settings. Blocking strictly necessary cookies may stop parts of the site, such as the booking form, from working.</p>
<h2>Third-party policies</h2>
<p>Third-party providers set and control their own cookies. Please see their privacy policies for details: <a href="https://www.gohighlevel.com/privacy-policy" target="_blank" rel="noopener">HighLevel</a> and <a href="https://privacycenter.instagram.com/policy" target="_blank" rel="noopener">Instagram</a>.</p>
<h2>Contact us</h2>
<p>Questions about this policy? Call us at <a href="{PHONE_TEL}">{PHONE}</a>.</p>
""")

# ---------- 404 ----------
write("404.html", head("Page not found | Macro Headshots", "The page you are looking for could not be found.", "/404", robots="noindex,follow") + nav(None) + f"""
<section class="page-hero" style="padding-bottom:120px">{BLOBS}<div class="wrap"><span class="eyebrow">404</span><h1>We could not find that page</h1>
<p class="lead">The link may be old or mistyped. Here are some good places to start.</p>
<div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" href="/">Go to home</a><a class="btn btn-outline" href="/appointments">Book a session</a><a class="btn btn-outline" href="/pricing">See pricing</a></div></div></section>
""" + footer())

# ---------- icons, manifest, OG image ----------
ICONS = os.path.join(BRAND, "icons")
shutil.copy(f"{ICONS}/favicon.ico", f"{OUT}/favicon.ico")
shutil.copy(f"{ICONS}/apple-touch-icon.png", f"{OUT}/apple-touch-icon.png")
for n in ("favicon-32.png", "favicon-16.png", "icon-192.png", "icon-512.png"):
    shutil.copy(f"{ICONS}/{n}", f"{OUT}/assets/{n}")
json.dump({"name": "Macro Headshots", "short_name": "Macro Headshots", "start_url": "/", "display": "browser",
           "background_color": "#ffffff", "theme_color": "#735ae5",
           "icons": [{"src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png"},
                     {"src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png"}]},
          open(f"{OUT}/site.webmanifest", "w"), indent=2)
og = _PIL.new("RGB", (1200, 630), (246, 243, 255))
col = _PIL.open(f"{BRAND}/hero-clients.webp").convert("RGBA"); col.thumbnail((760, 600))
og.paste(col, (1200 - col.width - 20, (630 - col.height) // 2), col)
logo = _PIL.open(f"{BRAND}/logo-new.png").convert("RGBA"); logo.thumbnail((420, 170))
og.paste(logo, (60, 235), logo)
og.save(f"{OUT}/assets/og-image.jpg", quality=86)

# ---------- sitemap & robots ----------
paths = ["/", "/services"] + [f"/{s}/" for s, _ in SERVICES] + ["/pricing", "/appointments", "/locations"] + [f"/{s}/" for s, _ in TOWNS] + ["/portfolio", "/guides"] + [f"/guides/{g['slug']}" for g in GUIDES] + ["/privacy-policy", "/cookie-policy"]
prio = {"/": "1.0", "/services": "0.9", "/locations": "0.8", "/portfolio": "0.6", "/guides": "0.6", "/appointments": "0.9", "/pricing": "0.9", "/privacy-policy": "0.2", "/cookie-policy": "0.2"}
urls = "".join(f"<url><loc>{canon(x)}</loc><lastmod>2026-11-09</lastmod><priority>{prio.get(x, '0.7')}</priority></url>" for x in paths)
open(f"{OUT}/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

# ---------- vercel config with security headers ----------
CSP = "; ".join([
    "default-src 'self'",
    "script-src 'self' https://www.instagram.com https://link.msgsndr.com",
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
    "font-src 'self' data: https://fonts.gstatic.com",
    "img-src 'self' data: blob: https:",
    "connect-src 'self' https://www.instagram.com",
    "frame-src https://api.leadconnectorhq.com https://*.leadconnectorhq.com https://link.msgsndr.com https://www.instagram.com",
    "media-src 'self' https:",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "frame-ancestors 'none'",
    "upgrade-insecure-requests",
])
SEC = [
    {"key": "Content-Security-Policy", "value": CSP},
    {"key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains; preload"},
    {"key": "X-Content-Type-Options", "value": "nosniff"},
    {"key": "X-Frame-Options", "value": "DENY"},
    {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
    {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()"},
    {"key": "Cross-Origin-Opener-Policy", "value": "same-origin"},
    {"key": "X-DNS-Prefetch-Control", "value": "on"},
]
json.dump({"cleanUrls": True,
           "headers": [{"source": "/(.*)", "headers": SEC},
                       {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=86400, stale-while-revalidate=604800"}]},
                       {"source": "/(css|js)/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]}],
           "redirects": [{"source": "/home", "destination": "/", "permanent": True}, {"source": "/gallery", "destination": "/portfolio", "permanent": True}],
           "rewrites": [{"source": "/headshots-in-:town/", "destination": "/headshots-in-:town"}] + [{"source": f"/{s}/", "destination": f"/{s}"} for s, _ in SERVICES]},
          open(f"{OUT}/vercel.json", "w"), indent=2)
print("pages:", 3 + len(TOWNS), "assets:", len(os.listdir(f"{OUT}/assets")))
