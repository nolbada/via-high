# -*- coding: utf-8 -*-
# 세트 정의: 청석고1 3과 ❶
META=dict(sch='cheongseok-go1', src='cheongseok-go1/L3/sx-data.js', pidx=0, lesson='3과', title='호랑이와 한국 문화 (Tigers in Korean Culture)', label='❶', page='yoyak-lian-z1')
Q = [
 dict(
  id=1,
  summary="Tae Keller's book, (A) in 2020, helped children around the world learn more about Korean (B).",
  ko="Tae Keller의 책은 2020년에 <b>(A) 출간되어</b> 전 세계 아이들이 한국 <b>(B) 문화</b>에 대해 더 알게 되도록 도왔다.",
  opts=[["released","culture"],["translated","culture"],["translated","language"],["reviewed","history"],["released","food"]],
  optko=["출간하다 – 문화","번역하다 – 문화","번역하다 – 언어","비평하다 – 역사","출간하다 – 음식"],
  ans=0,
  wrong=[None,
         "translated(번역하다)가 틀려요. 본문은 책을 번역했다는 말이 아니라 출판(publish)했다고 해요.",
         "둘 다 틀려요. 번역했다는 말도, language(언어)를 알게 됐다는 말도 본문에 없어요.",
         "둘 다 틀려요. reviewed(비평하다)도 history(역사)도 본문에 나오지 않아요.",
         "food(음식)가 틀려요. 아이들이 알게 된 건 음식이 아니라 한국 문화(culture)예요."],
  evid=[dict(n=1, hl=["Korean culture","published her book"])],
  swaps=[["publish","release","출판하다 → 출간하다, 내놓다"],["a bit more","more","조금 더 → 더"],["writer Tae Keller published her book","Tae Keller's book, released","작가가 책을 출판했을 때 → 책이 출간되어"]],
  swapnote="publish(출판하다)는 시험에서 release(내놓다, 출간하다)로 바뀌어 나와요. 같은 뜻이니 본문 단어만 찾지 마세요.",
  use=[dict(w="release",ex="The band will release a new song next week.",ko="그 밴드는 다음 주에 새 노래를 발표할 것이다."),
       dict(w="culture",ex="Food is an important part of culture.",ko="음식은 문화의 중요한 부분이다.")],
  flow="본문 1번은 이야기의 첫 문장이에요. 작가 Tae Keller가 호랑이 책을 내자 전 세계 아이들이 한국 문화를 조금 더 알게 됐다고 시작해요.",
 ),
 dict(
  id=2,
  summary="In the book, a girl (A) a tiger, and when her grandmother becomes ill, she makes a (B) with it.",
  ko="책에서 한 소녀가 호랑이를 <b>(A) 만나고</b>, 할머니가 아프게 되자 그 호랑이와 <b>(B) 거래</b>를 한다.",
  opts=[["encounters","bargain"],["encounters","fight"],["avoids","bargain"],["avoids","fight"],["imagines","plan"]],
  optko=["마주치다 – 거래","마주치다 – 싸움","피하다 – 거래","피하다 – 싸움","상상하다 – 계획"],
  ans=0,
  wrong=[None,
         "fight(싸움)가 틀려요. 소녀는 호랑이와 싸우는 게 아니라 거래(deal)를 해요.",
         "avoids(피하다)가 틀려요. 소녀는 호랑이를 피하지 않고 만나요(meets).",
         "둘 다 틀려요. 소녀는 호랑이를 피하지도, 싸우지도 않아요.",
         "둘 다 틀려요. 소녀는 호랑이를 상상하는 게 아니라 실제로 만나고, 계획이 아니라 거래를 해요."],
  evid=[dict(n=2, hl=["meets a tiger"]), dict(n=4, hl=["gets sick","makes a deal"])],
  swaps=[["meet","encounter","만나다 → 마주치다"],["deal","bargain","거래 → 거래, 흥정"],["sick","ill","아픈 → 아픈"]],
  swapnote="meet(만나다)는 encounter(마주치다)로, sick(아픈)은 ill(아픈)로 바뀌어 나올 수 있어요. deal(거래)은 bargain(거래)으로도 써요.",
  use=[dict(w="encounter",ex="We encountered a deer on the trail.",ko="우리는 산길에서 사슴을 마주쳤다."),
       dict(w="bargain",ex="They made a bargain to share the cake.",ko="그들은 케이크를 나눠 먹기로 거래를 했다.")],
  flow="본문 2번에서 소녀가 호랑이를 만나고(3번: 할머니도 그 호랑이를 알아요), 4번에서 할머니가 아프게 되자 소녀가 호랑이와 거래를 해요.",
 ),
 dict(
  id=3,
  summary="Keller's prize-winning book was (A) by an old (B) that her grandmother used to tell her.",
  ko="Keller의 수상 도서는 할머니가 들려주곤 하던 옛 <b>(B) 이야기</b>에서 <b>(A) 영감을 받았다</b>.",
  opts=[["inspired","story"],["inspired","rumor"],["limited","story"],["limited","rumor"],["limited","song"]],
  optko=["영감을 주다 – 이야기","영감을 주다 – 소문","제한하다 – 이야기","제한하다 – 소문","제한하다 – 노래"],
  ans=0,
  wrong=[None,
         "rumor(소문)가 틀려요. 할머니가 들려주던 건 소문이 아니라 옛 설화(folktale), 즉 옛이야기예요.",
         "limited(제한하다)가 틀려요. 옛 설화는 책을 제한한 게 아니라 책에 영감(inspiration)을 줬어요.",
         "둘 다 틀려요. 제한했다는 말도, 소문이라는 말도 본문에 없어요.",
         "둘 다 틀려요. 제한했다는 말도, 노래라는 말도 본문에 없어요. 옛이야기(설화)예요."],
  evid=[dict(n=5, hl=["inspiration","old folktale"])],
  swaps=[["inspiration","inspire","영감 → 영감을 주다"],["folktale","story","옛 설화 → 이야기"],["award-winning","prize-winning","수상한 → 상을 받은"]],
  swapnote="inspiration(영감)은 inspire(영감을 주다)로, folktale(옛 설화)은 story(이야기)로 쉽게 바꿔 나와요. 품사가 바뀌어도 뜻은 같아요.",
  use=[dict(w="inspire",ex="Her teacher inspired her to become a writer.",ko="선생님은 그녀가 작가가 되도록 영감을 주었다."),
       dict(w="story",ex="My grandmother told me a funny story.",ko="할머니는 나에게 재미있는 이야기를 들려주셨다.")],
  flow="본문 5번이 중요해요. 상을 받은 Keller의 책에 영감을 준 것은 할머니가 어릴 때부터 들려주던 옛 설화였어요.",
 ),
 dict(
  id=4,
  summary="Keller wanted to (A) people's interest in tigers by writing her own (B).",
  ko="Keller는 자신의 <b>(B) 소설</b>을 씀으로써 호랑이에 대한 사람들의 관심을 <b>(A) 되살리고</b> 싶어 했다.",
  opts=[["renew","novel"],["renew","speech"],["reduce","novel"],["reduce","speech"],["hide","poem"]],
  optko=["되살리다 – 소설","되살리다 – 연설","줄이다 – 소설","줄이다 – 연설","숨기다 – 시"],
  ans=0,
  wrong=[None,
         "speech(연설)가 틀려요. Keller는 연설이 아니라 책(book)을 써서 관심을 되살리려 했어요.",
         "reduce(줄이다)가 틀려요. 관심을 줄이려는 게 아니라 되살리려(revive) 했어요.",
         "둘 다 틀려요. 관심을 줄인다는 말도, 연설이라는 말도 본문에 없어요.",
         "둘 다 틀려요. 관심을 숨긴다는 말도, 시를 쓴다는 말도 본문에 없어요."],
  evid=[dict(n=7, hl=["revive","interest in tigers","writing her own book"])],
  swaps=[["revive","renew","되살리다 → 되살리다, 새롭게 하다"],["public","people","대중 → 사람들"],["book","novel","책 → 소설"]],
  swapnote="revive(되살리다)는 renew(되살리다, 새롭게 하다)나 restore(회복시키다)로 바뀌어 나와요. the public(대중)은 people(사람들)로 쉽게 바뀌어요.",
  use=[dict(w="renew",ex="The festival helped renew interest in old songs.",ko="그 축제는 옛 노래에 대한 관심을 되살리는 데 도움이 되었다."),
       dict(w="novel",ex="She wrote a novel about a dragon.",ko="그녀는 용에 관한 소설을 썼다.")],
  flow="본문 7번은 이 글의 마무리예요. Keller가 책을 쓴 이유는 호랑이에 대한 사람들의 관심을 다시 살리고 싶어서예요.",
 ),
]

