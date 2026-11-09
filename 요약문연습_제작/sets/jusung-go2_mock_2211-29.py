# -*- coding: utf-8 -*-
# 세트 정의: 주성고2 모의고사 22년 11월 29번
META=dict(sch='jusung-go2', src='jusung-go2/mock/sx-data.js', pidx=0, lesson='22년 11월 29번', title='', label='', page='yoyak-2211-29')
Q = [
 dict(
  id=1,
  summary="Pre-emption is a strategy meant to (A) a rival's start of some activity, and even a simple announcement of intent may (B) rivals' wish to do the same.",
  ko="선매 행위는 경쟁자가 어떤 활동을 <b>(A) 시작하지 못하게 막으려는</b> 전략이고, 단순한 의도의 공표도 경쟁자들이 같은 행동을 하려는 마음을 <b>(B) 약하게 할</b> 수 있다.",
  opts=[["block","weaken"],["block","strengthen"],["support","strengthen"],["support","weaken"],["ignore","weaken"]],
  optko=["막다 – 약하게 하다","막다 – 강하게 하다","돕다 – 강하게 하다","돕다 – 약하게 하다","무시하다 – 약하게 하다"],
  ans=0,
  wrong=[None,
         "strengthen(강하게 하다)이 틀려요. 공표는 경쟁자의 마음을 단념시키지(discourage), 키우지 않아요.",
         "둘 다 틀려요. 선매 행위는 경쟁자를 돕는(support) 게 아니라 막는 거고, 마음을 강하게 한다는 말도 반대예요.",
         "support(돕다)가 틀려요. 경쟁자의 시작을 돕는 게 아니라 막으려고(prevent) 만든 전략이에요.",
         "ignore(무시하다)가 틀려요. 경쟁자를 무시하는 게 아니라 시작하지 못하게 막는 전략이에요."],
  evid=[dict(n=1, hl=["prevent a rival from starting"]), dict(n=2, hl=["discourage rivals from doing the same"])],
  swaps=[["prevent","block","방지하다 → 막다"],["discourage","weaken","단념시키다 → 약하게 하다"],["a rival from starting","a rival's start","경쟁자가 시작하는 것을 → 경쟁자의 시작"]],
  swapnote="prevent(방지하다)는 block(막다)이나 stop(멈추다)으로, discourage(단념시키다)는 weaken(약하게 하다)이나 deter(막다)로 바뀌어 나올 수 있어요.",
  use=[dict(w="block",ex="A wall can block the wind.",ko="벽은 바람을 막을 수 있다."),
       dict(w="weaken",ex="Bad news can weaken your hope.",ko="나쁜 소식은 희망을 약하게 할 수 있다.")],
  flow="본문 1번에서 선매 행위의 뜻(경쟁자가 시작하지 못하게 막기)을 말하고, 2번에서 In some case(어떤 경우)로 좁혀 말뿐인 공표도 선매가 될 수 있다고 이어요.",
 ),
 dict(
  id=2,
  summary="Because the right (A) can bring greater rewards, a firm may (B) its advertising around a newcomer's market launch to make it harder for the newcomer's ads to influence buyers.",
  ko="올바른 <b>(A) 시점</b>이 더 큰 이득을 가져올 수 있어서, 기업은 새 업체가 시장에 나오는 전후로 광고를 <b>(B) 늘려</b> 그 업체의 광고가 구매자들에게 영향을 주기 더 어렵게 만들 수 있다.",
  opts=[["moment","increase"],["moment","reduce"],["price","reduce"],["price","increase"],["location","copy"]],
  optko=["시점 – 늘리다","시점 – 줄이다","가격 – 줄이다","가격 – 늘리다","위치 – 따라 하다"],
  ans=0,
  wrong=[None,
         "reduce(줄이다)가 틀려요. 경쟁자가 들어올 때 광고를 줄이는 게 아니라 늘려요(up-weight).",
         "둘 다 틀려요. 본문이 중요하다고 한 건 가격이 아니라 타이밍(시점)이고, 광고도 줄이지 않고 늘려요.",
         "price(가격)가 틀려요. 본문은 가격이 아니라 타이밍(시점)이 중요하다고 해요.",
         "둘 다 틀려요. 위치 이야기는 본문에 없고, 광고를 따라 하는 게 아니라 늘리는 거예요."],
  evid=[dict(n=3, hl=["timing is sometimes very important","much more rewarding"]), dict(n=4, hl=["up-weighting advertising"]), dict(n=5, hl=["make it more difficult"])],
  swaps=[["timing","moment","타이밍 → 시점"],["up-weighting","increase","가중치를 높이다 → 늘리다"],["entrant","newcomer","진입자 → 새로 들어온 업체"],["difficult","hard","어려운 → 어려운(더 어렵게)"],["make an impression on","influence","인상을 남기다 → 영향을 주다"]],
  swapnote="timing(타이밍)은 moment(순간, 시점)로, up-weighting(가중치를 높이기)은 increase(늘리다)로 바뀌었어요. 어려운 합성어는 쉬운 동사 하나로 줄여 읽어요.",
  use=[dict(w="moment",ex="Wait for the right moment to speak.",ko="말할 알맞은 시점을 기다려라."),
       dict(w="increase",ex="The shop will increase its prices next month.",ko="그 가게는 다음 달에 가격을 올릴 것이다.")],
  flow="본문 3번에서 타이밍이 중요하다고 말하고 → 4번에서 그 예로 새 진입자가 오기 전후에 광고를 늘리는 이야기 → 5번에서 그 목적(진입자 광고가 인상을 남기기 어렵게)이 나와요.",
 ),
 dict(
  id=3,
  summary="Another pre-emption strategy is to (A) a wide range of product versions, which makes it hard for rivals to find (B) market demand.",
  ko="또 다른 선매 행위 전략은 다양한 제품 버전을 <b>(A) 출시하는</b> 것이고, 이는 경쟁자가 <b>(B) 충족되지 않은</b> 시장 수요를 찾기 어렵게 만든다.",
  opts=[["release","unmet"],["release","declining"],["remove","declining"],["limit","unmet"],["remove","unmet"]],
  optko=["출시하다 – 충족되지 않은","출시하다 – 줄어드는","없애다 – 줄어드는","제한하다 – 충족되지 않은","없애다 – 충족되지 않은"],
  ans=0,
  wrong=[None,
         "declining(줄어드는)이 틀려요. 본문은 아직 채워지지 않은(untapped) 수요를 찾기 어렵다고 해요.",
         "둘 다 틀려요. 제품을 없애는 게 아니라 다양하게 내놓는 전략이고, 수요가 줄어든다는 말도 없어요.",
         "limit(제한하다)이 틀려요. 제품 종류를 제한하는 게 아니라 다양하게 출시(launch)해요.",
         "remove(없애다)가 틀려요. 제품을 없애는 게 아니라 다양하게 출시(launch)해요."],
  evid=[dict(n=7, hl=["launch a large variety of product variants"]), dict(n=8, hl=["untapped pockets of market demand"])],
  swaps=[["launch","release","출시하다 → 출시하다"],["variety","range","다양성 → 범위, 종류"],["variant","version","변형 → 버전"],["untapped","unmet","손대지 않은 → 충족되지 않은"]],
  swapnote="untapped(아직 손대지 않은)는 unmet(충족되지 않은)으로 바뀌었어요. 앞 문장의 accommodated(수용된)의 반대말이라고 생각하면 쉬워요.",
  use=[dict(w="release",ex="The company will release a new phone next week.",ko="그 회사는 다음 주에 새 휴대폰을 출시할 것이다."),
       dict(w="unmet",ex="Many people have unmet needs in the city.",ko="도시에는 충족되지 않은 필요를 가진 사람이 많다.")],
  flow="본문 6번에서 또 다른 전략(제품 확산)을 소개 → 7번에서 다양한 제품을 출시한다고 풀이 → 8번에서 시장이 꽉 차면 경쟁자가 빈틈 수요를 찾기 어렵다고 마무리해요.",
 ),
]

