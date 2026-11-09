# -*- coding: utf-8 -*-
# 세트 정의: 금천고2 4과 ❸
META=dict(sch='jusung-go2', src='jusung-go2/L4/sx-data.js', pidx=2, lesson='4과', title='수리할 권리와 수리 카페', label='❸', page='yoyak-lian-z3')
Q = [
 dict(
  id=1,
  summary="Many people discard damaged devices because they are hard to repair, as some are difficult to take apart and some makers oblige customers to bring them to an official service center.",
  ko="많은 사람이 고장 난 장치를 <b>(A) 버리는데</b>, 수리하기 어렵기 때문이다. 어떤 것은 분해하기 어렵고, 어떤 제조사는 고객이 공식 수리소로 가져오도록 <b>(B) 강제한다</b>.",
  opts=[["discard","oblige"],["discard","permit"],["preserve","oblige"],["preserve","permit"],["donate","forbid"]],
  optko=["버리다 – 강제하다","버리다 – 허용하다","보존하다 – 강제하다","보존하다 – 허용하다","기부하다 – 금지하다"],
  ans=0,
  wrong=[None,
         "permit(허용하다)이 틀려요. 제조사는 공식 수리소로 가져오라고 요구(require)하는 거지, 허락해 주는 게 아니에요.",
         "preserve(보존하다)가 틀려요. 사람들은 고장 난 장치를 보관하지 않고 버려요(dispose of).",
         "둘 다 틀려요. 장치를 보존한다는 말도, 제조사가 허용한다는 말도 본문에 없어요.",
         "둘 다 틀려요. 장치를 기부한다는 말도, 공식 수리소로 가져오는 것을 금지한다는 말도 본문에 없어요."],
  evid=[dict(n=1, hl=["dispose of their damaged devices","too difficult to repair"]), dict(n=2, hl=["difficult to disassemble","require that it be brought to an official service center"])],
  swaps=[["dispose","discard","버리다 → 버리다"],["require","oblige","요구하다 → 강제하다"],["disassemble","take apart","분해하다 → 분해하다"]],
  swapnote="dispose of(버리다)는 discard(버리다)로, require(요구하다)는 oblige(강제하다)로 바뀌어 나와요. 본문 단어만 찾지 말고 뜻이 같은 말을 찾으세요.",
  use=[dict(w="discard",ex="Please do not discard old batteries in the trash.",ko="낡은 배터리를 쓰레기통에 버리지 마세요."),
       dict(w="oblige",ex="The law will oblige drivers to wear seat belts.",ko="그 법은 운전자가 안전벨트를 착용하도록 강제할 것이다.")],
  flow="본문 1번에서 사람들이 고장 난 장치를 버리는 이유가 나오고, 2번에서 For example! 분해하기 어렵고 공식 수리소로만 가져와야 한다고 구체적인 예를 들어요.",
 ),
 dict(
  id=2,
  summary="Many companies do not permit customers to take broken items to independent repair shops, and some products are deliberately designed to be hard to fix, so consumers often cannot obtain the instructions or parts.",
  ko="많은 회사는 고객이 고장 난 물건을 독립적인 수리점에 가져가는 것을 <b>(A) 허용하지</b> 않고, 어떤 제품은 고치기 어렵도록 <b>(B) 고의로</b> 만들어져서 소비자가 설명서나 부품을 구하지 못하는 일이 많다.",
  opts=[["permit","deliberately"],["permit","accidentally"],["forbid","deliberately"],["forbid","accidentally"],["require","occasionally"]],
  optko=["허용하다 – 고의로","허용하다 – 우연히","금지하다 – 고의로","금지하다 – 우연히","요구하다 – 가끔"],
  ans=0,
  wrong=[None,
         "accidentally(우연히)가 틀려요. 본문은 일부러(intentionally) 고치기 어렵게 만든다고 해요.",
         "forbid(금지하다)가 틀려요. 'do not forbid'는 '금지하지 않는다'가 되어 본문과 반대가 돼요.",
         "둘 다 틀려요. 회사는 허용하지 않고(not allow), 제품은 일부러 그렇게 만들어졌다고 해요.",
         "둘 다 틀려요. 회사가 외부 수리점 이용을 허용하지 않는다고 했고, '가끔'이라는 말은 없어요."],
  evid=[dict(n=3, hl=["do not allow their customers to take their damaged items to third-party repair shops"]), dict(n=4, hl=["intentionally designed to be difficult to repair"]), dict(n=5, hl=["unable to acquire the instructions for how to fix their items or the parts needed to complete repairs"])],
  swaps=[["allow","permit","허용하다 → 허용하다"],["intentionally","deliberately","의도적으로 → 고의로"],["third-party","independent","제삼자의 → 독립적인"],["acquire","obtain","얻다 → 얻다"]],
  swapnote="allow(허용하다)는 permit(허용하다)으로, intentionally(의도적으로)는 deliberately(고의로)로 바뀌어 나와요. 부정문(not)이 붙어 있는지도 꼭 확인하세요.",
  use=[dict(w="permit",ex="The school does not permit students to use phones in class.",ko="학교는 학생이 수업 중에 휴대폰을 사용하도록 허용하지 않는다."),
       dict(w="deliberately",ex="He deliberately left the door open.",ko="그는 일부러 문을 열어 두었다.")],
  flow="본문 3번에서 외부 수리점 이용을 막고, 4번에서 What is more! 아예 일부러 고치기 어렵게 만들고, 5번에서 설명서와 부품까지 구하기 어렵다고 문제를 하나씩 쌓아 가요.",
 ),
 dict(
  id=3,
  summary="To protect consumers' rights, the right-to-repair movement tries to resolve these problems by advocating laws that let owners fix their products themselves or bring them to a technician of their choice.",
  ko="소비자의 권리를 보호하기 위해, 수리할 권리 운동은 소유자가 자기 제품을 직접 고치거나 자신이 고른 기술자에게 가져가도록 해 주는 법률을 <b>(B) 옹호함으로써</b> 이러한 문제를 <b>(A) 해결하려 한다</b>.",
  opts=[["resolve","advocating"],["resolve","opposing"],["ignore","advocating"],["worsen","opposing"],["avoid","delaying"]],
  optko=["해결하다 – 옹호하다","해결하다 – 반대하다","무시하다 – 옹호하다","악화시키다 – 반대하다","피하다 – 미루다"],
  ans=0,
  wrong=[None,
         "opposing(반대하다)이 틀려요. 이 운동은 수리할 권리를 보장하는 법을 반대하지 않고 추진해요.",
         "ignore(무시하다)가 틀려요. 이 운동은 문제를 무시하는 게 아니라 해결하려고 해요.",
         "둘 다 틀려요. 문제를 악화시킨다는 말도, 법에 반대한다는 말도 본문에 없어요.",
         "둘 다 틀려요. 문제를 피하거나 법을 미룬다는 말은 본문에 없어요."],
  evid=[dict(n=6, hl=["solve these problems by promoting legislation","fix it yourself or bring it to a technician of your choice"]), dict(n=7, hl=["To protect the rights of consumers"])],
  swaps=[["solve","resolve","해결하다 → 해결하다"],["promote","advocate","추진하다 → 옹호하다"],["legislation","laws","법률 제정 → 법률"]],
  swapnote="solve(해결하다)는 resolve(해결하다)로, promote(추진하다)는 advocate(옹호하다)로 바뀌어 나와요. 운동의 목표가 무엇인지 방향부터 잡으세요.",
  use=[dict(w="resolve",ex="We need to resolve this problem before Friday.",ko="우리는 금요일 전에 이 문제를 해결해야 한다."),
       dict(w="advocate",ex="Many doctors advocate regular exercise.",ko="많은 의사가 규칙적인 운동을 옹호한다.")],
  flow="본문 6번이 핵심이에요. 수리할 권리 운동은 법률을 추진해서 '내 제품은 내가 직접, 또는 내가 고른 기술자에게 고치게 한다'는 권리를 지키려 하고, 7번은 소비자의 권리를 지키기 위한 네 가지 요구가 이어진다고 알려 줘요.",
 ),
]

