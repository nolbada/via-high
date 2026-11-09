# -*- coding: utf-8 -*-
# 세트 정의: 주성고1 4과 ❺
META=dict(sch='jusung-go1', src='jusung-go1/L4/sx-data.js', pidx=4, lesson='4과', title='웹 접근성 (Web Accessibility)', label='❺', page='yoyak-lian-z5')
Q = [
 dict(
  id=1,
  summary="Website accessibility features are not (A) to people with disabilities, since they can make online experiences easier for (B), whatever their abilities or situations.",
  ko="웹 사이트의 접근성 특징들은 장애가 있는 사람들에게 <b>(A) 한정되지</b> 않으며, 능력이나 상황이 어떠하든 <b>(B) 모두</b>에게 온라인 경험을 더 용이하게 만들 수 있다.",
  opts=[["limited","everybody"],["limited","experts"],["useful","everybody"],["useful","nobody"],["open","beginners"]],
  optko=["한정된 – 모든 사람","한정된 – 전문가","유용한 – 모든 사람","유용한 – 아무도","열려 있는 – 초보자"],
  ans=0,
  wrong=[None,
         "experts(전문가)가 틀려요. 본문은 능력이나 상황과 상관없이 모든 사람(everyone)에게 쉬워진다고 해요.",
         "useful(유용한)이 틀려요. 'not useful to'가 되면 장애가 있는 사람들에게 도움이 안 된다는 뜻이 돼요. 본문은 그들'만' 돕는 게 아니라는 뜻이에요.",
         "둘 다 틀려요. useful(유용한)은 뜻이 어긋나고, nobody(아무도)는 본문과 정반대예요.",
         "둘 다 틀려요. open(열려 있는)도 beginners(초보자)도 본문에 나오지 않아요."],
  evid=[dict(n=1, hl=["people with disabilities"]), dict(n=2, hl=["make online experiences easier for everyone","regardless of abilities or situations"])],
  swaps=[["help","limit","돕다 → 한정하다 (not just help = not limited)"],["everyone","everybody","모든 사람 → 모든 사람"],["regardless of","whatever","~와 상관없이 → ~이든 상관없이"]],
  swapnote="'단지 ~만 돕는 게 아니다'는 'not limited to ~(~에 한정되지 않는다)'로 바뀌어 나와요. everyone(모든 사람)은 everybody(모든 사람)로도 써요.",
  use=[dict(w="limited",ex="The class is limited to twenty students.",ko="그 수업은 스무 명의 학생으로 한정된다."),
       dict(w="everybody",ex="Everybody in my class likes this song.",ko="우리 반의 모든 사람이 이 노래를 좋아한다.")],
  flow="본문 1번에서 접근성 특징은 장애가 있는 사람만 돕는 게 아니라고 말하고, 2번에서 능력이나 상황과 상관없이 모두에게 쉬워진다고 이어져요.",
 ),
 dict(
  id=2,
  summary="When websites are (A) to navigate and understand, everyone can (B) from a more inclusive online experience.",
  ko="웹 사이트가 탐색하고 이해하기에 <b>(A) 간단하면</b> 모든 사람이 더 차별 없는 온라인 경험으로부터 <b>(B) 이익을 얻을</b> 수 있다.",
  opts=[["simple","profit"],["simple","suffer"],["difficult","profit"],["difficult","suffer"],["simple","escape"]],
  optko=["간단한 – 이익을 얻다","간단한 – 고통받다","어려운 – 이익을 얻다","어려운 – 고통받다","간단한 – 벗어나다"],
  ans=0,
  wrong=[None,
         "suffer(고통받다)가 틀려요. 본문은 모두가 득을 본다(benefit)고 해요.",
         "difficult(어려운)가 틀려요. 사이트가 어려우면 득을 보기 힘들어요. 본문은 쉬울(easy) 때의 이야기예요.",
         "둘 다 틀려요. 어려운 사이트가 아니라 쉬운 사이트이고, 고통받는 게 아니라 득을 봐요.",
         "escape(벗어나다)가 틀려요. 본문은 더 포용적인 경험으로부터 득을 본다(benefit)고 해요."],
  evid=[dict(n=3, hl=["easy to navigate and understand","benefit from a more inclusive online experience"])],
  swaps=[["easy","simple","쉬운 → 간단한"],["benefit","profit","득을 보다 → 이익을 얻다"],["we","everyone","우리 → 모든 사람"]],
  swapnote="benefit(득을 보다)은 profit(이익을 얻다)이나 gain(얻다)으로 바뀌어 나와요. easy(쉬운)도 simple(간단한)로 자주 바뀌어요.",
  use=[dict(w="simple",ex="The rules of this game are simple.",ko="이 게임의 규칙은 간단하다."),
       dict(w="profit",ex="Many small shops profit from tourists.",ko="많은 작은 가게가 관광객 덕분에 이익을 얻는다.")],
  flow="본문 3번은 1~2번의 결론이에요. 웹 사이트가 탐색하고 이해하기 쉬우면 우리 모두가 더 차별 없는 온라인 경험으로 득을 본다고 마무리해요.",
 ),
 dict(
  id=3,
  summary="The (A) of reading and writing (B) from culture to culture: some people read from left to right, others from right to left, and others from top to bottom.",
  ko="읽고 쓰는 <b>(A) 방식</b>은 문화마다 <b>(B) 다르다</b>. 어떤 사람들은 왼쪽에서 오른쪽으로, 다른 사람들은 오른쪽에서 왼쪽으로, 또 다른 사람들은 위에서 아래로 읽는다.",
  opts=[["methods","vary"],["methods","stay"],["results","vary"],["results","stay"],["tools","stay"]],
  optko=["방식 – 다르다","방식 – 그대로이다","결과 – 다르다","결과 – 그대로이다","도구 – 그대로이다"],
  ans=0,
  wrong=[None,
         "stay(그대로이다)가 틀려요. 본문은 문화마다 다르다(different)고 해요.",
         "results(결과)가 틀려요. 결과 이야기는 본문에 없고, 읽고 쓰는 체계(방식)가 다르다는 이야기예요.",
         "둘 다 틀려요. 결과 이야기도 없고, 문화마다 그대로라는 말은 본문과 반대예요.",
         "둘 다 틀려요. 도구 이야기는 본문에 없고, 문화마다 그대로라는 말은 본문과 반대예요."],
  evid=[dict(n=4, hl=["Reading and writing systems are different across cultures"]), dict(n=5, hl=["from left to right","from right to left"]), dict(n=6, hl=["from top to bottom"])],
  swaps=[["system","method","체계 → 방식"],["different","vary","다른 → 다르다, 달라지다"],["across cultures","from culture to culture","문화마다 → 문화에 따라"]],
  swapnote="'A is different'는 'A varies(A는 달라진다)'로 바뀌어 나와요. 형용사가 동사로 변해도 뜻은 같아요.",
  use=[dict(w="method",ex="This teacher uses a new method to teach English.",ko="이 선생님은 영어를 가르치는 새로운 방식을 쓴다."),
       dict(w="vary",ex="Prices vary from store to store.",ko="가격은 가게마다 다르다.")],
  flow="본문 4번이 이 단락의 주제문이에요. 읽고 쓰는 체계는 문화마다 다르다고 말하고, 5~6번에서 방향 세 가지를 예로 들어요.",
 ),
 dict(
  id=4,
  summary="Some global websites (A) these differences and (B) their sites for people in different regions, so the same site looks different in another language setting.",
  ko="몇몇 세계적인 웹 사이트는 이러한 차이를 <b>(A) 고려하고</b> 다른 지역의 사람들을 위해 사이트를 <b>(B) 맞추기</b> 때문에, 같은 사이트도 다른 언어 설정에서는 다르게 보인다.",
  opts=[["consider","adapt"],["consider","hide"],["ignore","adapt"],["ignore","hide"],["avoid","delete"]],
  optko=["고려하다 – 맞추다","고려하다 – 숨기다","무시하다 – 맞추다","무시하다 – 숨기다","피하다 – 지우다"],
  ans=0,
  wrong=[None,
         "hide(숨기다)가 틀려요. 사이트를 숨기는 게 아니라 지역 사람들에게 맞게 조정(adjust)해요.",
         "ignore(무시하다)가 틀려요. 차이를 무시하는 게 아니라 고려해요(take into consideration).",
         "둘 다 틀려요. 차이를 무시하지도, 사이트를 숨기지도 않아요.",
         "둘 다 틀려요. 차이를 피하거나 사이트를 지운다는 말은 본문에 없어요."],
  evid=[dict(n=7, hl=["take these differences into consideration","adjust their websites for people in different regions"]), dict(n=9, hl=["in a different language setting","see a different format"])],
  swaps=[["consideration","consider","고려 → 고려하다"],["adjust","adapt","조정하다 → 맞추다"],["see a different format","looks different","다른 구성 방식을 보다 → 다르게 보이다"]],
  swapnote="'take A into consideration(A를 고려하다)'은 한 단어 consider(고려하다)로 줄여 나와요. adjust(조정하다)는 adapt(맞추다)로 바뀌어요.",
  use=[dict(w="consider",ex="Please consider the weather before you go out.",ko="나가기 전에 날씨를 고려해 주세요."),
       dict(w="adapt",ex="She adapted the story for young children.",ko="그녀는 어린아이들을 위해 이야기를 각색했다.")],
  flow="본문 7번에서 세계적인 웹 사이트가 문화 차이를 고려해 지역별로 조정한다고 하고, 8번 예시(검색 버튼·로고 위치)를 지나 9번에서 언어 설정에 따라 구성이 달라진다고 마무리해요.",
 ),
]

