# -*- coding: utf-8 -*-
# 세트 정의: 금천고2 4과 ❺
META=dict(sch='cheongseok-go2', src='cheongseok-go2/L4/sx-data.js', pidx=4, lesson='4과', title='수리할 권리와 수리 카페', label='❺', page='yoyak-lian-z5')
Q = [
 dict(
  id=1,
  summary="In January 2021, France (A) a law requiring manufacturers to include a repairability (B) on five categories of electronic products.",
  ko="2021년 1월, 프랑스는 제조사가 다섯 가지 종류의 전자 제품에 수리 가능성 <b>(B) 등급</b>을 포함하도록 요구하는 법을 <b>(A) 제정했다</b>.",
  opts=[["enacted","rating"],["enacted","penalty"],["rejected","rating"],["rejected","penalty"],["postponed","deadline"]],
  optko=["제정하다 – 등급","제정하다 – 벌금","거부하다 – 등급","거부하다 – 벌금","연기하다 – 기한"],
  ans=0,
  wrong=[None,
         "penalty(벌금)가 틀려요. 제조사가 제품에 붙여야 하는 것은 벌금이 아니라 수리 가능성 지수(index)예요.",
         "rejected(거부하다)가 틀려요. 프랑스 정부는 법안을 거부한 게 아니라 통과시켰어요(passed).",
         "둘 다 틀려요. 법안을 거부하지 않았고, 붙이라고 한 것도 벌금이 아니에요.",
         "둘 다 틀려요. 법안을 연기한(postponed) 게 아니라 통과시켰고, 기한(deadline) 이야기도 본문에 없어요."],
  evid=[dict(n=1, hl=["repairability index","passed a bill"])],
  swaps=[["pass","enact","통과시키다 → 제정하다"],["index","rating","지수 → 등급, 평가"],["bill","law","법안 → 법"],["devices","products","장치 → 제품"]],
  swapnote="pass a bill(법안을 통과시키다)은 시험에서 enact a law(법을 제정하다)로 바뀌어 나와요. index(지수)는 rating(등급)으로도 써요.",
  use=[dict(w="enact",ex="The government enacted a new law to protect the sea.",ko="정부는 바다를 보호하기 위해 새 법을 제정했다."),
       dict(w="rating",ex="This restaurant has a high rating from visitors.",ko="이 식당은 방문객들에게 높은 평점을 받고 있다.")],
  flow="본문 1번은 이 글의 출발점이에요. 2021년 1월에 프랑스 정부가 스마트폰, 노트북 같은 다섯 종류 제품에 수리 가능성 지수를 붙이게 하는 법안을 통과시켰어요.",
 ),
 dict(
  id=2,
  summary="The index gives a score from 0 to 10 and a color label, and it (A) several (B), such as the availability of repair information and the price of spare parts.",
  ko="그 지수는 0에서 10 사이의 점수와 색깔 라벨을 주며, 수리 정보를 구할 수 있는지와 여분 부품의 가격 같은 몇 가지 <b>(B) 요소</b>를 <b>(A) 고려한다</b>.",
  opts=[["considers","factors"],["considers","rivals"],["ignores","factors"],["ignores","rivals"],["reduces","risks"]],
  optko=["고려하다 – 요소","고려하다 – 경쟁자","무시하다 – 요소","무시하다 – 경쟁자","줄이다 – 위험"],
  ans=0,
  wrong=[None,
         "rivals(경쟁자)가 틀려요. 점수에 반영되는 것은 경쟁자가 아니라 수리 정보, 분해, 부품 가격 같은 요소(elements)예요.",
         "ignores(무시하다)가 틀려요. 지수는 요소를 무시하는 게 아니라 고려해요(takes into account).",
         "둘 다 틀려요. 요소를 무시한다는 말도, 경쟁자 이야기도 본문에 없어요.",
         "둘 다 틀려요. 지수가 위험(risks)을 줄인다는 말은 본문에 없어요."],
  evid=[dict(n=3, hl=["several elements","takes into account"])],
  swaps=[["element","factor","요소 → 요인, 요소"],["take into account","consider","고려하다 → 고려하다"],["ease","simplicity","용이성 → 간단함"],["spare","extra","여분의 → 추가의"]],
  swapnote="element(요소)는 factor(요인)로, take into account(고려하다)는 consider(고려하다)로 바뀌어 나와요. 여러 단어가 한 단어로 줄기도 해요.",
  use=[dict(w="consider",ex="Please consider all the options before you decide.",ko="결정하기 전에 모든 선택지를 고려해 주세요."),
       dict(w="factor",ex="Price is an important factor when we buy shoes.",ko="신발을 살 때 가격은 중요한 요소이다.")],
  flow="본문 2~3번에서 지수를 어떻게 매기는지 나와요. 0에서 10까지 점수와 색깔 라벨로 보여 주고, 수리 정보, 분해의 쉬움, 부품 가격 같은 요소들을 고려해요.",
 ),
 dict(
  id=3,
  summary="The index was (A) to have two positive effects: it helps consumers make informed decisions, and it (B) manufacturers to make products easier to repair.",
  ko="그 지수는 두 가지 긍정적인 효과를 가지도록 <b>(A) 의도되었다</b>. 소비자가 정보에 근거한 결정을 내리도록 돕고, 제조사가 제품을 수리하기 더 쉽게 만들도록 <b>(B) 동기를 부여한다</b>.",
  opts=[["intended","motivates"],["intended","forces"],["predicted","motivates"],["predicted","forces"],["forbidden","discourages"]],
  optko=["의도하다 – 동기를 부여하다","의도하다 – 강요하다","예측하다 – 동기를 부여하다","예측하다 – 강요하다","금지하다 – 의욕을 꺾다"],
  ans=0,
  wrong=[None,
         "forces(강요하다)가 틀려요. 본문은 제조사에게 억지로 시키는 게 아니라 장려한다(encourages)고 해요.",
         "predicted(예측하다)가 틀려요. 지수는 효과를 예측한 게 아니라 효과를 위해 설계된(designed) 거예요.",
         "둘 다 틀려요. 지수는 예측된 것도 아니고, 제조사에게 강요하는 것도 아니에요.",
         "둘 다 틀려요. 금지된 것이 아니고, 의욕을 꺾는 것도 아니라 오히려 장려해요."],
  evid=[dict(n=5, hl=["designed to have two positive effects"]), dict(n=7, hl=["encourages","easier to repair"])],
  swaps=[["design","intend","설계하다 → 의도하다"],["encourage","motivate","장려하다 → 동기를 부여하다"],["allow","help","허락하다 → 돕다"],["make","produce","만들다 → 생산하다"]],
  swapnote="designed to(~하도록 설계된)는 intended to(~하도록 의도된)로, encourage(장려하다)는 motivate(동기를 부여하다)로 바뀌어 나와요.",
  use=[dict(w="intend",ex="The park was intended to be a quiet place for everyone.",ko="그 공원은 모두를 위한 조용한 장소가 되도록 의도되었다."),
       dict(w="motivate",ex="A good teacher can motivate students to study harder.",ko="좋은 선생님은 학생들이 더 열심히 공부하도록 동기를 부여할 수 있다.")],
  flow="본문 5번에서 이 지수가 두 가지 좋은 효과를 노리고 만들어졌다고 말해요. 6번은 소비자 쪽(알고 고르기), 7번은 제조사 쪽(고치기 쉬운 제품 만들기) 효과예요.",
 ),
 dict(
  id=4,
  summary="With fewer electronic items ending up in landfills, France can (A) a (B) to a more sustainable society in the near future.",
  ko="전자 제품이 쓰레기 매립지에 덜 쌓이면서, 프랑스는 가까운 미래에 더 지속 가능한 사회로의 <b>(B) 전환</b>을 <b>(A) 기대할 수 있다</b>.",
  opts=[["anticipate","shift"],["anticipate","return"],["avoid","shift"],["avoid","return"],["regret","delay"]],
  optko=["기대하다 – 전환","기대하다 – 복귀","피하다 – 전환","피하다 – 복귀","후회하다 – 지연"],
  ans=0,
  wrong=[None,
         "return(복귀)이 틀려요. 프랑스는 예전으로 돌아가는 게 아니라 더 지속 가능한 사회로 나아가요(transition).",
         "avoid(피하다)가 틀려요. 프랑스는 변화를 피하는 게 아니라 기대해요(can expect).",
         "둘 다 틀려요. 변화를 피한다는 말도, 예전으로 돌아간다는 말도 본문에 없어요.",
         "둘 다 틀려요. 후회한다거나 지연된다는 말은 본문에 없어요."],
  evid=[dict(n=8, hl=["transition to a more sustainable society","can expect"])],
  swaps=[["expect","anticipate","기대하다 → 예상하다, 기대하다"],["transition","shift","전환 → 변화, 전환"],["landfill","dump","쓰레기 매립지 → 쓰레기 버리는 곳"],["society","community","사회 → 공동체"]],
  swapnote="transition(전환)은 shift(변화)나 change(변화)로, expect(기대하다)는 anticipate(예상하다)로 바뀌어 나와요. 모두 쉬운 뜻으로 풀어서 읽어 보세요.",
  use=[dict(w="anticipate",ex="Farmers anticipate heavy rain this weekend.",ko="농부들은 이번 주말에 폭우가 올 것으로 예상한다."),
       dict(w="shift",ex="There was a big shift in people's habits after the new rule.",ko="새 규칙 이후 사람들의 습관에 큰 변화가 있었다.")],
  flow="본문 8번은 결과예요(As a result). 수리하기 쉬워지면 버려지는 전자 제품이 줄고, 그래서 프랑스는 더 지속 가능한 사회로 바뀔 것을 기대할 수 있어요.",
 ),
 dict(
  id=5,
  summary="The (A) of the index may spread far beyond France, since companies selling in France must label their products, and other countries may follow its (B) lead.",
  ko="프랑스에서 판매하는 회사는 제품에 라벨을 붙여야 하므로, 그 지수의 <b>(A) 영향</b>은 프랑스를 훨씬 넘어 퍼질 수 있고, 다른 나라들이 그 <b>(B) 획기적인</b> 선례를 따를 수도 있다.",
  opts=[["influence","groundbreaking"],["influence","outdated"],["cost","groundbreaking"],["cost","outdated"],["reputation","risky"]],
  optko=["영향 – 획기적인","영향 – 시대에 뒤떨어진","비용 – 획기적인","비용 – 시대에 뒤떨어진","평판 – 위험한"],
  ans=0,
  wrong=[None,
         "outdated(시대에 뒤떨어진)가 틀려요. 본문은 프랑스의 선례를 혁신적인(innovative) 것으로 보고 있어요.",
         "cost(비용)가 틀려요. 멀리 퍼질 것은 비용이 아니라 지수의 영향(impact)이에요.",
         "둘 다 틀려요. 퍼지는 것은 비용이 아니고, 선례도 시대에 뒤떨어진 게 아니에요.",
         "둘 다 틀려요. 평판 이야기는 본문에 없고, 선례를 위험하다고 하지도 않았어요."],
  evid=[dict(n=9, hl=["impact of the index","spread far beyond France"]), dict(n=10, hl=["label its products"]), dict(n=11, hl=["innovative lead"])],
  swaps=[["impact","influence","영향 → 영향력"],["innovative","groundbreaking","혁신적인 → 획기적인"],["sell","market","팔다 → 시장에 내놓다"],["follow","adopt","따르다 → 받아들이다"]],
  swapnote="impact(영향)는 influence(영향력)로, innovative(혁신적인)는 groundbreaking(획기적인)이나 pioneering(선구적인)으로 바뀌어 나와요.",
  use=[dict(w="influence",ex="Parents have a strong influence on their children.",ko="부모는 자녀에게 큰 영향을 미친다."),
       dict(w="groundbreaking",ex="Scientists made a groundbreaking discovery about the ocean.",ko="과학자들은 바다에 관한 획기적인 발견을 했다.")],
  flow="본문 9번에서 However(하지만)로 이야기가 넓어져요. 프랑스에서 팔려면 어느 회사든 라벨을 붙여야 하니(10번) 영향이 퍼지고, 성공하면 더 많은 나라가 따라 할 거라고(11번) 마무리해요.",
 ),
]

