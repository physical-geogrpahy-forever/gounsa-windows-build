# 2026-10-27 SHETRAN 0.648ha 네 방향 개방경계: 가상 사면, 4개 피복과 10–50mm/h 원본 35회 계산

## 연구 조건

- 목적: 1ha 미만 국지 지형에서 나지, 억새, 듬성한 참나무 맹아, 억새+참나무 맹아 연속패치가 동일 강우사상의 원토양 박리, 국지 침식/퇴적 및 유사 배출에 미치는 영향. **단일모델 SHETRAN 4.7.2 원본 물리식 유지**.
- [실제 완료 GitHub Actions 40455147463](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40455147463) 5개 독립 강우작업×각7개 native 실행 **35/35 성공**. GNU Fortran 원본 upstream SHA `cf9cd540add78ad3accbaf62b4199d2032887f6b`. 진단용 `SYMAIN WRITE`만 추가하고 정적 배열 `NOCTAB=20→180` 확장. 이는 **원본의 계산식을 유지한 수정 빌드이지 upstream 무수정 바이너리가 아니다**.
- 전체17×29 격자, 활성15×27=405셀×16m²=6480m²=**0.648ha**. 4m 합성 DEM 및 참나무 102, 억새228, 나지75 등 가상 패치. 1h 무강우 준비 후 10/20/30/40/50mm/h로 각 3h 강우, 모델12h. PET0. **현장 DEM, 관측 LAI, 토양/식생매개변수 아님**.
- **동서남북 가장자리 80개 식생/토양 격자**를 원본 `OCmod:JEOCBC`의 **Type5 native polynomial head-dependent flow**로 지정. 원본 `OCmod2:OCQBC` 공식 `FROMQ=−(A H^4 + B H^3 + C H^2 + D H + E)`에서 `C=50`, 나머지0, `H=water_surface−ground_surface`: 수심이 양수이면 양의 outward flux `Q_out=50 H²` [m³/s]. `k=50`은 측정값이 아니라 가상 유출계수; 네 방향에서 **유출 가능성**을 열었지만 항상 네 방향에서 동시에 유출됐다는 자료는 아직 없다. 북측 상단도 열린 경계지만 물이 빠지는 양은 경계 수심에 따라 달라진다.
- 입력 오류 **OC1059**는 이전 `FRD` 폐쇄형 Type1과 새로운 Type5를 같은 29개 element에 중복 부여해서 발생. 기존 `I`를 활성사면 외주에서 `.`로 변경한 뒤 native 10mm/h 나지와 50mm/h 혼재 smoke 두 개 성공. 오류는 원본 침식 수치발산이 아니라 시험 생성 BC 충돌.
- `SYBC` routine이 비어 있어도 `SYCOLM`은 `QWAT(face)>0`인 외향 경계에서 `QSED(face)`를 결정한다. 실험에서는 **원본 QOC와 QSED에서 직접 읽어 적산한 물 및 유사 경계배출량이 모든 35회에서 양수**. `SYBC`는 외부 유사경계 유입/강제 항목이 비어 있는 것; `SYCOLM`을 통한 외부 유사배출은 실제 존재함.

## ON 원토양 박리로 생성된 새로운 유사 총량 (m³ solid)

| 강우강도 mm/h | 나지 | 억새 | 듬성한 참나무 맹아 | 억새+참나무 혼재 |
|---:|---:|---:|---:|---:|
| 10 | 1.248842 | 0.873195 | 1.132402 | 0.926896 |
| 20 | 10.355333 | 9.844801 | 10.207316 | 9.930026 |
| 30 | 16.603509 | 16.021195 | 16.454447 | 16.139416 |
| 40 | 21.551500 | 20.882753 | 21.396746 | 21.029997 |
| 50 | 25.675134 | 24.879295 | 25.507889 | 25.069872 |

이것은 원래 토양 박리로 새로 생성된 이동 유사 공급량이며, 다음 표의 **경계 밖 배출량**과 다르다.

## ON 경계 배출 유사 총량 (m³ solid)

| 강우강도 mm/h | 나지 | 억새 | 듬성한 참나무 맹아 | 억새+참나무 혼재 |
|---:|---:|---:|---:|---:|
| 10 | 0.041621 | 0.021589 | 0.032156 | 0.022436 |
| 20 | 2.990695 | 2.853339 | 2.927945 | 2.858082 |
| 30 | 7.935353 | 7.752950 | 7.855421 | 7.760990 |
| 40 | 14.531496 | 14.309311 | 14.432845 | 14.316509 |
| 50 | 21.630846 | 21.396716 | 21.528775 | 21.404709 |

