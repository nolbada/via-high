# -*- coding: utf-8 -*-
# 세트 정의: 주성고2 모의고사 22년 11월 35번
META=dict(sch='jusung-go2', src='jusung-go2/mock/sx-data.js', pidx=6, lesson='22년 11월 35번', title='', label='', page='yoyak-2211-35')
Q = [
 dict(
  id=1,
  summary="Envy is the most (A) of all human emotions, so it is very hard to (B) the envy that drives people's actions.",
  ko="질투는 모든 인간 감정 중에서 가장 <b>(A) 알쏭달쏭한</b> 감정이어서, 사람들의 행동을 이끄는 질투를 <b>(B) 알아보기</b>가 매우 어렵다.",
  opts=[["puzzling","recognize"],["obvious","recognize"],["obvious","hide"],["puzzling","ignore"],["familiar","measure"]],
  optko=["알쏭달쏭한 – 알아보다","뻔한 – 알아보다","뻔한 – 숨기다","알쏭달쏭한 – 무시하다","익숙한 – 재다"],
  ans=0,
  wrong=[None,
         "obvious(뻔한)가 틀려요. 본문은 질투가 가장 까다롭고 이해하기 어려운(elusive) 감정이라고 해요.",
         "둘 다 틀려요. obvious(뻔한)가 아니라 이해하기 어려운 감정이고, hide(숨기다)가 아니라 알아채기(discern) 어렵다는 내용이에요.",
         "ignore(무시하다)가 틀려요. 무시하기가 아니라 알아채기(discern) 어렵다는 말이에요.",
         "둘 다 틀려요. familiar(익숙한)가 아니라 까다로운 감정이고, measure(재다)는 본문에 없어요."],
  evid=[dict(n=1, hl=["none is trickier or more elusive than envy"]), dict(n=2, hl=["very difficult to actually discern the envy"])],
  swaps=[["elusive","puzzling","이해하기 어려운 → 알쏭달쏭한"],["discern","recognize","알아차리다 → 알아보다"],["motivate","drive","자극하다 → 이끌다"]],
  swapnote="elusive(이해하기 어려운)는 puzzling(알쏭달쏭한)이나 hard to grasp(파악하기 힘든)로, discern(알아차리다)은 recognize(알아보다)나 notice(알아채다)로 바뀌어 나와요.",
  use=[dict(w="puzzling",ex="The puzzling message made everyone confused.",ko="그 알쏭달쏭한 메시지는 모두를 헷갈리게 했다."),
       dict(w="recognize",ex="I can recognize her voice easily.",ko="나는 그녀의 목소리를 쉽게 알아본다.")],
  flow="본문 1번에서 질투가 가장 까다로운 감정이라고 하고 → 2번에서 그래서 행동 뒤의 질투를 알아채기가 어렵다고 이어져요.",
 ),
 dict(
  id=2,
  summary="People rarely (A) envy directly, because it comes with the (B) that they are weaker than others in something they care about.",
  ko="사람들은 질투를 직접 <b>(A) 보여 주는</b> 일이 드문데, 질투에는 자신이 소중히 여기는 것에서 남보다 약하다는 <b>(B) 인식</b>이 따르기 때문이다.",
  opts=[["show","recognition"],["show","denial"],["share","denial"],["hide","recognition"],["feel","recognition"]],
  optko=["보여 주다 – 인식","보여 주다 – 부인","나누다 – 부인","숨기다 – 인식","느끼다 – 인식"],
  ans=0,
  wrong=[None,
         "denial(부인)이 틀려요. 질투는 열등함을 인정(admission)하는 것이지 부인하는 게 아니에요.",
         "둘 다 틀려요. 질투를 나누는(share) 게 아니라 거의 표현하지 않고, 인정이 아니라 부인(denial)도 아니에요.",
         "hide(숨기다)가 틀려요. '거의 숨기지 않는다'는 말이 되어 본문과 반대예요.",
         "feel(느끼다)이 틀려요. 본문은 질투를 느끼는 게 아니라 직접 표현하는 경우가 거의 없다고 해요."],
  evid=[dict(n=3, hl=["we almost never directly express the envy"]), dict(n=4, hl=["admission to ourselves that we are inferior to another person"])],
  swaps=[["express","show","표현하다 → 보여 주다"],["admission","recognition","인정 → 인식, 인정"],["inferior","weaker","열등한 → 더 약한"],["value","care","가치 있게 여기다 → 소중히 여기다"]],
  swapnote="express(표현하다)는 show(보여 주다)나 reveal(드러내다)로, inferior(열등한)는 weaker(더 약한)나 lower(더 낮은)로 바뀌어 나와요.",
  use=[dict(w="show",ex="She never shows her feelings to others.",ko="그녀는 자신의 감정을 남에게 절대 보여 주지 않는다."),
       dict(w="recognition",ex="He felt the recognition of his own mistake.",ko="그는 자신의 실수를 깨닫는 인식을 느꼈다.")],
  flow="본문 3번에서 질투를 직접 표현하지 않는다고 하고 → 4번에서 그 이유, 곧 질투는 남보다 못하다고 스스로 인정하는 일이기 때문이라고 설명해요.",
 ),
 dict(
  id=3,
  summary="Because admitting weakness is (A) and being noticed by others is even worse, people soon (B) their envy as other feelings such as unfairness or anger.",
  ko="약함을 인정하는 것은 <b>(A) 괴롭고</b> 남에게 들키는 것은 훨씬 더 나쁘기 때문에, 사람들은 곧 자신의 질투를 불공평함이나 분노 같은 다른 감정으로 <b>(B) 가린다</b>.",
  opts=[["distressing","mask"],["distressing","reveal"],["pleasant","reveal"],["natural","mask"],["unnecessary","express"]],
  optko=["괴로운 – 가리다","괴로운 – 드러내다","즐거운 – 드러내다","자연스러운 – 가리다","불필요한 – 표현하다"],
  ans=0,
  wrong=[None,
         "reveal(드러내다)이 틀려요. 들키기 싫어서 질투를 감추려(disguise) 해요.",
         "둘 다 틀려요. 인정하는 일은 즐겁지(pleasant) 않고 고통스러우며, 질투는 드러내지(reveal) 않고 감춰요.",
         "natural(자연스러운)이 틀려요. 열등함을 인정하는 일은 고통스러운(painful) 일이에요.",
         "둘 다 틀려요. 인정은 불필요한(unnecessary) 게 아니라 고통스럽고, 질투는 표현(express)하지 않고 감춰요."],
  evid=[dict(n=5, hl=["painful to admit this inferiority","even worse"]), dict(n=6, hl=["motivated to disguise it to ourselves"])],
  swaps=[["painful","distressing","고통스러운 → 괴로운"],["disguise","mask","감추다 → 가리다"],["see","notice","보다 → 알아차리다"]],
  swapnote="painful(고통스러운)은 distressing(괴로운)이나 hurtful(마음 아픈)로, disguise(감추다)는 mask(가리다)나 conceal(숨기다)로 바뀌어 나와요.",
  use=[dict(w="distressing",ex="It was a distressing moment for the whole family.",ko="그것은 온 가족에게 괴로운 순간이었다."),
       dict(w="mask",ex="He tried to mask his fear with a smile.",ko="그는 두려움을 미소로 가리려고 했다.")],
  flow="본문 5번에서 인정도 아프고 들키는 건 더 나쁘다 → 6번에서 And so(그래서) 질투를 불공평함이나 분노로 감춘다는 결론이 나와요.",
 ),
]

