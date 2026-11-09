# -*- coding: utf-8 -*-
# 세트 정의: 주성고1 3과 ❻
META=dict(sch='jusung-go1', src='jusung-go1/L3/sx-data.js', pidx=5, lesson='3과', title='문화유산을 지킨 모뉴먼츠 맨', label='❻', page='yoyak-lian-z6')
Q = [
 dict(
  id=1,
  summary="Over 7,000 languages are (A) used around the world, but most belong to small groups, and half of them could (B) within the next generation.",
  ko="7,000개가 넘는 언어가 전 세계에서 <b>(A) 현재</b> 사용되고 있지만 대부분은 소규모 집단에 속하고, 그중 절반은 다음 세대 이내에 <b>(B) 사라질</b> 수 있다.",
  opts=[["presently","vanish"],["presently","grow"],["rarely","vanish"],["rarely","grow"],["formerly","spread"]],
  optko=["현재 – 사라지다","현재 – 늘어나다","거의 ~않게 – 사라지다","거의 ~않게 – 늘어나다","예전에 – 퍼지다"],
  ans=0,
  wrong=[None,
         "grow(늘어나다)가 틀려요. 본문은 절반이 사라질(disappear) 수도 있다고 해요.",
         "rarely(거의 ~않게)가 틀려요. 본문은 지금(currently) 7,000개가 넘는 언어가 쓰이고 있다고 해요.",
         "둘 다 틀려요. 지금도 쓰이고 있고, 절반은 사라질 수 있다는 내용이에요.",
         "둘 다 틀려요. formerly(예전에)는 지금 쓰이는 언어라는 내용과 안 맞고, spread(퍼지다)는 본문과 반대예요."],
  evid=[dict(n=1, hl=["currently being used around the world"]), dict(n=2, hl=["small groups of people","could disappear within the next generation"])],
  swaps=[["currently","presently","현재 → 지금, 현재"],["disappear","vanish","사라지다 → 사라지다(자취를 감추다)"],["spoken","belong to","(언어가) 사용되다 → (언어가) ~에 속하다"]],
  swapnote="currently(현재)는 presently(지금)로, disappear(사라지다)는 vanish(사라지다)로 바뀌어 나와요. 본문 단어만 찾지 말고 같은 뜻의 말을 찾으세요.",
  use=[dict(w="presently",ex="The museum is presently closed for repairs.",ko="그 박물관은 현재 수리를 위해 문을 닫았다."),
       dict(w="vanish",ex="The old village seemed to vanish after the flood.",ko="그 오래된 마을은 홍수 뒤에 사라진 것 같았다.")],
  flow="본문 1번에서 지금 7,000개가 넘는 언어가 쓰이고 있다고 시작해요. 2번에서 대부분이 소규모 집단의 언어이고 절반은 곧 사라질 수 있다는 반전이 나와요.",
 ),
 dict(
  id=2,
  summary="Language is important for (A) people's identity with their culture, so losing it would be a great loss, and that is why some organizations work to (B) languages.",
  ko="언어는 사람들의 정체성을 그들의 문화와 <b>(A) 연결하는</b> 데 중요하므로 언어를 잃는 것은 큰 손실이고, 그래서 일부 단체가 언어를 <b>(B) 보호하려고</b> 노력한다.",
  opts=[["linking","protect"],["linking","replace"],["separating","protect"],["separating","replace"],["copying","ignore"]],
  optko=["연결하는 – 보호하다","연결하는 – 대체하다","분리하는 – 보호하다","분리하는 – 대체하다","따라 하는 – 무시하다"],
  ans=0,
  wrong=[None,
         "replace(대체하다)가 틀려요. 단체들은 언어를 다른 것으로 바꾸는 게 아니라 보존(preserve)하려고 해요.",
         "separating(분리하는)이 틀려요. 언어는 정체성을 문화와 연결(connect)해 줘요.",
         "둘 다 틀려요. 언어는 정체성과 문화를 연결해 주고, 단체들은 언어를 지키려고 해요.",
         "둘 다 틀려요. copying(따라 하는)도 ignore(무시하다)도 본문에 없어요."],
  evid=[dict(n=3, hl=["a great loss","connecting people’s identity to their culture"]), dict(n=4, hl=["work to preserve them"])],
  swaps=[["connect","link","연결하다 → 연결하다, 잇다"],["preserve","protect","보존하다 → 보호하다"],["plays a big role in","is important for","큰 역할을 하다 → ~에 중요하다"]],
  swapnote="connect(연결하다)는 link(잇다)로, preserve(보존하다)는 protect(보호하다)로도 바뀌어 나와요. 뜻이 같은 짝으로 기억해 두세요.",
  use=[dict(w="link",ex="Roads link the small town to the big city.",ko="도로는 그 작은 마을을 큰 도시와 연결한다."),
       dict(w="protect",ex="We should protect old buildings for the future.",ko="우리는 미래를 위해 오래된 건물을 보호해야 한다.")],
  flow="본문 3번은 언어를 잃으면 왜 큰 손실인지(정체성과 문화를 이어 주니까) 말해요. 4번의 This is why로 그래서 단체들이 언어를 지키려 한다고 이어져요.",
 ),
 dict(
  id=3,
  summary="The nonprofit group Wikitongues aims to save endangered languages by (A) speakers on video and making language resources more (B).",
  ko="비영리 단체 Wikitongues는 화자들을 영상으로 <b>(A) 촬영하고</b> 언어 자원을 더 <b>(B) 이용 가능하게</b> 만들어 소멸 위기의 언어를 지키려 한다.",
  opts=[["filming","available"],["filming","limited"],["erasing","limited"],["erasing","available"],["translating","expensive"]],
  optko=["촬영하는 – 이용 가능한","촬영하는 – 제한된","지우는 – 제한된","지우는 – 이용 가능한","번역하는 – 비싼"],
  ans=0,
  wrong=[None,
         "limited(제한된)가 틀려요. 본문은 자원을 더 접근하기 쉽게(accessible) 만든다고 해요.",
         "둘 다 틀려요. 영상을 지우는 게 아니라 기록하고, 자원은 제한이 아니라 접근하기 쉽게 만들어요.",
         "erasing(지우는)이 틀려요. 영상을 지우는 게 아니라 기록(record)해요.",
         "둘 다 틀려요. 번역하거나 비싸게 만든다는 말은 본문에 없어요."],
  evid=[dict(n=5, hl=["Wikitongues","preserving all languages that are in danger of being lost"]), dict(n=6, hl=["recording videos of individuals speaking these languages","more accessible"])],
  swaps=[["record","film","기록하다 → 촬영하다"],["accessible","available","접근 가능한 → 이용할 수 있는"],["in danger of being lost","endangered","사라질 위험에 처한 → 멸종 위기의"]],
  swapnote="accessible(접근 가능한)은 available(이용할 수 있는)로 바뀌어 나와요. in danger of being lost처럼 긴 말이 endangered(위기에 처한) 한 단어로 줄어들기도 해요.",
  use=[dict(w="film",ex="Students film short videos for their school project.",ko="학생들은 학교 과제를 위해 짧은 영상을 촬영한다."),
       dict(w="available",ex="The map is available on the school website.",ko="그 지도는 학교 웹사이트에서 이용할 수 있다.")],
  flow="본문 5번에서 Wikitongues가 For example(예를 들어)로 등장해 위기의 언어를 모두 지키겠다는 목표를 말해요. 6번에서 그 방법, 영상 기록과 자료 공개가 나와요.",
 ),
]

