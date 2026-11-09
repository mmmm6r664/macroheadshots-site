"""Validate JSON-LD in the built site against schema.org vocab + Google required fields."""
import json,re,glob,html,sys,collections
V=json.load(open('/tmp/schema.jsonld'))['@graph']
cls={};props={}
def ids(x): 
    if x is None: return []
    return [y['@id'] for y in (x if isinstance(x,list) else [x])]
for n in V:
    t=n['@type'] if isinstance(n['@type'],list) else [n['@type']]
    nid=n['@id'].replace('schema:','')
    if 'rdfs:Class' in t: cls[nid]=[i.replace('schema:','') for i in ids(n.get('rdfs:subClassOf'))]
    if 'rdf:Property' in t: props[nid]=[i.replace('schema:','') for i in ids(n.get('schema:domainIncludes'))]
def ancestors(c):
    out={c};st=[c]
    while st:
        for p in cls.get(st.pop(),[]):
            if p not in out: out.add(p);st.append(p)
    return out
ROOT=sys.argv[1]; SITE='https://macroheadshots.com'
pages={}
for f in glob.glob(f'{ROOT}/**/*.html',recursive=True):
    p=f[len(ROOT):-5]; p='/' if p=='/index' else p
    pages[p]=open(f).read()
def exists(url):
    if not url.startswith(SITE): return True
    u=url[len(SITE):].split('#')[0] or '/'
    return u in pages or u.rstrip('/') in pages
errs=collections.Counter(); notes=[]; counts=collections.Counter(); idmap={}
def walk(o,page,path='$'):
    if isinstance(o,list):
        for i,x in enumerate(o): walk(x,page,f'{path}[{i}]')
        return
    if not isinstance(o,dict): return
    t=o.get('@type')
    if t:
        counts[t]+=1
        if t not in cls: errs[(page,f'unknown type {t}')]+=1
        anc=ancestors(t)
        if '@id' in o and len(o)>1: idmap[o['@id']]=t
        for k,v in o.items():
            if k.startswith('@'): continue
            if k not in props: errs[(page,f'unknown property {t}.{k}')]+=1
            elif props[k] and not (anc & set(props[k])): errs[(page,f'{k} not valid on {t}')]+=1
            if isinstance(v,str) and k in('url','item','image','logo','mainEntityOfPage') and v.startswith(SITE) and not v.startswith(SITE+'/assets') and not exists(v): errs[(page,f'{k} points to missing page {v}')]+=1
            walk(v,page,f'{path}.{k}')
        # Google required/recommended
        if t in('ProfessionalService','LocalBusiness'):
            for r in('name','address'): 
                if r not in o: errs[(page,f'{t} missing {r}')]+=1
            a=o.get('address',{})
            for r in('streetAddress','addressLocality','addressRegion','postalCode','addressCountry'):
                if r not in a: errs[(page,f'address missing {r}')]+=1
        if t=='Offer':
            for r in('price','priceCurrency'):
                if r not in o: errs[(page,f'Offer missing {r}')]+=1
            if 'price' in o and not re.fullmatch(r'\d+(\.\d+)?',str(o['price'])): errs[(page,'Offer price not numeric')]+=1
        if t=='Service' and 'provider' not in o: errs[(page,'Service missing provider')]+=1
        if t=='BreadcrumbList':
            items=o['itemListElement']
            for i,it in enumerate(items):
                if it.get('position')!=i+1: errs[(page,'breadcrumb position')]+=1
                if not it.get('name') or not it.get('item'): errs[(page,'breadcrumb missing name/item')]+=1
            canon=re.search(r'rel="canonical" href="([^"]+)"',pages[page]).group(1)
            if items[-1]['item']!=canon: errs[(page,f'breadcrumb last item {items[-1]["item"]} != canonical {canon}')]+=1
            vis=re.search(r'<nav class="crumbs"[^>]*>(.*?)</nav>',pages[page],re.S)
            if not vis: errs[(page,'no visible breadcrumb')]+=1
            else:
                vn=[html.unescape(re.sub('<[^>]+>','',x)) for x in re.findall(r'<(?:a|span aria-current="page")[^>]*>(.*?)</(?:a|span)>',vis.group(1))]
                if len(vn)!=len(items): errs[(page,f'visible crumbs {len(vn)} vs LD {len(items)}')]+=1
        if t=='FAQPage':
            for q in o['mainEntity']:
                if html.escape(q['name'],quote=True) not in pages[page] and q['name'] not in pages[page]: errs[(page,'FAQ question not visible')]+=1
for p,s in pages.items():
    blocks=re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S)
    for b in blocks:
        try: walk(json.loads(b),p)
        except json.JSONDecodeError as e: errs[(p,'JSON error '+str(e))]+=1
# @id references
for p,s in pages.items():
    for ref in set(re.findall(r'\{"@id": "([^"]+)"\}',s)):
        if ref not in idmap: errs[(p,f'dangling @id {ref}')]+=1
print('pages',len(pages)); print('types',dict(counts))
print('problems',sum(errs.values()))
for (p,m),n in sorted(errs.items()): print(f'  {p}: {m}' + (f' (x{n})' if n>1 else ''))
