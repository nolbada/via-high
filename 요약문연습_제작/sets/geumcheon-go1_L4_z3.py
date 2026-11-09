# -*- coding: utf-8 -*-
# 세트 정의: 금천고1 4과 ❸
META=dict(sch='geumcheon-go1', src='geumcheon-go1/L4/sx-data.js', pidx=2, lesson='4과', title='AI Neural Implants', label='❸', page='yoyak-lian-z3')
Q = [
 dict(
  id=1,
  summary="Before people fully (A) AI-powered neural implants, many difficult ethical issues need to be (B).",
  ko="사람들이 AI 기반 신경 임플란트를 완전히 <b>(A) 받아들이기</b> 전에, 여러 까다로운 윤리적 문제들이 <b>(B) 해결되어야</b> 한다.",
  opts=[["accept","resolved"],["accept","ignored"],["reject","resolved"],["reject","ignored"],["develop","postponed"]],
  optko=["받아들이다 – 해결되다","받아들이다 – 무시되다","거부하다 – 해결되다","거부하다 – 무시되다","개발하다 – 미뤄지다"],
  ans=0,
  wrong=[None,
         "ignored(무시되다)가 틀려요. 본문은 윤리적 문제가 해결되어야(addressed) 한다고 해요.",
         "reject(거부하다)가 틀려요. 본문은 이 시대를 완전히 받아들이기(embrace) 전의 이야기예요.",
         "둘 다 틀려요. 거부하는 이야기도, 문제를 무시하는 이야기도 아니에요.",
         "둘 다 틀려요. develop(개발하다)도, postponed(미뤄지다)도 본문에 나오지 않아요."],
  evid=[dict(n=1, hl=["fully embrace","tricky","addressed"])],
  swaps=[["embrace","accept","받아들이다 → 받아들이다"],["tricky","difficult","까다로운 → 어려운"],["address","resolve","(문제를) 다루다 → 해결하다"]],
  swapnote="embrace(받아들이다)는 accept(받아들이다)로, tricky(까다로운)는 difficult(어려운)로 바뀌어요. 본문 단어를 그대로 찾지 말고 뜻이 같은 말을 찾으세요.",
  use=[dict(w="accept",ex="She was happy to accept the invitation.",ko="그녀는 기쁘게 초대를 받아들였다."),
       dict(w="resolve",ex="We need to resolve this problem today.",ko="우리는 오늘 이 문제를 해결해야 한다.")],
  flow="본문 1번은 첫 문장이에요. AI 임플란트 시대를 완전히 받아들이기 전에 까다로운 윤리 문제부터 해결해야 한다고 시작해요.",
 ),
 dict(
  id=2,
  summary="Depending too heavily on technology may (A) our natural growth and create (B) about whether we are human, AI, or something in between.",
  ko="기술에 지나치게 의존하는 것은 우리의 자연스러운 성장을 <b>(A) 늦추고</b> 우리가 인간인지, AI인지, 그 중간인지에 대한 <b>(B) 불확실성</b>을 만들 수 있다.",
  opts=[["slow","uncertainty"],["slow","confidence"],["boost","uncertainty"],["boost","confidence"],["protect","clarity"]],
  optko=["늦추다 – 불확실성","늦추다 – 자신감","북돋우다 – 불확실성","북돋우다 – 자신감","지키다 – 명확함"],
  ans=0,
  wrong=[None,
         "confidence(자신감)가 틀려요. 본문은 혼란(confusion)이 생긴다고 해요.",
         "boost(북돋우다)가 틀려요. 지나친 의존은 성장을 북돋는 게 아니라 늦춰요(delay).",
         "둘 다 틀려요. 성장을 북돋우지도, 자신감이 생기지도 않아요. 본문은 반대예요.",
         "둘 다 틀려요. 성장을 지키거나(protect) 명확함(clarity)이 생긴다는 말은 없어요."],
  evid=[dict(n=4, hl=["over-reliance on technology","delay our natural development","confusion"])],
  swaps=[["over-reliance","depending too heavily","지나친 의존 → 지나치게 의존하는 것"],["delay","slow","지연시키다 → 늦추다"],["development","growth","발달 → 성장"],["confusion","uncertainty","혼란 → 불확실성"]],
  swapnote="delay(지연시키다)는 slow(늦추다)나 hold back(붙잡아 두다)으로, confusion(혼란)은 uncertainty(불확실성)로 바뀌어 나와요.",
  use=[dict(w="slow",ex="Heavy rain can slow the bus.",ko="폭우는 버스를 늦출 수 있다."),
       dict(w="uncertainty",ex="There is still uncertainty about the test date.",ko="시험 날짜에 대해 아직 불확실성이 있다.")],
  flow="본문 4번은 However(그러나)로 시작해요. 기술에 너무 기대면 자연스러운 발달이 늦어지고, 내가 인간인지 AI인지 헷갈리게 된다는 경고예요.",
 ),
 dict(
  id=3,
  summary="Hackers or organizations could (A) personal data without permission through AI-connected implants, so our thoughts, emotions, and behaviors could be (B) by them.",
  ko="해커나 조직이 AI와 연결된 임플란트를 통해 허가 없이 개인 정보를 <b>(A) 얻을</b> 수 있고, 그래서 우리의 생각, 감정, 행동이 그들에 의해 <b>(B) 조종될</b> 수 있다.",
  opts=[["obtain","manipulated"],["obtain","protected"],["delete","manipulated"],["delete","protected"],["share","observed"]],
  optko=["얻다 – 조종되다","얻다 – 보호되다","삭제하다 – 조종되다","삭제하다 – 보호되다","공유하다 – 관찰되다"],
  ans=0,
  wrong=[None,
         "protected(보호되다)가 틀려요. 본문은 해커에게 통제된다(controlled)고 해요.",
         "delete(삭제하다)가 틀려요. 본문은 정보를 지우는 게 아니라 허락 없이 접근한다(access)고 해요.",
         "둘 다 틀려요. 정보를 지우는 얘기도, 보호받는 얘기도 아니에요.",
         "둘 다 틀려요. 정보를 공유하거나(share) 단순히 관찰되는(observed) 게 아니라, 생각과 행동까지 통제돼요."],
  evid=[dict(n=6, hl=["access personal data without permission"]), dict(n=7, hl=["controlled by hackers"])],
  swaps=[["access","obtain","접근하다 → 얻다"],["control","manipulate","통제하다 → 조종하다"]],
  swapnote="access(접근하다)는 obtain(얻다)으로, control(통제하다)은 manipulate(조종하다)로 바뀌어 나와요. 모르는 단어여도 앞뒤 뜻으로 짐작해 보세요.",
  use=[dict(w="obtain",ex="You can obtain a free ticket at the door.",ko="입구에서 무료 표를 얻을 수 있다."),
       dict(w="manipulate",ex="Some people try to manipulate others with lies.",ko="어떤 사람들은 거짓말로 다른 사람들을 조종하려 한다."),]
  ,
  flow="본문 5번은 새 문제를 알리는 말(Another critical issue = 또 다른 중요한 문제)이에요. 6번은 개인 정보가 새는 위험, 7번은 This means(이는 ~라는 뜻이다)로 생각과 행동까지 통제될 수 있다는 결과예요.",
 ),
 dict(
  id=4,
  summary="Because of its high price, the technology may not be (A) to everyone, which could (B) the gap between people who can pay for implants and those who cannot.",
  ko="높은 가격 때문에 그 기술은 모든 사람에게 <b>(A) 이용 가능하지</b> 않을 수 있고, 이는 임플란트 비용을 낼 수 있는 사람과 그렇지 못한 사람 사이의 격차를 <b>(B) 벌릴</b> 수 있다.",
  opts=[["accessible","widen"],["accessible","narrow"],["useful","widen"],["harmful","narrow"],["familiar","reduce"]],
  optko=["이용 가능한 – 넓히다","이용 가능한 – 좁히다","유용한 – 넓히다","해로운 – 좁히다","익숙한 – 줄이다"],
  ans=0,
  wrong=[None,
         "narrow(좁히다)가 틀려요. 비싸서 못 쓰는 사람이 생기니 격차는 줄어드는 게 아니라 커져요(intensify).",
         "useful(유용한)이 틀려요. 본문은 쓸모가 아니라 모두가 이용할 수 있느냐(available)를 말해요.",
         "둘 다 틀려요. 해로운 기술이라는 말도, 격차가 좁아진다는 말도 본문과 반대예요.",
         "둘 다 틀려요. 익숙한(familiar) 기술인지는 나오지 않고, 격차는 줄지 않고 커져요."],
  evid=[dict(n=8, hl=["not be available to all","high cost"]), dict(n=9, hl=["intensify the division","afford the implants"])],
  swaps=[["cost","price","비용 → 가격"],["available","accessible","이용할 수 있는 → 접근 가능한"],["intensify","widen","심화시키다 → 넓히다"],["division","gap","분열 → 격차"],["afford","pay","(~할) 여유가 있다 → 돈을 내다"]],
  swapnote="intensify(심화시키다)는 widen(넓히다)이나 deepen(깊게 하다)으로, division(분열)은 gap(격차)으로 바뀌어 나와요.",
  use=[dict(w="accessible",ex="The museum is accessible to everyone by bus.",ko="그 박물관은 버스로 누구나 이용할 수 있다."),
       dict(w="widen",ex="They plan to widen the road next year.",ko="그들은 내년에 도로를 넓힐 계획이다.")],
  flow="본문 8번에서 비싸서 모두가 못 쓸 수 있다고 하고, 9번에서 살 수 있는 사람과 없는 사람 사이가 더 벌어진다고 마무리해요.",
 ),
]

