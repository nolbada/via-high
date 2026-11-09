# -*- coding: utf-8 -*-
# 세트 정의: 금천고2 3과 ❸
META=dict(sch='geumcheon-go2', src='geumcheon-go2/L3/sx-data.js', pidx=2, lesson='3과', title='투표하는 방법에는 여러 가지가 있다', label='❸', page='yoyak-lian-z3')
Q = [
 dict(
  id=1,
  summary="On the day of the vote, each possible event was (A) a letter, and every council member was (B) to list the options in order of preference.",
  ko="투표 당일, 각각의 가능한 행사에 글자가 하나씩 <b>(A) 배정되었고</b>, 모든 자치회 구성원은 선택지를 선호하는 순서대로 나열하도록 <b>(B) 지시받았다</b>.",
  opts=[["assigned","directed"],["assigned","forbidden"],["removed","directed"],["removed","forbidden"],["denied","excused"]],
  optko=["배정하다 – 지시하다","배정하다 – 금지하다","제거하다 – 지시하다","제거하다 – 금지하다","거부하다 – 면제하다"],
  ans=0,
  wrong=[None,
         "forbidden(금지하다)이 틀려요. 본문은 순서대로 적으라고 시켰지(instructed, 지시했다), 못 쓰게 막지 않았어요.",
         "removed(제거하다)가 틀려요. 글자는 행사에서 빼는 게 아니라 하나씩 붙여 준(give, 주다) 거예요.",
         "둘 다 틀려요. 글자를 없앴다는 말도, 적는 걸 금지했다는 말도 본문에 없어요.",
         "둘 다 틀려요. 글자를 못 받은 행사도, 적는 일을 면제받은 사람도 본문에 없어요."],
  evid=[dict(n=1, hl=["each possible event was given a letter"]), dict(n=2, hl=["instructed to write down the options in order of preference"])],
  swaps=[["give","assign","주다 → 배정하다"],["instruct","direct","지시하다 → 지시하다, 명령하다"],["write down","list","적다 → 나열하다"]],
  swapnote="give(주다)는 시험에서 assign(배정하다)으로, instruct(지시하다)는 direct(지시하다)나 order(명령하다)로 바뀌어 나와요. 본문 단어만 찾지 말고 뜻이 같은 말을 찾으세요.",
  use=[dict(w="assign",ex="The teacher will assign a seat to each student.",ko="선생님은 학생마다 자리를 배정할 것이다."),
       dict(w="direct",ex="The coach will direct the players to run.",ko="코치는 선수들에게 달리라고 지시할 것이다.")],
  flow="본문 1번에서 행사마다 글자 A, B, C가 하나씩 주어지고, 2번에서 20명의 자치회원이 투표용지에 선호하는 순서대로 적으라고 지시를 받아요.",
 ),
 dict(
  id=2,
  summary="A member who (A) the charity concert most, then the bake sale, then the art show, would (B) CBA on the voting slip.",
  ko="자선 콘서트를 가장 <b>(A) 선호하고</b>, 그다음 빵 바자회, 그다음 미술 전시회를 선호하는 구성원은 투표용지에 CBA를 <b>(B) 기록할</b> 것이다.",
  opts=[["prefers","record"],["prefers","erase"],["avoids","record"],["avoids","erase"],["ignores","cancel"]],
  optko=["선호하다 – 기록하다","선호하다 – 지우다","피하다 – 기록하다","피하다 – 지우다","무시하다 – 취소하다"],
  ans=0,
  wrong=[None,
         "erase(지우다)가 틀려요. 본문은 CBA를 적는다(write)고 해요.",
         "avoids(피하다)가 틀려요. 자선 콘서트는 가장 먼저 고른 첫 번째 선택(first choice)이에요.",
         "둘 다 틀려요. 자선 콘서트를 피하는 것도, CBA를 지우는 것도 본문과 반대예요.",
         "둘 다 틀려요. 자선 콘서트를 무시한다는 말도, 투표를 취소한다는 말도 본문에 없어요."],
  evid=[dict(n=3, hl=["first choice, followed by the bake sale and the art show","they would write CBA"])],
  swaps=[["choice","prefer","선택 → 선호하다"],["write","record","적다 → 기록하다"],["followed by","then","뒤따르는 → 그다음"]],
  swapnote="'첫 번째 선택(first choice)'은 prefer(선호하다)로, write(적다)는 record(기록하다)로 바뀌어 나올 수 있어요. 예시 문장이라도 뜻이 같은 말로 바꿔 나와요.",
  use=[dict(w="prefer",ex="I prefer tea to coffee.",ko="나는 커피보다 차를 선호한다."),
       dict(w="record",ex="Please record your name on the list.",ko="명단에 당신의 이름을 기록해 주세요.")],
  flow="본문 3번은 예시예요. 자선 콘서트(C)가 1순위, 빵 바자회(B)가 2순위, 미술 전시회(A)가 3순위면 CBA라고 적어요. 순서가 곧 선호도예요.",
 ),
 dict(
  id=3,
  summary="After every member had (A) a vote, the slips were (B), and the results were then listed.",
  ko="모든 구성원이 투표를 <b>(A) 던진</b> 후, 투표용지는 <b>(B) 집계되었고</b>, 그다음 결과가 나열되었다.",
  opts=[["cast","tallied"],["cast","discarded"],["withdrawn","tallied"],["withdrawn","discarded"],["reversed","delayed"]],
  optko=["던지다(행사하다) – 집계하다","던지다(행사하다) – 버리다","철회하다 – 집계하다","철회하다 – 버리다","뒤집다 – 미루다"],
  ans=0,
  wrong=[None,
         "discarded(버리다)가 틀려요. 투표용지는 버려지지 않고 하나하나 세어졌어요(counted).",
         "withdrawn(철회하다)이 틀려요. 구성원들은 투표를 마쳤지(voted) 철회하지 않았어요.",
         "둘 다 틀려요. 투표를 철회했다는 말도, 용지를 버렸다는 말도 본문에 없어요.",
         "둘 다 틀려요. 투표를 뒤집거나 집계를 미뤘다는 말은 본문에 없어요."],
  evid=[dict(n=4, hl=["After every member had voted","the voting slips were counted"])],
  swaps=[["vote","cast","투표하다 → (표를) 던지다"],["count","tally","세다 → 집계하다"],["results","results","결과 → 결과"]],
  swapnote="'투표하다(vote)'는 cast a vote(표를 던지다)로, count(세다)는 tally(집계하다)로 바뀌어 나와요. 선거 기사에 자주 나오는 표현이니 꼭 익혀 두세요.",
  use=[dict(w="cast",ex="Citizens cast their votes at school.",ko="시민들은 학교에서 표를 던진다."),
       dict(w="tally",ex="Workers tally the votes after the election.",ko="직원들은 선거 후에 표를 집계한다.")],
  flow="본문 4번은 순서가 핵심이에요. 모든 구성원이 투표를 마침 → 그다음에 투표용지를 셈(집계). 5번에서 결과가 나와요.",
 ),
]

