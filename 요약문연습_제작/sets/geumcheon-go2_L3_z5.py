# -*- coding: utf-8 -*-
# 세트 정의: 금천고2 3과 ❺
META=dict(sch='geumcheon-go2', src='geumcheon-go2/L3/sx-data.js', pidx=4, lesson='3과', title='투표하는 방법에는 여러 가지가 있다', label='❺', page='yoyak-lian-z5')
Q = [
 dict(
  id=1,
  summary="The council members (A) the votes using the AV method and soon realized that the (B) would be different.",
  ko="자치회 구성원들은 AV 방식을 사용하여 표를 <b>(A) 검토했고</b>, 곧 <b>(B) 결과</b>가 달라질 것이라는 것을 깨달았다.",
  opts=[["inspected","outcome"],["inspected","budget"],["ignored","outcome"],["ignored","budget"],["approved","reason"]],
  optko=["검토하다 – 결과","검토하다 – 예산","무시하다 – 결과","무시하다 – 예산","승인하다 – 이유"],
  ans=0,
  wrong=[None,
         "budget(예산)이 틀려요. 달라질 것은 돈이 아니라 투표 결과(result)예요.",
         "ignored(무시하다)가 틀려요. 자치회는 표를 무시한 게 아니라 꼼꼼히 살펴봤어요(examined).",
         "둘 다 틀려요. 표를 무시하지도 않았고, 예산 이야기도 나오지 않아요.",
         "둘 다 틀려요. 표를 승인한(approved) 게 아니라 살펴봤고, 달라진 것은 이유가 아니라 결과예요."],
  evid=[dict(n=1, hl=["examined the votes","a different result"])],
  swaps=[["examine","inspect","살펴보다 → 면밀히 조사하다"],["result","outcome","결과 → 결과"],["realized","noticed","깨달았다 → 알아차렸다"]],
  swapnote="examine(살펴보다)은 inspect(조사하다)나 review(검토하다)로, result(결과)는 outcome(결과)으로 바뀌어 나와요. 같은 뜻의 다른 단어를 찾으세요.",
  use=[dict(w="inspect",ex="The teacher inspected every test paper carefully.",ko="선생님은 모든 시험지를 꼼꼼히 살펴보았다."),
       dict(w="outcome",ex="The outcome of the game surprised everyone.",ko="경기의 결과는 모두를 놀라게 했다.")],
  flow="본문 1번은 새 장면의 시작이에요. Next(다음으로) 자치회가 AV 방식으로 표를 다시 살펴보니, 이전과 다른 결과가 나올 것임을 곧 알아차려요.",
 ),
 dict(
  id=2,
  summary="The AV method can have more than one (A) of counting, and because the charity concert did not get a (B) of the first-preference votes, a second round was needed.",
  ko="AV 방식은 집계가 한 차례 이상의 <b>(A) 단계</b>를 가질 수 있고, 자선 콘서트가 1지망 표의 <b>(B) 과반수</b>를 얻지 못했기 때문에 2차 집계가 필요했다.",
  opts=[["stage","majority"],["stage","quarter"],["test","majority"],["test","minority"],["stage","minority"]],
  optko=["단계 – 과반수","단계 – 4분의 1","시험 – 과반수","시험 – 소수","단계 – 소수"],
  ans=0,
  wrong=[None,
         "quarter(4분의 1)가 틀려요. 1차에서 이기려면 절반이 넘는(50% 이상) 표가 필요해요.",
         "test(시험)가 틀려요. 본문은 집계를 여러 차례(round) 할 수 있다고 해요.",
         "둘 다 틀려요. 집계는 시험이 아니고, 이기려면 소수(minority)가 아니라 과반수가 필요해요.",
         "minority(소수)가 틀려요. 1차에서 이기려면 절반이 넘는 표가 필요하고, 콘서트는 40%뿐이었어요."],
  evid=[dict(n=2, hl=["more than one round of counting"]), dict(n=3, hl=["more than 50%"]), dict(n=4, hl=["only received 40%","a second round of counting was required"])],
  swaps=[["round","stage","차례, 회 → 단계"],["more than 50%","a majority","50% 초과 → 과반수"],["required","needed","요구되다 → 필요하다"]],
  swapnote="round(회, 차례)는 stage(단계)로, '50%가 넘는 표'는 majority(과반수)로 바뀌어 나와요. 숫자가 말로 바뀌는 것도 바꿔 말하기예요.",
  use=[dict(w="stage",ex="The project has three stages.",ko="그 프로젝트는 세 단계로 이루어져 있다."),
       dict(w="majority",ex="The majority of students chose the park.",ko="대다수의 학생들이 공원을 선택했다.")],
  flow="본문 2번은 집계가 여러 번 있을 수 있다는 규칙, 3번은 1차에서 이기려면 1지망 표가 50%를 넘어야 한다는 규칙, 4번은 콘서트가 40%뿐이라 2차로 간다는 적용이에요.",
 ),
 dict(
  id=3,
  summary="Option A, the art show, had the fewest first-preference votes, so it was (A), and its votes were (B) according to second choices, which made the bake sale the winner.",
  ko="미술 전시회인 선택지 A는 가장 적은 1지망 표를 얻어 <b>(A) 제외되었고</b>, 그 표들은 두 번째 선택에 따라 <b>(B) 재분배되어</b> 빵 바자회가 승자가 되었다.",
  opts=[["excluded","discarded"],["excluded","multiplied"],["promoted","reallocated"],["excluded","reallocated"],["promoted","discarded"]],
  optko=["제외하다 – 버리다","제외하다 – 곱하다","승격시키다 – 재분배하다","제외하다 – 재분배하다","승격시키다 – 버리다"],
  ans=3,
  wrong=[
         "discarded(버리다)가 틀려요. 5표는 버려진 게 아니라 두 번째 선호에 따라 다른 선택지로 옮겨졌어요(redistributed).",
         "multiplied(곱하다)가 틀려요. 표가 곱해져 늘어난 게 아니라 다른 선택지로 나뉘어 더해졌어요.",
         "promoted(승격시키다)가 틀려요. 가장 적은 표를 받은 A는 올라간 게 아니라 탈락(eliminated)했어요.",
         None,
         "둘 다 틀려요. A는 올라간 게 아니라 탈락했고, 표도 버려지지 않고 재분배됐어요."],
  evid=[dict(n=5, hl=["the fewest first-preference votes"]), dict(n=6, hl=["option A was eliminated","redistributed based on their second preferences"]), dict(n=9, hl=["the bake sale would be the winner"])],
  swaps=[["eliminated","excluded","탈락시키다 → 제외하다"],["redistributed","reallocated","다시 나누다 → 다시 배정하다"],["based","according","~에 기반하여 → ~에 따라"],["preferences","choices","선호 → 선택"]],
  swapnote="eliminate(탈락시키다)는 exclude(제외하다)로, redistribute(재분배하다)는 reallocate(다시 배정하다)로 바뀌어 나와요. re-가 붙은 말은 '다시'라는 느낌으로 기억하세요.",
  use=[dict(w="exclude",ex="They excluded the late students from the list.",ko="그들은 늦은 학생들을 명단에서 제외했다."),
       dict(w="reallocate",ex="The school reallocated money to the library.",ko="학교는 도서관에 돈을 다시 배정했다.")],
  flow="본문 5번에서 미술 전시회 A가 1지망 표 꼴찌, 6번에서 A가 탈락하고 그 표가 2지망대로 다른 곳에 나뉘고, 7~9번에서 빵 바자회가 11대 9로 앞서 승자가 돼요.",
 ),
 dict(
  id=4,
  summary="The AV method is not (A) because it can sometimes give second-preference votes more (B) than first-preference votes.",
  ko="AV 방식은 때때로 2지망 표에 1지망 표보다 더 큰 <b>(B) 영향력</b>을 주기도 하므로 <b>(A) 완벽하지</b> 않다.",
  opts=[["simple","delay"],["flawless","impact"],["flawless","delay"],["simple","impact"],["expensive","benefit"]],
  optko=["단순한 – 지연","완벽한 – 영향력","완벽한 – 지연","단순한 – 영향력","비싼 – 이익"],
  ans=1,
  wrong=["둘 다 틀려요. 본문은 AV 방식이 단순한지 이야기하지 않고, 지연(delay) 이야기도 없어요.",
         None,
         "delay(지연)가 틀려요. 문제는 시간이 늦어지는 게 아니라 2지망 표의 영향력이 커진다는 거예요.",
         "simple(단순한)이 틀려요. 본문은 AV 방식이 완벽하지 않다(not perfect)고 해요.",
         "둘 다 틀려요. 비용이나 이익 이야기는 본문에 나오지 않아요."],
  evid=[dict(n=10, hl=["not perfect"]), dict(n=11, hl=["a greater influence than first-preference votes"]), dict(n=12, hl=["mainly due to the second-preference votes it received"])],
  swaps=[["perfect","flawless","완벽한 → 흠 없는"],["influence","impact","영향력 → 영향"],["greater","more","더 큰 → 더 많은"],["allows","give","허용하다 → 주다"]],
  swapnote="perfect(완벽한)는 flawless(흠 없는)로, influence(영향력)는 impact(영향)로 바뀌어 나와요. 처음 보는 단어여도 앞뒤 뜻으로 짐작해 보세요.",
  use=[dict(w="flawless",ex="Her speech was almost flawless.",ko="그녀의 연설은 거의 흠잡을 데 없었다."),
       dict(w="impact",ex="Social media has a big impact on teenagers.",ko="소셜 미디어는 십대에게 큰 영향을 미친다.")],
  flow="본문 10번은 Unfortunately(안타깝게도)로 시작하는 반전이에요. AV도 완벽하지 않아서, 11번처럼 2지망 표가 1지망 표보다 영향력이 클 때가 있고, 12번에서 빵 바자회가 그 예예요.",
 ),
]

