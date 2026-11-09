# -*- coding: utf-8 -*-
# 세트 정의: 금천고2 3과 ❹
META=dict(sch='geumcheon-go2', src='geumcheon-go2/L3/sx-data.js', pidx=3, lesson='3과', title='투표하는 방법에는 여러 가지가 있다', label='❹', page='yoyak-lian-z4')
Q = [
 dict(
  id=1,
  summary="In the FPTP method, the option with the most first-preference votes (A), while the second and third preferences are (B).",
  ko="FPTP 방식에서는 1지망 표를 가장 많이 얻은 선택지가 <b>(A) 우세하고</b>, 반면 2지망과 3지망은 <b>(B) 무시된다</b>.",
  opts=[["prevails","disregarded"],["prevails","counted"],["fails","disregarded"],["fails","counted"],["withdraws","emphasized"]],
  optko=["우세하다 – 무시되다","우세하다 – 집계되다","실패하다 – 무시되다","실패하다 – 집계되다","철회하다 – 강조되다"],
  ans=0,
  wrong=[None,
         "counted(집계되다)가 틀려요. 2지망과 3지망은 전혀 중요하지 않아서 무시돼요(ignored).",
         "fails(실패하다)가 틀려요. 표를 가장 많이 얻은 선택지는 실패하는 게 아니라 이겨요(wins).",
         "둘 다 틀려요. 표가 가장 많은 선택지는 이기고, 2지망·3지망은 세지 않고 무시돼요.",
         "둘 다 틀려요. withdraws(철회하다), emphasized(강조되다) 모두 본문에 없어요."],
  evid=[dict(n=2, hl=["the most first-preference votes wins"]), dict(n=3, hl=["they are ignored"])],
  swaps=[["win","prevail","이기다 → 우세하다, 이기다"],["ignore","disregard","무시하다 → 무시하다"],["whichever gets","the option with","무엇이든 얻는 것 → ~을 가진 선택지"]],
  swapnote="win(이기다)은 prevail(우세하다)로, ignore(무시하다)는 disregard(무시하다)로 바뀌어 나와요. 아는 단어를 어려운 단어로 바꾼 거니까 뜻을 짐작해 보세요.",
  use=[dict(w="prevail",ex="Common sense will prevail in the end.",ko="결국에는 상식이 우세할 것이다."),
       dict(w="disregard",ex="He chose to disregard the warning.",ko="그는 경고를 무시하기로 했다.")],
  flow="본문 2번에서 1지망 표를 제일 많이 받은 선택지가 이기고, 3번에서 2지망과 3지망은 아예 무시된다고 해요.",
 ),
 dict(
  id=2,
  summary="The FPTP method is (A) used in political elections around the world, and the student council quickly (B) that the charity concert would win because it earned 8 first-preference votes.",
  ko="FPTP 방식은 전 세계 정치 선거에서 <b>(A) 자주</b> 사용되며, 학생 자치회는 자선 콘서트가 8표의 1지망 표를 얻었기 때문에 이긴다고 빠르게 <b>(B) 결론지었다</b>.",
  opts=[["frequently","concluded"],["frequently","denied"],["rarely","concluded"],["rarely","denied"],["exclusively","assumed"]],
  optko=["자주 – 결론짓다","자주 – 부인하다","드물게 – 결론짓다","드물게 – 부인하다","오로지 – 가정하다"],
  ans=0,
  wrong=[None,
         "denied(부인하다)가 틀려요. 학생 자치회는 결과를 부인한 게 아니라 알아냈어요(determined).",
         "rarely(드물게)가 틀려요. 본문은 이 방식이 흔히(commonly) 쓰인다고 해요.",
         "둘 다 틀려요. 이 방식은 흔히 쓰이고, 자치회는 결과를 부인하지 않았어요.",
         "둘 다 틀려요. 이 방식이 오로지 정치 선거에서만 쓰인다는 말도, 자치회가 짐작만 했다는 말도 없어요. 표를 세어서 알아냈어요."],
  evid=[dict(n=4, hl=["commonly used in political elections"]), dict(n=5, hl=["determined"]), dict(n=6, hl=["received 8 first-preference votes"])],
  swaps=[["commonly","frequently","흔히 → 자주"],["determine","conclude","알아내다 → 결론짓다"],["receive","earn","받다 → 얻다"]],
  swapnote="commonly(흔히)는 frequently(자주)로, determine(알아내다, 결정하다)은 conclude(결론짓다)로 바뀌어 나와요. 한국어로 보면 거의 같은 말이에요.",
  use=[dict(w="frequently",ex="She frequently visits her grandmother.",ko="그녀는 할머니를 자주 방문한다."),
       dict(w="conclude",ex="The team concluded that the plan was too risky.",ko="그 팀은 그 계획이 너무 위험하다고 결론지었다.")],
  flow="본문 4번에서 이 방식이 전 세계 선거에서 흔히 쓰인다고 말한 뒤, 5~6번에서 학생 자치회 예시로 넘어가요. C가 8표로 이겼어요(A는 5표, B는 7표).",
 ),
 dict(
  id=3,
  summary="Although the FPTP method is (A) and easy to understand, it has a serious weakness: a winner can emerge without the (B) of the majority.",
  ko="FPTP 방식은 <b>(A) 간단하고</b> 이해하기 쉽지만, 심각한 약점이 있다. 과반수의 <b>(B) 지지</b> 없이도 승자가 나올 수 있다는 것이다.",
  opts=[["straightforward","backing"],["straightforward","opposition"],["complicated","backing"],["complicated","opposition"],["flawless","opposition"]],
  optko=["간단한 – 지지","간단한 – 반대","복잡한 – 지지","복잡한 – 반대","흠 없는 – 반대"],
  ans=0,
  wrong=[None,
         "opposition(반대)이 틀려요. 본문은 과반수의 지지(support) 없이도 이길 수 있다고 해요.",
         "complicated(복잡한)가 틀려요. 본문은 이 방식이 복잡하지 않고(uncomplicated) 이해하기 쉽다고 해요.",
         "둘 다 틀려요. 복잡하지 않은 방식이고, 문제는 반대가 아니라 지지가 부족하다는 점이에요.",
         "둘 다 틀려요. 약점이 있다고 했으니 흠이 없는(flawless) 방식이 아니고, 반대 이야기도 없어요."],
  evid=[dict(n=7, hl=["uncomplicated and easy to understand","significant weakness"]), dict(n=8, hl=["without the support of the majority"])],
  swaps=[["uncomplicated","straightforward","복잡하지 않은 → 간단한"],["support","backing","지지 → 지지, 후원"],["significant","serious","상당한 → 심각한"]],
  swapnote="uncomplicated(복잡하지 않은)는 straightforward(간단한)로, support(지지)는 backing(지지, 후원)으로 바뀌어 나와요. significant(상당한)도 serious(심각한)로 바뀌었어요.",
  use=[dict(w="straightforward",ex="The instructions were clear and straightforward.",ko="그 설명은 명확하고 간단했다."),
       dict(w="backing",ex="The plan won the backing of many parents.",ko="그 계획은 많은 학부모의 지지를 얻었다.")],
  flow="본문 7번에서 '쉽다, but 약점이 있다'로 방향이 꺾이고(but = 하지만), 8번에서 그 약점이 과반수 지지 없이도 이길 수 있다는 것이라고 설명해요.",
 ),
 dict(
  id=4,
  summary="Even though the charity concert won under the FPTP method, only 8 of 20 council members (A) it as their first preference, which equaled just 40% of the (B) votes.",
  ko="자선 콘서트가 FPTP 방식에서 이겼지만, 20명의 자치회 구성원 중 8명만이 그것을 1지망으로 <b>(A) 골랐고</b>, 이는 <b>(B) 전체</b> 표의 겨우 40%에 해당했다.",
  opts=[["selected","overall"],["selected","invalid"],["rejected","overall"],["rejected","invalid"],["postponed","additional"]],
  optko=["고르다 – 전체의","고르다 – 무효의","거부하다 – 전체의","거부하다 – 무효의","미루다 – 추가의"],
  ans=0,
  wrong=[None,
         "invalid(무효의)가 틀려요. 8표는 전체 표(total votes) 중 40%라고 했어요. 무효표 이야기는 없어요.",
         "rejected(거부하다)가 틀려요. 8명은 자선 콘서트를 거부한 게 아니라 1지망으로 골랐어요(chose).",
         "둘 다 틀려요. 8명은 자선 콘서트를 골랐고, 무효표 이야기는 본문에 없어요.",
         "둘 다 틀려요. 콘서트를 미뤘다는 말도, 추가 표 이야기도 본문에 없어요."],
  evid=[dict(n=10, hl=["hold a charity concert"]), dict(n=11, hl=["chose the charity concert as their first preference","40% of the total votes"])],
  swaps=[["choose","select","고르다 → 고르다, 선발하다"],["total","overall","전체의 → 전체의, 전반적인"],["equal","equal","해당하다 → 해당하다"]],
  swapnote="choose(고르다)는 select(고르다, 선발하다)로, total(전체의)은 overall(전체의, 전반적인)로 바뀌어 나와요. 숫자 40%가 어디에서 나온 값인지도 함께 확인하세요.",
  use=[dict(w="select",ex="The coach will select five players for the team.",ko="코치는 팀에 들어갈 선수 다섯 명을 선발할 것이다."),
       dict(w="overall",ex="The overall score was higher than last year.",ko="전체 점수는 작년보다 높았다.")],
  flow="본문 10번에서 자치회의 선택은 자선 콘서트였지만, 11번에서 However(하지만)로 뒤집혀요. 20명 중 8명, 즉 40%만 그걸 1지망으로 골랐어요.",
 ),
]

