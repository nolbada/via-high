# -*- coding: utf-8 -*-
# 세트 정의: 주성고2 모의 22년 11월 33번
META=dict(sch='jusung-go2', src='jusung-go2/mock/sx-data.js', pidx=4, lesson='22년 11월 33번', title='', label='', page='yoyak-2211-33')
Q = [
 dict(
  id=1,
  summary="Although negative numbers are more (A) than positive numbers, we must think about them in daily life, yet many people still do not feel (B) about them.",
  ko="음수는 양수보다 더 <b>(A) 추상적</b>이지만 우리는 일상생활에서 음수를 생각해야 하는데도, 많은 사람들은 여전히 음수에 대해 <b>(B) 편안하게</b> 느끼지 못한다.",
  opts=[["intangible","comfortable"],["concrete","comfortable"],["concrete","anxious"],["intangible","anxious"],["simple","curious"]],
  optko=["만질 수 없는(추상적인) – 편안한","구체적인 – 편안한","구체적인 – 불안한","만질 수 없는(추상적인) – 불안한","단순한 – 호기심 있는"],
  ans=0,
  wrong=[None,
         "concrete(구체적인)가 틀려요. 본문은 음수가 쿠키처럼 눈에 보이지 않는 abstract(추상적인) 숫자라고 해요.",
         "둘 다 틀려요. 음수는 구체적이지 않고, 문장 끝의 do not feel(느끼지 못한다)과 anxious(불안한)를 이으면 뜻이 이상해져요.",
         "anxious(불안한)가 틀려요. 'do not feel anxious(불안하게 느끼지 않는다)'가 되어 본문과 반대예요. 본문은 음수와 편하게 지내지 못한다고 해요.",
         "둘 다 틀려요. 음수가 단순하다는 말도, 호기심 이야기도 본문에 없어요."],
  evid=[dict(n=1, hl=["more abstract than positive numbers"]), dict(n=2, hl=["haven’t quite made peace with negative numbers"])],
  swaps=[["abstract","intangible","추상적인 → 만질 수 없는, 추상적인"],["made peace with","feel comfortable about","~와 화해하다 → ~에 대해 편안하게 느끼다"],["negative numbers","negative numbers","음수 → 음수(그대로)"]],
  swapnote="abstract(추상적인)는 intangible(만질 수 없는)로 바뀌어 나올 수 있어요. 'made peace with(~와 잘 지내다)'는 'feel comfortable(편안하게 느끼다)'로 풀어 쓸 수 있어요.",
  use=[dict(w="intangible",ex="Love is an intangible thing that you cannot hold in your hand.",ko="사랑은 손에 쥘 수 없는 만질 수 없는 것이다."),
       dict(w="comfortable",ex="I feel comfortable when I talk to my best friend.",ko="나는 가장 친한 친구와 이야기할 때 편안하게 느낀다.")],
  flow="본문 1번에서 음수는 눈에 보이지 않아 추상적이라고 해요. 그래도 생각해야 한다고 하고, 2번의 Still(그런데도)에서 많은 사람이 음수와 친해지지 못했다고 이어져요.",
 ),
 dict(
  id=2,
  summary="People have come up with (A) ways to (B) the negative sign, such as printing losses in red or labeling underground floors B1 and B2.",
  ko="사람들은 손실을 빨간색으로 인쇄하거나 지하층을 B1, B2로 부르는 것처럼 음수의 기호를 <b>(B) 피하기</b> 위한 <b>(A) 창의적인</b> 방법들을 생각해 냈다.",
  opts=[["creative","avoid"],["creative","emphasize"],["costly","avoid"],["costly","emphasize"],["official","explain"]],
  optko=["창의적인 – 피하다","창의적인 – 강조하다","비용이 많이 드는 – 피하다","비용이 많이 드는 – 강조하다","공식적인 – 설명하다"],
  ans=0,
  wrong=[None,
         "emphasize(강조하다)가 틀려요. 본문은 두려운 음수 기호를 피하려는(sidestep) 방법이라고 해요.",
         "costly(비용이 많이 드는)가 틀려요. 본문의 funny little strategies(우스꽝스럽고 사소한 전략)는 돈이 아니라 꾀에 관한 이야기예요.",
         "둘 다 틀려요. 돈 이야기도 없고, 음수 기호를 강조하는 것도 아니에요.",
         "둘 다 틀려요. 공식적이라는 말은 없고, 기호를 설명하는 게 아니라 피하려는 거예요."],
  evid=[dict(n=3, hl=["funny little mental strategies","sidestep the dreaded negative sign"]), dict(n=4, hl=["printed in red"]), dict(n=6, hl=["B1 and B2"])],
  swaps=[["sidestep","avoid","피하다 → 피하다"],["strategies","ways","전략 → 방법"],["funny little","creative","우스꽝스럽고 사소한 → 창의적인"]],
  swapnote="sidestep(옆으로 비켜 피하다)은 avoid(피하다)로 바뀌어 나와요. 처음 보는 단어여도 '두려운 기호를 ~한다'는 흐름으로 뜻을 짐작하세요.",
  use=[dict(w="avoid",ex="He took a different road to avoid the traffic.",ko="그는 교통 체증을 피하려고 다른 길로 갔다."),
       dict(w="creative",ex="She came up with a creative way to save water.",ko="그녀는 물을 아끼는 창의적인 방법을 생각해 냈다.")],
  flow="본문 3번이 주제문이에요. 사람들은 두려운 음수 기호를 피하려고 별별 꾀를 냈고, 4번(빨간색·괄호), 5번(기원전), 6번(지하 B1, B2)이 그 예시예요.",
 ),
 dict(
  id=3,
  summary="Even for temperatures, many people (A) saying 5 below zero over negative 5 degrees, because the negative sign simply looks (B).",
  ko="기온에서도 많은 사람들은 음수 기호가 그저 <b>(B) 매력 없어</b> 보이기 때문에 영하 5도라고 말하는 것을 음수 5도보다 <b>(A) 선호한다</b>.",
  opts=[["avoid","pleasing"],["favor","unattractive"],["avoid","unattractive"],["favor","pleasing"],["favor","confusing"]],
  optko=["피하다 – 기분 좋은","선호하다 – 매력 없는","피하다 – 매력 없는","선호하다 – 기분 좋은","선호하다 – 헷갈리는"],
  ans=1,
  wrong=["둘 다 틀려요. 많은 사람들은 5 below zero를 더 좋아하고, 음수 기호는 보기 불쾌하다고 했어요.",
         None,
         "avoid(피하다)가 틀려요. 사람들이 피하는 건 -5 쪽이고, '5 below zero'라고 말하는 쪽은 선호해요.",
         "pleasing(기분 좋은)이 틀려요. 본문은 음수 기호가 unpleasant(불쾌한)하게 보인다고 해요.",
         "confusing(헷갈리는)이 틀려요. 본문은 헷갈린다는 말이 아니라 보기에 불쾌하다는 말이에요."],
  evid=[dict(n=7, hl=["many prefer to say 5 below zero"]), dict(n=8, hl=["looks so unpleasant"])],
  swaps=[["prefer","favor","선호하다 → 선호하다, 더 좋아하다"],["unpleasant","unattractive","불쾌한 → 매력 없는, 보기 싫은"],["say","saying","말하다 → 말하는 것"]],
  swapnote="prefer(선호하다)는 favor(선호하다)로, unpleasant(불쾌한)는 unattractive(매력 없는)나 disagreeable(불쾌한)로 바뀔 수 있어요. 긍정·부정 방향이 뒤집히지 않았는지 꼭 확인하세요.",
  use=[dict(w="favor",ex="Most students favor a shorter school day.",ko="대부분의 학생들은 더 짧은 수업 시간을 선호한다."),
       dict(w="unattractive",ex="The old building looked dull and unattractive.",ko="그 오래된 건물은 칙칙하고 매력 없어 보였다.")],
  flow="본문 7번에서 기온은 예외라고 하지만, 그때도 많은 사람이 '영하 5도'라고 말하길 선호해요. 8번에서 그 이유가 나와요. 음수 기호가 그냥 보기 불쾌하다는 거예요.",
 ),
]

