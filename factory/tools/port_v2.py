"""v1(유형 줄 + 이전 회/다음 회) 구조의 학교 메인 화면을 v2(회차 버튼 그리드·단계식 열림)로 바꾼다. (261025)

쉬운 설명: 옛 방식(v1)으로 만든 학교 앱의 첫 화면 '유형 풀코스' 부분만 새 디자인(작은 회차 버튼)으로 갈아 끼운다.
달력·이어서 풀기·오답 노트·전체 랜덤·학습 기록 등 나머지는 그대로 둔다.

사용: python3 factory/tools/port_v2.py <학교폴더> [...]      예) port_v2.py new-go1
      --dry : 파일을 쓰지 않고 바뀔 수 있는지만 확인
      --file 경로 : h/<학교>/index.html 대신 이 파일을 바꾼다(시험용)
조각: snippets/stage_css.txt, stage_state.txt, stage_grid.txt, rows.txt(v2), hand.txt(v2 마지막 줄)
이미 v2(stState 있음)면 건너뛴다."""
import sys,os,re
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.abspath(os.path.join(HERE,'..','..'))
SN=os.path.join(HERE,'..','snippets')
def sn(n): return open(os.path.join(SN,n+'.txt'),encoding='utf-8').read()
STAGE_CSS=sn('stage_css').rstrip('\n')+'\n'
STATE=sn('stage_state').rstrip('\n')
GRID=sn('stage_grid')
ROWS=sn('rows').rstrip('\n')
HAND_STAGE=[l for l in sn('hand').split('\n') if "[data-stage]" in l][0]
SEL_V1="  if(!selNo||selNo<1||selNo>N){selNo=N;for(var i=0;i<N;i++)if(!flat[i].done){selNo=i+1;break}}"
F_LINE="  var f=flat[selNo-1],v=f.v,pr=prog(v);"
FONT_BAD=re.compile(r'font:(\d{3}) ([0-9.]+)px(?:/([0-9.]+))? inherit;(font-family:inherit;)?')
def fix_font(m):
    o='font-weight:%s;font-size:%spx;'%(m.group(1),m.group(2))
    if m.group(3): o+='line-height:%s;'%m.group(3)
    return o+'font-family:inherit;'
def convert(s,name):
    if 'stState' in s: return None
    def need(x,what):
        if s.count(x)!=1: raise SystemExit('%s: %s 를 정확히 1번 찾지 못함 (%d번)'%(name,what,s.count(x)))
    need(SEL_V1,'회 자동 선택 줄(v1)'); s=s.replace(SEL_V1,STATE)
    need(F_LINE,'선택한 회 시작 줄')
    a=s.index(F_LINE)
    m=re.compile(r"  h\+='</div></div><div class=\"rnav\">[^\n]*\n").search(s,a)
    if not m: raise SystemExit(name+': 이전 회/다음 회(rnav) 줄을 찾지 못함')
    mid=s[a:m.start()]
    for must in ['<h2>','ACT.forEach','window.QGO','soonbox','qtot']:
        if must not in mid: raise SystemExit(name+': 선택한 회 구간에 '+must+' 없음 (구조가 v1과 다름)')
    s=s[:a]+GRID+ROWS+'\n'+s[m.end():]
    k="  var ns=e.target.closest('[data-no]');"
    need(k,'이전/다음 회 버튼 처리 줄'); s=s.replace(k,HAND_STAGE+'\n'+k)
    s=FONT_BAD.sub(fix_font,s)
    need('</head>','</head>'); s=s.replace('</head>',STAGE_CSS+'</head>')
    s=s.replace('<a class="wnb mxb" href="dajigi.html"><span><b>스페셜 · 교과서 다지기</b><small>문법·어휘 · 매번 다른 20문항 · 4과와 모의고사를 끝낸 뒤에</small>',
                '<a class="wnb mxb spb" href="dajigi.html"><span><b>스페셜 · 교과서 다지기</b><small>문법·어휘 · 매번 다른 20문항 · <em>4과와 모의고사를 끝낸 뒤에</em></small>')
    return s
def main():
    av=sys.argv[1:];dry='--dry' in av
    if '--file' in av:
        p=av[av.index('--file')+1];targets=[(p,p)]
    else: targets=[(sc,os.path.join(ROOT,'h',sc,'index.html')) for sc in av if not sc.startswith('--')]
    if not targets: print(__doc__);sys.exit(1)
    for name,p in targets:
        s=open(p,encoding='utf-8').read();t=convert(s,name)
        if t is None: print(name,'이미 v2');continue
        if not dry: open(p,'w',encoding='utf-8').write(t)
        print(name,'v2로 바꿈' if not dry else 'v2로 바꿀 수 있음(--dry)')
if __name__=='__main__': main()
