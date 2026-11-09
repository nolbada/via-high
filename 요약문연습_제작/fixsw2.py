import glob
OLD="function swList(){return (DATA.story||[]).map(function(s){return {a:s.a,form:s.form,b:s.b,k:s.k,id:'sw:'+s.a.toLowerCase(),n:s.n,sq:s.sq,sum:s.sum,hook:s.hook,en:s.en,ko:s.ko}})}"
NEW="""function swList(){
  var L=(DATA.story||[]).map(function(s){return {a:s.a,form:s.form,b:s.b,k:s.k,id:'sw:'+s.a.toLowerCase(),n:s.n,sq:s.sq,sum:s.sum,hook:s.hook,en:s.en,ko:s.ko}}),seen={};
  L.forEach(function(s){seen[s.a.toLowerCase()]=1});
  /* 모든 문제의 '이 단어, 이렇게 바뀌었어요' 단어도 빠짐없이 바꿔 말하기 연습에 넣는다 */
  Qs.forEach(function(q,qi){(q.swaps||[]).forEach(function(w){var k=String(w[0]).toLowerCase();if(seen[k])return;seen[k]=1;L.push({a:w[0],form:w[0],b:w[1],k:w[2],id:'sw:'+k,n:0,sq:qi+1,sum:'',hook:'',en:'',ko:''})})});
  return L.map(function(s,i){return {s:s,i:i}}).sort(function(x,y){return (x.s.sq-y.s.sq)||(x.i-y.i)}).map(function(x){return x.s});
}"""
R=[(OLD,NEW),
("h+='<div class=\"swr\"><div class=\"swq\"><span class=\"sa\">'+words(s.a)","h+='<div class=\"swr\"><div class=\"swq\"><span class=\"qn\">'+s.sq+'번</span><span class=\"sa\">'+words(s.a)"),
(".wl .lc{",".qn{font-size:12px;font-weight:800;color:#fff;background:var(--sub);border-radius:6px;padding:2px 6px;margin-right:6px;flex:none}\n.wl .lc{")]
fs=glob.glob('/home/claude/via-high/h/**/yoyak-*.html',recursive=True)+['/home/claude/work/real_body.html','/home/claude/via-high/요약문연습_제작/real_body.html']
n=bad=0
for f in fs:
    t=open(f,encoding='utf-8').read()
    if 'class="qn"' in t: continue
    if not all(a in t for a,b in R): bad+=1;print('NOFIT',f);continue
    for a,b in R:t=t.replace(a,b,1)
    open(f,'w',encoding='utf-8').write(t);n+=1
print('patched',n,'nofit',bad)
