# -*- coding: utf-8 -*-
# 세트 정의: 주성고2 모의고사 22년 11월 36번
META=dict(sch='jusung-go2', src='jusung-go2/mock/sx-data.js', pidx=7, lesson='22년 11월 36번', title='', label='', page='yoyak-2211-36')
Q = [
 dict(
  id=1,
  summary="The right to be forgotten is (A) from the right to privacy because it can cover information that is already (B).",
  ko="잊힐 권리는 이미 <b>(B) 공개된</b> 정보까지 다룰 수 있기 때문에 사생활 권리와 <b>(A) 다르다</b>.",
  opts=[["different","public"],["different","private"],["identical","public"],["identical","private"],["opposite","hidden"]],
  optko=["다른 – 공개된","다른 – 비공개의","똑같은 – 공개된","똑같은 – 비공개의","반대의 – 숨겨진"],
  ans=0,
  wrong=[None,
         "private(비공개의)이 틀려요. 잊힐 권리는 이미 공개된(public) 정보에도 적용돼요.",
         "identical(똑같은)이 틀려요. 본문은 두 권리가 구별된다(distinct)고 해요.",
         "둘 다 틀려요. 두 권리는 똑같지 않고, 비공개 정보는 사생활 권리 쪽 이야기예요.",
         "둘 다 틀려요. 두 권리는 반대가 아니라 관련이 있고, 숨겨진 정보 이야기도 아니에요."],
  evid=[dict(n=1, hl=["distinct from"]), dict(n=3, hl=["in the public domain"])],
  swaps=[["distinct","different","구별되는 → 다른"],["domain","public","영역 → 공개된 (in the public domain = 공개된)"]],
  swapnote="distinct(구별되는)는 different(다른), separate(분리된)로 바뀌어 나와요. public domain(공공의 영역)은 그냥 public(공개된)으로 줄여 나오기도 해요.",
  use=[dict(w="different",ex="My opinion is different from yours.",ko="내 의견은 네 의견과 다르다."),
       dict(w="public",ex="The park is open to the public.",ko="그 공원은 일반 대중에게 열려 있다.")],
  flow="본문 1번에서 잊힐 권리와 사생활 권리는 구별된다고 하고, 2번에서 사생활 권리를 설명한 뒤, 3번의 in contrast(반면에)에서 잊힐 권리는 이미 공개된 정보에도 적용된다고 대비해요.",
 ),
 dict(
  id=2,
  summary="The right to be forgotten helps people (A) their lives without being forever (B) by one event in the past.",
  ko="잊힐 권리는 사람들이 과거의 한 사건에 의해 영원히 <b>(B) 규정되지</b> 않고 자신의 삶을 <b>(A) 이어 가도록</b> 돕는다.",
  opts=[["continue","labeled"],["continue","rewarded"],["end","labeled"],["end","rewarded"],["remember","judged"]],
  optko=["이어 가다 – 낙인찍히는","이어 가다 – 보상받는","끝내다 – 낙인찍히는","끝내다 – 보상받는","기억하다 – 판단되는"],
  ans=0,
  wrong=[None,
         "rewarded(보상받는)가 틀려요. 본문은 사건에 의해 규정되지 않는다는 내용이고, 보상 이야기는 없어요.",
         "end(끝내다)가 틀려요. 본문은 삶을 끝내는 게 아니라 이어 나가게(move on) 한다는 거예요.",
         "둘 다 틀려요. 삶을 끝낸다는 말도, 보상받는다는 말도 본문에 없어요.",
         "remember(기억하다)가 틀려요. 이 권리는 과거를 기억하게 하는 게 아니라 잊히게 하는 권리예요."],
  evid=[dict(n=4, hl=["not to be forever defined"]), dict(n=5, hl=["move on with their lives"])],
  swaps=[["define","label","규정하다 → 낙인찍다, 이름 붙이다"],["move","continue","나아가다 → 이어 가다 (move on = 계속 살아가다)"],["period","event","기간 → 사건"]],
  swapnote="defined(규정되는)는 labeled(낙인찍히는), judged(판단되는)로 바뀌어 나올 수 있어요. move on(털고 나아가다)은 continue(이어 가다)와 비슷한 느낌이에요.",
  use=[dict(w="continue",ex="She will continue to study after school.",ko="그녀는 방과 후에도 계속 공부할 것이다."),
       dict(w="label",ex="Do not label people by one mistake.",ko="한 번의 실수로 사람들에게 낙인을 찍지 마라.")],
  flow="본문 4번에서 특정 시점의 정보로 영원히 규정되지 않을 권리라고 하고, 5번에서 그 이유는 사람들이 한 사건에 묶이지 않고 삶을 이어 가게 하려는 것이라고 말해요.",
 ),
 dict(
  id=3,
  summary="The right to be forgotten can sometimes (A) with other rights, so (B) are made for security or public health reasons.",
  ko="잊힐 권리는 때때로 다른 권리와 <b>(A) 충돌할</b> 수 있어서 안보나 공공 보건의 이유로 <b>(B) 예외</b>가 만들어진다.",
  opts=[["clash","exemptions"],["clash","penalties"],["agree","exemptions"],["agree","penalties"],["merge","rewards"]],
  optko=["충돌하다 – 예외, 면제","충돌하다 – 처벌","일치하다 – 예외, 면제","일치하다 – 처벌","합쳐지다 – 보상"],
  ans=0,
  wrong=[None,
         "penalties(처벌)가 틀려요. 본문은 처벌이 아니라 공식적인 예외(exceptions)를 만든다고 해요.",
         "agree(일치하다)가 틀려요. 본문은 다른 권리와 충돌한다(conflict)고 해요.",
         "둘 다 틀려요. 권리들이 서로 일치하는 것도, 처벌이 생기는 것도 본문에 없어요.",
         "둘 다 틀려요. 권리가 합쳐진다는 말도, 보상이 생긴다는 말도 본문에 없어요."],
  evid=[dict(n=7, hl=["come into conflict with other rights"]), dict(n=8, hl=["formal exceptions"])],
  swaps=[["conflict","clash","충돌 → 부딪치다, 충돌하다"],["exception","exemption","예외 → 예외, 면제"]],
  swapnote="come into conflict(충돌하다)는 clash(부딪치다)로, exception(예외)은 exemption(면제)으로 바뀌어 나올 수 있어요.",
  use=[dict(w="clash",ex="Their ideas often clash with each other.",ko="그들의 생각은 서로 자주 충돌한다."),
       dict(w="exemption",ex="Students get an exemption from the fee.",ko="학생들은 그 비용을 면제받는다.")],
  flow="본문 6번까지 이 권리를 지지하는 이유를 말하다가, 7번의 Despite(~에도 불구하고)에서 반전이 와요. 다른 권리와 충돌할 수 있고, 8번의 For example(예를 들어)에서 안보와 공중 보건을 이유로 한 예외 사례를 들어요.",
 ),
]