G = {}
G.update({
 "negative":["negative","음수의, 부정적인"],"numbers":["number","숫자, 수"],"number":["number","숫자, 수"],
 "are":["be","~이다"],"a":["a","하나의"],"lot":["lot","많음 (a lot more = 훨씬 더)"],"more":["more","더 많은"],
 "abstract":["abstract","추상적인"],"than":["than","~보다"],"positive":["positive","양의, 긍정적인"],
 "you":["you","여러분"],"can't":["cannot","~할 수 없다"],"see":["see","보다"],"cookies":["cookie","쿠키"],
 "and":["and","그리고"],"certainly":["certainly","틀림없이"],"eat":["eat","먹다"],"them":["they","그것들"],
 "but":["but","하지만"],"can":["can","~할 수 있다"],"think":["think","생각하다"],"about":["about","~에 대해"],
 "have":["have","~해야 하다, 가지다"],"to":["to","~로, ~하기 위해"],"in":["in","~안에"],"all":["all","모든"],
 "aspects":["aspect","측면"],"of":["of","~의"],"daily":["daily","일상의"],"life":["life","생활, 삶"],
 "from":["from","~에서"],"debts":["debt","빚, 채무"],"contending":["contend","씨름하다, 맞서다"],"with":["with","~와"],
 "freezing":["freezing","몹시 추운"],"temperatures":["temperature","기온"],"parking":["parking","주차"],"garages":["garage","주차장"],
 "still":["still","그런데도, 여전히"],"many":["many","많은"],"of":["of","~의"],"us":["we","우리"],"haven't":["have not","~하지 않았다"],
 "quite":["quite","꽤, 그다지"],"made":["make","만들다 (make peace with = ~와 화해하다)"],"peace":["peace","평화, 화해"],
 "people":["people","사람들"],"invented":["invent","만들어 내다"],"sorts":["sort","종류"],"funny":["funny","우스꽝스러운"],
 "little":["little","사소한, 작은"],"mental":["mental","정신적인"],"strategies":["strategy","전략, 방법"],
 "sidestep":["sidestep","피하다"],"the":["the","그"],"dreaded":["dreaded","두려운"],"sign":["sign","기호"],
 "on":["on","~에"],"mutual":["mutual","상호의 (mutual fund = 뮤추얼 펀드)"],"fund":["fund","펀드, 기금"],"statements":["statement","명세서"],
 "losses":["loss","손실"],"printed":["print","인쇄하다"],"red":["red","빨간색"],"or":["or","또는"],
 "stuck":["stick","갇히다, 붙다 (stuck = 갇힌)"],"parentheses":["parentheses","괄호"],"no":["no","~이 없는"],
 "found":["find","발견하다"],"be":["be","~이다, ~되다"],"history":["history","역사"],"books":["book","책"],
 "tell":["tell","말해 주다"],"that":["that","~라는 것"],"born":["bear","낳다 (born = 태어난)"],"not":["not","~가 아니다"],
 "underground":["underground","지하의"],"levels":["level","층"],"often":["often","종종"],"designations":["designation","명칭"],
 "like":["like","~와 같은"],"temperatures":["temperature","기온"],"one":["one","하나"],"few":["few","몇 안 되는"],
 "exceptions":["exception","예외"],"folks":["folk","사람들"],"do":["do","하다"],"say":["say","말하다"],
 "especially":["especially","특히"],"here":["here","여기"],"degrees":["degree","도 (온도)"],"outside":["outside","바깥"],
 "though":["though","비록 ~이지만"],"even":["even","심지어"],"then":["then","그때"],"prefer":["prefer","선호하다"],
 "below":["below","~ 아래"],"zero":["zero","영(0)"],"there's":["there is","~이 있다"],"something":["something","무언가"],
 "just":["just","정말, 그저"],"looks":["look","~처럼 보이다"],"so":["so","정말"],"unpleasant":["unpleasant","불쾌한"],
 "although":["although","비록 ~이지만"],"must":["must","~해야 한다"],"yet":["yet","그런데도"],"does":["do","하다"],
 "feel":["feel","느끼다"],"intangible":["intangible","만질 수 없는, 추상적인"],"concrete":["concrete","구체적인"],
 "comfortable":["comfortable","편안한"],"anxious":["anxious","불안한"],"simple":["simple","단순한"],"curious":["curious","호기심 있는"],
 "come":["come","오다 (come up with = ~을 생각해 내다)"],"up":["up","위로"],"ways":["way","방법"],"such":["such","그런 (such as = ~와 같은)"],
 "as":["as","~처럼"],"printing":["print","인쇄하다"],"labeling":["label","이름을 붙이다"],"floors":["floor","층"],
 "creative":["creative","창의적인"],"avoid":["avoid","피하다"],"emphasize":["emphasize","강조하다"],"costly":["costly","비용이 많이 드는"],
 "official":["official","공식적인"],"explain":["explain","설명하다"],"for":["for","~에 대해"],"over":["over","~보다 (선호) "],
 "because":["because","~때문에"],"simply":["simply","그저"],"saying":["say","말하다"],"favor":["favor","선호하다"],
 "unattractive":["unattractive","매력 없는"],"pleasing":["pleasing","기분 좋은"],"confusing":["confusing","헷갈리는"],
 "julius":["Julius","율리우스"],"caesar":["Caesar","카이사르"],"b.c.":["B.C.","기원전"],"ithaca":["Ithaca","이타카(지명)"],
 "new":["new","새로운"],"york":["York","요크"],"b1":["B1","지하 1층"],"b2":["B2","지하 2층"],"-100":["-100","-100"],"-5":["-5","-5"],
 "they":["they","그들"],"their":["their","그들의"],"people":["people","사람들"],"in":["in","~안에"],"was":["be","~였다"],
 "is":["be","~이다"],"has":["have","가지다"],"it's":["it is","그것은 ~이다"],"hasn't":["have not","~하지 않았다"],
 "many":["many","많은"],"most":["most","대부분의"],"also":["also","또한"],"own":["own","자신의"],
 "us":["we","우리"],"we":["we","우리"],"4":["4","4"],"100":["100","100"],"5":["5","5"],"history":["history","역사"],
 "place":["place","장소"],"really":["really","정말"],"that’s":["that is","그것은 ~이다"],
})

