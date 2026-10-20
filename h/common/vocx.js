/* 어휘 퀴즈 해설: 다의어 = 사전 뜻 번호 + 해당 뜻 강조, 단어 관계 = 두 단어 뜻 모두 표기 */
(function(){
var WM={
'fix':'v. 고치다, 수리하다','mend':'v. 고치다, 수선하다','in addition':'adv. 게다가, 덧붙여','roughly':'adv. 대략, 약',
'buy':'v. 사다, 구입하다','sensible':'a. 분별 있는, 합리적인','rational':'a. 이성적인, 합리적인','choice':'n. 선택',
'in fact':'adv. 사실은, 실제로','actually':'adv. 실제로, 사실은','precisely':'adv. 정확히','poisonous':'a. 독이 있는, 유독한',
'decrease':'v. 감소하다 (n. 감소)','gather':'v. 모으다, 모이다','forecast':'v. 예보하다, 예측하다','treat':'v. 다루다, 대하다, 치료하다',
'handle':'v. 다루다, 처리하다','deal with ~':'v. ~을 다루다, 처리하다','feasible':'a. 실현 가능한','realistic':'a. 현실적인',
'deliberately':'adv. 고의로, 일부러','get':'v. 얻다, 받다','obtain':'v. 얻다, 획득하다','finish':'v. 끝내다, 마치다',
'encourage':'v. 격려하다, 장려하다','possess':'v. 소유하다, 가지고 있다','call for ~':'v. ~을 요구하다, 필요로 하다',
'forbid':'v. 금지하다','ban':'v. 금지하다 (n. 금지)','aim':'n. 목표, 목적','achieve':'v. 이루다, 달성하다',
'fulfill':'v. 이행하다, 달성하다, 충족시키다','extra':'a. 추가의, 여분의','while':'conj. ~인 반면에, ~하는 동안',
'show':'v. 보여주다, 나타내다','change':'n. 변화 (v. 바꾸다)','influence':'n. 영향 (v. 영향을 미치다)','useful':'a. 유용한, 쓸모 있는',
'happen':'v. 일어나다, 발생하다','viewpoint':'n. 관점, 시각','enormous':'a. 거대한, 막대한','just':'adv. 단지, 그저',
'perhaps':'adv. 아마, 어쩌면','maybe':'adv. 아마, 어쩌면','precious':'a. 귀중한, 소중한','principal':'a. 주요한, 주된',
'items':'n. 물품들, 항목들 (item의 복수형)','troops':'n. 군대, 병력 (troop의 복수형)','convinced':'v. 설득했다, 납득시켰다 (convince의 과거형)',
'commanded':'v. 명령했다 (command의 과거형)','retrieve':'v. 되찾아오다, 회수하다','finding out':'v. 알아내다 (find out의 -ing형)',
'sculptures':'n. 조각품들 (sculpture의 복수형)','eliminated':'v. 제거했다 (eliminate의 과거형)','hurried':'v. 서둘렀다 (hurry의 과거형)',
'give back':'v. 돌려주다','works':'n. 작품들 (work의 복수형)','exertions':'n. 노력, 수고 (exertion의 복수형)','source':'n. 원천, 출처',
'protection':'n. 보호','move':'v. 옮기다, 이동하다','saving':'v. 구하다 (save의 -ing형)','linking':'v. 연결하다 (link의 -ing형)',
'conserve':'v. 보존하다, 아끼다','presently':'adv. 현재, 지금','concise':'a. 간결한','confront':'v. 맞서다, 직면하다',
'wounded':'a. 부상을 입은','explanation':'n. 설명','guarantees':'v. 보장한다 (guarantee의 3인칭 단수형)','out loud':'adv. 소리 내어',
'characteristics':'n. 특징, 특성 (characteristic의 복수형)','impairments':'n. 장애 (impairment의 복수형)','almost':'adv. 거의',
'notice':'v. 알아차리다 (n. 주목, 공지)','whole':'a. 전체의, 전부의','inevitably':'adv. 불가피하게, 필연적으로','provide':'v. 제공하다',
'aged':'a. 나이 든, 고령의','vision':'n. 시력, 시야','modify':'v. 수정하다, 변경하다','completely':'adv. 완전히',
'profit':'n. 이익, 수익 (v. 이익을 얻다)','type':'n. 종류, 유형','restrict':'v. 제한하다','depend on':'v. ~에 의존하다, ~에 달려 있다',
'areas':'n. 지역들, 분야들 (area의 복수형)','released':'v. 출시했다, 발표했다 (release의 과거형)','issued':'v. 발행했다 (issue의 과거형)',
'too':'adv. 또한, 너무','bargain':'n. 거래, 싸게 산 물건','stimulus':'n. 자극','plentiful':'a. 풍부한, 많은',
'approximated':'v. 어림잡았다, 거의 ~였다 (approximate의 과거형)','goes back to':'v. ~로 거슬러 올라간다 (go back to의 3인칭 단수형)',
'diverse':'a. 다양한','facets':'n. 측면들 (facet의 복수형)','wrongly':'adv. 잘못되게, 부당하게','frightening':'a. 무서운, 겁나는',
'contradictory':'a. 모순되는','bravery':'n. 용감함, 용기','hurt':'v. 다치게 하다, 아프다','die out':'v. 멸종하다, 사라지다',
'disappeared':'v. 사라졌다 (disappear의 과거형)','restored':'v. 복원했다, 회복했다 (restore의 과거형)','symbolizes':'v. 상징한다 (symbolize의 3인칭 단수형)',
'holy':'a. 신성한','regarded as':'v. ~로 여겨졌다 (regard A as B의 과거형·과거분사)','referred to':'v. 언급했다, 가리켰다 (refer to의 과거형)',
'stanza':'n. (시의) 연','reworked':'v. 다시 손봤다, 개작했다 (rework의 과거형)','attract':'v. 끌어들이다, 끌다','significance':'n. 중요성, 의미',
'gathers':'v. 모은다 (gather의 3인칭 단수형)','in danger':'(숙어) 위험에 처한','catastrophes':'n. 대참사들 (catastrophe의 복수형)',
'especially':'adv. 특히','obvious':'a. 분명한, 명백한','shield':'v. 보호하다, 가리다 (n. 방패)','accomplishing':'v. 이루다, 완수하다 (accomplish의 -ing형)',
'supplied':'v. 공급했다 (supply의 과거형)','throw away':'v. 버리다','discarded':'v. 버렸다 (discard의 과거형)','wind up':'v. 결국 ~하게 되다',
'oceanic':'a. 바다의, 해양의','particular':'a. 특정한, 특별한','decompose':'v. 분해되다, 썩다','consume':'v. 소비하다, 먹다',
'grow':'v. 자라다, 기르다','carried':'v. 운반했다 (carry의 과거형)','draw out':'v. 끌어내다, 뽑아내다','efficacy':'n. 효능, 효험',
'take in':'v. 흡수하다, 받아들이다','hopeful':'a. 희망적인, 기대하는','investigated':'v. 조사했다 (investigate의 과거형)','data':'n. 자료, 데이터',
'produces':'v. 생산한다 (produce의 3인칭 단수형)','usually':'adv. 보통, 대개','discharges':'n. 배출(물) (discharge의 복수형)',
'converting':'v. 전환하다 (convert의 -ing형)','origins':'n. 기원, 근원 (origin의 복수형)','finally':'adv. 마침내, 결국','opportunity':'n. 기회',
'special':'a. 특별한','regarded':'v. 여겼다, 평가했다 (regard의 과거형)','abandoned':'v. 버렸다, 포기했다 (abandon의 과거형)',
'by contrast':'adv. 대조적으로, 그에 반해','sick':'a. 아픈','watched':'v. 지켜봤다 (watch의 과거형)','passed on':'v. 세상을 떠났다 (pass on의 과거형)',
'famous':'a. 유명한','restricted':'v. 제한했다 (restrict의 과거형·과거분사)','earn a living':'v. 생계를 꾸리다','steadily':'adv. 꾸준히',
'creative':'a. 창의적인','producing':'v. 생산하다 (produce의 -ing형)','portrayed':'v. 묘사했다 (portray의 과거형)','deformed':'a. 기형의, 변형된',
'surprise':'v. 놀라게 하다 (n. 놀람)','only':'adv. 오직, 단지','have a look at':'v. ~을 한 번 보다','participating in':'v. ~에 참여하다 (participate in의 -ing형)',
'remarkable':'a. 놀랄 만한, 주목할 만한','opposing':'v. 반대하다 (oppose의 -ing형)','chances':'n. 기회들 (chance의 복수형)','showed':'v. 보여줬다 (show의 과거형)',
'beautifully':'adv. 아름답게','astonishing':'a. 깜짝 놀랄 만한','potential':'n. 잠재력, 가능성','advantages':'n. 이점들 (advantage의 복수형)',
'illnesses':'n. 질병들 (illness의 복수형)','incorporate':'v. 포함하다, 통합하다','rather than':'prep. ~보다는, ~ 대신에','create':'v. 만들어 내다, 창조하다',
'remember':'v. 기억하다','anticipate':'v. 예상하다, 기대하다','accept':'v. 받아들이다, 수락하다','worries':'n. 걱정들 (worry의 복수형)',
'matter':'n. 문제, 일 (v. 중요하다)','because of':'prep. ~ 때문에','tackled':'v. 다뤘다, 해결하려 했다 (tackle의 과거형)','anxious':'a. 불안해하는, 걱정하는',
'defend':'v. 방어하다, 지키다','difficulties':'n. 어려움들 (difficulty의 복수형)','depending on':'prep. ~에 따라','rigorously':'adv. 철저하게, 엄격하게',
'conquer':'v. 정복하다, 극복하다','emphasizes':'v. 강조한다 (emphasize의 3인칭 단수형)','unbelievable':'a. 믿을 수 없는, 놀라운'
};
/* 한글 문장 속 강조할 부분 (자동으로 못 찾는 문장용): [문장 시작, 강조] */
var KHO=[
['그 오래된 배관에는','납'],['수리할 권리 운동은 다음','추진'],['텍사스는 미국에서','주'],['많은 회사는 그들의 고객들이','제삼자'],
['드레스에 커피를','망쳤'],['그 스캔들은','파멸시켰'],['1943년에, 14개의','만들기 위해 모였다'],['바람의 힘이','힘이'],
['그 교사는 학생들을','남게 했다'],['모뉴먼츠 맨은 연합군이','연합군'],['그는 아침 기차를','서둘렀다'],['나는 서둘러','서둘러'],
['그녀는 아침 일찍 파리로','떠났다'],['네가 밖으로 갈 때','열어 두어라'],['그 홍수는 마을에서','몇 채의 집만 남겼다'],
['그러나 작은 폭발들이','남아 있게 했다'],['그는 양손을 내 목에','조르기'],['그녀는 오늘 아침 오렌지들로부터','짜냈다'],
['불충분한 포장 자재와','자재'],['그는 아이들을 위해 케이크를','조각들'],['그 다리는 하나하나','하나하나'],['여러 해 동안, 그들은','식별'],
['그 책을 내일 도서관에','반납'],['그 책은 좋은 조언을','가치가 있다'],['그 단체는 이 언어들을','영상을 기록'],
['열 개의 서로 다른 부서가','형성하고 있다'],['텍스트와 함께, 대부분의','다른 형식'],['대체 텍스트는 비문자','간단한'],
['연한 노란색 글씨는','배경'],['이러한 이유로, 접근성 있는','배경 색'],['농부는 집 바로 옆에','옥수수밭'],['당신은 온라인 양식의','칸'],
['새 퀴즈 프로의','구성 방식'],['이미지 파일은','JPEG 형식'],['그 여우는 마른 잎','덫'],['Keller는 그녀','되살리고'],
['교사는 과학 실험에','흥미를 끌기'],['그녀의 단정한','외모'],['한국 문화에서 호랑이의','등장'],['여러분 중 일부는','등장하는'],
['그러나, 과거에는 호랑이에게','흔했기'],['이 집들은 강을','향하고'],['제마가 거짓말을','얼굴'],['그 도시는 해외에서','개최할'],
['그들은 친구의 생일을','열기로'],['그러나, 한국에서 열린','열린'],['많은 사람들은 그의 지혜와','여긴다'],['백호는 신성한','여겨진다'],
['마지막 절을','절을'],['이 노래의 한 구절','구절'],['그녀는 그를 어려운','여긴다'],['우리는 오늘 아침 일찍','보기'],
['그 노래는 세계적인','시청'],['호랑이가 한국의 상징이라는','부정할'],['저희는 15개의','수집했습니다'],['2021년에, 국립','모은'],
['기온은 이번 여름','도달할'],['기후 변화가 위험 수준에','도달하지'],['우리는 높은 쇼핑센터','층'],['게다가, 이것은 단지','다른 곳'],
['그 화재로 그의','타 버렸다'],['종종, 플라스틱 쓰레기는','태워지는'],['우리는 정원 중앙에','심기로'],['다행히도, 오염된','심는'],
['정부가 산업용','배기가스'],['그는 직면하는','보여준다'],['우리는 겉으로','소중히 여겨야'],['그녀는 팀 내에서','가치'],
['각 예술가에게는','높이 평가받게'],['결정을 내리기 전에','검토해'],['첫 번째로 살펴볼','살펴볼'],['다른 사람 실수할','못되게'],
['이제 〈비열한 개〉','비열한'],['새 모델은','특징으로 포함한다'],['그녀의 그림을 보면','등장한다는'],['이런 종류의 꽃은','흔하다'],
['가속페달을 밟는 힘을','힘'],['그녀의 작품 〈푸른 방','반사되는'],['그 남자는 법정에서','드러내지'],['이 두 나무 조각을','붙여라'],
['선생님은 학생들의 숙제를','도울'],['유엔은 긴급','구호 물자'],['이곳은 좋은 와인을','즐길'],['〈빨간 썰매〉에는','꽃밭'],
['이 글에서는','글'],['당신은 태양으로부터','발라야'],['이러한 장치를','캡처'],['당신은 그 인기 있는','월간 호']
];
var IRR={lead:'led',leave:'left'};
var N=['①','②','③','④','⑤','⑥','⑦','⑧','⑨'];
var headM={};
function E(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function esc(s){return s.replace(/[.*+?^$()|[\]\\{}]/g,'\\$&')}
function buildHead(){if(!window.VOC||headM.__done)return;headM.__done=1;
  VOC.SYN.forEach(function(x){if(x.m&&!headM[x.h])headM[x.h]=(x.pos?x.pos+' ':'')+x.m;x.ant.forEach(function(a){if(a.m&&!headM[a.w])headM[a.w]=a.m})})}
function mw(w){buildHead();return WM[w]||headM[w]||''}
function KHL(m,k){
  for(var j=0;j<KHO.length;j++)if(k.indexOf(KHO[j][0])===0&&k.indexOf(KHO[j][1])>=0)return KHO[j][1];
  var s=String(m).replace(/^\s*(vt|vi|v|n|a|adj|adv|prep|conj|pron)\.\s*/,'').replace(/\[[^\]]*\]/g,'').replace(/\([^)]*\)/g,'');
  var alts=s.split(/[,;·\/]/).map(function(x){return x.replace(/~/g,'').replace(/^\s+|\s+$/g,'')}).filter(Boolean),cands=[];
  alts.forEach(function(a){
    a=a.replace(/^(을|를|에게|에|의|이|가|와|과|로|으로|에서)\s+/,'');
    var words=a.split(/\s+/);
    [a,words[words.length-1],words[0]].forEach(function(c){
      if(!c)return;var x=c;
      for(var n=0;n<4;n++){if(x.length>=2&&cands.indexOf(x)<0)cands.push(x);
        var y=x.replace(/(하다|되다|시키다|이다|에서|에게|으로|적인|스러운|하는|하게|한|인|의|은|는|을|를|에|로|다|히|게)$/,'');if(y===x)break;x=y}
    })
  });
  cands.sort(function(a,b){return b.length-a.length});
  for(var i=0;i<cands.length;i++){var c=cands[i];if(c.length>=2&&k.indexOf(c)>=0)return c}
  for(var i=0;i<cands.length;i++){var c=cands[i];if(c.length>=2){var p=c.slice(0,2),ix=k.indexOf(p);if(ix>=0){var e=ix+2;while(e<k.length&&/[가-힣]/.test(k.charAt(e))&&e-ix<c.length+1)e++;return k.slice(ix,e)}}}
  return '';
}
function EHL(e,w){
  var tries=[];
  if(IRR[w])tries.push(new RegExp('\\b'+IRR[w]+'\\b','i'));
  tries.push(new RegExp('\\b'+esc(w)+'(?:s|es|ed|d|ing)?\\b','i'),new RegExp('\\b'+esc(w.slice(0,Math.max(3,w.length-1)))+'\\w*','i'),new RegExp('\\b'+esc(w.slice(0,3))+'\\w*','i'));
  for(var i=0;i<tries.length;i++){var m=tries[i].exec(e);if(m)return m[0]}return '';
}
function hl(s,sub){s=String(s);sub=(sub||'').replace(/\s+$/,'');var i=sub?s.indexOf(sub):-1;
  if(i<0)return E(s);return E(s.slice(0,i))+'<b class="vxh">'+E(sub)+'</b>'+E(s.slice(i+sub.length))}
function fbkO(q){
  var r=q.a==='s'?'비슷한 뜻':q.a==='a'?'반대 뜻':'서로 관련 없음';
  var ws=[q.x.l,q.x.r];
  return '<div class="vxo">'+ws.map(function(w){var m=mw(w);return'<div class="vxw"><b>'+E(w)+'</b><span>'+E(m||'')+'</span></div>'}).join('')+'</div><div class="vxr">'+E(q.x.l)+' — '+E(q.x.r)+' &rarr; <b>'+r+'</b></div>';
}
function fbkP(q){
  var bi=-1;q.all.forEach(function(z,i){if(z.e===q.a)bi=i});
  var no=function(i){return N[i]||(i+1)+'.'};
  var h='<div class="vxs">교과서 문장</div><div class="vxb same"><div class="vxe">'+hl(q.tx.e,EHL(q.tx.e,q.tx.h||q.w))+'</div><div class="vxk">'+hl(q.tx.k,KHL(q.bm,q.tx.k))+'</div><div class="vxn"><b>'+E(q.w)+'</b> = '+(bi>=0?no(bi)+' ':'')+E(q.bm)+'</div></div>';
  h+='<div class="vxs"><b>'+E(q.w)+'</b>의 뜻</div><div class="vxls">'+q.all.map(function(z,i){return'<div class="vxl'+(i===bi?' on':'')+'"><b>'+no(i)+'</b> '+E(z.m)+(i===bi?'<span class="vxt">교과서</span>':'')+'</div>'}).join('')+'</div>';
  h+='<div class="vxs">예문 비교</div>'+q.all.map(function(z,i){var same=i===bi;
    return'<div class="vxb '+(same?'same':'diff')+'"><div class="vxn"><b>'+no(i)+'</b> '+E(z.m)+'<span class="vxt'+(same?'':' d')+'">'+(same?'교과서와 같은 뜻':'다른 뜻')+'</span></div><div class="vxe">'+hl(z.e,EHL(z.e,q.w))+'</div><div class="vxk">'+hl(z.k,KHL(z.m,z.k))+'</div></div>'}).join('');
  return h;
}
function fbk(q){return q.t==='O'?fbkO(q):fbkP(q)}
var st=document.createElement('style');
st.textContent='.vxh{color:var(--pri);font-weight:800;text-decoration:underline;text-underline-offset:3px}'
+'.vxs{font-size:13px;font-weight:800;color:var(--sub);margin:12px 0 4px;padding-top:8px;border-top:1px solid var(--line)}'
+'.vxs:first-child{border-top:0;margin-top:2px;padding-top:0}'
+'.vxo{display:flex;flex-direction:column;gap:6px;margin:2px 0 8px}'
+'.vxw{display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}.vxw b{font-size:17px;color:var(--navy)}.vxw span{color:var(--ink);font-size:15px}'
+'.vxr{margin-top:6px;padding-top:8px;border-top:1px solid var(--line)}'
+'.vxls{display:flex;flex-direction:column;gap:3px}.vxl{font-size:15px}.vxl.on{font-weight:800}.vxl b{color:var(--pri)}'
+'.vxt{display:inline-block;font-size:11.5px;font-weight:800;color:var(--pri);border:1px solid var(--pri);border-radius:999px;padding:0 7px;margin-left:6px;vertical-align:1px}.vxt.d{color:var(--sub);border-color:var(--line)}'
+'.vxb{border-radius:10px;padding:8px 10px;margin:6px 0;background:var(--card);border:1px solid var(--line)}.vxb.same{border-color:var(--pri);background:var(--priL)}'
+'.vxb .vxn{font-size:13.5px;font-weight:700;margin-bottom:4px;color:var(--sub)}.vxb.same .vxn{color:var(--ink)}.vxb .vxn b{color:var(--pri)}'
+'.vxe{font-size:15.5px;line-height:1.55}.vxk{font-size:14.5px;line-height:1.55;color:var(--sub);margin-top:2px}';
document.head.appendChild(st);
window.VX={fbk:fbk,mw:mw,KHL:KHL,EHL:EHL,WM:WM};
})();
