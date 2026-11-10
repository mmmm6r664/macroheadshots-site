# Executed inside generate.py (exec) so it can use the shared helpers: head, nav, footer, write, icon, e, etc.
# Builds: 8 service landing pages, /services hub, /locations hub, /portfolio, /guides hub, guide articles.
from guides import GUIDES

GAL = {x[0][:-5]: x for x in GALLERY}  # "headshot-05a" -> manifest row
def gimg(key, alt, cls=""):
    n, w, h, _ = GAL[key]
    return f'<img{f" class={chr(34)}{cls}{chr(34)}" if cls else ""} src="/assets/gallery/{n}" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async">'

TOWN_NAMES = dict((s.replace("headshots-in-", ""), n) for s, n in TOWNS)
AREA = [{"@type": "City", "name": f"{n}, NJ"} for _, n in TOWNS]
PKG_OFFERS = [{"@type": "Offer", "name": t, "price": a.strip("$"), "priceCurrency": "USD",
               "description": f"{s}. {sh}. Retouched, color graded and emailed within 24 hours.", "url": SITE + "/pricing"}
              for t, a, s, sh in PRICES]

SERVICE_INFO = {
 "corporate-headshots": dict(
    kw="Corporate headshots NJ", title="Corporate Headshots NJ | Macro Headshots, Totowa",
    desc="Corporate headshots in NJ from $50: polished business portraits for LinkedIn, company websites and bios. Totowa studio, retouched within 24 hours.",
    h1="Corporate headshots in New Jersey", stype="Corporate headshot photography",
    lead="Polished, confident business portraits for LinkedIn, company websites, staff directories and bios, photographed at our Totowa studio and retouched within 24 hours.",
    photos=["headshot-20b", "headshot-05a", "headshot-12a", "headshot-32a", "headshot-30a", "headshot-23a"],
    who=["Professionals updating LinkedIn or a company bio", "New hires and recently promoted staff", "Consultants, lawyers, accountants and advisors", "Job seekers preparing for interviews"],
    inc=["Coaching on posture and expression", "Unlimited backgrounds: studio backdrops or digital changes", "Editing, retouching and color grading on every chosen image", "Digital files emailed within 24 hours"],
    guides=["what-to-wear-corporate-headshot", "headshot-cost-new-jersey", "retouched-headshots-24-hours"],
    faqs=[("How long does a corporate headshot session take?", "From 5 minutes for one headshot up to 1 hour for ten, depending on the package you choose."),
          ("Can my headshot match my colleagues' photos?", "Yes. Tell us the background and framing your company uses and we will match it.")]),
 "linkedin-headshots": dict(
    kw="LinkedIn headshots NJ", title="LinkedIn Headshots NJ | $50, Ready in 24 Hours",
    desc="LinkedIn headshots in NJ: a 5-minute session for $50, professionally retouched and emailed within 24 hours. Studio on US-46 in Totowa.",
    h1="LinkedIn headshots in New Jersey", stype="LinkedIn profile photo photography",
    lead="A great LinkedIn photo in about five minutes: professional lighting, a clean background and natural retouching, emailed to you within 24 hours for $50.",
    photos=["headshot-29b", "headshot-15a", "headshot-09a", "headshot-33a", "headshot-18a", "headshot-04a"],
    who=["Job seekers and career changers", "Sales and business development professionals", "Recent graduates and students", "Anyone whose current photo is a cropped selfie"],
    inc=["Framing that reads clearly at thumbnail size", "Clean background in a color that suits you", "Retouching that keeps you looking like you", "A square crop ready for LinkedIn"],
    guides=["are-linkedin-headshots-worth-it", "what-to-wear-corporate-headshot", "headshot-cost-new-jersey"],
    faqs=[("How much is a LinkedIn headshot?", "Our single-headshot package is $50 for a 5-minute session, retouched and emailed within 24 hours."),
          ("What size photo does LinkedIn need?", "We deliver a high-resolution file that you can upload directly; LinkedIn crops it to a circle, so we frame your face in the center.")]),
 "acting-headshots": dict(
    kw="Acting headshots NJ", title="Acting Headshots NJ | Macro Headshots Studio",
    desc="Acting headshots in NJ that look like you: varied expressions, multiple looks and light, natural retouching. Totowa studio near NYC.",
    h1="Acting headshots in New Jersey", stype="Actor headshot photography",
    lead="Headshots that show casting directors exactly who will walk into the room, with varied expressions, multiple looks and light, natural retouching.",
    photos=["headshot-26b", "headshot-13a", "headshot-27a", "headshot-06a", "headshot-14c", "headshot-26c"],
    who=["Actors building or refreshing their book", "Models and performers", "Students applying to drama programs", "Voice actors and hosts who need a face for their profile"],
    inc=["Time for several looks in 30- or 60-minute sessions", "Direction for range: commercial and theatrical expressions", "Light retouching that stays true to life", "Digital files ready for casting sites"],
    guides=["acting-vs-corporate-headshots", "headshot-cost-new-jersey"],
    faqs=[("How many looks can I do?", "A 30-minute session usually allows two or three looks; a 1-hour session allows more."),
          ("Will my headshots be heavily retouched?", "No. Acting headshots get light retouching so you look exactly like you do in person.")]),
 "residency-headshots": dict(
    kw="Medical residency headshots NJ", title="Residency Headshots NJ | ERAS Photos in 24 Hours",
    desc="Medical residency (ERAS) headshots in NJ: business-professional portraits plus an ERAS-ready file (JPG under 150 KB, face centered), retouched in 24 hours.",
    h1="Medical residency headshots (ERAS) in New Jersey", stype="Medical residency application photography",
    lead="Business-professional portraits for your residency application, with an ERAS-ready version and your full-resolution files emailed within 24 hours.",
    photos=["headshot-22b", "headshot-22a", "headshot-25a", "headshot-22c", "headshot-25b", "headshot-31a"],
    who=["Medical students applying through ERAS", "International medical graduates", "Fellowship applicants", "Residents updating hospital directory photos"],
    inc=["Head-and-shoulders framing on a plain background", "An ERAS file that meets AAMC rules: JPG, 150 KB max, face centered (sized 375 x 525 px)", "Full-resolution retouched images for other uses", "Delivery within 24 hours for tight deadlines"],
    guides=["medical-residency-headshots", "what-to-wear-corporate-headshot", "retouched-headshots-24-hours"],
    faqs=[("What are the ERAS photo requirements?", "AAMC requires a JPG/JPEG or PNG file of 150 KB or less with your face centered. We deliver it at 375 x 525 pixels (2.5 x 3.5 inches at 150 dpi), the passport-size portrait applicants commonly use."),
          ("Can I also get a white-coat photo?", "Yes. Bring your white coat for a second look; follow your program's guidance on which photo to submit.")]),
 "professional-headshots": dict(
    kw="Professional headshots NJ", title="Professional Headshots NJ | From $50, Totowa Studio",
    desc="Professional headshots in NJ from $50: corporate, LinkedIn, acting and personal branding portraits, retouched and emailed within 24 hours.",
    h1="Professional headshots in New Jersey", stype="Professional headshot photography",
    lead="Whatever you need a headshot for, we photograph you at our Totowa studio, help you look your best, and email retouched images within 24 hours.",
    photos=["headshot-01a", "headshot-07a", "headshot-24a", "headshot-28a", "headshot-17a", "headshot-03b"],
    who=["Business and corporate professionals", "Actors and performers", "Medical residency applicants", "Realtors, consultants, speakers and creators"],
    inc=["Sessions from 5 minutes to 1 hour", "Unlimited backgrounds", "Editing, retouching and color grading", "Digital delivery by email within 24 hours"],
    guides=["headshot-cost-new-jersey", "what-to-wear-corporate-headshot", "are-linkedin-headshots-worth-it"],
    faqs=[("Where is your studio?", "195 US-46, Suite 9, Totowa, NJ 07512, with easy access from I-80, Route 23 and the Garden State Parkway."),
          ("Do you offer prints?", "No. All images are delivered as digital files by email.")]),
 "executive-headshots": dict(
    kw="Executive headshots NJ", title="Executive Headshots NJ | Macro Headshots, Totowa",
    desc="Executive headshots in NJ for leadership pages, board bios, press and speaking: polished portraits with careful retouching, ready in 24 hours.",
    h1="Executive headshots in New Jersey", stype="Executive portrait photography",
    lead="Authoritative, approachable portraits for leadership pages, board bios, press releases and speaking engagements, with careful retouching and fast delivery.",
    photos=["headshot-20a", "headshot-24b", "headshot-30b", "headshot-01a", "headshot-10a", "headshot-12c"],
    who=["CEOs, founders and leadership teams", "Board members and partners", "Speakers and media spokespeople", "Executives announcing a new role"],
    inc=["Studio or office-style backgrounds", "Multiple looks in longer sessions", "Detailed, natural retouching", "Files suited to web, press and print use"],
    guides=["what-to-wear-corporate-headshot", "on-location-company-headshots", "headshot-cost-new-jersey"],
    faqs=[("Can you photograph our executives at our office?", "Yes, for groups of 10 or more within 30 miles of our Totowa studio we bring our studio equipment to you. Smaller groups visit the studio."),
          ("How quickly can we get images for a press release?", "Retouched images are emailed within 24 hours of the session.")]),
 "team-headshots": dict(
    kw="Company team headshots NJ", title="Team Headshots NJ | On-Location Company Photos",
    desc="Company team headshots in NJ: we photograph your whole team on location or at our Totowa studio, with consistent results and 24-hour delivery.",
    h1="Company team headshots in New Jersey", stype="Corporate team headshot photography",
    lead="For teams of 10 or more within 30 miles of Totowa, we bring our studio equipment to your office. Smaller teams visit our studio. Retouched within 24 hours.",
    photos=["headshot-34a", "headshot-01b", "headshot-10b", "headshot-30c", "headshot-10a", "headshot-20c"],
    who=["Companies refreshing their website and directory", "Law firms, medical practices and agencies", "Real estate brokerages", "Teams onboarding new staff"],
    inc=["Matching lighting, framing and background for everyone", "On-location setup for 10+ employees within 30 miles", "Each person picks their favorite image", "Retouched files within 24 hours"],
    guides=["on-location-company-headshots", "what-to-wear-corporate-headshot"],
    faqs=[("How much do team headshots cost?", "It depends on team size, location and images per person. Call 877-622-4973 for a quote."),
          ("Do you come to our office?", "Yes, if you have at least 10 employees and are within 30 miles of our Totowa studio. Smaller teams are welcome at the studio."),
          ("How long does each person take?", "Usually just a few minutes per person, so the session fits around meetings.")],
    no_price=True),
 "headshot-retouching": dict(
    kw="Headshot retouching", title="Headshot Retouching | Natural Results in 24 Hours",
    desc="Professional headshot retouching: blemish removal, skin tone, color grading and background changes, natural results delivered within 24 hours.",
    h1="Professional headshot retouching", stype="Photo retouching",
    lead="Our retouching team removes blemishes, evens skin tones, color grades and changes backgrounds, keeping you natural and recognizable.",
    photos=["headshot-03a", "headshot-21a", "headshot-27b", "headshot-08b", "headshot-14a", "headshot-16a"],
    who=["Every Macro Headshots client (included in every package)", "Professionals who want a natural, polished look", "Actors who need light, true-to-life edits", "Businesses that need a consistent background across a team"],
    inc=["Blemish and stray-hair cleanup", "Skin tone and color correction", "Color grading for a consistent look", "Digital background changes"],
    guides=["retouched-headshots-24-hours", "acting-vs-corporate-headshots"],
    faqs=[("Is retouching included?", "Yes. Every headshot you choose is edited, retouched and color graded at no extra cost."),
          ("Can you change my background?", "Yes. With unlimited backgrounds, we can shoot on a studio backdrop or change it digitally.")]),
}
GUIDE_BY = {g["slug"]: g for g in GUIDES}

