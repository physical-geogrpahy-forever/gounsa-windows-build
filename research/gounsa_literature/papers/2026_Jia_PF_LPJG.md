# Jia et al. (2026) PF-LPJG

## 서지정보
Jia, Z., Chen, S., Fu, Y. H., Martín Belda, D., Wårlind, D., Olin, S., Xu, C., & Tang, J. (2026). Advancing ecohydrological modelling: coupling LPJ-GUESS with ParFlow for integrated vegetation and surface-subsurface hydrology simulations. *Geoscientific Model Development*, 19, 1727–1747. https://doi.org/10.5194/gmd-19-1727-2026

## 이 논문을 검색한 이유
고운사 기준 3의 정확한 의미인 `외부 토양-지형/수문모델이 계산한 상태를 vegetation model에 주입하여 생장과 수분스트레스를 갱신할 수 있는가`를 직접 구현한 현대적 published precedent를 찾기 위해 검토했다.

## 연구 유형
Model coupling / ecohydrology model development and basin-scale evaluation.

## 공간구조
- ParFlow: fully distributed 3-D surface-subsurface hydrology
- LPJ-GUESS: geographic grid cells with dynamic vegetation
- published Danube experiment: 10 km grid
- within LPJ-GUESS cell, demographic patch/cohort structure remains spatially implicit

## 적용환경
Danube River Basin, Europe, across humid/semi-arid and mountain-to-lowland environments.

## 핵심과정
- ParFlow 3-D variably saturated subsurface flow
- overland flow
- groundwater redistribution
- topographic lateral flow
- LPJ-GUESS vegetation productivity and dynamic vegetation
- two-way daily vegetation-hydrology coupling

## 식생입력
LPJ-GUESS dynamic vegetation including plant functional types and demographic vegetation structure. The published Danube experiment was not designed as a fine-scale postfire understory study.

## 핵심 coupling
The authors modified LPJ-GUESS soil discretization to four variable-depth layers:
- 0.1 m
- 0.3 m
- 0.6 m
- 1.0 m
- total 2 m

to align with ParFlow soil columns.

Crucially:
1. ParFlow runs hourly.
2. After 24 ParFlow timesteps, LPJ-GUESS reads updated soil moisture and runoff fields.
3. ParFlow soil-water content **overwrites LPJ-GUESS internal soil moisture state**.
4. LPJ-GUESS computes daily P-ET / vegetation water fluxes.
5. These fluxes are disaggregated back to hourly forcing for ParFlow.

Conceptually:

```text
ParFlow hourly x24
 -> soil moisture + surface/subsurface runoff
 -> overwrite LPJ-GUESS soil state
 -> LPJ-GUESS daily vegetation/water calculation
 -> P-ET feedback
 -> ParFlow next day
```

This is direct proof that criterion 3 does not require the vegetation model to own dynamic soil depth or lateral hydrology.

## 파라미터와 단위
- ParFlow time step in coupled workflow: hourly
- LPJ-GUESS exchange interval: daily
- LPJ soil interaction depth in published coupling: 0–2 m
- Danube grid: 10 km
- four LPJ soil-layer thicknesses: 0.1, 0.3, 0.6, 1.0 m

## 고운사에 사용할 수 있는 부분
1. clean external soil-state overwrite architecture
2. two-way root/ET-hydrology feedback
3. proof that LPJ-GUESS can surrender native one-dimensional soil hydrology to external 3-D model
4. direct precedent for `hydrology owns water state; vegetation owns plant response`
5. open coupled code archived on Zenodo, making architecture inspectable

## 필요한 새로운 coupling
For Gounsa fine hillslope use:
- reduce horizontal cell size from 10 km to 10–50 m class
- feed storm-driven soil-depth/layer changes
- conservative remap of soil water, C/N and roots when layer geometry changes
- potentially use a lighter hillslope hydrology/geomorph engine than full ParFlow
- postfire Korean tree/shrub/herb parameterization

Fine-scale geomorphic remapping remains a **새로운 coupling**.

## 한계
1. published validation is coarse basin scale, not 10–50 m hillslope
2. internal LPJ demographic patches remain statistical
3. explicit herb/shrub understory dynamics were not the central demonstration
4. daily vegetation exchange does not reproduce within-storm plant demographic response, although hourly hydrology is retained
5. ParFlow adds substantial computational/infrastructure complexity

## 최종 판정
**강하게 유지: strongest modern direct precedent for criterion 3.**

Five criteria:
- spatial cohort/grid: geographic grid YES, within-cell cohorts spatially implicit
- explicit understory succession: GOOD architecture, application evidence incomplete
- soil/geomorph coupling readiness: EXCELLENT / direct two-way implementation
- watershed/topography: EXCELLENT
- <=daily: YES, hourly hydrology + daily vegetation exchange
