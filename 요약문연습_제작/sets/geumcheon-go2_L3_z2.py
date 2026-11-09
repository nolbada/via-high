# -*- coding: utf-8 -*-
# 세트 정의: 금천고2 3과 ❷
META=dict(sch='geumcheon-go2', src='geumcheon-go2/L3/sx-data.js', pidx=1, lesson='3과', title='투표하는 방법에는 여러 가지가 있다', label='❷', page='yoyak-lian-z2')
Q = [
 dict(
  id=1,
  summary="The student council had to (A) how to raise money for children in need, but members held (B) opinions about the three options.",
  ko="학생 자치회는 어려움에 처한 아이들을 위해 모금할 방법을 <b>(A) 결정해야</b> 했지만, 세 가지 선택지에 대해 <b>(B) 대립하는</b> 의견을 가졌다.",
  opts=[["determine","opposing"],["determine","identical"],["predict","opposing"],["predict","identical"],["abandon","unanimous"]],
  optko=["결정하다 – 대립하는","결정하다 – 똑같은","예측하다 – 대립하는","예측하다 – 똑같은","포기하다 – 만장일치의"],
  ans=0,
  wrong=[None,
         "identical(똑같은)이 틀려요. 본문은 의견이 서로 부딪쳤다(conflicting)고 해요.",
         "predict(예측하다)가 틀려요. 자치회는 미래를 맞히는 게 아니라 모금 방법을 정해야(decide) 했어요.",
         "둘 다 틀려요. 예측해야 했던 것도, 의견이 똑같았던 것도 아니에요.",
         "둘 다 틀려요. 모금을 포기한 게 아니고, 만장일치(모두 같은 의견)도 아니에요."],
  evid=[dict(n=1, hl=["needed to decide how to raise money"]), dict(n=2, hl=["conflicting opinions"])],
  swaps=[["decide","determine","결정하다 → 확정하다, 결정하다"],["conflicting","opposing","상충하는 → 대립하는"],["needed to","had to","~해야 했다"]],
  swapnote="decide(결정하다)는 determine(결정하다, 알아내다)으로, conflicting(상충하는)은 opposing(대립하는)이나 contradictory(모순되는)로 바뀌어 나와요.",
  use=[dict(w="determine",ex="We must determine the best way to solve this problem.",ko="우리는 이 문제를 해결할 가장 좋은 방법을 결정해야 한다."),
       dict(w="opposing",ex="The two teams had opposing views on the rule.",ko="두 팀은 그 규칙에 대해 대립하는 견해를 가졌다.")],
  flow="본문 1번에서 자치회는 아이들을 위한 모금 방법을 정해야 하고, 2번에서 선택지 세 가지(미술 전시회, 빵 바자회, 자선 콘서트)를 두고 의견이 서로 부딪쳐요.",
 ),
 dict(
  id=2,
  summary="When asked for advice, their advisor (A) the council to try a different voting method instead of the (B) one.",
  ko="조언을 구하자 고문 교사는 자치회가 <b>(B) 기존의</b> 방법 대신 다른 투표 방법을 시도하도록 <b>(A) 촉구했다</b>.",
  opts=[["urged","conventional"],["urged","innovative"],["forbade","conventional"],["forbade","innovative"],["warned","unfamiliar"]],
  optko=["촉구하다 – 기존의","촉구하다 – 획기적인","금지하다 – 기존의","금지하다 – 획기적인","경고하다 – 낯선"],
  ans=0,
  wrong=[None,
         "innovative(획기적인)가 틀려요. 선생님이 쓰지 말라고 한 건 익숙한(familiar) 기존 방법이에요.",
         "forbade(금지하다)가 틀려요. 선생님은 막은 게 아니라 다른 방법을 시도해 보라고 권했어요.",
         "둘 다 틀려요. 금지한 것도 아니고, 쓰지 말라고 한 방법도 획기적인 방법이 아니에요.",
         "둘 다 틀려요. 경고한 게 아니라 권했고, 쓰지 말라고 한 건 낯선 방법이 아니라 익숙한 방법이에요."],
  evid=[dict(n=4, hl=["not to use the familiar voting method","try something different"])],
  swaps=[["encouraged","urged","권장했다 → 촉구했다"],["familiar","conventional","익숙한 → 기존의, 관습적인"],["something different","a different voting method","다른 것 → 다른 투표 방법"]],
  swapnote="encourage(권장하다)는 urge(촉구하다)나 advise(조언하다)로, familiar(익숙한)는 conventional(관습적인)이나 customary(관례적인)로 바뀌어 나와요.",
  use=[dict(w="urge",ex="The teacher urged us to read the text carefully.",ko="선생님은 우리에게 본문을 꼼꼼히 읽으라고 촉구했다."),
       dict(w="conventional",ex="She chose a conventional method instead of a risky one.",ko="그녀는 위험한 방법 대신 기존의 방법을 골랐다.")],
  flow="본문 3번에서 투표로 정하기로 했는데, 4번에서 Akers 선생님이 반전을 줘요. 늘 쓰던 투표 말고 다른 것을 해 보라고 권해요.",
 ),
 dict(
  id=3,
  summary="After some (A), the council members decided to try three voting systems to find out whether the methods would (B) different results.",
  ko="약간의 <b>(A) 조사</b> 후에, 자치회 구성원들은 그 방법들이 서로 다른 결과를 <b>(B) 낼지</b> 알아보려고 세 가지 투표 시스템을 시도해 보기로 결정했다.",
  opts=[["investigation","produce"],["investigation","prevent"],["election","produce"],["election","prevent"],["debate","conceal"]],
  optko=["조사 – 만들어 내다","조사 – 막다","선거 – 만들어 내다","선거 – 막다","토론 – 감추다"],
  ans=0,
  wrong=[None,
         "prevent(막다)가 틀려요. 방법마다 결과가 달라질지 궁금해한 거지, 결과를 막으려는 게 아니에요.",
         "election(선거)이 틀려요. 투표 전에 한 건 선거가 아니라 조사(research)예요.",
         "둘 다 틀려요. 투표 전에 한 건 조사이고, 결과를 막는다는 말도 없어요.",
         "둘 다 틀려요. 토론을 했다는 말도, 결과를 감춘다는 말도 본문에 없어요."],
  evid=[dict(n=5, hl=["After doing some research","try three different voting systems"]), dict(n=6, hl=["different methods would yield different results"])],
  swaps=[["research","investigation","조사 → 조사, 탐구"],["yield","produce","내다 → 만들어 내다"],["curious","wondering","궁금한 → 궁금해하는"]],
  swapnote="research(조사)는 investigation(조사, 수사)이나 study(연구)로, yield(결과를 내다)는 produce(만들어 내다)나 generate(생성하다)로 바뀌어 나와요.",
  use=[dict(w="investigation",ex="After a long investigation, the police found the answer.",ko="오랜 조사 끝에 경찰은 답을 찾았다."),
       dict(w="produce",ex="Different methods can produce different results.",ko="다른 방법은 다른 결과를 만들어 낼 수 있다.")],
  flow="본문 5번에서 자치회는 조사를 한 뒤 세 가지 투표 방식(FPTP, AV, 콩도르세)을 써 보기로 하고, 6번에서 방식마다 결과가 다를지 궁금해해요.",
 ),
]

