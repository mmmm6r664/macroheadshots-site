import json, glob, os
from playwright.sync_api import sync_playwright
pages=['index.html','headshots-in-wayne.html','pricing.html','appointments.html','privacy-policy.html']
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True)
    for f in pages:
        pg.goto('http://localhost:8812/'+f); pg.wait_for_timeout(300)
        pg.evaluate("document.querySelectorAll('img').forEach(i=>{i.loading='eager'})"); pg.wait_for_timeout(2500)
        r=pg.evaluate('''()=>[...document.images].filter(i=>i.offsetWidth>0).map(i=>{const r=i.getBoundingClientRect();return {src:i.src.split('/').pop().slice(0,28),w:Math.round(r.width),h:Math.round(r.height),ratio:+(r.height/r.width).toFixed(2),cls:(i.className||i.parentElement.className).slice(0,25)}}).filter(x=>x.h>620||x.ratio>1.6)''')
        print(f, 'tall images:', r[:6])
    b.close()