# 단어 사전: 표면형(소문자) -> [기본형, 이 글에서의 뜻]
G = {
 "council":["council","(학생) 자치회, 위원회"],"members":["member","구성원, 회원"],"votes":["vote","표, 투표"],"vote":["vote","표, 투표"],
 "voting":["vote","투표하다"],"inspected":["inspect","면밀히 조사하다, 검토하다"],"inspect":["inspect","면밀히 조사하다, 검토하다"],
 "examined":["examine","살펴보다, 검토하다"],"examine":["examine","살펴보다, 검토하다"],"method":["method","방식, 방법"],
 "soon":["soon","곧"],"realized":["realize","깨닫다"],"result":["result","결과"],"outcome":["outcome","결과"],
 "budget":["budget","예산"],"ignored":["ignore","무시하다"],"approved":["approve","승인하다"],"reason":["reason","이유"],
 "different":["different","다른"],"potentially":["potentially","잠재적으로, 경우에 따라"],"include":["include","포함하다"],
 "round":["round","(경기·집계의) 회, 차례"],"rounds":["round","(경기·집계의) 회, 차례"],"counting":["counting","집계, 표 세기"],
 "stage":["stage","단계"],"stages":["stage","단계"],"majority":["majority","과반수, 대다수"],"minority":["minority","소수"],
 "quarter":["quarter","4분의 1"],"test":["test","시험"],"charity":["charity","자선"],"concert":["concert","콘서트"],
 "first-preference":["first-preference","1지망의 (가장 선호하는)"],"second-preference":["second-preference","2지망의 (두 번째로 선호하는)"],
 "preferences":["preference","선호(도)"],"choices":["choice","선택"],"needed":["need","필요하다"],"required":["require","요구하다, 필요로 하다"],
 "option":["option","선택지"],"win":["win","이기다"],"won":["win","이기다"],"winner":["winner","승자"],"received":["receive","받다"],
 "receive":["receive","받다"],"total":["total","전체의, 합계"],"fewest":["few","가장 적은 (few의 최상급)"],"art":["art","미술"],
 "show":["show","전시회, 쇼"],"eliminated":["eliminate","탈락시키다, 제거하다"],"excluded":["exclude","제외하다"],"exclude":["exclude","제외하다"],
 "promoted":["promote","승격시키다, 올리다"],"redistributed":["redistribute","다시 나누다, 재분배하다"],
 "reallocated":["reallocate","다시 배정하다, 재분배하다"],"reallocate":["reallocate","다시 배정하다, 재분배하다"],
 "discarded":["discard","버리다"],"multiplied":["multiply","곱하다, 늘리다"],"based":["base","~에 기반을 두다 (based on ~ = ~에 기반하여)"],
 "according":["according to","~에 따라"],"added":["add","더하다, 추가하다"],"meant":["mean","의미하다"],"bake":["bake","(빵을) 굽다"],
 "sale":["sale","판매, 바자회"],"perfect":["perfect","완벽한"],"flawless":["flawless","흠 없는, 완벽한"],"simple":["simple","단순한"],
 "expensive":["expensive","비싼"],"benefit":["benefit","이익, 혜택"],"delay":["delay","지연"],"impact":["impact","영향(력)"],
 "influence":["influence","영향(력)"],"greater":["great","더 큰"],"allows":["allow","허용하다, ~하게 하다"],"sometimes":["sometimes","때때로"],
 "mainly":["mainly","주로"],"due":["due to","~ 때문에"],"case":["case","경우"],"unfortunately":["unfortunately","안타깝게도"],
 "give":["give","주다"],"using":["use","사용하다"],"counted":["count","(수를) 세다"],"next":["next","다음으로"],
 "teacher":["teacher","선생님"],"paper":["paper","종이, 시험지"],"carefully":["carefully","꼼꼼히"],"every":["every","모든"],
 "project":["project","프로젝트, 과제"],"three":["three","셋"],"students":["student","학생"],"chose":["choose","선택하다"],
 "park":["park","공원"],"late":["late","늦은"],"list":["list","명단"],"school":["school","학교"],"money":["money","돈"],
 "library":["library","도서관"],"speech":["speech","연설"],"almost":["almost","거의"],"social":["social","사회적인"],
 "media":["media","매체"],"teenagers":["teenager","십대"],"game":["game","경기"],"surprised":["surprise","놀라게 하다"],
 "everyone":["everyone","모든 사람"],"fight":["fight","싸우다"],"unnecessary":["unnecessary","불필요한"],
 "reviewed":["review","검토하다"],"noticed":["notice","알아차리다"],"realize":["realize","깨닫다"],
}

