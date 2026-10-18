---
name: high-y
description: 고교 교과서 핵심 문장을 H-S코스(Y xray 심화 방식: 동사→주절→절 열기→준동사) 앱으로 만들 때 쓴다.
---

# H-S코스 앱 만들기 (high-y)

H-S코스 = Switch(전원 ON, 고난도 대비). V시그널 Y의 xray 심화 방식 그대로, 준동사까지 뜯어 분석한다. 내부 이름은 'H-S코스'. 서열 표현 금지. 학생 화면 표기는 아래 '이름 표기' 규칙을 따른다.

## 이름 표기 (학생 화면 vs 교사용)
- 학생이 보는 모든 곳(앱 제목·목록 행·선택 화면·기록 화면·정답 링크 페이지)에는 H-S코스라고 쓰지 않고 '핵심 7문장 분석 (심화)'라고 쓴다. 학생은 K·S를 모른다. 예: '3과 핵심 7문장 분석 (심화)', '청석고1 4과 핵심 7문장 분석 (심화)'.
- 'H-S코스'는 선생님끼리 부르는 내부 이름(파일·스킬·대화)에서만 쓴다. 기본은 '핵심 7문장 분석 (기본)'(내부명 H-K코스).
- 새로 만들 때 build 결과의 제목·헤더·rec-h·목록 행을 모두 점검해 'H-S' 글자가 학생 화면에 남지 않게 한다.

## 작업 전
- 원본을 실제로 연다: https://nolbada.github.io/via/vsignal-y/xray.html#adv (nolbada/via 의 vsignal-y/xray.html). 읽기 전용.
- 필요한 자료를 먼저 말한다: 학교·과, 핵심 문장(영문), 기준 해석.

## 도구
textbook/_tools/h-course/ 의 build_hs.py, test_hs.py, README.md. 기준 사례: textbook/g1-geumcheon-mirae/l3/y/. 문장 데이터는 xray.html 의 const S=[...] 를 교체한다.

## 문장 항목 (build_hs.py 의 add(...))
{lv:'심화', id, tok, ch, ko, nodes, dec, vn, why, nf, em}
- nodes: 주절 노드(S, V, G 동사 묶음, form 1~5, fl 가릴 토큰, sk, note)와 절 노드(kind, sub, anc/np, gv/om/host/fill/form2 …).
- G: be going to V, have p.p., be p.p., be -ing, 조동사+동사는 한 그룹.
- nf: 준동사(to부정사 부사적/명사적/형용사적, 동명사, 분사).
- 형식: 자동사+전치사는 1형식+전치사구, confine A to B 는 3형식, It wasn't until A that B 는 that 뒤가 뼈대.

## 흐름
동사 찾기 → 주절(S, V, 형식 닮은꼴; 절은 테이프로 가림) → 절 열기 → 준동사. 앱은 고르기만, 쓰기는 종이.

## 검수
- test_hs.py 로 모든 문장이 끝까지 통과하는지 확인.
- 단계별 화면 캡처를 사용자에게 먼저 보여 준다.
- 해석·분석 데이터 전수 확인.
- Pages 반영 1~2분, 안 바뀌면 ?v=숫자.
