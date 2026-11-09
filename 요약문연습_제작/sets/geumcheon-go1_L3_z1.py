# -*- coding: utf-8 -*-
# 세트 정의: 금천고1 3과 ❶
META=dict(sch='geumcheon-go1', src='geumcheon-go1/L3/sx-data.js', pidx=0, lesson='3과', title='The True Art Lovers', label='❶', page='yoyak-lian-z1')
Q = [
 dict(
  id=1,
  summary="The docent will introduce three artists who did not (A) their art in spite of the (B) in their lives.",
  ko="도슨트는 삶 속의 <b>(B) 어려움</b>에도 불구하고 자신의 예술을 <b>(A) 포기하지</b> 않은 세 명의 예술가를 소개할 것이다.",
  opts=[["abandon","difficulties"],["abandon","achievements"],["change","difficulties"],["change","achievements"],["hide","honors"]],
  optko=["포기하다 – 어려움","포기하다 – 성취","바꾸다 – 어려움","바꾸다 – 성취","숨기다 – 영예"],
  ans=0,
  wrong=[None,
         "achievements(성취)가 틀려요. 본문은 성취가 아니라 인생의 역경(challenges)이에요.",
         "change(바꾸다)가 틀려요. 예술가들은 예술을 바꾼 게 아니라 포기하지 않았어요(never gave up).",
         "둘 다 틀려요. 예술을 바꾼다는 말도, 성취라는 말도 본문에 없어요.",
         "둘 다 틀려요. 예술을 숨겼다는 말도, honors(영예)라는 말도 본문에 없어요."],
  evid=[dict(n=3, hl=["never gave up on their art","challenges in their lives"])],
  swaps=[["challenge","difficulty","역경 → 어려움"],["give up on","abandon","~을 포기하다 → 포기하다"],["despite","in spite of","~에도 불구하고 → ~에도 불구하고"]],
  swapnote="challenge(역경)는 시험에서 difficulty(어려움), hardship(고난)로 바뀌어 나와요. give up(포기하다)은 abandon(포기하다, 버리다)으로 바뀌어요.",
  use=[dict(w="abandon",ex="He did not abandon his dream.",ko="그는 자신의 꿈을 포기하지 않았다."),
       dict(w="difficulty",ex="She smiled in spite of the difficulty.",ko="그녀는 그 어려움에도 불구하고 미소 지었다.")],
  flow="본문 1~2번은 도슨트(전시 안내자)의 인사예요. 3번에서 오늘 만날 세 예술가는 인생의 역경에도 예술을 포기하지 않은 사람들이라고 소개해요.",
 ),
 dict(
  id=2,
  summary="Each artist has a (A) painting style and a story that has made their work greatly (B).",
  ko="각 예술가에게는 <b>(A) 독특한</b> 화풍과 작품이 크게 <b>(B) 인정받게</b> 만든 이야기가 있다.",
  opts=[["distinctive","appreciated"],["distinctive","ignored"],["ordinary","appreciated"],["ordinary","criticized"],["borrowed","forgotten"]],
  optko=["독특한 – 높이 평가받는","독특한 – 무시당하는","평범한 – 높이 평가받는","평범한 – 비판받는","빌려 온 – 잊힌"],
  ans=0,
  wrong=[None,
         "ignored(무시당하는)가 틀려요. 본문은 작품이 높이 평가받게(highly valued) 됐다고 해요.",
         "ordinary(평범한)가 틀려요. 본문은 화풍이 평범한 게 아니라 독특한(unique) 화풍이라고 해요.",
         "둘 다 틀려요. 평범하다는 말도, 비판받았다는 말도 본문에 없어요.",
         "둘 다 틀려요. 빌려 온 화풍이라는 말도, 잊혔다는 말도 본문에 없어요."],
  evid=[dict(n=4, hl=["unique painting style","highly valued"])],
  swaps=[["unique","distinctive","독특한 → 독특한, 특유의"],["value","appreciate","높이 평가하다 → 높이 평가하다, 인정하다"],["highly","greatly","매우 → 크게"]],
  swapnote="unique(독특한)는 distinctive(독특한, 특유의)로, valued(높이 평가받는)는 appreciated(인정받는)로 바뀌어 나와요. 본문 단어가 아니라 뜻이 같은 말을 찾으세요.",
  use=[dict(w="distinctive",ex="The singer has a distinctive voice.",ko="그 가수는 독특한 목소리를 가지고 있다."),
       dict(w="appreciate",ex="Everyone will appreciate your hard work.",ko="모두가 너의 노력을 높이 평가할 것이다.")],
  flow="본문 4번은 세 예술가 모두에게 해당하는 이야기예요. 각자 독특한 화풍과 사연이 있고, 그 덕분에 작품이 높이 평가받는다고 해요.",
 ),
 dict(
  id=3,
  summary="Traylor was born a (A) and, even after becoming free, he continued to suffer from racial (B) at work.",
  ko="Traylor는 <b>(A) 노예</b>로 태어났고, 자유의 몸이 된 후에도 일터에서 계속 인종적 <b>(B) 편견</b>에 시달렸다.",
  opts=[["slave","prejudice"],["slave","kindness"],["citizen","prejudice"],["citizen","kindness"],["painter","equality"]],
  optko=["노예 – 편견, 차별","노예 – 친절","시민 – 편견, 차별","시민 – 친절","화가 – 평등"],
  ans=0,
  wrong=[None,
         "kindness(친절)가 틀려요. 본문은 친절이 아니라 인종차별(racial discrimination)에 직면했다고 해요.",
         "citizen(시민)이 틀려요. 본문은 Traylor가 노예(slavery)로 태어났다고 해요.",
         "둘 다 틀려요. 시민으로 태어난 게 아니라 노예였고, 친절이 아니라 차별을 겪었어요.",
         "둘 다 틀려요. Traylor는 화가로 태어난 게 아니라 85세에 그림을 시작했고, 평등이 아니라 차별을 겪었어요."],
  evid=[dict(n=7, hl=["born into slavery"]), dict(n=8, hl=["still had to face racial discrimination"])],
  swaps=[["slavery","slave","노예 신분 → 노예"],["discrimination","prejudice","차별 → 편견, 차별"],["still had to face","continued to suffer from","여전히 직면해야 했다 → 계속 시달렸다"]],
  swapnote="discrimination(차별)은 prejudice(편견)로 바뀌어 나올 수 있어요. slavery(노예 제도)는 slave(노예)로 품사가 바뀌어도 뜻은 이어져요.",
  use=[dict(w="slave",ex="The story is about a slave who dreamed of freedom.",ko="그 이야기는 자유를 꿈꾼 노예에 관한 것이다."),
       dict(w="prejudice",ex="We must fight prejudice against others.",ko="우리는 다른 사람에 대한 편견과 맞서 싸워야 한다.")],
  flow="본문 7번에서 Traylor는 노예로 태어나 농장에서 일해요. 8번에서 Although(비록 ~지만)로 반전! 자유의 몸이 되어도 인종차별은 계속됐어요.",
 ),
 dict(
  id=4,
  summary="At about 70, Traylor (A) to a city and took a factory job, and at 85, when he was too ill to work, he began drawing to (B) his life experiences.",
  ko="70세 무렵 Traylor는 도시로 <b>(A) 이사했고</b> 공장에서 일자리를 얻었으며, 85세에 몸이 너무 아파 일을 할 수 없게 되자 자신의 인생 경험을 <b>(B) 전달하려고</b> 그림을 그리기 시작했다.",
  opts=[["relocated","convey"],["relocated","hide"],["returned","convey"],["returned","hide"],["escaped","forget"]],
  optko=["이사하다 – 전달하다","이사하다 – 숨기다","돌아오다 – 전달하다","돌아오다 – 숨기다","탈출하다 – 잊다"],
  ans=0,
  wrong=[None,
         "hide(숨기다)가 틀려요. 그림을 그린 이유는 인생 경험을 숨기려는 게 아니라 표현하려는(express) 거예요.",
         "returned(돌아오다)가 틀려요. 몽고메리는 돌아간 곳이 아니라 70세 무렵 새로 옮겨 간(moved) 도시예요.",
         "둘 다 틀려요. 돌아왔다는 말도, 경험을 숨기려 했다는 말도 본문에 없어요.",
         "둘 다 틀려요. 도시로 탈출했다는 말도, 경험을 잊으려 했다는 말도 본문에 없어요."],
  evid=[dict(n=9, hl=["moved to the city of Montgomery"]), dict(n=10, hl=["too ill to work","turned to drawing to express his life experiences"])],
  swaps=[["move","relocate","이주하다 → 이사하다"],["express","convey","표현하다 → 전달하다"],["turned to drawing","began drawing","그림으로 눈을 돌렸다 → 그림을 그리기 시작했다"],["found a job in a factory","took a factory job","공장에서 일자리를 얻었다 → 공장 일을 맡았다"]],
  swapnote="move(이주하다)는 relocate(이사하다, 옮기다)로, express(표현하다)는 convey(전달하다)로 바뀌어 나와요. 처음 보는 단어여도 앞뒤 뜻으로 짐작해 보세요.",
  use=[dict(w="relocate",ex="His family decided to relocate to a new city.",ko="그의 가족은 새로운 도시로 이사하기로 결정했다."),
       dict(w="convey",ex="Music can convey feelings without words.",ko="음악은 말 없이 감정을 전달할 수 있다.")],
  flow="본문 9번에서 70세 무렵 몽고메리로 이주해 공장 일을 해요. 10번에서 85세에 몸이 너무 아파 일을 못 하게 되자 그제야 그림을 시작해요(It wasn't until ~ = ~하고서야 비로소).",
 ),
]

