# -*- coding: utf-8 -*-
# 세트 정의: 청석고1 4과 ❺
META=dict(sch='cheongseok-go1', src='cheongseok-go1/L4/sx-data.js', pidx=4, lesson='4과', title='자연이 준 환경 해결책', label='❺', page='yoyak-lian-z5')
Q = [
 dict(
  id=1,
  summary="Coffee is (A) around the world, but its used grounds usually end up in landfills, where they can (B) a harmful greenhouse gas.",
  ko="커피는 전 세계에서 <b>(A) 인기 있지만</b>, 사용된 커피 찌꺼기는 보통 매립지로 가고, 거기에서 해로운 온실가스를 <b>(B) 만들어 낼</b> 수 있다.",
  opts=[["popular","produce"],["popular","absorb"],["rare","produce"],["rare","absorb"],["popular","remove"]],
  optko=["인기 있는 – 만들어 내다","인기 있는 – 흡수하다","드문 – 만들어 내다","드문 – 흡수하다","인기 있는 – 없애다"],
  ans=0,
  wrong=[None,
         "absorb(흡수하다)가 틀려요. 매립지의 커피 찌꺼기는 온실가스를 빨아들이는 게 아니라 만들어 내요.",
         "rare(드문)가 틀려요. 세계 사람의 30~40%가 매일 마시니까 드문 게 아니라 인기가 많아요.",
         "둘 다 틀려요. 커피는 드물지 않고, 찌꺼기는 온실가스를 흡수하지 않고 만들어 내요.",
         "remove(없애다)가 틀려요. 찌꺼기는 온실가스를 없애는 게 아니라 만들어 내요."],
  evid=[dict(n=1, hl=["thirty to forty percent of people in the world drink coffee each day"]), dict(n=3, hl=["create a harmful greenhouse gas"])],
  swaps=[["create","produce","만들다 → 만들어 내다"],["drink coffee each day","is popular","매일 커피를 마신다 → 인기 있다"],["sent to","end up in","~로 보내지다 → ~에 가게 되다"]],
  swapnote="create(만들다)는 시험에서 produce(만들어 내다), generate(발생시키다)로 바뀌어 나와요. 본문 단어만 찾지 말고 뜻이 같은 말을 찾으세요.",
  use=[dict(w="produce",ex="Cows produce a lot of gas.",ko="소는 많은 가스를 만들어 낸다."),
       dict(w="popular",ex="Coffee is popular among students.",ko="커피는 학생들 사이에서 인기가 많다.")],
  flow="본문 1번에서 전 세계 사람의 30~40%가 매일 커피를 마신다고 해요. 2~3번에서 그 찌꺼기가 매립지로 가서 해로운 온실가스를 만들 수 있다고 이어져요.",
 ),
 dict(
  id=2,
  summary="Because people cannot be stopped from drinking coffee, we can (A) greenhouse gas emissions by (B) used coffee grounds into biofuel.",
  ko="사람들이 커피 마시는 것을 막을 수 없으므로, 우리는 사용된 커피 찌꺼기를 바이오 연료로 <b>(B) 바꿈으로써</b> 온실가스 배출을 <b>(A) 줄일</b> 수 있다.",
  opts=[["decrease","converting"],["decrease","throwing"],["increase","converting"],["increase","throwing"],["postpone","adding"]],
  optko=["줄이다 – 바꾸다","줄이다 – 던지다","늘리다 – 바꾸다","늘리다 – 던지다","미루다 – 더하다"],
  ans=0,
  wrong=[None,
         "throwing(던지다)이 틀려요. 찌꺼기를 그냥 버리는 게 아니라 바이오 연료로 바꾸는 거예요.",
         "increase(늘리다)가 틀려요. 목표는 온실가스를 늘리는 게 아니라 줄이는 거예요.",
         "둘 다 틀려요. 온실가스는 늘리는 게 아니라 줄이고, 찌꺼기는 던지는 게 아니라 바꿔요.",
         "둘 다 틀려요. 온실가스 배출을 미룬다는 말도, 찌꺼기를 더한다는 말도 본문에 없어요."],
  evid=[dict(n=4, hl=["no way to stop everyone in the world from drinking coffee"]), dict(n=5, hl=["reduce greenhouse gas emissions","turning used coffee grounds into biofuel"])],
  swaps=[["reduce","decrease","줄이다 → 줄이다"],["turn","convert","바꾸다 → 전환하다, 바꾸다"],["no way to stop","cannot be stopped","막을 방법이 없다 → 막을 수 없다"]],
  swapnote="reduce(줄이다)는 decrease(줄이다), cut(줄이다)으로, turn into(~로 바꾸다)는 convert(전환하다)로 바뀌어 나와요. 반대말 increase(늘리다)와 헷갈리지 마세요.",
  use=[dict(w="decrease",ex="The number of cars will decrease next year.",ko="자동차 수가 내년에 줄어들 것이다."),
       dict(w="convert",ex="This machine can convert water into ice.",ko="이 기계는 물을 얼음으로 바꿀 수 있다.")],
  flow="본문 4번은 'Unfortunately!' 사람들이 커피를 안 마실 수는 없다는 아쉬운 이야기예요. 5번에서 However! 대신 찌꺼기를 바이오 연료로 바꿔 온실가스를 줄이자는 반전이 나와요.",
 ),
 dict(
  id=3,
  summary="Biofuel is a natural fuel made from plants or animals, and researchers (A) that algae can (B) on old coffee grounds without any added nutrients.",
  ko="바이오 연료는 식물이나 동물로 만든 천연 연료이고, 연구자들은 조류가 어떤 영양분도 더하지 않은 오래된 커피 찌꺼기에서 <b>(B) 자랄</b> 수 있다는 것을 <b>(A) 발견했다</b>.",
  opts=[["discovered","develop"],["discovered","vanish"],["doubted","develop"],["doubted","vanish"],["predicted","shrink"]],
  optko=["발견하다 – 자라다","발견하다 – 사라지다","의심하다 – 자라다","의심하다 – 사라지다","예측하다 – 줄어들다"],
  ans=0,
  wrong=[None,
         "vanish(사라지다)가 틀려요. 조류는 사라지는 게 아니라 커피 찌꺼기에서 자라요.",
         "doubted(의심하다)가 틀려요. 연구자들은 의심한 게 아니라 알아냈어요(found).",
         "둘 다 틀려요. 연구자들은 의심하지 않았고, 조류도 사라지지 않고 자라요.",
         "둘 다 틀려요. 예측했다는 말도, 조류가 줄어든다는 말도 본문에 없어요."],
  evid=[dict(n=6, hl=["natural fuel","plant or animal sources"]), dict(n=7, hl=["found","grow algae","without adding any other nutrients"])],
  swaps=[["find","discover","알아내다 → 발견하다"],["grow","develop","자라다 → 성장하다, 발달하다"],["sources","plants or animals","원료 → 식물이나 동물"]],
  swapnote="find out(알아내다)은 discover(발견하다), 때로는 realize(깨닫다)로 바뀌어 나와요. grow(자라다)는 develop(성장하다)이나 thrive(잘 자라다)로도 바뀌어요.",
  use=[dict(w="discover",ex="Scientists discovered a new kind of plant.",ko="과학자들은 새로운 종류의 식물을 발견했다."),
       dict(w="develop",ex="Small seeds develop into big trees.",ko="작은 씨앗은 큰 나무로 자란다.")],
  flow="본문 6번에서 바이오 연료가 식물이나 동물로 만든 천연 연료라고 설명해요. 7번에서 연구자들이 오래된 커피 찌꺼기에서 아무것도 더하지 않고 조류를 키울 수 있다는 걸 알아냈다고 이어져요.",
 ),
]