# 단어 사전: 표면형(소문자) -> [기본형, 이 글에서의 뜻]
G = {
 "fptp":["FPTP","FPTP(1위 한 명만 뽑는 투표 방식)"],"method":["method","방식, 방법"],"option":["option","선택지"],"options":["option","선택지"],
 "most":["most","가장 많은"],"first-preference":["first-preference","1지망의"],"votes":["vote","표"],"vote":["vote","표, 투표"],
 "prevails":["prevail","우세하다, 이기다"],"prevail":["prevail","우세하다, 이기다"],"second":["second","두 번째의"],"third":["third","세 번째의"],
 "preferences":["preference","지망, 선호"],"preference":["preference","지망, 선호"],"disregarded":["disregard","무시하다"],"disregard":["disregard","무시하다"],
 "counted":["count","집계하다, 세다"],"fails":["fail","실패하다"],"withdraws":["withdraw","철회하다"],"emphasized":["emphasize","강조하다"],
 "simplest":["simple","가장 간단한"],"three":["three","세 가지"],"voters":["voter","투표자"],"given":["give","주다"],"several":["several","여러 가지의"],
 "whichever":["whichever","어느 것이든"],"gets":["get","얻다"],"wins":["win","이기다"],"win":["win","이기다"],"won":["win","이기다"],
 "neither":["neither","어느 쪽도 ~않다"],"nor":["nor","~도 아니다"],"matters":["matter","중요하다"],"ignored":["ignore","무시하다"],
 "commonly":["commonly","흔히"],"used":["use","사용하다"],"political":["political","정치의"],"elections":["election","선거"],
 "around":["around","~ 곳곳의"],"world":["world","세계"],"student":["student","학생"],"council":["council","자치회, 위원회"],
 "quickly":["quickly","빠르게"],"determined":["determine","알아내다, 결정하다"],"winner":["winner","승자"],"charity":["charity","자선"],
 "concert":["concert","콘서트"],"received":["receive","받다"],"while":["while","반면에"],"earned":["earn","얻다"],"frequently":["frequently","자주"],
 "concluded":["conclude","결론짓다"],"denied":["deny","부인하다"],"rarely":["rarely","드물게"],"exclusively":["exclusively","오로지"],
 "assumed":["assume","가정하다, 짐작하다"],"uncomplicated":["uncomplicated","복잡하지 않은"],"easy":["easy","쉬운"],"understand":["understand","이해하다"],
 "significant":["significant","상당한, 중요한"],"weakness":["weakness","약점"],"possible":["possible","가능한"],"support":["support","지지"],
 "majority":["majority","과반수"],"although":["although","~이긴 하지만"],"straightforward":["straightforward","간단한, 복잡하지 않은"],
 "backing":["backing","지지, 후원"],"serious":["serious","심각한"],"emerge":["emerge","나타나다, 나오다"],"without":["without","~ 없이"],
 "opposition":["opposition","반대"],"complicated":["complicated","복잡한"],"flawless":["flawless","흠 없는"],"case":["case","경우"],
 "according":["according to","~에 따르면"],"results":["result","결과"],"choice":["choice","선택"],"hold":["hold","개최하다"],
 "however":["however","하지만"],"members":["member","구성원"],"chose":["choose","고르다"],"equaled":["equal","~에 해당하다, 같다"],
 "total":["total","전체의"],"selected":["select","고르다, 선발하다"],"select":["select","고르다, 선발하다"],"overall":["overall","전체의, 전반적인"],
 "invalid":["invalid","무효의"],"rejected":["reject","거부하다"],"postponed":["postpone","미루다"],"additional":["additional","추가의"],
 "even":["even","~이긴 하지만 (even though)"],"though":["though","~이긴 하지만"],"under":["under","~ 아래에서, ~ 방식으로"],
 "just":["just","겨우, 단지"],"only":["only","오직, ~만"],"common":["common","흔한"],"sense":["sense","상식, 분별력"],"end":["end","끝"],
 "chose":["choose","고르다"],"warning":["warning","경고"],"visits":["visit","방문하다"],"grandmother":["grandmother","할머니"],
 "team":["team","팀"],"plan":["plan","계획"],"risky":["risky","위험한"],"instructions":["instruction","설명, 지시"],"clear":["clear","명확한"],
 "won":["win","이기다, 얻다"],"parents":["parent","학부모"],"coach":["coach","코치"],"five":["five","다섯"],"players":["player","선수"],
 "score":["score","점수"],"higher":["high","높은"],"year":["year","해"],"last":["last","지난"],"finally":["finally","마침내"],
 "support":["support","지지"],"council’s":["council","자치회의"],"percent":["percent","퍼센트"],"members":["member","구성원"],
 "uses":["use","사용하다"],"emerges":["emerge","나오다"],
}

