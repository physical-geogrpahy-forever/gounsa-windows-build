# 2026-10-27 SHETRAN 원본 단일모델 0.648ha 패치식생 강우강도 10–50mm/h 실험 프로토콜

## 1. 질문과 연구 한계
사용자 요청: 기존 0.2816ha 가상사면보다 큰 (그러나 1ha 미만) 사면에서 **강우 10, 20, 30, 40, 50mm/h에 따른 ①나지 ②억새 피복 ③듬성듬성한 참나무 맹아 피복 ④억새-참나무 맹아의 패치 혼재**가 유수침식, 유사퇴적 및 격자별 순지표고도 변화에 미치는 효과를 **기존 한 모델 SHETRAN 원본**으로 계산. 나지 외 세 식생 배치에서는 수관차단 ON/OFF도 병렬 비교.

이것은 실제 고운사 관측자료 사용 전 **synthetic process demonstration**이며, 고운사 예측 결과라고 써서는 안 된다.

## 2. 고정 입력

- 원본 SHETRAN 4.7.2 Git commit `cf9cd540add78ad3accbaf62b4199d2032887f6b` 의 수문, 식생, 침식, 수송 물리식 변경 **없음**. 단계별 유사보존과 격자별 `GNU×DTUZ` 및 `DLS` 저장후처리만 추가하는 **diagnostic-only Fortran `WRITE` 및 보조 적산 배열**.
- 셀 크기 **4m**, 경계격자 포함 17×29=493셀, 총 범위 `493×16=7888m²=0.7888ha`, 활성 사면 내부 15×27=405셀, 활성육상 `405×16=6480m²=0.648ha`; 옛 176개 활성육상 0.2816ha와 구분. 4m 공간해상도는 억새 포기와 가지 공간배치를 모두 세밀히 재현하기에 부족할 수 있음.
- 고도는 북측 높은 단순 사면 + 가상 수렴형 횡단면: `z=200+4[0.18(y−1)+0.12 max(y−8,0)]+0.025(x−9)^2+0.09 sin(0.8x+0.3y)`(m) 후 0.01m 반올림. 실제 DEM 또는 현장 기울기 기록 아님. 남북 전면에 불투수/무흐름 경계: **유역 유출구 없음**, 사면 하부로 이동한 물 및 유사의 외부배출을 물리적으로 검증할 수 없음.
- 강우 균일 10,20,30,40,50mm/h, 사상지속 3h, 각 30,60,90,120,150mm 누적, 이전 1h 무강우 준비기간. 총 모델 시간 12h, 잠재증발산 0으로 통일해 canopy ON/OFF의 비수관 ET 교란 제거.
- 원본 FRD `:FR20` `PMAX,PALFA,QMAX,TMAX,BSOFT`에서 **진짜 네 번째 TMAX 0.015625h(56.25초)**, 첫 PMAX=1mm 고정, BSOFT=F로 원래 검증오류 재발방지. 14초 더 작은 TMAX와 공간해상도 검증은 별도 필요.
- 원토양 입도, GKR/GKF/밀도, 초기 토양수분 등의 그 밖의 값들은 업스트림 Cobres 예제를 유지한 **가상 기준조건**, 현장 실측으로 보정된 것이 아님. 초기 이동가능 퇴적층 10mm로 수정. 실제 얕은 암반 토심의 유한 원토양재고 상한이나 사건 내 DEM→유량 재연결은 원본 미구현.
- 3개 원본 네이티브 식생유형: `NVC=1` 참나무 맹아(시험 `PLAI=0.85, CLAI=3.0, CSTCAP=1.50mm`, 적하높이 2m, 적하직경 4mm, 적하 분율0.5); `NVC=2` 억새(`PLAI=.65, CLAI=.75, CSTCAP=.70mm`, 적하높이 0.8m, 3mm, 분율0.5); `NVC=3` 나지(`PLAI=0, CLAI=0`, 적하 분율0). 모두 임의 가상 시험값이며 문헌이나 실측 확정값이 아님. `CPLAI=MIN(CLAI,1)*PLAI`로 CLAI 1 이상인 참나무는 구조상 포화 제한이 존재.
- 지표면 피복 `SY41`의 FCG는 나지0, 억새.55, 참나무.12로 나누어 사용 (각각 **별도 가상 시험 매개변수**, LAI와 동일시하지 않음). `SY41e`는 셀별 식생 종류의 공간적 지표면 보호차이를 표현. 수관 OFF라도 같은 FCG는 유지.

