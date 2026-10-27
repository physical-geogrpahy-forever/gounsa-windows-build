# 2026-10-27 고운사 SHETRAN 주모델 선정 인계

## 이번 세션의 신규 논문
- 없음. 신규 문헌 검색 대신 저장소의 기존 원본 코드 조사와 기존 native 실행 보고서를 대조하고, 사용자의 명시적 모델 선택을 결정문으로 고정하였다.

## 신규 식 및 확인된 기존 식
- 신규 물리식 추가 없음.
- 기존 원본 Type 5 개방경계의 가상 시험 관계 `Q_out = 50 h^2` [m³/s]를 그대로 인용. 계수 50은 관측 및 현장 검증이 아닌 실험설정.
- SHETRAN 원본의 수관저류, 직접강우/수관적하 박리, 유수박리 및 4방향 유사 수송을 기존 결정문에서 확인.

## 변경된 판정
- **SHETRAN 4.7.2를 고운사 단일 강우사상 유수침식 주모델로 최종 선정한다.**
- ‘주모델 미선정, SHETRAN 최종 채택 보류’에서 ‘주모델 선정 완료, 현장 정량 예측 타당성 검증 보류’로 변경.
- 대체 주엔진 탐색은 종료하고 SHETRAN 검증과 실제 고운사 현장 입력 구축을 우선한다.
- 35회 합성사면 native 실험의 실행성 및 이동가능 유사수지 폐합과 고운사 현장량 검증은 구분.

## 새로 작성하거나 갱신한 파일
- `decisions/2026-10-27_SHETRAN_SELECTED_AS_GOUNSA_SINGLE_STORM_EROSION_ENGINE.md` 신규
- `MASTER.md` 선정 요약을 최상단에 기록
- `models/SHETRAN.md` 모델 선정 및 한계 추가
- `INDEX.md` 실제 papers 442, models 93, decisions 78에 맞춰 재생성
- `sessions/2026-10-27_1435_SHETRAN_SELECTION_HANDOFF.md` 신규

## 완료된 검증의 기준 출처
- `decisions/2026-10-27_SHETRAN_OPEN_FOUR_SIDES_0P648HA_35_SCENARIOS_NATIVE.md`
- 실제 Actions: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40455147463
- 원본 upstream `cf9cd540add78ad3accbaf62b4199d2032887f6b`.

## 다음 단계
1. 네 방향별 QOC 및 QSED 적산과 `k` 경계조건 민감도 검정.
2. 50mm/h 혼재 조건의 141.487mm 극단 국지 퇴적 원인 및 유사 저장고/토심 제한 검토.
3. 같은 물리 영역에 대해 4m→2m→1m 공간수렴 검증.
4. 실제 고운사 DEM과 억새/참나무 맹아 피복배치, LAI, 토양입경 및 침식저항, 토심, 암편, 현장 강우 조건으로 수관 ON/OFF 비교.
5. `PMAX`/`TMAX` 파라미터 혼동이 재발하지 않도록 고정된 원본 input parsing 및 QA 활용.

## 주의
- 원본 코드의 강우사상 중 DEM 자동 지형갱신 및 개별 세류 self-incision 구현을 주장하지 않는다.
- 141.487 mm는 가상 사면의 국지 최대값이며 고운사 실측 결과가 아니다.