# 단어 사전: 표면형(소문자) -> [기본형, 이 글에서의 뜻]
G = {}
def _g(base,mean,*forms):
    for f in forms: G[f]=[base,mean]
_g("january","1월","january"); _g("france","프랑스","france","france’s","france's"); _g("law","법","law"); _g("require","요구하다","requiring","requires")
_g("manufacturer","제조사","manufacturers","manufacturer"); _g("include","포함시키다","include"); _g("repairability","수리 가능성","repairability")
_g("rating","등급, 평가","rating"); _g("category","종류, 범주","categories"); _g("electronic","전자의","electronic"); _g("product","제품","products","product")
_g("enact","제정하다","enacted"); _g("penalty","벌금, 처벌","penalty"); _g("reject","거부하다","rejected"); _g("postpone","연기하다","postponed")
_g("deadline","마감 기한","deadline"); _g("with","~와 함께, ~하면서","with")
_g("index","지수","index"); _g("give","주다","gives"); _g("score","점수","score"); _g("from","~부터","from"); _g("color","색깔","color")
_g("label","라벨, 라벨을 붙이다","label"); _g("consider","고려하다","considers","consider"); _g("several","몇 가지의","several")
_g("factor","요인, 요소","factors","factor"); _g("such as","~ 같은","such"); _g("availability","이용 가능성, 구할 수 있음","availability")
_g("repair","수리, 수리하다","repair"); _g("information","정보","information"); _g("price","가격","price"); _g("spare","여분의","spare"); _g("part","부품, 부분","parts")
_g("rival","경쟁자","rivals"); _g("ignore","무시하다","ignores"); _g("reduce","줄이다","reduces"); _g("risk","위험","risks")
_g("design","설계하다","designed"); _g("intend","의도하다","intended"); _g("positive","긍정적인","positive"); _g("effect","효과","effects")
_g("help","돕다","helps"); _g("consumer","소비자","consumers"); _g("make","만들다","make"); _g("informed","정보에 근거한","informed"); _g("decision","결정","decisions")
_g("motivate","동기를 부여하다","motivates"); _g("manufacturers","제조사","manufacturers"); _g("easier","더 쉬운","easier"); _g("predict","예측하다","predicted")
_g("force","강요하다","forces"); _g("forbid","금지하다","forbidden"); _g("discourage","의욕을 꺾다","discourages")
_g("fewer","더 적은","fewer"); _g("item","물품, 제품","items"); _g("end","끝나다 (end up in = 결국 ~에 이르다)","ending"); _g("landfill","쓰레기 매립지","landfills")
_g("anticipate","기대하다, 예상하다","anticipate"); _g("shift","변화, 전환","shift"); _g("sustainable","지속 가능한","sustainable"); _g("society","사회","society")
_g("future","미래","future"); _g("near","가까운","near"); _g("avoid","피하다","avoid"); _g("return","복귀, 되돌아감","return"); _g("regret","후회하다","regret"); _g("delay","지연","delay")
_g("more","더 ~한","more"); _g("influence","영향, 영향력","influence"); _g("spread","퍼지다","spread"); _g("far","훨씬, 멀리","far"); _g("beyond","~을 넘어","beyond")
_g("company","회사","companies"); _g("sell","팔다","selling"); _g("country","나라","countries"); _g("follow","따르다","follow"); _g("lead","선례, 앞장섬","lead")
_g("groundbreaking","획기적인","groundbreaking"); _g("outdated","시대에 뒤떨어진","outdated"); _g("cost","비용","cost"); _g("reputation","평판","reputation"); _g("risky","위험한","risky")
_g("government","정부","government"); _g("bill","법안","bill"); _g("pass","통과시키다","passed"); _g("every","모든","every"); _g("five","다섯의","five")
_g("smartphone","스마트폰","smartphones"); _g("laptop","노트북","laptops"); _g("washing machine","세탁기","washing"); _g("machine","기계","machines")
_g("television","텔레비전","televisions"); _g("lawn mower","잔디 깎는 기계","lawn","mowers"); _g("device","장치","devices"); _g("appliance","(가전) 기기","appliances")
_g("electrical","전기의","electrical"); _g("use","사용하다","using"); _g("range","범위가 ~에 이르다","ranging"); _g("color-coded","색으로 구분한","color-coded")
_g("system","시스템, 체계","system"); _g("let","~하게 해 주다","lets"); _g("easily","쉽게","easily"); _g("purchase","구입하다","purchase","purchasing")
_g("take into account","고려하다","takes"); _g("account","고려, 계산","account"); _g("element","요소","elements"); _g("disassembly","분해","disassembly"); _g("ease","쉬움, 용이성","ease")
_g("low","낮은","low"); _g("number","숫자","number"); _g("bright","밝은","bright"); _g("red","빨간","red"); _g("mean","의미하다","means"); _g("difficult","어려운","difficult")
_g("whereas","~에 반해","whereas"); _g("high","높은","high"); _g("green","초록색의","green"); _g("indicate","나타내다","indicates"); _g("firstly","첫째로","firstly")
_g("allow","허락하다, ~할 수 있게 하다","allows"); _g("new","새로운","new"); _g("secondly","둘째로","secondly"); _g("encourage","장려하다","encourages")
_g("result","결과","result"); _g("electrical","전기의","electrical"); _g("expect","기대하다","expect"); _g("transition","전환","transition"); _g("society","사회","society")
_g("impact","영향","impact"); _g("likely","~할 가능성이 있는","likely"); _g("however","하지만","however"); _g("live","살다","live"); _g("global","세계적인","global")
_g("economy","경제","economy"); _g("want","원하다","wants"); _g("market","시장","market"); _g("according","~에 따라 (according to)","according"); _g("need","필요가 있다","need")
_g("successful","성공적인","successful"); _g("around","~ 곳곳의","around"); _g("world","세계","world"); _g("innovative","혁신적인","innovative")
_g("seeing","보다","seeing"); _g("see","보다, 알다","see"); _g("before","~하기 전에","before"); _g("they","그들","they"); _g("other","다른","other")
_g("must","~해야 한다","must"); _g("may","~할 수도 있다","may"); _g("since","~이므로","since"); _g("their","그들의","their"); _g("its","그것의","its")
_g("because","~ 때문에","because"); _g("easy","쉬운","easy"); _g("year","해, 년","year"); _g("many","많은","many")
_g("inspect","면밀히 조사하다","inspect"); _g("fix","고치다","fix","fixed"); _g("simplicity","간단함","simplicity"); _g("extra","추가의","extra"); _g("community","공동체","community")
_g("dump","쓰레기 버리는 곳","dump"); _g("adopt","받아들이다","adopt"); _g("produce","생산하다","produce"); _g("protect","보호하다","protect"); _g("sea","바다","sea")
_g("restaurant","식당","restaurant"); _g("high","높은","high"); _g("visitor","방문객","visitors"); _g("option","선택지","options"); _g("decide","결정하다","decide")
_g("important","중요한","important"); _g("shoes","신발","shoes"); _g("buy","사다","buy"); _g("park","공원","park"); _g("quiet","조용한","quiet"); _g("place","장소","place")
_g("teacher","선생님","teacher"); _g("student","학생","students"); _g("study","공부하다","study"); _g("harder","더 열심히","harder"); _g("parent","부모","parents")
_g("child","자녀, 아이","children"); _g("scientist","과학자","scientists"); _g("discovery","발견","discovery"); _g("ocean","바다, 대양","ocean")
_g("farmer","농부","farmers"); _g("heavy","심한","heavy"); _g("rain","비","rain"); _g("weekend","주말","weekend"); _g("habit","습관","habits"); _g("rule","규칙","rule")
_g("big","큰","big"); _g("strong","강한","strong"); _g("good","좋은","good"); _g("test","시험","test"); _g("paper","종이, 시험지","paper")
_g("carefully","꼼꼼히","carefully"); _g("every","모든","every")