# 단어 사전: 표면형(소문자) -> [기본형, 이 글에서의 뜻]
G = {
 "before":["before","~하기 전에"],"people":["people","사람들"],"fully":["fully","완전히"],"accept":["accept","받아들이다"],
 "ai-powered":["AI-powered","AI로 작동하는, AI 기반의"],"neural":["neural","신경의"],"implants":["implant","임플란트(몸속에 심는 의료 기기)"],
 "implant":["implant","임플란트(몸속에 심는 의료 기기)"],"difficult":["difficult","어려운"],"ethical":["ethical","윤리적인"],
 "issues":["issue","문제"],"need":["need","필요하다"],"resolved":["resolve","해결하다"],"resolve":["resolve","해결하다"],
 "ignored":["ignore","무시하다"],"reject":["reject","거부하다"],"develop":["develop","개발하다"],"postponed":["postpone","미루다"],
 "embrace":["embrace","받아들이다"],"era":["era","시대"],"tricky":["tricky","까다로운"],"addressed":["address","(문제를) 다루다, 해결하다"],
 "address":["address","(문제를) 다루다, 해결하다"],"should":["should","~해야 한다"],"many":["many","많은"],
 "depending":["depend","의존하다"],"heavily":["heavily","심하게, 많이"],"technology":["technology","기술"],
 "may":["may","~할 수 있다"],"slow":["slow","늦추다"],"natural":["natural","자연스러운"],"growth":["growth","성장"],
 "create":["create","만들어 내다"],"uncertainty":["uncertainty","불확실성"],"whether":["whether","~인지 아닌지"],
 "human":["human","인간"],"something":["something","어떤 것"],"between":["between","~ 사이에"],
 "confidence":["confidence","자신감"],"boost":["boost","북돋우다"],"protect":["protect","지키다"],"clarity":["clarity","명확함"],
 "over-reliance":["over-reliance","지나친 의존"],"reliance":["reliance","의존"],"delay":["delay","지연시키다, 늦추다"],
 "development":["development","발달"],"confusion":["confusion","혼란"],"however":["however","그러나"],
 "hackers":["hacker","해커"],"organizations":["organization","조직, 단체"],"could":["could","~할 수 있다"],
 "obtain":["obtain","얻다"],"personal":["personal","개인의"],"data":["data","자료, 정보"],"without":["without","~ 없이"],
 "permission":["permission","허가"],"through":["through","~을 통해"],"ai-connected":["AI-connected","AI와 연결된"],
 "thoughts":["thought","생각"],"emotions":["emotion","감정"],"behaviors":["behavior","행동"],"manipulated":["manipulate","조종하다"],
 "manipulate":["manipulate","조종하다"],"protected":["protect","보호하다"],"delete":["delete","삭제하다"],"share":["share","공유하다"],
 "observed":["observe","관찰하다"],"access":["access","접근하다, 접근"],"controlled":["control","통제하다"],"risk":["risk","위험"],
 "because":["because","~ 때문에"],"high":["high","높은"],"price":["price","가격"],"cost":["cost","비용"],
 "accessible":["accessible","이용 가능한"],"everyone":["everyone","모든 사람"],"which":["which","(앞 내용 전체를 가리키는) 이는"],
 "widen":["widen","넓히다"],"gap":["gap","격차"],"pay":["pay","돈을 내다"],"cannot":["cannot","~할 수 없다"],
 "narrow":["narrow","좁히다"],"useful":["useful","유용한"],"harmful":["harmful","해로운"],"familiar":["familiar","익숙한"],
 "reduce":["reduce","줄이다"],"available":["available","이용할 수 있는"],"due":["due to","~ 때문에"],"additional":["additional","추가적인"],
 "intensify":["intensify","심화시키다"],"division":["division","분열, 격차"],"afford":["afford","(~할) 여유가 있다"],
 "technology.":["technology","기술"],"unequal":["unequal","불평등한"],"social":["social","사회적인"],"inequality":["inequality","불평등"],
 "greater":["great","더 큰"],"lead":["lead","이끌다"],"given":["given that","~라는 점을 고려하면"],"such":["such","이러한"],
 "those":["those","(~한) 사람들"],"implants.":["implant","임플란트"],"era":["era","시대"],"integration":["integration","통합"],
 "raises":["raise","(문제를) 제기하다"],"concerns":["concern","우려"],"mean":["mean","의미하다"],"means":["mean","의미하다, 뜻하다"],
 "brains":["brain","뇌"],"brain":["brain","뇌"],"believed":["believe","믿다, 여기다"],"central":["central","중심이 되는"],
 "identity":["identity","정체성"],"existence":["existence","존재"],"value":["value","가치"],"beings":["being","존재"],
 "reliance":["reliance","의존"],"another":["another","또 다른"],"critical":["critical","중요한"],"privacy":["privacy","프라이버시, 사생활"],
 "organizations":["organization","조직, 단체"],"connected":["connect","연결하다"],"behaviours":["behaviour","행동"],"emotions":["emotion","감정"],
 "even":["even","더욱"],"all":["all","모든 사람"],"access":["access","접근하다, 접근"],"intensify":["intensify","심화시키다"],
 "implants":["implant","임플란트(몸속에 심는 의료 기기)"],"identity,":["identity","정체성"],"fully":["fully","완전히"],
 "era":["era","시대"],"hackers.":["hacker","해커"],"conditions":["condition","상태"],"complete":["complete","완전한"],
}

