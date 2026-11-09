# -*- coding: utf-8 -*-
# 세트 정의: 주성고2 모의고사 22년 11월 31번
META=dict(sch='jusung-go2', src='jusung-go2/mock/sx-data.js', pidx=2, lesson='22년 11월 31번', title='', label='', page='yoyak-2211-31')
Q = [
 dict(
  id=1,
  summary="Organisms learn only when events (A) their expectations, which makes surprise a (B) driver of learning.",
  ko="유기체는 사건이 그들의 기대에 <b>(A) 어긋날</b> 때에만 학습하고, 그래서 놀람은 학습의 <b>(B) 기본적인</b> 동력이 된다.",
  opts=[["contradict","basic"],["contradict","minor"],["confirm","minor"],["confirm","basic"],["fulfill","weak"]],
  optko=["어긋나다 – 기본적인","어긋나다 – 사소한","확인해 주다 – 사소한","확인해 주다 – 기본적인","충족시키다 – 약한"],
  ans=0,
  wrong=[None,
         "minor(사소한)가 틀려요. 본문은 놀람이 학습의 근본적인(fundamental) 동력이라고 해요.",
         "둘 다 틀려요. confirm(확인해 주다)은 기대가 맞는다는 말이고, minor(사소한)는 본문과 반대예요.",
         "confirm(확인해 주다)이 틀려요. 기대가 맞아떨어질 때가 아니라 깨질 때(violate) 학습해요.",
         "둘 다 틀려요. fulfill(충족시키다)은 기대가 이루어진다는 뜻이고, weak(약한)는 본문과 반대예요."],
  evid=[dict(n=2, hl=["only learn when events violate their expectations"]), dict(n=3, hl=["surprise is one of the fundamental drivers of learning"])],
  swaps=[["violate","contradict","어기다, 깨다 → 어긋나다, 모순되다"],["fundamental","basic","근본적인 → 기본적인"],["organisms","organisms","유기체 → 유기체 (그대로)"]],
  swapnote="violate(어기다)는 contradict(어긋나다)로, fundamental(근본적인)은 basic(기본적인)이나 essential(필수적인)로 바뀌어 나와요.",
  use=[dict(w="contradict",ex="His actions contradict his words.",ko="그의 행동은 그의 말과 어긋난다."),
       dict(w="basic",ex="Water is a basic need for all living things.",ko="물은 모든 생물에게 기본적인 필요이다.")],
  flow="본문 1번 '오류 신호가 없으면 학습 없다' → 2번 '기대가 깨질 때만 학습' → 3번 In other words(다시 말해) 놀람이 학습의 근본 동력이에요.",
 ),
 dict(
  id=2,
  summary="When the same notes are repeated, the brain's responses gradually (A) because the brain learns to (B) the next note, but a sudden change causes a strong surprise reaction.",
  ko="같은 음이 반복되면 뇌가 다음 음을 <b>(B) 예측하는</b> 것을 배우기 때문에 뇌의 반응은 서서히 <b>(A) 약해지지만</b>, 갑작스러운 변화는 강한 놀람 반응을 일으킨다.",
  opts=[["weaken","predict"],["weaken","ignore"],["strengthen","predict"],["strengthen","forget"],["intensify","ignore"]],
  optko=["약해지다 – 예측하다","약해지다 – 무시하다","강해지다 – 예측하다","강해지다 – 잊다","격렬해지다 – 무시하다"],
  ans=0,
  wrong=[None,
         "ignore(무시하다)가 틀려요. 본문은 뇌가 다음 사건을 예상(anticipate)하는 것을 배운다고 해요.",
         "strengthen(강해지다)이 틀려요. 음이 반복되면 반응은 점점 줄어들어요(decrease).",
         "둘 다 틀려요. 반응은 줄어들고, 뇌는 다음 음을 잊는 게 아니라 예상해요.",
         "둘 다 틀려요. 반응은 격렬해지지 않고 줄어들며, 뇌는 음을 무시하는 게 아니에요."],
  evid=[dict(n=5, hl=["progressively decrease"]), dict(n=6, hl=["learning to anticipate the next event"]), dict(n=8, hl=["strong surprise reaction"])],
  swaps=[["decrease","weaken","줄어들다 → 약해지다"],["anticipate","predict","예상하다 → 예측하다"],["progressively","gradually","점진적으로 → 서서히"],["repeat","repeated","반복되다 → 반복되다 (같은 말)"]],
  swapnote="decrease(줄어들다)는 weaken(약해지다), diminish(줄어들다)로, anticipate(예상하다)는 predict(예측하다), expect(기대하다)로 바뀌어 나와요.",
  use=[dict(w="weaken",ex="The sound began to weaken as we walked away.",ko="우리가 걸어서 멀어지자 소리가 약해지기 시작했다."),
       dict(w="predict",ex="No one can predict the weather exactly.",ko="아무도 날씨를 정확히 예측할 수 없다.")],
  flow="본문 4~5번 같은 음을 계속 들으면 반응이 줄어요 → 6번 이것이 '적응', 뇌가 다음을 예상하는 중 → 7~8번 Suddenly(갑자기) 음이 바뀌면 강한 놀람 반응이 나와요.",
 ),
 dict(
  id=3,
  summary="Adaptation depends not on repetition alone but on whether notes are (A), so the brain becomes (B) to an alternating pattern yet shows surprise at an unexpected repetition.",
  ko="적응은 반복만이 아니라 음이 <b>(A) 예측할 수 있는지</b>에 달려 있어서, 뇌는 교차하는 패턴에 <b>(B) 익숙해지지만</b> 예상치 못한 반복에는 놀람을 보인다.",
  opts=[["random","accustomed"],["foreseeable","accustomed"],["loud","accustomed"],["foreseeable","sensitive"],["random","sensitive"]],
  optko=["무작위의 – 익숙한","예측할 수 있는 – 익숙한","시끄러운 – 익숙한","예측할 수 있는 – 민감한","무작위의 – 민감한"],
  ans=1,
  wrong=["random(무작위의)이 틀려요. 본문은 음이 예측 가능한지(predictable)가 핵심이라고 해요.",
         None,
         "loud(시끄러운)가 틀려요. 음의 크기 이야기는 본문에 없어요.",
         "sensitive(민감한)가 틀려요. ABABA 같은 교차에는 익숙해져서 반응이 다시 줄어요.",
         "둘 다 틀려요. 핵심은 무작위가 아니라 예측 가능성이고, 교차 패턴에는 민감해지지 않고 익숙해져요."],
  evid=[dict(n=9, hl=["whether the notes are predictable"]), dict(n=10, hl=["gets used to this alternation"]), dict(n=11, hl=["an unexpected repetition"])],
  swaps=[["predictable","foreseeable","예측 가능한 → 예측할 수 있는"],["gets used to","becomes accustomed to","~에 익숙해지다 → ~에 익숙해지다"],["alternating","alternating","교차하는 → 교차하는 (그대로)"],["unexpected","unexpected","예상치 못한 → 예상치 못한 (그대로)"]],
  swapnote="predictable(예측 가능한)은 foreseeable(예측할 수 있는)로, get used to(~에 익숙해지다)는 become accustomed to로 바뀌어 나와요.",
  use=[dict(w="foreseeable",ex="A rainy day is foreseeable from dark clouds.",ko="먹구름을 보면 비 오는 날이 예측된다."),
       dict(w="accustomed",ex="She soon became accustomed to the new school.",ko="그녀는 곧 새 학교에 익숙해졌다.")],
  flow="본문 9번 '반복만이 아니라 예측 가능한지가 중요' → 10번 For instance(예를 들어) ABABA는 익숙해져 반응 감소 → 11번 However(그러나) 예상 밖의 ABABB는 놀람을 일으켜요.",
 ),
]