# 단어 사전: 표면형(소문자) -> [기본형, 이 글에서의 뜻]
G = {
 "website":["website","웹 사이트"],"websites":["website","웹 사이트"],"site":["site","(웹) 사이트"],"sites":["site","(웹) 사이트"],
 "accessibility":["accessibility","접근성"],"features":["feature","특징, 기능"],"feature":["feature","특징, 기능"],
 "are":["be","~이다"],"not":["not","~않다"],"to":["to","~에게, ~하기 위해"],"people":["people","사람들"],
 "disabilities":["disability","장애"],"since":["since","~이기 때문에"],"they":["they","그것들"],"can":["can","~할 수 있다"],
 "make":["make","만들다"],"online":["online","온라인의"],"experiences":["experience","경험"],"experience":["experience","경험"],
 "easier":["easy","더 쉬운"],"easy":["easy","쉬운"],"whatever":["whatever","~이든 상관없이"],"their":["their","그들의"],
 "abilities":["ability","능력"],"or":["or","또는"],"situations":["situation","상황"],"regardless":["regardless of","~와 상관없이"],
 "help":["help","돕다"],"just":["just","단지"],"don’t":["do not","~않는다"],"everyone":["everyone","모든 사람"],"everybody":["everybody","모든 사람"],
 "limited":["limit","한정하다 (limited to ~ = ~에 한정된)"],"experts":["expert","전문가"],"useful":["useful","유용한"],
 "nobody":["nobody","아무도 ~않다"],"open":["open","열려 있는"],"beginners":["beginner","초보자"],
 "when":["when","~할 때"],"navigate":["navigate","(사이트를) 탐색하다, 찾아다니다"],"understand":["understand","이해하다"],
 "we":["we","우리"],"all":["all","모두"],"benefit":["benefit","득을 보다, 이익"],"from":["from","~로부터"],
 "more":["more","더"],"inclusive":["inclusive","모두를 포함하는, 차별 없는"],"simple":["simple","간단한"],
 "profit":["profit","이익을 얻다"],"suffer":["suffer","고통받다"],"difficult":["difficult","어려운"],"escape":["escape","벗어나다"],
 "reading":["read","읽다 (reading = 읽기)"],"writing":["write","쓰다 (writing = 쓰기)"],"write":["write","쓰다"],"read":["read","읽다"],
 "systems":["system","체계"],"system":["system","체계"],"different":["different","다른"],"across":["across","~ 전체에 걸쳐, ~마다"],
 "cultures":["culture","문화"],"culture":["culture","문화"],"western":["Western","서양의"],"left":["left","왼쪽"],"right":["right","오른쪽"],
 "while":["while","~인 반면"],"those":["those","그 사람들"],"some":["some","일부, 몇몇"],"middle":["middle","중간의"],
 "eastern":["Eastern","동양의"],"like":["like","~와 같은"],"that":["that","그것"],"japan":["Japan","일본"],
 "top":["top","위"],"bottom":["bottom","아래"],"others":["other","다른 사람들"],"methods":["method","방식"],"method":["method","방식"],
 "vary":["vary","다르다, 달라지다"],"stay":["stay","그대로이다, 머물다"],"results":["result","결과"],"tools":["tool","도구"],
 "global":["global","세계적인"],"these":["this","이"],"differences":["difference","차이"],"take":["take","취하다 (take into consideration = 고려하다)"],
 "consideration":["consideration","고려"],"adjust":["adjust","조정하다"],"regions":["region","지역"],"countries":["country","나라"],
 "country":["country","나라"],"text":["text","글, 문자"],"button":["button","버튼"],"search":["search","검색"],"logo":["logo","로고"],
 "visit":["visit","방문하다"],"same":["same","같은"],"language":["language","언어"],"setting":["setting","설정"],
 "format":["format","구성 방식, 형식"],"will":["will","~할 것이다"],"see":["see","보다"],"if":["if","만약 ~라면"],
 "where":["where","~하는 곳"],"consider":["consider","고려하다"],"adapt":["adapt","맞추다, 적응시키다"],"hide":["hide","숨기다"],
 "ignore":["ignore","무시하다"],"avoid":["avoid","피하다"],"delete":["delete","지우다"],"looks":["look","~처럼 보이다"],
 "another":["another","다른"],"so":["so","그래서"],"for":["for","~을 위해"],"in":["in","~에서"],"of":["of","~의"],
 "and":["and","그리고"],"with":["with","~와 함께, ~이 있는"],"than":["than","~보다"],"understood":["understand","이해하다"],
 "easily":["easily","쉽게"],"differ":["differ","다르다"],"adjusted":["adjust","조정하다"],"adapted":["adapt","맞추다"],
 "have":["have","가지다"],"is":["be","~이다"],"on":["on","~에"],"read":["read","읽다"],"web":["web","웹"],
 "move":["move","움직이다"],"place":["place","장소"],
 "class":["class","수업"],"twenty":["twenty","스무 명(20)"],"students":["student","학생"],"song":["song","노래"],"rules":["rule","규칙"],
 "game":["game","게임"],"shops":["shop","가게"],"small":["small","작은"],"many":["many","많은"],"tourists":["tourist","관광객"],
 "prices":["price","가격"],"store":["store","가게"],"teacher":["teacher","선생님"],"uses":["use","쓰다"],"new":["new","새로운"],
 "teach":["teach","가르치다"],"english":["English","영어"],"please":["please","제발, ~해 주세요"],"weather":["weather","날씨"],
 "before":["before","~하기 전에"],"go":["go","가다"],"out":["out","밖으로"],"story":["story","이야기"],"young":["young","어린"],
 "children":["child","아이들"],"she":["she","그녀"],"my":["my","나의"],"this":["this","이"],"will":["will","~할 것이다"],
 "different":["different","다른"],"differences":["difference","차이"],"likes":["like","좋아하다"],"the":["the","그"],
}