# 단어 사전: 표면형(소문자) -> [기본형, 이 글에서의 뜻]
G = {
 "right":["right","권리"],"rights":["right","권리"],"forgotten":["forget","잊다"],"forget":["forget","잊다"],
 "privacy":["privacy","사생활"],"private":["private","비공개의, 사적인"],"public":["public","공개된, 공공의"],
 "information":["information","정보"],"already":["already","이미"],"cover":["cover","(범위를) 다루다, 포함하다"],
 "because":["because","~ 때문에"],"different":["different","다른"],"identical":["identical","똑같은"],
 "opposite":["opposite","반대의"],"hidden":["hide","숨기다 (hidden = 숨겨진)"],"distinct":["distinct","구별되는, 다른"],
 "related":["relate","관련시키다 (related = 관련된)"],"domain":["domain","영역"],"individual":["individual","개인"],
 "among":["among","~ 중에서"],"traditionally":["traditionally","전통적으로"],"regarded":["regard","여기다"],
 "protected":["protect","보호하다"],"personal":["personal","개인적인"],"revealed":["reveal","드러내다, 공개하다"],
 "contrast":["contrast","대조, 반대"],"applied":["apply","적용하다"],"applies":["apply","적용하다"],
 "broadly":["broadly","폭넓게"],"includes":["include","포함하다"],"defined":["define","규정하다, 정의하다"],
 "specific":["specific","특정한"],"point":["point","시점, 지점"],"time":["time","시간, 때"],
 "motivation":["motivation","동기, 이유"],"allow":["allow","허락하다, ~하게 해 주다"],"individuals":["individual","개인"],
 "move":["move","움직이다 (move on = 털고 나아가다)"],"lives":["life","삶"],"life":["life","삶"],
 "event":["event","사건"],"period":["period","기간"],"example":["example","예시"],
 "recognized":["recognize","인정하다, 인식하다"],"countries":["country","나라"],"criminal":["criminal","범죄의"],
 "convictions":["conviction","유죄 판결"],"eventually":["eventually","결국"],"spent":["spend","(효력이) 소멸되다 (여기서는 '쓰다' 아님)"],
 "continue":["continue","계속하다, 이어 가다"],"affect":["affect","영향을 미치다"],"person":["person","사람"],
 "despite":["despite","~에도 불구하고"],"reason":["reason","이유"],"reasons":["reason","이유"],
 "supporting":["support","지지하다"],"sometimes":["sometimes","때때로"],"come":["come","오다 (come into conflict = 충돌하다)"],
 "conflict":["conflict","충돌, 갈등"],"other":["other","다른"],"formal":["formal","공식적인"],
 "exceptions":["exception","예외"],"exception":["exception","예외"],"made":["make","만들다"],
 "security":["security","안보, 보안"],"health":["health","건강, 보건"],"forever":["forever","영원히"],
 "labeled":["label","낙인찍다, 이름 붙이다"],"judged":["judge","판단하다"],"rewarded":["reward","보상하다"],
 "reward":["reward","보상"],"rewards":["reward","보상"],"remember":["remember","기억하다"],"end":["end","끝내다"],
 "helps":["help","돕다"],"past":["past","과거"],"clash":["clash","충돌하다, 부딪치다"],"exemptions":["exemption","예외, 면제"],
 "exemption":["exemption","예외, 면제"],"penalties":["penalty","처벌"],"agree":["agree","일치하다, 동의하다"],
 "merge":["merge","합쳐지다"],"label":["label","낙인찍다, 이름 붙이다"],"fee":["fee","요금, 비용"],
 "park":["park","공원"],"opinion":["opinion","의견"],"mistake":["mistake","실수"],"mistakes":["mistake","실수"],
 "students":["student","학생"],"ideas":["idea","생각"],"often":["often","자주"],"study":["study","공부하다"],
 "school":["school","학교"],"people":["person","사람들"],"open":["open","열려 있는"],"get":["get","얻다, 받다"],
 "continue":["continue","계속하다, 이어 가다"],"relate":["relate","관련시키다"],
 "kept":["keep","유지하다"],"strictly":["strictly","엄격하게"],"revealed":["reveal","드러내다, 공개하다"],
 "protect":["protect","보호하다"],"affects":["affect","영향을 미치다"],"public domain":["public domain","공공의 영역"],
 "regard":["regard","여기다"],"fact":["fact","사실"],
}

