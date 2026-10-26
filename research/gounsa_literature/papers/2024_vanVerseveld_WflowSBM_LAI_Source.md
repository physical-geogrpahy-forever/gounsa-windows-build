# van Verseveld et al. (2024) Wflow_sbm LAI canopy source

## 서지정보
van Verseveld, W. J., Weerts, A. H., Visser, M., Buitink, J., Imhoff, R. O., Boisgontier, H., Bouaziz, L., Eilander, D., Hegnauer, M., ten Velden, C., & Russell, B. (2024). Wflow_sbm v0.7.3, a spatially distributed hydrological model: From global data to local applications. *Geoscientific Model Development, 17*, 3199–3234. https://doi.org/10.5194/gmd-17-3199-2024

## 연구 이유
Canopy interception with quantitative variable LAI, native throughfall, 2D surface runoff, and sediment full source in currently available Wflow.jl.

## Methods, spatial structure, vegetation
Actual published hydrological distributed SBM; variable LAI [m²/m²] controls leaf water storage `S_leaf_max(t)=S_leaf LAI(t)` [mm], woody canopy capacity added, canopy gap `f_gap(t)=exp(-k LAI(t))`, Rutter/Gash interception and throughfall model, vertical soil processes and surface flow routing. Model applied catchments of varying environments globally. This **paper evaluates hydrology**, not Wflow.jl sediment dt convergence or Korean burned forest soil loss.

## 2026 source confirmation
Deltares/Wflow.jl MIT Julia actual `Wflow/src/vegetation/parameters.jl` `leaf_area_index`, `storage_wood`, `storage_specific_leaf`, `light_extinction_coefficient`; `vegetation/canopy.jl` Gash/Rutter time-varying `throughfall, interception, stemflow, canopy_storage`; `sediment/erosion/rainfall_erosion.jl` physically computes EUROSEM rainfall erosion from `precipitation, interception, waterlevel, canopy_height, canopy_gap_fraction, soilcover_fraction` and `overland_flow_erosion.jl` ANSWERS detachment from water flux and USLE parameters.
Important **distinct modules**: `Model(type=SedimentModel)` is post-processing on hydrology output, not a fully simultaneous two-dimensional fluid-sediment-finite-volume model.

## Critical process exclusion
`Wflow/src/sediment/sediment_transport/overland_flow_transport.jl` native `accucapacityflux_rate!(...,network,...)` performs directed-network accumulating transport. Wflow_sediment official doc identifies **land runoff/level from kinematic wave**. Even though modern Wflow_sbm can separately run **2D local inertial land flow**, there is NO source proof that `wflow_sediment` tracks genuinely two-component 2D sediment advection coupled to that flow in its released model. Thus fails strict 2D sediment requirement. No emergent micro-rill incision or Exner original hillslope dynamic in reviewed paths.

## Application
Strongest identified officially maintained fully open canopy+rain+flow erosion original **process implementations**, with real example NetCDFs and native run configurations (official Wflow.jl examples). Yet not suitable for fine Gounsa rill/DEM high-resolution original integrated main model without explicitly new coupling. Unit test/native full run and observed sediment validation not performed in this review.

## 고운사 coupling
2D hydrodynamic and dynamic sediment coupling to different engine must be new code, and USLE C-based flow detachment is not dynamic RLD-based erosion resistance. Need ensure sediment source is not double-counted. No unsourced claim already native.

## Decision
**Exclude strict Gounsa standalone 2D erosion engine.** Keep native LAI and leaf-drip erosion formula and sediment routine reference as *verified software source*; do not promote to final main model.

## Sources
https://gmd.copernicus.org/articles/17/3199/2024/gmd-17-3199-2024.html
https://github.com/Deltares/Wflow.jl
https://deltares.github.io/Wflow.jl/quarto/model_docs/model_configurations.html
https://deltares.github.io/Wflow.jl/quarto/model_docs/vertical/shared_processes.html
https://deltares.github.io/Wflow.jl/v0.5.2/model/sediment/
