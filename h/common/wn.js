(function(W){
  if(W.WN)return;
  var TM=/[?&]t=1(&|$)/.test(W.location.search);if(TM){W.TEACHER_MODE=true;try{W.document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;var u=a.getAttribute('href')||'';if(/(^index\.html$)|(\/via\/wn\/$)|(^\d\d[ab]\.html$)/.test(u)){var cm=/[?&]c=([AB])(&|$)/.exec(W.location.search);a.setAttribute('href',u+'?t=1'+(cm?'&c='+cm[1]:''))}},true)}catch(x){}}var URL_=TM?'https://script.google.com/macros/s/AKfycbz0OolJAHbhYzjWxOkRY851Sn1-ZKL3JOYf4eWancUEotJsm4-z6aWzcm-71I9CIWyR/exec':(W.WN_URL||'https://script.google.com/macros/s/AKfycbzc2ei1hfWwFPviIFZndCLPchR7NRlrUtY9IqZ6mL2sruJxshFJMpGaKp3LeHHUEl6Apg/exec'),PIN='6900',QK='wn_q',HK='wn_hq';
  function ls(){try{return W.localStorage}catch(e){return null}}
  function g(k){var l=ls();try{return l&&l.getItem(k)}catch(e){return null}}
  function s(k,v){var l=ls();try{l&&l.setItem(k,v)}catch(e){}}
  function name(){if(TM)return'신유정'+((/[?&]c=([AB])(&|$)/.exec(W.location.search)||[])[1]||'');return(g('wn_name')||g('recm_name')||g('rec_name')||'').replace(/\s+/g,'')}
  function jq(k){try{return JSON.parse(g(k)||'[]')}catch(e){return[]}}
  function post(b){return fetch(URL_,{method:'POST',headers:{'Content-Type':'text/plain'},body:JSON.stringify(b),keepalive:true}).then(function(r){return r.json()})}
  var busy=false,again=false;
  function flush(){
    var n=name(),Q=jq(QK),H=jq(HK);
    if(busy){again=true;return Promise.resolve(false)}
    if(!n||(!Q.length&&!H.length))return Promise.resolve(false);
    busy=true;var p=Promise.resolve();
    if(Q.length){var items=[];Q.forEach(function(b){items=items.concat(b)});
      p=p.then(function(){return post({act:'add',name:n,pin:PIN,items:items}).then(function(r){if(r&&r.ok)s(QK,JSON.stringify(jq(QK).slice(Q.length)))})})}
    H.forEach(function(h){p=p.then(function(){return post({act:'hw',name:n,pin:PIN,level:h.level,day:h.day,score:h.score}).then(function(r){if(r&&r.ok)s(HK,JSON.stringify(jq(HK).filter(function(x){return!(x.level===h.level&&x.day===h.day&&x.score===h.score)})))})})});
    return p.then(function(){busy=false;if(again){again=false;flush()}return true},function(){busy=false;again=false;return false});
  }
  function gate(cb){
    if(name()){cb();flush();return}
    var d=document.createElement('div');
    d.style.cssText='position:fixed;inset:0;z-index:99999;background:Canvas;color:CanvasText;display:flex;align-items:center;justify-content:center;padding:20px;font-family:-apple-system,"Apple SD Gothic Neo","Noto Sans KR","Malgun Gothic",system-ui,sans-serif';
    d.innerHTML='<div style="width:100%;max-width:420px"><div style="font-size:22px;font-weight:800;margin-bottom:12px">이름</div><input id="wng" type="text" autocomplete="off" style="width:100%;font-size:18px;padding:12px;border:1px solid #8885;border-radius:12px;background:Canvas;color:CanvasText"><button id="wnb" style="width:100%;margin-top:10px;padding:13px;border:0;border-radius:12px;font-size:16px;font-weight:700;background:#2f7d5b;color:#fff">시작</button><div id="wnm" style="margin-top:8px;font-size:14px;opacity:.7;min-height:20px"></div></div>';
    document.body.appendChild(d);
    var b=d.querySelector('#wnb'),m=d.querySelector('#wnm'),i=d.querySelector('#wng');
    function go(){var v=(i.value||'').replace(/\s+/g,'');if(!v)return;b.disabled=true;m.textContent='확인 중...';
      post({act:'list',name:v,pin:PIN}).then(function(r){
        if(r&&r.ok){s('wn_name',v);d.remove();cb();flush()}
        else{b.disabled=false;m.textContent='등록된 이름이 아니에요.'}
      },function(){b.disabled=false;m.textContent='연결이 안 됐어요. 인터넷을 확인해 주세요.'})}
    b.onclick=go;i.onkeydown=function(e){if(e.key==='Enter')go()};i.focus();
  }
  function DEL(w,src){var k=String(w||'').toLowerCase().trim(),hit=false;
    if(!busy){var Q=jq(QK).map(function(b){return b.filter(function(it){var m=String(it.w||'').toLowerCase().trim()===k&&it.src===src;if(m)hit=true;return!m})}).filter(function(b){return b.length});if(hit){s(QK,JSON.stringify(Q));return Promise.resolve({ok:true,removed:true})}}
    var n=name();if(!n)return Promise.resolve(null);
    function go(){return post({act:'del',name:n,pin:PIN,w:w,src:src})}
    return flush().then(go).then(function(r){if(r&&r.ok&&r.removed===false&&r.reason==='none')return new Promise(function(z){setTimeout(z,3000)}).then(go);return r}).catch(function(){return null})}
  W.WN={add:function(items){
    if(!items||!items.length)return Promise.resolve(false);
    var Q=jq(QK);Q.push(items);s(QK,JSON.stringify(Q));return flush();
  },hw:function(level,day,score){
    var H=jq(HK);H.push({level:level,day:day,score:score});s(HK,JSON.stringify(H));return flush();
  },del:DEL,gate:gate,flush:flush,name:name,list:function(){var n=name();if(!n)return Promise.resolve(null);return flush().then(function(){return post({act:"list",name:n,pin:PIN})}).catch(function(){return null})}};
  flush();
})(window);