# 직독직해 조각
JD={
 1:[["The right to be forgotten is [[different]]","잊힐 권리는 [[다르다]]"],
    ["from the right to privacy","사생활 권리와"],
    ["because it can cover information","왜냐하면 그것이 정보를 다룰 수 있기 때문이다"],
    ["that is already [[public]].","이미 [[공개된]]."]],
 2:[["The right to be forgotten helps people [[continue]] their lives","잊힐 권리는 사람들이 자신의 삶을 [[이어 가도록]] 돕는다"],
    ["without being forever [[labeled]]","영원히 [[규정되지]] 않고"],
    ["by one event in the past.","과거의 한 사건에 의해."]],
 3:[["The right to be forgotten can sometimes [[clash]]","잊힐 권리는 때때로 [[충돌할]] 수 있다"],
    ["with other rights,","다른 권리와,"],
    ["so [[exemptions]] are made","그래서 [[예외]]가 만들어진다"],
    ["for security or public health reasons.","안보나 공공 보건의 이유로."]],
}

FC={
 1:[["본문 1~2번","잊힐 권리 vs 사생활 권리","둘은 구별되지만 관련이 있어요. 사생활 권리는 보호 정보를 공개하지 않을 권리예요."],
    ["본문 3번","In contrast! 이미 공개된 정보에도 적용","사생활 권리와 달리 잊힐 권리는 공개된 영역의 정보도 다뤄요."],
    ["정답 포인트","{{distinct|구별되는}} = {{different|다른}}, {{public domain|공공의 영역}} = {{public|공개된}}","본문 표현이 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 4번","특정 시점의 정보로 영원히 규정되지 않을 권리","한 순간의 정보가 평생 따라다니지 않게 해요."],
    ["본문 5~6번","한 사건에 묶이지 않고 삶을 이어 간다","영국·프랑스의 과거 유죄 판결 소멸이 예예요."],
    ["정답 포인트","{{move on|털고 나아가다}} = {{continue|이어 가다}}, {{defined|규정되는}} = {{labeled|낙인찍히는}}","뜻이 같은 말을 찾으면 돼요."]],
 3:[["본문 7번","Despite! 반전 문장","좋은 이유가 있어도 다른 권리와 부딪힐 수 있어요."],
    ["본문 8번","For example! 안보·공중 보건의 예외","충돌할 때 공식적인 예외가 만들어져요."],
    ["정답 포인트","{{conflict|충돌}} = {{clash|충돌하다}}, {{exceptions|예외}} = {{exemptions|예외, 면제}}","바뀐 단어가 어렵게 느껴져도 뜻은 같아요."]],
}