# 직독직해 조각
JD={
 1:[["In the FPTP method,","FPTP 방식에서는,"],
    ["the option with the most first-preference votes [[prevails]],","1지망 표를 가장 많이 얻은 선택지가 [[우세하고]],"],
    ["while the second and third preferences are [[disregarded]].","반면 2지망과 3지망은 [[무시된다]]."]],
 2:[["The FPTP method is [[frequently]] used","FPTP 방식은 [[자주]] 사용되며,"],
    ["in political elections around the world,","전 세계 정치 선거에서,"],
    ["and the student council quickly [[concluded]] that the charity concert would win","학생 자치회는 자선 콘서트가 이길 것이라고 빠르게 [[결론지었다]]"],
    ["because it earned 8 first-preference votes.","그것이 8표의 1지망 표를 얻었기 때문에."]],
 3:[["Although the FPTP method is [[straightforward]] and easy to understand,","FPTP 방식은 [[간단하고]] 이해하기 쉽지만,"],
    ["it has a serious weakness:","그것에는 심각한 약점이 있다."],
    ["a winner can emerge without the [[backing]] of the majority.","과반수의 [[지지]] 없이도 승자가 나올 수 있다는 것이다."]],
 4:[["Even though the charity concert won under the FPTP method,","자선 콘서트가 FPTP 방식에서 이겼지만,"],
    ["only 8 of 20 council members [[selected]] it as their first preference,","20명의 자치회 구성원 중 8명만이 그것을 1지망으로 [[골랐고]],"],
    ["which equaled just 40% of the [[overall]] votes.","이는 [[전체]] 표의 겨우 40%에 해당했다."]],
}

