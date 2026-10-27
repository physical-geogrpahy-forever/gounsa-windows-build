# Doten et al. (2006) DHSVM 산림산지 유사모형

## 서지정보
Doten, C. O., Bowling, L. C., Lanini, J. S., Maurer, E. P., & Lettenmaier, D. P. (2006). A spatially distributed model for the dynamic prediction of sediment erosion and transport in mountainous forested watersheds. *Water Resources Research, 42*. https://doi.org/10.1029/2004WR003829

## 이 논문을 검색한 이유
고운사에서 요구하는 산림 수관차단, leaf drip + surface runoff detachment, mountain watershed 선례를 단일모형이 제공하는지 검사.

## 연구유형과 공간구조
Spatially distributed DEM grid model and catchment scale; hillslope overland routing is explicit finite-difference **kinematic wave**, sediment is modified SHESED transport equation. DO NOT call the 2D sediment conservation formulation a genuinely 2D shallow-water hydraulics solver. Published application: Rainy Creek, east Cascade mountains, Washington, USA.

## 모델 과정 / 방법론
DHSVM hydrology provides saturation and infiltration excess runoff, canopy leaf drip, rainfall, channel discharge. Event hillslope detachment is separated into rainfall impact, canopy leaf drip and flow detachment. Roads/channel flow and stochastic mass wasting can also supply sediment. Overland kinematic routing uses Courant stability; sediment transport capacity constrains concentration and exports.

## 식생 입력
DHSVM two-storey canopy and LAI-dependent interception are documented in Thyer et al. (2004) and in subsequent official DHSVM publications, including overstory/understory capacity. Doten DHSVM uses leaf-drip input into sediment detachment. Dynamic root RLD-dependent erodibility unverified. Native vegetation impact in the published paper must not be generalized to real field Gounsa erosion validation.

## 핵심 식 / 모수 / 단위
Doten et al.'s flow detachment depends on overland transport capacity, settling velocity and a coefficient from soil cohesion; detachment components feed finite difference advection. Dimensions: runoff Q [m3/s], sediment concentration [m3 sediment/m3 water], time step [s], raindrop/leaf drip energy and sediment [kg, as applicable]; do not invent numerical coefficients from abstract only.

