import json, os, glob
from playwright.sync_api import sync_playwright
pages = sorted(glob.glob('site2/*.html'))
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 360, 'height': 780}, device_scale_factor=2, is_mobile=True, has_touch=True)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    for f in pages:
        name = os.path.basename(f)
        errs.clear()
        pg.goto('http://localhost:8812/' + name, wait_until='domcontentloaded'); pg.wait_for_timeout(500)
        r = pg.evaluate('''() => {
          const sw = document.documentElement.scrollWidth, cw = document.documentElement.clientWidth;
          const wide = [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.right > cw + 1 && getComputedStyle(e).position !== 'fixed' && !e.closest('.marquee') && !e.closest('.hero-blobs') && !e.closest('.table-wrap'); }).slice(0,3).map(e => e.className || e.tagName);
          const small = [...document.querySelectorAll('a,button')].filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && (r.height < 32) && !e.closest('.footer') && !e.closest('.prose') && !e.closest('.lead') && !e.classList.contains('skip'); }).slice(0,4).map(e => (e.innerText||e.getAttribute('aria-label')||'').trim().slice(0,25) + ':' + Math.round(e.getBoundingClientRect().height));
          const lds = [...document.querySelectorAll('script[type="application/ld+json"]')].map(s => { try { return JSON.parse(s.textContent)['@type']; } catch (e) { return 'INVALID'; } });
          const noalt = [...document.images].filter(i => !i.hasAttribute('alt')).length;
          const nodim = [...document.images].filter(i => !i.getAttribute('width')).map(i=>i.src.split('/').pop()).slice(0,3);
          return {overflow: sw - cw, wide, small, h1: document.querySelectorAll('h1').length, lds, noalt, nodim,
                  title: document.title.length, desc: (document.querySelector('meta[name=description]')||{}).content?.length,
                  canon: document.querySelector('link[rel=canonical]')?.href};
        }''')
        print(name, json.dumps(r), errs[:1])
    b.close()