G = {
 "the":["the","그"],"student":["student","학생"],"council":["council","자치회, 위원회"],"had":["have","~해야 했다 (had to)"],
 "to":["to","~하기 위해, ~하는"],"how":["how","어떻게, ~하는 방법"],"raise":["raise","(돈을) 모으다"],"money":["money","돈"],
 "for":["for","~을 위해"],"children":["child","아이들"],"in":["in","~에 있는"],"need":["need","어려움, 필요"],
 "but":["but","하지만"],"members":["member","구성원"],"held":["hold","가지다, 품다"],"opinions":["opinion","의견"],
 "about":["about","~에 대해"],"three":["three","세 가지"],"options":["option","선택지"],"determine":["determine","결정하다"],
 "opposing":["opposing","대립하는"],"identical":["identical","똑같은"],"predict":["predict","예측하다"],
 "abandon":["abandon","포기하다"],"unanimous":["unanimous","만장일치의"],"needed":["need","~해야 하다"],"decide":["decide","결정하다"],
 "conflicting":["conflicting","상충하는, 부딪치는"],"their":["their","그들의"],"were":["be","~였다"],"there":["there","거기에"],
 "members":["member","구성원"],"greenville":["Greenville","(학교 이름)"],"high":["high","고등의"],"school":["school","학교"],
 "of":["of","~의"],"art":["art","미술"],"show":["show","전시회"],"bake":["bake","(빵을) 굽다"],"sale":["sale","판매, 바자회"],
 "charity":["charity","자선"],"concert":["concert","콘서트"],"options":["option","선택지"],"and":["and","그리고"],
 "a":["a","하나의"],"or":["or","또는"],"so":["so","그래서"],"they":["they","그들"],"decided":["decide","결정하다"],"put":["put","두다, 부치다"],
 "it":["it","그것"],"vote":["vote","투표"],"voting":["vote","투표하다 (voting = 투표의)"],"method":["method","방법"],"methods":["method","방법"],
 "systems":["system","시스템, 제도"],"system":["system","시스템, 제도"],"when":["when","~할 때"],"asked":["ask","묻다, 구하다"],
 "advice":["advice","조언"],"advisor":["advisor","고문, 조언자"],"ms.":["Ms.","~ 선생님"],"akers":["Akers","(사람 이름)"],"she":["she","그녀"],
 "encouraged":["encourage","권장하다, 격려하다"],"them":["they","그들을"],"not":["not","~하지 않다"],"use":["use","사용하다"],
 "familiar":["familiar","익숙한"],"but":["but","하지만"],"try":["try","시도하다"],"something":["something","어떤 것"],"different":["different","다른"],
 "instead":["instead","대신에"],"urged":["urge","촉구하다"],"urge":["urge","촉구하다"],"forbade":["forbid","금지하다"],"warned":["warn","경고하다"],
 "conventional":["conventional","기존의, 관습적인"],"innovative":["innovative","획기적인"],"unfamiliar":["unfamiliar","낯선"],
 "one":["one","(앞에 나온 명사를 대신하는) 것"],"after":["after","~ 후에"],"doing":["do","하다"],"some":["some","약간의"],
 "research":["research","조사, 연구"],"investigation":["investigation","조사"],"election":["election","선거"],"debate":["debate","토론"],
 "produce":["produce","만들어 내다"],"prevent":["prevent","막다"],"conceal":["conceal","감추다"],"entire":["entire","전체의"],
 "was":["be","~였다"],"curious":["curious","궁금한"],"find":["find","찾다"],"out":["out","밖으로 (find out = 알아내다)"],
 "if":["if","~인지"],"whether":["whether","~인지 아닌지"],"would":["would","~할 것이다"],"yield":["yield","(결과를) 내다"],
 "results":["result","결과"],"first-past-the-post":["first-past-the-post","단순 다수결 방식"],"fptp":["FPTP","단순 다수결"],
 "alternative":["alternative","대안의"],"av":["AV","대안 투표"],"condorcet":["Condorcet","콩도르세 (사람 이름)"],"council's":["council","자치회의"],
 "wondering":["wonder","궁금해하다"],"identical":["identical","똑같은"],"raise":["raise","(돈을) 모으다"],"in need":["in need","어려움에 처한"],
 "advisor,":["advisor","고문"],"options,":["option","선택지"],"the council":["council","자치회"],
}

