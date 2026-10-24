"""6개 학교 앱을 기준(금천고1)과 기계적으로 대조한다. (v2 기준, 261025)
사용: python3 audit.py [학교 ...]        <- 기본: 내 컴퓨터의 저장소 파일을 검사(인터넷 필요 없음, 로컬 모드)
      python3 audit.py --live            <- 저장소 없이 실제 사이트(nolbada.github.io/via-high)를 검사
      python3 audit.py --dump            <- 기준 수치 표 출력(SPEC_values.md 갱신용)
v2 = 메인 화면 '유형 풀코스'가 회차 버튼(.sgrid/.stb) + 단계식 열림(done/lock/now). 버튼을 눌러야 유형 목록이 열린다.
필요: pip install playwright && playwright install chromium"""
import sys,os,re,json,subprocess,socket,time,hashlib
from playwright.sync_api import sync_playwright
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(HERE,'..','..'))
SCHOOLS=['geumcheon-go1','geumcheon-go2','cheongseok-go1','cheongseok-go2','jusung-go1','jusung-go2']
REF='geumcheon-go1'
# (이름, 선택자, 속성들, 상태필요)  색은 테마 변수로 해석해서 비교
PROBES=[
 ('체크박스','.arow .ck input','width,height,accentColor'),
 ('완료 체크칸','.arow .ck i.okb','width,height,borderRadius,fontSize,fontWeight'),
 ('유형 이름 줄','.arow a.at','fontSize,fontWeight,paddingTop,paddingBottom'),
 ('유형 이름 b','.arow a.at b','fontSize,fontWeight'),
 ('매번 다른 문제 표시','.arow a.at .vr','fontSize'),
 ('전체선택 버튼','.qsel button','fontSize,fontWeight,textDecorationLine'),
 ('체크한 유형 이어서 풀기','.qgo','fontSize,fontWeight,borderRadius,paddingTop,borderTopWidth'),
 ('이어서 풀기 카드','.rsm','borderTopWidth,borderRadius,paddingTop,paddingLeft,marginTop'),
 ('이어서 풀기 제목','.rsm b','fontSize'),
 ('이어서 풀기 부제','.rsm small','fontSize'),
 ('배지 줄','.pins','gap,marginTop'),
 ('학습 기록 카드','.rec','borderTopWidth,borderRadius,paddingTop,paddingLeft'),
 ('기록 소제목','.rr em','fontSize'),
 ('이용 시간 소제목 줄','.rec .lrd','fontSize,marginTop'),
 ('기록 카드 큰 칸','.rec .lrs>div','paddingTop,borderTopLeftRadius'),
]
# v2 회차 버튼(유형 풀코스 그리드). 1회 끝냄 상태(done/now/lock이 모두 보이는 상태)에서 잰다
STAGE_PROBES=[
 ('풀코스 제목','.sgh b','fontSize,fontWeight,borderLeftWidth,paddingLeft'),
 ('풀코스 진행 알약','.sgh span','fontSize,fontWeight,borderTopLeftRadius'),
 ('회차 그리드','.sgrid','columnGap,rowGap,marginBottom'),
 ('회차 버튼','.stb','width,height,borderTopWidth,borderTopLeftRadius,paddingTop,paddingBottom'),
 ('회차 단원 뱃지','.stb .sbd','fontSize,fontWeight'),
 ('회차 번호','.stb .sno','fontSize,fontWeight'),
 ('잠금 점','.stb.lock','::after'),
]
STAGE_COLORS=[('끝난 회차 배경','.stb.done','backgroundColor','--priL'),('끝난 회차 테두리','.stb.done','borderTopColor','--pri'),
 ('끝난 회차 숫자','.stb.done .sno','color','--pri'),('지금 회차 테두리','.stb.now','borderTopColor','--pri'),
 ('잠긴 회차 배경','.stb.lock','backgroundColor','--off'),('잠긴 회차 숫자','.stb.lock .sno','color','--offInk'),
 ('풀코스 제목 막대','.sgh b','borderLeftColor','--pri'),('풀코스 진행 알약 배경','.sgh span','backgroundColor','--priL')]
BADGES={'3과','4과','모의','최종'}
COLORS=[('완료 체크칸 배경','.arow .ck i.okb','backgroundColor','--pri'),('완료 체크 글자','.arow .ck i.okb','color','--onpri'),
 ('체크한 유형 버튼 배경','.qgo','backgroundColor','--pri'),
 ('이어서 풀기 테두리','.rsm','borderTopColor','--pri'),('이어서 풀기 제목색','.rsm b','color','--pri'),('기록 카드 테두리','.rec','borderTopColor','--pri')]