## 3. 같은 지형 4개 식생지도 (405 active cells)
| 사면 | 참나무 맹아 격자 | 억새 격자 | 나지 격자 | 비고 |
|---|---:|---:|---:|---|
| 나지 | 0 | 0 | 405 | 음성대조 |
| 억새 피복 | 0 | 405 | 0 | 균일 억새 |
| 듬성듬성 참나무 맹아 | 102 | 0 | 303 | 맹아 군집 6개 중심 |
| 억새+참나무 패치 혼재 | 102 | 228 | 75 | 억새 연속 포기 패치와 맹아 군집, 나지 갭 |

모든 조건에서 강우, 지형, 토양, 피복지도는 **시나리오에서 명시한 차이 외 동일**. 참나무와 억새 patch는 4m 격자당 한 종류만 가능(동일 셀 수직 다층 수관 중첩 없음).

## 4. 총 35회 단일모델 네이티브 계산

- 각 강우강도에서 bare 1회, grass ON/OFF 2회, oak_sparse ON/OFF 2회, mixed ON/OFF 2회: **7 case/강우×5=35회**.
- 검증 순서: bare10mm/h 입력 및 원본 계산 smoke, mixed30mm/h smoke, 전체 35행렬. native sediment ledger `Σsource+initial stock−final stock−boundary export` 상대 0.1% 이내; 전원 시나리오 native exit 0일 때에만 full matrix PASS.
- 주 출력: `source_detachment_solid_m3` (새 원토양 박리로 이동 유사에 공급된 고체 체적), `mean_original_soil_erosion_mm`, `delta_z_event_end_mm=∆DLS−ΣGNU DTUZ`, 양수 순상승 격자와 음수 순하강 격자 수, 최대 국지 지표 변화, canopy ON−OFF의 같은 격자 효과.
- **순상승은 퇴적층 상태변화와 원토양 박리를 차감해 정의**하며, 원본 SHETRAN을 사상 중 지형변화 피드백 가능 모델이라고 주장하지 않음. 0.001mm 초과 순상승은 가상 수치 진단에만 사용하며 실제 현장에서의 측정 가능한 침식/퇴적 해상도로 간주 금지.
- 결과 산출물이 생성되기 전에는 **성공/실패나 경향(10→50, 식생차)을 절대 예측해서 보고하지 않는다.**

## 5. 실행 및 코드
- [GitHub Actions 원본 전체 실험](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40447553464)
- [입력 및 35 시나리오 매트릭스 생성 코드](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_large_patch_matrix_20261027.py)
- [원본 단계 및 셀별 누적 박리 진단 코드](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_large_patch_diagnostics_20261027.py)
- [워크플로](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/.github/workflows/shetran_large_patch_rainfall_matrix_20261027.yml)

## 6. 최종 채택과 별개로 아직 남는 과제
- 폐쇄 출구를 실제 지형의 하단 열림 유출구로 변경 및 토사 배출 확인.
- 같은 물리영역 2m, 1m 등 grid-spacing 민감도, DEM의 국지 곡률 및 실제 산지 경사 재현.
- 실측 억새와 참나무 맹아의 LAI, 주기적 leaf-off, 수관저류, 잎적하, 관측 토심 및 실강우 확보.
- 고운사 실측 격자와 토양 속성, 암편, 사면 출구 조건 적용 및 DEM/퇴적량 관측으로 정량 평가.
