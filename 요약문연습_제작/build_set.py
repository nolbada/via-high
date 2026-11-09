# -*- coding: utf-8 -*-
# 사용: python3 build_set.py sets/<id>.py   -> out/<page>.html, data/<id>.json, blind/<id>.json
import sys,re,json,os
VH='/home/claude/via-high/h/'
def load(path):
    ns={'re':re,'json':json}
    exec(open(path,encoding='utf-8').read(),ns)
    return ns
def reorder(q,TARGET):
    t=TARGET[q['id']]; a=q['ans']
    idx=list(range(5)); idx.remove(a)
    order=idx[:t]+[a]+idx[t:]
    for k in ('opts','optko','wrong'): q[k]=[q[k][i] for i in order]
    q['ans']=t
def main(path):
    ns=load(path); META=ns['META']
    d=json.loads(open(META['src'] if META['src'].startswith('/') else VH+META['src'],encoding='utf-8').read().split('=',1)[1].rsplit(';',1)[0])
    P=d['passages'][META['pidx']]; EN,KO=P['en'],P['ko']
    Q,G,JD,FC,STORY,SCENES,HLKO,UM,TARGET=[ns[k] for k in ('Q','G','JD','FC','STORY','SCENES','HLKO','UM','TARGET')]
    assert sorted(TARGET)==[q['id'] for q in Q],'TARGET ids'
    for q in Q:
        reorder(q,TARGET)
        q['jd']=JD[q['id']]; q['fc']=FC[q['id']]
        for u in q['use']:
            u['wk'],u['hk']=UM[u['w']]
            assert re.search(r'\b'+u['w']+r'\w*',u['ex'],re.I),u['w']
            assert u['hk'] in u['ko'],(u['w'],u['hk'])
        filled=q['summary'].replace('(A)',q['opts'][q['ans']][0]).replace('(B)',q['opts'][q['ans']][1])
        joined=' '.join(c[0].replace('[[','').replace(']]','') for c in q['jd'])
        assert joined==filled,(q['id'],joined,filled)
        assert len(q['opts'])==5 and len(q['optko'])==5 and len(q['wrong'])==5 and q['wrong'][q['ans']] is None
        q['evid_full']=[dict(en=EN[e['n']-1],ko=KO[e['n']-1],hl=e['hl'],hlko=HLKO[e['n']],n=e['n']) for e in q['evid']]
        for e in q['evid_full']:
            assert len(e['hlko'])==len(e['hl']),(q['id'],e['n'])
            for h in e['hl']: assert h in e['en'],('hl',q['id'],e['n'],h)
            for h in e['hlko']: assert h in e['ko'],('hlko',e['n'],h)
    swk={sw[0].lower():sw for q in Q for sw in q['swaps']}
    for st in STORY:
        sw=swk[st['a']]; st['b']=sw[1]; st['k']=sw[2]
        st['en']=EN[st['n']-1]; st['ko']=KO[st['n']-1]
        assert re.search(r'\b'+st['form']+r'\b',st['en'],re.I),st['a']
        q=[x for x in Q if x['id']==st['sq']][0]
        filled=q['summary'].replace('(A)',q['opts'][q['ans']][0]).replace('(B)',q['opts'][q['ans']][1])
        assert st['sum'].replace('[[','').replace(']]','') in filled,(st['a'],filled)
    STORY.sort(key=lambda x:x['n'])
    marks=[m for sc in SCENES for m in re.findall(r'\[\[(\w+)\|',sc['line'])]
    assert sorted(marks)==sorted(st['form'] for st in STORY),marks
    for sc in SCENES: sc['en']=[EN[n-1] for n in sc['ns']]; sc['kos']=[KO[n-1] for n in sc['ns']]
    full=dict(meta=META,scenes=SCENES,story=STORY,passage=[dict(n=i+1,en=EN[i],ko=KO[i]) for i in range(len(EN))],questions=Q,gloss=G)
    base=os.path.splitext(os.path.basename(path))[0]
    os.makedirs('data',exist_ok=True)
    json.dump(full,open('data/%s.json'%base,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    T=open('real_body.html',encoding='utf-8').read()
    T=T.replace("var SCH='geumcheon-go1';","var SCH="+json.dumps(META['sch'])+";")
    T=T.replace('<title>4과 요약문 연습 ❶ · 금천고1</title>','<title>%s 요약문 연습 %s</title>'%(META['lesson'],META['label']))
    T=re.sub(r"<span class=\"tag\">금천고1</span><h1>4과 AI Neural Implants</h1><p class=\"sub\">요약문 완성 ❶ · 5문제</p>",
      lambda m:"<a class=\"tag\" href=\"../yoyak.html\" style=\"text-decoration:none\">목록</a><h1>'+DATA.meta.lesson+' '+esc(DATA.meta.title)+'</h1><p class=\"sub\">요약문 연습 '+DATA.meta.label+' · '+Qs.length+'문제</p>",T)
    out=T.replace('__DATA__',json.dumps(full,ensure_ascii=False))
    os.makedirs('out',exist_ok=True)
    open('out/%s__%s__%s.html'%(META['sch'],META.get('dir') or META['src'].split('/')[1],META['page']),'w',encoding='utf-8').write(out)
    print('OK',base,len(Q),'questions',len(out))
if __name__=='__main__': main(sys.argv[1])
