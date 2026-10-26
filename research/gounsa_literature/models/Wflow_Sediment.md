# Wflow.jl / wflow_sediment: actual open source LAI+leafdrip rain-and-runoff erosion, directed-network lateral transport

## Identity
- Deltares `Deltares/Wflow.jl` Julia MIT repository, includes `Wflow/src/vegetation/`, `Wflow/src/sediment/erosion/`, `Wflow/src/sediment/sediment_transport/`, unit tests `Wflow/test/`, official sediment_config TOML and NetCDF test cases.
- Underlying hydrology paper: van Verseveld et al. (2024), `Geoscientific Model Development, 17`, 3199–3234 DOI 10.5194/gmd-17-3199-2024. **This paper itself is hydrology validation, not native sediment validation**. No novel run in this investigation.

## Verified exact original source
1. `Wflow/src/vegetation/parameters.jl`: parameters `leaf_area_index` [m²/m²], `storage_specific_leaf`, `storage_wood`, `light_extinction_coefficient`, `canopy_gap_fraction`, `maximum_canopy_storage`. Cyclic LAI input recalculates Smax and gap. Documentation equations: `S_leaves_max=S_leaf*LAI`, `canopygapfraction=exp(-Kext*LAI)`.
2. `Wflow/src/vegetation/canopy.jl`: two native implementations `GashInterceptionModel`, `RutterInterceptionModel`. Stores canopy water, outputs `throughfall, interception, stemflow, canopy_storage`. `rainfall_interception.jl` does drainage/time integration (original Gash routine comment warns daily and stemflow factor TODO).
3. `Wflow/src/sediment/erosion/rainfall_erosion.jl::update_rainfall_erosion_model!`: `RainfallErosionEurosemModel` reads `precipitation`, `interception`, `waterlevel`, `canopy_height`, `canopy_gap_fraction`, `soilcover_fraction`, detachability/exponent and computes separate direct rainfall and leafdrip energy according to official model docs.
4. `Wflow/src/sediment/erosion/overland_flow_erosion.jl::update_overland_flow_erosion_model!`: `OverlandFlowErosionAnswersModel`, uses runoff q, USLE C and K, slope, area, ANSWERS factor for native flow erosion.
5. `Wflow/src/sediment/sediment_transport/overland_flow_transport.jl::update_sediment_overland_model!`: sediment `accucapacityflux_rate!(sediment_rate, deposition, erosion, network, transport_capacity)` over a **land-flow directed network**, not 2D conservative sediment advection and not physical rill incision.
6. `Wflow/src/sediment_model.jl` separate `SedimentModel` executable configuration post-processes saved hydrology outputs, does not jointly solve 2D SWE + 2D sediment and deforming bed in one native solver.
7. Official docs https://deltares.github.io/Wflow.jl/quarto/model_docs/model_configurations.html explicitly state sediment model uses precipitation, **kinematic-wave land runoff, river runoff, kinematic-wave water level, interception**. Water `wflow_sbm` can separately use `local_inertial` 2D land flow, **but sediment still not native full two-component 2D transport**. Do not call the entire combined model genuine 2D erosion.

## Applicability and uncertainty
Native LAI canopy interception, canopy storage and throughfall, physically explicit direct and leaf-drip rain detachment and hydrologic runoff-driven separate soil detachment are all actually present in contemporary full open source, unlike TREX or DHSVM public release. Official test data present, but version exact SHA and physical numerical regression at Gounsa hill grid not run. Native flow detachment still depends on USLE `C` factor and does not automatically take root biomass RLD from LAI. Overland soil mass finite erosion budget, dynamic bed elevation and native rill incision not independently verified. For small steep forest with TLS rills, native sediment routing is inadequate.

## Verdict
**Exclude as Gounsa strict original 2D erosion main engine**, retain fully implemented verified canopy-erosion source reference (particularly source terms, units, native process separation). If coupling to independent genuine 2D SWE is used, explicitly NEW coupling and requires stability, water/sediment mass and physics tests. No running output claimed.

## Links
https://github.com/Deltares/Wflow.jl
https://deltares.github.io/Wflow.jl/v0.5.2/model/sediment/
https://deltares.github.io/Wflow.jl/stable/getting_started/download_example_models.html
https://doi.org/10.5194/gmd-17-3199-2024
