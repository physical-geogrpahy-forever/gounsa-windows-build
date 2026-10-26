# 2026-10-26 고운사 원본 침식엔진 재검색 인계: 계속 엄격한 원본 확인

## 사용자 결정
원본 OpenLISEM 7.5.2 Windows 2D 실제 실행은 완료됐지만 침식 dt nonconvergence, 물리 토층 초과가 확인되어 폐기. 이후 '의심이 되면 버려' 및 '계속 찾으라' 지시: 소스 공개본, quantitative LAI canopy interception, throughfall/leaf drip, *runoff* detachment, soil sediment transport in genuine 2D, mountain/steep precedent, finite sediment/water mass QA and dt convergence required. No claim native model meets all without exact code and native numerical validation.

## 이번 세션 핵심 신규 판정
1. **Wflow.jl current official native code actually inspected:** source `Deltares/Wflow.jl/Wflow/src/vegetation/parameters.jl`, `vegetation/canopy.jl`, `vegetation/rainfall_interception.jl` show actual LAI/canopy storage/gap, Gash/Rutter, `throughfall,stemflow,interception`. `Wflow/src/sediment/erosion/rainfall_erosion.jl` EUROSEM native canopy-height/interception rain detachment; `overland_flow_erosion.jl` ANSWERS based on q + USLE soil C/K. **BUT** `sediment_transport/overland_flow_transport.jl` invokes `accucapacityflux_rate!(...,network,...)`, routed by a directed land network, not true 2D conservative sediment transport. Modern `wflow_sbm` 2D local inertial optional hydrology DOES NOT demonstrate 2D sediment native. **REJECT strict one-model engine**; keep original canopy + erosion equations as scientifically useful source-verified bench.
2. **tRIBS-FEaST model published 2013 and 2014:** Kim, Ivanov & Katopodes (2013) WRR 49, 5134–5154 DOI 10.1002/wrcr.20373, fully coupled 2D Saint-Venant + Hairsine-Rose; Kim, Han, Cho (2014) DOI 10.9798/KOSHAM.2014.14.5.351. But current official MIT `tRIBS-Model/tRIBS` v6 source `tHydro/tIntercept.cpp` Rutter dynamic canopy and `tHydroModel.cpp` `LAI_LU` exists; code tree contains **NO actual FEaST Hairsine-Rose sediment module**, nor source-only integrated 2013 code, thus published genuine 2D architecture ≠ downloadable matching runnable source. **REJECT native all-in-one**; reference paper-only.
3. **FeST (Politecnico di Milano)** official Fortran GPL Chisel, detailed FORD `Sediment.f90`, LAI-responsive canopy `Cmax LAI/LAImax`, interrill/river erosion; but sediment uses `sedFlowDirection`, `sedReach`, Muskingum–Cunge and USLE parameters, NOT full 2D hillslope flow-driven sediment flux or rill incision. **REJECT**.
4. **Song et al. (2024) Korean Naerincheon SSEM** DOI 10.7744/kjoas.510312 ~829km² >90% forest mountainous rain-runoff DR+DF true physically interpreted; original published `∂h/∂t+∂q/∂x=r` **1D kinematic flow path**, 250m cells, sediment observation from rating curve and per-event calibrations, no LAI canopy nor public source. **REJECT** as native complete highres engine; Korean forest secondary ref.
5. **HydroPol2D** actual GPL MATLAB code `interceptionModel.m`: `S_max=C*LAI`, output throughfall/canopy evaporation; 2D local inertial overland; but native pollutant buildup/washoff coefficient simulation not physically-based soil sediment detachment/deposition. Original repo `marcusnobrega-eng/HydroPol2D`. **REJECT**.
6. **HydroSed2D Penn State** open GPL true 2D SWE+sediment but no demonstrated canopy LAI interception/leafdrop, **REJECT** one native model.
7. **WASA-SED** University Potsdam semi-distributed, **REJECT genuine 2D**.
8. **ParFlow** open physically rich 3D groundwater + 2D surface + plant canopy but no native verified hillslope sediment detach and deposition, **REJECT**.
No new time-step native erosional stability test was run for any of these because each fails a prerequisite code/process gate. Do NOT call valid paper software broken; they simply do not pass this research-specific combined requirement.

## Archive writes and provenance
- NEW `papers/2013_Kim_Ivanov_Katopodes_tRIBS_OFM_HairsineRose.md`
- NEW `papers/2014_Kim_Han_Cho_tRIBS_FEaST_Combined.md`
- NEW `papers/2024_vanVerseveld_WflowSBM_LAI_Source.md`
- NEW `papers/2024_Song_SSEM_NaerinForestStormErosion.md` (canonical)
- NEW `models/Wflow_Sediment.md`, `models/tRIBS_FEaST.md`, `models/FeST.md`, `models/HydroPol2D.md`
- NEW `decisions/2026-10-26_WFLOW_TRIBS_FEST_SSEM_STRICT_SOURCE_GATE.md`, includes 2nd-pass HydroPol2D/HydroSed2D/WASA-SED/ParFlow.
- UPDATED `MASTER.md`, `INDEX.md`.
- Accidental duplicate Song manuscript file `papers/2024_Song_SSEM_Naerincheon_PhysicalErosion.md` was **deleted** after verifying canonical alternative, no duplicate remains.

## Next defensible task
Continue searching **not yet tested candidate native source lines** where original, released same version truly includes BOTH LAI-interception+leafdrop rainfall energy AND genuine 2D conservative multi-class sediment advection with finite loose-layer shield. If none, do not loop rejected models: compare original-source-preserved canopy and published 2D numerical architecture as **new coupling ONLY** after user accepts custom model development. Main engine remains **unselected**.

Source pointers:
https://github.com/Deltares/Wflow.jl
https://doi.org/10.5194/gmd-17-3199-2024
https://doi.org/10.1002/wrcr.20373
https://doi.org/10.9798/KOSHAM.2014.14.5.351
https://github.com/tRIBS-Model/tRIBS
https://www.fest.polimi.it/doc/module/sediment.html
https://www.kjoas.org/articles/xml/P91L/
https://github.com/marcusnobrega-eng/HydroPol2D
https://water.engr.psu.edu/liu/hydrosed2d.html