FC={
 1:[["본문 2번","1지망 표를 가장 많이 받으면 이긴다","여러 선택지 중 1등 표만 세요."],
    ["본문 3번","2지망, 3지망은 아예 안 센다","{{ignored|무시된다}} — 전혀 중요하지 않아요."],
    ["정답 포인트","{{wins|이기다}} = {{prevails|우세하다}}, {{ignored|무시되다}} = {{disregarded|무시되다}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 4번","전 세계 선거에서 흔히 쓰이는 방식","{{commonly used|흔히 사용되는}}"],
    ["본문 5~6번","학생 자치회: C가 8표로 이겼다","A는 5표, B는 7표를 받았어요."],
    ["정답 포인트","{{commonly|흔히}} = {{frequently|자주}}, {{determined|알아내다}} = {{concluded|결론짓다}}","{{receive|받다}}가 {{earn|얻다}}로 바뀌기도 했어요."]],
 3:[["본문 7번","쉽다, But 약점이 있다","{{uncomplicated|복잡하지 않은}} 방식이지만 {{significant weakness|상당한 약점}}이 있어요."],
    ["본문 8번","과반수 지지 없이도 이길 수 있다","그게 바로 이 방식의 약점이에요."],
    ["정답 포인트","{{uncomplicated|복잡하지 않은}} = {{straightforward|간단한}}, {{support|지지}} = {{backing|지지}}","{{significant|상당한}}은 {{serious|심각한}}으로 바뀌었어요."]],
 4:[["본문 10번","자치회의 선택은 자선 콘서트","FPTP 결과로는 콘서트가 이겼어요."],
    ["본문 11번","However! 20명 중 8명만 1지망이었다","{{40% of the total votes|전체 표의 40%}}밖에 안 돼요."],
    ["정답 포인트","{{chose|골랐다}} = {{selected|골랐다}}, {{total|전체의}} = {{overall|전체의}}","이긴 선택지가 과반수가 아니라는 점이 핵심이에요."]],
}