G = {
 "organisms":["organism","유기체, 생물"],"learn":["learn","배우다, 학습하다"],"only":["only","오직, ~할 때만"],
 "events":["event","사건"],"their":["their","그들의"],"expectations":["expectation","기대"],
 "which":["which","그리고 그것은"],"makes":["make","만들다"],"surprise":["surprise","놀람"],
 "driver":["driver","동력, 원동력"],"drivers":["driver","동력, 원동력"],"learning":["learn","배우다, 학습"],
 "contradict":["contradict","어긋나다, 모순되다"],"basic":["basic","기본적인"],"minor":["minor","사소한"],
 "confirm":["confirm","확인해 주다"],"fulfill":["fulfill","충족시키다"],"weak":["weak","약한"],
 "violate":["violate","어기다, 깨다"],"fundamental":["fundamental","근본적인"],"possible":["possible","가능한"],
 "error":["error","오류"],"signal":["signal","신호"],"without":["without","~ 없이"],"words":["word","말, 단어"],
 "imagine":["imagine","상상하다"],"hearing":["hear","듣다"],"series":["series","일련, 연속"],
 "identical":["identical","똑같은"],"notes":["note","음, 음표"],"note":["note","음"],
 "each":["each","각각의"],"draws":["draw","끌어내다"],"response":["response","반응"],"responses":["response","반응"],
 "auditory":["auditory","청각의"],"areas":["area","영역"],"brain":["brain","뇌"],"brain's":["brain","뇌"],"your":["your","당신의"],
 "repeat":["repeat","반복되다"],"repeated":["repeat","반복하다"],"progressively":["progressively","점진적으로"],
 "decrease":["decrease","줄어들다, 감소하다"],"called":["call","부르다"],"adaptation":["adaptation","적응"],
 "deceptively":["deceptively","착각할 만큼"],"simple":["simple","단순한"],"phenomenon":["phenomenon","현상"],
 "shows":["show","보여 주다"],"learning":["learn","배우다, 학습"],"anticipate":["anticipate","예상하다"],
 "next":["next","다음의"],"event":["event","사건"],"suddenly":["suddenly","갑자기"],"changes":["change","바뀌다, 변화"],
 "primary":["primary","일차의, 주된"],"cortex":["cortex","피질"],"immediately":["immediately","즉시"],
 "strong":["strong","강한"],"reaction":["reaction","반응"],"fade":["fade","사라지다"],"away":["away","멀리, 사라져"],
 "additional":["additional","추가적인"],"neurons":["neuron","뉴런, 신경세포"],"begin":["begin","시작하다"],
 "vigorously":["vigorously","힘차게"],"fire":["fire","(뉴런이) 활성화되다, 발화하다"],"unexpected":["unexpected","예상치 못한"],
 "sound":["sound","소리"],"repetition":["repetition","반복"],"leads":["lead","이끌다, 이어지다"],"lead":["lead","이끌다"],
 "matters":["matter","중요하다"],"whether":["whether","~인지 아닌지"],"predictable":["predictable","예측 가능한"],
 "instance":["instance","예, 사례"],"alternating":["alternate","교차하다"],"alternation":["alternation","교차"],
 "gets":["get","되다"],"used":["use","익숙한 (get used to = ~에 익숙해지다)"],"activity":["activity","활동"],
 "again":["again","다시"],"decreases":["decrease","줄어들다"],"time":["time","때, 번"],"however":["however","그러나"],
 "triggers":["trigger","일으키다"],"such":["such","~와 같은"],"set":["set","한 세트, 묶음"],
 "weaken":["weaken","약해지다"],"predict":["predict","예측하다"],"ignore":["ignore","무시하다"],
 "strengthen":["strengthen","강해지다"],"forget":["forget","잊다"],"intensify":["intensify","격렬해지다, 강해지다"],
 "gradually":["gradually","서서히"],"becomes":["become","되다"],"learns":["learn","배우다"],"causes":["cause","일으키다"],
 "sudden":["sudden","갑작스러운"],"change":["change","변화"],"same":["same","같은"],"depends":["depend","달려 있다"],
 "alone":["alone","~만으로"],"pattern":["pattern","패턴"],"yet":["yet","그러나"],"shows":["show","보여 주다"],
 "random":["random","무작위의"],"accustomed":["accustomed","익숙한"],"loud":["loud","시끄러운"],
 "foreseeable":["foreseeable","예측할 수 있는"],"sensitive":["sensitive","민감한"],"adaptation":["adaptation","적응"],
 "organism":["organism","유기체"],"expectation":["expectation","기대"],"observe":["observe","관찰하다"],
 "violates":["violate","어기다"],"notes":["note","음, 음표"],"fundamentally":["fundamentally","근본적으로"],
 "weakens":["weaken","약해지다"],"organisms":["organism","유기체, 생물"],"expect":["expect","예상하다"],
 "use":["use","사용하다"],"used":["use","익숙한 (get used to = ~에 익숙해지다)"],
}

