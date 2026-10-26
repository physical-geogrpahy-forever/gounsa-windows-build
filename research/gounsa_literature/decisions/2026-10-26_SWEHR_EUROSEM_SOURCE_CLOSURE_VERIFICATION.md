# 2026-10-26 원본 수문-유수침식 모형 초기 및 경계조건 복구: 보존시험 결과

## 결론
SWEHR McGuire 2016 공개 C 원본의 강제 물/유사 외부유입과 초기조건 결함을 분리/정정해 **원본 방정식 유지 상태에서** 0mm/h 통제부터 10,20,30,40,50mm/h×1h 조건을 재실행하고 물수지 및 독립 유사수지(원토양 박리-지표퇴적층-부유토사-경계유사량)를 통과했다. EUROSEM 1998 공개 F77 원본은 고정형 72열 포맷 및 원본 테스트 입력의 두 사면 불연결, 잘못된 강우 누적 데이터 카운트를 복구하고 5강우의 **수문 물수지**만 통과했다. EUROSEM의 유사수지는 독립 검증되지 않았다.

## 정정이 반드시 필요했던 원본 경계조건
공개 SWEHR C `SWEHR.c`에는 `j=ny`의 벽 경계처리 뒤 **무조건 실행되는** `Sediment and Water Inflow B.C. at j=ny` 블록이 있으며 외부 `U[3]` 최대 -0.035 m²/s 및 `SED` up to 500kg/m³의 입력조건이 박혀 있다. 이 때문에 10–50mm/h 강우 단독 실험에서 보인 기존 수십 cm 지표변화는 외부 유사 공급조건이 개입한 것이다. 단독 강우 실험에서는 해당 외부 공급을 비활성화하고 j=ny 표준 wall BC로 환원했다.

추가로 `DEPTHINIT`을 `U[1]`에 복사, `SOLID=0`, `M[k]=0`, `TOTM=0`, `TOTSED=0` 및 `DEP=0`를 명시했다. 침투 검증을 위해 공개 예제 `Ks=0`을 고정 시험값 `2×10⁻⁶m/s`로 설정했다. 이 값과 `a=ad=0.25`는 현장 관측값이 아니며 신규 또는 학술적으로 검증된 기계식이 아님. `F=0.004` 원본 수송항은 유지.

## 실행 검증
9개 독립 시험: 무강우/무침식 닫힌 경계, 30mm/h 단시간 닫힌 경계, 30mm/h 열린 경계 침투만, 30mm/h 열린 경계 침식, 10–50mm/h×3600s 다섯 사상. **9/9 PASS**.

전체 1h 시험 원토양 박리량 [kg] = (0.0188734,0.0463353,0.0934287,0.1614564,0.2494528).
경계유사수송량 [kg] = (0.00000229085,0.000363979,0.00453919,0.0224688,0.0663485).
같은 시험면적 9.5625m²에서 경계배출량을 t/ha/event로 환산하면 약 (0.00000240,0.000381,0.00475,0.0235,0.0694).
물수지 상대잔차 최대 약 2.32e-13, 별도 원토양-퇴적층-부유사-경계유사량 수지 잔차 최대 약 2.22e-13. 고도변화가 담고 있는 loose-layer 저장고를 따로 이중계산하지 않고 순 고도변화/유사유출 적산 수지와 박리/퇴적층 저장 수지 2가지 독립 방식으로 확인.

## EUROSEM 공개 원본 시험
기존 test.par은 사면 두 개가 불연결되어 있었고 test.pcp 누적강우 자료는 3개 행이 존재하나 count가 2로 표기되어 있었다. NELE=1 첫 사면만 택하고 미사용 계산순서/우량계 라인을 제거하여 고정행 자료 읽기 일치, cumulative depth 0→R mm at 60min→R at 100min 3점을 명시함. 디버그 컴파일 -fcheck=bounds 등 사용; 결과 정적 출력의 F9.3 자리수 오류를 E14.6로 변경하였으며 지배 방정식을 바꾸지 않음.

반복 실험에서 10,20,30,40,50 mm/h 모두 return code=0이고 물수지 오류 = (0,-0.0333,-0.0002,+0.0060,+0.0088)%로 1% 기준 통과. 30mm/h 별도 재시도도 동일 출력. 그러나 원본 erosion mass의 정량 검증에는 독립 sediment budget ledger가 없어 **sediment NOT PASS**. 총박리량 [kg] = (0,351,47348,139376,238136), 순침식량 [kg] = (0,1.51,47044,139088,237937); 큰 값임을 들어 무조건 가능/불가능이라고 하지 않고 sed flux / deposition / original soil loss 재검증 필요. 강우시험면적 14500m², slope S=0.85 및 cover 0.15는 고운사 현장 조건이 아님.

## 연구모형 결정에 미치는 영향
- 이 결과는 original-source engineering benchmark로서 지난 2026-10-26 기각 수치가 전부 코드 본연의 계산된 침식이라고 한 것을 바로잡는다.
- 2026-09-22 잠정 선정된 `Iber+ -> SSSPAM/mARM` 본 생산 모형을 SWEHR로 바꾸는 결정이 아님.
- HETEROFOR/실측식생 강우분배/줄기 유하 위치를 SWEHR에 새로 결합했다고 주장하지 않음.
- 모형 실행과 사건별 물리 검증을 구분; 사이트 생산 예측 및 LiDAR 검증은 아직 전혀 아님.

## 재현 링크
원본 실행 및 파일: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/swehr-water-sediment-closure-20261026/experiments/rainfall_10_50
독립 9개 Native SWEHR QA: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40254743506
EUROSEM 6개 QA: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40255588717
전체 판정 보고서: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/swehr-water-sediment-closure-20261026/experiments/rainfall_10_50/CLOSURE_VERIFICATION_2026-10-26.md

## 추가 남은 검증
EUROSEM 독립 sediment ledger, 해상도 및 시간간격 수렴, 고운사 실제 토심/공극/수리전도도/입경/사면구조, HETEROFOR 수관 저장/적하/수간유하의 공간 위치 연동.