# 직독직해 조각: [영어 조각, 한글 조각]. [[ ]] 는 빈칸에 들어간 정답 단어 표시
JD={
 1:[["The council members [[inspected]] the votes using the AV method","자치회 구성원들은 AV 방식으로 표를 [[검토했고]]"],
    ["and soon realized","곧 깨달았다"],
    ["that the [[outcome]] would be different.","[[결과]]가 달라질 것이라는 것을."]],
 2:[["The AV method can have more than one [[stage]] of counting,","AV 방식은 집계가 한 차례 이상의 [[단계]]를 가질 수 있고,"],
    ["and because the charity concert did not get a [[majority]]","자선 콘서트가 [[과반수]]를 얻지 못했기 때문에"],
    ["of the first-preference votes,","1지망 표의,"],
    ["a second round was needed.","2차 집계가 필요했다."]],
 3:[["Option A, the art show, had the fewest first-preference votes,","미술 전시회인 선택지 A는 가장 적은 1지망 표를 얻어,"],
    ["so it was [[excluded]],","[[제외되었고]],"],
    ["and its votes were [[reallocated]]","그 표들은 [[재분배되었다]]"],
    ["according to second choices,","두 번째 선택에 따라,"],
    ["which made the bake sale the winner.","이는 빵 바자회를 승자로 만들었다."]],
 4:[["The AV method is not [[flawless]]","AV 방식은 [[완벽하지]] 않다"],
    ["because it can sometimes give second-preference votes","그것이 때때로 2지망 표에게 줄 수 있기 때문이다"],
    ["more [[impact]] than first-preference votes.","1지망 표보다 더 큰 [[영향력]]을."]],
}