# 단어 사전: 표면형(소문자) -> [기본형, 이 글에서의 뜻]
G = {
 "one":["one","하나의"],"reason":["reason","이유"],"many":["many","많은"],"people":["people","사람들"],
 "dispose":["dispose","버리다 (dispose of = ~을 버리다)"],"their":["their","그들의"],"damaged":["damage","손상시키다 (damaged = 고장 난, 손상된)"],
 "devices":["device","장치, 기기"],"device":["device","장치, 기기"],"are":["be","~이다"],"too":["too","너무"],
 "difficult":["difficult","어려운"],"repair":["repair","수리하다, 수리"],"for":["for","~을 위해"],"example":["example","예, 보기"],
 "may":["may","~할 수도 있다"],"disassemble":["disassemble","분해하다"],"manufacturer":["manufacturer","제조사"],
 "require":["require","요구하다"],"brought":["bring","가져오다"],"official":["official","공식적인"],"service":["service","서비스, 수리"],
 "center":["center","센터, 소"],"fixed":["fix","고치다"],"fix":["fix","고치다"],
 "companies":["company","회사"],"allow":["allow","허용하다"],"customers":["customer","고객"],"take":["take","가져가다"],
 "items":["item","물건, 품목"],"third-party":["third-party","제삼자의 (회사와 상관없는)"],"shops":["shop","가게"],
 "what":["what","무엇"],"more":["more","더"],"some":["some","어떤, 몇몇"],"products":["product","제품"],
 "intentionally":["intentionally","의도적으로, 일부러"],"designed":["design","설계하다, 만들다"],
 "common":["common","흔한"],"consumers":["consumer","소비자"],"unable":["unable","~할 수 없는"],"acquire":["acquire","얻다, 구하다"],
 "instructions":["instruction","설명(서), 사용법"],"how":["how","어떻게"],"parts":["part","부품"],"needed":["need","필요하다"],
 "complete":["complete","완료하다"],"repairs":["repair","수리"],
 "right-to-repair":["right-to-repair","수리할 권리의"],"movement":["movement","운동"],"trying":["try","시도하다, 애쓰다"],
 "tries":["try","시도하다, 애쓰다"],"solve":["solve","해결하다"],"these":["these","이러한"],"problems":["problem","문제"],
 "promoting":["promote","추진하다, 촉진하다"],"legislation":["legislation","법률 제정, 법률"],"states":["state","명시하다"],
 "following":["following","다음의"],"own":["own","소유하다 (형용사로는 '자신의')"],"product":["product","제품"],
 "right":["right","권리"],"yourself":["yourself","직접, 스스로"],"technician":["technician","기술자"],"choice":["choice","선택"],
 "protect":["protect","보호하다"],"rights":["right","권리"],"demands":["demand","요구하다"],"four":["four","네 개의"],"things":["thing","것"],
 "discard":["discard","버리다"],"preserve":["preserve","보존하다"],"donate":["donate","기부하다"],
 "oblige":["oblige","강제하다, 의무를 지우다"],"permit":["permit","허용하다"],"forbid":["forbid","금지하다"],
 "makers":["maker","제조사"],"bring":["bring","가져오다"],"apart":["apart","따로따로 (take apart = 분해하다)"],
 "hard":["hard","어려운"],"because":["because","~ 때문에"],"as":["as","~이므로"],"them":["them","그것들을"],"to":["to","~로"],"an":["an","하나의"],
 "broken":["break","깨뜨리다 (broken = 고장 난)"],"independent":["independent","독립적인"],"deliberately":["deliberately","고의로, 일부러"],
 "accidentally":["accidentally","우연히"],"occasionally":["occasionally","가끔"],"often":["often","자주"],"cannot":["can","~할 수 없다"],
 "obtain":["obtain","얻다"],"consumers'":["consumer","소비자"],"resolve":["resolve","해결하다"],"advocating":["advocate","옹호하다"],
 "advocate":["advocate","옹호하다"],"opposing":["oppose","반대하다"],"ignore":["ignore","무시하다"],"worsen":["worsen","악화시키다"],
 "avoid":["avoid","피하다"],"delaying":["delay","미루다"],"laws":["law","법"],"owners":["owner","소유자"],"let":["let","~하게 해 주다"],
 "themselves":["themselves","직접, 스스로"],"choose":["choose","고르다"],"law":["law","법"],"drivers":["driver","운전자"],
 "batteries":["battery","배터리"],"seat":["seat","좌석"],"belts":["belt","띠, 벨트"],"school":["school","학교"],"students":["student","학생"],
 "phones":["phone","휴대폰"],"class":["class","수업"],"left":["leave","두다, 떠나다"],"door":["door","문"],"open":["open","열린"],
 "doctors":["doctor","의사"],"regular":["regular","규칙적인"],"exercise":["exercise","운동"],"friday":["Friday","금요일"],
 "need":["need","필요하다"],"before":["before","~ 전에"],"problem":["problem","문제"],"trash":["trash","쓰레기"],"old":["old","낡은"],
 "do":["do","하다"],"not":["not","~않다"],"is":["be","~이다"],"can":["can","~할 수 있다"],"or":["or","또는"],"and":["and","그리고"],
 "if":["if","만약"],"you":["you","당신"],"it":["it","그것"],"they":["they","그들"],"its":["its","그것의"],"be":["be","~이다"],
 "have":["have","가지다"],"has":["have","가지다"],"that":["that","~라는 것"],"of":["of","~의"],"in":["in","~에서"],"by":["by","~함으로써"],
 "so":["so","그래서"],"will":["will","~할 것이다"],"does":["do","하다"],"use":["use","사용하다"],"wear":["wear","착용하다"],
 "owner":["owner","소유자"],"technicians":["technician","기술자"],"your":["your","당신의"],"choice,":["choice","선택"],
 "dispose of":["dispose of","~을 버리다"],"damaged,":["damage","고장 난"],
}

