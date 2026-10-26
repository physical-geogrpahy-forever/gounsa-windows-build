# 2026-10-26 strict original-source search: Wflow.jl, tRIBS-FEaST, FeST, SSEM

## Why
The user requested continued deep search after rejecting OpenLISEM 7.5.2 (native 2D sediment numerics instability) and TREX, Iber+, ASTERIX (essential source/vegetation gaps). Current hard gate: (1) **real original source** and strict LAI or quantitative canopy-water dynamic including throughfall/leafdrip, (2) actual runoff-caused erosion and rainfall splash and sediment mass transfer, (3) mountainous/steep applicability; genuine **2D hydrodynamics and sediment transport**, soil mass, original numerical timestep convergence. For any uncertain major gate, **discard from main engine candidates**; avoid optimistic paper-only promises.

## New source-backed model lineage comparison

| lineage | source identifiable/current | Dynamic quantitative canopy | Actual rain and runoff detachment | Sediment transport 2D | Slope/field precedent | Verdict |
|---|---|---|---|---|---|---|
| **Deltares Wflow.jl + wflow_sediment** | **YES**, MIT Julia `Deltares/Wflow.jl`, `Wflow/src/vegetation`, `src/sediment`, native example TOML + NetCDF | **YES**, LAI/Gash/Rutter and canopy storage/throughfall/wood, separate direct vs canopy drip KE in EUROSEM module; "interception" input is native hydrologic output | **YES**, explicit EUROSEM rainfall splash and ANSWERS flow detachment with USLE factors | **NO**: network `accucapacityflux_rate!` and kinematic-wave flow input, no original 2D sediment advection/Exner rills; separate hydrologic 2D local inertial config is NOT proof sediment uses 2D | Hydrologic catchment studies, no verified Gounsa rill erosion | **REJECT strict native 2D** (excellent physically documented component-level benchmark) |
| **Kim 2013 / Kim Han Cho 2014 tRIBS-FEaST** | Published complete true 2D *paper* exists; current official `tRIBS-Model/tRIBS` MIT C++ **hydrology only**, no FEaST Hairsine–Rose source | Rutter ODE with C, S, drainage and throughfall in current tRIBS; LAI land-use state also in hydrology but LAI→native splash/leafdrip not verified | Published 2013 model true rainfall and runoff erosion via Hairsine–Rose, not accessible same source in v6 repo | In *paper* yes, triangular Roe finite volume; actual v6 executable no | Lucky Hills Arizona and laboratory flume; 2014 Korean paper; 2023 vegetated microtopography study assumed infiltration zero | **REJECT reproducible original release**, reference equation-level only |
| **Politecnico FeST** | **YES** official code Chisel, FORD 2026 docs `Sediment.f90` GPL and canopy module | YES `C_max * LAI/LAI_max` + canopy storage and throughfall | Rainfall interrill and channel erosion; NOT separate native full 2D flow detachment on hillslope | **NO**, `sedFlowDirection`, `sedReach`, channel Muskingum-Cunge; RUSLE C/K interrill source | Italy hydrologic basins, no verified actual 2D steep sediment | **REJECT** |
| **Song et al 2024 SSEM** | Full methods paper open, original model source **unverified** | no native canopy LAI / throughfall impact shown | Yes DR rain `k KE exp(-bh)` and DF runoff `α(TC/1000-C)h` | **NO**, 1D kinematic `∂h/∂t+∂q/∂x=r`, DEM D8 flow paths, 250m grids | **YES** Korean Naerincheon 829 km² >90% forest, 2020 three events, sediment NSE .63,.71,.62 but **Q-SS rating curve** validation and **each event separately calibrated**, peak ratios .55,.54,.78 | **REJECT native 2D LAI / no public source** |

## Original code cross-check

