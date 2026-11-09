# -*- coding: utf-8 -*-
# 세트 정의: 주성고2 모의고사 22년 11월 30번
META=dict(sch='jusung-go2', src='jusung-go2/mock/sx-data.js', pidx=1, lesson='22년 11월 30번', title='', label='', page='yoyak-2211-30')
Q = [
 dict(
  id=1,
  summary="Light from above makes the top of an object bright and its bottom gradually darker, and this shading gives the object (A) so that viewers can (B) its shape.",
  ko="위에서 오는 빛은 물체의 위쪽은 밝게, 아래쪽은 점차 어둡게 만들고, 이 음영은 물체에 <b>(A) 입체감</b>을 주어 보는 사람이 그 모양을 <b>(B) 알아볼</b> 수 있게 한다.",
  opts=[["dimension","recognize"],["dimension","hide"],["flatness","recognize"],["flatness","hide"],["brightness","change"]],
  optko=["입체감 – 알아보다","입체감 – 숨기다","평평함 – 알아보다","평평함 – 숨기다","밝기 – 바꾸다"],
  ans=0,
  wrong=[None,
         "hide(숨기다)가 틀려요. 음영 덕분에 모양을 숨기는 게 아니라 알아보게 돼요.",
         "flatness(평평함)가 틀려요. 음영은 물체에 깊이감(depth)을 줘요.",
         "둘 다 틀려요. 음영은 평평하게 만들지도, 모양을 숨기지도 않아요.",
         "둘 다 틀려요. 본문은 밝기를 바꾼다고 하지 않고, 깊이감을 주어 모양을 구별하게 한다고 해요."],
  evid=[dict(n=3, hl=["gradually shade darker toward the bottom"]), dict(n=4, hl=["gives the object depth","distinguish its shape"])],
  swaps=[["depth","dimension","깊이감 → 입체감"],["distinguish","recognize","구별하다 → 알아보다"],["the viewer","viewers","보는 사람 → 보는 사람들"]],
  swapnote="depth(깊이)는 dimension(차원, 입체감)으로, distinguish(구별하다)는 recognize(알아보다)로 바뀌어 나올 수 있어요.",
  use=[dict(w="dimension",ex="The drawing has a third dimension.",ko="그 그림에는 세 번째 차원, 즉 입체감이 있다."),
       dict(w="recognize",ex="I could not recognize him in the dark.",ko="나는 어둠 속에서 그를 알아볼 수 없었다.")],
  flow="본문 2~3번에서 위에서 빛을 받으면 위는 밝고 아래로 갈수록 어두워져요 → 4번에서 이 음영이 깊이감을 주어 모양을 구별하게 해 줘요.",
 ),
 dict(
  id=2,
  summary="An animal that is exactly the same color as its background is easily (A) under light from above, yet most animals are actually (B) on their upper side than on their lower side.",
  ko="배경과 정확히 같은 색인 동물은 위에서 빛을 받으면 쉽게 <b>(A) 눈에 띄지만</b>, 대부분의 동물은 실제로 아랫면보다 윗면이 더 <b>(B) 어둡다</b>.",
  opts=[["noticeable","darker"],["noticeable","lighter"],["hidden","darker"],["hidden","lighter"],["unclear","brighter"]],
  optko=["눈에 띄는 – 더 어두운","눈에 띄는 – 더 밝은","숨겨진 – 더 어두운","숨겨진 – 더 밝은","불분명한 – 더 밝은"],
  ans=0,
  wrong=[None,
         "lighter(더 밝은)가 틀려요. 본문은 대부분의 동물이 윗부분이 더 어둡다고 해요.",
         "hidden(숨겨진)이 틀려요. 배경과 같은 색이어도 빛을 받으면 쉽게 눈에 띄어요.",
         "둘 다 틀려요. 눈에 띈다고 했는데 숨겨진다고 했고, 윗부분은 더 어두운데 더 밝다고 했어요.",
         "둘 다 틀려요. 쉽게 보인다고 했고(unclear 아님), 윗부분은 더 어두워요(brighter 아님)."],
  evid=[dict(n=5, hl=["easily visible"]), dict(n=6, hl=["darker above than they are below"])],
  swaps=[["visible","noticeable","보이는 → 눈에 띄는"],["the substrate","its background","밑바탕 → 배경"],["above ... below","upper side ... lower side","위 ... 아래 → 윗면 ... 아랫면"]],
  swapnote="visible(눈에 보이는)은 noticeable(눈에 띄는)로 바뀌어 나와요. 5번의 반전(However)도 놓치지 마세요.",
  use=[dict(w="noticeable",ex="The red car is very noticeable on the gray street.",ko="빨간 차는 회색 거리에서 매우 눈에 띈다."),
       dict(w="dark",ex="It gets dark early in winter.",ko="겨울에는 일찍 어두워진다.")],
  flow="본문 5번: 배경과 같은 색이어도 빛이 비치면 눈에 띈다 → 6번에서 However! 하지만 대부분의 동물은 위가 더 어둡다는 반전이 나와요.",
 ),
 dict(
  id=3,
  summary="Because the dark back of an animal is (A) and its light belly is shaded by light from above, the animal looks like one color and (B) into its background.",
  ko="동물의 어두운 등은 위에서 오는 빛에 <b>(A) 밝아지고</b> 밝은 배는 음영이 생기기 때문에, 동물은 한 가지 색처럼 보이며 배경 속으로 <b>(B) 섞여 든다</b>.",
  opts=[["brightened","merges"],["brightened","stands out"],["darkened","merges"],["darkened","stands out"],["hidden","separates"]],
  optko=["밝아지다 – 섞이다","밝아지다 – 눈에 띄다","어두워지다 – 섞이다","어두워지다 – 눈에 띄다","숨겨지다 – 분리되다"],
  ans=0,
  wrong=[None,
         "stands out(눈에 띄다)이 틀려요. 동물은 배경과 섞여서 안 보이게 돼요.",
         "darkened(어두워지다)가 틀려요. 어두운 등은 빛을 받아 밝아져요.",
         "둘 다 틀려요. 등은 밝아지고, 동물은 눈에 띄지 않고 배경에 섞여요.",
         "둘 다 틀려요. 본문에 등이 숨겨진다는 말도, 배경과 분리된다는 말도 없어요."],
  evid=[dict(n=7, hl=["the darker back is lightened"]), dict(n=8, hl=["easily blends in with the substrate"])],
  swaps=[["lighten","brighten","밝아지다 → 밝아지다"],["blend","merge","섞이다 → 합쳐지다"],["a single color","one color","하나의 색 → 한 가지 색"]],
  swapnote="blend in(섞이다)은 merge(합쳐지다)로도 바뀌어 나와요. 한국말로는 모두 '섞인다'예요.",
  use=[dict(w="brighten",ex="The sun will brighten the room.",ko="햇빛이 방을 환하게 해 줄 것이다."),
       dict(w="merge",ex="Two small rivers merge into one big river.",ko="두 작은 강이 합쳐져 하나의 큰 강이 된다.")],
  flow="본문 7번에서 위에서 빛을 받으면 어두운 등은 밝아지고 밝은 배는 어두워져요 → 8번에서 그래서 한 가지 색처럼 보여 배경에 섞여요.",
 ),
]