JD={
 1:[["In January 2021, France [[enacted]] a law","2021년 1월, 프랑스는 법을 [[제정했다]]"],
    ["requiring manufacturers to include","제조사가 포함하도록 요구하는"],
    ["a repairability [[rating]]","수리 가능성 [[등급]]을"],
    ["on five categories of electronic products.","다섯 가지 종류의 전자 제품에."]],
 2:[["The index gives a score from 0 to 10 and a color label,","그 지수는 0에서 10 사이의 점수와 색깔 라벨을 주며,"],
    ["and it [[considers]] several [[factors]],","몇 가지 [[요소]]를 [[고려한다]],"],
    ["such as the availability of repair information","수리 정보를 구할 수 있는지와"],
    ["and the price of spare parts.","여분 부품의 가격 같은."]],
 3:[["The index was [[intended]] to have two positive effects:","그 지수는 두 가지 긍정적인 효과를 가지도록 [[의도되었다]]:"],
    ["it helps consumers make informed decisions,","소비자가 정보에 근거한 결정을 내리도록 돕고,"],
    ["and it [[motivates]] manufacturers","제조사에게 [[동기를 부여한다]]"],
    ["to make products easier to repair.","제품을 수리하기 더 쉽게 만들도록."]],
 4:[["With fewer electronic items ending up in landfills,","전자 제품이 쓰레기 매립지에 덜 쌓이면서,"],
    ["France can [[anticipate]] a [[shift]]","프랑스는 [[전환]]을 [[기대할 수 있다]]"],
    ["to a more sustainable society","더 지속 가능한 사회로의"],
    ["in the near future.","가까운 미래에."]],
 5:[["The [[influence]] of the index may spread far beyond France,","그 지수의 [[영향]]은 프랑스를 훨씬 넘어 퍼질 수 있고,"],
    ["since companies selling in France must label their products,","프랑스에서 판매하는 회사는 제품에 라벨을 붙여야 하므로,"],
    ["and other countries may follow","다른 나라들이 따를 수도 있다"],
    ["its [[groundbreaking]] lead.","그 [[획기적인]] 선례를."]],
}

