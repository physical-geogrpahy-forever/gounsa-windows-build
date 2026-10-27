# 2026-10-27 Classic OpenLISEM 7.5.2 원본 코드와 기존 Windows 수치시험 재감사 — NO-GO 유지

## 목적 및 선행 판단
2026-10-27 채팅에서 원본 OpenLISEM 7.5.2가 5–10cm/LAI/2D 침식 원본 후보라고 다시 언급되었으나, 2026-10-26 네이티브 12회 실패를 누락한 잘못된 권고였다. 본 감사는 GitHub 공개 태그 `v7.5.2`, `main_C` HEAD와 고운사 GitHub Actions 원본 재현 로그를 교차 검증한다. **원본 7.5.2 주모델 NO-GO는 철회되지 않는다.**

## 1. 원본 계보 및 코드 대조
- 공개저장소 https://github.com/vjetten/openlisem ; 감사 기준 **태그 `v7.5.2`**, 공개 배포 Windows installer `openLisemSetup_7.5.2.exe`, SHA256 `f8a5722ed0b370f32fb3dae5c55465427abe75b1155b50bf12aa5516d6b4ca79` (Windows Action 설치 단계에서 확인).
- `main_C`는 `v7.5.2`보다 8커밋 앞서 있으므로 같은 체크아웃으로 혼동해서는 안 된다.
- 동일 Git blob SHA:
  - `hydro/lisInterception.cpp`: `fd3cac3999c5b26cfeb2612d330f468f66de3563`
  - `erosion/lisErosionSplash.cpp`: `7f75a144c2fdc12dd3781708643c1b4dff9fbffa`
  - `erosion/lisErosionAux.cpp`: `019a31f7233352c9347407906b9f641e27e60582`
  - `erosion/lisSWOF2DSediment.cpp`: `683eb85b59da4a74b95363374efb223c094e933b`
  - `flow/lisBoundary.cpp`: `3c2251ca9c381756e4bc1a6f05f21fae29f71bf0`
- 차이가 있는 `flow/lisSWOF2DopenMUSCL.cpp`: tag `c7fd45b59c4bdd15066ffc8078ca044e7d03c68e` / main_C `b6cc361c3513e8b09c6038c6b7ef86b5b450e801`. 비교결과 이 파일에 +14/-2줄 변경. main_C에서 유사 계산 및 침전속도 코드 자체는 그대로이므로 **새 브랜치에서 오류가 고쳐졌다고 단정하지 않는다**.

## 2. 태그 v7.5.2 실제 통합 실행 경로
- `model/lisModel.cpp::HydrologyProcesses` -> `hydro/lisInterception.cpp::cell_Interception`에서 LAI/피복도/수관저류량을 사용하여 유효강우를 산정.
- `erosion/lisErosionSplash.cpp::SplashDetachment`는 직접강우와 수관낙수의 운동에너지를 별도 계산해 빗방울 박리 모의.
- `flow/lisOverlandflow.cpp::OverlandFlow2Ddyn` -> **`fullSWOF2openMUSCL`** (실제 현재 사용되는 2차원 유동. `fullSWOF2open`은 OBSOLETE) -> `SWOFSediment(dt_cfl,...)` -> `SedimentSSContinuous` -> `SWOFSedimentAdvection`.
- `flow/lisSWOF2DopenMUSCL.cpp`의 `Boundary2Ddyn(_dt,...)`가 경계 유출/유사 배출 수행; `FlowBoundaryType=1`이면 개방 경계.

## 3. 코드 수준 위험 검증
1. **침전속도 분기 불연속**: `erosion/lisErosionAux.cpp::GetSV(d)`. `d<100 µm` Stokes, `d>=100 µm`에서 `dm=d/1000.0; 10.0*sqrt(1.0+0.01*(1.65*GRAV*dm^3)-1.0)/dm`. 전례 숫자 실험 99.9µm 약 0.0089745m/s, 100µm 약 1.272262m/s (약 142배). 100µm 수치의 적절한 SI 계산값 약 0.00779m/s. 단독 원인 인과관계는 독립 수정 A/B 실행으로만 확정 가능.
2. **유한 토사저장량 미제한**: `SedimentSSContinuous`의 `DetachMaterial(...)` 호출 주석 처리, 농도제한용 `if(SS+detachment>MAXCONC*sswatervol)` 주석 처리. `MaxConcentration`은 농도 산정함수이지 토양 질량저장고 검사는 아님. 25cm 수문토심은 자동으로 최대 침식 가능 토사량이 되지 않는다.
3. **CFL 하한 위험**: `flow/lisSWOF2DopenMUSCL.cpp::findSmallestCFLdt`의 `qMax(TimestepfloodMin,dt_req_min)`; 0.05–0.1m 격자에서 필요한 물리 CFL보다 사용자가 지정한 minimum timestep이 길면 시간증분이 제한을 위반할 위험. UI/기본 runfile의 디폴트가 달라 명시 입력과 내부 로그 검증 필요. 실제 cm 시험으로 성능 확인하지 않았음.
4. **병렬 쓰기 경쟁 가능성**: `SWOFSedimentAdvection`의 OpenMP 병렬 루프 안에서 주변 셀 공유버퍼 `tma/tmb/tmc/tmd->Drcr += flux[i]` 직접 쓰기. atomic/reduction 없음. 실제 경쟁 및 결과변동 여부는 1core/다중core native 대조 미실시, **잠재 결함**으로만 표시.
5. **후처리 물수지 보정**: `correctMassBalance(sumh,h)`가 내부 유동 뒤 수심을 일괄 보정. 종료 시 전역수지 폐합만으로 개별 유량/유사물리 정당성 확인 불가능.
6. `SWOFSediment`는 유동 내부 timestep으로 호출되어 있으므로 '외부 timestep 전체에 유사 계산'이라고 단정하지 않는다. 5/10/20초 비교는 외부 시간간격 민감도.

