/* 공용폰 모드: 주소 끝에 ?shared=1 로 들어오면 기록을 이 탭에만 임시로 저장한다(새로 들어오거나 탭을 닫으면 비움). 이 표시가 없으면 아무 일도 하지 않는다. */
(function(){try{
  var ss=window.sessionStorage;
  if(/[?&]shared=1(&|$)/.test(location.search)){
    var nv=((window.performance&&performance.getEntriesByType&&performance.getEntriesByType('navigation'))||[])[0];
    if(!nv||nv.type==='navigate'){for(var i=ss.length-1;i>=0;i--){var k=ss.key(i);if(k&&(k.indexOf('S:')===0||k==='wq'))ss.removeItem(k)}}
    ss.setItem('vhshared','1');
  }
  if(ss.getItem('vhshared')!=='1')return;
  var P=Storage.prototype,g=P.getItem,s=P.setItem,r=P.removeItem,L=window.localStorage;
  function ok(t,k){return t===L&&typeof k==='string'&&k.indexOf('vh')===0}
  P.getItem=function(k){return ok(this,k)?g.call(ss,'S:'+k):g.call(this,k)};
  P.setItem=function(k,v){return ok(this,k)?s.call(ss,'S:'+k,v):s.call(this,k,v)};
  P.removeItem=function(k){return ok(this,k)?r.call(ss,'S:'+k):r.call(this,k)};
}catch(e){}})();
/* 학생 기록: 이 폰(브라우저)에만 저장. 키 = "구간:활동" 예) L4:ko, mock:abc */
var PG=(function(){
  var seg=location.pathname.split('/'),i=seg.indexOf('h'),school=(i>=0&&seg[i+1])||'x',KEY='vhp:'+school;
  function load(){try{return JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){return{}}}
  function save(o){try{localStorage.setItem(KEY,JSON.stringify(o))}catch(e){}}
  return{
    get:function(){return load()},
    n:function(k){return (load()[k]||{}).n||0},
    mark:function(k){if(!k)return;var o=load(),e=o[k]||{n:0};e.n++;e.t=Date.now();o[k]=e;save(o)},
    unmark:function(k){var o=load();delete o[k];save(o)},
    /* 직접 기록 버튼이 필요한 쪽(정답지·별도 활동지)에 붙이는 작은 버튼 */
    bar:function(k,label){
      var b=document.createElement('button');b.type='button';
      function paint(){var n=PG.n(k);b.textContent=n?('✓ '+label+' · '+n+'번 했어요 (한 번 더 +1)'):('✓ '+label);b.style.background=n?'#1d4ed8':'#fff';b.style.color=n?'#fff':'#1d4ed8'}
      b.style.cssText='position:fixed;left:12px;bottom:12px;bottom:calc(12px + env(safe-area-inset-bottom));z-index:9999;border:1.5px solid #1d4ed8;border-radius:999px;padding:11px 15px;font:700 13px/1 sans-serif;cursor:pointer';
      b.onclick=function(){PG.mark(k);paint()};paint();document.body.appendChild(b)}
  }
})();
