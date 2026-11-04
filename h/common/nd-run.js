(function(){var SN={'geumcheon-go1':'금천고1','jusung-go1':'주성고1','cheongseok-go1':'청석고1'},m=/\/h\/([a-z0-9-]+)\//.exec(location.pathname),f=document.getElementById('foot');if(f)f.textContent='비타민 영어클리닉 · '+((m&&SN[m[1]])||'');})();

(function(){
var TY={
 voc:{n:'어휘',how:''},
 find:{n:'TF',how:''},
 eob:{n:'어법선택',how:''},
 awk:{n:'어색한 곳',how:''},
 und:{n:'밑줄의 의미',how:''}
};
var q=location.search,T=(/nd-(voc|find|eob|awk|und)\.html/.exec(location.pathname)||/[?&]t=(voc|find|eob|awk|und)/.exec(q)||[])[1]||'voc';
var pk=(/[?&]part=(\d+)/.exec(q)||[])[1];var P=pk?+pk:0;
var K=P?('mockp'+P+':'+(T==='eob'?'eobeop':T==='awk'?'awk':T)):'mock:'+T;
var ids=(PARTS.mock[P]||[]);var KEEP={voc:.7,find:.7,eob:.75,awk:.7,und:.7};
var H=document.getElementById('stage'),CNT=document.getElementById('cnt'),PB=document.getElementById('pb');
document.getElementById('h1').innerHTML='유형 풀코스 · '+TY[T].n+' <span class="fc">FULL COURSE</span>';
document.getElementById('rng').textContent=P?('이번 범위: '+PARTS.names.mock[P]):'';
document.getElementById('how').style.display='none';
var ACTN=T==='eob'?'eobeop':T;
if(WN.MODE){document.getElementById('h1').insertAdjacentHTML('afterend',WN.MIX?WN.mixInfo():'<div class="how" style="border-color:#b45309"><b>오답 다시 풀기</b> · 오답 노트에 담은 문제만 보여요. <a href="../wrong.html">오답 노트 ›</a></div>')}
var all=[];
ids.forEach(function(e){var sp=String(e).split(':'),pid=sp[0],d=ND[pid];if(!d||!d[T])return;var L=d[T],a=0,b=L.length;if(sp.length>2){a=Math.floor(L.length*(+sp[1])/10);b=Math.floor(L.length*(+sp[2])/10)}var kn=Math.ceil((b-a)*KEEP[T]);if(P===11){a+=kn}else{b=a+kn}for(var i=a;i<b;i++)all.push({id:pid+'#'+i,pid:pid,it:L[i],lab:pid==='2610-41'?'26년 10월 41~42번':pid.replace(/^(\d\d)(\d\d)-(\d+)$/,'$1년 $2월 $3번')})});
if(WN.MODE){var _wi=WN.ids('mock',P,ACTN);all=all.filter(function(x){return _wi.indexOf(x.id)>=0})}
if(!all.length){H.innerHTML=WN.MODE?'<div class="card sum"><h3>오답 노트에 담긴 문제가 없어요</h3><a class="nx sub" style="text-decoration:none;text-align:center" href="../wrong.html">오답 노트 ›</a></div>':'<div class="card sum"><h3>이 범위에는 이 유형 문제가 없어요</h3></div>';return}
var SK='nd:'+K+WN.SUF,S;try{S=JSON.parse(localStorage.getItem(SK)||'null')}catch(e){}
if(!S||S.n!==all.length)S={n:all.length,done:{},round:1,wrong:{},fin:0};
function save(){try{localStorage.setItem(SK,JSON.stringify(S))}catch(e){}}
var queue=[],pos=0;
function shuf(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j];a[j]=t}return a}
function build(){queue=all.filter(function(x){return !S.done[x.id]});pos=0}
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function top(){var d=Object.keys(S.done).length;CNT.textContent=(S.round>1?(S.round+'번째 돌기 · '):'')+'맞힌 문제 '+d+' / '+all.length;PB.style.width=(d/all.length*100)+'%'}
function show(){
 top();
 if(pos>=queue.length){
  var left=all.filter(function(x){return !S.done[x.id]});
  if(!left.length){return fin()}
  H.innerHTML='<div class="card sum"><h3>'+S.round+'번째 돌기 끝</h3><p>틀린 문제 <b>'+left.length+'개</b>만 다시 풀어요.</p><button class="nx" id="again" type="button">틀린 것만 다시 ›</button></div>';
  document.getElementById('again').onclick=function(){S.round++;save();build();show()};return}
 var x=queue[pos],it=x.it,h='<div class="card"><span class="tag">'+x.lab+' · '+(pos+1)+'/'+queue.length+'</span>';
 if(T==='voc'||T==='eob'||T==='und'){
  var ord=shuf(it.ch.map(function(c,i){return i}));
  h+='<div class="ctx">'+(T==='eob'?esc(it.s).replace('( ______ )','<b>(&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)</b>'):it.q)+'</div>'+(it.ask?'<div class="ask">'+it.ask+'</div>':'<div class="ask">알맞은 것을 고르세요.</div>');
  ord.forEach(function(i){h+='<button class="ch" type="button" data-i="'+i+'">'+it.ch[i]+'</button>'});
 }else if(T==='find'){
  h+='<div class="ctx">'+esc(it.s)+'</div><div class="ask">지문 내용과 맞을까요?</div><div class="tf"><button class="ch" data-i="1" type="button">맞아요 (T)</button><button class="ch" data-i="0" type="button">틀려요 (F)</button></div>';
 }else{
  var t=it.t.replace(/\[\[(\d)\|([^\]]+)\]\]/g,function(m,n,w){return '<button class="sp2" type="button" data-i="'+n+'"><sup>'+'①②③④⑤'[n-1]+'</sup>'+esc(w)+'</button>'});
  h+='<div class="ctx" style="font-size:16.5px">'+t+'</div><div class="ask">문맥상 어색한 곳은?</div><div id="spx"></div>';
 }
 h+='<div id="fb"></div><div id="wnm"></div></div>';H.innerHTML=h;window.scrollTo(0,0);
 function wnItem(){return{kind:'mock',part:P,act:ACTN,qid:x.id,label:x.lab+' · '+TY[T].n}}
 function wnMan(){var m=document.getElementById('wnm');if(!m)return;m.innerHTML='';var b=WN.manual(wnItem());if(b)m.appendChild(b)}
 wnMan();
 var locked=0;
 function pass(ok,txt,ex){
  if(locked)return;locked=1;
  if(ok){S.done[x.id]=1}else{S.wrong[x.id]=(S.wrong[x.id]||0)+1;try{WN.add(wnItem());wnMan()}catch(e){}}
  save();top();
  var fb=document.getElementById('fb');
  fb.innerHTML=((T==='und'||T==='voc'||T==='eob')&&it.tr?'<div class="trb"><b>'+(T==='und'?'밑줄 해석':'문장 해석')+'</b>'+esc(it.tr)+'</div>':'')+'<div class="why"><b class="'+(ok?'r':'w')+'">'+(ok?'정답!':'아쉬워요')+'</b> '+txt+'</div>'+(T==='eob'&&it.g?'<div class="trb"><b>쉬운 문법 설명</b>'+esc(it.g).replace(/\n/g,'<br>')+'</div>':'')+(T==='voc'&&it.alt?'<div class="trb"><b>바꿔 쓸 수 있는 말</b>'+esc(it.alt)+'</div>':'')+(ex||(it.e?'<div class="ez"><b>쉽게 말해</b>'+esc(it.e)+'</div>':''))+'<button class="nx" id="nx" type="button">'+(pos+1<queue.length?'다음 ›':'이 돌기 마치기 ›')+'</button>';
  document.getElementById('nx').onclick=function(){pos++;show()};
  try{document.getElementById('nx').focus({preventScroll:true})}catch(e){}
 }
 var bs=H.querySelectorAll('.ch,.sp2');
 [].forEach.call(bs,function(b){b.onclick=function(){
  if(locked&&T!=='awk')return;var i=+b.getAttribute('data-i'),ok,txt;
  if(T==='voc'||T==='eob'||T==='und'){ok=i===it.a;
   [].forEach.call(bs,function(o){var oi=+o.getAttribute('data-i');o.disabled=true;if(oi===it.a)o.classList.add('ok');else if(oi===i)o.classList.add('no')});
   txt=esc(it.why)}
  else if(T==='find'){var ans=it.a?1:0;ok=i===ans;
   [].forEach.call(bs,function(o){var oi=+o.getAttribute('data-i');o.disabled=true;if(oi===ans)o.classList.add('ok');else if(oi===i)o.classList.add('no')});
   txt='정답은 <b>'+(it.a?'맞아요(T)':'틀려요(F)')+'</b>. '+esc(it.why)}
  else{
   if(locked){var cd=document.getElementById('sc'+i);if(cd)cd.scrollIntoView({behavior:'smooth',block:'center'});return}
   ok=i===it.a;[].forEach.call(bs,function(o){var oi=+o.getAttribute('data-i');if(oi===it.a)o.classList.add('ok');else if(oi===i)o.classList.add('no')});
   var shown=function(n){return (new RegExp('\\[\\['+n+'\\|([^\\]]+)\\]\\]').exec(it.t)||[])[1]};
   var cards='';it.sp.forEach(function(sp,k){var n=k+1,bad=n===it.a;
    cards+='<div class="spc'+(bad?' bad':'')+'" id="sc'+n+'"><div class="spt"><b>'+'①②③④⑤'[k]+' '+esc(shown(n))+'</b> <span class="vd">'+(bad?'어색함':'맞음')+'</span></div>'
     +'<div class="spw"><b>'+esc(sp.b)+'</b> : '+esc(sp.m)+(sp.n?'<br><span class="nt">'+esc(sp.n)+'</span>':'')+'</div>'
     +'<div>'+esc(sp.y)+'</div>'+(sp.e?'<div class="ez"><b>쉽게 말해</b>'+esc(sp.e)+'</div>':'')+'</div>'});
   pass(ok,(ok?'찾았어요. ':'')+'어색한 곳은 <b>'+'①②③④⑤'[it.a-1]+' '+esc(shown(it.a))+'</b>, 원래 말은 <b>'+esc(it.fix)+'</b>.',cards);return}
    pass(ok,txt)}});
}
function fin(){
 if(!S.fin){S.fin=1;save();if(!WN.MODE){try{PG.mark(K)}catch(e){}}}
 var tot=0,w=0;Object.keys(S.wrong).forEach(function(k){w++});
 H.innerHTML='<div class="card sum"><div class="big">✓</div><h3>'+TY[T].n+' 끝!</h3><p>'+all.length+'문제를 모두 맞혔어요.'+(w?'<br>한 번 이상 틀렸던 문제는 <b>'+w+'개</b>예요. 다음 수업 첫머리에 한 번 더 훑어 보면 눈에 남아요.':'<br>한 번에 다 맞혔어요!')+'</p>'+(WN.MODE?(WN.MIX?WN.mixSum():'<p class="wn-l" style="margin:12px 0 0;font-size:14px;color:var(--sub)">이제 안 봐도 되는 문제는 오답 노트에서 \'빼기\'로 뺄 수 있어요.</p>'):'<button class="nx sub" id="rst" type="button">처음부터 다시 풀기</button>')+'<a class="nx" style="text-decoration:none;text-align:center" href="../index.html">← 목록</a></div>';
 PB.style.width='100%';CNT.textContent='완료';
 var _r=document.getElementById('rst');if(_r)_r.onclick=function(){S={n:all.length,done:{},round:1,wrong:{},fin:1};save();build();show()};
}
build();show();
})();
