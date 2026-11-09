import re,json
T=open('page_template.html',encoding='utf-8').read()
D=json.load(open('q_full.json',encoding='utf-8'))
def rep(old,new,cnt=1):
    global T
    assert T.count(old)>=1,old[:60]
    T=T.replace(old,new) if cnt==0 else T.replace(old,new,1)
# head
rep('<title>4과 요약문 완성 ❶ · 샘플</title>','<title>4과 요약문 연습 ❶ · 금천고1</title>')
rep('<meta charset="utf-8">','<meta charset="utf-8"><script src="../../common/base.js?v=261105a"></script>')
# WN client (from minimock 02a)
src=open('/home/claude/via-high/h/minimock/h2/02a.html',encoding='utf-8').read()
a=src.index('(function(W){\n  if(W.WN)return;'); b=src.index('})(window);',a)+len('})(window);')
wn=src[a:b]
assert 'gate:gate,flush:flush,name:name}' in wn
wn=wn.replace('gate:gate,flush:flush,name:name}','gate:gate,flush:flush,name:name,list:function(){var n=name();if(!n)return Promise.resolve(null);return flush().then(function(){return post({act:"list",name:n,pin:PIN})}).catch(function(){return null})}}')
wn=wn.replace("if(!W.WN)","")
WNS='<script>\n'+wn+'\nif(!WN.name())WN.gate(function(){location.reload()});\n</script>\n'
rep('<script>\nvar DATA=__DATA__;',WNS+'<script>\nvar DATA=__DATA__;')
# keys
rep("var NOTES=jget(K_NOTE,{}), ASK=jget(K_ASK,{}), PR=jget(K_PROG,{a:{}});","var NOTES=jget(K_NOTE,{}), PR=jget(K_PROG,{a:{}}), SRV={}, SRC='요약문 완성', PUSHED=jget('vhvs:'+SCH,{});")
rep("var K_NOTE='vhv:'+SCH, K_ASK='vhvq:'+SCH, K_PROG='vhvp:'+SCH;","var K_NOTE='vhv:'+SCH, K_PROG='vhvp:'+SCH;")
# push on tap
rep("n.c=(n.c||0)+1;n.t=Date.now();n.q=curQ;NOTES[id]=n;jset(K_NOTE,NOTES);",
 "n.c=(n.c||0)+1;n.t=Date.now();n.q=curQ;NOTES[id]=n;jset(K_NOTE,NOTES);\n  if(!PUSHED['w:'+id]){PUSHED['w:'+id]=1;jset('vhvs:'+SCH,PUSHED);try{WN.add([{w:lem,m:g[1],src:SRC,how:'탭',ask:true}])}catch(e){}}")
# ask handler -> removed; rv pushes swap
a=T.index("  else if(act==='ask'){"); b=T.index("  else if(act==='chk'){go('chk')}")
T=T[:a]+T[b:]
rep("  else if(act==='teach')go('teach');\n","")
rep("  else if(act==='tab'){tTab=v;render()}\n","")
rep("else if(act==='rv'){swOpen[v]=!swOpen[v];render()}",
 "else if(act==='rv'){swOpen[v]=!swOpen[v];if(swOpen[v])pushSw(v);render()}")
rep("else if(act==='rvall'){var o=v==='open';swList().forEach(function(s){if(o)swOpen[s.id]=true;else delete swOpen[s.id]});render()}",
 "else if(act==='rvall'){var o=v==='open';swList().forEach(function(s){if(o){swOpen[s.id]=true;pushSw(s.id)}else delete swOpen[s.id]});render()}")
rep("function swList(){","""function pushSw(id){
  if(String(id).indexOf('c')===0&&!/^sw:/.test(id))return;
  var s=swList().filter(function(x){return x.id===id})[0];if(!s||PUSHED[id])return;
  PUSHED[id]=1;jset('vhvs:'+SCH,PUSHED);
  try{WN.add([{w:s.a,m:s.k+' → '+s.b,src:SRC,how:'바꿔 말하기',ask:true}])}catch(e){}
}
function swList(){""")
rep("else h=vTeach();","else h=vHome();")
# home: remove teach button, flag count from server
rep('<button data-a="teach">선생님 화면 (미리보기)</button>','')
rep('<span class="tag">샘플 · 금천고1</span>','<span class="tag">금천고1</span>')
# srv-based flags
a=T.index("function nFlag(){"); b=T.index("function sceneLine(")
NEW='''function sk(id){return id.indexOf('sw:')===0?id.slice(3):id}
function wrongOf(id){var r=SRV[sk(id).toLowerCase()];return r&&r.c>0?r.c:0}
function flagList(){return Object.keys(SRV).map(function(k){return SRV[k]}).filter(function(r){return r.c>0}).sort(function(a,b){return b.c-a.c})}
function nFlag(){return flagList().length}
function srvLoad(){
  try{WN.list().then(function(r){
    if(!r||!r.ok||!r.items)return;SRV={};
    r.items.forEach(function(i){if(String(i.src||'').indexOf(SRC)>=0)SRV[String(i.w).toLowerCase()]={w:i.w,m:i.m,c:i.c||0}});
    if(view==='home'||view==='chk'||view==='sw')render();
  })}catch(e){}
}
function vChk(){
  var L=flagList();
  var h='<div class="top"><button class="back" data-a="home">목록</button><span class="cnt">선생님 확인 단어 '+L.length+'개</span></div>';
  if(!L.length)return h+'<div class="empty">틀린 단어가 없어요.</div>';
  h+='<p class="hint">선생님이 물어봤을 때 틀린 단어예요. 먼저 뜻을 떠올려 보고 확인해 보세요. 오답노트(H로드맵)에도 같이 있어요.</p><div class="card">';
  L.forEach(function(r){
    var id=r.w.toLowerCase(),o=swOpen['c'+id];
    h+='<div class="swr"><div class="swq"><span class="sa">'+esc(r.w)+'</span><span class="sb">'+(o?'<em>'+esc(r.m)+'</em>':'뜻은?')+'</span><small class="flag">'+r.c+'번 틀림</small><button data-a="rv" data-v="c'+esc(id)+'">'+(o?'가리기':'확인')+'</button></div></div>';
  });
  return h+'</div><a class="btn sec" style="display:block;text-align:center;text-decoration:none" href="https://nolbada.github.io/via/wn/">H로드맵 오답노트 열기</a>';
}
'''
T=T[:a]+NEW+T[b:]
rep("fl=ASK[s.id]&&ASK[s.id].r==='x';","fl=wrongOf(s.id);")
rep("(fl?'<small class=\"flag\">다시 확인</small>':'')","(fl?'<small class=\"flag\">'+fl+'번 틀림</small>':'')")
# remove tSwaps & vTeach
a=T.index("function tSwaps(){"); b=T.index("render();\n</script>")
T=T[:a]+T[b:]
rep("var swOpen={},swD={},tTab='words';","var swOpen={},swD={};")
T=T.replace("render();\n</script>","render();srvLoad();window.addEventListener('pageshow',srvLoad);\n</script>",1) if T.count("render();\n</script>")==1 else T
open('real_body.html','w',encoding='utf-8').write(T)
out=T.replace('__DATA__',json.dumps(D,ensure_ascii=False))
open('yoyak-lian.html','w',encoding='utf-8').write(out)
print(len(out))
