# -*- coding: utf-8 -*-
# 세트 정의: 금천고2 4과 ❶
META=dict(sch='jusung-go2', src='jusung-go2/L4/sx-data.js', pidx=0, lesson='4과', title='수리할 권리와 수리 카페', label='❶', page='yoyak-lian-z1')
Q = [
 dict(
  id=1,
  summary="Liz (A) dropped her laptop on the street, (B) damaging it, so its screen is cracked and some keys do not work.",
  ko="Liz는 길에서 노트북을 <b>(A) 무심코</b> 떨어뜨려 <b>(B) 심하게</b> 망가뜨렸고, 그래서 화면은 금이 가고 몇몇 키는 작동하지 않는다.",
  opts=[["unintentionally","severely"],["unintentionally","slightly"],["deliberately","severely"],["deliberately","slightly"],["carefully","slightly"]],
  optko=["의도치 않게 – 심하게","의도치 않게 – 약간","일부러 – 심하게","일부러 – 약간","조심스럽게 – 약간"],
  ans=0,
  wrong=[None,
         "slightly(약간)가 틀려요. 본문은 노트북이 심하게(seriously) 망가졌다고 해요.",
         "deliberately(일부러)가 틀려요. Liz는 일부러가 아니라 실수로(accidentally) 떨어뜨렸어요.",
         "둘 다 틀려요. 일부러 떨어뜨린 것도, 조금만 망가진 것도 아니에요.",
         "둘 다 틀려요. 조심스럽게(carefully) 다뤘다면 떨어뜨리지 않았을 거고, 망가진 정도도 약간이 아니에요."],
  evid=[dict(n=1, hl=["accidentally dropped","seriously damaging"]), dict(n=2, hl=["the screen is cracked","some keys are not working"])],
  swaps=[["accidentally","unintentionally","실수로 → 의도하지 않고"],["seriously","severely","심각하게 → 심하게"],["cracked","damaged","금이 간 → 손상된"]],
  swapnote="accidentally(실수로)는 unintentionally(의도치 않게)로, seriously(심각하게)는 severely(심하게)로 바뀌어 나와요. 처음 보는 단어여도 앞뒤 뜻으로 짐작해 보세요.",
  use=[dict(w="unintentionally",ex="He unintentionally broke his friend's glasses.",ko="그는 의도치 않게 친구의 안경을 부러뜨렸다."),
       dict(w="severely",ex="The storm severely damaged the old bridge.",ko="그 폭풍은 오래된 다리를 심하게 손상시켰다.")],
  flow="본문 1번에서 Liz가 스터디 모임에 가다가 실수로 노트북을 떨어뜨려 심하게 망가뜨렸고, 2번에서 화면이 금 가고 키가 안 되는 상태가 구체적으로 나와요.",
 ),
 dict(
  id=2,
  summary="Liz is (A) to have her laptop fixed because repairs are often (B) and slow, and the laptop is about five years old.",
  ko="수리는 흔히 <b>(B) 비용이 많이 들고</b> 오래 걸리며 노트북도 5년 정도 되었기 때문에, Liz는 노트북을 고치는 것을 <b>(A) 꺼린다</b>.",
  opts=[["reluctant","costly"],["reluctant","cheap"],["eager","cheap"],["eager","costly"],["unable","affordable"]],
  optko=["꺼리는 – 비용이 많이 드는","꺼리는 – 값싼","열망하는 – 값싼","열망하는 – 비용이 많이 드는","할 수 없는 – 알맞은 가격의"],
  ans=0,
  wrong=[None,
         "cheap(값싼)이 틀려요. 본문은 수리가 비싸다(expensive)고 해요.",
         "둘 다 틀려요. Liz는 고치기를 망설이고(hesitate) 있고, 수리는 값싸지도 않아요.",
         "eager(열망하는)가 틀려요. Liz는 고치고 싶어 하는 게 아니라 망설이고 있어요.",
         "둘 다 틀려요. Liz는 고칠 수 있지만 망설이는 거예요(can have it repaired). 수리비도 알맞은 가격이 아니라 비싸요."],
  evid=[dict(n=3, hl=["hesitating"]), dict(n=4, hl=["expensive","take a long time"])],
  swaps=[["hesitate","reluctant","망설이다 → 꺼리는"],["expensive","costly","비싼 → 비용이 많이 드는"],["take a long time","slow","오랜 시간이 걸리다 → 느린"]],
  swapnote="hesitating(망설이는)은 reluctant(꺼리는)로, expensive(비싼)는 costly(비용이 많이 드는)로 바뀌어 나와요. 본문 단어만 찾지 말고 뜻이 같은 말을 찾으세요.",
  use=[dict(w="reluctant",ex="She was reluctant to speak in front of the class.",ko="그녀는 반 친구들 앞에서 말하기를 꺼렸다."),
       dict(w="costly",ex="A costly mistake can ruin a project.",ko="비용이 많이 드는 실수는 프로젝트를 망칠 수 있다.")],
  flow="본문 3번에서 Liz는 고칠 수는 있지만 망설이고, 4번에서 그 이유가 나와요. 수리는 비싸고 오래 걸리기도 하거든요.",
 ),
 dict(
  id=3,
  summary="Although (A) the old laptop and buying a new one may seem (B), it would contribute to the serious problem of e-waste.",
  ko="오래된 노트북을 <b>(A) 버리고</b> 새것을 사는 것이 <b>(B) 합리적</b>으로 보일 수 있지만, 그것은 전자 쓰레기라는 심각한 문제에 기여하게 될 것이다.",
  opts=[["discarding","sensible"],["discarding","foolish"],["repairing","sensible"],["repairing","foolish"],["preserving","unreasonable"]],
  optko=["버리기 – 합리적인","버리기 – 어리석은","수리하기 – 합리적인","수리하기 – 어리석은","보존하기 – 불합리한"],
  ans=0,
  wrong=[None,
         "foolish(어리석은)가 틀려요. 본문은 새로 사는 게 더 합리적인(reasonable) 선택처럼 보일 수 있다고 해요.",
         "repairing(수리하기)이 틀려요. 합리적으로 보이는 건 수리가 아니라 오래된 걸 버리고(get rid of) 새로 사는 거예요.",
         "둘 다 틀려요. 수리하기가 아니라 버리기이고, 어리석다는 말도 아니에요.",
         "둘 다 틀려요. 보존하는 게 아니라 버리는 것이고, 불합리하다고 하지 않고 합리적으로 보인다고 했어요."],
  evid=[dict(n=6, hl=["getting rid of the old one","a more reasonable option"]), dict(n=8, hl=["contributing to a serious problem"])],
  swaps=[["get rid of","discard","버리다 → 버리다"],["reasonable","sensible","합리적인 → 분별 있는, 합리적인"],["option","choice","선택 → 선택"]],
  swapnote="getting rid of(~을 버리는 것)는 discarding(버리는 것)으로, reasonable(합리적인)은 sensible(분별 있는, 합리적인)로 바뀌어 나와요.",
  use=[dict(w="discard",ex="Please do not discard the old batteries in the trash.",ko="오래된 배터리를 쓰레기통에 버리지 마세요."),
       dict(w="sensible",ex="Taking an umbrella was a sensible choice.",ko="우산을 가져간 것은 합리적인 선택이었다.")],
  flow="본문 6번에서 Liz는 낡은 노트북을 버리고 새로 사는 게 합리적으로 보이지만, 7번의 However(하지만)부터 방향이 뒤집혀요. 8번에서 버리면 전자 쓰레기 문제에 기여하게 된다고 해요.",
 ),
]