# 기억할 흐름 카드뉴스: [본문 번호 태그, 한 줄 큰 문장, 작은 보충, (마지막이면 강조)]
FC={
 1:[["본문 1번","자치회가 AV 방식으로 표를 다시 본다","Next(다음으로), 새로운 방식으로 투표를 살펴봐요."],
    ["그 결과","곧 결과가 달라질 것을 알아챈다","{{realize|깨닫다}}: 이전과 다른 결과가 나온다는 걸 알아차려요."],
    ["정답 포인트","{{examine|살펴보다}} = {{inspect|면밀히 조사하다}}, {{result|결과}} = {{outcome|결과}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 2번","집계는 여러 번 할 수 있다","AV 방식은 한 번으로 안 끝날 수 있어요."],
    ["본문 3~4번","1차에서 이기려면 50%가 넘어야 한다","콘서트는 40%뿐이라 2차로 넘어가요."],
    ["정답 포인트","{{round|회, 차례}} = {{stage|단계}}, 50% 초과 = {{majority|과반수}}","숫자가 말로 바뀌어 나와요."]],
 3:[["본문 5번","미술 전시회 A가 1지망 표 꼴찌","겨우 5명만 투표했어요."],
    ["본문 6번","A는 탈락, 그 표는 2지망대로 다시 나뉜다","{{eliminate|탈락시키다}} → {{redistribute|다시 나누다}}"],
    ["본문 7~9번","빵 바자회가 11대 9로 승자","나뉜 표가 더해져 순서가 바뀌었어요."],
    ["정답 포인트","{{eliminated|탈락시켰다}} = {{excluded|제외했다}}, {{redistributed|다시 나눴다}} = {{reallocated|다시 배정했다}}","re-는 '다시'라는 신호예요."]],
 4:[["본문 10번","But! AV 방식도 완벽하지는 않다","Unfortunately(안타깝게도)가 반전 신호예요."],
    ["본문 11번","2지망 표가 1지망 표보다 영향력이 클 때가 있다","이게 AV 방식의 약점이에요."],
    ["정답 포인트","{{perfect|완벽한}} = {{flawless|흠 없는}}, {{influence|영향력}} = {{impact|영향}}","처음 보는 단어여도 앞뒤로 짐작해요."]],
}