## 원본 소스 실제 확인 (2026-10-26)
Official [PNNL/DHSVM-PNNL](https://github.com/pnnl/DHSVM-PNNL) `DHSVM/sourcecode/` file listing includes `InterceptionStorage.c`, `RouteSurface.c`, `MassEnergyBalance.c` but **no Doten-style erosion/soil sediment transport code files in entire official model source root**. `MainDHSVM.c` + `CMakeLists.txt` do not reveal a compiled sediment module; the 2018 v3.2 release tree is principally hydrology. Historical Doten (2006) published extension must NOT be assumed directly executable using current PNNL code. Unmodified native 2D full-hydrodynamic criterion is also not met (official repo README default D4 neighbor routing, optional D8).

## 고운사에서 쓸 수 있는 부분과 새 coupling
LAI/overstory-understory canopy equations, rainfall interception, leaf drip and mountain forest calibration literature can inform a separate hydrologic benchmark. Reconstructing Doten erosion code from paper or coupling another erosion model is **new implementation/coupling**.

## 한계 및 최종 판정
**통합 원본 엔진으로 제외**, mountain forest canopy+splash/runoff process literature as a supportive case only. Full published erosion module source not verified in the official PNNL downloadable tree. Prior published sediment work is not sufficient evidence for runnable release. No program build/run in this investigation.

## Sources
https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2004WR003829
https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2017MS001120
https://github.com/pnnl/DHSVM-PNNL
https://www.pnnl.gov/projects/distributed-hydrology-soil-vegetation-model


## 2026-10-27 매우 중요한 공개원본 발견: 과거 '침식 C 코드 미확보' 판정 정정

**기존 위쪽 기록은 `pnnl/DHSVM-PNNL`만 확인했으므로 불완전했다.** [`jhamman/DHSVM` master](https://github.com/jhamman/DHSVM)에는 실제 **Doten-era LAI 수관차단·적하 운동량·빗방울 및 유수박리·사면유사 및 하천유사수송 코드가 공개**되어 있다. [상세 새 모델 원본감사](../models/DHSVM_Doten_2006_Original_Open_C_Sediment_Canopy_Execution_Path_2026.md) 참조. 새 논문으로 중복 등록하지 않음.

- **원본 소스 모두 Makefile 빌드 목록에 존재:** `makefile` blob `d3aea1b578d5b07dc5c2e6241c29eefac551f904`; `InterceptionStorage.o`, `MassEnergyBalance.o`, `InitNewMonth.o`, `RouteSurface.o`, `RouteChannelSediment.o`, `CalcBagnold.o`, `InitSedTables.o`, `InitSedMap.o`.
- **LAI 수관차단 활성 연산:** `InitNewMonth.c L114–116` `Smax=LAI×Fract×LAI_WATER_MULTIPLIER`, `InterceptionStorage.c L45–65` canopy S(t), net rainfall and leafdrip vs direct throughfall moment-squared; `MassEnergyBalance.c L270–274` 이 함수를 호출. `RouteSurface.c L284–331`은 `MomentSq`를 강우박리에 사용하고 유수흐름과 입경별 수송능/하천퇴적 계산.
- **저자 실제 논문** Rainy Creek **30m 계산격자 49,085개**, 수문 강제/모의 **3시간 간격** (Wiley full text §3). 2D 지역의 데이터 수집=5cm numerical 2D run 아님. 문헌 §2.2 표면유수는 **kinematic wave**, 세립 토사 무한 공급 가정. 미세격자 mass-wasting과 표면침식 30m 해상도를 혼동 금지.
- **완전히 새로 발견된 원본 정적결함 4개** (`RouteSurface.c` source):
  1. **나지일 때 `DR=0`** (`if no OverStory and no UnderStory` L293–295), 하지만 `MassEnergyBalance.c L277–279`은 나지에 `MomentSq=MS_Rainfall`을 계산한다. 이는 고운사 나지/억새/참나무 비교의 강우박리 오류로 이어질 수 있음.
  2. rain-induced DR 계산이 **`sedoutflow>0`, `h>0.001m` and `streampower>0.004` 조건 속에 묶임**: 얕은 무유출에서 빗방울 박리 계산 미실행.
  3. `RouteSurface`가 vegetation matrix인 `VType[]`를 받음에도 rain detachment은 `VType->OverStory`, `VType->Fract`로 **첫 식생유형만** 참조; 다른 hydrological/impervious branches에는 `VType[VegMap[y][x].Veg−1]` 사용. **패치별 수관종류를 박리 수식에 전달하지 않는 결함 후보**.
  4. `MassEnergyBalance.c L215–220`의 `if(RainfallIntensity>10)`과 바로 아래 `else if(10≤intensity<100)`은 중복돼 후자 분기가 **정확히10mm/h만 선택**; 10–50mm/h 대부분 첫 계수만 사용.
- **유동 자유2D 불충족**: `RouteSurface.c L392–405` `TopoMap.Dir[n]/TotalDir` 양수 방향 분배, `SedimentFlag L595–599` 침식 켠 순간 `kinematic routing` 강제. 양쪽 자유 x/y SWE 해법 아님.
- **공개 소스 존재 = 2006 논문에 사용된 정확 같은 SHA 아니며, 실험 입력파일 없음, native 빌드·실행·질량수지 미검증**. `makefile` 주석 2006 Oct가 논문 첫 발표 Apr 2006보다 늦음. 상단 보고한 원본 미공개 판단은 바꾸되 **고운사 5~10cm 기존 단일모델 채택 탈락**은 변경 없음.

출처: https://doi.org/10.1029/2004WR003829 | https://github.com/jhamman/DHSVM
