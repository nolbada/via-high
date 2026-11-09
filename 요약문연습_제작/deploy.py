# 사용: python3 deploy.py <data/id.json> ...  : out 페이지를 via-high 로 복사하고 목록 행을 추가
import sys,json,re,shutil,os
VH='/home/claude/via-high/h/'
for dj in sys.argv[1:]:
    d=json.load(open(dj,encoding='utf-8')); M=d['meta']
    L=M['src'].split('/')[1]            # L3 / L4
    dst='%s%s/%s/%s.html'%(VH,M['sch'],L,M['page'])
    shutil.copy('out/%s__%s__%s.html'%(M['sch'],L,M['page']),dst)
    ip='%s%s/index.html'%(VH,M['sch']); s=open(ip,encoding='utf-8').read()
    href='%s/%s.html'%(L,M['page'])
    if href in s: print('row exists',href); continue
    row='["%s 요약문 연습 %s","바꿔 말하기·단어 물어보기","%s","key:%s:%s"],'%(M['lesson'],M['label'],href,L,M['page'])
    m=re.search(r'"플러스 자료","subs":\[\{"t":"","items":\[',s); assert m,ip
    s=s[:m.end()]+row+s[m.end():]
    open(ip,'w',encoding='utf-8').write(s); print('added',href)
