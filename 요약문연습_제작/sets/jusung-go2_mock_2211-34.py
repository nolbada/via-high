# -*- coding: utf-8 -*-
# 세트 정의: 주성고2 모의고사 22년 11월 34번
META=dict(sch='jusung-go2', src='jusung-go2/mock/sx-data.js', pidx=5, lesson='22년 11월 34번', title='', label='', page='yoyak-2211-34')
Q = [
 dict(
  id=1,
  summary="Studies that observe humans cannot be properly (A) because people have different lifestyles and environments, so they are not (B) enough to be suitable subjects.",
  ko="인간을 관찰하는 연구는 사람마다 생활 방식과 환경이 달라서 적절하게 <b>(A) 관리될</b> 수 없고, 그래서 사람들은 적절한 대상이 되기에 충분히 <b>(B) 비슷하지</b> 않다.",
  opts=[["managed","similar"],["managed","diverse"],["repeated","diverse"],["repeated","similar"],["ignored","diverse"]],
  optko=["관리하다 – 비슷한","관리하다 – 다양한","반복하다 – 다양한","반복하다 – 비슷한","무시하다 – 다양한"],
  ans=0,
  wrong=[None,
         "diverse(다양한)가 틀려요. 본문은 사람들이 서로 비슷하지 않아서 문제라고 해요.",
         "둘 다 틀려요. repeat(반복하다)는 본문에 없고, 사람들이 diverse(다양하다)는 점이 문제의 이유지 '충분히 ~ 않다'의 내용이 아니에요.",
         "repeated(반복하다)가 틀려요. 본문은 연구를 반복하는 게 아니라 통제(관리)가 안 된다고 해요.",
         "둘 다 틀려요. ignore(무시하다)는 본문에 없고, diverse(다양한)는 '충분히 ~ 않다'와 맞지 않아요."],
  evid=[dict(n=1, hl=["cannot be properly controlled"]), dict(n=2, hl=["different lifestyles","different environments"]), dict(n=3, hl=["insufficiently homogeneous"])],
  swaps=[["controlled","managed","통제하다 → 관리하다"],["homogeneous","similar","동질적인 → 비슷한"],["insufficiently","not enough","충분하지 않게 → 충분히 ~ 않은"]],
  swapnote="control(통제하다)은 manage(관리하다)로, homogeneous(동질적인)는 similar(비슷한), uniform(똑같은)으로 바뀔 수 있어요. 어려운 단어는 앞뒤 흐름으로 짐작해요.",
  use=[dict(w="manage",ex="She can manage her time well.",ko="그녀는 자신의 시간을 잘 관리할 수 있다."),
       dict(w="similar",ex="The twins have similar voices.",ko="그 쌍둥이는 비슷한 목소리를 가졌다.")],
  flow="본문 1번에서 인간 관찰 연구는 통제가 안 된다고 말하고, 2번에서 사람마다 생활과 환경이 다르다는 이유를 대요. 3번 Thus(따라서)로 '비슷하지 않아서 실험 대상으로 부적절하다'고 결론을 내요.",
 ),
 dict(
  id=2,
  summary="Other variables can make it hard to (A) the effect of one factor, as shown when the apparent (B) between coffee and heart disease mostly disappeared once smoking was considered.",
  ko="다른 변수들은 한 요인의 영향을 <b>(A) 분리하기</b> 어렵게 만들 수 있는데, 흡연을 고려하자 커피와 심장 질환 사이의 겉보기 <b>(B) 연관성</b>이 대부분 사라진 것이 그 예이다.",
  opts=[["separate","connection"],["separate","difference"],["increase","difference"],["increase","connection"],["predict","difference"]],
  optko=["분리하다 – 연관성","분리하다 – 차이","늘리다 – 차이","늘리다 – 연관성","예측하다 – 차이"],
  ans=0,
  wrong=[None,
         "difference(차이)가 틀려요. 본문은 커피와 심장병 사이의 '관련(상관관계)'이 사라졌다고 해요.",
         "둘 다 틀려요. 영향을 늘리는 게 아니라 분리하기 어렵다는 이야기고, 차이가 아니라 관련성이에요.",
         "increase(늘리다)가 틀려요. 본문은 영향을 분리하기 어렵다고 해요.",
         "둘 다 틀려요. 예측하다(predict)나 차이(difference)는 본문에 없어요."],
  evid=[dict(n=5, hl=["isolate the effects"]), dict(n=7, hl=["significant correlation"]), dict(n=8, hl=["most of this correlation disappeared"])],
  swaps=[["isolate","separate","분리하다 → 떼어 놓다"],["correlation","connection","상관관계 → 연관성"],["corrected for","considered","~을 수정하다 → 고려하다"]],
  swapnote="isolate(분리하다)는 separate(떼어 놓다)로, correlation(상관관계)은 connection(연관성)이나 link(연결)로 바뀌어 나와요.",
  use=[dict(w="separate",ex="Please separate the red socks from the blue ones.",ko="빨간 양말을 파란 양말과 분리해 주세요."),
       dict(w="connection",ex="There is a clear connection between sleep and health.",ko="수면과 건강 사이에는 분명한 연관성이 있다.")],
  flow="본문 5~6번에서 교란 변수 때문에 한 요인의 영향을 떼어 내기 어렵다고 해요. 7번 Similarly(마찬가지로)로 커피 예시가 나오고, 8번 However(그러나)에서 흡연을 고려하자 상관관계가 대부분 사라져요.",
 ),
 dict(
  id=3,
  summary="Researchers can often (A) for known confounding factors, but unknown ones (B) the reliability of causal conclusions.",
  ko="연구자들은 알려진 교란 변수는 종종 <b>(A) 보정할</b> 수 있지만, 알려지지 않은 교란 변수는 인과적 결론의 신뢰성을 <b>(B) 약화시킨다</b>.",
  opts=[["adjust","weaken"],["adjust","strengthen"],["search","strengthen"],["search","weaken"],["wait","strengthen"]],
  optko=["보정하다 – 약화시키다","보정하다 – 강화하다","찾다 – 강화하다","찾다 – 약화시키다","기다리다 – 강화하다"],
  ans=0,
  wrong=[None,
         "strengthen(강화하다)이 틀려요. 알려지지 않은 변수는 결론을 믿기 어렵게 만들어요.",
         "둘 다 틀려요. 본문은 변수를 찾는 게 아니라 수정(보정)한다고 하고, 신뢰성은 강화가 아니라 손상돼요.",
         "search(찾다)가 틀려요. 본문은 알려진 변수를 수정(보정)할 수 있다고 해요.",
         "둘 다 틀려요. 기다린다는 말은 본문에 없고, 신뢰성은 강화가 아니라 손상돼요."],
  evid=[dict(n=9, hl=["correct for them"]), dict(n=10, hl=["undermine the reliability"])],
  swaps=[["correct","adjust","수정하다 → 보정하다"],["undermine","weaken","손상시키다 → 약화시키다"],["it is possible","can","가능하다 → ~할 수 있다"]],
  swapnote="correct(수정하다)는 adjust(조정하다)로, undermine(손상시키다)은 weaken(약화시키다), damage(해치다)로 바뀌어 나올 수 있어요.",
  use=[dict(w="adjust",ex="You can adjust the chair to your height.",ko="의자를 네 키에 맞게 조정할 수 있다."),
       dict(w="weaken",ex="Bad news can weaken people's trust.",ko="나쁜 소식은 사람들의 신뢰를 약화시킬 수 있다.")],
  flow="본문 9번은 If(만약) 변수가 알려져 있으면 수정할 수 있다는 좋은 경우, 10번은 However(그러나) 알려져 있지 않으면 결론의 신뢰성이 손상된다는 나쁜 경우예요.",
 ),
]