def faq_block(items, title="Frequently asked questions"):
    det = "".join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}<span class="plus">+</span></summary><div class="ans"><p>{e(a)}</p></div></details>' for i, (q, a) in enumerate(items))
    return f'<section class="section" id="faq"><div class="wrap faq-grid"><div><span class="eyebrow">FAQ</span><h2>{title}</h2><p class="lead" style="margin-top:16px">More answers in our <a href="/guides" style="color:var(--brand);font-weight:600">headshot guides</a>.</p></div><div class="faq">{det}</div></div></section>'

def faq_ld_only(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def guide_cards(slugs, title="Helpful guides"):
    cards = "".join(f'<a class="guide-card" href="/guides/{s}"><span class="eyebrow" style="margin-bottom:10px">Guide</span><h3>{e(GUIDE_BY[s]["q"])}</h3><p>{e(GUIDE_BY[s]["short"])}</p><span class="more">Read the guide →</span></a>' for s in slugs)
    return f'<section class="section soft"><div class="wrap"><div class="section-head"><h2>{title}</h2></div><div class="guide-grid">{cards}</div></div></section>'

def service_links(exclude=None):
    chips = "".join(f'<a href="/{s}/">{n}</a>' for s, n in SERVICES if s != exclude)
    return f'<section class="section" style="padding-top:0"><div class="wrap"><div class="section-head"><h2>Other headshot services</h2></div><div class="areas">{chips}<a href="/locations">Locations we serve</a></div></div></section>'

# ---------- service landing pages ----------
for slug, name in SERVICES:
    S = SERVICE_INFO[slug]
    path = f"/{slug}/"
    hero_imgs = "".join(gimg(k, f"{name} by Macro Headshots", "tall" if i == 0 else "") for i, k in enumerate(S["photos"][:3]))
    more = "".join(f'<figure>{gimg(k, f"{name} example by Macro Headshots")}</figure>' for k in S["photos"][3:])
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "@id": SITE + path + "#service", "name": name,
              "serviceType": S["stype"], "description": S["desc"], "url": SITE + path,
              "provider": {"@id": SITE + "/#business"}, "areaServed": AREA,
              "image": SITE + "/assets/gallery/" + GAL[S["photos"][0]][0]}
    if not S.get("no_price"):
        svc_ld["offers"] = PKG_OFFERS
    crumb = [("Home", "/"), ("Services", "/services"), (name, path)]
    pricing_block = (pricing_teaser() if not S.get("no_price") else
        f'<section class="section"><div class="wrap"><div class="cta-band"><div><h2>Get a quote for your team</h2><p>Tell us your team size and location and we will plan the session.</p></div><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-primary" href="{PHONE_TEL}">Call {PHONE}</a><a class="btn btn-white" href="/appointments">Send a request</a></div></div></div></section>')
    extra = residency() if slug == "residency-headshots" else ""
    body = f"""
<section class="hero svc-hero">{BLOBS}
  <div class="wrap hero-grid">
    <div>
      {crumbs(crumb)}
      <span class="eyebrow">{icon('pin')} Totowa, NJ studio · serving North Jersey</span>
      <h1>{e(S['h1'])}</h1>
      <p class="lead">{e(S['lead'])}</p>
      <div class="hero-actions"><a class="btn btn-primary" href="/appointments">Book your session</a><a class="btn btn-outline" href="{'/pricing' if not S.get('no_price') else PHONE_TEL}">{'See pricing' if not S.get('no_price') else 'Call for a quote'}</a></div>
      <div class="chips"><span class="chip">{icon('clock')} Retouched in 24 hours</span><span class="chip">{icon('layers')} Unlimited backgrounds</span><span class="chip">{icon('sparkle')} Every photo retouched</span></div>
    </div>
    <div class="hero-visual"><div class="hero-photos">{hero_imgs}</div></div>
  </div>
</section>
<section class="section soft"><div class="wrap two-col">
  <div class="info-card"><h2>Who it's for</h2>{bullets(S['who'])}</div>
  <div class="info-card"><h2>What's included</h2>{bullets(S['inc'])}</div>
</div></section>
<section class="section"><div class="wrap"><div class="section-head"><h2>Recent {name.lower()}</h2></div><div class="svc-gallery">{more}</div>
<p style="margin-top:18px"><a href="/portfolio" style="color:var(--brand);font-weight:600">See the full portfolio →</a></p></div></section>
{extra}
{pricing_block}
{how_it_works(True) if not S.get('no_price') else ''}
{faq_block(S['faqs'])}
{guide_cards(S['guides'])}
{service_links(slug)}
"""
    write(f"{slug}.html", head(S["title"], S["desc"], path, [svc_ld, faq_ld_only(S["faqs"]), breadcrumb(crumb)],
                               preload="/assets/gallery/" + GAL[S["photos"][0]][0]) + nav(path) + body + cta() + footer())

