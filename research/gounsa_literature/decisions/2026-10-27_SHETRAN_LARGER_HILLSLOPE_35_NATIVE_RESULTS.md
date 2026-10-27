# SHETRAN 원본 물리식 0.648ha 대조실험: 4개 식생 × 10–50mm/h, 총35 조건 네이티브 완료

실행일 2026-10-27, 고운사 프로젝트. **고운사 실측 DEM, 강우, LAI가 아닌 인위적 가상사면의 모델 기능 및 민감도 실험**. 현장 침식 퇴적량으로 사용 금지.

## 질문
0.648ha 가상 산지사면에서 원본 **하나의 모델 SHETRAN 4.7.2**이 강우강도 10,20,30,40,50mm/h에 따라 ①완전나지 ②억새 피복 ③듬성듬성 참나무 맹아 ④억새와 참나무 맹아가 공간패치로 혼재한 상태의 국지 침식과 퇴적 및 순지표고도 변화를 계산하는가? 같은 식생 패치에서 식생 수관차단 ON/OFF 차이는?

## 원본 네이티브 결과 완결성
- 업스트림 소스 [nclwater/Shetran cf9cd540](https://github.com/nclwater/Shetran/tree/cf9cd540add78ad3accbaf62b4199d2032887f6b); GNU Fortran Debug 빌드. 수관-수문-원토양 박리-격자별 유사수송-퇴적 **물리식 변경 전혀 없음**. `SYMAIN` 진단용 유사 고체체적 수지 출력과 별도 누적 원토양 박리깊이 읽기용 배열/WRITE 추가.
- 확장된 사면에서 원본 `NOCTAB=20` 정적 배열상한보다 OC 자동경계 54개가 많아 **`sglobal.f90` 컴파일 용량 `NOCTAB=80`으로만 수정**. 이 빌드는 "원본 물리식+배열 한도 증가+진단 추가"이지 **완전히 무수정 원본 executable이 아님**. 최초 실패 `OCREAD error1050`은 입력/컴파일 용량문제지 침식 수치 실패 아님.
- 확대된 405 육상격자에 맞게 원본 Cobres `VSD :VS08c` 토층 범주지도 및 `FRD RAINFALL STATIONS` 강우배정지도 전면 갱신. 두 번째 `VSREAD error1032`도 176개 이전 마스크를 복사한 시험생성 오류, 물리모형 발산 아님.
- [순차 원본 35회 성공 + 2회 smoke, Actions 40448419992](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40448419992), [5개 강우별 병렬 7회×5=35회 성공, Actions 40448993167](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40448993167).
- **35개 케이스 순차 실행과 별도 병렬 35개 실행의 동일 케이스 1:1 숫자 정확 재현**: 원토양 박리 공급량 `max abs diff=0m³ solid`, 평균 순지표고도 변화 `max abs diff=0mm`.
- Native 유사수지 기준: 모든 35회 내부 native solid ledger `relative_mass_error < 0.001` (0.1%). 전체 중 최대 상대잔차 **0.00046853284591364503 (비율) = 0.04685328459%**, 50mm/h 조건. 출력 크기가 클 때 float 잔차 누적효과가 증가하므로 원본 수지검증은 모든 강도에서 통과하지만 local accuracy validation과 구분.

## 가상 입력과 단위
- 4m 정방격자, 17×29 전체 **0.7888ha**, 15×27 활성사면 **405셀=0.648ha**. 1ha 미만 유지. 지형은 유역자료가 아닌 가상 남북 경사+가로 수렴사면. **하단 및 측면 경계가 막힌 no-outlet closed domain**이며 유사배출량은 0. 지표고도가 응집 퇴적층 변화로 내부 계산에 재반영되는 fully coupled morphodynamics는 존재하지 않고, `∆z=∆DLS−ΣGNU DTUZ`는 사상 종료 후 원본 변수 후처리.
- Rain 10,20,30,40,50 mm/h×3h, 누적강우 30,60,90,120,150mm, 1h 사전 무강우, 총 12h, 잠재증발산0. 원본 FRD 첫 `PMAX=1mm` 고정, **실제 넷째 필드 TMAX=0.015625h(56.25sec)**, BSOFT=F.
- 토성 및 침식계수 등: 원본 Cobres 예제(실제 고운사 관측/보정값 아님), 이동가능 초기 loose sediment DLS 10mm.
- 격자별 종 배치 405셀: 완전 나지 (bare 405), 억새 (grass 405), 듬성듬성한 참나무 맹아(참나무102 나지303), 억새와 참나무 혼재(참나무102 억새228 나지75). NVC=1 oak,2 Miscanthus,3 bare.
- 임의 시험수관 파라미터: 참나무 `PLAI=.85 CLAI=3 CSTCAP=1.5mm`, 억새 `PLAI=.65 CLAI=.75 CSTCAP=.7mm`; bare PLAI0, crown drip fraction0. 동일식생 내 OFF는 PLAI0으로 변경하고 나머지 지표 토양 및 ground cover `FCG` 범주나 공간배치 유지, PET0으로 비수관 ET 교란 최소화. `FCG`: 나지0, 억새0.55, 참나무0.12 (**LAI와 별개**, 임의 가상값). `CPLAI=MIN(CLAI,1)×PLAI`와 원본 적하에 따른 nonlinearity 존재. 루트 및 토심 재고를 식생 천이와 결합하거나 현장 검증한 실험 아님.

## 결과 1. 원토양에서 새로 박리되어 이동퇴적계에 공급된 유사량 [m³ 고체체적]
(이는 외부 사면 유사배출량이나 특정 셀의 퇴적량이 아니다. 모든 값 수관 ON.)

| 강우 [mm/h] | 나지 | 억새 | 듬성듬성 참나무 맹아 | 억새+참나무 패치 혼재 |
|---:|---:|---:|---:|---:|
| 10 | 1.43919585 | 0.99277208 | 1.30008711 | 1.05320325 |
| 20 | 12.00467095 | 11.46080613 | 11.84936949 | 11.55171524 |
| 30 | 18.98555694 | 18.57674762 | 18.94448448 | 18.64226084 |
| 40 | 23.96871903 | 23.51866900 | 23.77133688 | 23.61349286 |
| 50 | 28.37127125 | 27.60650734 | 27.92018246 | 27.68095455 |

나지 대비 피복 ON의 박리량 감소(%):
| 강우 [mm/h] | 억새 | 듬성듬성 참나무 | 혼재 |
|---:|---:|---:|---:|
|10|31.019|9.666|26.820|
|20|4.530|1.294|3.773|
|30|2.153|0.216|1.808|
|40|1.878|0.823|1.482|
|50|2.696|1.590|2.433|

이 특정 가상 매개변수에서 낮은 10mm/h에 피복에 따른 총 박리차가 특히 크고, 20–50mm/h에서 좁아진다. **이것이 실제 참나무보다 억새가 보호효과 높다는 일반적 물리 법칙이나 현장예측을 뜻하지 않는다**. 억새는 405셀 완전피복, 참나무는 102셀과 303셀 나지로 **피복 공간면적부터 다르다**.

## 결과 2. 같은 지표면 FCG와 패치지도에서 수관차단만 ON−OFF
아래 값은 원토양 박리 공급량 **OFF−ON (m³ solid)**. 양수이면 수관차단 활성일 때 박리 공급량이 작다. PET=0.

| 강우 [mm/h] | 억새 | 참나무 맹아 | 혼재 |
|---:|---:|---:|---:|
|10|0.39654053|0.13634837|0.35533318|
|20|0.41621582|0.14770747|0.37735452|
|30|0.20500268|0.02855933|0.22469717|
|40|0.17046273|0.18015427|0.19339405|
|50|0.41252127|0.42945615|0.48729802|

각 intensities에서 수관차단 활성 효과가 양수였음. **고정된 LAI 및 인위 canopy storage 조건에만 성립**하며 개별 참나무 맹아 생장/초본 잎 구조 현장 데이터로 일반화할 수 없음. 수관차단 플래그가 실제로 PLAI=0 조건이고 잎의 동역학까지 완전히 독립한 ablation switch는 아님.

## 결과 3. 국지 순지표고도 및 닫힌 경계의 극단적 인공 축적
- 순지표고도 산출 `∆z_post(x,y)=DLS_end−DLS_start−ΣGNU Δt`. positive는 저류 퇴적층 두께 증가가 자체 원토양 박리 두께보다 크다는 뜻. fully dynamic topo change feedback 아님.
- `∆z_post>0.001mm` 양의 변화 셀 수:
| 강우 | 나지 | 억새 | 참나무 맹아 | 혼재 |
|---:|---:|---:|---:|---:|
|10|11|11|12|10|
|20|38|38|39|38|
|30|46|44|45|45|
|40|56|55|54|54|
|50|57|56|58|59|
- 나지 평균 순고도변화 ON [mm]: 10 `−0.0493066`, 20 `−0.4178097`, 30 `−0.6569769`, 40 `−0.8233682`, 50 `−0.9737380`; 혼재 ON: `−0.0357576, −0.4025236, −0.6468593, −0.8134557, −0.9504301`. **큰 국지 양퇴적과 음침식이 평균에서 서로 상쇄되는 특성**.
- 무유출구 사면에서 최대 양의 `∆z` 나지 기준 **10mm/h +1.6635mm, 20 +102.2712mm, 30 +170.4182mm, 40 +305.2660mm, 50 +406.5417mm**. 50mm/h 나지 최강 국지 침식 `−34.0958mm`. 50mm/h의 과도한 퇴적 집중은 하단이 막힌 합성 경계조건 영향이 강할 수 있어 **실제 고운사 퇴적고도라고 해석할 수 없고, 정량 현장수준 모델로 곧바로 채택 금지**. 경계 밖 물과 유사배출에 대한 검증과 갱신이 필수.

## 핵심 물리모델 판정
- **통과:** 원본 SHETRAN 하나의 canopy/LAI 상태, 2D 침식/입경별 유사수송/퇴적, 405셀 0.648ha/3식생 유형/35 원본 계산 성공, 닫힌 경계의 native sediment stock conservation; 2개 독립 실행 배치(순차와 병렬) 결과 35/35 **완전 일치**.
- **미완료 및 제약:** 열린 하단 유출구의 water/sediment balance, 동일 영역 공간해상도 수렴, 큰 비에서 후퇴하는 토심 H finite source limiter, 실제 지형/기상/토성/LAI, 수관저류, 잎적하, 지표피복률 실측, 고해상도 억새 포기 및 맹아 패치. `∆z_post`는 사상 내 DEM 갱신을 재반영하지 않음.
- 결론: **연구요구의 네 피복 시나리오 및 10–50mm/h 민감도 계산이 단일 SHETRAN 엔진에서 실행 가능**함을 실제 시험으로 확인. 고운사 정량 침식·퇴적에 적절한 입력 및 출구 수문검증을 마친 것은 아니므로 **모델 현장 채택 최종선언 보류**.

## 모든 재현자료
- [35케이스 전부 순차 실행과 smoke 성공 Actions 40448419992](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40448419992) [최종 결과/격자별 CSV artifact](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40448419992/artifacts/12710245614)
- [5강우 분리 7건씩 네이티브 성공 Actions 40448993167](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40448993167)
- [10mm/h 행렬 및 405셀×7개 CSV](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40448993167/artifacts/12709945809)
- [20mm/h 행렬 및 405셀×7개 CSV](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40448993167/artifacts/12710125321)
- [30mm/h 행렬 및 405셀×7개 CSV](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40448993167/artifacts/12709543405)
- [40mm/h 행렬 및 405셀×7개 CSV](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40448993167/artifacts/12708904801)
- [50mm/h 행렬 및 405셀×7개 CSV](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40448993167/artifacts/12709960799)
- [가상 사면, NVC/FCG/수관/강우행렬 입력 생성 및 시뮬레이션 스크립트](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_large_patch_matrix_20261027.py)
- [NOCTAB 원본 capacity-only 컴파일 패치](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_large_patch_capacity_20261027.py)
- [단계별 독립 native mass 및 셀별 박리심도 진단](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_large_patch_diagnostics_20261027.py)
- [실험 설계, 입력 가정 및 실패한 준비작업 원인](2026-10-27_SHETRAN_0P648HA_FOUR_COVERS_10TO50MMH_EXPERIMENT_PROTOCOL.md)

## 단위와 실험자 과실 표기
- 발표할 때 수치 `m³ solid`를 `m³ erosion of bulk soil`, `sediment yield outside plot`, `tonnes`로 바꾸지 말 것. 변환하려면 건조밀도, 벌크밀도, 공극비 등 물리 단위 확인 및 외부 유출량 separate flux 측정이 필수.
- 초기 176 셀 기반 Cobres VSS와 강우 grid mask 재생성을 누락했거나 NOCTAB=20을 넘긴 입력 생성 오류는 **원본 SHETRAN 수치불안정과 전혀 다르다**.


## 2026-10-27 생성된 실제 native 셀별 지도 17장 (합성지형)
- [성공한 maps workflow 40450170885](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40450170885) 및 [17 PNG 지도 원본 산출물 artifact](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40450170885/artifacts/12710256837).
- 전체 original native 35회 outputs 중 아카이브의 `cells.csv` 35개와 `summary_matrix.csv`를 그대로 읽어 제작, **모의계산을 새로 하지 않음**.
- 강우 10/30/50 mm/h의 나지, 억새, 듬성 참나무, 패치 혼재 4사면 **총 12장의 native 순고도변화 지도**, 패치혼재 canopy ON−OFF **3장 국지 차분 지도**, 혼재 native `NVC` 패치 입력지도 1장, 강우별 원토양 박리 공급량 곡선 1장, 총17장.
- 단위 mm이며 채색의 범위는 계산된 극단 local depression/accumulation 때문에 10mm/h는 ±2mm, 30/50은 ±10mm로 잘라 표현. 각 그림에 **실제 출력의 최대 최소치를 별도 기재**. 그러므로 색채 상한을 실제 최대치로 오해 금지.
- 그림들은 georeferenced Gounsa DTM이 아닌 `x,y` synthetic grid indices다. 눈에 띄는 사면 하단 국지 상승은 폐쇄 출구에 의한 인공 유사축적 영향이 있을 수 있으므로 실제 퇴적예측으로 주장 불가.
- [그림 생성 스크립트](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_render_405cell_model_artifact_20261027.py).