G = {
 "on":["on","~에"],"day":["day","날"],"vote":["vote","투표; 투표하다"],"each":["each","각각의"],"possible":["possible","가능한"],
 "event":["event","행사"],"was":["be","~이었다(be)"],"letter":["letter","글자, 알파벳"],"every":["every","모든"],
 "council":["council","(학생) 자치회, 위원회"],"member":["member","구성원"],"members":["member","구성원"],
 "options":["option","선택지"],"order":["order","순서"],"preference":["preference","선호"],"list":["list","나열하다; 목록"],
 "listed":["list","나열하다"],"results":["result","결과"],"result":["result","결과"],"then":["then","그다음에"],
 "assigned":["assign","배정하다"],"assign":["assign","배정하다"],"directed":["direct","지시하다"],"direct":["direct","지시하다"],
 "forbidden":["forbid","금지하다 (forbidden = 금지된)"],"removed":["remove","제거하다"],"denied":["deny","거부하다"],
 "excused":["excuse","면제하다, 봐주다"],"art":["art","미술"],"show":["show","전시회; 보여 주다"],"bake":["bake","(빵을) 굽다"],
 "sale":["sale","판매, 바자회"],"charity":["charity","자선"],"concert":["concert","콘서트"],"represented":["represent","나타내다"],
 "indicated":["indicate","나타내다, 가리키다"],"stood":["stand","서다 (stood for = ~을 의미했다)"],"given":["give","주다 (was given = 주어졌다)"],
 "voting":["voting","투표"],"slip":["slip","(종이) 용지"],"slips":["slip","(종이) 용지"],"instructed":["instruct","지시하다"],
 "write":["write","적다"],"down":["down","아래로 (write down = 적어 두다)"],"example":["example","예"],"first":["first","첫 번째의"],
 "choice":["choice","선택"],"followed":["follow","뒤따르다 (followed by = 뒤이어 ~이 오는)"],"after":["after","~한 후에"],
 "counted":["count","세다, 집계하다"],"voted":["vote","투표하다"],"cast":["cast","던지다, (표를) 행사하다"],"tallied":["tally","집계하다"],
 "tally":["tally","집계하다"],"discarded":["discard","버리다"],"withdrawn":["withdraw","철회하다"],"reversed":["reverse","뒤집다"],
 "delayed":["delay","미루다"],"prefers":["prefer","선호하다"],"prefer":["prefer","선호하다"],"record":["record","기록하다"],
 "erase":["erase","지우다"],"avoids":["avoid","피하다"],"ignores":["ignore","무시하다"],"cancel":["cancel","취소하다"],
 "most":["most","가장 (많이)"],"would":["would","~할 것이다"],"charity concert":["charity concert","자선 콘서트"],
 "possible":["possible","가능한"],"follows":["follow","뒤따르다"],"cba":["CBA","C, B, A 순서(자선 콘서트, 빵 바자회, 미술 전시회)"],
 "citizens":["citizen","시민"],"workers":["worker","직원"],"teacher":["teacher","선생님"],"coach":["coach","코치"],
 "players":["player","선수"],"seat":["seat","자리"],"student":["student","학생"],"tea":["tea","차"],"coffee":["coffee","커피"],
 "name":["name","이름"],"election":["election","선거"],"votes":["vote","표"],"school":["school","학교"],
}