G = {
 "pre-emption":["pre-emption","선매 행위(경쟁자보다 먼저 선수 치기)"],"pre-emptive":["pre-emptive","선제적인"],
 "means":["mean","의미하다"],"strategy":["strategy","전략"],"designed":["design","(목적을 갖고) 만들다"],
 "prevent":["prevent","방지하다, 막다"],"rival":["rival","경쟁자"],"rivals":["rival","경쟁자"],"rival's":["rival","경쟁자"],
 "starting":["start","시작하다"],"start":["start","시작"],"some":["some","어떤"],"particular":["particular","특정한"],
 "activity":["activity","활동"],"case":["case","경우"],"move":["move","조치, 움직임"],"simply":["simply","단순히"],
 "announcement":["announcement","공표, 발표"],"intent":["intent","의도"],"discourage":["discourage","단념시키다"],
 "doing":["do","하다"],"same":["same","같은"],"simple":["simple","단순한"],"wish":["wish","바람, 마음"],
 "block":["block","막다"],"weaken":["weaken","약하게 하다"],"strengthen":["strengthen","강하게 하다"],
 "support":["support","돕다, 지지하다"],"ignore":["ignore","무시하다"],"even":["even","~조차"],
 "idea":["idea","개념, 생각"],"implies":["imply","암시하다"],"timing":["timing","타이밍, 시기 선택"],"important":["important","중요한"],
 "decision":["decision","결정"],"action":["action","조치, 행동"],"point":["point","시점, 지점"],"time":["time","시간, 시점"],
 "rewarding":["rewarding","득이 되는, 보람 있는"],"different":["different","다른"],"rewards":["reward","이득, 보상"],
 "sometimes":["sometimes","때때로"],"very":["very","매우"],"much":["much","훨씬"],"might":["might","~일 수도 있다"],
 "right":["right","알맞은, 올바른"],"bring":["bring","가져오다"],"greater":["great","더 큰"],"firm":["firm","기업, 회사"],
 "moment":["moment","순간, 시점"],"increase":["increase","늘리다, 올리다"],"reduce":["reduce","줄이다"],
 "price":["price","가격"],"location":["location","위치"],"copy":["copy","따라 하다, 베끼다"],
 "advertising":["advertising","광고(하기)"],"ads":["ad","광고"],"newcomer's":["newcomer","새로 들어온 업체"],"newcomer":["newcomer","새로 들어온 업체"],
 "market":["market","시장"],"launch":["launch","출시하다, 진출하다"],"launches":["launch","출시하다, 진출하다"],
 "harder":["hard","더 어려운"],"influence":["influence","영향을 주다"],"buyers":["buyer","구매자"],"around":["around","~ 전후로, 주변에"],
 "involve":["involve","포함하다"],"up-weighting":["up-weight","가중치를 높이다"],"period":["period","기간"],"before":["before","~ 전에"],
 "during":["during","~ 동안"],"new":["new","새로운"],"entrant":["entrant","진입자, 새로 들어온 업체"],"entrant’s":["entrant","진입자"],
 "make":["make","만들다"],"difficult":["difficult","어려운"],"impression":["impression","인상"],"potential":["potential","잠재적인"],
 "product":["product","제품"],"proliferation":["proliferation","확산, 급증"],"another":["another","또 다른"],"strategy":["strategy","전략"],
 "general":["general","일반적인"],"large":["large","큰, 많은"],"variety":["variety","다양성, 종류"],"variants":["variant","변형"],
 "very":["very","매우"],"little":["little","거의 없는"],"demand":["demand","수요"],"accommodated":["accommodate","수용하다"],
 "arguably":["arguably","거의 틀림없이"],"already":["already","이미"],"filled":["fill","채우다"],"competitors":["competitor","경쟁자"],
 "find":["find","찾다"],"untapped":["untapped","아직 손대지 않은"],"pockets":["pocket","(작은) 틈새, 주머니"],
 "wide":["wide","넓은, 다양한"],"range":["range","범위, 종류"],"versions":["version","버전, 형태"],"release":["release","출시하다"],
 "unmet":["unmet","충족되지 않은"],"declining":["decline","줄어드는"],"remove":["remove","없애다"],"limit":["limit","제한하다"],
 "hard":["hard","어려운"],"makes":["make","만들다"],"leave":["leave","남기다"],"weaker":["weak","약한"],
 "launch":["launch","출시하다, 진출하다"],"discourages":["discourage","단념시키다"],"announce":["announce","발표하다"],
 "wall":["wall","벽"],
}