G = {
 "observational":["observational","관찰에 의한"],"studies":["study","연구"],"study":["study","연구"],"humans":["human","인간"],
 "cannot":["cannot","~할 수 없다"],"properly":["properly","적절하게"],"controlled":["control","통제하다"],
 "live":["live","살다"],"different":["different","서로 다른"],"lifestyles":["lifestyle","생활 방식"],
 "environments":["environment","환경"],"thus":["thus","따라서"],"insufficiently":["insufficiently","충분하지 않게"],
 "homogeneous":["homogeneous","동질적인"],"suitable":["suitable","적절한"],"experimental":["experimental","실험의"],
 "subjects":["subject","대상"],"confounding":["confounding","교란시키는"],"factors":["factor","요인, 변수"],
 "factor":["factor","요인, 변수"],"undermine":["undermine","손상시키다"],"our":["our","우리의"],"ability":["ability","능력"],
 "draw":["draw","(결론을) 도출하다"],"sound":["sound","타당한"],"causal":["causal","인과적인"],"conclusions":["conclusion","결론"],
 "epidemiological":["epidemiological","역학의"],"surveys":["survey","조사"],"variables":["variable","변수"],
 "variable":["variable","변수"],"known":["know","알려진 (known = 알려져 있는)"],"unknown":["unknown","알려지지 않은"],
 "make":["make","~하게 만들다"],"difficult":["difficult","어려운"],"epidemiologists":["epidemiologist","역학자"],
 "isolate":["isolate","분리하다"],"effects":["effect","영향"],"effect":["effect","영향"],"specific":["specific","특정한"],
 "being":["be","~되고 있는"],"studied":["study","연구하다 (studied = 연구되는)"],"example":["example","예"],
 "argued":["argue","주장하다"],"since":["since","~이기 때문에"],"drink":["drink","마시다"],"smoke":["smoke","흡연하다"],
 "researchers":["researcher","연구자"],"difficulty":["difficulty","어려움"],"determining":["determine","결정짓다"],
 "link":["link","연관성"],"alcohol":["alcohol","알코올"],"consumption":["consumption","섭취"],"cancer":["cancer","암"],
 "similarly":["similarly","마찬가지로"],"famous":["famous","유명한"],"identified":["identify","확인하다"],
 "significant":["significant","상당한"],"correlation":["correlation","상관관계"],"coffee":["coffee","커피"],
 "drinking":["drink","마시다 (drinking = 마시는 것)"],"coronary":["coronary","관상 동맥의"],"heart":["heart","심장"],
 "disease":["disease","질병"],"however":["however","그러나"],"most":["most","대부분"],"disappeared":["disappear","사라지다"],
 "once":["once","~하자, ~하면"],"corrected":["correct","수정하다 (corrected for = ~에 대해 보정하다)"],"fact":["fact","사실"],
 "drinkers":["drinker","마시는 사람"],"possible":["possible","가능한"],"often":["often","종종"],"correct":["correct","수정하다, 보정하다"],
 "reliability":["reliability","신뢰성"],"draw":["draw","(결론을) 도출하다"],"weaken":["weaken","약화시키다"],
 "strengthen":["strengthen","강화하다"],"manage":["manage","관리하다"],"managed":["manage","관리하다 (managed = 관리되는)"],
 "repeated":["repeat","반복하다 (repeated = 반복되는)"],"ignored":["ignore","무시하다 (ignored = 무시되는)"],
 "similar":["similar","비슷한"],"diverse":["diverse","다양한"],"separate":["separate","분리하다"],"connection":["connection","연관성"],
 "difference":["difference","차이"],"increase":["increase","늘리다"],"predict":["predict","예측하다"],"adjust":["adjust","조정하다, 보정하다"],
 "search":["search","찾다"],"wait":["wait","기다리다"],"considered":["consider","고려하다 (considered = 고려되는)"],
 "apparent":["apparent","겉보기의"],"between":["between","~ 사이에"],"mostly":["mostly","대부분"],"smoking":["smoking","흡연"],
 "people":["people","사람들"],"environment":["environment","환경"],"lifestyle":["lifestyle","생활 방식"],"hard":["hard","어려운"],
 "shown":["show","보여 주다 (shown = 보여진)"],"conclusion":["conclusion","결론"],"unknown":["unknown","알려지지 않은"],
 "observe":["observe","관찰하다"],"cannot":["cannot","~할 수 없다"],"differ":["differ","다르다"],"enough":["enough","충분히"],
 "reliable":["reliable","믿을 만한"],"effects":["effect","영향"],"correlations":["correlation","상관관계"],
 "damage":["damage","해치다"],"known":["know","알려진"],"smoking":["smoking","흡연"],"smoke":["smoke","흡연하다"],"smoking":["smoking","흡연"],
 "heart":["heart","심장"],"variable":["variable","변수"],
}