# 직독직해 조각: [영어 조각, 한글 조각]. [[ ]] 는 빈칸에 들어간 정답 단어 표시
JD={
 1:[["Before people fully [[accept]]","사람들이 완전히 [[받아들이기]] 전에"],
    ["AI-powered neural implants,","AI 기반 신경 임플란트를,"],
    ["many difficult ethical issues","여러 까다로운 윤리적 문제들이"],
    ["need to be [[resolved]].","[[해결되어야]] 한다."]],
 2:[["Depending too heavily on technology","기술에 지나치게 의존하는 것은"],
    ["may [[slow]] our natural growth","우리의 자연스러운 성장을 [[늦출]] 수 있고"],
    ["and create [[uncertainty]]","[[불확실성]]을 만들어 낼 수 있다"],
    ["about whether we are human, AI, or something in between.","우리가 인간인지, AI인지, 그 중간인지에 대한."]],
 3:[["Hackers or organizations could [[obtain]] personal data","해커나 조직이 개인 정보를 [[얻을]] 수 있고"],
    ["without permission through AI-connected implants,","AI와 연결된 임플란트를 통해 허가 없이,"],
    ["so our thoughts, emotions, and behaviors","그래서 우리의 생각, 감정, 행동이"],
    ["could be [[manipulated]] by them.","그들에 의해 [[조종될]] 수 있다."]],
 4:[["Because of its high price,","높은 가격 때문에,"],
    ["the technology may not be [[accessible]] to everyone,","그 기술은 모든 사람에게 [[이용 가능하지]] 않을 수 있고,"],
    ["which could [[widen]] the gap","이는 격차를 [[벌릴]] 수 있다"],
    ["between people who can pay for implants and those who cannot.","임플란트 비용을 낼 수 있는 사람과 그렇지 못한 사람 사이의."]],
}