G = {
 "over":["over","~이 넘는"],"languages":["language","언어"],"language":["language","언어"],"are":["be","~이다, ~에 있다"],"is":["be","~이다"],
 "used":["use","사용하다 (used = 사용되는)"],"around":["around","~ 전역에서, 주위에"],"world":["world","세계"],
 "most":["most","대부분"],"belong":["belong","속하다 (belong to = ~에 속하다)"],"small":["small","작은"],"groups":["group","집단, 무리"],
 "half":["half","절반"],"could":["can","~할 수도 있다 (could = 가능성)"],"within":["within","~ 이내에"],"next":["next","다음의"],
 "generation":["generation","세대"],"presently":["presently","현재, 지금"],"vanish":["vanish","사라지다"],"grow":["grow","늘어나다, 자라다"],
 "rarely":["rarely","거의 ~않게"],"formerly":["formerly","예전에"],"spread":["spread","퍼지다"],"currently":["currently","현재"],
 "being":["be","~이다 (being used = 사용되고 있는)"],"spoken":["speak","말하다 (spoken = 사용되는)"],"very":["very","매우"],
 "people":["people","사람들"],"people's":["people","사람들의"],"people’s":["people","사람들의"],"disappear":["disappear","사라지다"],"these":["these","이"],
 "important":["important","중요한"],"linking":["link","연결하다, 잇다"],"link":["link","연결하다, 잇다"],"identity":["identity","정체성"],
 "with":["with","~와 함께"],"their":["their","그들의"],"culture":["culture","문화"],"so":["so","그래서"],"losing":["lose","잃다"],
 "would":["will","~일 것이다"],"great":["great","큰"],"loss":["loss","손실"],"that":["that","그것"],"why":["why","이유"],
 "some":["some","일부"],"organizations":["organization","단체, 조직"],"work":["work","노력하다, 일하다"],"protect":["protect","보호하다"],
 "replace":["replace","대체하다"],"separating":["separate","분리하다"],"copying":["copy","따라 하다, 복사하다"],"ignore":["ignore","무시하다"],
 "connecting":["connect","연결하다"],"connect":["connect","연결하다"],"plays":["play","(역할을) 하다"],"role":["role","역할"],"big":["big","큰"],
 "preserve":["preserve","보존하다"],"preserving":["preserve","보존하다"],"them":["they","그것들"],"because":["because","~ 때문에"],
 "nonprofit":["nonprofit","비영리의"],"group":["group","집단, 단체"],"aims":["aim","목표로 하다"],"save":["save","지키다, 구하다"],
 "endangered":["endangered","멸종·소멸 위기에 처한"],"filming":["film","촬영하다"],"film":["film","촬영하다"],"speakers":["speaker","(언어를) 말하는 사람, 화자"],
 "video":["video","영상"],"videos":["video","영상"],"making":["make","만들다"],"resources":["resource","자원, 자료"],"more":["more","더"],
 "available":["available","이용할 수 있는"],"limited":["limited","제한된"],"erasing":["erase","지우다"],"translating":["translate","번역하다"],
 "expensive":["expensive","비싼"],"accessible":["accessible","접근하기 쉬운"],"record":["record","기록하다"],"recording":["record","기록하다"],
 "individuals":["individual","개인"],"speaking":["speak","말하다"],"set":["set","(목표를) 세우다"],"goal":["goal","목표"],"danger":["danger","위험"],
 "lost":["lose","잃다"],"wikitongues":["Wikitongues","위키텅스 (언어 보존 비영리 단체 이름)"],"organization":["organization","단체"],
 "called":["call","~라고 부르다"],"achieve":["achieve","달성하다"],"mother-tongue":["mother tongue","모국어"],"disappeared":["disappear","사라지다"],
 "currently":["currently","현재"],"museum":["museum","박물관"],"closed":["close","닫다 (closed = 닫힌)"],"repairs":["repair","수리"],
 "village":["village","마을"],"flood":["flood","홍수"],"roads":["road","도로"],"town":["town","마을, 소도시"],"city":["city","도시"],
 "buildings":["building","건물"],"future":["future","미래"],"students":["student","학생"],"short":["short","짧은"],"project":["project","과제, 프로젝트"],
 "map":["map","지도"],"website":["website","웹사이트"],"school":["school","학교"],"old":["old","오래된"],"seemed":["seem","~처럼 보이다"],
 "after":["after","~ 뒤에"],"should":["should","~해야 한다"],"belong":["belong","속하다"],"mother":["mother","어머니"],"tongue":["tongue","혀, 말(언어)"],
 "real":["real","진짜의"],"world's":["world","세계의"],
}