STORY=[
 dict(a="win",form="wins",n=2,sq=1,sum="the option with the most first-preference votes [[prevails]]",hook="1지망 표를 가장 많이 받은 선택지가 이긴다는 문장의 wins(이기다) → 요약문에서는 prevails(우세하다)로 바꿨어요."),
 dict(a="ignore",form="ignored",n=3,sq=1,sum="the second and third preferences are [[disregarded]]",hook="2지망과 3지망은 쓸모없어서 버려진다는 문장의 ignored(무시된) → 요약문에서는 disregarded(무시된)로 바꿨어요."),
 dict(a="commonly",form="commonly",n=4,sq=2,sum="is [[frequently]] used in political elections around the world",hook="전 세계 정치 선거에서 쓰인다는 문장의 commonly(흔히) → 요약문에서는 frequently(자주)로 바꿨어요."),
 dict(a="determine",form="determined",n=5,sq=2,sum="the student council quickly [[concluded]] that",hook="학생 자치회가 표를 세어 보고 이긴 쪽을 알아냈다는 문장의 determined(알아냈다) → 요약문에서는 concluded(결론지었다)로 바꿨어요."),
 dict(a="uncomplicated",form="uncomplicated",n=7,sq=3,sum="the FPTP method is [[straightforward]] and easy to understand",hook="복잡하지 않고 쉽다는 문장의 uncomplicated(복잡하지 않은) → 요약문에서는 straightforward(간단한)로 바꿨어요."),
 dict(a="support",form="support",n=8,sq=3,sum="without the [[backing]] of the majority",hook="과반수의 편이 되어 주는 표가 없어도 이긴다는 문장의 support(지지) → 요약문에서는 backing(지지)으로 바꿨어요."),
 dict(a="choose",form="chose",n=11,sq=4,sum="council members [[selected]] it as their first preference",hook="20명 중 8명만 콘서트를 1지망으로 골랐다는 문장의 chose(골랐다) → 요약문에서는 selected(골랐다)로 바꿨어요."),
 dict(a="total",form="total",n=11,sq=4,sum="40% of the [[overall]] votes",hook="전체 표 중 40%밖에 안 된다는 문장의 total(전체의) → 요약문에서는 overall(전체의)로 바꿨어요."),
]

SCENES=[
 dict(tag="본문 1~3번",ns=[1,2,3],line="FPTP는 가장 간단한 방식이에요. 1지망 표를 제일 많이 받은 쪽이 [[wins|이기고]], 2지망·3지망은 [[ignored|무시돼요]]."),
 dict(tag="본문 4~6번",ns=[4,5,6],line="전 세계 선거에서 [[commonly|흔히]] 쓰이는 방식이라, 학생 자치회가 써 보니 자선 콘서트(C)가 8표로 이겼다고 [[determined|알아냈어요]]."),
 dict(tag="본문 7~8번",ns=[7,8],line="[[uncomplicated|복잡하지 않아서]] 이해하기 쉽지만, 과반수의 [[support|지지]] 없이도 이길 수 있다는 약점이 있어요."),
 dict(tag="본문 11번",ns=[11],line="그런데 20명 중 8명만 콘서트를 1지망으로 [[chose|골랐어요]]. 겨우 40%, [[total|전체]] 표의 절반도 안 돼요!"),
]

HLKO={2:["가장 많은 1지망 표를 얻은 것이 이긴다"],3:["무시된다"],4:["정치 선거에서 흔히 사용된다"],5:["알아냈다"],6:["8표의 1지망 표를 받았기"],
 7:["복잡하지 않고 이해하기 쉽지만","상당한 약점"],8:["과반수의 지지 없이도"],10:["자선 콘서트를 개최하는 것"],
 11:["1지망으로 자선 콘서트를 골랐는데","전체 표의 40%"]}

UM={'prevail':('우세하다, 이기다','우세할'),'disregard':('무시하다','무시하기'),'frequently':('자주','자주'),'conclude':('결론짓다','결론지었다'),
 'straightforward':('간단한, 복잡하지 않은','간단'),'backing':('지지, 후원','지지'),'select':('고르다, 선발하다','선발할'),'overall':('전체의, 전반적인','전체')}

G.update({'win':['win','이기다'],'ignore':['ignore','무시하다'],'determine':['determine','알아내다, 결정하다'],'receive':['receive','받다'],'earn':['earn','얻다'],
 'choose':['choose','고르다'],'equal':['equal','~에 해당하다'],'conclude':['conclude','결론짓다'],'whichever':['whichever','어느 것이든'],'uncomplicated':['uncomplicated','복잡하지 않은']})

TARGET={1:3,2:0,3:4,4:1}
G.update({'because':['because','~ 때문에'],'first':['first','첫째의, 1지망의'],'out':['out of','~ 중에서']})