FC={
 1:[["본문 1번","프랑스가 새 법안을 통과시켰다","2021년 1월, 제조사에게 지수를 붙이라고 요구하는 법이에요."],
    ["대상","스마트폰, 노트북, 세탁기, TV, 잔디 깎는 기계","다섯 가지 전자 제품에 붙어요."],
    ["정답 포인트","{{pass a bill|법안을 통과시키다}} = {{enact a law|법을 제정하다}}","{{index|지수}} = {{rating|등급}}으로 바뀌어요."]],
 2:[["본문 2번","0~10점 + 색깔 라벨","소비자가 제품을 사기 전에 수리가 쉬운지 알 수 있어요."],
    ["본문 3번","무엇을 고려할까?","수리 정보, 분해의 쉬움, 부품 가격이에요."],
    ["정답 포인트","{{takes into account|고려하다}} = {{considers|고려하다}}, {{elements|요소}} = {{factors|요인}}","고려하는 것은 경쟁자가 아니라 수리와 관련된 요인이에요."]],
 3:[["본문 5번","지수는 두 가지 좋은 효과를 노렸다","그래서 만들어진 거예요."],
    ["본문 6~7번","소비자는 똑똑하게 고르고, 제조사는 고치기 쉬운 제품을 만든다","Firstly, Secondly로 두 효과를 나눠 말해요."],
    ["정답 포인트","{{designed|설계된}} = {{intended|의도된}}, {{encourages|장려하다}} = {{motivates|동기를 부여하다}}","강요하는 것이 아니라 장려해요."]],
 4:[["본문 8번","As a result! 결과가 나온다","수리하기 쉬운 제품이 늘어요."],
    ["그다음","버려지는 전자 제품이 줄어든다","{{landfills|쓰레기 매립지}}에 쌓이는 물건이 줄어요."],
    ["정답 포인트","{{expect|기대하다}} = {{anticipate|예상하다}}, {{transition|전환}} = {{shift|변화}}","더 지속 가능한 사회로 나아가는 방향이에요."]],
 5:[["본문 9번","However! 영향은 프랑스 밖으로","{{impact|영향}}가 멀리 퍼질 가능성이 있어요."],
    ["본문 10번","프랑스에서 팔려면 라벨 필수","세계 경제 속에서 모든 회사가 따라야 해요."],
    ["정답 포인트","{{impact|영향}} = {{influence|영향력}}, {{innovative|혁신적인}} = {{groundbreaking|획기적인}}","다른 나라들이 따를 수도 있어요."]],
}

