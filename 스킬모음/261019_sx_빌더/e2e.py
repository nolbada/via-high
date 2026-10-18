import sys,random
from playwright.sync_api import sync_playwright
units=sys.argv[1:]
apps=['ko','abc','mun','blank']
fails=0
with sync_playwright() as p:
    b=p.chromium.launch()
    for u in units:
        for app in apps:
            fn='blank' if app=='blank' else f'sunseo-{app}'
            for rep in range(3):
                pg=b.new_page(viewport={'width':420,'height':900})
                errs=[]
                pg.on('pageerror',lambda e:errs.append(str(e)))
                pg.goto(f'http://localhost:8766/{u}/{fn}.html?r={rep}')
                pg.wait_for_timeout(200)
                pg.evaluate("localStorage.clear()"); pg.reload(); pg.wait_for_timeout(200)
                n=0;whyok=0;ctxok=0;hl=0
                for step in range(12):
                    if pg.query_selector('.sum'):break
                    try:
                        if app=='mun':
                            pg.click('.mk >> nth=%d'%random.randint(0,4)); pg.click('.sb')
                        elif app=='abc':
                            pg.click('.ob >> nth=%d'%random.randint(0,4)); pg.click('.sb')
                        elif app=='ko':
                            for _ in range(3):
                                if pg.query_selector('.sb[disabled]'): pg.click('.pb >> nth=0')
                            pg.click('.sb')
                        else:
                            pg.click('.ob >> nth=%d'%random.randint(0,4))
                    except Exception as e:
                        errs.append('click:'+str(e)[:80]);break
                    n+=1
                    if pg.query_selector('.ctx'):ctxok+=1
                    if pg.query_selector('.why'):whyok+=1
                    if pg.query_selector('.hlbox'):hl+=1
                    nx=pg.query_selector('.nx')
                    if nx:nx.click()
                bad=(errs or ctxok!=n or hl!=n or (app!='blank' and whyok!=n) or n==0)
                if bad:fails+=1
                print(u,app,rep,'solved',n,'ctx',ctxok,'hl',hl,'why',whyok,'ERR' if bad else 'ok',errs[:2])
                pg.close()
    b.close()
print('FAILS',fails)
