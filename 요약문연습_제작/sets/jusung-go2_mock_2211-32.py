# -*- coding: utf-8 -*-
# 세트 정의: 주성고2 모의고사 22년 11월 32번
META=dict(sch='jusung-go2', src='jusung-go2/mock/sx-data.js', pidx=3, lesson='22년 11월 32번', title='', label='', page='yoyak-2211-32')
Q = [
 dict(
  id=1,
  summary="The close (A) among global markets makes the economy (B) to financial failures that spread like a flu.",
  ko="전 세계 시장 사이의 긴밀한 <b>(A) 연결</b>은 경제를 독감처럼 퍼지는 금융 실패에 <b>(B) 노출되게</b> 만든다.",
  opts=[["connection","exposed"],["connection","immune"],["separation","immune"],["competition","exposed"],["separation","open"]],
  optko=["연결 – 노출된","연결 – 면역이 된","분리 – 면역이 된","경쟁 – 노출된","분리 – 열린"],
  ans=0,
  wrong=[None,
         "immune(면역이 된)이 틀려요. 본문은 시장이 감염에 취약(vulnerable)하다고 해요.",
         "둘 다 틀려요. 본문은 시장이 서로 연결(connected)되어 있어서 취약하다고 해요.",
         "competition(경쟁)이 틀려요. 본문은 경쟁이 아니라 서로 이어져 있다는 이야기예요.",
         "둘 다 틀려요. 시장이 분리(separation)되어 있다는 말은 본문과 반대예요."],
  evid=[dict(n=1, hl=["connectedness of the global economic market","vulnerable"]), dict(n=2, hl=["spreading like a flu"])],
  swaps=[["connectedness","connection","연결성 → 연결"],["vulnerable","exposed","취약한 → 노출된"],["economic market","economy","경제 시장 → 경제"]],
  swapnote="vulnerable(취약한)은 exposed(노출된), weak(약한), sensitive(민감한)로 바뀌어 나올 수 있어요.",
  use=[dict(w="connection",ex="The connection between the two cities is a long bridge.",ko="두 도시 사이의 연결은 긴 다리이다."),
       dict(w="exposed",ex="Children are exposed to a lot of ads on the internet.",ko="아이들은 인터넷에서 많은 광고에 노출된다.")],
  flow="본문 1번에서 세계 시장이 서로 연결돼 있어서 감염에 약하다고 시작하고, 2번에서 실패가 독감처럼 채무자 → 은행 → 보험사로 퍼진다고 예를 들어요.",
 ),
 dict(
  id=2,
  summary="Trouble in the market can (A) without any contact, so a bank may become (B) even if none of its investments fail.",
  ko="시장의 문제는 접촉 없이도 <b>(A) 일어날</b> 수 있어서, 은행은 투자가 하나도 실패하지 않아도 <b>(B) 파산할</b> 수 있다.",
  opts=[["happen","bankrupt"],["happen","profitable"],["stop","profitable"],["stop","bankrupt"],["disappear","successful"]],
  optko=["일어나다 – 파산한","일어나다 – 이익이 나는","멈추다 – 이익이 나는","멈추다 – 파산한","사라지다 – 성공한"],
  ans=0,
  wrong=[None,
         "profitable(이익이 나는)이 틀려요. 본문은 은행이 지급 불능(insolvent)이 될 수 있다고 해요.",
         "둘 다 틀려요. 감염은 멈추는(stop) 게 아니라 접촉 없이도 일어나요.",
         "stop(멈추다)이 틀려요. 본문은 접촉 없이도 감염이 일어난다(occur)고 해요.",
         "둘 다 틀려요. 감염이 사라진다거나 은행이 성공한다는 말은 본문에 없어요."],
  evid=[dict(n=3, hl=["unexpected characteristics"]), dict(n=4, hl=["Infection can occur even without any contact"]), dict(n=5, hl=["become insolvent","without having any of its investments fail"])],
  swaps=[["occur","happen","일어나다 → 일어나다, 벌어지다"],["insolvent","bankrupt","지급 불능의 → 파산한"],["infection","trouble","감염 → 문제"]],
  swapnote="insolvent(지급 불능의)는 처음 보면 어렵지만 bankrupt(파산한)로 바뀌어 나와요. 돈을 못 갚는 은행이라고 떠올리세요.",
  use=[dict(w="happen",ex="Strange things can happen at night.",ko="이상한 일들이 밤에 일어날 수 있다."),
       dict(w="bankrupt",ex="The shop went bankrupt after two years.",ko="그 가게는 2년 뒤에 파산했다.")],
  flow="본문 3번에서 예상 밖의 특징이 있다고 한 뒤, 4번에서 접촉 없이도 감염이 일어나고, 5번에서 투자가 실패하지 않아도 은행이 지급 불능이 될 수 있다고 이어져요.",
 ),
 dict(
  id=3,
  summary="Fear and uncertainty can be (A) to financial markets, because if people expect others to (B) their money, the bank will actually fail.",
  ko="두려움과 불확실성은 금융 시장에 <b>(A) 해로울</b> 수 있는데, 사람들이 다른 사람들이 자기 돈을 <b>(B) 인출할</b> 것이라고 예상하면 은행이 실제로 무너지기 때문이다.",
  opts=[["harmful","withdraw"],["harmful","deposit"],["helpful","deposit"],["helpful","withdraw"],["useless","borrow"]],
  optko=["해로운 – 인출하다","해로운 – 예금하다","도움이 되는 – 예금하다","도움이 되는 – 인출하다","쓸모없는 – 빌리다"],
  ans=0,
  wrong=[None,
         "deposit(예금하다)이 틀려요. 본문은 사람들이 돈을 빼 가는(pull out) 것을 무서워한다고 해요.",
         "둘 다 틀려요. 두려움은 도움이 되는 게 아니라 해롭고, 돈은 넣는 게 아니라 빼 가요.",
         "helpful(도움이 되는)이 틀려요. 본문은 두려움이 시장에 손해를 끼친다(damaging)고 해요.",
         "둘 다 틀려요. 두려움은 쓸모없는 게 아니라 해롭고, 돈을 빌린다는 말은 본문에 없어요."],
  evid=[dict(n=6, hl=["damaging to financial markets"]), dict(n=9, hl=["pull their money out"]), dict(n=10, hl=["self-fulfilling"])],
  swaps=[["damaging","harmful","손해를 끼치는 → 해로운"],["pull out","withdraw","빼내다 → 인출하다"],["expected","expect","예상했다 → 예상하다"]],
  swapnote="pull out(빼내다)은 withdraw(인출하다)로 바뀌어 나와요. 은행 이야기에서는 돈을 찾아간다는 뜻이에요.",
  use=[dict(w="harmful",ex="Too much sugar is harmful to your teeth.",ko="너무 많은 설탕은 치아에 해롭다."),
       dict(w="withdraw",ex="He went to the bank to withdraw some money.",ko="그는 돈을 조금 인출하려고 은행에 갔다.")],
  flow="본문 6번에서 두려움이 시장에 해롭다고 하고, 9번에서 다들 돈을 빼 가려 하면 나도 마지막이 되기 싫어 빼게 된다고 설명해요. 10번에서 이것을 자기충족적이라고 정리해요.",
 ),
]