### Wflow.jl precise functional path
- `Wflow/src/vegetation/parameters.jl` has `leaf_area_index`, `storage_specific_leaf`, `storage_wood`, `light_extinction_coefficient`; current time-varying `LAI(t)` controls maximum canopy store and canopy gap.
- `Wflow/src/vegetation/canopy.jl` has `GashInterceptionModel`/`RutterInterceptionModel` output `throughfall, interception, stemflow, canopy_storage`.
- `Wflow/src/sediment/erosion/rainfall_erosion.jl` consumes `precipitation,interception,waterlevel,canopy_height,canopy_gap_fraction,soilcover_fraction` and implements `RainfallErosionEurosemModel` (direct/drip rainfall KE).
- `Wflow/src/sediment/erosion/overland_flow_erosion.jl` computes physical runoff-based soil-loss rate from `q, USLE C,K,slope,area,ANSWERS factor`.
- `Wflow/src/sediment/sediment_transport/overland_flow_transport.jl` uses `accucapacityflux_rate!` through directed network; `Wflow/src/sediment_model.jl` is **a hydrology-output post-processing model**, not live 2D SWE sediment flux. Official docs sediment expects **kinematic-wave land runoff**. Wflow.jl hydrology's 2D land local-inertial is a separate routing configuration and **cannot be called a proven native 2D sediment solver**.
- Official tests https://deltares.github.io/Wflow.jl/stable/getting_started/download_example_models.html supply original sediment TOML & NetCDF inputs. NO native Gounsa run or physical sediment timestep/mass stability QA done; **source passes process gate but fails transport dimensionality**.

### tRIBS-FEaST software/research mismatch
- Kim et al 2013 WRR DOI 10.1002/wrcr.20373 presents genuine 2D Roe SWE + Hairsine–Rose multiparticle, original/deposited soil layer, plus basin hydrology; Kim, Han, Cho 2014 DOI 10.9798/KOSHAM.2014.14.5.351 Korean paper claims experimental flume consistency. Published original completed **but not proven available as matching public code**.
- Official `tRIBS-Model/tRIBS` v6.0 C++ `src/tHydro/tIntercept.cpp` demonstrates Rutter canopy, `tHydroModel.cpp` LAI land variable. Search `Hairsine` returned **no source file**, `sediment` only mesh comment, no released erosion solver. Published tRIBS-OFM-FEaST ≠ current public native tRIBS executable. LAI→drip erosive energy not native proven. Do not reconstruct and claim published source.

### FeST and SSEM methodology
- FeST official docs https://www.fest.polimi.it/doc/module/sediment.html `Sediment.f90` includes `InterrillDetachmentRate`, `SedimentRouting`, `sedFlowDirection`, `sedReach`, `rusleC`, `rusleK`. Downstream routing Muskingum-Cunge channels; native hillslope not full 2D runoff flow detachment/Exner. FeST native canopy from https://www.fest.polimi.it/reference/canopy.html `Ct=Cmax LAI/LAImax`, throughfall/vegetation fraction.
- Song et al. 2024 DOI 10.7744/kjoas.510312 article full XML explicitly provides Eq.2 `∂h/∂t+∂q/∂x=r` and separate rain/flow detachment Eq.4–6, 250m DEM on Naerincheon >90% forest, against **rating-curve sediment** and each-event calibration. Does not meet real 2D or canopy dynamics despite real Korean mountains.

## Final decision
None of these 4 new lines satisfies **all** strict requirements at native released-source level. The scientific papers are valid in their context. No numerical engine resurrected or selected. Wflow is notable as the *most clearly source-audited original* canopy+drip+runoff erosion source; its inability to simulate conservative 2D lateral sediment is an explicit fatal gate for this project. Kim 2013/2014 is the strongest *published integrated 2D design* but same original executable source does not exist in official accessible repo, so original direct-use candidate discarded. Continue search only for new source lineages with demonstrable source + hydrology + genuine 2D sediment; do not revert to rejected methods without materially new evidence.

## Reference links
- https://github.com/Deltares/Wflow.jl
- https://deltares.github.io/Wflow.jl/quarto/model_docs/model_configurations.html
- https://gmd.copernicus.org/articles/17/3199/2024/gmd-17-3199-2024.html
- https://github.com/tRIBS-Model/tRIBS
- https://doi.org/10.1002/wrcr.20373
- https://doi.org/10.9798/KOSHAM.2014.14.5.351
- https://www.fest.polimi.it/doc/module/sediment.html
- https://www.fest.polimi.it/reference/canopy.html
- https://www.kjoas.org/articles/xml/P91L/