# 단어 사전: 표면형(소문자) -> [기본형, 이 글에서의 뜻]
G = {
 "envy":["envy","질투"],"human":["human","인간의"],"emotions":["emotion","감정"],"emotion":["emotion","감정"],
 "trickier":["tricky","까다로운"],"elusive":["elusive","파악하기 어려운, 모호한"],"elusiveness":["elusiveness","파악하기 어려움, 모호함"],
 "difficult":["difficult","어려운"],"actually":["actually","실제로"],"discern":["discern","알아차리다"],
 "motivates":["motivate","자극하다, 동기를 주다"],"people's":["people","사람들의"],"actions":["action","행동"],
 "reason":["reason","이유"],"simple":["simple","간단한"],"almost":["almost","거의"],"directly":["directly","직접적으로"],
 "express":["express","표현하다"],"feeling":["feel","느끼다"],"entails":["entail","수반하다, 필요로 하다"],
 "admission":["admission","인정, 시인"],"ourselves":["ourselves","우리 자신"],"inferior":["inferior","열등한"],
 "another":["another","다른"],"person":["person","사람"],"something":["something","무언가"],"value":["value","가치 있게 여기다"],
 "puzzling":["puzzling","알쏭달쏭한, 이해하기 어려운"],"recognize":["recognize","알아보다, 인식하다"],
 "obvious":["obvious","뻔한, 명백한"],"hide":["hide","숨기다"],"ignore":["ignore","무시하다"],
 "familiar":["familiar","익숙한"],"measure":["measure","재다, 측정하다"],"drives":["drive","이끌다, 몰아가다"],
 "actions":["action","행동"],"rarely":["rarely","드물게"],"show":["show","보여 주다"],
 "recognition":["recognition","인식, 인정"],"denial":["denial","부인"],"share":["share","나누다"],
 "feel":["feel","느끼다"],"weaker":["weak","더 약한"],"others":["other","다른 사람들"],"care":["care","소중히 여기다, 신경 쓰다"],
 "comes":["come","따라오다 (comes with ~ = ~이 따르다)"],"because":["because","~ 때문에"],
 "admitting":["admit","인정하다"],"weakness":["weakness","약함"],"distressing":["distressing","괴로운"],
 "noticed":["notice","알아차리다"],"worse":["worse","더 나쁜"],"soon":["soon","곧"],"mask":["mask","가리다, 감추다"],
 "reveal":["reveal","드러내다"],"pleasant":["pleasant","즐거운"],"natural":["natural","자연스러운"],
 "unnecessary":["unnecessary","불필요한"],"unfairness":["unfairness","불공평함"],"anger":["anger","분노"],
 "feelings":["feeling","감정, 느낌"],"such":["such as","~ 같은"],"even":["even","훨씬, 심지어"],
 "painful":["painful","고통스러운"],"admit":["admit","인정하다"],"inferiority":["inferiority","열등함"],
 "motivated":["motivate","~하고자 하게 되다"],"disguise":["disguise","감추다, 위장하다"],
 "experience":["experience","경험하다"],"initial":["initial","최초의"],"distribution":["distribution","분배"],
 "goods":["goods","재산, 재화"],"attention":["attention","관심"],"resentment":["resentment","분개"],
 "fairness":["fairness","공정함"],"directly":["directly","직접적으로"],"never":["never","결코 ~ 않다"],
 "message":["message","메시지"],"confused":["confuse","헷갈리게 하다"],"everyone":["everyone","모두"],
 "easily":["easily","쉽게"],"voice":["voice","목소리"],"feelings":["feeling","감정"],"mistake":["mistake","실수"],
 "moment":["moment","순간"],"whole":["whole","전체의"],"family":["family","가족"],"tried":["try","애쓰다"],
 "fear":["fear","두려움"],"smile":["smile","미소"],"unfair":["unfair","불공평한"],"trickier":["tricky","까다로운"],
 "unfairness":["unfairness","불공평함"],"instead":["instead","대신에"],
}