# 단어 사전: 표면형(소문자) -> [기본형, 이 글에서의 뜻]
G = {
 "welcome":["welcome","환영하다"],"dream":["dream","꿈"],"art":["art","예술, 미술"],"gallery":["gallery","미술관, 화랑"],
 "i'm":["I am","나는 ~이다"],"docent":["docent","도슨트(전시 안내자)"],"exhibit":["exhibit","전시회"],"shadows":["shadow","그림자"],
 "spotlights":["spotlight","주목, 스포트라이트"],"today":["today","오늘"],"going":["go","가다 (be going to ~ = ~할 예정이다)"],
 "meet":["meet","만나다"],"three":["three","셋의"],"amazing":["amazing","놀라운"],"artists":["artist","예술가"],"artist":["artist","예술가"],
 "never":["never","결코 ~않다"],"gave":["give","주다 (give up on = ~을 포기하다)"],"despite":["despite","~에도 불구하고"],
 "challenges":["challenge","역경, 어려움"],"challenge":["challenge","역경, 어려움"],"lives":["life","삶"],"life":["life","삶"],
 "each":["each","각각의"],"unique":["unique","독특한"],"painting":["painting","그림, 그리기"],"style":["style","화풍, 스타일"],
 "story":["story","이야기, 사연"],"made":["make","만들다"],"work":["work","작품, 일하다"],"highly":["highly","매우, 높이"],
 "valued":["value","높이 평가하다 (valued = 높이 평가받는)"],"let's":["let us","~하자"],"explore":["explore","살펴보다, 탐구하다"],
 "artwork":["artwork","미술 작품"],"first":["first","첫 번째의"],"examine":["examine","살펴보다"],"going":["go","가다 (be going to ~ = ~할 예정이다)"],
 "born":["bear","낳다 (be born = 태어나다)"],"slavery":["slavery","노예 제도, 노예 신분"],"early":["early","어린 시절의, 이른"],
 "spent":["spend","보내다"],"working":["work","일하다"],"cotton":["cotton","목화"],"farm":["farm","농장"],
 "although":["although","비록 ~이지만"],"became":["become","~이 되다"],"free":["free","자유로운"],"man":["man","남자"],
 "american":["American","미국의"],"civil":["civil","시민의 (Civil War = 남북전쟁)"],"war":["war","전쟁"],"still":["still","여전히"],
 "face":["face","직면하다"],"racial":["racial","인종의, 인종적인"],"discrimination":["discrimination","차별"],"low":["low","낮은"],
 "wages":["wage","임금"],"later":["later","이후에"],"around":["around","~쯤, 무렵"],"years":["year","해, 년"],"old":["old","나이가 ~인"],
 "moved":["move","이주하다, 옮기다"],"city":["city","도시"],"where":["where","그곳에서"],"found":["find","찾다, 얻다"],"job":["job","일자리"],
 "factory":["factory","공장"],"wasn't":["be","~이 아니었다 (It wasn't until ~ = ~하고서야 비로소)"],"until":["until","~까지"],
 "too":["too","너무 ~한 (too ~ to … = 너무 ~해서 …할 수 없다)"],"ill":["ill","아픈"],"turned":["turn","향하다 (turn to ~ = ~으로 눈을 돌리다)"],
 "drawing":["drawing","그림 그리기"],"express":["express","표현하다"],"experiences":["experience","경험"],"experience":["experience","경험"],
 "docent":["docent","도슨트(전시 안내자)"],"introduce":["introduce","소개하다"],"will":["will","~할 것이다"],"did":["do","하다 (did not = ~하지 않았다)"],
 "spite":["spite","(in spite of = ~에도 불구하고)"],"their":["their","그들의"],"abandon":["abandon","포기하다, 버리다"],
 "difficulties":["difficulty","어려움"],"difficulty":["difficulty","어려움"],"achievements":["achievement","성취"],
 "change":["change","바꾸다"],"hide":["hide","숨기다"],"honors":["honor","영예, 명예"],"greatly":["greatly","크게"],
 "has":["have","가지다"],"distinctive":["distinctive","독특한, 특유의"],"appreciated":["appreciate","높이 평가하다 (appreciated = 인정받는)"],
 "appreciate":["appreciate","높이 평가하다, 인정하다"],"ignored":["ignore","무시하다"],"ordinary":["ordinary","평범한"],
 "criticized":["criticize","비판하다"],"borrowed":["borrow","빌리다"],"forgotten":["forget","잊다 (forgotten = 잊힌)"],
 "slave":["slave","노예"],"prejudice":["prejudice","편견, 차별"],"kindness":["kindness","친절"],"citizen":["citizen","시민"],
 "painter":["painter","화가"],"equality":["equality","평등"],"continued":["continue","계속하다"],"suffer":["suffer","시달리다, 고통받다"],
 "becoming":["become","~이 되다"],"even":["even","~조차, ~한 후에도"],"after":["after","~한 후에"],"at":["at","~에서"],
 "relocated":["relocate","이사하다, 옮기다"],"relocate":["relocate","이사하다, 옮기다"],"convey":["convey","전달하다"],
 "returned":["return","돌아오다"],"escaped":["escape","탈출하다"],"forget":["forget","잊다"],"took":["take","얻다, 맡다"],
 "began":["begin","시작하다"],"drawn":["draw","그리다"],"singer":["singer","가수"],"voice":["voice","목소리"],
 "everyone":["everyone","모두"],"hard":["hard","열심히 하는, 힘든"],"story":["story","이야기, 사연"],"dreamed":["dream","꿈꾸다"],
 "freedom":["freedom","자유"],"fight":["fight","맞서 싸우다"],"others":["other","다른 사람들"],"against":["against","~에 맞서"],
 "family":["family","가족"],"decided":["decide","결정하다"],"music":["music","음악"],"feelings":["feeling","감정"],"without":["without","~ 없이"],
 "words":["word","말, 단어"],"smiled":["smile","미소 짓다"],"dream":["dream","꿈"],"must":["must","~해야 한다"],"about":["about","~에 관하여, 약"],
 "intro":["intro","소개"],"themselves":["themselves","그들 자신"],"usa":["USA","미국"],"u.s.":["U.S.","미국"],"montgomery":["Montgomery","몽고메리(미국 앨라배마주의 도시)"],
 "alabama":["Alabama","앨라배마(미국의 주)"],"isabel":["Isabel","Isabel(도슨트 이름)"],"williams":["Williams","Williams(성)"],
 "traylor":["Traylor","Traylor(첫 번째 예술가 Bill Traylor)"],"bill":["Bill","Bill(이름)"],"began":["begin","시작하다"],
 "whose":["whose","그 사람의"],"who":["who","~하는 (사람)"],"that":["that","~하는 (관계대명사)"],"when":["when","~할 때"],
 "which":["which","~하는 것"],"1853":["1853","1853년"],"70":["70","70"],"85":["85","85"],"2":["2","2"],
}