JD={
 1:[["On the day of the vote,","투표 당일,"],
    ["each possible event was [[assigned]] a letter,","각각의 가능한 행사에 글자가 하나씩 [[배정되었고]],"],
    ["and every council member was [[directed]]","모든 자치회 구성원은 [[지시받았다]]"],
    ["to list the options in order of preference.","선택지를 선호하는 순서대로 나열하도록."]],
 2:[["A member who [[prefers]] the charity concert most,","자선 콘서트를 가장 [[선호하고]],"],
    ["then the bake sale, then the art show,","그다음 빵 바자회, 그다음 미술 전시회를 선호하는 구성원은"],
    ["would [[record]] CBA on the voting slip.","투표용지에 CBA를 [[기록할]] 것이다."]],
 3:[["After every member had [[cast]] a vote,","모든 구성원이 투표를 [[던진]] 후,"],
    ["the slips were [[tallied]],","투표용지는 [[집계되었고]],"],
    ["and the results were then listed.","그다음 결과가 나열되었다."]],
}

FC={
 1:[["본문 1번","행사마다 글자가 하나씩 주어졌다","미술 전시회 A, 빵 바자회 B, 자선 콘서트 C예요."],
    ["본문 2번","20명 모두 선호 순서대로 적으라고 지시받았다","투표용지에 1순위부터 차례로 적어요."],
    ["정답 포인트","{{give|주다}} = {{assign|배정하다}}, {{instruct|지시하다}} = {{direct|지시하다}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 3번","예시: 자선 콘서트가 1등이면?","C가 첫 번째 선택이에요."],
    ["순서","C 다음 B, 그다음 A","자선 콘서트 → 빵 바자회 → 미술 전시회. 그래서 CBA예요."],
    ["정답 포인트","{{first choice|첫 번째 선택}} = {{prefer|선호하다}}, {{write|적다}} = {{record|기록하다}}","예시 문장도 뜻이 같은 말로 바뀌어 나와요."]],
 3:[["본문 4번","모든 구성원이 투표를 마쳤다","투표가 먼저 끝나요."],
    ["그다음","투표용지를 센다","순서가 중요해요. 투표 끝 → 집계."],
    ["정답 포인트","{{vote|투표하다}} = {{cast|(표를) 던지다}}, {{count|세다}} = {{tally|집계하다}}","본문 5번에서 결과가 나와요."]],
}