STORY=[
 dict(a="pass",form="passed",n=1,sq=1,sum="France [[enacted]] a law requiring manufacturers",hook="프랑스 정부가 법안을 통과시켰다는 첫 문장의 passed(통과시켰다) → 요약문에서는 enacted(제정했다)로 바꿨어요."),
 dict(a="index",form="index",n=1,sq=1,sum="a repairability [[rating]] on five categories",hook="제품에 붙이는 수리 가능성 index(지수) → 요약문에서는 rating(등급)으로 바꿨어요."),
 dict(a="element",form="elements",n=3,sq=2,sum="it considers several [[factors]], such as the availability",hook="수리 정보, 분해, 부품 가격 같은 elements(요소) → 요약문에서는 factors(요인)로 바꿨어요."),
 dict(a="design",form="designed",n=5,sq=3,sum="The index was [[intended]] to have two positive effects",hook="두 가지 좋은 효과를 노리고 만들었다는 designed(설계되었다) → 요약문에서는 intended(의도되었다)로 바꿨어요."),
 dict(a="encourage",form="encourages",n=7,sq=3,sum="it [[motivates]] manufacturers to make products",hook="제조사가 고치기 쉬운 제품을 만들도록 북돋는 encourages(장려한다) → 요약문에서는 motivates(동기를 부여한다)로 바꿨어요."),
 dict(a="expect",form="expect",n=8,sq=4,sum="France can [[anticipate]] a shift",hook="더 나은 사회를 바라볼 수 있다는 expect(기대하다) → 요약문에서는 anticipate(예상하다)로 바꿨어요."),
 dict(a="transition",form="transition",n=8,sq=4,sum="anticipate a [[shift]] to a more sustainable society",hook="지속 가능한 사회로 넘어가는 transition(전환) → 요약문에서는 shift(변화)로 바꿨어요."),
 dict(a="impact",form="impact",n=9,sq=5,sum="The [[influence]] of the index may spread",hook="프랑스를 넘어 퍼질 지수의 impact(영향) → 요약문에서는 influence(영향력)로 바꿨어요."),
 dict(a="innovative",form="innovative",n=11,sq=5,sum="its [[groundbreaking]] lead",hook="다른 나라가 따라 할 프랑스의 innovative(혁신적인) 선례 → 요약문에서는 groundbreaking(획기적인)으로 바꿨어요."),
]

