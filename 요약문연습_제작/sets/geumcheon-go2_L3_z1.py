# -*- coding: utf-8 -*-
# 세트 정의: 금천고2 3과 ❶
META=dict(sch='geumcheon-go2', src='geumcheon-go2/L3/sx-data.js', pidx=0, lesson='3과', title='투표하는 방법에는 여러 가지가 있다', label='❶', page='yoyak-lian-z1')
Q = [
 dict(
  id=1,
  summary="While we make many (A) choices on our own, there are many situations in which decisions must be made (B).",
  ko="우리는 혼자서 많은 <b>(A) 개인적인</b> 선택을 하지만, 결정이 <b>(B) 집단적으로</b> 이루어져야 하는 상황도 많다.",
  opts=[["individual","collectively"],["individual","independently"],["collective","individually"],["occasional","jointly"],["trivial","collectively"]],
  optko=["개인적인 – 집단적으로","개인적인 – 독립적으로","집단적인 – 개별적으로","가끔의 – 공동으로","사소한 – 집단적으로"],
  ans=0,
  wrong=[None,
         "independently(독립적으로)가 틀려요. 본문은 우리가 집단으로(as a group) 결정해야 하는 상황이 많다고 해요.",
         "둘 다 틀려요. 방향이 뒤집혔어요. 개인 선택은 individual(개인적인), 집단 결정은 collectively(집단적으로)예요.",
         "occasional(가끔의)이 틀려요. 점심이나 직업 같은 개인 선택은 '가끔'이 아니라 일상 속 개인적인 선택이에요.",
         "trivial(사소한)이 틀려요. 본문은 선택이 사소하다고 하지 않고 개인적인(personal) 선택이라고만 해요."],
  evid=[dict(n=1, hl=["many personal choices"]), dict(n=2, hl=["we must make decisions as a group"])],
  swaps=[["personal","individual","개인적인 → 개인의, 개인적인"],["group","collectively","집단(으로서) → 집단적으로"]],
  swapnote="personal(개인적인)은 individual(개인의)로, as a group(집단으로서)은 collectively(집단적으로)나 jointly(공동으로)로 바뀌어 나와요.",
  use=[dict(w="individual",ex="Each individual student has a different goal.",ko="학생 한 명 한 명이 서로 다른 목표를 가지고 있다."),
       dict(w="collectively",ex="The members collectively decided to change the rule.",ko="구성원들은 집단적으로 그 규칙을 바꾸기로 결정했다.")],
  flow="본문 1번에서 점심, 직업 같은 개인 선택 이야기 → 2번에서 However! 집단으로 결정해야 할 때도 많다는 반전이 나와요.",
 ),
 dict(
  id=2,
  summary="Group decision-making is more (A) than personal choice because it involves many people with (B) opinions.",
  ko="집단 의사 결정은 많은 사람이 <b>(B) 서로 다른</b> 의견을 가지고 있어서 개인의 선택보다 더 <b>(A) 복잡하다</b>.",
  opts=[["complex","divergent"],["complex","unanimous"],["simple","divergent"],["effortless","unanimous"],["costly","divergent"]],
  optko=["복잡한 – 서로 갈리는","복잡한 – 만장일치의","간단한 – 서로 갈리는","수월한 – 만장일치의","돈이 많이 드는 – 서로 갈리는"],
  ans=0,
  wrong=[None,
         "unanimous(만장일치의)가 틀려요. 본문은 의견이 서로 다르다(differing)고 해요. 만장일치는 의견이 하나로 모인다는 뜻이에요.",
         "simple(간단한)이 틀려요. 본문은 집단 결정이 개인 선택만큼 간단하지 않다(not as simple)고 해요.",
         "둘 다 틀려요. 집단 결정은 수월하지도 않고, 의견이 하나로 모이지도 않아요.",
         "costly(돈이 많이 드는)가 틀려요. 본문에 돈이나 비용 이야기는 없고, 간단하지 않다는 말만 나와요."],
  evid=[dict(n=3, hl=["not as simple as our personal choices","numerous voices with differing opinions"])],
  swaps=[["simple","complex","간단한 → 복잡한 (not simple = complex)"],["differ","divergent","서로 다르다(differing) → 서로 갈리는"],["numerous","many","수많은 → 많은"],["voices","people","목소리 → 사람들"]],
  swapnote="not as simple(간단하지 않다)은 more complex(더 복잡하다)로, differing(서로 다른)은 divergent(서로 갈리는)나 different(다른)로 바뀌어 나와요. 부정 표현이 긍정 표현으로 바뀌는 점에 주의하세요.",
  use=[dict(w="complex",ex="The rules of this game are too complex for beginners.",ko="이 게임의 규칙은 초보자에게 너무 복잡하다."),
       dict(w="divergent",ex="The two groups held divergent views on the plan.",ko="두 모임은 그 계획에 대해 서로 갈리는 견해를 가졌다.")],
  flow="본문 3번은 2번의 이유예요. 집단 결정이 개인 선택보다 어려운 까닭은 서로 다른 의견을 가진 사람들의 목소리가 많이 얽혀 있기 때문이에요.",
 ),
 dict(
  id=3,
  summary="Voting is often (A) to make group decisions more equitable and efficient, and many voting (B) have been created over time.",
  ko="투표는 집단 결정을 더 공평하고 효율적으로 만들기 위해 흔히 <b>(A) 활용되며</b>, 많은 투표 <b>(B) 기법</b>이 시간이 흐르면서 만들어져 왔다.",
  opts=[["employed","techniques"],["employed","drawbacks"],["abandoned","techniques"],["abandoned","drawbacks"],["ignored","drawbacks"]],
  optko=["활용되는 – 기법","활용되는 – 단점","버려지는 – 기법","버려지는 – 단점","무시되는 – 단점"],
  ans=0,
  wrong=[None,
         "drawbacks(단점)가 틀려요. 본문은 다양한 투표 방법(methods)이 개발되었다고 해요. 단점 이야기는 없어요.",
         "abandoned(버려지는)가 틀려요. 투표는 버려지는 게 아니라 흔히 쓰이는(often used) 방법이에요.",
         "둘 다 틀려요. 투표는 버려지지 않고 널리 쓰이며, 단점이 아니라 방법이 개발되었어요.",
         "둘 다 틀려요. 투표는 무시되는 게 아니라 흔히 쓰이고, 단점이 아니라 방법이 개발되었어요."],
  evid=[dict(n=4, hl=["Voting is often used","fairer and more efficient","various voting methods have been developed"])],
  swaps=[["use","employ","사용하다 → 활용하다"],["fair","equitable","공정한 → 공평한"],["method","technique","방법 → 기법"],["developed","created","개발되다 → 만들어지다"]],
  swapnote="used(사용되는)는 employed(활용되는)로, fair(공정한)는 equitable(공평한)로, methods(방법)는 techniques(기법)로 바뀌어 나와요. 모두 같은 뜻의 짝이에요.",
  use=[dict(w="employ",ex="Many schools employ new technology in class.",ko="많은 학교가 수업에 새로운 기술을 활용한다."),
       dict(w="technique",ex="She learned a new technique for solving math problems.",ko="그녀는 수학 문제를 푸는 새로운 기법을 배웠다.")],
  flow="본문 4번은 투표를 쓰는 이유(더 공정하고 효율적으로)와 그 결과(여러 방법이 개발됨)를 말하고, 5번에서 이야기로 그 방법들을 보여 주겠다고 이어져요.",
 ),
]

