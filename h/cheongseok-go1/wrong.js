/* 오답 노트: 틀린 문제를 이 기기(브라우저)에 모아 두고, 모아서 다시 풀게 한다.
   저장 위치: localStorage "vhw:<학교폴더>" = [{id,kind,part,act,qid,label,t,q?}]
   kind: 'L4' | 'mock' | ..., act: voc|find|awk|eobeop|ko|abc|mun|blank
   qid : 활동 안에서 그 문제를 가리키는 값(문자열). voc 은 문제 전체를 q 에 저장.
   전체 랜덤(?mix=1): 같은 활동 페이지를 '이번 회차에 뽑힌 문제만' 보여 주는 모드로 재사용한다.
   저장 위치: localStorage "vhmx:<학교폴더>" = {round,used:[id..],cur:[{kind,part,act,qid,w}],done:{},open:{},cyc}
   규칙: 1차 오답은 자동 저장(c=1), 2차 오답은 별표(star=true). 학생이 문제를 뺄 수 없다. 예전에 별표가 켜진 항목은 그대로 둔다. */
var WN=(function(){
  var seg=location.pathname.split('/'),i=seg.indexOf('h'),school=(i>=0&&seg[i+1])||'x',KEY='vhw:'+school;
  function load(){try{return JSON.parse(localStorage.getItem(KEY)||'[]')}catch(e){return[]}}
  function save(a){try{localStorage.setItem(KEY,JSON.stringify(a))}catch(e){}}
  var tt=0;
  function toast(n,star){
    if(!document.body||Date.now()-tt<4000)return;tt=Date.now();
    var d=document.createElement('a');d.href=base()+'wrong.html';
    d.textContent=star?'2차 오답이라 별표(★)가 생겼어요 ›':'오답 노트에 담았어요 (지금 '+n+'개) ›';
    d.style.cssText='position:fixed;left:50%;top:14px;transform:translateX(-50%);background:#b45309;color:#fff;padding:9px 16px;border-radius:999px;font:700 14px sans-serif;z-index:99999;text-decoration:none;box-shadow:0 4px 14px rgba(0,0,0,.25);transition:opacity .6s;white-space:nowrap';
    document.body.appendChild(d);setTimeout(function(){d.style.opacity=0},3200);setTimeout(function(){d.remove()},3900)}
  function base(){var p=location.pathname,k=p.indexOf('/'+school+'/');return k>=0?p.slice(0,k+school.length+2):'./'}
  var WR=/[?&]wrong=1\b/.test(location.search),MX=!WR&&/[?&]mix=1\b/.test(location.search),MKEY='vhmx:'+school,SR=WR&&/[?&]star=1\b/.test(location.search);
  function mxLoad(){try{var o=JSON.parse(localStorage.getItem(MKEY)||'null');return o&&o.cur?o:null}catch(e){return null}}
  function mxSave(o){try{localStorage.setItem(MKEY,JSON.stringify(o))}catch(e){}}
  var MS=MX?mxLoad():null;
  function here(){var p=location.pathname,k=(/\/(L\d+|mock)\//.exec(p)||[])[1]||'',f=p.split('/').pop().replace('.html','');
    var a={'vocab':'voc','find':'find','awkward-test':'awk','eobeop-test':'eobeop','sunseo-ko':'ko','sunseo-abc':'abc','sunseo-mun':'mun','blank':'blank'}[f];
    var m=/[?&]part=(\d+)/.exec(location.search);return{kind:k,part:m?+m[1]:0,act:a}}
  function mxPick(kind,part,act){return ((MS&&MS.cur)||[]).filter(function(x){return x.kind===kind&&x.part===part&&x.act===act})}
  if(MX){var go=function(){[].forEach.call(document.querySelectorAll('a.back'),function(a){a.href=base()+'mix.html';a.textContent='← 랜덤 문제'})};
    if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',go);else go()}
  /* 랜덤 이어 풀기: 묶음이 끝나면 아래에 다음 유형 바 (261022) */
  if(MX){(function(){var h0=here(),K0=h0.kind+'|'+h0.part+'|'+h0.act,QK='vhmq:'+school,shown='';
    function bar(){var q=null;try{q=JSON.parse(localStorage.getItem(QK)||'null')}catch(e){}
      var s=mxLoad();if(!q||!q.l||!s||q.r!==s.round||!(s.done&&s.done[K0]))return;
      var idx=-1;q.l.forEach(function(x,i){if(x.k===K0)idx=i});if(idx<0)return;
      var nx=null;for(var i=idx+1;i<q.l.length;i++){if(!(s.done&&s.done[q.l[i].k])){nx=q.l[i];break}}
      var key=nx?nx.k:'end';if(shown===key||!document.body)return;shown=key;
      var old=document.getElementById('vhmnext');if(old)old.remove();
      var a=document.createElement('a');a.id='vhmnext';a.href=base()+(nx?nx.u:'mix.html');a.textContent=nx?'다음 유형: '+nx.n+' \u203a':'체크한 유형을 모두 끝냈어요 \u00b7 랜덤 문제로';
      a.onclick=function(){if(nx){var s2=mxLoad();if(s2){s2.open=s2.open||{};s2.open[nx.k]=1;mxSave(s2)}}else{try{localStorage.removeItem(QK)}catch(e){}}};
      a.style.cssText='position:fixed;left:12px;right:104px;bottom:12px;z-index:9998;background:#1e2a44;color:#fff;text-align:center;font:800 15px/1.2 sans-serif;padding:15px 12px;border-radius:14px;text-decoration:none;box-shadow:0 3px 10px rgba(0,0,0,.3)';
      document.body.appendChild(a)}
    setInterval(bar,700)})()}
  /* 오답 다시 풀기(?wrong=1) 보강: 안내 문구 정리, 다음 묶음 이어가기, 푼 문제 수 기록 (261021) */
  if(WR){
    var SK='vhs:'+school,counted=0;
    function sget(){try{return JSON.parse(localStorage.getItem(SK)||'{}')}catch(e){return{}}}
    function fixNote(){
      if(!document.body)return;
      var tw=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT),n,hit=null;
      while((n=tw.nextNode())){if(n.nodeValue.indexOf('이제 안 봐도 되는')>=0){hit=n;break}}
      if(!hit)return;
      hit.nodeValue=hit.nodeValue.replace(/이제 안 봐도 되는 문제는[^.]*\./,'이 묶음을 다 풀었어요.');
      var h=here();
      if(!counted&&h.act){counted=1;WN.addSolved(WN.ids(h.kind,h.part,h.act).length,'w')}
      var q=null;try{q=JSON.parse(sessionStorage.getItem('wq')||'null')}catch(e){}
      var a=document.createElement('a'),nx=q&&q.urls&&q.urls[q.i+1];
      a.style.cssText='display:inline-block;margin-left:6px;color:#0f766e;text-decoration:underline;font-weight:700';
      if(nx){a.href=nx;a.textContent='다음 묶음 풀기 ›';a.onclick=function(){q.i++;try{sessionStorage.setItem('wq',JSON.stringify(q))}catch(e){}}}
      else{a.href=base()+'wrong.html';a.textContent='오답 노트로 돌아가기 ›';a.onclick=function(){try{sessionStorage.removeItem('wq')}catch(e){}}}
      hit.parentNode.insertBefore(a,hit.nextSibling)}
    var _ft=0;function go2(){if(_ft)return;_ft=setTimeout(function(){_ft=0;fixNote()},60)}
    var st=function(){new MutationObserver(go2).observe(document.body,{childList:true,subtree:true,characterData:true});go2()};
    if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',st);else st()}
  return{
    MODE:WR||MX,
    MIX:MX,
    /* 이어 풀기 기록 키 꼬리: 오답 다시 풀기 ':w', 전체 랜덤 ':m<회차>', 평소 '' */
    SUF:WR?(SR?':ws':':w'):MX?':m'+(MS?MS.round:0):'',
    mixRound:function(){return MS?MS.round:0},
    /* 이 묶음을 다 풀었다고 표시(활동 페이지가 끝났을 때 부른다) */
    finish:function(){if(!MX)return;var s=mxLoad(),h=here();if(!s||!h.act)return;var k=h.kind+'|'+h.part+'|'+h.act;s.done=s.done||{};if(s.done[k])return;s.done[k]=1;mxSave(s);var n=0;(s.cur||[]).forEach(function(x){if(x.kind===h.kind&&x.part===h.part&&x.act===h.act)n+=(x.w||0)});WN.addSolved(n,'m')},
    mixNote:function(fin){if(fin)WN.finish();return'<b>랜덤 '+WN.mixRound()+'회</b> · 이번 세트에 뽑힌 문제만 보여요. <a href="'+base()+'mix.html" style="color:#0f766e;text-decoration:underline">랜덤 문제로 ›</a>'+(fin?'<div style="margin-top:6px">이 묶음을 다 풀었어요. 틀린 문제는 <a href="'+base()+'wrong.html" style="color:#0f766e;text-decoration:underline">오답 노트</a>에 담겨요.</div>':'')},
    mixInfo:function(){return'<div class="how" style="border-color:#b45309"><b>랜덤 '+WN.mixRound()+'회</b> · 이번 세트에 뽑힌 지문으로 문제를 새로 풀어요. <a href="'+base()+'mix.html">랜덤 문제로 ›</a></div>'},
    mixSum:function(){WN.finish();return'<p class="wn-l" style="margin:12px 0 0;font-size:14px">이 묶음을 다 풀었어요. 틀린 문제는 <a href="'+base()+'wrong.html">오답 노트</a>에 담겨요.<br><a href="'+base()+'mix.html">랜덤 문제로 돌아가기 ›</a></p>'},
    /* 전체 랜덤 현황(MIXPOOL 이 있을 때): 회차, 전체/남은 문항 */
    mixStat:function(){var s=mxLoad(),P=window.MIXPOOL,tot=0,use={};if(s)(s.used||[]).forEach(function(i){use[i]=1});var left=0;
      if(P)P.units.forEach(function(u){tot+=u[4];if(!use[u[0]+':'+u[1]+':'+u[2]+':'+u[3]])left+=u[4]});
      var ks={},nd=0;((s&&s.cur)||[]).forEach(function(x){ks[x.kind+'|'+x.part+'|'+x.act]=1});Object.keys(ks).forEach(function(k){if(!(s.done&&s.done[k]))nd++});
      return{round:s?s.round:0,total:tot,left:left,bundles:Object.keys(ks).length,undone:nd}},
    /* 직접 담기: 다른 기기에서 풀었다가 기억나는 틀린 문제를 담는 버튼. p = add() 항목. 오답 다시 풀기·랜덤 모드에서는 만들지 않는다. 담기만 되고 빼기는 없다. */
    manual:function(p){if(MX||WR)return null;
      var b=document.createElement('button');b.type='button';b.className='wn-man';
      function paint(){var on=WN.has(p.kind,p.part,p.act,p.qid);b.textContent=on?'오답 노트에 담겼어요':'틀렸거나 헷갈렸어요 · 오답 노트에 담기';b.disabled=on;
        b.style.cssText='display:inline-block;margin:6px 0 0;padding:7px 12px;border-radius:999px;font:700 12.5px/1.2 inherit;font-family:inherit;cursor:'+(on?'default':'pointer')+';border:1.5px solid '+(on?'#a8a29e':'#0f766e')+';background:'+(on?'#f5f5f4':'#fff')+';color:'+(on?'#78716c':'#0f766e')}
      b.onclick=function(e){e.stopPropagation();e.preventDefault();if(WN.has(p.kind,p.part,p.act,p.qid))return;WN.add(p);paint()};
      b.onkeydown=function(e){e.stopPropagation()};
      paint();return b},
    school:school,
    addSolved:function(n,k){if(!(n>0))return;var s={};try{s=JSON.parse(localStorage.getItem('vhs:'+school)||'{}')}catch(e){}s.n=(s.n||0)+n;if(k)s[k]=(s[k]||0)+n;try{localStorage.setItem('vhs:'+school,JSON.stringify(s))}catch(e){}},
    solvedBy:function(k){try{return(JSON.parse(localStorage.getItem('vhs:'+school)||'{}')[k])||0}catch(e){return 0}},
    solved:function(){try{return(JSON.parse(localStorage.getItem('vhs:'+school)||'{}').n)||0}catch(e){return 0}},
    list:function(){return load()},
    count:function(){return load().length},
    id:function(kind,part,act,qid){return kind+':'+part+':'+act+':'+qid},
    has:function(kind,part,act,qid){var id=WN.id(kind,part,act,qid);return load().some(function(x){return x.id===id})},
    /* it = {kind,part,act,qid,label,q?}  이미 있으면 그대로 둔다 */
    add:function(it){var a=load();it.id=WN.id(it.kind,it.part,it.act,it.qid);
      var x=a.filter(function(y){return y.id===it.id})[0];
      if(x){var had=x.star!==false;x.w=1;x.c=(x.c||1)+1;x.star=true;save(a);if(!had)toast(a.length,true);return}
      it.t=Date.now();it.w=1;it.c=1;it.star=false;a.push(it);save(a);toast(a.length)},
    /* 별표: 틀린 문제는 자동으로 켜짐. 맞혔지만 헷갈린 문제도 별표로 담을 수 있다(w=0).
       별을 끄면 틀린 적 있는 문제는 노트에 남고, 별만 친 문제는 노트에서도 빠진다. */
    isStar:function(kind,part,act,qid){var id=WN.id(kind,part,act,qid),x=load().filter(function(y){return y.id===id})[0];return !!x&&x.star!==false},
    star:function(it){var a=load();it.id=WN.id(it.kind,it.part,it.act,it.qid);
      var x=a.filter(function(y){return y.id===it.id})[0];
      if(!x){it.t=Date.now();it.w=0;it.star=true;a.push(it);save(a);return true}
      if(x.star===false){x.star=true;save(a);return true}
      if(x.w===0){save(a.filter(function(y){return y.id!==it.id}));return false}
      x.star=false;save(a);return false},
    setStar:function(id,on){var a=load(),x=a.filter(function(y){return y.id===id})[0];if(!x)return;
      if(on){x.star=true;save(a);return}
      if(x.w===0){save(a.filter(function(y){return y.id!==id}));return}
      x.star=false;save(a)},
    starCount:function(){return load().filter(function(x){return x.star!==false}).length},
    remove:function(id){save(load().filter(function(x){return x.id!==id}))},
    /* 오답 다시 풀기 모드(?wrong=1)에서 이 활동·구간에 담긴 문제 id 목록 */
    ids:function(kind,part,act){if(MX)return mxPick(kind,part,act).map(function(x){return x.qid});return load().filter(function(x){return x.kind===kind&&x.part===part&&x.act===act&&(!SR||x.star!==false)}).map(function(x){return x.qid})},
    items:function(kind,part,act){if(MX)return mxPick(kind,part,act);return load().filter(function(x){return x.kind===kind&&x.part===part&&x.act===act&&(!SR||x.star!==false)})}
  }
})();