# 직독직해 조각: [영어 조각, 한글 조각]. [[ ]] 는 빈칸에 들어간 정답 단어 표시
JD={
 1:[["Many people [[discard]] damaged devices","많은 사람이 고장 난 장치를 [[버린다]]"],
    ["because they are hard to repair,","그것들이 수리하기 어렵기 때문에,"],
    ["as some are difficult to take apart","어떤 것은 분해하기 어렵고"],
    ["and some makers [[oblige]] customers to bring them to an official service center.","어떤 제조사는 고객이 그것들을 공식 수리소로 가져오도록 [[강제한다]]."]],
 2:[["Many companies do not [[permit]] customers","많은 회사는 고객이 ~하는 것을 [[허용하지]] 않는다"],
    ["to take broken items to independent repair shops,","고장 난 물건을 독립적인 수리점에 가져가는 것을,"],
    ["and some products are [[deliberately]] designed to be hard to fix,","그리고 어떤 제품은 고치기 어렵도록 [[고의로]] 만들어진다,"],
    ["so consumers often cannot obtain the instructions or parts.","그래서 소비자는 설명서나 부품을 구하지 못하는 일이 많다."]],
 3:[["To protect consumers' rights,","소비자의 권리를 보호하기 위해,"],
    ["the right-to-repair movement tries to [[resolve]] these problems","수리할 권리 운동은 이러한 문제를 [[해결하려 한다]]"],
    ["by [[advocating]] laws","법률을 [[옹호함으로써]]"],
    ["that let owners fix their products themselves","소유자가 자기 제품을 직접 고치도록 해 주는"],
    ["or bring them to a technician of their choice.","또는 자신이 고른 기술자에게 가져가도록 해 주는."]],
}