# 단어 사전: 표면형(소문자) -> [기본형, 이 글에서의 뜻]
G = {
 "statistics":["statistics","통계 자료"],"show":["show","보여 주다"],"about":["about","약, ~에 대해"],"thirty":["thirty","30"],
 "forty":["forty","40"],"percent":["percent","퍼센트"],"people":["people","사람들"],"world":["world","세계"],
 "drink":["drink","마시다"],"drinking":["drink","마시다"],"coffee":["coffee","커피"],"each":["each","각각의, 매~"],"day":["day","하루"],
 "coffee-making":["coffee-making","커피 만드는"],"process":["process","과정"],"however":["however","그러나"],
 "generates":["generate","발생시키다"],"used":["use","사용하다 (used = 사용된, 쓰고 난)"],"grounds":["ground","(커피) 찌꺼기"],
 "normally":["normally","보통"],"usually":["usually","보통"],"sent":["send","보내다"],"landfills":["landfill","매립지"],
 "there":["there","거기에서"],"they":["they","그것들"],"can":["can","~할 수 있다"],"create":["create","만들다"],
 "harmful":["harmful","해로운"],"greenhouse":["greenhouse","온실"],"gas":["gas","가스"],
 "unfortunately":["unfortunately","불행하게도"],"way":["way","방법"],"stop":["stop","멈추게 하다, 막다"],"everyone":["everyone","모든 사람"],
 "we":["we","우리"],"reduce":["reduce","줄이다"],"emissions":["emission","배출"],"turning":["turn","바꾸다 (turn A into B = A를 B로 바꾸다)"],
 "into":["into","~으로"],"biofuel":["biofuel","바이오 연료"],"natural":["natural","천연의, 자연의"],"fuel":["fuel","연료"],
 "made":["make","만들다"],"plant":["plant","식물"],"plants":["plant","식물"],"animal":["animal","동물"],"animals":["animal","동물"],
 "sources":["source","원료, 출처"],"researchers":["researcher","연구자"],"found":["find","알아내다, 발견하다"],
 "grow":["grow","자라게 하다, 자라다"],"algae":["algae","조류(물속에 사는 식물성 생물)"],"old":["old","오래된"],
 "without":["without","~ 없이"],"adding":["add","더하다"],"added":["add","더하다"],"any":["any","어떤 ~도"],"other":["other","다른"],
 "nutrients":["nutrient","영양분"],"popular":["popular","인기 있는"],"produce":["produce","만들어 내다"],
 "absorb":["absorb","흡수하다"],"rare":["rare","드문"],"remove":["remove","없애다"],"around":["around","~ 곳곳에서"],
 "end":["end","끝나다 (end up in = 결국 ~에 가게 되다)"],"up":["up","위로 (end up in)"],"because":["because","~ 때문에"],
 "cannot":["cannot","~할 수 없다"],"stopped":["stop","막다"],"from":["from","~로부터"],"decrease":["decrease","줄이다"],
 "increase":["increase","늘리다"],"postpone":["postpone","미루다"],"converting":["convert","전환하다, 바꾸다"],
 "convert":["convert","전환하다, 바꾸다"],"throwing":["throw","던지다"],"discovered":["discover","발견하다"],
 "discover":["discover","발견하다"],"develop":["develop","자라다, 성장하다"],"vanish":["vanish","사라지다"],
 "doubted":["doubt","의심하다"],"predicted":["predict","예측하다"],"shrink":["shrink","줄어들다"],"is":["be","~이다"],
 "a":["a","하나의"],"cows":["cow","소"],"lot":["lot","많음 (a lot of = 많은)"],"number":["number","수"],"cars":["car","자동차"],
 "next":["next","다음의"],"year":["year","해"],"machine":["machine","기계"],"water":["water","물"],"ice":["ice","얼음"],
 "students":["student","학생"],"among":["among","~ 사이에서"],"scientists":["scientist","과학자"],"new":["new","새로운"],
 "kind":["kind","종류"],"small":["small","작은"],"seeds":["seed","씨앗"],"big":["big","큰"],"trees":["tree","나무"],
 "end up":["end up","결국 ~에 가게 되다"],"will":["will","~할 것이다"],"emission":["emission","배출"],
}