G = {
 "light":["light","빛 (또 '밝은')"],"above":["above","위에서, 위쪽에"],"top":["top","위쪽"],"object":["object","물체"],
 "bright":["bright","밝은"],"bottom":["bottom","아래쪽"],"gradually":["gradually","점차"],"darker":["dark","더 어두운"],
 "dark":["dark","어두운"],"shading":["shading","음영(밝고 어두움의 차이)"],"gives":["give","주다"],"viewers":["viewer","보는 사람"],
 "viewer":["viewer","보는 사람"],"shape":["shape","모양"],"dimension":["dimension","입체감, 차원"],"flatness":["flatness","평평함"],
 "recognize":["recognize","알아보다"],"hide":["hide","숨기다"],"brightness":["brightness","밝기"],"change":["change","바꾸다"],
 "animal":["animal","동물"],"animals":["animal","동물"],"exactly":["exactly","정확히"],"same":["same","같은"],"color":["color","색"],
 "background":["background","배경"],"easily":["easily","쉽게"],"under":["under","~ 아래에서, ~을 받아"],"most":["most","대부분의"],
 "actually":["actually","실제로"],"upper":["upper","위쪽의"],"lower":["lower","아래쪽의"],"side":["side","면, 쪽"],
 "noticeable":["noticeable","눈에 띄는"],"lighter":["light","더 밝은"],"hidden":["hide","숨겨진"],"unclear":["unclear","불분명한"],
 "brighter":["bright","더 밝은"],"because":["because","~ 때문에"],"back":["back","등"],"belly":["belly","배(복부)"],
 "brightened":["brighten","밝아지다 (brightened = 밝아진)"],"darkened":["darken","어두워지다 (darkened = 어두워진)"],
 "merges":["merge","섞이다, 합쳐지다"],"merge":["merge","섞이다, 합쳐지다"],"stands":["stand out","눈에 띄다"],"stand":["stand out","눈에 띄다"],
 "separates":["separate","분리되다"],"shaded":["shade","음영이 생기다"],"shade":["shade","음영이 생기다"],"looks":["look","~처럼 보이다"],
 "into":["into","~ 속으로"],"countershading":["countershading","카운터셰이딩(위는 어둡고 아래는 밝은 보호색)"],
 "process":["process","과정"],"optical":["optical","시각적인"],"flattening":["flatten","평평하게 하다"],
 "provides":["provide","제공하다"],"camouflage":["camouflage","위장"],"sunlight":["sunlight","햇빛"],"illuminates":["illuminate","(빛을) 비추다"],
 "illuminated":["illuminate","(빛을) 비추다 (illuminated = 빛이 비춰진)"],"brightest":["bright","가장 밝은"],"color":["color","색"],
 "depth":["depth","깊이(감)"],"allows":["allow","~하게 해 주다"],"distinguish":["distinguish","구별하다"],
 "thus":["thus","따라서"],"even":["even","~일지라도"],"uniformly":["uniformly","균일하게"],"substrate":["substrate","밑바탕"],
 "visible":["visible","눈에 보이는"],"however":["however","그러나"],"below":["below","아래에"],"lightened":["lighten","밝아지다 (lightened = 밝아진)"],
 "lighten":["lighten","밝아지다"],"appears":["appear","~처럼 보이다"],"single":["single","하나의"],"blends":["blend","섞이다"],
 "blend":["blend","섞이다"],"pattern":["pattern","형태, 무늬"],"coloration":["coloration","배색, 색깔 형태"],"destroys":["destroy","파괴하다"],
 "visual":["visual","시각적인"],"impression":["impression","인상"],"organism":["organism","생물체"],"brighten":["brighten","밝아지다, 환하게 하다"],
 "shade":["shade","음영이 생기다"],"make":["make","만들다"],"makes":["make","만들다"],"darker":["dark","더 어두운"],"toward":["toward","~쪽으로"],
 "can":["can","~할 수 있다"],"one":["one","하나의"],
}

