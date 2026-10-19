/* 오답 노트: 틀린 문제를 이 기기(브라우저)에 모아 두고, 모아서 다시 풀게 한다.
   저장 위치: localStorage "vhw:<학교폴더>" = [{id,kind,part,act,qid,label,t,q?}]
   kind: 'L4' | 'mock' | ..., act: voc|find|awk|eobeop|ko|abc|mun|blank
   qid : 활동 안에서 그 문제를 가리키는 값(문자열). voc 은 문제 전체를 q 에 저장.
   전체 랜덤(?mix=1): 같은 활동 페이지를 '이번 회차에 뽑힌 문제만' 보여 주는 모드로 재사용한다.
   저장 위치: localStorage "vhmx:<학교폴더>" = {round,used:[id..],cur:[{kind,part,act,qid,w}],done:{},open:{},cyc}
   기본은 남기기 — 맞춰도 자동으로 빠지지 않고, 학생이 오답노트에서 직접 '빼기'를 눌러야 빠진다. */
var WN=(function(){
  var seg=location.pathname.split('/'),i=seg.indexOf('h'),school=(i>=0&&seg[i+1])||'x',KEY='vhw:'+school;
  function load(){try{return JSON.parse(localStorage.getItem(KEY)||'[]')}catch(e){return[]}}
  function save(a){try{localStorage.setItem(KEY,JSON.stringify(a))}catch(e){}}
  var tt=0;
  function toast(n){
    if(!document.body||Date.now()-tt<4000)return;tt=Date.now();
    var d=document.createElement('a');d.href=base()+'wrong.html';
    d.textContent='오답 노트에 담았어요 (지금 '+n+'개) ›';
    d.style.cssText='position:fixed;left:50%;top:14px;transform:translateX(-50%);background:#b45309;color:#fff;padding:9px 16px;border-radius:999px;font:700 14px sans-serif;z-index:99999;text-decoration:none;box-shadow:0 4px 14px rgba(0,0,0,.25);transition:opacity .6s;white-space:nowrap';
    document.body.appendChild(d);setTimeout(function(){d.style.opacity=0},3200);setTimeout(function(){d.remove()},3900)}
  function base(){var p=location.pathname,k=p.indexOf('/'+school+'/');return k>=0?p.slice(0,k+school.length+2):'./'}
  var WR=/[?&]wrong=1\b/.test(location.search),MX=!WR&&/[?&]mix=1\b/.test(location.search),MKEY='vhmx:'+school;
  function mxLoad(){try{var o=JSON.parse(localStorage.getItem(MKEY)||'null');return o&&o.cur?o:null}catch(e){return null}}
  function mxSave(o){try{localStorage.setItem(MKEY,JSON.stringify(o))}catch(e){}}
  var MS=MX?mxLoad():null;
  function here(){var p=location.pathname,k=(/\/(L\d+|mock)\//.exec(p)||[])[1]||'',f=p.split('/').pop().replace('.html','');
    var a={'vocab':'voc','find':'find','awkward-test':'awk','eobeop-test':'eobeop','sunseo-ko':'ko','sunseo-abc':'abc','sunseo-mun':'mun','blank':'blank'}[f];
    var m=/[?&]part=(\d+)/.exec(location.search);return{kind:k,part:m?+m[1]:0,act:a}}
  function mxPick(kind,part,act){return ((MS&&MS.cur)||[]).filter(function(x){return x.kind===kind&&x.part===part&&x.act===act})}
  if(MX){var go=function(){[].forEach.call(document.querySelectorAll('a.back'),function(a){a.href=base()+'mix.html';a.textContent='← 전체 랜덤'})};
    if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',go);else go()}
  return{
    MODE:WR||MX,
    MIX:MX,
    /* 이어 풀기 기록 키 꼬리: 오답 다시 풀기 ':w', 전체 랜덤 ':m<회차>', 평소 '' */
    SUF:WR?':w':MX?':m'+(MS?MS.round:0):'',
    mixRound:function(){return MS?MS.round:0},
    /* 이 묶음을 다 풀었다고 표시(활동 페이지가 끝났을 때 부른다) */
    finish:function(){if(!MX)return;var s=mxLoad(),h=here();if(!s||!h.act)return;var k=h.kind+'|'+h.part+'|'+h.act;s.done=s.done||{};if(s.done[k])return;s.done[k]=1;mxSave(s)},
    mixNote:function(fin){if(fin)WN.finish();return'<b>전체 랜덤 '+WN.mixRound()+'회차</b> · 이번 회차에 뽑힌 문제만 보여요. <a href="'+base()+'mix.html" style="color:#0f766e;text-decoration:underline">전체 랜덤으로 ›</a>'+(fin?'<div style="margin-top:6px">이 묶음을 다 풀었어요. 틀린 문제는 <a href="'+base()+'wrong.html" style="color:#0f766e;text-decoration:underline">오답 노트</a>에 담겨요.</div>':'')},
    mixInfo:function(){return'<div class="how" style="border-color:#b45309"><b>전체 랜덤 '+WN.mixRound()+'회차</b> · 이번 회차에 뽑힌 지문으로 문제를 새로 풀어요. <a href="'+base()+'mix.html">전체 랜덤으로 ›</a></div>'},
    mixSum:function(){WN.finish();return'<p class="wn-l" style="margin:12px 0 0;font-size:14px">이 묶음을 다 풀었어요. 틀린 문제는 <a href="'+base()+'wrong.html">오답 노트</a>에 담겨요.<br><a href="'+base()+'mix.html">전체 랜덤으로 돌아가기 ›</a></p>'},
    /* 전체 랜덤 현황(MIXPOOL 이 있을 때): 회차, 전체/남은 문항 */
    mixStat:function(){var s=mxLoad(),P=window.MIXPOOL,tot=0,use={};if(s)(s.used||[]).forEach(function(i){use[i]=1});var left=0;
      if(P)P.units.forEach(function(u){tot+=u[4];if(!use[u[0]+':'+u[1]+':'+u[2]+':'+u[3]])left+=u[4]});
      var ks={},nd=0;((s&&s.cur)||[]).forEach(function(x){ks[x.kind+'|'+x.part+'|'+x.act]=1});Object.keys(ks).forEach(function(k){if(!(s.done&&s.done[k]))nd++});
      return{round:s?s.round:0,total:tot,left:left,bundles:Object.keys(ks).length,undone:nd}},
    school:school,
    list:function(){return load()},
    count:function(){return load().length},
    id:function(kind,part,act,qid){return kind+':'+part+':'+act+':'+qid},
    has:function(kind,part,act,qid){var id=WN.id(kind,part,act,qid);return load().some(function(x){return x.id===id})},
    /* it = {kind,part,act,qid,label,q?}  이미 있으면 그대로 둔다 */
    add:function(it){var a=load();it.id=WN.id(it.kind,it.part,it.act,it.qid);
      if(a.some(function(x){return x.id===it.id}))return;
      it.t=Date.now();a.push(it);save(a);toast(a.length)},
    remove:function(id){save(load().filter(function(x){return x.id!==id}))},
    /* 오답 다시 풀기 모드(?wrong=1)에서 이 활동·구간에 담긴 문제 id 목록 */
    ids:function(kind,part,act){if(MX)return mxPick(kind,part,act).map(function(x){return x.qid});return load().filter(function(x){return x.kind===kind&&x.part===part&&x.act===act}).map(function(x){return x.qid})},
    items:function(kind,part,act){if(MX)return mxPick(kind,part,act);return load().filter(function(x){return x.kind===kind&&x.part===part&&x.act===act})}
  }
})();