JD={
 1:[["Studies that observe humans","인간을 관찰하는 연구는"],
    ["cannot be properly [[managed]]","적절하게 [[관리될]] 수 없다"],
    ["because people have different lifestyles and environments,","사람들이 서로 다른 생활 방식과 환경을 가지고 있어서,"],
    ["so they are not [[similar]] enough","그래서 그들은 충분히 [[비슷하지]] 않다"],
    ["to be suitable subjects.","적절한 대상이 되기에는."]],
 2:[["Other variables can make it hard","다른 변수들은 어렵게 만들 수 있다"],
    ["to [[separate]] the effect of one factor,","한 요인의 영향을 [[분리하는]] 것을,"],
    ["as shown when the apparent [[connection]]","겉보기 [[연관성]]이 ~했을 때 보여지듯이"],
    ["between coffee and heart disease","커피와 심장 질환 사이의"],
    ["mostly disappeared once smoking was considered.","흡연이 고려되자 대부분 사라졌다."]],
 3:[["Researchers can often [[adjust]] for known confounding factors,","연구자들은 알려진 교란 변수는 종종 [[보정할]] 수 있지만,"],
    ["but unknown ones [[weaken]]","알려지지 않은 것들은 [[약화시킨다]]"],
    ["the reliability of causal conclusions.","인과적 결론의 신뢰성을."]],
}