JD={
 1:[["Light from above","위에서 오는 빛은"],
    ["makes the top of an object bright","물체의 위쪽을 밝게 만들고"],
    ["and its bottom gradually darker,","아래쪽을 점차 더 어둡게 만들며,"],
    ["and this shading gives the object [[dimension]]","이 음영은 물체에 [[입체감]]을 준다"],
    ["so that viewers can [[recognize]] its shape.","그래서 보는 사람들이 그 모양을 [[알아볼]] 수 있도록."]],
 2:[["An animal that is exactly the same color as its background","배경과 정확히 같은 색인 동물은"],
    ["is easily [[noticeable]] under light from above,","위에서 빛을 받으면 쉽게 [[눈에 띄지만]],"],
    ["yet most animals are actually [[darker]]","하지만 대부분의 동물은 실제로 [[더 어둡다]]"],
    ["on their upper side than on their lower side.","아랫면보다 윗면이."]],
 3:[["Because the dark back of an animal is [[brightened]]","동물의 어두운 등이 [[밝아지고]]"],
    ["and its light belly is shaded by light from above,","밝은 배는 위에서 오는 빛에 음영이 생기기 때문에,"],
    ["the animal looks like one color","동물은 한 가지 색처럼 보이며"],
    ["and [[merges]] into its background.","배경 속으로 [[섞여 든다]]."]],
}

