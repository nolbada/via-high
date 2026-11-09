import glob,sys
R=[
("  view=v;hideSheet();window.__goTop=1;render();window.__goTop=0;window.scrollTo(0,0)\n}",
 "  view=v;try{if(v==='home')sessionStorage.removeItem('vhyv');else sessionStorage.setItem('vhyv',JSON.stringify({p:location.pathname,v:v,c:cur,t:Date.now()}))}catch(e){}\n  hideSheet();window.__goTop=1;render();window.__goTop=0;window.scrollTo(0,0)\n}"),
("window.addEventListener('popstate',function(){histPushed=false;view='home';",
 "window.addEventListener('popstate',function(){histPushed=false;view='home';try{sessionStorage.removeItem('vhyv')}catch(e){}"),
("render();srvLoad();window.addEventListener('pageshow',srvLoad);",
 "/* 자동 새로고침(기록 연동)이 일어나도 보던 문제로 되돌린다 */\ntry{var sv=JSON.parse(sessionStorage.getItem('vhyv')||'null');if(sv&&sv.p===location.pathname&&Date.now()-sv.t<600000&&sv.v&&sv.v!=='home'){view=sv.v;cur=sv.c||0;try{history.pushState({v:view},'');histPushed=true}catch(e){}}}catch(e){}\nrender();srvLoad();window.addEventListener('pageshow',srvLoad);"),
]
fs=glob.glob('/home/claude/via-high/h/**/yoyak-*.html',recursive=True)+['/home/claude/work/real_body.html','/home/claude/via-high/요약문연습_제작/real_body.html']
n=s=bad=0
for f in fs:
    t=open(f,encoding='utf-8').read()
    if 'vhyv' in t: s+=1;continue
    if not all(a in t for a,b in R): bad+=1;print('NOFIT',f);continue
    for a,b in R:t=t.replace(a,b,1)
    open(f,'w',encoding='utf-8').write(t);n+=1
print('patched',n,'skipped',s,'nofit',bad)
