# -*- coding: utf-8 -*-
# 세트 정의: 금천고2 4과 ❹
META=dict(sch='jusung-go2', src='jusung-go2/L4/sx-data.js', pidx=3, lesson='4과', title='수리할 권리와 수리 카페', label='❹', page='yoyak-lian-z4')
Q = [
 dict(
  id=1,
  summary="First, companies must make information about their products (A) to the public, and third parties, including individuals, should be able to (B) the parts and tools needed for repairs.",
  ko="첫째, 회사들은 제품에 대한 정보를 대중에게 <b>(A) 접근 가능하게</b> 만들어야 하고, 개인을 포함한 제삼자가 수리에 필요한 부품과 도구를 <b>(B) 얻을</b> 수 있어야 한다.",
  opts=[["accessible","acquire"],["accessible","destroy"],["confidential","acquire"],["confidential","restrict"],["affordable","replace"]],
  optko=["접근 가능한 – 얻다","접근 가능한 – 파괴하다","기밀의 – 얻다","기밀의 – 제한하다","가격이 알맞은 – 교체하다"],
  ans=0,
  wrong=[None,
         "destroy(파괴하다)가 틀려요. 제삼자는 부품과 도구를 없애는 게 아니라 구할(obtain) 수 있어야 해요.",
         "confidential(기밀의)이 틀려요. 정보는 숨기는 게 아니라 모두가 이용할 수 있게(available) 해야 해요.",
         "둘 다 틀려요. 정보는 기밀이 아니라 공개해야 하고, 부품과 도구도 제한(restrict)이 아니라 구할 수 있게 해야 해요.",
         "둘 다 틀려요. affordable(가격이 알맞은)과 replace(교체하다)는 본문에 없어요. 본문은 정보 공개와 부품·도구 구하기예요."],
  evid=[dict(n=1, hl=["make information about their products available to everyone"]), dict(n=2, hl=["obtain the parts and tools"])],
  swaps=[["available","accessible","이용할 수 있는 → 접근 가능한"],["obtain","acquire","구하다 → 얻다, 입수하다"],["required","needed","필요한 → 필요한"],["everyone","the public","모두 → 대중"]],
  swapnote="available(이용할 수 있는)은 accessible(접근 가능한)로, obtain(구하다)은 acquire(얻다)로 바뀌어 나와요. 본문 단어만 찾지 말고 뜻이 같은 말을 찾으세요.",
  use=[dict(w="accessible",ex="The library is accessible to all students.",ko="그 도서관은 모든 학생이 이용할 수 있다."),
       dict(w="acquire",ex="He acquired a new skill by practicing every day.",ko="그는 매일 연습해서 새로운 기술을 얻었다.")],
  flow="본문 1번(첫 번째 요구)은 회사가 제품 정보를 모두에게 공개하는 것, 2번(두 번째 요구)은 개인도 수리용 부품과 도구를 구할 수 있어야 한다는 거예요.",
 ),
 dict(
  id=2,
  summary="By law, companies should be (A) from stopping consumers from installing custom software on their own devices, and manufacturers should design devices so that repairs are as (B) as possible.",
  ko="법적으로 회사들은 소비자들이 자신의 장치에 맞춤형 소프트웨어를 설치하지 못하게 막는 것이 <b>(A) 금지되어야</b> 하고, 제조사들은 수리가 최대한 <b>(B) 간단하도록</b> 장치를 설계해야 한다.",
  opts=[["banned","straightforward"],["banned","complicated"],["encouraged","straightforward"],["encouraged","complicated"],["permitted","expensive"]],
  optko=["금지된 – 간단한","금지된 – 복잡한","권장된 – 간단한","권장된 – 복잡한","허용된 – 비싼"],
  ans=0,
  wrong=[None,
         "complicated(복잡한)가 틀려요. 제조사는 수리를 최대한 쉽게(easy) 만들어야 해요.",
         "encouraged(권장된)가 틀려요. 소비자가 소프트웨어를 설치하지 못하게 막는 행위는 권장이 아니라 법으로 금지(prohibited)돼야 해요.",
         "둘 다 틀려요. 막는 행위는 권장이 아니라 금지돼야 하고, 수리는 복잡한 게 아니라 쉬워야 해요.",
         "둘 다 틀려요. permitted(허용된)는 금지와 정반대이고, expensive(비싼)는 본문에 없어요."],
  evid=[dict(n=3, hl=["preventing consumers from installing custom software","prohibited by law"]), dict(n=4, hl=["makes repairs as easy as possible"])],
  swaps=[["prohibited","banned","금지된 → 금지된"],["easy","straightforward","쉬운 → 간단한, 명료한"],["preventing","stopping","막는 → 막는"],["install","installing","설치하다 → 설치하는"]],
  swapnote="prohibited(금지된)는 banned(금지된)나 forbidden(금지된)으로, easy(쉬운)는 simple(간단한)이나 straightforward(간단한)로 바뀌어 나와요.",
  use=[dict(w="ban",ex="The school banned phones in the classroom.",ko="그 학교는 교실에서 휴대폰을 금지했다."),
       dict(w="straightforward",ex="The instructions were straightforward, so everyone understood them.",ko="설명서가 간단해서 모두가 이해했다.")],
  flow="본문 3번(세 번째 요구)은 소비자가 자기 장치에 소프트웨어를 설치하는 걸 막는 행위를 법으로 금지하자는 거고, 4번(마지막 요구)은 제조사가 수리하기 쉽게 설계하라는 거예요.",
 ),
 dict(
  id=3,
  summary="Supporters believe that achieving these goals will greatly (A) e-waste, and the movement's (B) is growing in Europe as well as in the U.S.",
  ko="지지자들은 이 목표들을 달성하면 전자 쓰레기가 크게 <b>(A) 줄어들 것</b>이라고 믿고, 이 운동의 <b>(B) 영향력</b>은 미국뿐 아니라 유럽에서도 커지고 있다.",
  opts=[["diminish","impact"],["diminish","opposition"],["increase","impact"],["increase","opposition"],["eliminate","impact"]],
  optko=["줄이다 – 영향력","줄이다 – 반대","늘리다 – 영향력","늘리다 – 반대","없애다 – 영향력"],
  ans=0,
  wrong=[None,
         "opposition(반대)이 틀려요. 본문은 이 운동의 영향력(influence)이 커지고 있다고 해요.",
         "increase(늘리다)가 틀려요. 목표가 이뤄지면 전자 쓰레기는 훨씬 적게(far less) 나와요.",
         "둘 다 틀려요. 전자 쓰레기는 늘어나는 게 아니라 줄고, 커지는 건 반대가 아니라 영향력이에요.",
         "eliminate(없애다)가 틀려요. 본문은 완전히 없앤다가 아니라 훨씬 적게(far less) 나온다고 해요."],
  evid=[dict(n=5, hl=["far less e-waste will be generated"]), dict(n=6, hl=["more than 40 states in the U.S."]), dict(n=7, hl=["growing influence in Europe"])],
  swaps=[["influence","impact","영향력 → 영향, 파급력"],["less","diminish","훨씬 적게 나오다 → 줄이다"],["advocates","supporters","지지자들 → 지지자들"],["accomplished","achieving","이루어진 → 달성하는"]],
  swapnote="influence(영향력)는 impact(영향)로 바뀌고, 'far less e-waste will be generated(전자 쓰레기가 훨씬 적게 나온다)'는 'diminish e-waste(전자 쓰레기를 줄이다)'로 바뀌어 나와요.",
  use=[dict(w="diminish",ex="Regular exercise can diminish stress.",ko="규칙적인 운동은 스트레스를 줄여 줄 수 있다."),
       dict(w="impact",ex="The new law had a big impact on small shops.",ko="그 새 법은 작은 가게들에 큰 영향을 주었다.")],
  flow="본문 5번에서 목표가 이뤄지면 전자 쓰레기가 훨씬 적게 나온다고 하고, 6번에서 미국 40개 넘는 주가 움직이고, 7번에서 유럽에서도 영향력이 커진다고 이어져요.",
 ),
]

