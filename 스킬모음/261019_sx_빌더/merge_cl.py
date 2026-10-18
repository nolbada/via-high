import json,glob,os,re,sys
S='/tmp/claude-0/-home-claude/4d132f9d-5ef6-5252-931c-ecbc6e47e615/scratchpad/cl/'
bad=0;tot=0
for fn in sorted(glob.glob('data/*.json')):
    name=os.path.basename(fn)[:-5]; cf=S+f'cl_{name}.json'
    if not os.path.exists(cf): print('MISSING',name); bad+=1; continue
    d=json.load(open(fn,encoding='utf8')); c=json.load(open(cf,encoding='utf8'))
    for p in d['passages']:
        e=c.get(p['id']); n=len(p['en'])
        if not e or len(e['cl'])!=n or len(e['st'])!=n: print('BAD',name,p['id']); bad+=1; continue
        order='기승전결'; idx=[order.index(x) for x in e['st']]
        if idx!=sorted(idx) or set(idx)!={0,1,2,3}: print('STAGE',name,p['id'],e['st']); bad+=1
        for i,x in enumerate(e['cl']):
            tot+=1
            if len(x['m'])>30: print('LONG',name,p['id'],i,len(x['m']),x['m'])
            if not x.get('m') or not x.get('t'): print('EMPTY',name,p['id'],i); bad+=1
        p['cl']=e['cl'];p['st']=e['st'];p['stt']=e['stt']
    if '--write' in sys.argv: json.dump(d,open(fn,'w',encoding='utf8'),ensure_ascii=False,indent=1)
print('cards',tot,'bad',bad)