# 기억할 흐름 카드뉴스
FC={
 1:[["본문 1번","AI 임플란트 시대, 아직 이르다","완전히 받아들이기 전에 해야 할 일이 있어요."],
    ["본문 1번","까다로운 윤리 문제가 먼저","문제를 해결해야 한다고 말해요."],
    ["정답 포인트","{{embrace|받아들이다}} = {{accept|받아들이다}}, {{addressed|해결되다}} = {{resolved|해결되다}}","{{tricky|까다로운}} = {{difficult|어려운}}으로도 바뀌어요."]],
 2:[["본문 3번","뇌는 우리 정체성의 중심","인간이라는 존재의 핵심이에요."],
    ["본문 4번","However! 기술에 너무 기대면","자연스러운 발달이 늦어져요."],
    ["그 결과","내가 인간인지 AI인지 헷갈린다","{{confusion|혼란}}이 생긴다는 경고예요."],
    ["정답 포인트","{{delay|지연시키다}} = {{slow|늦추다}}, {{confusion|혼란}} = {{uncertainty|불확실성}}","{{development|발달}} = {{growth|성장}}"]],
 3:[["본문 5번","또 다른 중요한 문제, 프라이버시","새 문제의 시작이에요."],
    ["본문 6번","허락 없이 개인 정보에 접근","조직이나 해커가 임플란트로 들어와요."],
    ["본문 7번","This means! 생각·감정·행동까지","해커에게 통제될 수 있어요."],
    ["정답 포인트","{{access|접근하다}} = {{obtain|얻다}}, {{controlled|통제되다}} = {{manipulated|조종되다}}","허락 없이 얻고, 그다음 조종까지 가요."]],
 4:[["본문 8번","값이 비싸서 모두가 못 쓴다","{{cost|비용}} = {{price|가격}}"],
    ["본문 9번","살 수 있는 사람 vs 없는 사람","그 사이가 더 벌어져요."],
    ["정답 포인트","{{available|이용할 수 있는}} = {{accessible|접근 가능한}}, {{intensify|심화시키다}} = {{widen|넓히다}}","{{division|분열}} = {{gap|격차}}"]],
}