SCENES=[
 dict(tag="본문 1번",ns=[1],line="프랑스 정부가 제조사에게 수리 가능성 [[index|지수]]를 붙이라는 법안을 [[passed|통과시켰다]]."),
 dict(tag="본문 3번",ns=[3],line="점수는 수리 정보, 분해, 부품 가격 같은 [[elements|요소]]를 보고 매긴다."),
 dict(tag="본문 5~7번",ns=[5,6,7],line="이 지수는 두 가지 효과를 노리고 [[designed|만들어졌다]]. 소비자는 똑똑하게 고르고, 제조사는 고치기 쉬운 제품을 만들도록 [[encourages|장려받는다]]."),
 dict(tag="본문 8번",ns=[8],line="버려지는 전자 제품이 줄어 지속 가능한 사회로의 [[transition|전환]]을 [[expect|기대할]] 수 있다."),
 dict(tag="본문 9~11번",ns=[9,10,11],line="이 지수의 [[impact|영향]]은 프랑스 밖으로 퍼지고, 다른 나라들도 [[innovative|혁신적인]] 선례를 따를 수 있다."),
]

HLKO={1:["수리 가능성 지수","법안을 통과시켰다"],3:["몇 가지 요소","고려한다"],5:["두 가지의 긍정적인 효과를 가지도록 만들어졌다"],
 7:["장려한다","수리하기 더 쉽게"],8:["더 지속 가능한 사회로 변화할 것","기대할 수 있다"],
 9:["그 지수의 영향","프랑스를 넘어 더 멀리 퍼질"],10:["라벨을 붙여야"],11:["혁신적인 선례"]}

UM={'enact':('제정하다','제정했다'),'rating':('등급, 평점','평점'),'consider':('고려하다','고려해'),'factor':('요소, 요인','요소'),'intend':('의도하다','의도되었다'),'motivate':('동기를 부여하다','동기를 부여할'),'anticipate':('예상하다, 기대하다','예상한다'),'shift':('변화, 전환','변화'),'influence':('영향','영향'),'groundbreaking':('획기적인','획기적인')}

TARGET={1:2,2:4,3:0,4:3,5:1}
G.update({'french':['French','프랑스의'],'into':['into','~ 안으로 (take into account = 고려하다)'],'including':['include','포함하다'],'company':['company','회사'],'sell':['sell','팔다'],'following':['follow','따르다']})
