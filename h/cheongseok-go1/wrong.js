/* 오답 노트: 틀린 문제를 이 기기(브라우저)에 모아 두고, 모아서 다시 풀게 한다.
   저장 위치: localStorage "vhw:<학교폴더>" = [{id,kind,part,act,qid,label,t,q?}]
   kind: 'L4' | 'mock' | ..., act: voc|find|awk|eobeop|ko|abc|mun|blank
   qid : 활동 안에서 그 문제를 가리키는 값(문자열). voc 은 문제 전체를 q 에 저장.
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
  return{
    MODE:/[?&]wrong=1\b/.test(location.search),
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
    ids:function(kind,part,act){return load().filter(function(x){return x.kind===kind&&x.part===part&&x.act===act}).map(function(x){return x.qid})},
    items:function(kind,part,act){return load().filter(function(x){return x.kind===kind&&x.part===part&&x.act===act})}
  }
})();
