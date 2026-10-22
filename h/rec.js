/* REC: 고등 학생 기록을 기기 간에 잇는 공용 스크립트. 고1 개인 링크(gimal)=개인 코드, 고1 공용 링크(go1)와 고2(go2)=이름+6900.
   기존 구글 시트 서버(HUB.sync와 같은 주소·같은 요청 형식)를 쓰고, id는 REC 로 시작해 허브 기록과 섞이지 않는다. */
(function(){
  var W=window,D=document,P=location.pathname;
  var m=/\/h\/(geumcheon|jusung|cheongseok)-(gimal|go1|go2)\//.exec(P);
  if(!m||W.__rec)return;
  W.__rec=1;
  var URL_=W.REC_URL||'https://script.google.com/macros/s/AKfycbw1YQfKsgAXNk8NYoxOfz4bsCSy66fiim7HoFAUk162ksxrEbmspMs2UifNZ-93sdf05A/exec';
  var KIND=m[2],SCH=m[1],NUM='6900';
  var CODEKEY={geumcheon:'gk26-code',jusung:'js26-code',cheongseok:'cs26-code'}[SCH];
  var UK='rec_uid',MK='rec_meta',NK='rec_name',AK='rec_at',MAXV=45000;
  var LS=null;try{LS=W.localStorage;LS.getItem('x')}catch(e){return}
  function g(k){try{return LS.getItem(k)}catch(e){return null}}
  function s(k,v){try{LS.setItem(k,v)}catch(e){}}
  function d(k){try{LS.removeItem(k)}catch(e){}}
  function jg(k){try{return JSON.parse(g(k)||'null')}catch(e){return null}}
  function mirrored(k){
    if(!k||typeof k!=='string')return false;
    if(k.indexOf('rec_')===0||k.indexOf('hub_')===0||k.indexOf('mogo')===0)return false;
    if(/-code$/.test(k)||/teacher/i.test(k))return false;
    return true;
  }
  function keys(){var o=[],i,k;for(i=0;i<LS.length;i++){k=LS.key(i);if(mirrored(k))o.push(k)}return o}
  function ident(){
    if(KIND==='gimal'){var c=(g(CODEKEY)||'').toLowerCase();return /^[a-z0-9]{3,12}$/.test(c)?'REC|'+c:''}
    var n=(g(NK)||'').replace(/\s+/g,'');return n?'REC|'+KIND+'|'+n+'|'+NUM:'';
  }
  function dm(a,b){
    if(a===b)return a;
    var ta=typeof a,tb=typeof b,o,k;
    if(ta==='number'&&tb==='number')return Math.max(a,b);
    if(ta==='boolean'&&tb==='boolean')return a||b;
    if(Array.isArray(a)&&Array.isArray(b)){var seen={};o=[];a.concat(b).forEach(function(x){var t=JSON.stringify(x);if(!seen[t]){seen[t]=1;o.push(x)}});return o}
    if(a&&b&&ta==='object'&&tb==='object'&&!Array.isArray(a)&&!Array.isArray(b)){
      o={};for(k in a)o[k]=(k in b)?dm(a[k],b[k]):a[k];for(k in b)if(!(k in a))o[k]=b[k];return o}
    return b;
  }
  function merge(loc,rem){try{return JSON.stringify(dm(JSON.parse(loc),JSON.parse(rem)))}catch(e){return rem}}
  function post(body,keep){
    return fetch(URL_,{method:'POST',headers:{'Content-Type':'text/plain'},body:JSON.stringify(body),keepalive:!!keep})
      .then(function(r){return r.json()}).then(function(r){if(!r||!r.ok)throw new Error('rec');return r});
  }
  function unwrap(v){return(v&&typeof v==='object'&&typeof v.s==='string')?v.s:null}
  var busy=false,again=false;
  /* 바뀐 키만 올림 */
  function pending(skip){
    var meta=jg(MK)||{},ch={},sent={};
    keys().forEach(function(k){
      var v=g(k);if(v===null||v.length>MAXV||(skip&&skip[k]))return;
      if(meta[k]!==v){ch[k]={v:{s:v},t:Date.now()};sent[k]=v}
    });
    return {ch:ch,sent:sent,n:Object.keys(sent).length};
  }
  function push(id,keep,skip){
    var c=pending(skip);if(!c.n)return Promise.resolve(false);
    return post({act:'put',id:id,data:c.ch},keep).then(function(){
      var meta=jg(MK)||{},k;for(k in c.sent)meta[k]=c.sent[k];s(MK,JSON.stringify(meta));return true});
  }
  /* 받아서 반영(apply) 후 올림 */
  function sync(id,apply){
    if(busy){again=true;return Promise.resolve(false)}busy=true;
    return post({act:'put',id:id,data:{}}).then(function(r){
      var rem=r.data||{},meta=jg(MK)||{},rl=false,skip={},k;
      for(k in rem){
        var rs=unwrap(rem[k].v);if(rs===null)continue;
        var lv=g(k);
        if(lv===rs){meta[k]=rs;continue}
        if(lv===null){if(apply){s(k,rs);meta[k]=rs;rl=true}continue}
        var lchg=meta[k]!==lv;
        if(!lchg){if(apply){s(k,rs);meta[k]=rs;rl=true}}
        else if(meta[k]!==rs){
          s(k,merge(lv,rs));rl=true;
        }
      }
      s(MK,JSON.stringify(meta));s(AK,String(Date.now()));
      return push(id,false,skip).then(function(){busy=false;if(again){again=false;sched()}return rl},function(){busy=false;return rl});
    },function(e){busy=false;throw e});
  }
  function wipe(){keys().forEach(d);d(MK)}
  function reloadOnce(){
    try{var t=Number(sessionStorage.getItem('rec_rl')||0);if(Date.now()-t>20000){sessionStorage.setItem('rec_rl',String(Date.now()));location.reload()}}catch(e){}
  }
  var timer=null;
  function sched(){
    if(timer)return;
    timer=setTimeout(function(){timer=null;var id=ident();if(id&&id===g(UK))sync(id,false).then(function(rl){if(rl)reloadOnce()}).catch(function(){})},4000);
  }
  /* 저장이 일어나면 잠시 뒤 올림 */
  try{
    var sp=W.Storage.prototype,os=sp.setItem;
    sp.setItem=function(k){os.apply(this,arguments);if(this===LS&&mirrored(k))sched()};
  }catch(e){}
  function start(){
    var id=ident();if(!id)return;
    var prev=g(UK);
    var first=function(){
      s(UK,id);d(MK);
      return sync(id,true).then(function(rl){if(rl)reloadOnce()}).catch(function(){});
    };
    if(prev&&prev!==id){
      /* 공용 기기에서 다른 학생이 들어옴: 이전 학생 기록을 올리고 지운 뒤 새 학생 기록을 받는다 */
      push(prev,false).catch(function(){}).then(function(){wipe();return first()}).then(function(){reloadOnce()});
      return;
    }
    if(!prev){first();return}
    var last=Number(g(AK)||0);
    if(Date.now()-last>45000)sync(id,true).then(function(rl){if(rl)reloadOnce()}).catch(function(){});
    else sync(id,false).then(function(rl){if(rl)reloadOnce()}).catch(function(){});
    setInterval(function(){if(!D.hidden)sync(id,false).then(function(rl){if(rl)reloadOnce()}).catch(function(){})},60000);
    var hid=0;
    D.addEventListener('visibilitychange',function(){
      if(D.hidden){hid=Date.now();push(id,true).catch(function(){})}
      else if(hid&&Date.now()-hid>30000){sync(id,true).then(function(rl){if(rl)reloadOnce()}).catch(function(){})}
    });
    W.addEventListener('pagehide',function(){push(id,true).catch(function(){})});
  }
  /* go1·go2: 이름 입력 카드 (첫 화면에서만) */
  function mountCard(){
    if(KIND==='gimal')return;
    if(!/\/(index\.html)?$/.test(P)||!/-(go1|go2)\/(index\.html)?$/.test(P))return;
    var host=D.querySelector('.wrap')||D.body;if(!host)return;
    var name=g(NK),box=D.createElement('div');
    box.style.cssText='margin:12px 16px;padding:12px 14px;border:1px solid var(--line,#dbe4e1);border-radius:12px;background:var(--card,#fff);color:var(--ink,#16211f);font-size:15px;display:flex;gap:8px;align-items:center;flex-wrap:wrap';
    if(!name){
      box.innerHTML='<b style="flex:1 1 100%">이름</b><input id="rec-n" type="text" autocomplete="off" placeholder="이름" style="flex:1;min-width:120px;font-size:16px;padding:9px 10px;border:1px solid var(--line,#dbe4e1);border-radius:8px;background:transparent;color:inherit"><button id="rec-b" type="button" style="font-size:15px;font-weight:700;padding:9px 16px;border:0;border-radius:8px;background:var(--pri,#1d4ed8);color:#fff">시작</button><div id="rec-m" style="flex:1 1 100%;font-size:13px;color:var(--sub,#5a6b67)"></div>';
      host.insertBefore(box,host.firstChild);
      D.getElementById('rec-b').onclick=function(){
        var v=(D.getElementById('rec-n').value||'').replace(/\s+/g,'');
        if(!v){D.getElementById('rec-m').textContent='이름을 적어 주세요.';return}
        var b=this;b.disabled=true;D.getElementById('rec-m').textContent='기록을 불러오는 중...';
        var prevId=g(UK);
        var go=function(){
          s(NK,v);var id=ident();
          if(prevId&&prevId!==id){wipe()}
          s(UK,id);d(MK);
          sync(id,true).then(function(){location.reload()},function(){d(NK);d(UK);b.disabled=false;D.getElementById('rec-m').textContent='연결이 안 됐어요. 인터넷을 확인하고 다시 눌러 주세요.'});
        };
        if(prevId&&prevId!==('REC|'+KIND+'|'+v+'|'+NUM))push(prevId,false).catch(function(){}).then(go);else go();
      };
    }else{
      box.innerHTML='<span style="flex:1"><b>'+name.replace(/[<>&"]/g,'')+'</b> 기록 저장 중</span><button id="rec-x" type="button" style="font-size:13px;padding:7px 12px;border:1px solid var(--line,#dbe4e1);border-radius:8px;background:transparent;color:inherit">다른 이름으로</button>';
      host.insertBefore(box,host.firstChild);
      D.getElementById('rec-x').onclick=function(){
        var b=this,id=g(UK);b.disabled=true;b.textContent='저장하는 중...';
        (id?push(id,false):Promise.resolve()).then(function(){wipe();d(NK);d(UK);location.reload()},function(){b.disabled=false;b.textContent='저장이 안 됐어요. 다시 눌러 주세요'});
      };
    }
  }
  W.REC={id:ident,sync:function(){var id=ident();return id?sync(id,true):Promise.resolve(false)}};
  function ready(){start();mountCard()}
  if(D.readyState==='complete')ready();else W.addEventListener('load',ready);
})();