JD={
 1:[["Pre-emption is a strategy meant to [[block]]","선매 행위는 [[막으려는]] 전략이다"],
    ["a rival's start of some activity,","경쟁자가 어떤 활동을 시작하는 것을,"],
    ["and even a simple announcement of intent","그리고 단순한 의도의 공표조차"],
    ["may [[weaken]] rivals' wish to do the same.","경쟁자들이 같은 일을 하려는 마음을 [[약하게 할]] 수 있다."]],
 2:[["Because the right [[moment]] can bring greater rewards,","올바른 [[시점]]이 더 큰 이득을 가져올 수 있기 때문에,"],
    ["a firm may [[increase]] its advertising","기업은 광고를 [[늘릴]] 수 있다"],
    ["around a newcomer's market launch","새 업체가 시장에 나오는 전후로"],
    ["to make it harder","더 어렵게 만들려고"],
    ["for the newcomer's ads to influence buyers.","그 업체의 광고가 구매자들에게 영향을 주기가."]],
 3:[["Another pre-emption strategy is to [[release]]","또 다른 선매 행위 전략은 [[출시하는]] 것이다"],
    ["a wide range of product versions,","다양한 제품 버전을,"],
    ["which makes it hard for rivals","그것은 경쟁자들이 ~하기 어렵게 만든다"],
    ["to find [[unmet]] market demand.","[[충족되지 않은]] 시장 수요를 찾기가."]],
}