# 단어 사전: 표면형(소문자) -> [기본형, 이 글에서의 뜻]
G = {
 "children":["child","아이들"],"around":["around","~ 곳곳의"],"world":["world","세계"],"learned":["learn","알게 되다, 배우다"],
 "learn":["learn","알게 되다, 배우다"],"bit":["bit","조금"],"korean":["Korean","한국의"],"culture":["culture","문화"],
 "writer":["writer","작가"],"published":["publish","출판하다"],"book":["book","책"],"story":["story","이야기"],
 "starts":["start","시작하다"],"girl":["girl","소녀"],"meets":["meet","만나다"],"tiger":["tiger","호랑이"],"tigers":["tiger","호랑이"],
 "grandmother":["grandmother","할머니"],"knows":["know","알다"],"well":["well","잘 (as well = 역시)"],
 "gets":["get","~해지다"],"sick":["sick","아픈"],"ill":["ill","아픈"],"makes":["make","~을 하다, 만들다"],"deal":["deal","거래"],
 "keller's":["Keller","Keller(작가 이름)"],"inspiration":["inspiration","영감"],"award-winning":["award-winning","상을 받은, 수상한"],
 "prize-winning":["prize-winning","상을 받은, 수상한"],"old":["old","옛, 오래된"],"folktale":["folktale","옛 설화, 민간 이야기"],
 "halmoni":["halmoni","할머니(한국어)"],"used":["use","~하곤 했다 (used to ~)"],"tell":["tell","말해 주다, 들려주다"],
 "called":["call","부르다 (is called = ~라고 불린다)"],"sun":["sun","해"],"moon":["moon","달"],"brother":["brother","오빠, 형"],
 "sister":["sister","여동생, 누나"],"wanted":["want","원하다"],"revive":["revive","되살리다"],"public":["public","대중"],
 "interest":["interest","관심, 흥미"],"writing":["write","쓰다"],"own":["own","자기 자신의"],"released":["release","출간하다, 내놓다"],
 "release":["release","출간하다, 내놓다"],"translated":["translate","번역하다"],"reviewed":["review","비평하다, 검토하다"],
 "history":["history","역사"],"language":["language","언어"],"food":["food","음식"],"helped":["help","돕다"],
 "encounters":["encounter","마주치다, 만나다"],"encounter":["encounter","마주치다, 만나다"],"avoids":["avoid","피하다"],
 "imagines":["imagine","상상하다"],"bargain":["bargain","거래, 흥정"],"fight":["fight","싸움"],"plan":["plan","계획"],
 "becomes":["become","~해지다, ~이 되다"],"inspired":["inspire","영감을 주다"],"inspire":["inspire","영감을 주다"],
 "rumor":["rumor","소문"],"limited":["limit","제한하다"],"song":["song","노래"],"renew":["renew","되살리다, 새롭게 하다"],
 "reduce":["reduce","줄이다"],"hide":["hide","숨기다"],"novel":["novel","소설"],"speech":["speech","연설"],"poem":["poem","시"],
 "people's":["people","사람들"],"people":["people","사람들"],"band":["band","밴드"],"important":["important","중요한"],
 "part":["part","부분"],"deer":["deer","사슴"],"trail":["trail","산길"],"share":["share","나누다"],"cake":["cake","케이크"],
 "teacher":["teacher","선생님"],"become":["become","~이 되다"],"funny":["funny","재미있는"],"festival":["festival","축제"],
 "songs":["song","노래"],"dragon":["dragon","용"],"wrote":["write","쓰다"],"told":["tell","말해 주다"],"made":["make","~을 하다"],
 "week":["week","주"],"next":["next","다음의"],"new":["new","새로운"],"price":["price","가격"],
}