G = {
 "liz":["Liz","Liz(사람 이름)"],"laptop":["laptop","노트북 컴퓨터"],"street":["street","길, 거리"],
 "accidentally":["accidentally","실수로"],"dropped":["drop","떨어뜨리다"],"seriously":["seriously","심각하게"],
 "damaging":["damage","손상시키다"],"damaged":["damage","손상시키다 (damaged = 손상된)"],"screen":["screen","화면"],
 "cracked":["crack","금이 가다 (cracked = 금이 간)"],"keys":["key","(키보드의) 키"],"work":["work","작동하다"],
 "working":["work","작동하다"],"hesitating":["hesitate","망설이다"],"hesitate":["hesitate","망설이다"],
 "repairs":["repair","수리"],"repaired":["repair","수리하다 (have it repaired = 수리받다)"],"fixed":["fix","고치다 (fixed = 고쳐진)"],
 "expensive":["expensive","비싼"],"take":["take","(시간이) 걸리다"],"long":["long","오랜, 긴"],"time":["time","시간"],
 "often":["often","자주, 흔히"],"slow":["slow","느린, 오래 걸리는"],"about":["about","약, ~쯤"],"years":["year","해, 년"],"five":["five","다섯"],
 "unintentionally":["unintentionally","의도치 않게"],"severely":["severely","심하게"],"slightly":["slightly","약간, 조금"],
 "deliberately":["deliberately","일부러"],"carefully":["carefully","조심스럽게"],"reluctant":["reluctant","꺼리는, 내키지 않는"],
 "costly":["costly","비용이 많이 드는"],"cheap":["cheap","값싼"],"eager":["eager","열망하는, 몹시 하고 싶어 하는"],
 "unable":["unable","~할 수 없는"],"affordable":["affordable","(값이) 알맞은, 감당할 만한"],"because":["because","~ 때문에"],
 "discarding":["discard","버리다"],"discard":["discard","버리다"],"sensible":["sensible","분별 있는, 합리적인"],"foolish":["foolish","어리석은"],
 "repairing":["repair","수리하다"],"preserving":["preserve","보존하다"],"unreasonable":["unreasonable","불합리한, 터무니없는"],
 "buying":["buy","사다"],"new":["new","새로운"],"old":["old","오래된"],"seem":["seem","~처럼 보이다"],"contribute":["contribute","기여하다, 원인이 되다"],
 "contributing":["contribute","기여하다, 원인이 되다"],"serious":["serious","심각한"],"problem":["problem","문제"],"e-waste":["e-waste","전자 쓰레기"],
 "getting":["get","~하다 (get rid of = 버리다)"],"rid":["rid","없애다 (get rid of = ~을 버리다)"],"reasonable":["reasonable","합리적인"],
 "option":["option","선택(지)"],"choice":["choice","선택"],"waste":["waste","쓰레기"],"would":["would","~할 것이다"],
 "like":["like","~처럼 (seem like = ~처럼 보이다)"],"umbrella":["umbrella","우산"],"batteries":["battery","배터리"],"trash":["trash","쓰레기통"],
 "glasses":["glasses","안경"],"storm":["storm","폭풍"],"bridge":["bridge","다리"],"mistake":["mistake","실수"],"project":["project","프로젝트"],
 "study":["study","공부하다"],"group":["group","모임"],"meeting":["meeting","모임"],"turns":["turn","(on) 켜지다"],"still":["still","여전히"],
 "though":["though","~이지만"],"although":["although","~이지만"],"throws":["throw","던지다, 버리다"],"way":["way","길"],"sometimes":["sometimes","때때로"],
 "besides":["besides","게다가"],"case":["case","경우"],"purchasing":["purchase","구입하다"],"reality":["reality","현실"],"however":["however","하지만"],
}