# 직독직해 조각: [영어 조각, 한글 조각]
JD={
 1:[["Website accessibility features are not [[limited]] to people with disabilities,","웹 사이트의 접근성 특징들은 장애가 있는 사람들에게 [[한정되지]] 않는다,"],
    ["since they can make online experiences easier for [[everybody]],","그것들은 [[모두]]에게 온라인 경험을 더 용이하게 만들 수 있기 때문에,"],
    ["whatever their abilities or situations.","그들의 능력이나 상황이 어떠하든."]],
 2:[["When websites are [[simple]] to navigate and understand,","웹 사이트가 탐색하고 이해하기에 [[간단할]] 때,"],
    ["everyone can [[profit]]","모든 사람이 [[이익을 얻을]] 수 있다"],
    ["from a more inclusive online experience.","더 차별 없는 온라인 경험으로부터."]],
 3:[["The [[methods]] of reading and writing","읽고 쓰는 [[방식]]은"],
    ["[[vary]] from culture to culture:","문화마다 [[다르다]]:"],
    ["some people read from left to right,","어떤 사람들은 왼쪽에서 오른쪽으로 읽고,"],
    ["others from right to left,","다른 사람들은 오른쪽에서 왼쪽으로,"],
    ["and others from top to bottom.","또 다른 사람들은 위에서 아래로 읽는다."]],
 4:[["Some global websites [[consider]] these differences","몇몇 세계적인 웹 사이트는 이러한 차이를 [[고려하고]]"],
    ["and [[adapt]] their sites","그들의 사이트를 [[맞추어서]]"],
    ["for people in different regions,","다른 지역의 사람들을 위해,"],
    ["so the same site looks different","같은 사이트가 다르게 보인다"],
    ["in another language setting.","다른 언어 설정에서는."]],
}

