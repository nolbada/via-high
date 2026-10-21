# 기준 수치 (geumcheon-go1, 390px 화면)

- 체크박스: {"width": "20px", "height": "20px", "accentColor": "rgb(148, 163, 184)"}
- 완료 체크칸: {"width": "20px", "height": "20px", "borderRadius": "5px", "fontSize": "14px", "fontWeight": "900"}
- 유형 이름 줄: {"fontSize": "15.5px", "fontWeight": "700", "paddingTop": "13px", "paddingBottom": "13px"}
- 유형 이름 b: {"fontSize": "15.5px", "fontWeight": "700"}
- 매번 다른 문제 표시: {"fontSize": "11px"}
- 전체선택 버튼: {"fontSize": "13.3333px", "fontWeight": "400", "textDecorationLine": "underline"}
- 체크한 유형 이어서 풀기: {"fontSize": "13.3333px", "fontWeight": "400", "borderRadius": "12px", "paddingTop": "12px", "borderTopWidth": "1px"}
- 이어서 풀기 카드: {"borderTopWidth": "2px", "borderRadius": "12px", "paddingTop": "11px", "paddingLeft": "14px", "marginTop": "10px"}
- 이어서 풀기 제목: {"fontSize": "15px"}
- 이어서 풀기 부제: {"fontSize": "12.5px"}
- 번호 배지: {"width": "19px", "height": "19px", "fontSize": "10.5px", "fontWeight": "800", "borderTopWidth": "1px"}
- 배지 줄: {"gap": "3px", "marginTop": "5px"}
- 기록 회 제목: {"fontSize": "14px"}
- 기록 소요시간: {"fontSize": "12px"}
- 학습 기록 카드: {"borderTopWidth": "1px", "borderRadius": "12px", "paddingTop": "10px", "paddingLeft": "12px"}
- 기록 소제목: {"fontSize": "12px"}

# 색 (테마 변수 연결)

- 완료 체크칸 배경: .arow .ck i.okb backgroundColor = var(--pri) -> rgb(29, 78, 216)
- 완료 체크 글자: .arow .ck i.okb color = var(--onpri) -> rgb(255, 255, 255)
- 체크한 유형 버튼 배경: .qgo backgroundColor = var(--pri) -> rgb(29, 78, 216)
- 켜진 배지 배경: .pn.on i backgroundColor = var(--pri) -> rgb(29, 78, 216)
- 켜진 배지 글자: .pn.on i color = var(--onpri) -> rgb(255, 255, 255)
- 이어서 풀기 테두리: .rsm borderTopColor = var(--pri) -> rgb(29, 78, 216)
- 이어서 풀기 제목색: .rsm b color = var(--pri) -> rgb(29, 78, 216)
- 기록 카드 테두리: .rec borderTopColor = var(--pri) -> rgb(29, 78, 216)