FC={
 1:[["본문 1~2번","인간 연구는 통제가 안 된다","사람마다 생활 방식과 환경이 달라요."],
    ["본문 3번","Thus! 그래서 서로 비슷하지 않다","실험 대상으로 쓰기엔 부적절해요."],
    ["정답 포인트","{{controlled|통제된}} = {{managed|관리된}}, {{homogeneous|동질적인}} = {{similar|비슷한}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 5번","교란 변수는 영향을 떼어 내기 어렵게 한다","{{isolate|분리하다}}가 핵심 단어예요."],
    ["본문 7~8번","커피와 심장병 → 흡연을 고려하자 대부분 사라짐","{{correlation|상관관계}}가 사라졌어요."],
    ["정답 포인트","{{isolate|분리하다}} = {{separate|떼어 놓다}}, {{correlation|상관관계}} = {{connection|연관성}}","커피 예시에서 사라진 것이 무엇인지 찾아요."]],
 3:[["본문 9번","변수를 알면 수정할 수 있다","좋은 경우예요."],
    ["본문 10번","However! 모르면 결론이 믿기 어렵다","나쁜 경우예요."],
    ["정답 포인트","{{correct|수정하다}} = {{adjust|보정하다}}, {{undermine|손상시키다}} = {{weaken|약화시키다}}","알려진 경우와 모르는 경우를 나눠 읽어요."]],
}

STORY=[
 dict(a="controlled",form="controlled",n=1,sq=1,sum="cannot be properly [[managed]]",hook="사람 연구는 마음대로 조절이 안 된다는 문장의 controlled(통제된) → 요약문에서는 managed(관리된)로 바꿨어요."),
 dict(a="homogeneous",form="homogeneous",n=3,sq=1,sum="they are not [[similar]] enough",hook="사람들이 서로 같은 부류가 아니라는 문장의 homogeneous(동질적인) → 요약문에서는 similar(비슷한)로 바꿨어요."),
 dict(a="isolate",form="isolate",n=5,sq=2,sum="make it hard to [[separate]] the effect of one factor",hook="영향 하나만 쏙 떼어 내기 어렵다는 문장의 isolate(분리하다) → 요약문에서는 separate(떼어 놓다)로 바꿨어요."),
 dict(a="correlation",form="correlation",n=7,sq=2,sum="the apparent [[connection]] between coffee and heart disease",hook="커피와 심장병이 붙어 다닌 것처럼 보였다는 문장의 correlation(상관관계) → 요약문에서는 connection(연관성)으로 바꿨어요."),
 dict(a="correct",form="correct",n=9,sq=3,sum="Researchers can often [[adjust]] for known confounding factors",hook="알려진 변수는 바로잡을 수 있다는 문장의 correct(수정하다) → 요약문에서는 adjust(보정하다)로 바꿨어요."),
 dict(a="undermine",form="undermine",n=10,sq=3,sum="unknown ones [[weaken]] the reliability",hook="모르는 변수는 결론의 믿음을 갉아먹는다는 문장의 undermine(손상시키다) → 요약문에서는 weaken(약화시키다)으로 바꿨어요."),
]

SCENES=[
 dict(tag="본문 1~3번",ns=[1,2,3],line="사람은 생활도 환경도 제각각이라, 사람 연구는 [[controlled|통제]]하기 어렵고 실험 대상으로도 서로 [[homogeneous|동질적]]이지 않다."),
 dict(tag="본문 5번",ns=[5],line="숨은 변수가 있으면 한 요인의 영향만 [[isolate|분리하기]] 어렵다."),
 dict(tag="본문 7번",ns=[7],line="커피와 심장병 사이에 큰 [[correlation|상관관계]]가 있어 보였다."),
 dict(tag="본문 8번",ns=[8],line="하지만 흡연을 고려하자 그 관계는 대부분 사라졌다."),
 dict(tag="본문 9번",ns=[9],line="변수를 알면 [[correct|수정]]해서 바로잡을 수 있다."),
 dict(tag="본문 10번",ns=[10],line="모르면 결론의 신뢰성을 [[undermine|손상시킨다]]."),
]

HLKO={1:["적절하게 통제될 수 없다"],2:["서로 다른 생활 방식으로","서로 다른 환경에서"],3:["충분히 동질적이지 않다"],
 5:["영향을 분리하기 어렵게"],7:["상당한 상관관계"],8:["상관관계의 대부분은 사라졌다"],9:["그것들을 수정하는 것이 종종 가능하다"],10:["신뢰성을 손상시킬 것이다"]}

UM={'manage':('관리하다','관리할'),'similar':('비슷한','비슷한'),'separate':('분리하다','분리해'),'connection':('연관성','연관성'),'adjust':('조정하다, 보정하다','조정할'),'weaken':('약화시키다','약화시킬')}

G.update({'because':['because','~ 때문에'],'other':['other','다른'],'ones':['one','것들'],'framingham':['Framingham','프레이밍햄(연구 이름)'],'lifestyles':['lifestyle','생활 방식']})

TARGET={1:3,2:0,3:2}
