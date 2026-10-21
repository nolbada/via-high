import re,sys
import os
HERE=os.path.dirname(os.path.abspath(__file__))
R=os.path.join(HERE,'..','..','h')+os.sep
def rd(p): return open(p,encoding='utf-8').read()
SN=os.path.join(HERE,'..','snippets')
def sn(n): return rd(os.path.join(SN,n+'.txt'))
css,rsm,rows,rec,cnt,hand,chg,iife=[sn(n) for n in ['css','rsm','rows','rec','cnt','hand','chg','iife']]
def once(s,a,b,name):
    assert s.count(a)==1,(name,s.count(a)); return s.replace(a,b)
def port(school,road=None,mock=False):
    p=R+school+'/index.html'; s=rd(p)
    s=once(s,'</style>',css+'</style>','css')
    s=once(s,'function today(){','var QS={};\nfunction today(){','QS')
    s=once(s,"  var wn=WN.count();h+='<a class=\"wnb\"",rsm+"  var wn=WN.count();h+='<a class=\"wnb\"",'rsm')
    a=s.index("  ACT.forEach(function(a){var id=a[0],sc=setOf(v),u=sc.url[id];if(!u)return;");b=s.index("  if(!pr.n)h+='<div class=\"soonbox\">")
    s=s[:a]+rows+s[b:]
    a=s.index("  h+='<div class=\"rec\">");b=s.index("  h+='<div class=\"road\">")
    s=s[:a]+rec.replace('모두 끝냈어요 🎉','모두 끝냈어요')+s[b:]
    s=re.sub(r"function lbl\(x\)\{return [^\n]*\n","function lbl(x){return x.f.no+'회 ('+src(x.f.v)+') · '+(ACT.indexOf(x.a)+1)+'. '+x.a[1]}\n",s,1)
    s=s.replace("'+sn(v)+'회 (","'+f.no+'회 (").replace("'+sn(f.v)+'회<small>","'+f.no+'회<small>")
    s=once(s,"<span class=\"wm\"><b>'+esc(w[2])+'</b> '+esc(w[3])+'</span>","<span class=\"wm\">'+esc(w[3])+'</span>",'wm')
    s=once(s,"  document.getElementById('sum').textContent",cnt+"  document.getElementById('sum').textContent",'cnt')
    s=once(s,"document.getElementById('today').addEventListener('click',function(e){\n","document.getElementById('today').addEventListener('click',function(e){\n"+hand,'hand')
    i=s.index("document.getElementById('today').addEventListener('click'");j=s.index("\n});",i)+4
    s=s[:j]+"\n"+chg+s[j:]
    if road:
        a=s.index('var ROAD=[');b=s.index('];',a)+2; s=s[:a]+road+s[b:]
    open(p,'w',encoding='utf-8').write(s)
    pp=R+school+'/parts.js'; t=rd(pp)
    if '(261022)' not in t:
        ii=iife.replace("(L3|L4)","(L3|L4|mock)") if mock else iife
        t=t.rstrip('\n')+'\n\n'+ii
        open(pp,'w',encoding='utf-8').write(t)
if __name__=='__main__':
    port(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else None, 'mock' in sys.argv[3:])