## ON 물의 외부 배출량 (m³ liquid)

| 강우강도 mm/h | 나지 | 억새 | 듬성한 참나무 맹아 | 억새+참나무 혼재 |
|---:|---:|---:|---:|---:|
| 10 | 8.451 | 5.294 | 7.198 | 5.481 |
| 20 | 176.933 | 170.105 | 174.168 | 170.402 |
| 30 | 366.606 | 358.817 | 363.514 | 359.198 |
| 40 | 559.079 | 550.987 | 555.808 | 551.297 |
| 50 | 752.805 | 744.121 | 749.435 | 744.607 |

## native 35개 검증 및 극단 퇴적

- [전체 35개 GitHub Actions run](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40455147463). 5개 작업 모두 success, native 35/35 정상종료, 모두 positive net water/sediment border export, **최대 상대 native 이동가능 유사수지 잔차 5.84668×10⁻¹⁴**. 원본 `SYCOLM`의 실제 경계 QSED까지 물질수지에 포함시켜 확인. 이것은 **총토양 재고 보호 / 수치해상도 수렴** 증명이 아니다.
- 기존 폐쇄형 50mm/h 혼재 ON에서 극단적 국지 순퇴적 약 **405.89mm**, 네 방향 개방경계 혼재 ON에서 **141.487mm**로 약65% 감소. **나지 10mm/h**에서 폐쇄 약4.23mm → 개방 **1.631mm**. 경계상태가 진단결과에 매우 큰 영향을 준다. 다만 141mm 같은 국지 순퇴적은 여전히 과대/비현실적일 수 있고, 바로 현장예측에 적용 불가.
- 50mm/h 혼재 ON에서 새 원토양 박리 `25.06987m³ solid`, 경계 배출 유사 `21.40471m³ solid`, 경계 배출 물 `744.60660m³`, 내측 셀 최대 순퇴적 `141.487mm`. 같은 혼재 조건 수관 OFF는 박리 `25.44071m³`, 경계 배출 유사 `21.62747m³`, 물 `752.80508m³`, 최대 퇴적 `142.524mm`. 혼재 사면 ON/OFF 차이는 지표 피복 FCG 고정 + PET0에서 canopy interception component 차이 반영.
- 각 시나리오 실제 synthetic soil inventory 10mm loose layer, downstream edge 4m; 0.5–2m 같은영역 공간수렴 미검증. **원본 지형 DEM은 사건 도중 갱신되지 않는다**. event-end 순고도 `Δz = ΔDLS − Σ GNU dt`은 진단용 후처리. 1ha 미만 실제 고운사 현장적용 전 DEM, LAI, 포기/수관 geometry, 토심, 토양 침식 저항, 암편, 피복률 관측 필요.
- **k=50 경계 배출계수 가정의 영향**: 이 값을 검증하지 않고 이 유역/사면의 실제 개방경계 조건을 재현했다 주장 금지. 후속 k 민감도 시험 우선권 높음. 경계별(outflow by north/south/west/east) 물/유사 배출량은 현재 합계만 확인. 온전한 2D BC 지정, topographic gradient가 내부로 향하는 경계의 유출 여부도 검증 필요.

## 코드
- [native Type5 4방향 개방경계 생성](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_open_all_sides_native_20261027.py)
- [원본 내부 경계 유량/유사량 진단만 추가](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_open_boundary_native_water_audit_20261027.py)
- [7시나리오 독립 강우작업](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_open_one_rain_matrix_20261027.py)
- [실제 전체 35개 병렬실행 워크플로](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/.github/workflows/shetran_open_4edges_full_factorial_20261027.yml)

**판정:** SHETRAN 원본 물리식만으로 동서남북 경계에서 물과 유사가 바깥으로 나갈 수 있는 통합 2D 강우-수관-지표유출-유사수송 모의 기능이 실증됨. **가상사면 원본 기능 검증 통과**. **고운사 현장 정량 침식/퇴적 예측 및 최종 모델 채택은 정교한 outlet boundary, 공간격자 수렴 및 현장교정 전까지 보류**.