# 바꿔 말하기 스토리
STORY=[
 dict(a="embrace",form="embrace",n=1,sq=1,sum="Before people fully [[accept]] AI-powered neural implants",hook="AI 임플란트 시대를 완전히 맞이하기 전이라는 문장의 embrace(받아들이다) → 요약문에서는 accept(받아들이다)로 바꿨어요."),
 dict(a="tricky",form="tricky",n=1,sq=1,sum="many [[difficult]] ethical issues",hook="풀기 어려운 윤리 문제를 말하는 문장의 tricky(까다로운) → 요약문에서는 difficult(어려운)로 바꿨어요."),
 dict(a="address",form="addressed",n=1,sq=1,sum="need to be [[resolved]]",hook="그 문제들을 먼저 해결해야 한다는 문장의 addressed(다루어지다) → 요약문에서는 resolved(해결되다)로 바꿨어요."),
 dict(a="delay",form="delay",n=4,sq=2,sum="may [[slow]] our natural growth",hook="기술에 너무 기대면 자연스러운 발달이 뒤로 밀린다는 문장의 delay(지연시키다) → 요약문에서는 slow(늦추다)로 바꿨어요."),
 dict(a="development",form="development",n=4,sq=2,sum="our natural [[growth]]",hook="우리 몸과 마음이 자연스럽게 크는 이야기의 development(발달) → 요약문에서는 growth(성장)로 바꿨어요."),
 dict(a="confusion",form="confusion",n=4,sq=2,sum="create [[uncertainty]]",hook="내가 인간인지 AI인지 헷갈린다는 문장의 confusion(혼란) → 요약문에서는 uncertainty(불확실성)로 바뀌었어요."),
 dict(a="access",form="access",n=6,sq=3,sum="could [[obtain]] personal data",hook="해커가 허락 없이 정보에 들어간다는 문장의 access(접근하다) → 요약문에서는 obtain(얻다)으로 바꿨어요."),
 dict(a="control",form="controlled",n=7,sq=3,sum="could be [[manipulated]] by them",hook="생각과 행동이 해커 손에 들어간다는 문장의 controlled(통제되다) → 요약문에서는 manipulated(조종되다)로 바꿨어요."),
 dict(a="available",form="available",n=8,sq=4,sum="may not be [[accessible]] to everyone",hook="모두가 쓸 수 있지는 않다는 문장의 available(이용할 수 있는) → 요약문에서는 accessible(접근 가능한)로 바꿨어요."),
 dict(a="cost",form="cost",n=8,sq=4,sum="its high [[price]]",hook="값이 비싸다는 이야기의 cost(비용) → 요약문에서는 price(가격)로 바꿨어요."),
 dict(a="intensify",form="intensify",n=9,sq=4,sum="could [[widen]] the gap",hook="둘 사이가 더 벌어진다는 문장의 intensify(심화시키다) → 요약문에서는 widen(넓히다)으로 바꿨어요."),
 dict(a="division",form="division",n=9,sq=4,sum="the [[gap]] between people",hook="살 수 있는 사람과 없는 사람 사이를 말하는 division(분열) → 요약문에서는 gap(격차)으로 바꿨어요."),
]