JD={
 1:[["Liz [[unintentionally]] dropped her laptop on the street,","Liz는 길에서 노트북을 [[의도치 않게]] 떨어뜨렸고,"],
    ["[[severely]] damaging it,","그것을 [[심하게]] 손상시켰고,"],
    ["so its screen is cracked","그래서 화면은 금이 갔고"],
    ["and some keys do not work.","몇몇 키는 작동하지 않는다."]],
 2:[["Liz is [[reluctant]] to have her laptop fixed","Liz는 노트북을 고치는 것을 [[꺼린다]]"],
    ["because repairs are often [[costly]] and slow,","수리는 흔히 [[비용이 많이 들고]] 느리기 때문에,"],
    ["and the laptop is about five years old.","그리고 노트북이 5년 정도 되었기 때문이다."]],
 3:[["Although [[discarding]] the old laptop","오래된 노트북을 [[버리는 것]]이"],
    ["and buying a new one may seem [[sensible]],","그리고 새것을 사는 것이 [[합리적으로]] 보일 수 있지만,"],
    ["it would contribute to the serious problem of e-waste.","그것은 전자 쓰레기라는 심각한 문제에 기여하게 될 것이다."]],
}

FC={
 1:[["본문 1번","스터디 가던 길, 노트북을 떨어뜨렸다","실수로 떨어뜨려 심하게 망가졌어요."],
    ["본문 2번","화면은 금 가고, 키는 안 눌린다","켜지긴 하지만 상태가 나빠요."],
    ["정답 포인트","{{accidentally|실수로}} = {{unintentionally|의도치 않게}}, {{seriously|심각하게}} = {{severely|심하게}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 3번","고칠 수는 있는데 망설인다","Liz의 마음이 흔들려요."],
    ["본문 4번","수리는 비싸고 오래 걸린다","거기에 노트북도 5년이나 됐어요."],
    ["정답 포인트","{{hesitating|망설이는}} = {{reluctant|꺼리는}}, {{expensive|비싼}} = {{costly|비용이 많이 드는}}","반대말(eager, cheap)에 속지 마세요."]],
 3:[["본문 6번","낡은 건 버리고 새로 사는 게 합리적?","그럴듯해 보이는 생각이에요."],
    ["본문 7번","{{However|하지만}}","여기서 방향이 뒤집혀요."],
    ["본문 8번","버리면 전자 쓰레기 문제에 기여한다","{{e-waste|전자 쓰레기}}가 진짜 문제예요."],
    ["정답 포인트","{{getting rid of|버리는 것}} = {{discarding|버리는 것}}, {{reasonable|합리적인}} = {{sensible|분별 있는}}","'그럴듯해 보인다'가 핵심이에요."]],
}