STORY=[
 dict(a="give",form="given",n=1,sq=1,sum="each possible event was [[assigned]] a letter",hook="행사마다 알파벳이 하나씩 붙는 문장에 나온 given(give, 주다) → 요약문에서는 assigned(assign, 배정하다)로 바뀌었어요."),
 dict(a="instruct",form="instructed",n=2,sq=1,sum="every council member was [[directed]] to list the options",hook="자치회원 20명에게 순서대로 적으라고 시키는 문장의 instructed(instruct, 지시하다) → 요약문에서는 directed(direct, 지시하다)로 바뀌었어요."),
 dict(a="write",form="write",n=3,sq=2,sum="would [[record]] CBA on the voting slip",hook="자선 콘서트가 1등이면 CBA라고 적는 예시 문장의 write(적다) → 요약문에서는 record(기록하다)로 바뀌었어요."),
 dict(a="vote",form="voted",n=4,sq=3,sum="After every member had [[cast]] a vote",hook="모두 투표를 마친 뒤라는 문장의 voted(vote, 투표하다) → 요약문에서는 cast(던지다)로 바뀌었어요."),
 dict(a="count",form="counted",n=4,sq=3,sum="the slips were [[tallied]]",hook="투표용지를 세는 문장의 counted(count, 세다) → 요약문에서는 tallied(tally, 집계하다)로 바뀌었어요."),
]

SCENES=[
 dict(tag="본문 1번",ns=[1],line="투표 날, 행사마다 알파벳이 하나씩 [[given|주어졌다]]. 미술 전시회 A, 빵 바자회 B, 자선 콘서트 C."),
 dict(tag="본문 2번",ns=[2],line="자치회원 20명은 선호하는 순서대로 적으라고 [[instructed|지시받았다]]."),
 dict(tag="본문 3번",ns=[3],line="자선 콘서트가 1등이면 CBA라고 [[write|적는다]]."),
 dict(tag="본문 4번",ns=[4],line="모두 [[voted|투표하자]] 투표용지를 [[counted|세었다]]."),
]

HLKO={1:["각각의 가능한 행사에 글자가 하나씩 부여되었다"],2:["선호하는 순서대로 선택지를 적으라는 지시를 받았다"],
 3:["첫 번째 선택이고 빵 바자회와 미술 전시회가 뒤따른다면","그들은 CBA를 적을 것이다"],4:["모든 구성원이 투표를 마친 후","투표용지가 집계되었다"]}

UM={'assign':('배정하다','배정할'),'direct':('지시하다','지시할'),'prefer':('선호하다','선호한다'),'record':('기록하다','기록해'),'cast':('(표를) 던지다','던진다'),'tally':('집계하다','집계한다')}

TARGET={1:3,2:0,3:2}