# ---------- /services hub ----------
cards = "".join(f'<a class="svc-card" href="/{s}/">{gimg(SERVICE_INFO[s]["photos"][0], n + " by Macro Headshots")}<div class="bt-body"><div class="bt-head"><h3>{n}</h3><span class="arrow-btn">{icon("arrow")}</span></div><p>{e(SERVICE_INFO[s]["lead"])}</p></div></a>' for s, n in SERVICES)
hub_ld = {"@context": "https://schema.org", "@type": "ItemList", "name": "Macro Headshots services",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/{s}/", "name": n} for i, (s, n) in enumerate(SERVICES)]}
write("services.html", head("Headshot Services in NJ | Macro Headshots, Totowa", "Corporate, LinkedIn, acting, residency, executive and team headshots, plus retouching, from our Totowa, NJ studio. Retouched within 24 hours.", "/services",
      [hub_ld, breadcrumb([("Home", "/"), ("Services", "/services")])]) + nav("/services") + f"""
<section class="page-hero">{BLOBS}<div class="wrap">{crumbs([("Home", "/"), ("Services", "/services")])}<span class="eyebrow">Services</span><h1>Headshot services in New Jersey</h1>
<p class="lead">Choose the session that fits what you need the photo for. Every headshot is retouched and emailed within 24 hours.</p></div></section>
<section class="section soft" style="padding-top:48px"><div class="wrap"><div class="section-head"><h2>Choose your headshot service</h2></div><div class="svc-grid">{cards}</div></div></section>
""" + branding() + pricing_teaser() + cta() + footer())

# ---------- /locations hub ----------
tcards = "".join(f'<a class="town-card" href="/headshots-in-{k}/"><h3>{e(TOWN_NAMES[k])}</h3><small>{e(TOWN_INFO[k]["county"])}</small><p>{e(TOWN_INFO[k]["route"])}</p><span class="more">Directions &amp; details →</span></a>' for k in sorted(TOWN_NAMES) if k != "totowa")
mp = f'<img src="{MAP}" alt="Map of the Macro Headshots studio in Totowa, NJ" loading="lazy">' if MAP else ""
loc_crumb = [("Home", "/"), ("Locations", "/locations")]
write("locations.html", head("Locations | Macro Headshots Studio in Totowa, NJ", "Our headshot studio is at 195 US-46, Suite 9, Totowa, NJ, serving Wayne, Paterson, Clifton, Little Falls and North Jersey. Directions and service areas.", "/locations",
      [breadcrumb(loc_crumb)]) + nav("/locations") + f"""
<section class="page-hero">{BLOBS}<div class="wrap">{crumbs(loc_crumb)}<span class="eyebrow">{icon('pin')} Locations</span><h1>Our Totowa studio and the areas we serve</h1>
<p class="lead">One studio on US-46 in Totowa, a short drive from across Passaic County and North Jersey.</p></div></section>
<section class="section soft" id="studio" style="padding-top:48px"><div class="wrap contact-grid">
  <div class="contact-card">
    <span class="eyebrow">Totowa Studio</span>
    <h2>Macro Headshots, Totowa</h2>
    <div class="contact-row"><span class="ic">{icon('pin')}</span><div><small>Address</small><b>{ADDRESS}</b></div></div>
    <div class="contact-row"><span class="ic">{icon('phone')}</span><div><small>Phone</small><b><a href="{PHONE_TEL}">{PHONE}</a></b></div></div>
    <p>On the US-46 corridor with easy access from I-80, Route 23 and the Garden State Parkway.</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-primary" href="/appointments">Book a session</a><a class="btn btn-outline" href="{MAPS_URL}" target="_blank" rel="noopener">Get directions</a><a class="btn btn-outline" href="/headshots-in-totowa/">Headshots in Totowa</a></div>
  </div>
  <a class="map-card" href="{MAPS_URL}" target="_blank" rel="noopener" aria-label="Open the studio in Google Maps">{mp}<span class="pin"><b>Macro Headshots</b><br>195 US-46, Totowa, NJ</span></a>
</div><div class="wrap">{directions()}</div></section>
<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">Nearby service areas</span><h2>Headshots near you</h2><p class="lead">We have one studio, in Totowa. Clients from these towns come to us; pick yours for directions and local details. Teams of 10 or more within 30 miles can also book an <a href="/team-headshots/" style="color:var(--brand);font-weight:600">on-location session</a>.</p></div>
<div class="town-grid">{tcards}</div></div></section>
""" + cta() + footer())

# ---------- /portfolio ----------
cats = [("all", "All"), ("studio", "Studio"), ("location", "On location"), ("medical", "Medical")]
chips = "".join(f'<button type="button" class="filter{" active" if k == "all" else ""}" data-filter="{k}">{t}</button>' for k, t in cats)
alts = {"studio": "Studio headshot", "location": "On-location headshot", "medical": "Medical professional headshot"}
ORDERED = sorted(GALLERY, key=lambda x: (x[0][-6], x[0]))
items = "".join(f'<figure class="g-item" data-cat="{c}"><img src="/assets/gallery/{n}" alt="{alts[c]} by Macro Headshots" width="{w}" height="{h}" loading="lazy" decoding="async"></figure>' for n, w, h, c in ORDERED)
pf_crumb = [("Home", "/"), ("Portfolio & Reviews", "/portfolio")]
pf_ld = {"@context": "https://schema.org", "@type": "ImageGallery", "name": "Macro Headshots portfolio", "url": SITE + "/portfolio",
         "image": [SITE + f"/assets/gallery/{x[0]}" for x in ORDERED[:20]]}
write("portfolio.html", head("Headshot Portfolio & Reviews | Macro Headshots, NJ", "Real client headshots from Macro Headshots in Totowa, NJ: corporate, LinkedIn, executive, on-location and medical portraits, plus Google reviews.", "/portfolio",
      [pf_ld, breadcrumb(pf_crumb)]) + nav("/portfolio") + f"""
<section class="page-hero">{BLOBS}<div class="wrap">{crumbs(pf_crumb)}<span class="eyebrow">{icon('image')} Portfolio</span><h1>Headshot portfolio and reviews</h1>
<p class="lead">Recent sessions from our Totowa studio and on location, and what clients say about us.</p></div></section>
<section class="section soft" style="padding-top:48px"><div class="wrap">
  <div class="masonry" id="gallery-grid">{items}</div>
</div></section>
<div class="lightbox" id="lightbox" hidden role="dialog" aria-modal="true" aria-label="Photo viewer">
  <button type="button" class="lb-close" aria-label="Close">×</button><button type="button" class="lb-prev" aria-label="Previous photo">‹</button><img alt=""><button type="button" class="lb-next" aria-label="Next photo">›</button>
</div>
""" + testimonial("The best headshots in New York Metro Area. Period.") + instagram() + cta() + footer())

# ---------- /guides hub + articles ----------
g_crumb = [("Home", "/"), ("Guides & FAQs", "/guides")]
gcards = "".join(f'<a class="guide-card" href="/guides/{g["slug"]}"><h3>{e(g["q"])}</h3><p>{e(g["short"])}</p><span class="more">Read the guide →</span></a>' for g in GUIDES)
write("guides.html", head("Headshot Guides & FAQs | Macro Headshots, NJ", "Answers to common headshot questions: costs in NJ, what to wear, LinkedIn photos, acting vs corporate, ERAS residency photos and team sessions.", "/guides",
      [faq_ld(), breadcrumb(g_crumb)]) + nav("/guides") + f"""
<section class="page-hero">{BLOBS}<div class="wrap">{crumbs(g_crumb)}<span class="eyebrow">Guides &amp; FAQs</span><h1>Headshot guides and answers</h1>
<p class="lead">Straight answers to the questions we hear most, from pricing to what to wear.</p></div></section>
<section class="section soft" style="padding-top:48px"><div class="wrap"><div class="section-head"><h2>All headshot guides</h2></div><div class="guide-grid">{gcards}</div></div></section>
""" + faq() + cta() + footer())

SVC_FOR_GUIDE = {}
for s, info in SERVICE_INFO.items():
    for gs in info["guides"]:
        SVC_FOR_GUIDE.setdefault(gs, []).append(s)
SVC_NAME = dict(SERVICES)
os.makedirs(f"{OUT}/guides", exist_ok=True)
for g in GUIDES:
    path = f"/guides/{g['slug']}"
    crumb = g_crumb + [(g["q"], path)]
    img_n = GAL[g["img"]][0]
    art = {"@context": "https://schema.org", "@type": "Article", "headline": g["q"], "description": g["desc"],
           "image": SITE + "/assets/gallery/" + img_n, "datePublished": "2026-11-09", "dateModified": "2026-11-09",
           "author": {"@type": "Organization", "name": "Macro Headshots", "url": SITE + "/"},
           "publisher": {"@id": SITE + "/#business"}, "mainEntityOfPage": SITE + path}
    rel_svcs = "".join(f'<a href="/{s}/">{SVC_NAME[s]}</a>' for s in SVC_FOR_GUIDE.get(g["slug"], []))
    others = [x["slug"] for x in GUIDES if x["slug"] != g["slug"]][:3]
    faqs_html = "".join(f'<details><summary>{e(q)}<span class="plus">+</span></summary><div class="ans"><p>{e(a)}</p></div></details>' for q, a in g["faqs"])
    write(f"guides/{g['slug']}.html", head(g["title"], g["desc"], path, [art, faq_ld_only(g["faqs"]), breadcrumb(crumb)]) + nav("/guides") + f"""
<section class="page-hero article-hero">{BLOBS}<div class="wrap">{crumbs([("Home", "/"), ("Guides", "/guides"), ("This guide", path)])}<span class="eyebrow">Headshot guide</span><h1>{e(g["q"])}</h1></div></section>
<section class="section soft" style="padding-top:40px"><div class="wrap">
<article class="prose">
  <div class="answer"><b>Short answer:</b> {e(g["short"])}</div>
  <figure class="article-img">{gimg(g["img"], "Headshot by Macro Headshots")}</figure>
  {g["body"]}
  <h2>Common questions</h2>
  <div class="faq">{faqs_html}</div>
  <div class="article-cta"><p><b>Ready for your headshot?</b> Book at our Totowa studio, or call <a href="{PHONE_TEL}">{PHONE}</a>.</p><a class="btn btn-primary btn-sm" href="/appointments">Book a session</a></div>
  {f'<p class="related">Related services: <span class="areas">{rel_svcs}</span></p>' if rel_svcs else ''}
</article></div></section>
{guide_cards(others, "More headshot guides")}
""" + footer())
