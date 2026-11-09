import glob
R=[("<span class=\"ot\">'+words(o[0])+'<span class=\"dash\">–</span>'+words(o[1])+'</span>",
    "<span class=\"ot\">'+(done?words(o[0]):esc(o[0]))+'<span class=\"dash\">–</span>'+(done?words(o[1]):esc(o[1]))+'</span>"),
   ("밑줄 단어를 누르면 뜻이 나와요. 번호를 누르면 답을 골라요.","문장의 밑줄 단어를 누르면 뜻이 나와요. 보기를 누르면 답을 골라요.")]
fs=glob.glob('/home/claude/via-high/h/**/yoyak-*.html',recursive=True)+['/home/claude/work/real_body.html','/home/claude/via-high/요약문연습_제작/real_body.html']
n=bad=0
for f in fs:
    t=open(f,encoding='utf-8').read()
    if R[0][1] in t: continue
    if not all(a in t for a,b in R): bad+=1;print('NOFIT',f);continue
    for a,b in R:t=t.replace(a,b,1)
    open(f,'w',encoding='utf-8').write(t);n+=1
print('patched',n,'nofit',bad)