JD={
 1:[["Organisms learn only when events [[contradict]]","유기체는 사건이 [[어긋날]] 때만 학습한다"],
    ["their expectations,","그들의 기대에,"],
    ["which makes surprise","그리고 이것은 놀람을 만든다"],
    ["a [[basic]] driver of learning.","학습의 [[기본적인]] 동력으로."]],
 2:[["When the same notes are repeated,","같은 음이 반복되면,"],
    ["the brain's responses gradually [[weaken]]","뇌의 반응은 서서히 [[약해진다]]"],
    ["because the brain learns to [[predict]] the next note,","뇌가 다음 음을 [[예측하는]] 것을 배우기 때문에,"],
    ["but a sudden change causes","하지만 갑작스러운 변화는 일으킨다"],
    ["a strong surprise reaction.","강한 놀람 반응을."]],
 3:[["Adaptation depends not on repetition alone","적응은 반복만이 아니라"],
    ["but on whether notes are [[foreseeable]],","음이 [[예측할 수 있는지]]에 달려 있다,"],
    ["so the brain becomes [[accustomed]] to an alternating pattern","그래서 뇌는 교차하는 패턴에 [[익숙해진다]]"],
    ["yet shows surprise at an unexpected repetition.","하지만 예상치 못한 반복에는 놀람을 보인다."]],
}