JD={
 1:[["The student council had to [[determine]]","학생 자치회는 [[결정해야]] 했다"],
    ["how to raise money for children in need,","어려움에 처한 아이들을 위해 모금할 방법을,"],
    ["but members held [[opposing]] opinions","하지만 구성원들은 [[대립하는]] 의견을 가졌다"],
    ["about the three options.","세 가지 선택지에 대해."]],
 2:[["When asked for advice,","조언을 구하자,"],
    ["their advisor [[urged]] the council","그들의 고문 교사는 자치회에 [[촉구했다]]"],
    ["to try a different voting method","다른 투표 방법을 시도해 보라고"],
    ["instead of the [[conventional]] one.","[[기존의]] 방법 대신에."]],
 3:[["After some [[investigation]],","약간의 [[조사]] 후에,"],
    ["the council members decided to try three voting systems","자치회 구성원들은 세 가지 투표 시스템을 시도해 보기로 결정했다"],
    ["to find out whether the methods would [[produce]] different results.","그 방법들이 서로 다른 결과를 [[낼지]] 알아보려고."]],
}

FC={
 1:[["본문 1번","자치회가 모금 방법을 정해야 한다","어려운 아이들을 돕기 위한 돈이 필요해요."],
    ["본문 2번","그런데 의견이 서로 부딪친다","미술 전시회, 빵 바자회, 자선 콘서트 중 무엇을 할지 의견이 갈려요."],
    ["정답 포인트","{{decide|결정하다}} = {{determine|결정하다}}, {{conflicting|상충하는}} = {{opposing|대립하는}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 3번","그래서 투표로 정하기로 한다","여기까지는 평범한 이야기예요."],
    ["본문 4번","But! 선생님은 다른 방법을 권한다","늘 쓰던 방법 말고 다른 것을 해 보라고 해요."],
    ["정답 포인트","{{encouraged|권장했다}} = {{urged|촉구했다}}, {{familiar|익숙한}} = {{conventional|기존의}}","not to use ~ 는 '쓰지 말라'는 뜻이라 기존 방법이 답이에요."]],
 3:[["본문 5번","조사를 한 뒤 세 방식을 고른다","{{research|조사}} → {{investigation|조사}}"],
    ["본문 6번","방법마다 결과가 다를지 궁금하다","{{curious|궁금한}} 마음이 실험의 이유예요."],
    ["정답 포인트","{{yield|내다}} = {{produce|만들어 내다}}","'결과를 낸다'는 말을 다른 단어로 바꿨어요."]],
}