FC={
 1:[["본문 1번","선매 행위 = 경쟁자 막기","경쟁자가 특정 활동을 시작하지 못하게 만든 전략이에요."],
    ["본문 2번","말뿐인 공표도 선매","같은 행동을 하려는 경쟁자의 마음을 꺾어요."],
    ["정답 포인트","{{prevent|막다}} = {{block|막다}}, {{discourage|단념시키다}} = {{weaken|약하게 하다}}","본문 단어가 뜻이 비슷한 말로 바뀌어 나와요."]],
 2:[["본문 3번","타이밍이 중요하다","때에 따라 이득이 크게 달라져요."],
    ["본문 4번","진입자가 오기 전후로 광고를 늘린다","{{up-weighting|가중치를 높이기}}가 핵심이에요."],
    ["본문 5번","목적은 진입자 광고 효과 줄이기","{{make an impression|인상을 남기다}}를 더 어렵게 만들어요."],
    ["정답 포인트","{{timing|타이밍}} = {{moment|시점}}, {{up-weighting|가중치를 높이다}} = {{increase|늘리다}}","어려운 말을 쉬운 말로 바꿔 읽어요."]],
 3:[["본문 6번","또 다른 전략: 제품 확산","광고에 이어 두 번째 전략이에요."],
    ["본문 7번","다양한 제품을 출시한다","채워지지 않는 수요가 거의 없게 만들어요."],
    ["본문 8번","시장이 꽉 차면 빈틈 찾기 어렵다","{{untapped|손대지 않은}} 수요를 못 찾아요."],
    ["정답 포인트","{{launch|출시하다}} = {{release|출시하다}}, {{untapped|손대지 않은}} = {{unmet|충족되지 않은}}","{{variety|다양성}}은 {{range|범위, 종류}}로, {{variant|변형}}은 {{version|버전}}으로 바뀌어요."]],
}

