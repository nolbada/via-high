import json,sys,re
errs=[];warn=[]
f=sys.argv[1]
D=json.load(open(f,encoding='utf8'))
def E(m):errs.append(m)
for k in ['set','title','lesson','passages']:
    if k not in D:E('top missing '+k)
ids=set()
for ps in D['passages']:
    pid=ps.get('id','?')
    if pid in ids:E('dup id '+pid)
    ids.add(pid)
    for k in ['id','label','modes','nums','en','ko','key','why','theme','link','ins','blanks','gist']:
        if k not in ps:E(f'{pid} missing {k}')
    if errs and any(e.startswith(pid+' missing') for e in errs):continue
    n=len(ps['en'])
    for k in ['ko','key','why','nums']:
        if len(ps[k])!=n:E(f'{pid} len({k})={len(ps[k])}!={n}')
    if len(ps['link'])!=n-1:E(f'{pid} link len {len(ps["link"])} != {n-1}')
    if 'abc' in ps['modes'] and n<7:E(f'{pid} abc needs n>=7')
    if 'mun' in ps['modes'] and n<5:E(f'{pid} mun needs n>=5')
    if 'mun' in ps['modes'] and len([i for i in ps['ins'] if 1<=i<=n-1])<1:E(f'{pid} mun but no ins')
    for i in ps['ins']:
        if not(1<=i<=n-1):E(f'{pid} ins {i} out of range')
    if ps['why'][0]!='':E(f'{pid} why[0] must be empty')
    for i in range(n):
        c,l=ps['key'][i]
        if i>=1:
            w=ps['why'][i]
            if len(w)<25:E(f'{pid}[{i}] why too short')
            if len(w)>220:warn.append(f'{pid}[{i}] why long {len(w)}')
            if not re.search(r'[A-Za-z]{2,}',w):E(f'{pid}[{i}] why has no English')
        if not re.search(r'\([^()]*[A-Za-z]{2,}[^()]*\)\s*$',l):E(f'{pid}[{i}] key line lacks trailing (English): {l[:30]}')
        if len(l)>90:warn.append(f'{pid}[{i}] key line long')
        if c and not re.match(r'^[^()]*[A-Za-z][^()]*\([^()]*\)$',c):E(f'{pid}[{i}] conn format: {c}')
    if D.get('lesson') and not re.search(r'[A-Za-z]{2,}',ps['gist']):E(f'{pid} gist no English')
    for bi,b in enumerate(ps['blanks']):
        for k in ['s','ans','ans_ko','opts','clue']:
            if k not in b:E(f'{pid} blank{bi} missing {k}')
        if 's' in b and 'ans' in b:
            if not(0<=b['s']<n) or b['ans'] not in ps['en'][b['s']]:E(f'{pid} blank{bi} ans not in sentence')
        if len(b.get('opts',[]))!=4:E(f'{pid} blank{bi} opts!=4')
        if b.get('clue') and not re.search(r'[A-Za-z]{2,}',b['clue']):E(f'{pid} blank{bi} clue no English')
        for o in b.get('opts',[]):
            if o['en']==b.get('ans'):E(f'{pid} blank{bi} opt equals ans')
print(f, 'passages',len(D['passages']),'sentences',sum(len(p['en']) for p in D['passages']),'blanks',sum(len(p['blanks']) for p in D['passages']))
for m in errs[:60]:print('ERR',m)
print('errors',len(errs),'warnings',len(warn))
sys.exit(1 if errs else 0)