JD={
 1:[["Over 7,000 languages are [[presently]] used","7,000개가 넘는 언어가 [[현재]] 사용되고 있다"],
    ["around the world,","전 세계에서,"],
    ["but most belong to small groups,","하지만 대부분은 소규모 집단에 속하고,"],
    ["and half of them could [[vanish]]","그중 절반은 [[사라질]] 수 있다"],
    ["within the next generation.","다음 세대 이내에."]],
 2:[["Language is important","언어는 중요하다"],
    ["for [[linking]] people's identity with their culture,","사람들의 정체성을 그들의 문화와 [[연결하는]] 데,"],
    ["so losing it would be a great loss,","그래서 언어를 잃는 것은 큰 손실일 것이고,"],
    ["and that is why some organizations work to [[protect]] languages.","그것이 일부 단체가 언어를 [[보호하려고]] 노력하는 이유이다."]],
 3:[["The nonprofit group Wikitongues aims to save endangered languages","비영리 단체 Wikitongues는 소멸 위기의 언어를 지키려 한다"],
    ["by [[filming]] speakers on video","화자들을 영상으로 [[촬영하고]]"],
    ["and making language resources more [[available]].","언어 자원을 더 [[이용 가능하게]] 만듦으로써."]],
}

FC={
 1:[["본문 1번","지금 7,000개가 넘는 언어가 쓰이고 있다","{{currently|현재}} 전 세계에서 쓰이는 언어 수예요."],
    ["본문 2번","But! 대부분 소규모 집단의 언어","절반은 다음 세대 안에 사라질 수도 있어요."],
    ["정답 포인트","{{currently|현재}} = {{presently|지금}}, {{disappear|사라지다}} = {{vanish|사라지다}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 3번","언어를 잃으면 큰 손실","언어가 정체성과 문화를 이어 주기 때문이에요."],
    ["본문 4번","그래서 단체들이 언어를 지킨다","{{This is why|이것이 ~하는 이유이다}}로 이어져요."],
    ["정답 포인트","{{connect|연결하다}} = {{link|잇다}}, {{preserve|보존하다}} = {{protect|보호하다}}","두 칸 모두 같은 뜻의 말로 바뀌었어요."]],
 3:[["본문 5번","예: Wikitongues의 목표","{{For example|예를 들어}}로 사례가 시작돼요. 위기의 언어를 모두 보존해요."],
    ["본문 6번","방법 ① 영상 기록 ② 자료를 쉽게","화자들의 영상을 기록하고 자료에 더 쉽게 접근하게 해요."],
    ["정답 포인트","{{record|기록하다}} = {{film|촬영하다}}, {{accessible|접근 가능한}} = {{available|이용할 수 있는}}","본문 단어가 뜻이 같은 말로 바뀌었어요."]],
}