G = {
 "connectedness":["connectedness","연결성"],"connection":["connection","연결"],"global":["global","전 세계의"],
 "economic":["economic","경제의"],"economy":["economy","경제"],"market":["market","시장"],"markets":["market","시장"],
 "makes":["make","~하게 만들다"],"vulnerable":["vulnerable","취약한"],"potential":["potential","잠재적인"],
 "infection":["infection","감염"],"financial":["financial","금융의, 재정적인"],"failure":["failure","실패"],
 "failures":["failure","실패"],"fail":["fail","실패하다"],"way":["way","길, 방식"],"borrowers":["borrower","채무자(돈을 빌린 사람)"],
 "banks":["bank","은행"],"bank":["bank","은행"],"insurers":["insurer","보험사"],"spreading":["spread","퍼지다"],
 "spread":["spread","퍼지다"],"like":["like","~처럼"],"flu":["flu","독감"],"however":["however","그러나"],
 "unexpected":["unexpected","예상치 못한"],"characteristics":["characteristic","특징"],"comes":["come","오다"],
 "such":["such","그러한"],"occur":["occur","일어나다"],"even":["even","심지어"],"without":["without","~ 없이"],
 "contact":["contact","접촉"],"might":["might","~일지도 모른다"],"become":["become","~이 되다"],
 "insolvent":["insolvent","지급 불능의(빚을 못 갚는)"],"having":["have","가지다"],"investments":["investment","투자"],
 "fear":["fear","두려워하다, 두려움"],"uncertainty":["uncertainty","불확실성"],"damaging":["damage","손해를 끼치다"],
 "just":["just","꼭, 단지"],"cascading":["cascade","연속해서 쏟아지다"],"due":["due to","~ 때문에"],"bad":["bad","나쁜"],
 "woke":["wake","깨다"],"tomorrow":["tomorrow","내일"],"believed":["believe","믿다"],"enough":["enough","충분한"],
 "others":["other","다른 사람들"],"collective":["collective","집단의"],"know":["know","알다"],
 "well-managed":["well-managed","잘 운영되는"],"healthy":["healthy","건전한, 건강한"],"expected":["expect","예상하다"],
 "expect":["expect","예상하다"],"pull":["pull","당기다, 빼내다"],"money":["money","돈"],"last":["last","마지막의"],
 "distress":["distress","고통, 곤경"],"self-fulfilling":["self-fulfilling","자기충족적인(믿은 대로 현실이 되는)"],
 "particularly":["particularly","특별히"],"troublesome":["troublesome","골치 아픈"],"aspect":["aspect","측면"],
 "close":["close","긴밀한"],"among":["among","~ 사이에"],"economy":["economy","경제"],"flu":["flu","독감"],
 "exposed":["expose","노출시키다 (exposed = 노출된)"],"immune":["immune","면역이 된"],"separation":["separation","분리"],
 "competition":["competition","경쟁"],"open":["open","열린"],"trouble":["trouble","문제, 어려움"],"happen":["happen","일어나다"],
 "bankrupt":["bankrupt","파산한"],"profitable":["profitable","이익이 나는"],"stop":["stop","멈추다"],
 "disappear":["disappear","사라지다"],"successful":["successful","성공한"],"harmful":["harmful","해로운"],
 "withdraw":["withdraw","인출하다"],"deposit":["deposit","예금하다"],"helpful":["helpful","도움이 되는"],
 "useless":["useless","쓸모없는"],"borrow":["borrow","빌리다"],"actually":["actually","실제로"],
 "people":["people","사람들"],"because":["because","~ 때문에"],"markets":["market","시장"],"financial":["financial","금융의"],
 "exposed":["expose","노출시키다 (exposed = 노출된)"],"children":["child","아이들"],"ads":["ad","광고"],
 "internet":["internet","인터넷"],"cities":["city","도시"],"long":["long","긴"],"bridge":["bridge","다리"],
 "strange":["strange","이상한"],"things":["thing","일"],"night":["night","밤"],"shop":["shop","가게"],
 "years":["year","년"],"went":["go","가다"],"sugar":["sugar","설탕"],"teeth":["tooth","치아"],"some":["some","조금"],
 "pull out":["pull out","빼내다"],"nothing":["nothing","아무것도 ~ 않다"],"flow":["flow","흐름"],
 "woke up":["wake up","깨다"],"fear":["fear","두려워하다"],"none":["none","하나도 ~ 않다"],"its":["it","그것의"],
 "any":["any","어떤"],"borrowers":["borrower","채무자"],"between":["between","~ 사이에"],"two":["two","둘"],
 "after":["after","~ 후에"],"too":["too","너무"],"much":["much","많은"],"teeth":["tooth","치아"],
 "trouble":["trouble","문제"],"their":["they","그들의"],"our":["we","우리의"],"bank x":["Bank X","X은행"],
}

