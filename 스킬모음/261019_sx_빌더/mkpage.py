import json,sys
HEAD='''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#1d4ed8"><title>{title}</title>
<link rel="icon" type="image/svg+xml" href="{icon}icon.svg"><link rel="apple-touch-icon" href="{icon}icon-180.png">
<link rel="stylesheet" href="../../common/sx.css?v={ver}">
</head><body><div class="wrap"><div class="top"><a class="back" href="../index.html">← 목록</a></div>
<h1>{h1}</h1><p class="lede">{lede}</p>
<div id="mockinfo"></div>
<div class="how">{how}</div>
<div class="bar"><span id="cnt"></span><span class="sp"></span>{kbtn}<button id="rs" type="button">새 문제로 다시 풀기</button></div>
<div id="stage"></div>
<div class="foot">비타민 영어클리닉 · {school}</div></div>
<a class="homefab" href="../index.html">⌂ 목록</a>
{gate}<script src="../../common/prog.js?v={ver}"></script><script src="../../common/sx.js?v={ver}"></script>
<script src="sx-data.js?v={ver}"></script>
<script>SX.start('{app}',DATA,{{set:DATA.set,hw:DATA.hw&&DATA.hw['{app}']}});</script>
</body></html>
'''
INFO={
 'ko':('한글 순서배열','맨 위 문장 다음에 올 한글 문장 3개를 순서대로 쌓아요.','맨 위 문장 다음에 올 <b>한글 문장</b>을 순서대로 눌러 쌓고 <b>제출</b>해요. 연결어는 열쇠예요. 제출하면 이어지는 단서와 앞뒤 전체 흐름(노란 박스가 지금 푼 부분)이 나와요. 이 문제는 <b>매번 바뀌어요</b>. 풀다가 나가도 이어서 풀 수 있어요.',False),
 'abc':('순서배열 · ABC 묶음 (매번 다른 문제)','주어진 글 다음에 (A)(B)(C)의 순서를 골라요.','주어진 글 다음에 이어질 <b>(A)(B)(C)</b>의 순서를 골라 <b>제출</b>해요. 제출하면 왜 그 순서인지 단서와 전체 흐름(노란 박스)이 나와요. 이 문제는 <b>매번 바뀌어요</b>. 풀다가 나가도 이어서 풀 수 있어요.',True),
 'mun':('문장삽입 (매번 다른 문제)','주어진 문장이 들어갈 자리 ①~⑤를 골라요.','주어진 문장이 들어갈 자리 ①~⑤를 골라 <b>제출</b>해요. 제출하면 앞뒤 문장과 이어지는 단서와 전체 흐름(노란 박스)이 나와요. 이 문제는 <b>매번 바뀌어요</b>. 풀다가 나가도 이어서 풀 수 있어요.',True),
 'blank':('빈칸 추론 (매번 다른 문제)','빈칸에 들어갈 말을 골라요.','빈칸에 들어갈 말을 골라요. 고르면 정답과 해석, 그리고 이 빈칸이 글 흐름의 어디인지(노란 박스)가 나와요. 이 문제는 <b>매번 바뀌어요</b>. 풀다가 나가도 이어서 풀 수 있어요.',True),
}
def page(app,unit_title,school,ver,icon='../',gate=''):
    t,l,how,k=INFO[app]
    kbtn='<button id="kt" type="button">한글 해석 보기</button>' if k else '<button id="kt" type="button" style="display:none">한글</button>'
    return HEAD.format(title=f'{unit_title} {t}',h1=f'{unit_title} · {t}',lede=l,how=how,kbtn=kbtn,school=school,ver=ver,icon=icon,gate=gate,app=app)