# 기억할 흐름 카드뉴스
FC={
 1:[["본문 1번","접근성은 장애인만을 위한 게 아니다","웹 사이트의 접근성 특징은 {{people with disabilities|장애가 있는 사람들}}만 돕는 게 아니에요."],
    ["본문 2번","능력이나 상황과 상관없이 모두에게","온라인 경험이 더 쉬워져요."],
    ["정답 포인트","{{not just help|돕기만 하는 게 아니다}} = {{not limited|한정되지 않는다}}, {{everyone|모든 사람}} = {{everybody|모든 사람}}","본문 표현이 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 3번","웹 사이트가 쉬우면 모두가 득을 본다","탐색하고 이해하기 쉬운 사이트예요."],
    ["결과","더 차별 없는 온라인 경험","{{inclusive|모두를 포함하는}} 경험이에요."],
    ["정답 포인트","{{easy|쉬운}} = {{simple|간단한}}, {{benefit|득을 보다}} = {{profit|이익을 얻다}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 3:[["본문 4번","읽고 쓰는 체계는 문화마다 다르다","이 단락의 주제문이에요."],
    ["본문 5~6번","읽는 방향 세 가지","왼쪽에서 오른쪽(서양), 오른쪽에서 왼쪽(중동), 위에서 아래(일본 등)예요."],
    ["정답 포인트","{{system|체계}} = {{method|방식}}, {{are different|다르다}} = {{vary|다르다}}","형용사가 동사로 바뀌어도 뜻은 같아요."]],
 4:[["본문 7번","세계적인 사이트는 차이를 고려한다","지역 사람들에게 맞게 사이트를 조정해요."],
    ["본문 8~9번","그래서 모습이 달라진다","검색 버튼과 로고 자리가 바뀌고, 언어 설정에 따라 구성이 달라져요."],
    ["정답 포인트","{{take into consideration|고려하다}} = {{consider|고려하다}}, {{adjust|조정하다}} = {{adapt|맞추다}}","표현이 한 단어로 줄어 나와요."]],
}

# 바꿔 말하기 스토리
STORY=[
 dict(a="everyone",form="everyone",n=2,sq=1,sum="easier for [[everybody]]",hook="능력이나 상황과 상관없이 '모두에게' 쉬워진다는 문장의 everyone(모든 사람) → 요약문에서는 everybody(모든 사람)로 바꿨어요."),
 dict(a="easy",form="easy",n=3,sq=2,sum="When websites are [[simple]] to navigate and understand",hook="탐색하고 이해하기 '쉬운' 사이트라는 문장의 easy(쉬운) → 요약문에서는 simple(간단한)로 바꿨어요."),
 dict(a="benefit",form="benefit",n=3,sq=2,sum="everyone can [[profit]] from a more inclusive online experience",hook="모두가 차별 없는 경험으로 '득을 본다'는 문장의 benefit(득을 보다) → 요약문에서는 profit(이익을 얻다)으로 바꿨어요."),
 dict(a="system",form="systems",n=4,sq=3,sum="The [[methods]] of reading and writing",hook="읽고 쓰는 체계가 문화마다 다르다는 주제문의 systems(체계) → 요약문에서는 methods(방식)로 바꿨어요."),
 dict(a="different",form="different",n=4,sq=3,sum="[[vary]] from culture to culture",hook="문화마다 '다르다'는 말의 different(다른) → 요약문에서는 vary(다르다, 달라지다)로 바꿨어요."),
 dict(a="consideration",form="consideration",n=7,sq=4,sum="Some global websites [[consider]] these differences",hook="세계적인 사이트가 차이를 '고려한다'는 문장의 consideration(고려) → 요약문에서는 consider(고려하다)로 바꿨어요."),
 dict(a="adjust",form="adjust",n=7,sq=4,sum="and [[adapt]] their sites",hook="지역 사람들에게 맞게 사이트를 '조정한다'는 문장의 adjust(조정하다) → 요약문에서는 adapt(맞추다)로 바꿨어요."),
]

# 줄거리 장면
SCENES=[
 dict(tag="본문 2번",ns=[2],line="접근성 특징은 능력이나 상황과 상관없이 [[everyone|모든 사람]]의 온라인 경험을 쉽게 해 준다."),
 dict(tag="본문 3번",ns=[3],line="사이트가 탐색하기 [[easy|쉬우면]] 우리 모두가 차별 없는 경험으로 [[benefit|득을 본다]]."),
 dict(tag="본문 4번",ns=[4],line="읽고 쓰는 [[systems|체계]]는 문화마다 [[different|다르다]]: 왼쪽에서 오른쪽, 오른쪽에서 왼쪽, 위에서 아래."),
 dict(tag="본문 7번",ns=[7],line="세계적인 웹 사이트는 이 차이를 [[consideration|고려해서]] 지역마다 사이트를 [[adjust|조정한다]]."),
]

# 근거 본문 한글 해석에서 영어 형광펜과 같은 자리
HLKO={1:["장애가 있는 사람들"],2:["모두에게 온라인 경험을 더 용이하게 만들어 줄 수 있다","능력이나 상황과 상관없이"],
 3:["탐색하고 이해하기에 더 쉬울 때","더 차별 없는 온라인 경험으로부터 득을 볼 수 있다"],
 4:["읽기와 쓰기 체계는 문화마다 다르다"],5:["왼쪽에서 오른쪽으로","오른쪽에서 왼쪽으로"],6:["위에서 아래로"],
 7:["이러한 차이를 고려하고","다른 지역의 사람들을 위해 그들의 웹 사이트를 조정한다"],
 9:["다른 언어 설정으로","다른 구성 방식을 보게 될 것이다"]}

UM={'limited':('한정된','한정된다'),'everybody':('모든 사람','모든 사람'),'simple':('간단한','간단하다'),'profit':('이익을 얻다','이익을 얻는다'),
 'method':('방식','방식'),'vary':('다르다, 달라지다','다르다'),'consider':('고려하다','고려해'),'adapt':('맞추다, 각색하다','각색했다')}

G.update({'into':['into','~ 안으로 (take into consideration = 고려하다)'],'disability':['disability','장애'],'ability':['ability','능력'],'situation':['situation','상황'],'expert':['expert','전문가']})

TARGET={1:2,2:4,3:0,4:3}