# 직독직해 조각
JD={
 1:[["Tae Keller's book, [[released]] in 2020,","Tae Keller의 책은 2020년에 [[출간되어]]"],
    ["helped children around the world learn","전 세계 아이들이 알게 되도록 도왔다"],
    ["more about Korean [[culture]].","한국 [[문화]]에 대해 더."]],
 2:[["In the book, a girl [[encounters]] a tiger,","책에서 한 소녀는 호랑이를 [[만나고]],"],
    ["and when her grandmother becomes ill,","그리고 그녀의 할머니가 아프게 되자,"],
    ["she makes a [[bargain]] with it.","그녀는 그 호랑이와 [[거래]]를 한다."]],
 3:[["Keller's prize-winning book was [[inspired]]","Keller의 수상 도서는 [[영감을 받았다]]"],
    ["by an old [[story]] that her grandmother used to tell her.","그녀의 할머니가 들려주곤 하던 옛 [[이야기]]로부터."]],
 4:[["Keller wanted to [[renew]]","Keller는 [[되살리고]] 싶어 했다"],
    ["people's interest in tigers","호랑이에 대한 사람들의 관심을"],
    ["by writing her own [[novel]].","자신의 [[소설]]을 씀으로써."]],
}

FC={
 1:[["본문 1번","작가 Tae Keller가 호랑이 책을 냈다","2020년에 나온 When You Trap a Tiger예요."],
    ["결과","전 세계 아이들이 한국 문화를 알게 됐다","조금 더 알게 됐다는 뜻이에요."],
    ["정답 포인트","{{published|출판했다}} = {{released|출간됐다}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 2~3번","소녀가 호랑이를 만난다","할머니도 그 호랑이를 알고 있어요."],
    ["본문 4번","할머니가 아프다 → 거래","{{gets sick|아프게 되다}}, {{makes a deal|거래를 하다}}"],
    ["정답 포인트","{{meets|만나다}} = {{encounters|마주치다}}, {{deal|거래}} = {{bargain|거래}}","소녀는 호랑이를 피하지도 싸우지도 않아요."]],
 3:[["본문 5번","상을 받은 책에 영감을 준 것은?","할머니가 들려주던 옛 설화예요."],
    ["이어서","옛 설화 이름은 해님 달님","오빠, 여동생, 호랑이가 나오는 이야기예요."],
    ["정답 포인트","{{inspiration|영감}} → {{inspired|영감을 받은}}, {{folktale|옛 설화}} → {{story|이야기}}","품사가 바뀌어도 뜻은 같아요."]],
 4:[["본문 6번","해님 달님 이야기","오빠, 여동생, 그리고 호랑이가 나와요."],
    ["본문 7번","호랑이에 대한 관심을 되살리고 싶었다","그래서 자기만의 책을 썼어요."],
    ["정답 포인트","{{revive|되살리다}} = {{renew|되살리다}}, {{book|책}} = {{novel|소설}}","{{public|대중}}은 {{people|사람들}}로 바뀌어요."]],
}