G = {
 "first":["first","첫째, 첫 번째로"],"companies":["company","회사들"],"must":["must","~해야 한다"],"make":["make","~하게 만들다"],
 "information":["information","정보"],"products":["product","제품"],"public":["public","대중"],"accessible":["accessible","접근 가능한, 이용할 수 있는"],
 "available":["available","이용할 수 있는"],"everyone":["everyone","모두"],"third":["third","세 번째의, 제삼의"],"parties":["party","(어떤 일의) 당사자, 쪽"],
 "including":["include","포함하다"],"individuals":["individual","개인"],"able":["able","~할 수 있는"],"acquire":["acquire","얻다, 입수하다"],
 "obtain":["obtain","구하다, 얻다"],"parts":["part","부품"],"tools":["tool","도구"],"needed":["need","필요하다 (needed = 필요한)"],
 "required":["require","필요로 하다 (required = 필요한)"],"repairs":["repair","수리"],"repair":["repair","수리하다, 수리"],
 "destroy":["destroy","파괴하다"],"confidential":["confidential","기밀의, 비밀의"],"restrict":["restrict","제한하다"],
 "affordable":["affordable","가격이 알맞은"],"replace":["replace","교체하다, 대체하다"],"should":["should","~해야 한다"],
 "practice":["practice","관행, 행위"],"preventing":["prevent","막다, 못하게 하다"],"stopping":["stop","막다"],"consumers":["consumer","소비자"],
 "installing":["install","설치하다"],"custom":["custom","맞춤형의"],"software":["software","소프트웨어"],"own":["own","자기 자신의"],
 "devices":["device","장치, 기기"],"prohibited":["prohibit","금지하다 (prohibited = 금지된)"],"law":["law","법"],"banned":["ban","금지하다 (banned = 금지된)"],
 "ban":["ban","금지하다"],"finally":["finally","마지막으로"],"demands":["demand","요구하다"],"manufacturers":["manufacturer","제조사"],
 "design":["design","설계하다"],"way":["way","방식"],"easy":["easy","쉬운"],"possible":["possible","가능한"],
 "straightforward":["straightforward","간단한, 알기 쉬운"],"complicated":["complicated","복잡한"],"encouraged":["encourage","권장하다 (encouraged = 권장된)"],
 "permitted":["permit","허용하다 (permitted = 허용된)"],"expensive":["expensive","비싼"],"phones":["phone","휴대폰"],"school":["school","학교"],
 "classroom":["classroom","교실"],"instructions":["instruction","설명서, 지시"],"understood":["understand","이해하다"],"everyone":["everyone","모두"],
 "advocates":["advocate","지지자"],"supporters":["supporter","지지자"],"movement":["movement","(사회) 운동"],"movement's":["movement","(사회) 운동"],
 "goals":["goal","목표"],"accomplished":["accomplish","이루다 (accomplished = 이루어진)"],"achieving":["achieve","달성하다"],
 "less":["less","더 적은"],"e-waste":["e-waste","전자 쓰레기"],"generated":["generate","만들어 내다, 발생시키다"],"greatly":["greatly","크게"],
 "believe":["believe","믿다"],"diminish":["diminish","줄이다, 감소시키다"],"reduce":["reduce","줄이다"],"increase":["increase","늘리다"],
 "eliminate":["eliminate","없애다"],"impact":["impact","영향"],"opposition":["opposition","반대"],"influence":["influence","영향력"],
 "growing":["grow","커지다 (growing = 커지는)"],"europe":["Europe","유럽"],"states":["state","(미국의) 주"],"efforts":["effort","노력"],
 "thanks":["thanks to","~ 덕분에"],"legislation":["legislation","법률 제정, 법률"],"working":["work","노력하다, 일하다"],"begun":["begin","시작하다"],
 "gaining":["gain","얻다"],"countries":["country","나라, 국가"],"joining":["join","동참하다, 함께하다"],"cause":["cause","대의, 목적"],
 "library":["library","도서관"],"students":["student","학생"],"skill":["skill","기술"],"practicing":["practice","연습하다"],"acquired":["acquire","얻다"],
 "exercise":["exercise","운동"],"regular":["regular","규칙적인"],"stress":["stress","스트레스"],"shops":["shop","가게"],"small":["small","작은"],
 "regular":["regular","규칙적인"],"phone":["phone","휴대폰"],"banned":["ban","금지하다 (banned = 금지된)"],
 "right-to-repair":["right-to-repair","수리할 권리"],"u.s.":["U.S.","미국"],"help":["help","돕다"],
}