# 직독직해 조각: [영어 조각, 한글 조각]. [[ ]] 는 빈칸에 들어간 정답 단어 표시
JD={
 1:[["The docent will introduce three artists","도슨트는 세 명의 예술가를 소개할 것이다"],
    ["who did not [[abandon]] their art","자신의 예술을 [[포기하지]] 않은"],
    ["in spite of the [[difficulties]] in their lives.","삶 속의 [[어려움]]에도 불구하고."]],
 2:[["Each artist has","각 예술가에게는 있다"],
    ["a [[distinctive]] painting style and a story","[[독특한]] 화풍과 이야기가"],
    ["that has made their work greatly [[appreciated]].","작품이 크게 [[인정받게]] 만든."]],
 3:[["Traylor was born a [[slave]]","Traylor는 [[노예]]로 태어났고"],
    ["and, even after becoming free,","자유의 몸이 된 후에도,"],
    ["he continued to suffer from racial [[prejudice]] at work.","일터에서 계속 인종적 [[편견]]에 시달렸다."]],
 4:[["At about 70, Traylor [[relocated]] to a city","70세 무렵 Traylor는 도시로 [[이사했고]]"],
    ["and took a factory job,","공장에서 일자리를 얻었으며,"],
    ["and at 85, when he was too ill to work,","85세에 몸이 너무 아파 일을 할 수 없게 되자,"],
    ["he began drawing to [[convey]] his life experiences.","자신의 인생 경험을 [[전달하려고]] 그림을 그리기 시작했다."]],
}

