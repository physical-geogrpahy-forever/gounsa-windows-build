# 고운사 연구 인계: 2026-10-26 17:32 KST

## 이번 세션의 목표
앞선 장시간 채팅 연결 끊김 이후 고운사 물리 유수침식 모델을 새로 처음부터 시작하지 않고 이어간다. 최우선 3조건: (1) LAI/식생량·구조 기반 수관차단과 수관저류 및 수관통과(수간유하는 낮은 우선순위), (2) 명시적 직접유출 박리, (3) 산지/급경사 실제 적용.

## 이번에 새로 찾은 문헌
- Opedes et al. (2025), *Modelling the impact of trenches on soil erosion control using OpenLISEM on Mount Elgon, Uganda*, *Earth Surface Processes and Landforms* 50(6), e70074. https://doi.org/10.1002/esp.70074
- 급경사지 Mount Elgon Ukha 44.5 km², 12.5 m cells, 15 s timestep, 2D dynamic wave; 실제 지표수문 및 시나리오 토양유실. 조사한 trench 설치지의 82% 경사 10–30°: 전체 유역 경사 비율 아님.
- measured stream discharge calibration NSE 0.72/KGE 0.61; 유사 실측 부재로 토양침식 독립 검증 불가능.
- Correction https://doi.org/10.1002/esp.70154 존재; 세부 내용 추가 확인 대상.
- 새 논문별 파일: `../papers/2025_Opedes_OpenLISEM_MountElgon_Trenches.md`.

## 이번에 원본에서 재검증한 식과 프로세스
- `vjetten/openlisem`, branch `main_C`, SHA `d894c72428947247ce49eb88353dadf49b3123e8`.
- `hydro/lisInterception.cpp`: `k=1-exp(-0.45*LAI)`; `CS=Smax*(1-exp(-k*RainCumInt/Smax))`; `LeafDrain = max(0,Rainc - Delta CS)`; `RainNet = Cv*LeafDrain+(1-Cv)*Rainc`.
- `model/lisDataInit.cpp` LAI-dependent Smax with categories `0.2856*LAI`, `0.59*LAI^0.88` (mm, stored as m), custom `smax.map` possible, no Gounsa calibration demonstrated.
- `erosion/lisErosionSplash.cpp` separate direct rain and leaf-drip kinetic energy, stone and grass strip shielding; `erosion/lisSWOF2DSediment.cpp` 2D runoff detachment, suspended sediment movement/deposition; `flow/lisOverlandflow.cpp` actual FullSWOF2D dynamic solver on DEM.
- Important negative result: `StemflowFraction` declared in header but data-read and GUI value mapping are commented out. Native local SF calculation unverified.
- Sediment-derived in-event or interevent DEM elevation updating not established as existing model behavior: externally performing it is a **new coupling**.
- Native LPJ-GUESS FineRootC→extra cohesion, automatic dynamic root biomass conversion and fire-spall degradation are not available by default.

## 판정 변화
- OpenLISEM now strongly supported for the three simplified criteria at source + published real steep-slope application level, but still not completely validated native Gounsa engine.
- Do not assert Windows 7.5.2 setup equals inspected main_C SHA, or that earlier Linux Qt6/QWT failed build is fixed. No OpenLISEM original executable run or independent water/sediment mass budget QA in this chat.
- Stronger old requirement genuine2D+native live/dead RLD etc still unfulfilled, consistent with `MASTER.md`.

## 이번 세션에서 GitHub에 저장한 파일
1. `../papers/2025_Opedes_OpenLISEM_MountElgon_Trenches.md` (NEW)
2. `../decisions/2026-10-26_OPENLISEM_THREE_CRITERIA_SOURCE_AND_STEEP_SLOPE_AUDIT.md` (NEW)
3. `../models/OpenLISEM.md` (UPDATED)
4. `../MASTER.md` (UPDATED)
5. `../INDEX.md` (REBUILT from GitHub actual tree): Papers 430, Models 83, Decisions 57, includes CSV.
6. This session handoff (NEW).

## 바로 다음 시작 지점
1. 설치형 Windows openLisemSetup_7.5.2.exe 원본으로 *기존 공식 예제* 실제 실행 환경 확보. 동일 소스 해시 및 바이너리 출처 검토. 이전 Linux Qt6/QWT 컴파일 반복하지 않음.
2. 수관 저장 및 강우 수지 단계별 검사: total incident rainfall = throughfall + canopy storage increment + interception evaporation etc, 시간 누적/단위 확인.
3. 지표유출, splash, runoff-flow detachment, deposition, outlet sediment, mass budgets 별도 검증. 원본 공식 예제가 수문 전용이면 erosion 활성 예제를 따로 찾아서 입력 검사.
4. 고운사 동일 DEM, soil, boundaries에서 가상 억새 vs 참나무 맹아 canopy LAI/height/Smax/litter/roots sensitivity at 10,20,30,40,50 mm/h for 1h. 실제 생태/침식 데이터로 오인 금지. 침식 신호가 거의 없을 경우 canopy->rain energy->detachment 경로 활성/조건을 점검.
5. 이전 EUROSEM, SWEHR 임의계수 포크 등에서 나온 가상 산출을 OpenLISEM 원본 결과라고 쓰지 말 것.
