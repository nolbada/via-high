import sys
import os
HERE=os.path.dirname(os.path.abspath(__file__))
R=os.path.join(HERE,'..','..','h')+os.sep
def once(s,a,b,n):
    assert s.count(a)==1,(n,s.count(a)); return s.replace(a,b)
def patch(school):
    p=R+school+'/index.html'; s=open(p,encoding='utf-8').read()
    if 'data-day' in s: print('already',school); return
    s=once(s,'var selNo=0,cmode="m",wsel=null;','var selNo=0,cmode="m",wsel=null,rsel=null;','selNo')
    s=once(s,'</style>',".ncg .d[data-day]{cursor:pointer;-webkit-tap-highlight-color:transparent}\n.ncg .d.sel::after{content:\"\";position:absolute;bottom:0;left:50%;width:16px;height:3px;margin-left:-8px;border-radius:2px;background:var(--ink)}\n.pr .ph[data-go]{cursor:pointer}.pr .ph .gt{font-style:normal;font-weight:800;color:var(--sub);margin-left:6px}\n</style>",'css')
    s=once(s,"td=dkey(now),","td=dkey(now),rd0=rsel||td,rdD=new Date(+rd0.slice(0,4),+rd0.slice(5,7)-1,+rd0.slice(8,10)),",'td')
    s=once(s,"+(k===td?' tod':'')+(n?' dn':'')+'\"><span class=\"n\">","+(k===td?' tod':'')+(n?' dn':'')+(rsel&&k===rsel?' sel':'')+'\" data-day=\"'+k+'\"><span class=\"n\">",'cell')
    s=once(s,"dkey(new Date(e.t))===td){hit=1;","dkey(new Date(e.t))===rd0){hit=1;",'hit')
    s=once(s,"'<div class=\"pr\"><div class=\"ph\"><b>'+f.no+'회 ('+src(f.v)+')</b>'+(ts?'<span>소요 '+(ts>=60?Math.round(ts/60)+'분':ts+'초')+'</span>':'')+'</div>","'<div class=\"pr\"><div class=\"ph\" data-go=\"'+f.no+'\"><b>'+f.no+'회 ('+src(f.v)+')</b><span>'+(ts?'소요 '+(ts>=60?Math.round(ts/60)+'분':ts+'초'):'')+'<i class=\"gt\">\\u203a</i></span></div>",'ph')
    s=once(s,"'<div class=\"rr\"><em>오늘의 학습 · '+fmtMD(now)+'</em>'+(any?tl:'<b>아직 없어요</b>')+'</div>'","'<div class=\"rr\"><em>'+(rd0===td?'오늘의 학습':'학습 기록')+' · '+fmtMD(rdD)+'</em>'+(any?tl:'<b>'+(rd0===td?'아직 없어요':'이 날은 기록이 없어요')+'</b>')+'</div>'",'hdr')
    s=once(s,"document.getElementById('today').addEventListener('click',function(e){\n","document.getElementById('today').addEventListener('click',function(e){\n  var dy=e.target.closest('[data-day]');if(dy){rsel=dy.dataset.day===td0()?null:dy.dataset.day;today();var rc=document.querySelector('#today .rec');if(rc)rc.scrollIntoView({behavior:'smooth',block:'start'});return}\n  var gg=e.target.closest('[data-go]');if(gg){selNo=+gg.dataset.go;today();var bk=document.querySelector('#today .blk');if(bk)bk.scrollIntoView({behavior:'smooth',block:'start'});return}\n",'click')
    s=once(s,'var QS={};','var QS={};function td0(){var d=/[?&]d=(\\d{4})-(\\d\\d)-(\\d\\d)/.exec(location.search)?new Date(+RegExp.$1,+RegExp.$2-1,+RegExp.$3,12):new Date();return dkey(d)}','td0')
    open(p,'w',encoding='utf-8').write(s)
if __name__=='__main__':
    for x in sys.argv[1:]: patch(x)