JD={
 1:[["Although negative numbers are more [[intangible]] than positive numbers,","비록 음수는 양수보다 더 [[추상적이지만]],"],
    ["we must think about them in daily life,","우리는 일상생활에서 그것들을 생각해야 한다,"],
    ["yet many people still do not feel [[comfortable]] about them.","그런데도 많은 사람들은 여전히 그것들에 대해 [[편안하게]] 느끼지 못한다."]],
 2:[["People have come up with [[creative]] ways","사람들은 [[창의적인]] 방법들을 생각해 냈다"],
    ["to [[avoid]] the negative sign,","음수 기호를 [[피하기]] 위한,"],
    ["such as printing losses in red","손실을 빨간색으로 인쇄하는 것처럼"],
    ["or labeling underground floors B1 and B2.","또는 지하층을 B1, B2로 부르는 것처럼."]],
 3:[["Even for temperatures, many people [[favor]] saying 5 below zero","기온에서도 많은 사람들은 영하 5도라고 말하는 것을 [[선호한다]]"],
    ["over negative 5 degrees,","음수 5도보다,"],
    ["because the negative sign simply looks [[unattractive]].","음수 기호가 그저 [[매력 없어]] 보이기 때문에."]],
}

FC={
 1:[["본문 1번","음수는 눈에 안 보이는 추상적인 숫자","쿠키 -4개는 볼 수도 먹을 수도 없지만, 빚이나 추위처럼 생각은 해야 해요."],
    ["본문 2번","Still! 그래도 음수와 친하지 않다","많은 사람이 음수와 잘 지내지 못해요."],
    ["정답 포인트","{{abstract|추상적인}} = {{intangible|만질 수 없는}}, {{made peace|화해했다}} = {{comfortable|편안한}}","본문 표현이 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 3번","음수 기호를 피하는 꾀들","사람들은 두려운 기호를 피하려고 별별 방법을 만들어 냈어요."],
    ["본문 4~6번","빨간색, 기원전, 지하 B1","손실은 빨간색, 연도는 100 B.C., 지하층은 B1이에요."],
    ["정답 포인트","{{sidestep|피하다}} = {{avoid|피하다}}, {{strategies|전략}} = {{ways|방법}}","음수 기호를 강조하는 게 아니라 피하는 거예요."]],
 3:[["본문 7번","기온도 영하 5도라고 말하길 좋아한다","예외처럼 보여도 많은 사람이 -5 대신 5 below zero를 선호해요."],
    ["본문 8번","이유: 음수 기호는 보기 불쾌하다","그냥 보기에 별로인 느낌이 있어요."],
    ["정답 포인트","{{prefer|선호하다}} = {{favor|선호하다}}, {{unpleasant|불쾌한}} = {{unattractive|매력 없는}}","방향(좋다/싫다)이 뒤집히지 않았는지 보세요."]],
}