# 직독직해 조각
JD={
 1:[["Coffee is [[popular]] around the world,","커피는 전 세계에서 [[인기 있지만]],"],
    ["but its used grounds usually end up in landfills,","사용된 커피 찌꺼기는 보통 매립지로 가고,"],
    ["where they can [[produce]] a harmful greenhouse gas.","거기에서 그것들은 해로운 온실가스를 [[만들어 낼]] 수 있다."]],
 2:[["Because people cannot be stopped","사람들이 막을 수 없으므로"],
    ["from drinking coffee,","커피 마시는 것을,"],
    ["we can [[decrease]] greenhouse gas emissions","우리는 온실가스 배출을 [[줄일]] 수 있다"],
    ["by [[converting]] used coffee grounds into biofuel.","사용된 커피 찌꺼기를 바이오 연료로 [[바꿈으로써]]."]],
 3:[["Biofuel is a natural fuel","바이오 연료는 천연 연료이고"],
    ["made from plants or animals,","식물이나 동물로 만든,"],
    ["and researchers [[discovered]]","연구자들은 [[발견했다]]"],
    ["that algae can [[develop]] on old coffee grounds","조류가 오래된 커피 찌꺼기에서 [[자랄]] 수 있다는 것을"],
    ["without any added nutrients.","어떤 영양분도 더하지 않고."]],
}

