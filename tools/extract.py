import json,re,sys
from bs4 import BeautifulSoup
d=json.load(open(sys.argv[1]))
def els(html):
    s=BeautifulSoup(html,'html.parser')
    out={'title':s.title.text if s.title else '','desc':(s.find('meta',attrs={'name':'description'}) or {}).get('content',''),'sections':[]}
    for sec in s.select('.c-section'):
        cls=' '.join(sec.get('class',[]))
        items=[]
        for el in sec.select('.c-wrapper'):
            t=[c for c in el.get('class',[]) if c.startswith('c-') and c!='c-wrapper']
            if not t or t[0] in('c-section','c-row','c-column'): continue
            t=t[0][2:]
            if t in('heading','sub-heading','paragraph','bullet-list'):
                txt=el.get_text(' ',strip=True)
                if txt: items.append([t,txt])
            elif t=='image':
                im=el.find('img'); a=el.find('a')
                if im: items.append(['image',im.get('src'),im.get('alt',''),a.get('href') if a else ''])
            elif t=='button':
                a=el.find(['a','button']); items.append(['button',a.get_text(' ',strip=True),a.get('href','')])
            elif t=='faq':
                for q in el.select('.hl-faq-child'):
                    items.append(['faq',q.select_one('.hl-faq-child-heading').get_text(' ',strip=True),q.select_one('.hl-faq-child-panel').get_text(' ',strip=True)])
            else:
                items.append([t,el.get_text(' ',strip=True)[:200]])
        out['sections'].append({'id':sec.get('id'),'mobile':'mobile' in cls,'desktop':'desktop' in cls,'items':items})
    return out
res={p:els(v['html']) for p,v in d['pages'].items() if p!='/home'}
json.dump(res,open(sys.argv[2],'w'),indent=1,ensure_ascii=False)