# 단어 사전: 표면형(소문자) -> [기본형, 이 글에서의 뜻]
G = {
 "we":["we","우리"],"make":["make","만들다, 하다"],"many":["many","많은"],"personal":["personal","개인적인"],
 "choices":["choice","선택"],"choice":["choice","선택"],"lives":["life","삶"],"from":["from","~부터"],
 "who":["who","누구"],"lunch":["lunch","점심"],"career":["career","직업, 진로"],"pursue":["pursue","추구하다"],
 "however":["however","하지만"],"situations":["situation","상황"],"must":["must","~해야 한다"],
 "decisions":["decision","결정"],"decision":["decision","결정"],"group":["group","집단, 모임"],
 "decision-making":["decision-making","의사 결정"],"simple":["simple","간단한"],"involves":["involve","수반하다, 포함하다"],
 "numerous":["numerous","수많은"],"voices":["voice","목소리"],"differing":["differ","서로 다르다 (differing = 서로 다른)"],
 "opinions":["opinion","의견"],"voting":["vote","투표하다 (voting = 투표)"],"often":["often","흔히, 자주"],
 "used":["use","사용하다"],"fairer":["fair","공정한 (fairer = 더 공정한)"],"efficient":["efficient","효율적인"],
 "various":["various","다양한"],"methods":["method","방법"],"developed":["develop","개발하다"],"time":["time","시간"],
 "following":["following","다음의"],"story":["story","이야기"],"illustrates":["illustrate","보여주다, 설명하다"],
 "different":["different","다른"],"work":["work","작동하다, 적용되다"],"own":["own","자기 자신의"],
 "while":["while","~하는 반면"],"there":["there","거기에 (there are = ~이 있다)"],"which":["which","(관계사) 그 안에서"],
 "made":["make","만들다, 하다"],"individual":["individual","개인의, 개인적인"],"collectively":["collectively","집단적으로"],
 "independently":["independently","독립적으로"],"collective":["collective","집단의"],"individually":["individually","개별적으로"],
 "occasional":["occasional","가끔의"],"jointly":["jointly","공동으로"],"trivial":["trivial","사소한"],
 "complex":["complex","복잡한"],"divergent":["divergent","서로 갈리는, 다른"],"unanimous":["unanimous","만장일치의"],
 "effortless":["effortless","힘들지 않은, 수월한"],"costly":["costly","돈이 많이 드는"],"more":["more","더"],
 "than":["than","~보다"],"because":["because","~ 때문에"],"it":["it","그것"],"people":["people","사람들"],
 "with":["with","~을 가진"],"employed":["employ","활용하다 (employed = 활용되는)"],"employ":["employ","활용하다"],
 "techniques":["technique","기법"],"technique":["technique","기법"],"drawbacks":["drawback","단점"],
 "abandoned":["abandon","버리다 (abandoned = 버려지는)"],"ignored":["ignore","무시하다 (ignored = 무시되는)"],
 "equitable":["equitable","공평한"],"created":["create","만들어 내다"],"over":["over","~ 동안, ~에 걸쳐"],
 "group":["group","집단, 모임"],"share":["share","나누다"],"rules":["rule","규칙"],"rule":["rule","규칙"],
 "students":["student","학생"],"student":["student","학생"],"goal":["goal","목표"],"members":["member","구성원"],
 "decided":["decide","결정하다"],"change":["change","바꾸다"],"game":["game","게임"],"beginners":["beginner","초보자"],
 "too":["too","너무"],"two":["two","두 개의"],"groups":["group","모임, 집단"],"held":["hold","가지다"],
 "views":["view","견해"],"plan":["plan","계획"],"schools":["school","학교"],"technology":["technology","기술"],
 "class":["class","수업"],"learned":["learn","배우다"],"solving":["solve","풀다"],"math":["math","수학"],
 "problems":["problem","문제"],"new":["new","새로운"],"each":["each","각각의"],"has":["have","가지다"],
 "different":["different","다른"],"for":["for","~을 위해"],"in":["in","~에서"],"to":["to","~하기 위해"],
 "fair":["fair","공정한"],"method":["method","방법"],"use":["use","사용하다"],"pursue":["pursue","추구하다"],
 "difficult":["difficult","어려운"],"voters":["voter","투표자"],
}