STORY=[
 dict(a="publish",form="published",n=1,sq=1,sum="Tae Keller's book, [[released]] in 2020",hook="작가가 책을 냈다는 첫 문장의 published(출판했다) → 요약문에서는 released(출간된)로 바꿨어요."),
 dict(a="meet",form="meets",n=2,sq=2,sum="a girl [[encounters]] a tiger",hook="소녀가 호랑이를 만나는 장면의 meets(만나다) → 요약문에서는 encounters(마주치다)로 바꿨어요."),
 dict(a="deal",form="deal",n=4,sq=2,sum="she makes a [[bargain]] with it",hook="할머니가 아프자 소녀가 호랑이와 맺는 deal(거래) → 요약문에서는 bargain(거래)으로 바꿨어요."),
 dict(a="inspiration",form="inspiration",n=5,sq=3,sum="was [[inspired]] by an old story",hook="책을 쓰게 한 힘이 된 inspiration(영감) → 요약문에서는 inspired(영감을 받은)로 바꿨어요."),
 dict(a="folktale",form="folktale",n=5,sq=3,sum="an old [[story]] that her grandmother used to tell her",hook="할머니가 들려주던 옛날 이야기 folktale(옛 설화) → 요약문에서는 story(이야기)로 바꿨어요."),
 dict(a="revive",form="revive",n=7,sq=4,sum="wanted to [[renew]] people's interest in tigers",hook="호랑이에 대한 관심을 다시 살리고 싶다는 revive(되살리다) → 요약문에서는 renew(되살리다)로 바꿨어요."),
 dict(a="book",form="book",n=7,sq=4,sum="by writing her own [[novel]]",hook="자기 책을 쓴다는 마지막 문장의 book(책) → 요약문에서는 novel(소설)로 바꿨어요."),
]

SCENES=[
 dict(tag="본문 1번",ns=[1],line="작가 Tae Keller가 호랑이 [[book|책]]을 [[published|출판하자]] 전 세계 아이들이 한국 문화를 알게 됐다."),
 dict(tag="본문 2~4번",ns=[2,3,4],line="책 속 소녀가 호랑이를 [[meets|만난다]]. 할머니가 아프자 호랑이와 [[deal|거래]]를 한다."),
 dict(tag="본문 5번",ns=[5],line="책을 쓰게 한 [[inspiration|영감]]은 할머니가 들려주던 옛 [[folktale|설화]]였다."),
 dict(tag="본문 7번",ns=[7],line="호랑이에 대한 관심을 [[revive|되살리고]] 싶어서 직접 쓴 것이다."),
]

HLKO={1:["한국 문화","출판했을 때"],2:["호랑이를 만난"],4:["아프게 되자","거래를 한다"],5:["영감을 준 것은","옛 설화"],
 7:["그녀 자신의 책을 씀으로써","호랑이에 대한 대중의 흥미","되살리고"]}

UM={'release':('출간하다, 발표하다','발표할'),'culture':('문화','문화'),'encounter':('마주치다, 만나다','마주쳤다'),'bargain':('거래, 흥정','거래'),'inspire':('영감을 주다','영감을 주었다'),'story':('이야기','이야기'),'renew':('되살리다, 새롭게 하다','되살리는'),'novel':('소설','소설')}

G.update({'inspired':['inspire','영감을 주다']})

TARGET={1:2,2:0,3:4,4:1}
G.update({'tae':['Tae','Tae(작가 이름)'],'keller':['Keller','Keller(작가 이름)'],'keller’s':['Keller','Keller(작가 이름)'],'about':['about','~에 대해'],'trap':['trap','가두다, 잡다'],'public’s':['public','대중의']})
