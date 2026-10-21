import re,sys,shutil
import port
R=port.R
import os; os.makedirs(os.path.join(port.HERE,'_before'),exist_ok=True)
SRC={'T':'3과','L':'4과','D':'모의고사','F':'최종점검'}
def autoroad(school):
    s=open(R+school+'/index.html',encoding='utf-8').read()
    a=s.index('var VIS=[');b=s.index('\n];',a)
    weeks=[re.findall(r'\{([LTDF]):',ln) for ln in s[a:b].split('\n')[1:] if ln.strip().startswith('[')]
    ra=s.index('var ROAD=[');rb=s.index('];',ra)
    dates=re.findall(r"\['(\d+/\d+)','(\d+/\d+)'",s[ra:rb])
    assert len(dates)==len(weeks),(len(dates),len(weeks))
    no=0;rows=[]
    for (d0,d1),ks in zip(dates,weeks):
        grp=[]
        for k in ks:
            no+=1
            if grp and grp[-1][0]==k: grp[-1][2]=no
            else: grp.append([k,no,no])
        parts=[(str(g[1]) if g[1]==g[2] else '%d~%d'%(g[1],g[2]))+'회 ('+SRC[g[0]]+')' for g in grp]
        txt=' → '.join(parts)
        if all(k=='F' for k in ks): txt+=' · 틀린 문제, 약한 유형 골라 풀기'
        rng=(str(grp[0][1]) if False else '')
        first=grp[0][1];last=grp[-1][2]
        rg=(str(first)+'회') if first==last else '%d~%d회'%(first,last)
        rows.append("['%s','%s',\"%s\",\"%s\"]"%(d0,d1,rg,txt))
    return 'var ROAD=['+','.join(rows)+'];'
if __name__=='__main__':
    for sc in sys.argv[1:]:
        road=autoroad(sc); print(sc,road)
        if sc=='cheongseok-go2':
            p=R+sc+'/index.html';t=open(p,encoding='utf-8').read()
            a="풀코스 · '+nlab(v)+"; assert t.count(a)==1
            t=t.replace(a,"풀코스 · '+f.no+'회 ('+src(v)+')'+"); open(p,'w',encoding='utf-8').write(t)
        for fn in ['index.html','parts.js']:
            shutil.copy(R+sc+'/'+fn,os.path.join(port.HERE,'_before','%s_%s_before')%(sc,fn))
        port.port(sc,road)
        import patch2; patch2.patch(sc)