JD={
 1:[["First, companies must make information about their products [[accessible]]","첫째, 회사들은 제품에 대한 정보를 [[접근 가능하게]] 만들어야 한다"],
    ["to the public,","대중에게,"],
    ["and third parties, including individuals,","그리고 개인을 포함한 제삼자가"],
    ["should be able to [[acquire]]","[[얻을]] 수 있어야 한다"],
    ["the parts and tools needed for repairs.","수리에 필요한 부품과 도구를."]],
 2:[["By law, companies should be [[banned]]","법적으로 회사들은 [[금지되어야]] 한다"],
    ["from stopping consumers from installing custom software","소비자들이 맞춤형 소프트웨어를 설치하지 못하게 막는 것이"],
    ["on their own devices,","자신의 장치에,"],
    ["and manufacturers should design devices","그리고 제조사들은 장치를 설계해야 한다"],
    ["so that repairs are as [[straightforward]] as possible.","수리가 최대한 [[간단하도록]]."]],
 3:[["Supporters believe","지지자들은 믿는다"],
    ["that achieving these goals","이 목표들을 달성하면"],
    ["will greatly [[diminish]] e-waste,","전자 쓰레기를 크게 [[줄일 것이라고]],"],
    ["and the movement's [[impact]] is growing","그리고 이 운동의 [[영향력]]이 커지고 있다고"],
    ["in Europe as well as in the U.S.","미국뿐 아니라 유럽에서도."]],
}