## 4. 이미 실제로 시행한 Windows 원본 네이티브 계산
- 2026-10-26 https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304135775 : workflow job `121508937649` **success**, 실제 12회 원본 실행. 100m×100m, 5m grid, 25% 경사, 20mm/h 1h 이후 10분 배수. 자유 2D 경계 `Flow Boundary 2D=1`, 고급 옵션 활성, 원본 침전속도 기본식 SV=1/대체식 SV=3.
- 유사유출 kg/ha:
| 식생 / SV | 외부 Δt=5s | 10s | 20s |
|---|---:|---:|---:|
| Oak SV1 | 0.005993 | 123.037727 | 832.588686 |
| Oak SV3 | 0.030954 | 28.707586 | 268.530307 |
| Miscanthus SV1 | 0.004050 | 0.007095 | 238.256810 |
| Miscanthus SV3 | 0.018893 | 0.044177 | 88.121322 |
- 전역 water/sediment balance는 원본 출력 기준 폐합됐지만 시간간격 수렴은 불합격.
- Oak SV1 Δt20s 한 격자 순침식 5982.9t/ha > 가상 25cm 토심 × 1350kg/m³ = 3375t/ha.
- 1/2초 추가 실행 https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304815539 : job `121511206049` **failure**, 1s 억새 양쪽 SV 실행 각각 480초 시간초과, workflow 20min timeout. **수렴 입증 실패이며 안정성을 반증하는 독립 수치 결과도 아님**.
- 별도 2m 실행 https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40303685346 : job `121507441094` **failure**, 개별 실행 100초 제한으로 전부 timeouts, 30min workflow timeout. 유효 숫자 결과 미획득.
- 상세 최초 원자료 감사: [기존 원본 NO-GO 보고](2026-10-26_OPENLISEM_752_NATIVE_2D_STABILITY_FAILED.md), [과거 실패 복구](2026-10-26_OPENLISEM_752_PREVIOUS_NUMERICAL_FAILURE_RECOVERY.md).

## 5. 논문 선행사례의 정확한 범위
- Maggioli et al.(2022), https://doi.org/10.3389/fevo.2022.765148 : Classic LISEM 계열 5cm LAI 기반 수관저류 + 침식 모델링 **진실**, 라우팅은 kinematic wave, genuine freely spreading 2D SWE 적용 아님. 정확 사용 버전 및 원본 artifact 미특정.
- Cuomo(2018), https://doi.org/10.19199/2018.3.0557-1405.31 : LISEM 10cm canopy/erosion 선례지만 exact 2D/버전 불특정.
- Epple et al.(2025), https://doi.org/10.1002/esp.70127 : 1cm **신형** Bastian van den Bout LISEM 계열, 해당 run 수관차단 활성화 여부 및 해당 2025 공개 소스 동일성 불명. Classic 7.5.2과 서로 다른 엔진.

## 최종 판정 및 중단규칙
**Original Classic OpenLISEM v7.5.2 = 고운사 유수침식 주모델 NO-GO 유지.** 코드에 모듈 존재만을 근거로 고해상도에 다시 추천하지 않는다. 5cm Classic kinematic 선례를 5cm 자유 XY 2D 모형으로 과장하지 않는다. `main_C` 8커밋 증가도 QA 재통과 증거 아님. 1/2초 및 2m timeouts을 성공 또는 새로운 유사 수치로 취급하지 않는다.
**SHETRAN 4m 시험을 5cm 논문선례로 둔갑시키지 않는다.** 요구한 5–10cm + LAI 수관 + 직접강우/유수박리/퇴적 + genuine 2D + matching publicly runnable original을 현재까지 입증하지 못했으므로 주모델 선정 보류. 추후 조사 대상은 기존 기각 모델의 일반 홍보가 아니라 정확 논문-코드-실행판-실제 매개변수 및 수치 QA 연결 자료이다.
