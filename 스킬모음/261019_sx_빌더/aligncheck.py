import json,re,glob
tot=0;bad=[]
for f in sorted(glob.glob('data/*.json')):
    D=json.load(open(f,encoding='utf8'))
    for ps in D['passages']:
        for i in range(1,len(ps['en'])):
            w=ps['why'][i]
            # 영어 조각: 한글 괄호 앞의 영어 구절 (예: 'In contrast(반면)' 또는 \"Although(…)\")
            frs=re.findall(r"([A-Za-z][A-Za-z’'\- ,]{1,40}?)\s*\(",w)
            frs+=re.findall(r"\(([A-Za-z][A-Za-z’'\- ,.]{1,40})\)",w)
            frs=[x.strip(" ,'’") for x in frs if len(x.strip())>=2]
            if not frs:continue
            cur=ps['en'][i].lower(); prev=ps['en'][i-1].lower()
            tot+=1
            ok=any(x.lower() in cur or x.lower() in prev for x in frs)
            if not ok:bad.append((f.split('/')[-1],ps['id'],i,w[:80],frs[:3]))
print('checked',tot,'bad',len(bad))
for b in bad[:40]:print(b)