# 바꿔 말하기 스토리: 본문 등장 순서. a=본문 단어, n=본문 문장 번호, sq=요약문 번호, sum=요약문 속 바뀐 모습([[ ]]=바뀐 단어), hook=기억 고리
STORY=[
 dict(a="examine",form="examined",n=1,sq=1,sum="The council members [[inspected]] the votes",hook="자치회가 표를 다시 꼼꼼히 들여다보는 문장의 examined(살펴보았다) → 요약문에서는 inspected(면밀히 조사했다)로 바꿨어요."),
 dict(a="result",form="result",n=1,sq=1,sum="realized that the [[outcome]] would be different",hook="이전과 다른 결과가 나올 거라는 문장의 result(결과) → 요약문에서는 outcome(결과)으로 바꿨어요."),
 dict(a="round",form="round",n=2,sq=2,sum="more than one [[stage]] of counting",hook="집계를 여러 번 할 수 있다는 규칙의 round(회, 차례) → 요약문에서는 stage(단계)로 바꿨어요."),
 dict(a="required",form="required",n=4,sq=2,sum="a second round was [[needed]]",hook="콘서트가 40%뿐이라 2차 집계가 요구되었다는 문장의 required(요구되다) → 요약문에서는 needed(필요했다)로 바꿨어요."),
 dict(a="eliminated",form="eliminated",n=6,sq=3,sum="so it was [[excluded]]",hook="1지망 표 꼴찌 A가 탈락하는 문장의 eliminated(탈락시켰다) → 요약문에서는 excluded(제외했다)로 바꿨어요."),
 dict(a="redistributed",form="redistributed",n=6,sq=3,sum="its votes were [[reallocated]]",hook="탈락한 A의 5표가 2지망대로 다시 나뉘는 문장의 redistributed(재분배되었다) → 요약문에서는 reallocated(다시 배정되었다)로 바꿨어요."),
 dict(a="perfect",form="perfect",n=10,sq=4,sum="The AV method is not [[flawless]]",hook="Unfortunately로 시작하는 반전 문장의 perfect(완벽한) → 요약문에서는 flawless(흠 없는)로 바꿨어요."),
 dict(a="influence",form="influence",n=11,sq=4,sum="more [[impact]] than first-preference votes",hook="2지망 표가 1지망 표보다 힘이 세질 수 있다는 문장의 influence(영향력) → 요약문에서는 impact(영향)로 바꿨어요."),
]