# 줄거리 장면
SCENES=[
 dict(tag="본문 1번",ns=[1],line="AI 임플란트 시대를 [[embrace|받아들이기]] 전에, [[tricky|까다로운]] 윤리 문제부터 [[addressed|해결해야]] 한다."),
 dict(tag="본문 2~3번",ns=[2,3],line="AI와 뇌를 합치면 '인간이란 무엇인가' 하는 걱정이 생긴다. 뇌는 우리 정체성의 중심이니까."),
 dict(tag="본문 4번",ns=[4],line="기술에 너무 기대면 자연스러운 [[development|발달]]이 [[delay|늦어지고]], [[confusion|혼란]]이 생긴다."),
 dict(tag="본문 6번",ns=[6],line="또 다른 문제는 프라이버시. 해커가 허락 없이 개인 정보에 [[access|접근할]] 수 있다."),
 dict(tag="본문 7번",ns=[7],line="심지어 생각과 행동까지 해커에게 [[controlled|조종될]] 수 있다."),
 dict(tag="본문 8번",ns=[8],line="높은 [[cost|비용]] 때문에 모두가 [[available|이용할 수 있는]] 건 아닐 수 있다."),
 dict(tag="본문 9번",ns=[9],line="그러면 살 수 있는 사람과 없는 사람의 [[division|격차]]가 더 [[intensify|심해진다]]."),
]

# 근거 본문 한글 해석에서 영어 형광펜과 같은 자리
HLKO={1:["완전히 받아들이기","까다로운","해결되어야"],4:["지나친 의존","자연스러운 발달을 지연시키고","혼란"],
 6:["허가 없이 개인 정보에 접근할 수"],7:["해커에 의해 통제될 수"],
 8:["모든 사람에게 제공되지 않을 수","높은 비용"],9:["분열을 심화시킬 수","임플란트 비용을 감당할 수"]}

UM={'accept':('받아들이다','받아들였다'),'resolve':('해결하다','해결해야'),'slow':('늦추다','늦출'),'uncertainty':('불확실성','불확실성'),'obtain':('얻다','얻을 수'),'manipulate':('조종하다','조종하려'),'accessible':('이용 가능한','이용할 수 있다'),'widen':('넓히다','넓힐')}

G.update({'about':['about','~에 대한'],"there's":['there is','~이(가) 있다'],'organization':['organization','조직, 단체'],'depend':['depend','의존하다']})

TARGET={1:3,2:0,3:4,4:1}
