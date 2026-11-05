#!/usr/bin/env python3
"""바탕화면(홈 화면 앱)·태블릿 안정화 파일(h/common/base.js)을 모든 화면에 연결한다. 몇 번 돌려도 안전하다(이미 연결된 화면은 건너뜀).
새 화면·새 학교를 올린 뒤 저장소 맨 위 폴더에서 한 번 돌린다:  python3 factory/tools/attach_base.py
연결 방법: 각 html의 viewport 태그 바로 뒤에 <script src=".../common/base.js?v=261105a"></script> 한 줄만 넣는다(다른 곳은 바꾸지 않음).
--check 를 붙이면 빠진 화면만 알려 주고 아무것도 바꾸지 않는다."""
import os,re,sys
V=b'261105a'
VP=re.compile(rb'<meta[^>]+name=["\']viewport["\'][^>]*>',re.I)
HP=re.compile(rb'<head[^>]*>',re.I)
root=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','h'); root=os.path.normpath(root)
common=os.path.join(root,'common')
if not os.path.exists(os.path.join(common,'base.js')): sys.exit('h/common/base.js 가 없습니다')
check='--check' in sys.argv; n=0; miss=[]
for dp,dn,fn in os.walk(root):
    dn[:]=[d for d in dn if d not in('.git','node_modules')]
    for f in fn:
        if not f.endswith('.html'): continue
        p=os.path.join(dp,f); b=open(p,'rb').read()
        if b'common/base.js' in b: continue
        m=VP.search(b) or HP.search(b)
        if not m: miss.append(os.path.relpath(p,root)+' (head 없음, 건너뜀)'); continue
        rel=os.path.relpath(os.path.join(common,'base.js'),dp).replace(os.sep,'/')
        miss.append(os.path.relpath(p,root))
        if not check:
            tag=b'<script src="'+rel.encode()+b'?v='+V+b'"></script>'
            open(p,'wb').write(b[:m.end()]+tag+b[m.end():]); n+=1
print(('빠진 화면 %d개'%len(miss)) if check else ('새로 연결 %d개'%n))
for x in miss[:20]: print(' -',x)
