import re,shutil,port
from port import *
import patch2
SC='jusung-go2'
S0=os.path.join(HERE,'_before')+os.sep; os.makedirs(S0,exist_ok=True)
p=R+SC+'/index.html'; pp=R+SC+'/parts.js'
for fn in ['index.html','parts.js']:
    import os
    b=S0+SC+'_'+fn+'_before'
    if not os.path.exists(b): shutil.copy(R+SC+'/'+fn,b)
    else: shutil.copy(b,R+SC+'/'+fn)
s=rd(p)
s=once(s,'</style>',css+'</style>','css')
s=once(s,'function today(){','var QS={};function src(v){return v.src}\nfunction today(){','QS')
s=once(s,"  var wn=WN.count();h+='<a class=\"wnb\"",rsm+"  var wn=WN.count();h+='<a class=\"wnb\"",'rsm')
a=s.index("  ACT.forEach(function(a){var id=a[0],sc=setOf(v),u=sc.url[id];if(!u)return;");b=s.index("  if(!pr.n)h+='<div class=\"soonbox\">")
s=s[:a]+rows+s[b:]
a=s.index("  h+='<div class=\"rec\">");b=s.index("  h+='<div class=\"road\">")
s=s[:a]+rec.replace('모두 끝냈어요 🎉','모두 끝냈어요')+s[b:]
s=once(s,"  document.getElementById('sum').textContent",cnt+"  document.getElementById('sum').textContent",'cnt')
s=once(s,"document.getElementById('today').addEventListener('click',function(e){\n","document.getElementById('today').addEventListener('click',function(e){\n"+hand,'hand')
i=s.index("document.getElementById('today').addEventListener('click'");j=s.index("\n});",i)+4
s=s[:j]+"\n"+chg+s[j:]
s=once(s,'var PERSRC=true;','var PERSRC=false;','persrc')
# ROAD serials
off={'모의고사':3,'기출 복습':13,'교과서 기출':15}
a=s.index('var ROAD=[');b=s.index('];',a)+2;road=s[a:b]
def sub(m):
    n=int(m.group(1));src=m.group(2)
    if src in off: n+=off[src]
    return '%d회 (%s)'%(n,src)
road=re.sub(r'(\d+)회 \((모의고사|기출 복습|교과서 기출)\)',sub,road)
road=road.replace('월 11/30 · 1회 (최종점검)','월 11/30 · 19회 (최종점검)')
s=s[:a]+road+s[b:]
# weekday on ROAD header dates
s=once(s,"function fmtMD(d){","function rdt(s){var a=s.split('/');return fmtMD(new Date(Y,a[0]-1,+a[1]))}\nfunction fmtMD(d){",'rdt')
s=once(s,"'</span><span class=\"wd2\">'+w[0]+'~'+w[1]+'</span>","'</span><span class=\"wd2\">'+rdt(w[0])+'~'+rdt(w[1])+'</span>",'wd2') if "'</span><span class=\"wd2\">'+w[0]" in s else s
open(p,'w',encoding='utf-8').write(s)
t=rd(pp)
if '(261022)' not in t:
    ii=iife.replace("(L3|L4)","(L3|L4|mock)").replace("'blank':'blank'}","'blank':'blank','nd-voc':'voc','nd-find':'find','nd-eob':'eobeop','nd-awk':'awk','nd-und':'und'}")
    open(pp,'w',encoding='utf-8').write(t.rstrip('\n')+'\n\n'+ii)
patch2.patch(SC)
print(re.search(r'var ROAD=.*',rd(p)).group(0)[:1500])
