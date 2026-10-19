/* 덩어리(part): ?part=N 으로 각 활동 페이지가 자기 범위만 보여 준다.
   교과서 4과 : 1=본문 ❶❷❸ 2=❹❺ (L4 폴더 페이지)
   모의고사   : 1~10=1회독(하루 3지문) 11~15=2회독(하루 6지문) (mock 폴더 페이지)
   기록 키    : "<구간>p<번호>:<활동>"  예) L4p1:ko, mockp12:abc */
var PARTS={
  /* 주성고1 능률(오) 공통영어2: 지문 id z1~zN. 4과 5지문→2덩어리, 3과 6지문→4덩어리 */
  L4:{1:['z1','z2','z3'],2:['z4','z5']},
  L3:{1:['z1','z2'],2:['z3'],3:['z4','z5'],4:['z6']},
  names:{L4:{1:'본문 1~3',2:'본문 4~5'},L3:{1:'본문 1~2',2:'본문 3',3:'본문 4~5',4:'본문 6'}}
};
var PART=(function(){var m=/[?&]part=(1[0-5]|[1-9])\b/.exec(location.search);return m?+m[1]:0})();
/* 패시지 id가 이 덩어리에 속하는지. kind: 'L4' 또는 'mock' */
function inPart(kind,pid,part){part=part||PART;if(!part)return true;
  if(kind==='L4'||kind==='L3')return PARTS[kind][part].indexOf(pid)>=0;
  return PARTS.mock[part].indexOf(String(pid))>=0}
function partKey(kind){return PART?kind+'p'+PART:kind}

/* 걸린 시간: 활동을 끝내 PG.mark 가 불리면 "걸린 시간"을 잠깐 띄운다. (화면을 보고 있고 최근 1분 안에 만진 시간만 센다) */
(function(){
  if(window.NOTIMER)return;
  var TK='vhtm:'+location.pathname+':'+PART,act=0,last=Date.now(),shown=0;
  function ld(){try{return +localStorage.getItem(TK)||0}catch(e){return 0}}
  function sv(v){try{localStorage.setItem(TK,String(v))}catch(e){}}
  ['click','keydown','touchstart','scroll'].forEach(function(ev){addEventListener(ev,function(){last=Date.now()},true)});
  var base=ld();
  setInterval(function(){if(document.visibilityState==='visible'&&Date.now()-last<60000){act++;if(act%5===0)sv(base+act)}},1000);
  function fmt(s){return (s>=60?Math.floor(s/60)+'분 ':'')+(s%60)+'초'}
  addEventListener('load',function(){
    if(window.NOTIMER||typeof PG==='undefined')return;var m=PG.mark;
    PG.mark=function(k){m.apply(PG,arguments);if(shown||window.NOTIMER)return;shown=1;var t=base+act;try{localStorage.setItem('vhd:'+k,String(t))}catch(e){}sv(0);base=0;act=0;
      var d=document.createElement('div');d.textContent='걸린 시간 '+fmt(t);d.style.cssText='position:fixed;left:50%;bottom:84px;transform:translateX(-50%);background:#1e2a44;color:#fff;padding:11px 18px;border-radius:999px;font:700 15px sans-serif;z-index:99999;box-shadow:0 4px 14px rgba(0,0,0,.25);transition:opacity .6s';
      document.body.appendChild(d);setTimeout(function(){d.style.opacity=0},5500);setTimeout(function(){d.remove();shown=0},6200)}
  })
})();