STORY=[
 dict(a="prevent",form="prevent",n=1,sq=1,sum="meant to [[block]] a rival's start of some activity",hook="경쟁자가 시작하지 못하게 막는다는 첫 문장의 prevent(방지하다) → 요약문에서는 block(막다)으로 바꿨어요."),
 dict(a="discourage",form="discourage",n=2,sq=1,sum="may [[weaken]] rivals' wish to do the same",hook="말뿐인 공표로 경쟁자의 의욕을 꺾는다는 문장의 discourage(단념시키다) → 요약문에서는 weaken(약하게 하다)으로 바꿨어요."),
 dict(a="timing",form="timing",n=3,sq=2,sum="the right [[moment]] can bring greater rewards",hook="때에 따라 이득이 달라진다는 문장의 timing(타이밍) → 요약문에서는 moment(시점)로 바꿨어요."),
 dict(a="entrant",form="entrant",n=4,sq=2,sum="a [[newcomer]]'s market launch",hook="시장에 새로 들어오는 업체를 가리키는 entrant(진입자) → 요약문에서는 newcomer(새로 들어온 업체)로 바꿨어요."),
 dict(a="difficult",form="difficult",n=5,sq=2,sum="to make it [[harder]] for the newcomer's ads",hook="진입자 광고가 먹히기 힘들게 만든다는 문장의 difficult(어려운) → 요약문에서는 harder(더 어려운)로 바꿨어요."),
 dict(a="launch",form="launch",n=7,sq=3,sum="is to [[release]] a wide range of product versions",hook="제품을 시장에 내놓는다는 문장의 launch(출시하다) → 요약문에서는 release(출시하다)로 바꿨어요."),
 dict(a="variety",form="variety",n=7,sq=3,sum="a wide [[range]] of product versions",hook="제품을 아주 많은 종류로 내놓는다는 문장의 variety(다양성) → 요약문에서는 range(범위, 종류)로 바꿨어요."),
 dict(a="variant",form="variants",n=7,sq=3,sum="a wide range of product [[versions]]",hook="조금씩 다른 제품들을 가리키는 variants(변형) → 요약문에서는 versions(버전)로 바꿨어요."),
 dict(a="untapped",form="untapped",n=8,sq=3,sum="to find [[unmet]] market demand",hook="아직 아무도 손대지 않은 수요를 가리키는 untapped → 요약문에서는 unmet(충족되지 않은)으로 바꿨어요."),
]

SCENES=[
 dict(tag="본문 1번",ns=[1],line="선매 행위는 경쟁자가 일을 시작하지 못하게 [[prevent|막는]] 전략이다."),
 dict(tag="본문 2번",ns=[2],line="말뿐인 공표만으로도 경쟁자의 마음을 [[discourage|꺾을]] 수 있다."),
 dict(tag="본문 3번",ns=[3],line="그래서 [[timing|타이밍]]이 중요하다. 때에 따라 이득이 크게 달라진다."),
 dict(tag="본문 4번",ns=[4],line="새 [[entrant|진입자]]가 오기 전후로 광고를 확 늘린다."),
 dict(tag="본문 5번",ns=[5],line="목적은 진입자의 광고가 인상을 남기기 [[difficult|어렵게]] 만드는 것."),
 dict(tag="본문 6~7번",ns=[6,7],line="두 번째 전략은 제품 [[variants|변형]]을 엄청난 [[variety|종류]]로 [[launch|출시하는]] 것이다."),
 dict(tag="본문 8번",ns=[8],line="시장이 꽉 차면 경쟁자는 [[untapped|아직 손대지 않은]] 수요를 찾기 힘들다."),
]

HLKO={1:["경쟁자로 하여금 어떤 특정한 활동을 시작하는 것을 방지하기"],2:["경쟁자들이 같은 행동을 하는 것을 단념시킬"],
 3:["타이밍이 매우 중요하다","훨씬 더 득이 될 수 있다"],4:["광고의 가중치를 높이는 것"],5:["더 어렵게 만드는 것"],
 7:["다양한 제품 변형을 출시하는 것"],8:["아직 점유되지 않은 시장 수요 주머니"]}

UM={'block':('막다','막을'),'weaken':('약하게 하다','약하게 할'),'moment':('순간, 시점','시점'),'increase':('늘리다, 올리다','올릴'),'release':('출시하다','출시할'),'unmet':('충족되지 않은','충족되지 않은')}

G.update({'meant':['mean','~할 목적으로 만들어진 (meant to = ~하려는)'],'because':['because','~ 때문에'],'into':['into','~ 안으로'],'way':['way','방식, 방법'],'variant':['variant','변형'],'version':['version','버전, 형태']})

TARGET={1:1,2:3,3:4}