# 기억할 흐름 카드뉴스
FC={
 1:[["본문 1~2번","도슨트 Isabel의 인사","전시회를 안내하는 사람이 먼저 자기소개를 해요."],
    ["본문 3번","오늘 만날 세 예술가","인생의 역경에도 예술을 포기하지 않은 사람들이에요."],
    ["정답 포인트","{{give up on|~을 포기하다}} = {{abandon|포기하다}}, {{challenges|역경}} = {{difficulties|어려움}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 4번","세 예술가 모두의 공통점","각자 독특한 화풍과 사연이 있어요."],
    ["결과","그 덕분에 작품이 높이 평가받는다","화풍과 사연이 작품의 가치를 높여 줘요."],
    ["정답 포인트","{{unique|독특한}} = {{distinctive|독특한}}, {{valued|높이 평가받는}} = {{appreciated|인정받는}}","품질 평가 쪽 이야기를 찾아요."]],
 3:[["본문 7번","노예로 태어난 Traylor","미국 앨라배마의 목화 농장에서 일했어요."],
    ["본문 8번","Although! 자유의 몸이 되어도","낮은 임금을 받으며 인종차별을 계속 겪었어요."],
    ["정답 포인트","{{slavery|노예 신분}} → {{slave|노예}}, {{discrimination|차별}} = {{prejudice|편견}}","품사가 바뀌어도 뜻은 같아요."]],
 4:[["본문 9번","70세 무렵 몽고메리로 이주","도시의 공장에서 일자리를 얻었어요."],
    ["본문 10번","85세, 몸이 아파 일을 그만둔 뒤에야","그때서야 그림으로 눈을 돌렸어요."],
    ["정답 포인트","{{moved|이주했다}} = {{relocated|이사했다}}, {{express|표현하다}} = {{convey|전달하다}}","그림은 자기 경험을 드러내려는 수단이에요."]],
}

