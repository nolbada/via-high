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
