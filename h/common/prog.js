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
    /* 실수로 누른 확인 취소: 2번 이상이면 1번 줄이고, 1번이면 기록을 지운다 */
    dec:function(k){var o=load(),e=o[k];if(!e)return;if((e.n||0)>1){e.n--;o[k]=e}else delete o[k];save(o)},
    /* 직접 기록 버튼이 필요한 쪽(정답지·별도 활동지)에 붙이는 작은 버튼 */
    bar:function(k,label){
      var w=document.createElement('div'),b=document.createElement('button'),c=document.createElement('button');
      b.type='button';c.type='button';
      function paint(){var n=PG.n(k);b.textContent=n?('✓ '+label+' · '+n+'번'):('✓ '+label);b.style.background=n?'#1d4ed8':'#fff';b.style.color=n?'#fff':'#1d4ed8';c.style.display=n?'inline-block':'none';c.textContent=n>1?'\u22121':'취소'}
      w.style.cssText='position:fixed;left:12px;bottom:12px;bottom:calc(12px + env(safe-area-inset-bottom));z-index:9999;display:flex;gap:6px;align-items:center';
      b.style.cssText='border:1.5px solid #1d4ed8;border-radius:999px;padding:11px 15px;font:700 13px/1 sans-serif;cursor:pointer';
      c.style.cssText='border:1.5px solid #94a3b8;border-radius:999px;padding:11px 13px;font:700 13px/1 sans-serif;cursor:pointer;background:#fff;color:#475569';
      b.onclick=function(){PG.mark(k);paint()};c.onclick=function(){PG.dec(k);paint()};
      w.appendChild(b);w.appendChild(c);paint();document.body.appendChild(w);
      /* 오른쪽 아래 ⌂ 목록 버튼과 겹치지 않게 "빠른정답" 버튼을 위로 */
      function up(){var f=document.querySelector('a.fab');if(f){f.style.bottom='64px'}}
      up();document.addEventListener('DOMContentLoaded',up)}
  }
})();
/* 인라인 확인 버튼(핵심 7문장 분석 기본·심화): 옆에 취소 버튼을 붙인다 */
(function(){
  var m=/\/(L3|L4)\/(hk|hs)\//.exec(location.pathname);if(!m)return;var K='key:'+m[1]+':'+m[2];
  function go(){
    var bs=document.querySelectorAll('button'),b=null;
    for(var i=0;i<bs.length;i++){if(/^\u2713 확인했어요/.test(bs[i].textContent)){b=bs[i];break}}
    if(!b||b.dataset.dec)return;b.dataset.dec='1';
    var c=document.createElement('button');c.type='button';
    c.style.cssText='border:1.5px solid #94a3b8;border-radius:999px;padding:6px 11px;font:700 13px sans-serif;cursor:pointer;background:#fff;color:#475569;margin-left:6px';
    function paint(){var n=PG.n(K);c.style.display=n?'inline-block':'none';c.textContent=n>1?'\u22121':'취소'}
    c.onclick=function(){PG.dec(K);b.textContent=PG.n(K)?('\u2713 확인했어요 \u00b7 '+PG.n(K)+'번'):'\u2713 확인했어요';b.style.background=PG.n(K)?'#1d4ed8':'#fff';b.style.color=PG.n(K)?'#fff':'#1d4ed8';paint()};
    b.addEventListener('click',function(){setTimeout(paint,0)});
    b.parentNode.insertBefore(c,b.nextSibling);paint();
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',go);else go();
  window.addEventListener('load',go);
})();
/* REC 연동 불러오기 (고등 앱 폴더에서만 작동) */
(function(){try{if(window.__recl||!/\/h\/(geumcheon|jusung|cheongseok)-(gimal|go2)\//.test(location.pathname))return;window.__recl=1;var s=document.createElement('script');s.src=location.pathname.replace(/\/h\/.*$/,'/h/rec.js')+'?v=1';(document.head||document.documentElement).appendChild(s)}catch(e){}})();