# 줄거리 장면: [[영어|한글뜻]] 표시 단어가 바꿔 말하기 대상
SCENES=[
 dict(tag="본문 1번",ns=[1],line="자치회가 AV 방식으로 표를 [[examined|살펴보니]], [[result|결과]]가 달라질 것 같았다."),
 dict(tag="본문 2~4번",ns=[2,3,4],line="집계는 여러 [[round|차례]] 할 수 있고, 자선 콘서트가 40%뿐이라 2차 집계가 [[required|필요했다]]."),
 dict(tag="본문 5~9번",ns=[5,6,7,8,9],line="1지망 표 꼴찌인 미술 전시회 A는 [[eliminated|탈락했고]], 그 5표가 [[redistributed|다시 나뉘어]] 빵 바자회가 승자가 되었다."),
 dict(tag="본문 10~12번",ns=[10,11,12],line="하지만 AV 방식도 [[perfect|완벽하지]] 않다. 2지망 표가 1지망 표보다 더 큰 [[influence|영향력]]을 갖기도 한다."),
]

# 근거 본문 한글 해석에서 영어 형광펜과 같은 자리
HLKO={1:["표를 검토했고","다른 결과가"],2:["한 차례 이상의 집계"],3:["50% 이상"],4:["40%만을 받았기","2차 집계가 필요했다"],
 5:["가장 적은 1지망 표"],6:["선택지 A는 제거되었고","두 번째 선호도에 따라 재분배되었다"],9:["빵 바자회가 승자가 될 것이었다"],
 10:["완벽하지는 않다"],11:["1지망 표보다 더 큰 영향력"],12:["주로 그것이 얻은 2지망 표 때문"]}

UM={'inspect':('면밀히 조사하다, 검토하다','살펴보았다'),'outcome':('결과','결과'),'stage':('단계','단계'),'majority':('과반수, 대다수','대다수'),
 'exclude':('제외하다','제외했다'),'reallocate':('다시 배정하다, 재분배하다','다시 배정했다'),'flawless':('흠 없는, 완벽한','흠잡을 데 없었다'),'impact':('영향(력)','큰 영향')}

TARGET={1:0,2:3,3:1,4:4}

G.update({'because':['because','~ 때문에'],'get':['get','얻다'],'second':['second','두 번째의, 2차의'],'first':['first','첫 번째의, 1차의'],'needs':['need','필요로 하다'],'only':['only','오직, ~뿐'],'made':['make','만들다'],'therefore':['therefore','따라서'],'either':['either','~도 (부정문에서)']})
