import glob
B="<button class=\"back\" data-a=\"home\">목록</button>"
SW="<button class=\"back\" data-a=\"sw\">바꿔 말하기</button>"
R=[
("var h='<div class=\"top\">"+B+"<span class=\"cnt\">'+(cur+1)+' / '+Qs.length+'</span></div>';",
 "var h='<div class=\"top\">"+B+SW+"<span class=\"cnt\">'+(cur+1)+' / '+Qs.length+'</span></div>';"),
("var h='<div class=\"top\">"+B+"</div><h1>'+Qs.length+'문제 중 '+okCount()+'문제 맞았어요</h1>';",
 "var h='<div class=\"top\">"+B+SW+"</div><h1>'+Qs.length+'문제 중 '+okCount()+'문제 맞았어요</h1>';"),
("var h='<div class=\"top\">"+B+"<span class=\"cnt\">단어노트 '+L.length+'개</span></div>';",
 "var h='<div class=\"top\">"+B+SW+"<span class=\"cnt\">단어노트 '+L.length+'개</span></div>';"),
]
fs=glob.glob('/home/claude/via-high/h/**/yoyak-*.html',recursive=True)+['/home/claude/work/real_body.html','/home/claude/via-high/요약문연습_제작/real_body.html']
n=bad=0
for f in fs:
    t=open(f,encoding='utf-8').read()
    if SW in t.split('function vHome')[0]+t.split('function vQ')[1][:400] and 'class="back" data-a="sw"' in t: continue
    if not all(a in t for a,b in R): bad+=1;print('NOFIT',f);continue
    for a,b in R:t=t.replace(a,b,1)
    open(f,'w',encoding='utf-8').write(t);n+=1
print('patched',n,'nofit',bad)
