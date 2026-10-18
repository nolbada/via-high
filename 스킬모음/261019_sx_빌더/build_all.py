import json,os,re,shutil,sys
sys.path.insert(0,'/home/claude/work')
import mkpage
REPO='/home/claude/via-high/h'
VER='261019'
UNITS=[ # (data json(s), target dir, display unit title, school footer, gate)
 (['geumcheon-3'],'geumcheon-gimal/3','3과','금천고1 공통영어2 3과 The True Art Lovers',True),
 (['geumcheon-4'],'geumcheon-gimal/4','4과','금천고1 공통영어2 4과 AI Neural Implants',True),
 (['jusung-3'],'jusung-gimal/3','3과','주성고1 공통영어2 3과',True),
 (['jusung-4'],'jusung-gimal/4','4과','주성고1 공통영어2 4과',True),
 (['cheongseok-3'],'cheongseok-gimal/3','3과','청석고 공통영어2',True),
 (['cheongseok-4'],'cheongseok-gimal/4','4과','청석고 공통영어2',True),
 (['jusung-go2-L4'],'jusung-go2/L4','4과','주성고 영어II',False),
 (['mock-2211','mock-2311','mock-2410'],'jusung-go2/mock','모의고사 (22년 11월 · 23년 11월 · 24년 10월)','주성고 영어II',False),
]
only=sys.argv[1:] 
def load(names):
    D=None
    for n in names:
        d=json.load(open(f'/home/claude/work/data/{n}.json',encoding='utf8'))
        if D is None:D=d
        else:D['passages']+=d['passages']
    return D
os.makedirs(f'{REPO}/common',exist_ok=True)
for f in ['sx.js','sx.css']:
    shutil.copy(f'/home/claude/work/common/{f}',f'{REPO}/common/{f}')
for names,tgt,title,school,gate in UNITS:
    if only and tgt not in only:continue
    if not all(os.path.exists(f'/home/claude/work/data/{n}.json') for n in names):
        print('SKIP (no data)',tgt);continue
    D=load(names)
    if tgt.endswith('mock'):
        D['title']=title
    out=f'{REPO}/{tgt}'
    open(f'{out}/sx-data.js','w',encoding='utf8').write('var DATA='+json.dumps(D,ensure_ascii=False,separators=(',',':'))+';\n')
    g='<script src="../gate.js"></script>\n' if gate else ''
    ut=D['title'] if not tgt.endswith('mock') else title
    short=title if tgt.endswith('mock') else title
    for app,fn in [('ko','sunseo-ko'),('abc','sunseo-abc'),('mun','sunseo-mun'),('blank','blank')]:
        # 앱을 쓸 수 있는 구역이 있는 경우만
        html=mkpage.page(app,short if not tgt.endswith('mock') else '모의고사',school if False else school.split(' ')[0] if False else school,VER,'../',g)
        open(f'{out}/{fn}.html','w',encoding='utf8').write(html)
    print('built',tgt,len(D['passages']),'passages')
# index 라벨
REPL=[('순서배열 · 문장 단위 + 문장삽입','문장삽입 (매번 다른 문제)'),('순서배열 · 문장 단위 + 삽입','문장삽입 (매번 다른 문제)'),
      ('순서배열 문장 단위 + 삽입','문장삽입'),('>문장+삽입<','>문장삽입<'),('문장 단위 + 문장삽입','문장삽입'),('문장 단위 + 삽입','문장삽입')]
def relabel(p):
    s=open(p,encoding='utf8').read();o=s
    for a,b in REPL:s=s.replace(a,b)
    if s!=o:open(p,'w',encoding='utf8').write(s);print('relabeled',p)
for site in ['geumcheon-gimal','jusung-gimal','cheongseok-gimal','jusung-go2']:
    relabel(f'{REPO}/{site}/index.html')
for r,dd,ff in os.walk(f'{REPO}/cheongseok-gimal'):
    if 'index.html' in ff and r!=f'{REPO}/cheongseok-gimal':relabel(os.path.join(r,'index.html'))
