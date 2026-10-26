# SEIMS 원본 2D 및 침식 소스 감사 — 2026-10-26

## 실체
GPL-3.0, [lreis2415/SEIMS](https://github.com/lreis2415/SEIMS); Zhu et al. (2019) *Environmental Modelling & Software* 122:104526. Native C++ framework, erosion modules and real examples exist, cross-platform.

## 실제 함수
- `modules/erosion/SPLASHERO_PARK/SplashEro_Park.cpp` separate splash detachment, requires canopy **cover fraction** and other factors, not original measured LAI-linked leafdrip source.
- `modules/erosion/KinWavSed_OL/KinWavSed_OL.cpp` passes `m_DETSplash`, executes flow detachment and receives upstream sediment, `GetSedimentInFlow`, `CalcuFlowDetachment`, subsequent sediment routing. This is **kinematic wave network** not native full 2D spatial lateral sediment shallow-water law.
- `modules/hydrology/CASC2D_OF/CASC2D_OF.cpp` includes overland model and `m_flowOutIndex` and downstream routing; cannot infer full 2D coupled sediment solely from CASC2D model label.

## 고운사 기준
Original source YES, separate rain and runoff detachment YES, exact native LAI canopy-storage/leafdrip energetics UNKNOWN/NO evidence; true 2D sediment grid-face conservative flux FAIL native positive proof; steep burned forest observed sediment validation NO. Reject as native main engine before numerical sensitivity tests. Published hydrologic application not false, rather all-native fit fails.

## 참고
[Zhu 2019](../papers/2019_Zhu_Parallelized_SEIMS_Framework.md)
