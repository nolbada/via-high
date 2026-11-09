import sys,re,json,os
base=os.path.splitext(os.path.basename(sys.argv[1]))[0]
d=json.load(open('data/%s.json'%base,encoding='utf-8'))
G=d['gloss'];bad=[]
emo=re.compile('[\U0001F300-\U0001FAFF\u2600-\u2775\u2794-\u27BF\u2B50\u2B55]')
WRE=re.compile(r"[A-Za-z][A-Za-z'’\-]*[A-Za-z]|[A-Za-z]")
EASY=set('a an the of to in on at is are was were be been it its i he she we you they them his her our their my your this that these those and or but as by for with from not no so if do does did has have had will would can could may might must than then there here who whom which what when where how why also too very more most much many some any all each both one two'.split())
def need(txt,where):
    for w in WRE.findall(txt):
        k=w.lower()
        if k in EASY or len(k)<3: continue
        if k not in G: bad.append((where,k))
for p in d['passage']:
    pass
for q in d['questions']:
    need(q['summary'],'summary%d'%q['id'])
    for o in q['opts']:
        for x in o: need(x,'opt%d'%q['id'])
    for e in q['evid_full']: need(e['en'],'evid%d-%d'%(q['id'],e['n']))
miss={}
for w,k in bad: miss.setdefault(k,w)
txt=json.dumps(d,ensure_ascii=False)
if emo.search(txt): print('FAIL emoji')
if miss: print('WARN G 누락(눌러도 뜻이 안 나옴, 중요 단어면 G에 추가)',len(miss),list(miss)[:40])
for s in d['story']:
    if s['a']!=s['a'].lower() or ' ' in s['a']: print('FAIL 기본형?',s['a'])
if not emo.search(txt): print('QA OK',base)