BAD_TEXT=['내 진도는 내가 정해요','번호를 누르면','다시 누르면 접힙니다','🎉']
EMOJI=re.compile('[\U0001F300-\U0001FAFF\u2B50\u2705\u274C\u2728\u26A0\u2764\u2B06\u2B07]')  # 별표 U+2605, 체크 U+2713, 원숫자는 허용
def free_port():
    s=socket.socket();s.bind(('',0));p=s.getsockname()[1];s.close();return p
def measure(pg,base,sc):
    pg.goto(base+'h/%s/index.html'%sc);pg.wait_for_timeout(400)
    pg.evaluate("localStorage.clear()");pg.reload();pg.wait_for_timeout(400)
    S={}
    S['처음엔 회차 버튼만(목록 닫힘)']=pg.locator('.sgrid .stb').count()>0 and pg.locator('#today .blk').count()==0 and pg.locator('.arow').count()==0
    S['이전 회/다음 회 없음']=pg.locator('.rnav').count()==0
    nos=pg.eval_on_selector_all('.stb .sno','e=>e.map(x=>x.innerText.trim())')
    bds=pg.eval_on_selector_all('.stb .sbd','e=>e.map(x=>x.innerText.trim())')
    st0=pg.eval_on_selector_all('.stb','e=>e.map(x=>x.className)')
    S['회차 버튼 수']=len(nos)
    S['회차 번호 1~N 이어짐']=nos==['%d회'%(i+1) for i in range(len(nos))]
    S['단원 뱃지 2글자']=bool(bds) and all(b in BADGES for b in bds)
    S['처음 상태 1회 now, 나머지 lock']=bool(st0) and 'now' in st0[0].split() and all(('lock' in c.split()) for c in st0[1:])
    pg.click('.stb[data-stage="1"]');pg.wait_for_timeout(200)
    S['누르면 목록 열림']=pg.locator('#today .blk .arow').count()>0
    S['열린 목록 제목']=pg.inner_text('#today .blk h2').split('\n')[0] if pg.locator('#today .blk h2').count() else ''
    keys=pg.eval_on_selector_all('input[data-q]','e=>e.map(x=>x.dataset.q)')
    hrefs=pg.eval_on_selector_all('.arow a.at','e=>e.map(x=>x.getAttribute("href"))')
    now=int(time.time()*1000)
    pg.evaluate("""a=>{var o={};o[a[0]]={n:1,t:a[3]};o[a[1]]={n:1,t:a[3]};localStorage.setItem('vhp:'+WN.school,JSON.stringify(o));
      localStorage.setItem('vhbm:'+WN.school,JSON.stringify({k:a[2],u:a[4],t:a[3]}));localStorage.setItem('vhd:'+a[0],'75')}""",[keys[0],keys[1],keys[2],now,hrefs[2]])
    pg.click('.stb[data-stage="1"]');pg.wait_for_timeout(200)
    S['다시 누르면 닫힘']=pg.locator('#today .blk').count()==0
    lk=pg.locator('.stb.lock').count()
    if lk:
        n3=pg.get_attribute('.stb.lock >> nth=0','data-stage');pg.click('.stb[data-stage="%s"]'%n3);pg.wait_for_timeout(200)
        t=pg.inner_text('#today .blk .slk') if pg.locator('#today .blk .slk').count() else ''
        S['잠금 안내 문구']=t
        S['잠긴 회차는 목록 없음']=pg.locator('#today .blk .arow').count()==0
    else: S['잠금 안내 문구']='1회 먼저 끝내요';S['잠긴 회차는 목록 없음']=True
    pg.reload();pg.wait_for_timeout(500)
    pg.click('.stb[data-stage="1"]');pg.wait_for_timeout(200)
    R={}
    for n,sel,props in PROBES:
        R[n]=pg.evaluate("""([sel,props])=>{var e=document.querySelector(sel);if(!e)return null;var c=getComputedStyle(e),o={};props.split(',').forEach(function(p){o[p]=c[p]});return o}""",[sel,props])
    C={}
    for n,sel,prop,var in COLORS:
        C[n]=pg.evaluate("""([sel,prop,v])=>{var e=document.querySelector(sel);if(!e)return null;var t=document.createElement('i');t.style.color='var('+v+')';document.body.appendChild(t);var want=getComputedStyle(t).color;t.remove();return [getComputedStyle(e)[prop],want]}""",[sel,prop,var])
    S['유형 줄 수']=pg.locator('.arow').count(); S['체크박스 수(진행 중 제외 완료)']=pg.locator('input[data-q]').count()
    S['체크한 유형 이어서 풀기']=pg.locator('.qgo').count()==1
    S['전체 선택/해제']=pg.locator('.qsel button').count()==2
    S['이어서 풀기 카드']=pg.locator('.rsm').count()==1
    S['학습기록 제목']=' / '.join(pg.eval_on_selector_all('.rec .rr em','e=>e.map(x=>x.innerText)'))
    S['소요시간 표시(총합+활동별)']=pg.locator('.rec .lrs>div').count()==2 and pg.locator('.rec .lrd').count()==2 and pg.locator('.rec .lrv>div').count()==3
    S['달력 날짜 눌러보기']=pg.locator('.ncg .d[data-day]').count()>0
    S['ROAD 날짜 요일']=bool(re.match(r'^\d+/\d+\([월화수목금토일]\)~\d+/\d+\([월화수목금토일]\)$',pg.locator('.wr .wd2').first.inner_text())) if pg.locator('.wr .wd2').count() else False
    road=' '.join(pg.eval_on_selector_all('.wr .wm','e=>e.map(x=>x.innerText)'))
    nums=set()
    for a,b in re.findall(r'(\d+)(?:~(\d+))?회 \(',road):
        for k in range(int(a),int(b or a)+1): nums.add(k)
    S['ROAD 회번호 연속(1~N)']=(sorted(nums)==list(range(1,max(nums)+1))) if nums else False
    S['ROAD 최대 회']=max(nums) if nums else 0
    S['회 선택 표기']=S['열린 목록 제목']
    S['ROAD 글씨 겹침 없음']=pg.evaluate("""()=>{var bad=0;document.querySelectorAll('.wr').forEach(function(w){var k=[].map.call(w.children,function(c){return c.getBoundingClientRect()});for(var i=1;i<k.length;i++){if(k[i].top<k[i-1].bottom-1&&k[i].left<k[i-1].right-1)bad++}});return bad===0}""")
    # 1회를 모두 끝낸 상태: done / now / lock 버튼이 모두 보인다
    pg.evaluate("""k=>{var o={},t=Date.now();k.forEach(function(x){o[x]={n:1,t:t}});localStorage.setItem('vhp:'+WN.school,JSON.stringify(o));localStorage.removeItem('vhbm:'+WN.school)}""",keys)
    pg.reload();pg.wait_for_timeout(500)
    st1=pg.eval_on_selector_all('.stb','e=>e.map(x=>x.className)')
    S['1회 끝내면 1회 done·2회 now']=len(st1)>1 and 'done' in st1[0].split() and 'now' in st1[1].split()
    S['끝난 버튼에 글자 끝 없음']=('끝' not in pg.inner_text('.stb.done')) if pg.locator('.stb.done').count() else False
    S['진행 알약']=pg.inner_text('.sgh span') if pg.locator('.sgh span').count() else ''
    S['풀코스 제목 글자']=pg.inner_text('.sgh b') if pg.locator('.sgh b').count() else ''
    for n,sel,props in STAGE_PROBES:
        if props=='::after':
            R[n]=pg.evaluate("""sel=>{var e=document.querySelector(sel);if(!e)return null;var c=getComputedStyle(e,'::after');return {width:c.width,height:c.height,borderRadius:c.borderTopLeftRadius,right:c.right,top:c.top}}""",sel)
        else:
            R[n]=pg.evaluate("""([sel,props])=>{var e=document.querySelector(sel);if(!e)return null;var c=getComputedStyle(e),o={};props.split(',').forEach(function(p){o[p]=c[p]});return o}""",[sel,props])
    for n,sel,prop,var in STAGE_COLORS:
        C[n]=pg.evaluate("""([sel,prop,v])=>{var e=document.querySelector(sel);if(!e)return null;var t=document.createElement('i');t.style.color='var('+v+')';document.body.appendChild(t);var want=getComputedStyle(t).color;t.remove();return [getComputedStyle(e)[prop],want]}""",[sel,prop,var])
    pg.evaluate("localStorage.removeItem('vhmx:'+WN.school)");pg.goto(base+'h/%s/mix.html'%sc);pg.wait_for_timeout(400)
    if pg.locator('#go').count():
        pg.click('#go');pg.wait_for_timeout(300)
        S['랜덤 화면 구조']=(pg.locator('.mg .arow input[type=checkbox]').count()>=2 and pg.locator('.mg .arow input:checked').count()==0 and pg.locator('.qsel button').count()==2 and pg.locator('#qgo').count()==1)
    else: S['랜덤 화면 구조']=False
    body=pg.inner_text('body')
    hit=[t for t in BAD_TEXT if t in body]+EMOJI.findall(body)
    S['금지 문구/이모지 없음']=not hit
    if hit: S['금지 목록']=hit
    return R,C,S