# 바꿔 말하기 스토리: 본문 등장 순서
STORY=[
 dict(a="challenge",form="challenges",n=3,sq=1,sum="in spite of the [[difficulties]] in their lives",hook="포기하지 않은 세 예술가를 소개하는 문장의 challenges(역경) → 요약문에서는 difficulties(어려움)로 바꿨어요."),
 dict(a="unique",form="unique",n=4,sq=2,sum="a [[distinctive]] painting style",hook="각 예술가마다 다른 화풍을 말하는 문장의 unique(독특한) → 요약문에서는 distinctive(독특한, 특유의)로 바꿨어요."),
 dict(a="value",form="valued",n=4,sq=2,sum="their work greatly [[appreciated]]",hook="작품이 높이 평가받는다는 문장의 valued(높이 평가받는) → 요약문에서는 appreciated(인정받는)로 바꿨어요."),
 dict(a="slavery",form="slavery",n=7,sq=3,sum="Traylor was born a [[slave]]",hook="Traylor가 어떤 신분으로 태어났는지 나오는 문장의 slavery(노예 신분) → 요약문에서는 slave(노예)로 바꿨어요."),
 dict(a="discrimination",form="discrimination",n=8,sq=3,sum="racial [[prejudice]] at work",hook="자유의 몸이 되어도 겪은 어려움이 나오는 문장의 discrimination(차별) → 요약문에서는 prejudice(편견, 차별)로 바꿨어요."),
 dict(a="move",form="moved",n=9,sq=4,sum="Traylor [[relocated]] to a city",hook="70세 무렵 몽고메리로 옮겨 간 문장의 moved(이주했다) → 요약문에서는 relocated(이사했다)로 바꿨어요."),
 dict(a="express",form="express",n=10,sq=4,sum="he began drawing to [[convey]] his life experiences",hook="85세에 그림으로 눈을 돌린 이유가 나오는 문장의 express(표현하다) → 요약문에서는 convey(전달하다)로 바꿨어요."),
]

