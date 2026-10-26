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