STORY=[
 dict(a="currently",form="currently",n=1,sq=1,sum="are [[presently]] used",hook="7,000개가 넘는 언어가 지금 쓰이고 있다는 첫 문장의 currently(현재) → 요약문에서는 presently(지금)로 바꿨어요."),
 dict(a="disappear",form="disappear",n=2,sq=1,sum="could [[vanish]] within",hook="절반이 곧 사라질 수 있다는 문장의 disappear(사라지다) → 요약문에서는 vanish(사라지다)로 바꿨어요."),
 dict(a="connect",form="connecting",n=3,sq=2,sum="for [[linking]] people's identity",hook="언어가 정체성과 문화를 이어 준다는 문장의 connecting(연결하는) → 요약문에서는 linking(잇는)으로 바꿨어요."),
 dict(a="preserve",form="preserve",n=4,sq=2,sum="work to [[protect]] languages",hook="그래서 단체들이 언어를 지키려 한다는 문장의 preserve(보존하다) → 요약문에서는 protect(보호하다)로 바꿨어요."),
 dict(a="record",form="recording",n=6,sq=3,sum="by [[filming]] speakers",hook="화자들의 영상을 남긴다는 문장의 recording(기록하는 것) → 요약문에서는 filming(촬영하는 것)으로 바꿨어요."),
 dict(a="accessible",form="accessible",n=6,sq=3,sum="more [[available]]",hook="자료를 누구나 쉽게 쓰게 한다는 문장의 accessible(접근 가능한) → 요약문에서는 available(이용할 수 있는)로 바뀌었어요."),
]

SCENES=[
 dict(tag="본문 1~2번",ns=[1,2],line="[[currently|현재]] 7,000개가 넘는 언어가 쓰이지만, 절반은 곧 [[disappear|사라질]] 수 있다."),
 dict(tag="본문 3번",ns=[3],line="언어는 정체성과 문화를 [[connecting|연결해]] 주니, 잃으면 큰 손실이다."),
 dict(tag="본문 4번",ns=[4],line="그래서 일부 단체가 언어를 [[preserve|보존하려고]] 일한다."),
 dict(tag="본문 5~6번",ns=[5,6],line="Wikitongues는 화자들의 영상을 [[recording|기록하고]] 자료를 더 [[accessible|접근하기 쉽게]] 만든다."),
]

HLKO={1:["현재 전 세계에서 7,000개가 넘는 언어가 사용되고 있다"],
 2:["매우 소규모 집단의 사람들","다음 세대 이내에 사라질 수도 있다"],
 3:["큰 손실","정체성을 그들의 문화와 연결하는"],
 4:["언어를 보존하기 위해 일하는"],
 5:["Wikitongues","소멸될 위험에 처한 모든 언어들을 보존한다는 목표"],
 6:["이 언어들을 사용하는 개인들의 영상을 기록하고","더 접근 가능하게"]}

UM={'presently':('현재, 지금','현재'),'vanish':('사라지다','사라진'),'link':('연결하다','연결한다'),'protect':('보호하다','보호해야'),'film':('촬영하다','촬영한다'),'available':('이용할 수 있는','이용할 수'),}

TARGET={1:3,2:0,3:2}

G.update({'know':['know','알다'],'example':['example','예, 예시'],'works':['work','노력하다, 일하다']})