JD={
 1:[["The close [[connection]] among global markets","전 세계 시장 사이의 긴밀한 [[연결]]은"],
    ["makes the economy [[exposed]] to financial failures","경제를 금융 실패에 [[노출되게]] 만든다"],
    ["that spread like a flu.","독감처럼 퍼지는."]],
 2:[["Trouble in the market can [[happen]]","시장의 문제는 [[일어날]] 수 있다"],
    ["without any contact,","어떤 접촉도 없이,"],
    ["so a bank may become [[bankrupt]]","그래서 은행은 [[파산할]] 수 있다"],
    ["even if none of its investments fail.","투자 중 하나도 실패하지 않아도."]],
 3:[["Fear and uncertainty can be [[harmful]] to financial markets,","두려움과 불확실성은 금융 시장에 [[해로울]] 수 있다,"],
    ["because if people expect others to [[withdraw]] their money,","사람들이 다른 이들이 자기 돈을 [[인출할]] 것이라 예상하면,"],
    ["the bank will actually fail.","은행은 실제로 무너질 것이기 때문이다."]],
}

FC={
 1:[["본문 1번","세계 시장은 서로 이어져 있다","그래서 감염(문제)에 약해요."],
    ["본문 2번","실패가 독감처럼 퍼진다","채무자 → 은행 → 보험사 순서로 번져요."],
    ["정답 포인트","{{connectedness|연결성}} = {{connection|연결}}, {{vulnerable|취약한}} = {{exposed|노출된}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 3~4번","But! 접촉 없이도 감염된다","예상 밖의 특징이에요."],
    ["본문 5번","투자가 멀쩡해도 은행이 무너진다","그런데도 지급 불능이 될 수 있어요."],
    ["정답 포인트","{{occur|일어나다}} = {{happen|일어나다}}, {{insolvent|지급 불능의}} = {{bankrupt|파산한}}","돈을 못 갚는 은행을 떠올려요."]],
 3:[["본문 6번","두려움은 시장에 해롭다","나쁜 투자만큼 위험해요."],
    ["본문 7~9번","남들이 돈을 뺀다고 믿으면 나도 뺀다","마지막이 되기 싫어서요."],
    ["정답 포인트","{{damaging|손해를 끼치는}} = {{harmful|해로운}}, {{pull out|빼내다}} = {{withdraw|인출하다}}","두려움이 현실이 되는 자기충족적 고통이에요."]],
}