STORY=[
 dict(a="accidentally",form="accidentally",n=1,sq=1,sum="Liz [[unintentionally]] dropped her laptop",hook="길에서 노트북을 툭 떨어뜨린 그 문장의 accidentally(실수로) → 요약문에서는 unintentionally(의도치 않게)로 바꿨어요."),
 dict(a="seriously",form="seriously",n=1,sq=1,sum="[[severely]] damaging it",hook="노트북이 크게 망가졌다는 문장의 seriously(심각하게) → 요약문에서는 severely(심하게)로 바꿨어요."),
 dict(a="hesitate",form="hesitating",n=3,sq=2,sum="Liz is [[reluctant]] to have her laptop fixed",hook="고칠 수는 있는데 마음이 안 내키는 문장의 hesitating(망설이는) → 요약문에서는 reluctant(꺼리는)로 바꿨어요."),
 dict(a="expensive",form="expensive",n=4,sq=2,sum="repairs are often [[costly]] and slow",hook="수리비가 부담된다는 문장의 expensive(비싼) → 요약문에서는 costly(비용이 많이 드는)로 바꿨어요."),
 dict(a="reasonable",form="reasonable",n=6,sq=3,sum="may seem [[sensible]]",hook="새로 사는 게 낫겠다 싶은 문장의 reasonable(합리적인) → 요약문에서는 sensible(분별 있는)로 바꿨어요."),
]

SCENES=[
 dict(tag="본문 1번",ns=[1],line="스터디 가던 길, Liz가 [[accidentally|실수로]] 노트북을 떨어뜨려 [[seriously|심각하게]] 망가뜨렸다."),
 dict(tag="본문 3번",ns=[3],line="고칠 수는 있지만 [[hesitating|망설이고]] 있다."),
 dict(tag="본문 4번",ns=[4],line="수리는 [[expensive|비싸고]] 오래 걸린다."),
 dict(tag="본문 6번",ns=[6],line="낡은 걸 버리고 새로 사는 게 더 [[reasonable|합리적]]이라는 생각이 든다."),
 dict(tag="본문 8번",ns=[7,8],line="하지만 버리면 전자 쓰레기 문제에 기여하게 된다."),
]

HLKO={1:["실수로","심각하게 손상시켰다"],2:["화면은 금이 갔고","몇몇 키들은 작동하지 않는다"],3:["망설이고 있다"],4:["돈이 많이 들고","오랜 시간이 걸린다"],
 6:["오래된 노트북은 버리고","더 합리적인 선택"],8:["심각한 문제에 기여하게 될 것이다"]}

UM={'unintentionally':('의도치 않게','의도치 않게'),'severely':('심하게','심하게'),'reluctant':('꺼리는','꺼렸다'),'costly':('비용이 많이 드는','비용이 많이 드는'),'discard':('버리다','버리지'),'sensible':('분별 있는, 합리적인','합리적인')}

TARGET={1:3,2:0,3:2}
