import glob
R=[
("L.forEach(function(n){h+='<li><span class=\"lw\">'+esc(n.l)+'</span><span class=\"lm\">'+esc(n.k)+'</span>'+(n.c>1?'<span class=\"lc\">'+n.c+'번</span>':'')+'</li>'});",
 "L.forEach(function(n){h+='<li><span class=\"lw\">'+esc(n.l)+'</span><span class=\"lm\">'+esc(n.k)+'</span>'+(n.c>1?'<span class=\"lc\">'+n.c+'번</span>':'')+'<button class=\"rmw\" data-a=\"rmnote\" data-v=\"'+esc(n.l.toLowerCase())+'\">빼기</button></li>'});"),
("  else if(act==='next'){",
 "  else if(act==='rmnote'){var rid=String(v);var rn=NOTES[rid];delete NOTES[rid];jset(K_NOTE,NOTES);delete PUSHED['w:'+rid];jset('vhvs:'+SCH,PUSHED);try{WN.del(rn?rn.l:rid,SRC)}catch(x){}render()}\n  else if(act==='next'){"),
(".wl .lc{", ".wl .rmw{border:1px solid var(--line);background:#fff;color:var(--sub);border-radius:8px;padding:4px 10px;font-size:13px}\n.wl .lc{"),
]
fs=glob.glob('/home/claude/via-high/h/**/yoyak-*.html',recursive=True)+['/home/claude/work/real_body.html','/home/claude/via-high/요약문연습_제작/real_body.html']
n=bad=0
for f in fs:
    t=open(f,encoding='utf-8').read()
    if 'rmnote' in t: continue
    if not all(a in t for a,b in R): bad+=1;print('NOFIT',f);continue
    for a,b in R:t=t.replace(a,b,1)
    open(f,'w',encoding='utf-8').write(t);n+=1
print('patched',n,'nofit',bad)