STORY=[
 dict(a="connectedness",form="connectedness",n=1,sq=1,sum="The close [[connection]] among global markets",hook="세계 시장이 서로 이어져 있다는 첫 문장의 connectedness(연결성) → 요약문에서는 connection(연결)으로 바꿨어요."),
 dict(a="vulnerable",form="vulnerable",n=1,sq=1,sum="makes the economy [[exposed]] to financial failures",hook="감염에 약하다는 그 문장의 vulnerable(취약한) → 요약문에서는 exposed(노출된)로 바꿨어요."),
 dict(a="occur",form="occur",n=4,sq=2,sum="Trouble in the market can [[happen]] without any contact",hook="접촉 없이도 감염이 생긴다는 문장의 occur(일어나다) → 요약문에서는 happen(일어나다)으로 바꿨어요."),
 dict(a="insolvent",form="insolvent",n=5,sq=2,sum="so a bank may become [[bankrupt]]",hook="투자가 멀쩡한데도 은행이 돈을 못 갚게 된다는 문장의 insolvent(지급 불능의) → 요약문에서는 bankrupt(파산한)로 바뀌었어요."),
 dict(a="damaging",form="damaging",n=6,sq=3,sum="Fear and uncertainty can be [[harmful]] to financial markets",hook="두려움이 시장에 손해를 준다는 문장의 damaging(손해를 끼치는) → 요약문에서는 harmful(해로운)로 바꿨어요."),
]

SCENES=[
 dict(tag="본문 1~2번",ns=[1,2],line="세계 시장은 [[connectedness|연결성]] 때문에 [[vulnerable|취약해]], 한 곳의 실패가 독감처럼 퍼진다."),
 dict(tag="본문 4번",ns=[4],line="놀랍게도 접촉이 없어도 감염이 [[occur|일어난다]]."),
 dict(tag="본문 5번",ns=[5],line="투자가 하나도 실패하지 않아도 은행이 [[insolvent|지급 불능]]이 될 수 있다."),
 dict(tag="본문 6번",ns=[6],line="두려움과 불확실성도 시장에 [[damaging|손해를 끼친다]]."),
]

HLKO={1:["연결성","취약하게"],2:["독감처럼 퍼지면서"],3:["예상치 못한 특징들"],4:["감염이 심지어 어떤 접촉 없이도 일어날 수 있다"],
 5:["지급 불능이 될 수","투자 중 어느 하나도 실패하지 않고도"],6:["금융 시장에 손해를 끼칠 수"],9:["그들의 돈을 인출해 갈 것이라고"],10:["자기충족적일 수"]}

UM={'connection':('연결','연결'),'exposed':('노출된','노출된'),'happen':('일어나다','일어날'),'bankrupt':('파산한','파산했다'),'harmful':('해로운','해롭다'),'withdraw':('인출하다','인출하려고')}

G.update({"make":["make","만들다"],"out":["out","밖으로"],"being":["be","~이 되다"]})
TARGET={1:2,2:4,3:0}