FC={
 1:[["본문 1번","첫 번째 요구: 제품 정보를 모두에게","회사가 제품 정보를 공개하라는 거예요."],
    ["본문 2번","두 번째 요구: 부품과 도구를 구하게","개인도 수리에 필요한 부품과 도구를 구할 수 있어야 해요."],
    ["정답 포인트","{{available|이용할 수 있는}} = {{accessible|접근 가능한}}, {{obtain|구하다}} = {{acquire|얻다}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 3번","세 번째 요구: 설치를 막지 마라","소비자가 자기 장치에 소프트웨어를 깔지 못하게 막는 행위는 법으로 금지!"],
    ["본문 4번","마지막 요구: 수리하기 쉽게 설계","제조사는 수리를 최대한 쉽게 만들어야 해요."],
    ["정답 포인트","{{prohibited|금지된}} = {{banned|금지된}}, {{easy|쉬운}} = {{straightforward|간단한}}","금지와 쉬움, 두 칸 모두 방향이 맞아야 해요."]],
 3:[["본문 5번","목표가 이뤄지면 전자 쓰레기가 훨씬 줄어든다","지지자들의 주장이에요."],
    ["본문 6~7번","미국 40개 넘는 주와 유럽으로 번진다","점점 더 많은 나라가 동참해요."],
    ["정답 포인트","{{far less e-waste|훨씬 적은 전자 쓰레기}} → {{diminish|줄이다}}, {{influence|영향력}} = {{impact|영향}}","커지는 건 반대가 아니라 영향력이에요."]],
}

STORY=[
 dict(a="available",form="available",n=1,sq=1,sum="make information about their products [[accessible]] to the public",hook="제품 정보를 모두가 이용할 수 있게 하라는 문장의 available(이용할 수 있는) → 요약문에서는 accessible(접근 가능한)로 바뀌었어요."),
 dict(a="obtain",form="obtain",n=2,sq=1,sum="should be able to [[acquire]] the parts and tools",hook="수리용 부품과 도구를 구하라는 문장의 obtain(구하다) → 요약문에서는 acquire(얻다)로 바뀌었어요."),
 dict(a="prohibited",form="prohibited",n=3,sq=2,sum="companies should be [[banned]] from stopping consumers",hook="설치를 막는 행위를 법으로 막자는 문장의 prohibited(금지된) → 요약문에서는 banned(금지된)로 바뀌었어요."),
 dict(a="easy",form="easy",n=4,sq=2,sum="repairs are as [[straightforward]] as possible",hook="수리를 최대한 쉽게 하라는 마지막 요구의 easy(쉬운) → 요약문에서는 straightforward(간단한)로 바뀌었어요."),
 dict(a="influence",form="influence",n=7,sq=3,sum="the movement's [[impact]] is growing",hook="유럽에서도 힘이 커진다는 마지막 문장의 influence(영향력) → 요약문에서는 impact(영향)로 바뀌었어요."),
]

SCENES=[
 dict(tag="본문 1~2번",ns=[1,2],line="첫째, 제품 정보를 모두가 [[available|이용할 수 있게]] 하고, 둘째, 부품과 도구를 [[obtain|구할]] 수 있게 하라."),
 dict(tag="본문 3~4번",ns=[3,4],line="셋째, 소프트웨어 설치를 막는 행위는 법으로 [[prohibited|금지]]. 마지막으로, 수리를 [[easy|쉽게]] 설계하라."),
 dict(tag="본문 5~7번",ns=[5,6,7],line="목표가 이뤄지면 전자 쓰레기가 줄고, 미국 40여 개 주에 이어 유럽에서도 [[influence|영향력]]이 커지고 있다."),
]

HLKO={1:["제품에 대한 정보를 모두가 이용할 수 있게"],2:["부품들과 도구들을 구할 수 있어야"],
 3:["소비자들이 맞춤형 소프트웨어를 자신의 장치에 설치하지 못하게 하는","법으로 금지되어야"],4:["수리를 최대한 쉽게 만드는"],
 5:["훨씬 적은 전자 쓰레기가 발생할"],6:["미국 40개 이상의 주"],7:["유럽에서도 영향력이 커지고"]}

UM={'accessible':('접근 가능한, 이용할 수 있는','이용할 수 있다'),'acquire':('얻다, 입수하다','얻었다'),'ban':('금지하다','금지했다'),'straightforward':('간단한, 알기 쉬운','간단해서'),'diminish':('줄이다, 감소시키다','줄여'),'impact':('영향','영향을')}

TARGET={1:1,2:3,3:0}
G.update({'about':['about','~에 대한'],'second':['second','두 번째로'],'makes':['make','~하게 만들다'],'well':['well','잘 (as well as = ~뿐 아니라)'],'say':['say','말하다'],'far':['far','훨씬']})
