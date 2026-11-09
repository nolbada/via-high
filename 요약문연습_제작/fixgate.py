import glob
A="<script>(function(){try{if(window.__recl"
B="<script>window.REC_NOGATE=1;(function(){try{if(window.__recl"
fs=glob.glob('/home/claude/via-high/h/**/yoyak-*.html',recursive=True)+['/home/claude/work/real_body.html','/home/claude/via-high/요약문연습_제작/real_body.html']
n=0
for f in fs:
    t=open(f,encoding='utf-8').read()
    if 'REC_NOGATE' in t or A not in t: continue
    open(f,'w',encoding='utf-8').write(t.replace(A,B,1));n+=1
print('patched',n)
p='/home/claude/via-high/h/rec.js';t=open(p,encoding='utf-8').read()
a="    if(KIND==='gimal'||g(NK)||exempt())return;\n    if(/-(go1|go2)"
assert a in t
t=t.replace(a,"    if(KIND==='gimal'||g(NK)||exempt()||W.REC_NOGATE)return;\n    if(/-(go1|go2)",1)
t=t.replace("<script src=","<script src=")
open(p,'w',encoding='utf-8').write(t)