STORY=[
 dict(a="distinct",form="distinct",n=1,sq=1,sum="is [[different]] from the right to privacy",hook="잊힐 권리와 사생활 권리는 닮았지만 다르다는 첫 문장의 distinct(구별되는) → 요약문에서는 different(다른)로 바뀌었어요."),
 dict(a="define",form="defined",n=4,sq=2,sum="without being forever [[labeled]]",hook="한 시점의 정보로 평생 규정되지 않는다는 문장의 defined(규정되는) → 요약문에서는 labeled(낙인찍히는)로 바뀌었어요."),
 dict(a="conflict",form="conflict",n=7,sq=3,sum="can sometimes [[clash]] with other rights",hook="Despite로 꺾이며 다른 권리와 부딪힌다는 문장의 conflict(충돌) → 요약문에서는 clash(충돌하다)로 바뀌었어요."),
 dict(a="exception",form="exceptions",n=8,sq=3,sum="so [[exemptions]] are made",hook="안보나 공중 보건 때문에 따로 허용된다는 문장의 exceptions(예외) → 요약문에서는 exemptions(예외, 면제)로 바뀌었어요."),
]

SCENES=[
 dict(tag="본문 1~3번",ns=[1,2,3],line="잊힐 권리와 사생활 권리는 [[distinct|구별되는]] 권리다. 잊힐 권리는 이미 공개된 정보에도 적용된다."),
 dict(tag="본문 4~6번",ns=[4,5,6],line="한 시점의 정보에 평생 [[defined|규정되지]] 않고 삶을 이어 가게 하려는 권리다."),
 dict(tag="본문 7번",ns=[7],line="하지만 다른 권리와 [[conflict|충돌]]할 수도 있다."),
 dict(tag="본문 8번",ns=[8],line="그래서 안보·공중 보건 때문에 공식적인 [[exceptions|예외]]가 만들어진다."),
]

HLKO={1:["구별되지만"],3:["공공의 영역에 있었던 정보"],4:["영원히 정의되지 않아야"],5:["자신의 삶을 이어 나가고"],7:["다른 권리와 때때로 충돌할 수 있다"],8:["공식적인 예외"]}

UM={'different':('다른','다르다'),'public':('공개된, 공공의','일반 대중'),'continue':('계속하다, 이어 가다','계속'),'label':('낙인찍다, 이름 붙이다','낙인을 찍지'),'clash':('충돌하다, 부딪치다','충돌한다'),'exemption':('면제, 예외','면제받는다')}

TARGET={1:2,2:4,3:0}

G.update({'without':['without','~ 없이'],'being':['be','~되는 (being = ~되는 것)'],'such':['such','그러한'],'into':['into','~ 안으로 (come into conflict = 충돌하다)']})