# 기억할 흐름 카드뉴스: [본문 번호 태그, 한 줄 큰 문장, 작은 보충, (마지막이면 강조)]
FC={
 1:[["본문 1번","고장 난 장치를 버리는 이유","고치기가 너무 어렵기 때문이에요."],
    ["본문 2번","For example! 분해도 어렵고 공식 수리소로만","제조사가 공식 수리소로 가져오라고 요구해요."],
    ["정답 포인트","{{dispose of|버리다}} = {{discard|버리다}}, {{require|요구하다}} = {{oblige|강제하다}}","본문 표현이 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 3번","외부 수리점에는 못 맡기게 한다","{{third-party|제삼자의}} 가게는 회사와 상관없는 가게예요."],
    ["본문 4번","What is more! 일부러 고치기 어렵게 만든다","문제를 하나 더 쌓는 연결어예요."],
    ["본문 5번","설명서와 부품도 구하기 힘들다","그래서 소비자가 직접 고치기 어려워요."],
    ["정답 포인트","{{allow|허용하다}} = {{permit|허용하다}}, {{intentionally|일부러}} = {{deliberately|고의로}}","not이 붙은 문장이니 부정까지 확인해요."]],
 3:[["본문 7번","소비자의 권리를 지키려는 운동","수리할 권리 운동이 네 가지를 요구해요."],
    ["본문 6번","법을 추진해서 문제를 해결한다","내 제품은 내가 직접, 또는 내가 고른 기술자에게 고치게 해요."],
    ["정답 포인트","{{solve|해결하다}} = {{resolve|해결하다}}, {{promote|추진하다}} = {{advocate|옹호하다}}","운동의 방향이 무엇인지부터 잡아요."]],
}

