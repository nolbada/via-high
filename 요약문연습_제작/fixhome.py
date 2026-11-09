import glob,sys
roots=sys.argv[1:]
A='<a class="tag" href="../index.html" style="text-decoration:none">목록</a>'
B='<a class="tag" href="../yoyak.html" style="text-decoration:none">목록</a>'
n=0
for r in roots:
    fs=glob.glob(r+'/h/**/yoyak-*.html',recursive=True) if not r.endswith('.html') else [r]
    for f in fs+[r+'/요약문연습_제작/real_body.html',r+'/real_body.html']:
        try:t=open(f,encoding='utf-8').read()
        except:continue
        if A in t:open(f,'w',encoding='utf-8').write(t.replace(A,B,1));n+=1
print('patched',n)