JD={
 1:[["Envy is the most [[puzzling]] of all human emotions,","질투는 모든 인간 감정 중에서 가장 [[알쏭달쏭한]] 것이다,"],
    ["so it is very hard","그래서 매우 어렵다"],
    ["to [[recognize]] the envy","질투를 [[알아보기가]]"],
    ["that drives people's actions.","사람들의 행동을 이끄는."]],
 2:[["People rarely [[show]] envy directly,","사람들은 질투를 직접 [[보여 주는]] 일이 드물다,"],
    ["because it comes with the [[recognition]]","그것에는 [[인식]]이 따르기 때문이다"],
    ["that they are weaker than others","자신이 남보다 약하다는"],
    ["in something they care about.","자신이 소중히 여기는 것에서."]],
 3:[["Because admitting weakness is [[distressing]]","약함을 인정하는 것이 [[괴롭기]] 때문에"],
    ["and being noticed by others is even worse,","그리고 남에게 들키는 것은 훨씬 더 나쁘기 때문에,"],
    ["people soon [[mask]] their envy","사람들은 곧 자신의 질투를 [[가린다]]"],
    ["as other feelings such as unfairness or anger.","불공평함이나 분노 같은 다른 감정으로."]],
}

FC={
 1:[["본문 1번","질투는 가장 까다로운 감정","모든 감정 중 질투보다 이해하기 어려운 건 없어요."],
    ["본문 2번","행동 뒤의 질투는 알아채기 어렵다","{{discern|알아차리다}} = {{recognize|알아보다}}"],
    ["정답 포인트","{{elusive|파악하기 어려운}} = {{puzzling|알쏭달쏭한}}, {{discern|알아차리다}} = {{recognize|알아보다}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 3번","질투는 거의 직접 표현하지 않는다","왜 그럴까? 이유가 바로 뒤에 나와요."],
    ["본문 4번","질투는 남보다 못하다는 인정","내가 소중히 여기는 것에서 남보다 못하다고 스스로 인정하는 거예요."],
    ["정답 포인트","{{express|표현하다}} = {{show|보여 주다}}, {{admission|인정}} = {{recognition|인식}}","{{inferior|열등한}} = {{weaker|더 약한}}"]],
 3:[["본문 5번","인정도 아프고 들키는 건 더 나쁘다","{{painful|고통스러운}} → {{even worse|훨씬 더 나쁜}}"],
    ["본문 6번","그래서 질투를 감춘다","And so(그래서)가 결론 신호예요."],
    ["정답 포인트","{{painful|고통스러운}} = {{distressing|괴로운}}, {{disguise|감추다}} = {{mask|가리다}}","불공평함이나 분노로 포장해요."]],
}