FC={
 1:[["본문 2~3번","위에서 빛을 받으면 위는 밝고 아래는 어둡다","아래로 갈수록 점점 어두운색으로 변해요."],
    ["본문 4번","이 음영이 깊이감을 준다","보는 사람이 모양을 구별할 수 있어요."],
    ["정답 포인트","{{depth|깊이감}} = {{dimension|입체감}}, {{distinguish|구별하다}} = {{recognize|알아보다}}","본문 단어가 뜻이 같은 말로 바뀌어 나와요."]],
 2:[["본문 5번","배경과 같은 색이어도 빛을 받으면 눈에 띈다","{{visible|눈에 보이는}}"],
    ["본문 6번","However! 대부분 동물은 위가 더 어둡다","반전이 나오는 자리예요."],
    ["정답 포인트","{{visible|눈에 보이는}} = {{noticeable|눈에 띄는}}","{{darker|더 어두운}}는 본문 그대로 나와요."]],
 3:[["본문 7번","어두운 등은 밝아지고 밝은 배는 어두워진다","위에서 오는 빛 때문이에요."],
    ["본문 8번","그래서 한 가지 색처럼 보인다","배경과 쉽게 섞여요."],
    ["정답 포인트","{{lightened|밝아진}} = {{brightened|밝아진}}, {{blend in|섞이다}} = {{merge|합쳐지다}}","섞이는 쪽이 정답이에요."]],
}

STORY=[
 dict(a="depth",form="depth",n=4,sq=1,sum="this shading gives the object [[dimension]]",hook="음영이 물체에 입체감을 준다는 문장의 depth(깊이) → 요약문에서는 dimension(입체감)으로 바꿨어요."),
 dict(a="distinguish",form="distinguish",n=4,sq=1,sum="viewers can [[recognize]] its shape",hook="보는 사람이 모양을 구별한다는 문장의 distinguish(구별하다) → 요약문에서는 recognize(알아보다)로 바꿨어요."),
 dict(a="visible",form="visible",n=5,sq=2,sum="is easily [[noticeable]] under light from above",hook="같은 색이어도 빛을 받으면 눈에 보인다는 문장의 visible(눈에 보이는) → 요약문에서는 noticeable(눈에 띄는)로 바꿨어요."),
 dict(a="lighten",form="lightened",n=7,sq=3,sum="is [[brightened]]",hook="어두운 등이 빛을 받아 환해진다는 문장의 lighten(밝아지다) → 요약문에서는 brighten(밝아지다)으로 바꿨어요."),
 dict(a="blend",form="blends",n=8,sq=3,sum="and [[merges]] into its background",hook="동물이 배경에 슬쩍 섞인다는 문장의 blend(섞이다) → 요약문에서는 merge(합쳐지다)로 바꿨어요."),
]

SCENES=[
 dict(tag="본문 2~3번",ns=[2,3],line="햇빛이 위에서 비추면 물체는 위가 밝고 아래로 갈수록 어두워진다."),
 dict(tag="본문 4번",ns=[4],line="이 음영이 [[depth|깊이감]]을 주어 모양을 [[distinguish|구별]]하게 해 준다."),
 dict(tag="본문 5번",ns=[5],line="그래서 배경과 같은 색이어도 빛을 받으면 쉽게 [[visible|눈에 보인다]]."),
 dict(tag="본문 7번",ns=[7],line="하지만 대부분 동물은 위가 어두워서, 어두운 등이 빛을 받으면 [[lightened|밝아진다]]."),
 dict(tag="본문 8번",ns=[8],line="동물은 한 가지 색처럼 되어 배경에 쉽게 [[blends|섞인다]]."),
]

HLKO={3:["점차 더 어두운색으로 음영이 생기게"],4:["깊이감(입체감)를 주고","모양을 식별하게"],5:["쉽게 눈에 띌"],6:["아랫부분보다 윗부분이 더 어둡다"],
 7:["더 어두운 등은 밝아지고"],8:["밑바탕과 쉽게 섞인다"]}

UM={'dimension':('입체감, 차원','입체감'),'recognize':('알아보다','알아볼'),'noticeable':('눈에 띄는','눈에 띈다'),'dark':('어두운','어두워진다'),'brighten':('밝아지다, 환하게 하다','환하게'),'merge':('합쳐지다','합쳐져')}

TARGET={1:1,2:3,3:4}
G.update({'yet':['yet','하지만'],'like':['like','~처럼'],'out':['stand out','눈에 띄다']})