# 직독직해 조각: [영어 조각, 한글 조각]. [[ ]] 는 빈칸에 들어간 정답 단어 표시
JD={
 1:[["While we make many [[individual]] choices on our own,","우리는 혼자서 많은 [[개인적인]] 선택을 하지만,"],
    ["there are many situations","많은 상황들이 있다"],
    ["in which decisions must be made [[collectively]].","결정이 [[집단적으로]] 이루어져야 하는."]],
 2:[["Group decision-making is more [[complex]]","집단 의사 결정은 더 [[복잡하다]]"],
    ["than personal choice","개인의 선택보다"],
    ["because it involves many people","그것이 많은 사람을 수반하기 때문에"],
    ["with [[divergent]] opinions.","[[서로 다른]] 의견을 가진."]],
 3:[["Voting is often [[employed]]","투표는 흔히 [[활용된다]]"],
    ["to make group decisions more equitable and efficient,","집단 결정을 더 공평하고 효율적으로 만들기 위해,"],
    ["and many voting [[techniques]] have been created","그리고 많은 투표 [[기법]]이 만들어져 왔다"],
    ["over time.","시간이 흐르면서."]],
}

# 기억할 흐름 카드뉴스
FC={
 1:[["본문 1번","점심, 직업 같은 개인 선택","누구와 밥 먹을지, 무슨 직업을 고를지는 내가 정해요."],
    ["본문 2번","However! 집단으로 결정할 때도 많다","{{However|하지만}}이 나오면 반전이에요. 이제 집단 이야기예요."],
    ["정답 포인트","{{personal|개인적인}} = {{individual|개인의}}, {{as a group|집단으로서}} = {{collectively|집단적으로}}","본문 표현이 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 3번","집단 결정은 개인 선택만큼 간단하지 않다","{{simple|간단한}}이 아니라는 말은 곧 복잡하다는 뜻이에요."],
    ["이유","서로 다른 의견이 수많은 목소리로 모인다","{{numerous voices|수많은 목소리}}, {{differing opinions|서로 다른 의견}}"],
    ["정답 포인트","{{not simple|간단하지 않은}} = {{complex|복잡한}}, {{differing|서로 다른}} = {{divergent|서로 갈리는}}","부정 표현이 긍정 표현으로 바뀌었어요."]],
 3:[["본문 4번","투표로 더 공정하고 효율적으로","집단 결정을 이끄는 도구가 투표예요."],
    ["결과","시간이 흐르며 다양한 투표 방법이 개발됐다","{{various|다양한}} {{methods|방법}}"],
    ["정답 포인트","{{used|사용되는}} = {{employed|활용되는}}, {{methods|방법}} = {{techniques|기법}}","{{fair|공정한}} = {{equitable|공평한}}도 함께 기억해요."]],
}