STORY=[
 dict(a="elusive",form="elusive",n=1,sq=1,sum="the most [[puzzling]] of all human emotions",hook="질투는 알쏭달쏭 잡히지 않는 감정, 본문의 elusive(파악하기 어려운) → 요약문에서는 puzzling(알쏭달쏭한)으로 바꿨어요."),
 dict(a="discern",form="discern",n=2,sq=1,sum="to [[recognize]] the envy",hook="행동 뒤에 숨은 질투를 알아채기 힘들다는 문장의 discern(알아차리다) → 요약문에서는 recognize(알아보다)로 바꿨어요."),
 dict(a="express",form="express",n=3,sq=2,sum="rarely [[show]] envy directly",hook="질투를 대놓고 말하지 않는다는 문장의 express(표현하다) → 요약문에서는 show(보여 주다)로 바꿨어요."),
 dict(a="admission",form="admission",n=4,sq=2,sum="comes with the [[recognition]]",hook="나는 남보다 못하다고 스스로 인정하는 순간, 본문의 admission(인정) → 요약문에서는 recognition(인식)으로 바꿨어요."),
 dict(a="inferior",form="inferior",n=4,sq=2,sum="they are [[weaker]] than others",hook="남보다 처진다는 느낌, 본문의 inferior(열등한) → 요약문에서는 weaker(더 약한)로 바꿨어요."),
 dict(a="painful",form="painful",n=5,sq=3,sum="admitting weakness is [[distressing]]",hook="인정하기가 아프다는 문장의 painful(고통스러운) → 요약문에서는 distressing(괴로운)으로 바꿨어요."),
 dict(a="disguise",form="disguise",n=6,sq=3,sum="people soon [[mask]] their envy",hook="질투를 분노로 변장시킨다는 문장의 disguise(감추다) → 요약문에서는 mask(가리다)로 바꿨어요."),
]

SCENES=[
 dict(tag="본문 1~2번",ns=[1,2],line="질투는 가장 [[elusive|알쏭달쏭한]] 감정이라 행동 뒤의 질투를 [[discern|알아채기]] 어렵다."),
 dict(tag="본문 3번",ns=[3],line="이유는 간단하다. 우리는 질투를 거의 직접 [[express|표현하지]] 않는다."),
 dict(tag="본문 4번",ns=[4],line="질투는 남보다 [[inferior|못하다는]] 스스로의 [[admission|인정]]이기 때문이다."),
 dict(tag="본문 5번",ns=[5],line="인정하는 것도 [[painful|고통스럽고]] 들키는 건 더 나쁘다."),
 dict(tag="본문 6번",ns=[6],line="그래서 질투를 불공평함이나 분노로 [[disguise|감춘다]]."),
]

HLKO={1:["질투보다 더 까다롭거나 더 이해하기 어려운 것은 없다"],2:["질투를 실제로 알아차리는 것은 매우 어렵다"],
 3:["질투를 직접적으로 표현하는 경우가 거의 없다"],4:["다른 사람보다 열등하다는 스스로에 대한 인정"],
 5:["고통스러울","훨씬 더 나쁘다"],6:["그것을 우리 자신에게 감추고자 하게 되는데"]}

UM={'puzzling':('알쏭달쏭한, 이해하기 어려운','알쏭달쏭한'),'recognize':('알아보다, 인식하다','알아본다'),'show':('보여 주다','보여 주지'),
 'recognition':('인식, 인정','인식'),'distressing':('괴로운','괴로운'),'mask':('가리다, 감추다','가리려고')}

G.update({'hard':['hard','어려운'],'none':['none','아무것도 ~ 않다'],'people’s':['people','사람들의'],'people':['people','사람들'],'about':['about','~에 대해'],'being':['be','~되다'],'other':['other','다른'],'only':['only','오직 (not only A but B = A뿐 아니라 B도)'],'see':['see','알게 되다, 보다'],'motivate':['motivate','자극하다'],'drive':['drive','이끌다'],'care':['care','소중히 여기다']})

TARGET={1:2,2:4,3:1}