def main():
    args=[a for a in sys.argv[1:] if not a.startswith('--')]; dump='--dump' in sys.argv
    schools=args or SCHOOLS
    live='--live' in sys.argv
    if live: srv=None;base='https://nolbada.github.io/via-high/'
    else:
        port=free_port();srv=subprocess.Popen([sys.executable,'-m','http.server',str(port)],cwd=ROOT,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);time.sleep(1)
        base='http://localhost:%d/'%port
    fails=0;res={}
    try:
        with sync_playwright() as p:
            b=p.chromium.launch()
            for sc in ([REF]+[s for s in schools if s!=REF]):
                pg=b.new_page(viewport={'width':390,'height':844});errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
                res[sc]=measure(pg,base,sc)+(errs,);pg.close()
            b.close()
    finally:
        if srv: srv.terminate()
    ref=res[REF]
    if dump:
        print('# 기준 수치 (%s, 390px 화면)\n'%REF)
        for n,v in ref[0].items(): print('- %s: %s'%(n,json.dumps(v,ensure_ascii=False)))
        print('\n# 색 (테마 변수 연결)\n')
        for n,sel,prop,var in COLORS+STAGE_COLORS: print('- %s: %s %s = var(%s) -> %s'%(n,sel,prop,var,ref[1][n][0] if ref[1][n] else None))
        return
    for sc in schools:
        R,C,S,errs=res[sc];bad=[]
        for n in ref[0]:
            if R[n]!=ref[0][n]: bad.append('%s 수치 다름: %s (기준 %s)'%(n,R[n],ref[0][n]))
        for n in C:
            if C[n] is None or C[n][0]!=C[n][1]: bad.append('%s 색이 테마색과 다름: %s'%(n,C[n]))
        for n in ['체크한 유형 이어서 풀기','전체 선택/해제','이어서 풀기 카드','소요시간 표시(총합+활동별)','달력 날짜 눌러보기','ROAD 날짜 요일','ROAD 회번호 연속(1~N)','금지 문구/이모지 없음']:
            if not S[n]: bad.append('%s 실패 %s'%(n,S.get('금지 목록','') if n.startswith('금지') else ''))
        if S['유형 줄 수']<8: bad.append('유형 줄 수 %s'%S['유형 줄 수'])
        if not re.match(r'^1회 \(.+\)$',S['회 선택 표기']): bad.append('열린 목록 제목 형식(N회 (출처)): '+S['회 선택 표기'])
        for n in ['처음엔 회차 버튼만(목록 닫힘)','이전 회/다음 회 없음','회차 번호 1~N 이어짐','단원 뱃지 2글자','처음 상태 1회 now, 나머지 lock','누르면 목록 열림','다시 누르면 닫힘','잠긴 회차는 목록 없음','1회 끝내면 1회 done·2회 now','끝난 버튼에 글자 끝 없음']:
            if not S[n]: bad.append('v2 회차 버튼: %s 실패'%n)
        if not re.match(r'^\d+회 먼저 끝내요$|^준비 중이에요$',S['잠금 안내 문구']): bad.append('잠금 안내 문구: '+S['잠금 안내 문구'])
        if S['풀코스 제목 글자']!='유형 풀코스': bad.append('풀코스 제목: '+S['풀코스 제목 글자'])
        if not re.match(r'^%d회 중 1회$'%S['회차 버튼 수'],S['진행 알약']): bad.append('진행 알약: '+S['진행 알약'])
        if S['ROAD 최대 회'] and S['회차 버튼 수']!=S['ROAD 최대 회']: bad.append('회차 버튼 수(%s)와 ROAD 최대 회(%s)가 다름'%(S['회차 버튼 수'],S['ROAD 최대 회']))
        if not S['학습기록 제목'].startswith('누적 이용 시간 / 오늘 · ') or not re.search(r'\d+/\d+\([월화수목금토일]\)',S['학습기록 제목']): bad.append('학습기록 제목: '+S['학습기록 제목'])
        if errs: bad.append('JS 오류: %s'%errs)
        import urllib.request
        if live:
            pj=urllib.request.urlopen(base+'h/%s/parts.js?x=%d'%(sc,time.time())).read().decode('utf8')
        else: pj=open(os.path.join(ROOT,'h',sc,'parts.js'),encoding='utf8').read()
        if '(261022)' not in pj: bad.append('parts.js 이어서 풀기 코드 없음')
        if live:
            wj=urllib.request.urlopen(base+'h/%s/wrong.js?x=%d'%(sc,time.time())).read().decode('utf8')
        else: wj=open(os.path.join(ROOT,'h',sc,'wrong.js'),encoding='utf8').read()
        if 'vhmnext' not in wj: bad.append('wrong.js 랜덤 다음 유형 바 코드 없음')
        # 어휘 퀴즈: 다른 단어 문장으로 보기 채우기 금지, 보기 글씨 17px 이상
        import glob
        vb=[]
        for vp in glob.glob(os.path.join(ROOT,'h',sc,'L[34]','vocab.html')):
            vt=open(vp,encoding='utf8').read()
            if 'if(q.w!==p.w)q.items.forEach' in vt: vb.append(os.path.basename(os.path.dirname(vp))+' 다른 단어 문장으로 보기 채움')
            if 'font:600 16.5px/1.4 inherit' in vt: vb.append(os.path.basename(os.path.dirname(vp))+' 보기 글씨 지정이 무효(font 줄임식)')
        for x in vb: bad.append('어휘 퀴즈: '+x)
        # 글꼴 줄임식에 inherit를 섞으면 지정 전체가 무효 -> 학교 폴더 전체 금지
        fb=[]
        for dp,dn,fn in os.walk(os.path.join(ROOT,'h',sc)):
            if os.sep+'analysis' in dp or os.sep+'mock' in dp: continue
            for f in fn:
                if f.endswith(('.html','.js','.css')):
                    tx=open(os.path.join(dp,f),encoding='utf8').read()
                    if re.search(r'font:\d{3} [0-9.]+px(/[0-9.]+)? inherit',tx): fb.append(os.path.relpath(os.path.join(dp,f),os.path.join(ROOT,'h',sc)))
        for x in fb[:5]: bad.append('글꼴 줄임식 무효(font:... inherit): '+x)
        # 정답·해설 페이지(빠른정답 목차가 있는 모든 페이지): 같은 버튼 세트와 문항별 되돌아가기 링크
        for yp in glob.glob(os.path.join(ROOT,'h',sc,'L[34]','*.html'))+glob.glob(os.path.join(ROOT,'h',sc,'L[34]','yesang*','index.html')):
            yt=open(yp,encoding='utf8').read()
            if 'id="quick"' not in yt: continue
            rp=os.path.relpath(yp,os.path.join(ROOT,'h',sc))
            if 'id="fq"' not in yt: bad.append('정답 페이지 빠른정답 떠 있는 버튼 없음: '+rp)
            if 'class="homefab"' not in yt: bad.append('정답 페이지 목록 버튼 없음: '+rp)
            nb=len(re.findall(r'<(?:section|div) class="(?:sc|q)" id="q\d+"',yt))
            nl=len(re.findall(r'href="#(?:quick|k\d+)"',yt))
            if nb and nl<nb: bad.append('정답 페이지 문항별 되돌아가기 링크 부족(%d/%d): %s'%(nl,nb,rp))
            if 'id="fab"' in yt or 'class="fab"' in yt and 'id="fq"' in yt: bad.append('정답 페이지 빠른정답 버튼 중복: '+rp)
        # 다른 학교 이름이 학생 화면에 남는 사고 방지 (복사 잔재): 학교 폴더 안에 다른 학교 이름 금지
        NM={'geumcheon':'금천고','cheongseok':'청석고','jusung':'주성고'}
        own=sc.split('-')[0]
        for dp,dn,fn in os.walk(os.path.join(ROOT,'h',sc)):
            for f in fn:
                if f.endswith(('.html','.js')):
                    tx=open(os.path.join(dp,f),encoding='utf8').read()
                    for k,nm in NM.items():
                        if k!=own and nm in tx: bad.append('다른 학교 이름(%s)이 들어 있음: %s'%(nm,os.path.relpath(os.path.join(dp,f),os.path.join(ROOT,'h',sc))))
        for n in ['ROAD 글씨 겹침 없음','랜덤 화면 구조']:
            if not S[n]: bad.append('%s 실패'%n)
        print('%-16s %s  (유형줄 %s, 최대 %s회)'%(sc,'PASS' if not bad else 'FAIL',S['유형 줄 수'],S['ROAD 최대 회']))
        for x in bad: print('   -',x)
        fails+=bool(bad)
    sys.exit(1 if fails else 0)
main()
