# 학교별 '요약문 연습 목록' 페이지(h/<학교>/yoyak.html)를 만든다. 학교 index.html 의 YL/YM 을 읽어 쓴다.
import re,json,os,glob,sys
H=sys.argv[1] if len(sys.argv)>1 else '/home/claude/via-high/h'
NAME={'geumcheon':'금천고','jusung':'주성고','cheongseok':'청석고'}
CIR='❶❷❸❹❺❻❼❽'
PAGE="""<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>__T__ 요약문 연습</title>
<style>:root{--bg:#f6f8f7;--card:#fff;--ink:#16211f;--sub:#5b6b67;--line:#dbe4e1;--pri:#0f766e}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,'Malgun Gothic',sans-serif;-webkit-text-size-adjust:100%}
.w{max-width:560px;margin:0 auto;padding:14px 14px 40px}.back{display:inline-block;color:var(--sub);text-decoration:none;font-weight:700;font-size:15px;padding:6px 2px}h1{font-size:21px;margin:6px 0 14px}
h2{font-size:15px;color:var(--sub);margin:20px 2px 8px}.g{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}
a.r{display:flex;justify-content:space-between;align-items:center;padding:15px 16px;border-top:1px solid var(--line);text-decoration:none;color:var(--ink);font-size:16px;font-weight:700}a.r:first-child{border-top:0}a.r span+span{color:var(--pri);font-size:14px}</style></head><body><div class="w">
<a class="back" href="index.html">‹ 메인</a><h1>요약문 연습</h1>__B__</div></body></html>"""
def rows(items):return '<div class="g">'+''.join('<a class="r" href="%s"><span>%s</span><span>열기</span></a>'%(h,t) for t,h in items)+'</div>'
for idx in sorted(glob.glob(H+'/*/index.html')):
    d=os.path.dirname(idx);sch=os.path.basename(d)
    m=re.match(r'(geumcheon|jusung|cheongseok)-go([12])$',sch)
    if not m:continue
    s=open(idx,encoding='utf-8').read()
    i=s.find('var YL=')
    if i<0:continue
    dec=json.JSONDecoder();YL,e=dec.raw_decode(s,i+7)
    j=s.index('YM=',e)+3;YM,e2=dec.raw_decode(s,j)
    YM=[x for x in YM if os.path.exists(os.path.join(d,x[1]))]
    YL={k:[z for z in v if os.path.exists(os.path.join(d,'%s/yoyak-lian-z%d.html'%(k,z)))] for k,v in YL.items()}
    b=''
    for k in sorted(YL):
        z=YL[k]
        if z:b+='<h2>교과서 %s과</h2>'%k[1:]+rows([('요약문 연습 '+CIR[i-1],'%s/yoyak-lian-z%d.html'%(k,i)) for i in z])
    if YM:b+='<h2>모의고사</h2>'+rows([(t,h) for t,h in YM])
    if not b:continue
    t='%s%s'%(NAME[m.group(1)],'1' if m.group(2)=='1' else '2')
    open(d+'/yoyak.html','w',encoding='utf-8').write(PAGE.replace('__T__',t).replace('__B__',b));print(sch,sum(len(v) for v in YL.values()),len(YM))