FC={
 1:[["본문 1번","전 세계 30~40%가 매일 커피를 마신다","그만큼 커피는 인기가 많아요."],
    ["본문 2~3번","찌꺼기는 매립지로 가서 온실가스를 만든다","거기에서 해로운 온실가스가 나올 수 있어요."],
    ["정답 포인트","{{create|만들다}} = {{produce|만들어 내다}}","{{popular|인기 있는}}은 매일 마신다는 말을 바꾼 거예요."]],
 2:[["본문 4번","Unfortunately! 커피를 못 마시게 할 방법은 없다","그래서 마시는 건 막을 수 없어요."],
    ["본문 5번","However! 찌꺼기를 바이오 연료로 바꾼다","그러면 온실가스 배출을 줄일 수 있어요."],
    ["정답 포인트","{{reduce|줄이다}} = {{decrease|줄이다}}, {{turn|바꾸다}} = {{convert|전환하다}}","반대말 {{increase|늘리다}}와 헷갈리지 마세요."]],
 3:[["본문 6번","바이오 연료는 식물이나 동물로 만든 천연 연료","바이오 연료가 무엇인지 설명해요."],
    ["본문 7번","오래된 찌꺼기에서 조류가 자란다","다른 영양분을 더하지 않아도 돼요."],
    ["정답 포인트","{{find|알아내다}} = {{discover|발견하다}}, {{grow|자라다}} = {{develop|성장하다}}","연구자들이 알아낸 사실이에요."]],
}

STORY=[
 dict(a="create",form="create",n=3,sq=1,sum="where they can [[produce]] a harmful greenhouse gas",hook="찌꺼기가 매립지에서 해로운 가스를 만든다는 문장의 create(만들다) → 요약문에서는 produce(만들어 내다)로 바꿨어요."),
 dict(a="reduce",form="reduce",n=5,sq=2,sum="we can [[decrease]] greenhouse gas emissions",hook="온실가스 배출을 줄이자는 반전 문장의 reduce(줄이다) → 요약문에서는 decrease(줄이다)로 바꿨어요."),
 dict(a="turn",form="turning",n=5,sq=2,sum="by [[converting]] used coffee grounds into biofuel",hook="찌꺼기를 연료로 바꾼다는 turning(바꾸다) → 요약문에서는 converting(전환하다)으로 바꿨어요."),
 dict(a="find",form="found",n=7,sq=3,sum="researchers [[discovered]] that algae can develop",hook="연구자들이 새 사실을 알아냈다는 found(알아냈다) → 요약문에서는 discovered(발견했다)로 바꿨어요."),
 dict(a="grow",form="grow",n=7,sq=3,sum="algae can [[develop]] on old coffee grounds",hook="낡은 찌꺼기 위에서 조류가 자란다는 grow(자라다) → 요약문에서는 develop(성장하다)으로 바꿨어요."),
]

SCENES=[
 dict(tag="본문 1~3번",ns=[1,2,3],line="전 세계가 매일 마시는 커피, 그 찌꺼기는 매립지에서 온실가스를 [[create|만든다]]."),
 dict(tag="본문 5번",ns=[5],line="찌꺼기를 바이오 연료로 [[turning|바꿔서]] 온실가스를 [[reduce|줄이자]]!"),
 dict(tag="본문 7번",ns=[7],line="연구자들이 [[found|알아냈다]]. 오래된 찌꺼기에서 조류를 [[grow|키울]] 수 있다는 것을."),
]

HLKO={1:["세계의 약 30~40%의 사람들이 매일 커피를 마신다"],3:["해로운 온실가스를 만들 수 있다"],
 4:["세계의 모든 사람들이 커피를 마시는 것을 멈추게 할 방법은 없다"],5:["온실가스 배출을 줄일 수는 있다","사용된 커피 찌꺼기를 바이오 연료로 바꿈으로써"],
 6:["천연 연료","식물이나 동물성 원료"],7:["알아냈다","조류를 자라게 할","어떤 다른 영양분도 더하지 않고"]}

UM={'produce':('만들어 내다','만들어 낸다'),'popular':('인기 있는','인기가 많다'),'decrease':('줄이다, 줄어들다','줄어들'),'convert':('전환하다, 바꾸다','바꿀'),'discover':('발견하다','발견했다'),'develop':('자라다, 성장하다','자란다')}

TARGET={1:3,2:0,3:2}
G.update({'there’s':['there is','~이(가) 있다(there’s no way = ~할 방법이 없다)']})
