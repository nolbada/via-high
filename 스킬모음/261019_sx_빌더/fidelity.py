import json,re,subprocess,sys
REPO='/home/claude/via-high'
UN=[('geumcheon-3','h/geumcheon-gimal/3'),('geumcheon-4','h/geumcheon-gimal/4'),('jusung-3','h/jusung-gimal/3'),('jusung-4','h/jusung-gimal/4'),
    ('cheongseok-3','h/cheongseok-gimal/3'),('cheongseok-4','h/cheongseok-gimal/4'),('jusung-go2-L4','h/jusung-go2/L4'),
    ('mock-2211','h/jusung-go2/mock'),('mock-2311','h/jusung-go2/mock'),('mock-2410','h/jusung-go2/mock')]
LIT=re.compile(r'"(?:[^"\\\n]|\\.)*"')
def strings(d):
    S=set()
    for f in ['sunseo-ko','sunseo-abc','sunseo-mun','blank']:
        t=subprocess.run(['git','-C',REPO,'show',f'HEAD:{d}/{f}.html'],capture_output=True,text=True).stdout
        for m in LIT.finditer(t):
            try:S.add(json.loads(m.group(0)))
            except:pass
        # 일부 페이지는 작은따옴표 JS 문자열도 쓴다
    return S
norm=lambda s:re.sub(r'\s+','',s)
tot_bad=0
for name,d in UN:
    D=json.load(open(f'/home/claude/work/data/{name}.json',encoding='utf8'))
    S=strings(d); N={norm(x) for x in S}
    bad=[];nb=0
    for ps in D['passages']:
        for i,(e,k) in enumerate(zip(ps['en'],ps['ko'])):
            if norm(e) not in N:bad.append((ps['id'],i,'EN',e[:50]))
            if norm(k) not in N:bad.append((ps['id'],i,'KO',k[:40]))
        for b in ps['blanks']:
            nb+=1
            if norm(b['ans']) not in N and not any(norm(b['ans']) in x for x in N):bad.append((ps['id'],b['s'],'ANS',b['ans']))
            if norm(b['ans_ko']) not in N:bad.append((ps['id'],b['s'],'ANSKO',b['ans_ko']))
            for o in b['opts']:
                if norm(o['en']) not in N:bad.append((ps['id'],b['s'],'OPT',o['en']))
                if norm(o['ko']) not in N:bad.append((ps['id'],b['s'],'OPTKO',o['ko']))
    print(name,'blanks',nb,'mismatch',len(bad))
    for x in bad[:8]:print('   ',x)
    tot_bad+=len(bad)
print('TOTAL mismatch',tot_bad)