# 줄거리 장면
SCENES=[
 dict(tag="본문 1~3번",ns=[1,2,3],line="도슨트 Isabel이 인사하며, 인생의 [[challenges|역경]]에도 예술을 포기하지 않은 세 예술가를 소개한다."),
 dict(tag="본문 4번",ns=[4],line="각 예술가에게는 [[unique|독특한]] 화풍과, 작품이 높이 [[valued|평가받게]] 만든 이야기가 있다."),
 dict(tag="본문 6~7번",ns=[6,7],line="첫 번째 예술가 Bill Traylor는 [[slavery|노예]] 신분으로 태어나 목화 농장에서 일했다."),
 dict(tag="본문 8번",ns=[8],line="자유의 몸이 되었지만 낮은 임금을 받으며 인종 [[discrimination|차별]]을 겪었다."),
 dict(tag="본문 9번",ns=[9],line="70세 무렵 몽고메리시로 [[moved|이주해]] 공장에서 일했다."),
 dict(tag="본문 10번",ns=[10],line="85세, 몸이 아파 일을 못 하게 되자 인생 경험을 그림으로 [[express|표현했다]]."),
]

# 근거 본문 한글 해석에서 영어 형광펜과 같은 자리
HLKO={3:["결코 예술을 포기하지 않았던","인생의 역경"],4:["독특한 화풍","높이 평가받게"],7:["노예로 태어나"],8:["여전히 인종차별에 직면해야 했다"],
 9:["몽고메리시로 이주하여"],10:["몸이 너무 아파서 일을 할 수 없게 된","인생 경험을 표현하기 위해 그림으로 눈을 돌렸다"]}

UM={'abandon':('포기하다','포기하지'),'difficulty':('어려움','어려움'),'distinctive':('독특한, 특유의','독특한'),'appreciate':('높이 평가하다, 인정하다','높이 평가할'),'slave':('노예','노예'),'prejudice':('편견, 차별','편견'),'relocate':('이사하다, 옮기다','이사하기로'),'convey':('전달하다','전달할')}

TARGET={1:1,2:3,3:0,4:4}

G.update({"you're":["you are","너는 ~이다 (you're going to ~ = ~하게 될 것이다)"],"into":["into","~ 안으로 (born into slavery = 노예 신분으로 태어나)"]})