# 바꿔 말하기 스토리
STORY=[
 dict(a="personal",form="personal",n=1,sq=1,sum="many [[individual]] choices",hook="점심, 직업처럼 내가 정하는 선택을 말하는 personal(개인적인) → 요약문에서는 individual(개인의)로 바꿨어요."),
 dict(a="group",form="group",n=2,sq=1,sum="decisions must be made [[collectively]]",hook="However 뒤에서 집단으로 결정해야 한다는 말의 group(집단) → 요약문에서는 collectively(집단적으로)로 바꿨어요."),
 dict(a="differ",form="differing",n=3,sq=2,sum="with [[divergent]] opinions",hook="사람마다 생각이 다르다는 문장의 differing(서로 다른) → 요약문에서는 divergent(서로 갈리는)로 바꿨어요."),
 dict(a="use",form="used",n=4,sq=3,sum="Voting is often [[employed]]",hook="투표가 집단 결정에 쓰인다는 문장의 used(사용되는) → 요약문에서는 employed(활용되는)로 바꿨어요."),
 dict(a="fair",form="fairer",n=4,sq=3,sum="more [[equitable]] and efficient",hook="투표로 결정이 더 공정해진다는 말의 fairer(더 공정한) → 요약문에서는 equitable(공평한)로 바꿨어요."),
 dict(a="method",form="methods",n=4,sq=3,sum="many voting [[techniques]]",hook="시간이 흐르며 다양한 투표 방법이 생겼다는 말의 methods(방법) → 요약문에서는 techniques(기법)로 바꿨어요."),
]

# 줄거리 장면
SCENES=[
 dict(tag="본문 1번",ns=[1],line="점심 메뉴, 직업처럼 [[personal|개인적인]] 선택은 내가 한다."),
 dict(tag="본문 2번",ns=[2],line="하지만 [[group|집단]]으로 결정해야 하는 상황도 많다."),
 dict(tag="본문 3번",ns=[3],line="서로 [[differing|다른]] 의견이 많아서 집단 결정은 쉽지 않다."),
 dict(tag="본문 4번",ns=[4],line="투표가 [[used|쓰이면]] 결정이 [[fairer|더 공정해지고]] 다양한 [[methods|방법]]이 생겼다."),
 dict(tag="본문 5번",ns=[5],line="다음 이야기에서 그 방법들을 직접 보여 준다."),
]

# 근거 본문 한글 해석에서 영어 형광펜과 같은 자리
HLKO={1:["많은 개인적인 선택"],2:["집단으로서 결정을 내려야 하는"],3:["우리의 개인적인 선택들만큼 간단하지 않다","다른 의견을 가진 수많은 목소리"],
 4:["투표는 흔히","더 공정하고 더 효율적으로","다양한 투표 방법이 개발되어 왔다"]}

UM={'individual':('개인의, 개인적인','한 명 한 명'),'collectively':('집단적으로','집단적으로'),'complex':('복잡한','복잡하다'),'divergent':('서로 갈리는','서로 갈리는'),'employ':('활용하다','활용한다'),'technique':('기법','새로운 기법')}

TARGET={1:2,2:0,3:3}
