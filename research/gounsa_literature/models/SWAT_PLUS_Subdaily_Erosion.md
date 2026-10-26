# SWAT+ subdaily splash + overland erosion original-source audit

## 소스 계보
USDA/Texas A&M joint public Fortran code https://github.com/swat-model/swatplus `src/ero_ovrsed.f90`. Developer-supported per-version docs https://docs.swat.tamu.edu/62.0.1/model-theory/erosion-sediment/ . **Original Fortran source actually read**, not a hypothetical paper implementation.

## Native physical subdaily process
Subdaily erosion with `gampt > 0` uses distinct original `sedspl` and `sedov`, NOT daily classic MUSLE. `ero_ovrsed.f90` lines 116–122 `canopy_cover = min(1., pcom(j)%lai_sum)`; lines 131–152 rain impact `ke_direct = 8.95+8.44log10(rain intensity)`, `ke_leaf=15.8sqrt(0.5*maximum_canopy_height)-5.87`; `rdepth_leaf=rdepth_tot*canopy_cover`, `rdepth_direct=rdepth_tot-rdepth_leaf`; splash `sedspl=erod_k*ke_total*exp(-eros_spl*surface_runoff_depth)`, and lines 165–182 `sedov` via `usle_k`, `rill_mult`, `c_factor`, and flow bed shear. The explicit routing is **HRU** and catchment channel/network, not spatially distributed full 2D Saint-Venant gridded erosion.

### Fatal vegetation nuance (for Gounsa)
`canopy_cover=min(1,LAI)`: LAI≥1 generates identical 100% covered fraction in raindrop impact, so just increasing oak/grass LAI from 1 to 4 **does not change the direct vs leafdrip partition from this particular original function**. Distinguish other dynamic SWAT+ hydrology canopy interception logic; here `rdepth_tot` is computed from gross precipitation `wst(iwst)%weat%ts(k)` and splits by scalar `canopy_cover`, **not** by measured per-stem canopy drainage balance. It is not the native Rutter differential canopy-store simulation delivered into drop energetics.

## Quantitative vegetation input
LAI endogenous plant model and canopy height (and aboveground biomass+residue cover for USLE cover). This is quantitatively present, but the specific rain impact pathway saturates at LAI 1, and HRU spatial averages cannot resolve local tussock versus dispersed oak canopy runoff concentration, rill emergence or LiDAR erosion map.

## Spatial structure / application
Forest, crop and other HRU basin scales; user Gounsa strict original native 2D erosion requirement **FAIL**. Official reference executable and source exist but no event native numerical/dt mass QA performed in this investigation; not labelled stable.

## Final verdict
**Reject as standalone Gounsa native 2D engine.** Scientific reference that not all SWAT+ erosion runs use MUSLE; subdaily method may be useful for rain versus flow process comparison, not excuse to promote SWAT+ or slip a non-2D model into Gounsa decision.

## Sources
https://github.com/swat-model/swatplus/blob/main/src/ero_ovrsed.f90
https://docs.swat.tamu.edu/62.0.1/model-theory/erosion-sediment/
https://docs.swat.tamu.edu/62.0.1/input-reference/codes-bsn/
