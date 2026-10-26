# Song et al. (2024) — SSEM on mountainous Naerincheon forest watershed

## APA reference
Song, M. G., Kim, Y. H., Choi, C. U., Nguyen, V. L., & Yeon, M. H. (2024). Spatial analysis of soil erosion and deposition using physics-based distributed model. *Korean Journal of Agricultural Science, 51*(3), 375–389. https://doi.org/10.7744/kjoas.510312

## Why examined
One of few studies showing a concrete physically based rainfall/overland erosion model on a real **Korean steep mountainous forest basin**, but must test hydrodynamic dimension, native LAI and original source rather than relying on model label.

## Methods and location
Naerincheon basin, Gangwon/Inje, area ~829km² and forest >90%, steep mountainous upper subbasin. 2020 three storm events, hourly rainfall data from eight weather stations, Thiessen weighted precipitation, DEM resampled to **250m**. Runoff cross-validated against stage-to-flow rating curve, suspended sediment against **Q-SS rating relation** rather than continuously sampled event sediment. Every event parameters calibrated separately, so sediment NSE .63/.71/.62 and runoff NSE .43/.68/.70 are NOT independent space-time validation of per-cell morphological changes. Sediment peak ratio .55/.54/.78 (underprediction).

## Equations and actual implementation scope
Surface, saturated and unsaturated water `q(h)` with single flow-path kinematic PDE `∂h/∂t+∂q/∂x=r(x,t)`. DEM-derived flow direction/accumulation. Sediment continuity along x path `∂(h_s C_s)/∂t+∂(q_s C_s)/∂x-E_N=0` where raindrop `DR=k KE exp(-b h_s)`, `KE=a r`; overland-flow `DF=α(TC/1000-C) h_s`, sediment TC by Yang (1972) unit stream power with d50 and settling velocity. Equations 1–8 literally printed in full original XML. Although distributed raster and field slopes up to 40°, governing equations are **1D kinematic network**, not genuine 2D SWE. No documented `LAI`, Rutter/Gash canopy store/throughfall or plant-specific leaf drip kinetic in original SSEM methods. Actual source code licence, release and executable tests not found.

## Conclusion for Gounsa
**Reject** as original native 2D canopy-interception+erosion primary solver; regional Korean mountain forest 10–50mm/h storm erosion secondary methodological benchmark with observation/calibration caveats. Distinct from original 2010 SSEM and from OpenLISEM.

## Original XML
https://www.kjoas.org/articles/xml/P91L/