FC={
 1:[["본문 1~2번","기대가 깨져야 배운다","오류 신호란 예상과 다른 일이 벌어지는 거예요."],
    ["본문 3번","In other words! 놀람이 학습의 동력","앞 두 문장을 한 단어 '놀람'으로 정리해요."],
    ["정답 포인트","{{violate|어기다}} = {{contradict|어긋나다}}, {{fundamental|근본적인}} = {{basic|기본적인}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 4~5번","같은 음이 반복되면 반응이 줄어든다","{{progressively decrease|점점 줄어들다}}"],
    ["본문 6번","이것이 적응, 뇌가 다음을 예상한다","{{anticipate|예상하다}}"],
    ["본문 7~8번","Suddenly! 음이 바뀌면 강한 놀람","적응이 사라지고 뉴런이 힘차게 반응해요."],
    ["정답 포인트","{{decrease|줄어들다}} = {{weaken|약해지다}}, {{anticipate|예상하다}} = {{predict|예측하다}}","줄어드는 방향과 예상하는 뇌를 함께 찾아요."]],
 3:[["본문 9번","중요한 건 반복이 아니라 예측 가능성","{{predictable|예측 가능한}}"],
    ["본문 10번","For instance! ABABA도 익숙해진다","{{gets used to|~에 익숙해지다}} 그래서 반응이 다시 줄어요."],
    ["본문 11번","However! ABABB는 놀람을 일으킨다","{{unexpected repetition|예상치 못한 반복}}"],
    ["정답 포인트","{{predictable|예측 가능한}} = {{foreseeable|예측할 수 있는}}, {{gets used to|~에 익숙해지다}} = {{becomes accustomed to|~에 익숙해지다}}","익숙해지는 쪽과 놀라는 쪽을 구분해요."]],
}

STORY=[
 dict(a="violate",form="violate",n=2,sq=1,sum="only when events [[contradict]] their expectations",hook="기대가 깨질 때만 배운다는 문장의 violate(어기다) → 요약문에서는 contradict(어긋나다)로 바꿨어요."),
 dict(a="fundamental",form="fundamental",n=3,sq=1,sum="surprise a [[basic]] driver of learning",hook="놀람이 학습의 뿌리라는 문장의 fundamental(근본적인) → 요약문에서는 basic(기본적인)으로 바꿨어요."),
 dict(a="decrease",form="decrease",n=5,sq=2,sum="the brain's responses gradually [[weaken]]",hook="같은 음에 뇌 반응이 점점 작아지는 문장의 decrease(줄어들다) → 요약문에서는 weaken(약해지다)으로 바꿨어요."),
 dict(a="anticipate",form="anticipate",n=6,sq=2,sum="the brain learns to [[predict]] the next note",hook="뇌가 다음 음을 미리 짐작한다는 문장의 anticipate(예상하다) → 요약문에서는 predict(예측하다)로 바꿨어요."),
 dict(a="predictable",form="predictable",n=9,sq=3,sum="whether notes are [[foreseeable]]",hook="음이 미리 짐작되는지가 핵심이라는 문장의 predictable(예측 가능한) → 요약문에서는 foreseeable(예측할 수 있는)로 바꿨어요."),
]

SCENES=[
 dict(tag="본문 2번",ns=[2],line="기대가 깨질 때만 학습한다. 기대를 [[violate|어기는]] 일이 핵심!"),
 dict(tag="본문 3번",ns=[3],line="그래서 놀람은 학습의 [[fundamental|근본적인]] 동력이다."),
 dict(tag="본문 5번",ns=[5],line="같은 음이 계속되면 뇌의 반응이 점점 [[decrease|줄어든다]]."),
 dict(tag="본문 6번",ns=[6],line="뇌가 다음 음을 [[anticipate|예상하는]] 것을 배우는 중이다."),
 dict(tag="본문 9번",ns=[9],line="중요한 건 반복이 아니라 음이 [[predictable|예측 가능한]]지다."),
]

HLKO={2:["사건이 그들의 기대에 어긋날 때에만 학습한다"],3:["놀람은 학습의 근본적인 동력 중 하나"],
 5:["점진적으로 감소한다"],6:["다음 사건을 예상하는 것을 배우고"],8:["강한 놀람의 반응"],
 9:["그 음들이 예측 가능한지"],10:["이 교차에 익숙해지고"],11:["예상치 못한 반복"]}

UM={'contradict':('어긋나다, 모순되다','어긋난다'),'basic':('기본적인','기본적인'),'weaken':('약해지다','약해지기'),'predict':('예측하다','예측할'),'foreseeable':('예측할 수 있는','예측된다'),'accustomed':('익숙한','익숙해졌다')}

TARGET={1:0,2:2,3:4}

G.update({'other':['other','다른'],'because':['because','~ 때문에'],'out':['draw out','끌어내다 (out)'],'just':['just','단지'],'hear':['hear','듣다'],'ababa':['ABABA','교차하는 음의 예'],'ababb':['ABABB','예상 밖의 반복이 있는 음의 예']})