STORY=[
 dict(a="decide",form="decide",n=1,sq=1,sum="The student council had to [[determine]] how to raise money",hook="모금 방법을 정해야 한다는 첫 문장의 decide(결정하다) → 요약문에서는 determine(결정하다)으로 바꿨어요."),
 dict(a="conflicting",form="conflicting",n=2,sq=1,sum="members held [[opposing]] opinions",hook="세 가지 선택지를 두고 의견이 부딪친다는 문장의 conflicting(상충하는) → 요약문에서는 opposing(대립하는)으로 바꿨어요."),
 dict(a="familiar",form="familiar",n=4,sq=2,sum="instead of the [[conventional]] one",hook="늘 쓰던 투표 방법이라는 말의 familiar(익숙한) → 요약문에서는 conventional(기존의)로 바꿨어요."),
 dict(a="encouraged",form="encouraged",n=4,sq=2,sum="their advisor [[urged]] the council",hook="선생님이 다른 방법을 해 보라고 권했다는 말의 encouraged(권장했다) → 요약문에서는 urged(촉구했다)로 바꿨어요."),
 dict(a="research",form="research",n=5,sq=3,sum="After some [[investigation]],",hook="세 가지 방식을 정하기 전에 한 조사 → research(조사)를 요약문에서는 investigation(조사)으로 바꿨어요."),
 dict(a="yield",form="yield",n=6,sq=3,sum="whether the methods would [[produce]] different results",hook="방법마다 결과를 낼지 궁금하다는 문장의 yield(내다) → 요약문에서는 produce(만들어 내다)로 바꿨어요."),
]

SCENES=[
 dict(tag="본문 1번",ns=[1],line="아이들을 도울 모금 방법을 자치회가 [[decide|정해야]] 한다."),
 dict(tag="본문 2번",ns=[2],line="전시회냐 바자회냐 콘서트냐, 의견이 서로 [[conflicting|부딪친다]]."),
 dict(tag="본문 4번",ns=[4],line="선생님이 말한다. [[familiar|익숙한]] 투표 말고 다른 것을 해 보라고 [[encouraged|권했다]]."),
 dict(tag="본문 5번",ns=[5],line="자치회는 [[research|조사]]를 하고 세 가지 투표 방식을 고른다."),
 dict(tag="본문 6번",ns=[6],line="방식마다 결과를 [[yield|낼지]] 모두가 궁금하다."),
]

HLKO={1:["모금할 방법을 결정해야 했다"],2:["상충되는 의견들"],
 4:["익숙한 투표 방법을 사용하지 말고","다른 것을 시도해 보라고 권장했다"],
 5:["약간의 조사를 한 후","세 가지의 다른 투표 시스템을 시도해 보기로"],
 6:["각각 다른 방법이 서로 다른 결과를 낼지"]}

UM={'determine':('결정하다','결정해야'),'opposing':('대립하는','대립하는'),'urge':('촉구하다','촉구했다'),'conventional':('기존의, 관습적인','기존의'),'investigation':('조사','조사'),'produce':('만들어 내다','만들어 낼')}

G.update({'council’s':['council','자치회의']})
TARGET={1:2,2:4,3:0}
