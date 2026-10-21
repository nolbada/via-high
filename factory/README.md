# 학교 앱 공장 (factory)

어느 PC에서 작업해도 같은 결과가 나오게 하는 기준 묶음. 이 저장소(nolbada/via-high)를 받으면 전부 들어 있다.

## 구성
- SPEC.md : 기능·문구·회 번호 규칙 (사람이 읽는 기준)
- SPEC_values.md : 금천고1에서 뽑은 실제 크기·색 수치 (기계 대조 기준)
- snippets/ : 기준 코드 조각 8개 (css, rsm, rows, rec, cnt, hand, chg, iife)
- tools/port.py, run3.py, js2.py, patch2.py : 학교 파일에 조각을 넣는 도구
- tools/audit.py : 6개 학교를 기준과 자동 대조 (PASS/FAIL)

## 어느 PC에서든 시작
1. 저장소 받기 (git clone https://github.com/nolbada/via-high 또는 ZIP)
2. pip install playwright  그리고  playwright install chromium
3. 검수: python3 factory/tools/audit.py   (한 학교만: audit.py jusung-go2)
4. 기준 수치 다시 뽑기: python3 factory/tools/audit.py --dump

## 규칙
- "반영했다"는 말은 audit.py가 해당 학교 PASS일 때만 한다.
- 새 학교/새 기능을 넣으면 snippets와 SPEC을 먼저 고치고, 그다음 모든 학교에 적용한 뒤 audit.py를 돌린다.
- 올릴 때는 요청한 파일만 올린다 (다른 파일 건드리지 않기).