# 바꿔 말하기 스토리
STORY=[
 dict(a="dispose",form="dispose",n=1,sq=1,sum="Many people [[discard]] damaged devices",hook="고장 난 장치를 쓰레기로 내놓는다는 문장의 dispose of(버리다) → 요약문에서는 discard(버리다)로 바꿨어요."),
 dict(a="require",form="require",n=2,sq=1,sum="some makers [[oblige]] customers to bring them to an official service center",hook="제조사가 공식 수리소로 가져오라고 하는 문장의 require(요구하다) → 요약문에서는 oblige(강제하다)로 바꿨어요."),
 dict(a="allow",form="allow",n=3,sq=2,sum="Many companies do not [[permit]] customers",hook="외부 수리점에 못 맡기게 하는 문장의 allow(허용하다) → 요약문에서는 permit(허용하다)으로 바꿨어요."),
 dict(a="intentionally",form="intentionally",n=4,sq=2,sum="some products are [[deliberately]] designed to be hard to fix",hook="일부러 고치기 어렵게 만든다는 문장의 intentionally(의도적으로) → 요약문에서는 deliberately(고의로)로 바꿨어요."),
 dict(a="solve",form="solve",n=6,sq=3,sum="the right-to-repair movement tries to [[resolve]] these problems",hook="수리할 권리 운동이 문제를 풀려는 문장의 solve(해결하다) → 요약문에서는 resolve(해결하다)로 바꿨어요."),
 dict(a="promote",form="promoting",n=6,sq=3,sum="by [[advocating]] laws",hook="법률 제정을 밀어붙인다는 문장의 promoting(추진하다) → 요약문에서는 advocating(옹호하다)으로 바꿨어요."),
]

SCENES=[
 dict(tag="본문 1번",ns=[1],line="고장 난 장치를 [[dispose|버리는]] 이유는 고치기 너무 어렵기 때문이다."),
 dict(tag="본문 2번",ns=[2],line="분해하기도 힘들고, 제조사가 공식 수리소로 가져오라고 [[require|요구하기]]도 한다."),
 dict(tag="본문 3번",ns=[3],line="많은 회사가 외부 수리점에 맡기는 것을 [[allow|허용하지]] 않는다."),
 dict(tag="본문 4번",ns=[4],line="게다가 [[intentionally|의도적으로]] 고치기 어렵게 만든 제품도 있다."),
 dict(tag="본문 5번",ns=[5],line="설명서와 부품도 구하기 어렵다."),
 dict(tag="본문 6번",ns=[6],line="수리할 권리 운동은 이 문제를 [[solve|해결하려고]] 법률 제정을 [[promoting|추진한다]]."),
]

HLKO={1:["그들의 고장 난 장치들을 버리는","수리하기 너무 어렵기"],2:["분해하기 어려울","공식 수리소로 가져올 것을 요구할"],
 3:["그들의 고객들이 고장 난 물건들을 제삼자의 수리점으로 가지고 가는 것을 허용하지 않는다"],4:["의도적으로 수리하기 어렵게 만들어진다"],
 5:["그들의 물건을 고치는 방법에 대한 설명이나 수리를 완료하기 위해 필요한 부품들을 얻지 못하는"],
 6:["법률 제정을 추진함으로써 이러한 문제들을 해결하려고","그것을 직접 고치거나 당신이 선택한 기술자에게 가지고 갈"],7:["소비자의 권리를 보호하기 위해"]}

UM={'discard':('버리다','버리지'),'oblige':('강제하다','강제할'),'permit':('허용하다','허용하지'),'deliberately':('고의로','일부러'),'resolve':('해결하다','해결해야'),'advocate':('옹호하다','옹호한다')}

G.update({'dispose of':['dispose of','~을 버리다']})

TARGET={1:3,2:0,3:2}
