# tRIBS-FEaST: published 2D hydrology and Hairsine–Rose, original open-source sediment not present in released tRIBS

## Published original
Kim, Ivanov, and Katopodes (2013) WRR 49, 5134–5154, DOI 10.1002/wrcr.20373 and Kim, Han, Cho (2014), KS Hazard Mitigation, DOI 10.9798/KOSHAM.2014.14.5.351. True coupled unstructured-grid 2D Saint-Venant + Hairsine–Rose particle-size-aware separation between original soil and deposited layer. Surface runoff and rainfall detachment in one published numerical framework. Flume and experimental catchment verifications, notably Lucky Hills Arizona. 2023 Kim et al WRR study uses same physics but impervious infiltration assumption in that application's simulations.

## Latest official source audit
- https://github.com/tRIBS-Model/tRIBS, **fully open MIT source** and bundled benchmarks, current released tRIBS v6 hydrology.
- `src/tHydro/tIntercept.cpp::InterceptRutter` solves dynamic canopy storage C(t) with net rainfall, throughfall, drainage and evaporation using Runge-Kutta and Rutter capacity `coeffS`, drainage `coeffK exp(coeffb*(C-S))`; `src/tHydro/tHydroModel.cpp` maps `LAI_LU` as a land-use vegetation state.
- Yet source tree does **not** include a corresponding sediment/erosion finite volume Hairsine–Rose solver: `Hairsine` GitHub code search finds nothing, generic `erosion`/ `sediment` only in unrelated `tMeshList.h`. Thus **tRIBS v6 hydrology source is NOT the 2013/2014 complete tRIBS-FEaST original code**.
- Even where canopy Rutter exists, the exact native integration between canopy leafdrip energy and HR sediment in original published author source is **not directly verified**. LAI exists in hydrology but impact on `coeffS` is not guaranteed; do not infer automatically.

## Status
**Reject as publicly auditable runnable Gounsa original integrated erosion engine**, despite excellent true 2D scientific process paper. Historical software may have been implemented and validated; lack of code match does not refute paper. Do not use 2026 hydrology alone and assume full published sediment results can be reproduced.

## Citations and files
https://doi.org/10.1002/wrcr.20373
https://doi.org/10.9798/KOSHAM.2014.14.5.351
https://github.com/tRIBS-Model/tRIBS
[Kim 2013](../papers/2013_Kim_Ivanov_Katopodes_tRIBS_OFM_HairsineRose.md)
[Kim 2014](../papers/2014_Kim_Han_Cho_tRIBS_FEaST_Combined.md)
[Kim 2023](../papers/2023_Kim_tRIBS_FEaST_HairsineRose.md)