STORY=[
 dict(a="abstract",form="abstract",n=1,sq=1,sum="negative numbers are more [[intangible]] than positive numbers",hook="쿠키 -4개는 눈에 안 보인다는 문장의 abstract(추상적인) → 요약문에서는 intangible(만질 수 없는)로 바뀌었어요."),
 dict(a="sidestep",form="sidestep",n=3,sq=2,sum="creative ways to [[avoid]] the negative sign",hook="두려운 기호를 슬쩍 비켜 가는 문장의 sidestep(피하다) → 요약문에서는 avoid(피하다)로 바뀌었어요."),
 dict(a="prefer",form="prefer",n=7,sq=3,sum="many people [[favor]] saying 5 below zero",hook="영하 5도라고 말하길 더 좋아한다는 문장의 prefer(선호하다) → 요약문에서는 favor(선호하다)로 바뀌었어요."),
 dict(a="unpleasant",form="unpleasant",n=8,sq=3,sum="the negative sign simply looks [[unattractive]]",hook="음수 기호가 보기 싫다는 문장의 unpleasant(불쾌한) → 요약문에서는 unattractive(매력 없는)로 바뀌었어요."),
]

SCENES=[
 dict(tag="본문 1~2번",ns=[1,2],line="음수는 눈에 안 보이는 [[abstract|추상적인]] 숫자지만 생활에 꼭 필요한데, 그래도 많은 사람이 음수와 친하지 않다."),
 dict(tag="본문 3번",ns=[3],line="사람들은 음수 기호를 [[sidestep|피하려고]] 별별 꾀를 냈다."),
 dict(tag="본문 4~6번",ns=[4,5,6],line="손실은 빨간색, 연도는 기원전 100년, 지하층은 B1."),
 dict(tag="본문 7번",ns=[7],line="기온도 영하 5도라고 말하길 [[prefer|선호하는]] 사람이 많다."),
 dict(tag="본문 8번",ns=[8],line="음수 기호는 그냥 [[unpleasant|불쾌해]] 보이니까."),
]

HLKO={1:["음수는 양수보다 훨씬 더 추상적이지만"],2:["음수와 그다지 잘 지내지 못해 왔다"],
 3:["우스꽝스럽고 사소한 정신적 전략들","그 두려운 음수의 기호를 피하기 위해"],4:["빨간색으로 인쇄되거나"],6:["B1과 B2"],
 7:["많은 사람들은 영하 5도라고 말하길 선호한다"],8:["정말 불쾌하게만 보이는"]}

UM={'intangible':('만질 수 없는, 추상적인','만질 수 없는'),'comfortable':('편안한','편안하게'),'avoid':('피하다','피하려고'),'creative':('창의적인','창의적인'),'favor':('선호하다','선호한다'),'unattractive':('매력 없는','매력 없어')}

TARGET={1:0,2:3,3:1}

G.update({'can’t':['cannot','~할 수 없다'],'haven’t':['have not','~하지 않았다'],'garage':['garage','주차장'],'it’s':['it is','그것은 ~이다'],'there’s':['there is','~이 있다']})
