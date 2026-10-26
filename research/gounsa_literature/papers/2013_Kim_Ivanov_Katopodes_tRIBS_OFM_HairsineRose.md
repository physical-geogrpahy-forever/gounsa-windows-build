# Kim, Ivanov, and Katopodes (2013), tRIBS-OFM Hairsine–Rose 2D

## 서지정보
Kim, J., Ivanov, V. Y., & Katopodes, N. D. (2013). Modeling erosion and sedimentation coupled with hydrological and overland flow processes at the watershed scale. *Water Resources Research, 49*(9), 5134–5154. https://doi.org/10.1002/wrcr.20373

## 검색 이유
산림 수관차단과 진정한 2D Saint-Venant 방정식, 토사입경별 Hairsine–Rose 박리 및 퇴적, 유역 수문을 결합한 개발자 원본이 공개됐는지 검사.

## 연구 유형, 방법, 공간구조
Physical watershed hydrology + 2D dynamic shallow water and multi-size sediment mass conservation, unstructured triangular finite volume, Roe approximate Riemann solver. Hairsine–Rose distinguishes original soil and deposited loose sediment, differential rainfall/running water detachment, sediment settling. Numerical benchmark and Lucky Hills (Arizona) watershed hydro and sediment case, 10 events per corresponding 2013 dissertation Chapter 3. Explicit 2D, not D8 disguised. Those benchmarks were for published **authors' integrated FEaST version**, not contemporary official tRIBS v6 executable.

## 원논문의 식생 처리
tRIBS underlying basin hydrology includes interception, evapotranspiration, infiltration, soilwater and water table, with land-use/vegetation parameters. The 2013 research publication does not alone establish **LAI dynamically controlling canopy storage and distinct leaf drip energy within the Hairsine–Rose erosion source**. Underlying tRIBS hydrologic model has Rutter canopy as separate C++ code, but actual compiled FEaST version must be verified.

## 수학/단위
2D SWE water depth h [m], fluxes hu/hv [m²/s], sediment concentration [mass/volume], primary/deposited layer mass per unit bed area; rainfall and runoff erosion differential sources, settling velocity [m/s]. Published paper controls numerical scheme, exact coefficient values and uptake should come from full source or paper; do not invent.

## Source check 2026-10-26
Official source https://github.com/tRIBS-Model/tRIBS (v6.0 family, MIT, actual source tree inspected) provides `src/tHydro/tIntercept.cpp::InterceptRutter` with explicit state `C(t)`, coefficient capacity `coeffS`, canopy drainage `coeffK * exp(coeffb(C-S))`, `throughfall=coeffP*rain` plus drain. `tHydroModel.cpp` reads a `LAI_LU` land-use state.
**Crucial**: official C++ `src/` has no `Hairsine` code-search match and no sediment/erosion solver module in actual source tree; a `sediment` match only in unrelated mesh-list comment. Thus native released tRIBS v6 **is not original paper's erosion engine**. Cannot call Kim 2013 code freely runnable from official tRIBS.

## 고운사 suitability
Genuinely strong original published process architecture: 2D flux with deposition-layer shielding, and canopy water cycle in ecosystem. Gaps: inaccessible/unverified **integrated original FEaST source, release test data and native numerical stability**; demonstrable LAI→splash/leafdrip linkage absent; high-gradient postfire forest validation absent; soil-depth and rock spall dynamic coupling not native.

## 판정
**주모델 채택 탈락** under user's 'doubt → discard' rule; preserve only peer-reviewed coupling and Hairsine–Rose physics reference. Do not reconstruct FEaST and represent it as untouched published source.

## 검증 근거
https://agupubs.onlinelibrary.wiley.com/doi/10.1002/wrcr.20373
https://github.com/tRIBS-Model/tRIBS
https://deepblue.lib.umich.edu/bitstream/handle/2027.42/98011/kjongho_1.pdf?sequence=1
