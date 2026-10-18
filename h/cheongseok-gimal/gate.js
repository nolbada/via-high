/* 청석고 홈 연결용: 앱이 끝났을 때 점수를 홈에 알린다. 같은 주소(origin)의 localStorage를 쓴다. (금천과 키가 겹치지 않게 cs26-) */
(function(){
  var RK='cs26-rep',HK='cs26-hwauto';
  function rd(k){try{return JSON.parse(localStorage.getItem(k)||'{}')||{}}catch(e){return {}}}
  function wr(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
  window.GK={
    /* id 예: 'L3-find'. pct: 0~100 정수. 한 번 끝낼 때마다 한 번만 부른다. */
    report:function(id,pct){
      pct=Math.max(0,Math.min(100,Math.round(+pct||0)));
      var r=rd(RK),o=r[id]||{pct:0,last:0,tries:0};
      o.last=pct;o.pct=Math.max(o.pct||0,pct);o.tries=(o.tries||0)+1;o.t=Date.now();
      r[id]=o;wr(RK,r);return o
    },
    /* 숙제 세트 하나를 끝까지 돌렸을 때 한 번 부른다. id 예: 'L3-blank' */
    hw:function(id){
      var h=rd(HK);h[id]=(h[id]||0)+1;wr(HK,h);return h[id]
    }
  }
})();
