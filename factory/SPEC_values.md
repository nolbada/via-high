# 기준 수치 (geumcheon-go1, 390px 화면) — v2 기준 (261025)

쉬운 설명: 앱 화면의 글씨 크기·버튼 크기·색을 숫자로 적어 둔 표다. audit.py 가 6개 학교를 이 숫자와 같은지 자동으로 확인한다.
다시 뽑기: `python3 factory/tools/audit.py geumcheon-go1 --dump`

## v2 유형 풀코스 회차 버튼 (2026-10-24부터)
1회를 끝낸 상태(1회 = 끝, 2회 = 지금, 3회부터 = 잠금)에서 잰 값.

- 풀코스 제목 `.sgh b`: {"fontSize": "23px", "fontWeight": "900", "borderLeftWidth": "5px", "paddingLeft": "11px"} (letter-spacing -.5px, 줄높이 1.15)
- 풀코스 진행 알약 `.sgh span` ("21회 중 1회"): {"fontSize": "13.5px", "fontWeight": "800", "borderTopLeftRadius": "99px"} (padding 3px 11px)
- 제목 줄 `.sgh`: margin 22px 2px 10px, 가운데 정렬
- 회차 그리드 `.sgrid`: 한 줄 7칸(`repeat(7,minmax(0,1fr))`), {"columnGap": "6px", "rowGap": "6px", "marginBottom": "14px"}
- 회차 버튼 `.stb`: {"width": "46px", "height": "44.0938px", "borderTopLeftRadius": "11px", "paddingTop": "5px", "paddingBottom": "6px"}, CSS 테두리 1.5px(화면 측정값은 1px로 반올림)
- 단원 뱃지 `.stb .sbd` (3과·4과·모의·최종): {"fontSize": "10.5px", "fontWeight": "800"} 줄높이 1.2
- 회차 번호 `.stb .sno` ("1회"~"21회"): {"fontSize": "14px", "fontWeight": "800"} 줄높이 1.25
- 잠금 점 `.stb.lock::after`: {"width": "5px", "height": "5px", "borderRadius": "50%", "right": "4px", "top": "4px"} 투명도 .6
- 고른 버튼 `.stb.sel`: outline 2px solid var(--ink), outline-offset 1px
- 지금 버튼 `.stb.now`: 테두리 var(--pri) + 그림자 0 0 0 2px rgba(29,78,216,.18)
- 잠금 안내 `.slk` ("N회 먼저 끝내요"): 14px, padding 10px 12px, 둥글기 12px, 배경 var(--line), 글자 var(--sub)

### v2 색 (테마 변수 연결)
| 자리 | 선택자 · 속성 | 변수 | 금천고1 밝은 화면 값 | 어두운 화면 값 |
|---|---|---|---|---|
| 끝난 회차 배경 | .stb.done backgroundColor | --priL | #e6edfc = rgb(230, 237, 252) | #1a2a4a |
| 끝난 회차 테두리·숫자·뱃지 | .stb.done borderColor / .sno color | --pri | #1d4ed8 = rgb(29, 78, 216) | #8ab4ff |
| 지금 회차 테두리 | .stb.now borderColor | --pri | rgb(29, 78, 216) | #8ab4ff |
| 잠긴 회차 배경·테두리 | .stb.lock backgroundColor | --off | #e9eef8 = rgb(233, 238, 248) | #222c3d |
| 잠긴 회차 글자·점 | .stb.lock .sno color | --offInk | #6b7a93 = rgb(107, 122, 147) | #8d9ab0 |
| 안 열린(기본) 버튼 | .stb 배경 / 테두리 | --card / --line | #fff / #d9e0ec | #161d2a / #2a3548 |
| 뱃지 글자(기본) | .stb .sbd color | --pri | rgb(29, 78, 216) | #8ab4ff |
| 풀코스 제목 막대 | .sgh b borderLeftColor | --pri | rgb(29, 78, 216) | #8ab4ff |
| 진행 알약 | .sgh span 배경 / 글자 | --priL / --pri | rgb(230, 237, 252) / rgb(29, 78, 216) | |
| 스페셜 버튼 `.wnb.spb` | 테두리 / 배경 / 글자 | (고정색) | #0d9488 / #e3f6f2 / #0b4f48 | #2dd4bf / #12302d / #c6f3ec |

## 유형 목록(버튼을 눌러 열었을 때) — v1부터 그대로
- 체크박스: {"width": "20px", "height": "20px", "accentColor": "rgb(148, 163, 184)"}
- 완료 체크칸: {"width": "20px", "height": "20px", "borderRadius": "5px", "fontSize": "14px", "fontWeight": "900"}
- 유형 이름 줄: {"fontSize": "15.5px", "fontWeight": "700", "paddingTop": "13px", "paddingBottom": "13px"}
- 유형 이름 b: {"fontSize": "15.5px", "fontWeight": "700"}
- 매번 다른 문제 표시: {"fontSize": "11px"}
- 전체선택 버튼: {"fontSize": "12.5px", "fontWeight": "700", "textDecorationLine": "underline"} (v1 표에는 13.33px/400 이었으나 글꼴 줄임식 오류를 고친 뒤의 값이 맞다)
- 체크한 유형 이어서 풀기: {"fontSize": "15px", "fontWeight": "800", "borderRadius": "12px", "paddingTop": "12px", "borderTopWidth": "1px"}

## 나머지 화면 — 그대로
- 이어서 풀기 카드: {"borderTopWidth": "2px", "borderRadius": "12px", "paddingTop": "11px", "paddingLeft": "14px", "marginTop": "10px"}
- 이어서 풀기 제목: {"fontSize": "15px"}
- 이어서 풀기 부제: {"fontSize": "12.5px"}
- 학습 기록 카드: {"borderTopWidth": "1px", "borderRadius": "12px", "paddingTop": "10px", "paddingLeft": "12px"}
- 기록 소제목: {"fontSize": "12px"}
- 이용 시간 소제목 줄: {"fontSize": "12px", "marginTop": "2px"}
- 기록 카드 큰 칸: {"paddingTop": "12px", "borderTopLeftRadius": "12px"}
- (번호 배지 줄 `.pins`는 261023 학습 기록 카드 개편 때 없어져 측정값 없음)

# 색 (테마 변수 연결) — 그대로

- 완료 체크칸 배경: .arow .ck i.okb backgroundColor = var(--pri) -> rgb(29, 78, 216)
- 완료 체크 글자: .arow .ck i.okb color = var(--onpri) -> rgb(255, 255, 255)
- 체크한 유형 버튼 배경: .qgo backgroundColor = var(--pri) -> rgb(29, 78, 216)
- 이어서 풀기 테두리: .rsm borderTopColor = var(--pri) -> rgb(29, 78, 216)
- 이어서 풀기 제목색: .rsm b color = var(--pri) -> rgb(29, 78, 216)
- 기록 카드 테두리: .rec borderTopColor = var(--pri) -> rgb(29, 78, 216)
