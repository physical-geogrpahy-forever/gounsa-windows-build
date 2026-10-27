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


## 2026-10-27 신규 역사적 원본 버그 감사: Wflow.jl v1.0.3 EUROSEM splash units
Previously audited source chain remains: LAI canopy interception, leafdrip KE, overland flow erosion, directed-network sediment transport. **Strict 2D XY sediment solver still absent**, so not adopted Gounsa 5cm original.

**Crucial newly source-verified version dependency:**
- Upstream `Deltares/Wflow.jl` merged PR [#939](https://github.com/Deltares/Wflow.jl/pull/939) on **2026-06-15**, commit `b9de064dda8027dfd5567af1b5ccef8c35d0c869`, released in **v1.0.3 (2026-06-23, tag SHA `44f15035073cb011ae26a57620882de9a16dd041`)** and subsequent 1.0.4.
- `Wflow/src/sediment/erosion/erosion_process.jl::rainfall_erosion_eurosem`: **erroneous pre-fix** total kinetic energy calculation `ketot=(rddir*kedir+rdleaf*keleaf)*0.001` was corrected to `ketot=(rddir*kedir+rdleaf*keleaf)`. Given rain depth [mm], KE density [J m^-2 mm^-1], latter has the correct total [J m^-2]. This correction by itself multiplies kinetic-energy-dependent component by a factor **1000** for unchanged input.
- `Wflow/src/sediment/erosion/rainfall_erosion.jl` (at 2026 commit L151) now `waterlevel_mm = waterlevel[i]*1000.0` before EUROSEM rainfall erosion. Original waterlevel land [m] was passed to a shielding equation `exp(-eurosem_exponent*h)` expecting **h [mm]** and `eurosem_exponent [mm^-1]`; with original meters, water shielding was greatly underrepresented. Depending on positive depths, this correction reduces rain-splash detachment while the energy fix increases it. **Overall magnitude/sign at each cell is scenario-dependent**, not always exactly factor 1000.
- Upstream **modified the actual native sediment regression outputs** in `Wflow/test/run_sediment.jl`. Test first-cell rainfall erosion **0.01232301374083337 → 12.323013740833371** (exact ×1000 in that test); average rainfall erosion 0.0014726364432116048 → 1.433891239693397, and total soil erosion 0.010083427210107495 → 1.4425020304602927. These are **upstream internal test expectations** from the version change, **NOT a new Gounsa simulation, measured accuracy, or generic predicted real-world ratio**.
- The same code audit also shows `Deltares/Wflow.jl` as released complete Julia source. Do not suggest pre-1.0.3 version for any EUROSEM canopy sensitivity quantitative use without acknowledging these prior unit errors.
- Changelog confirms on [2026-06-23](https://github.com/Deltares/Wflow.jl/releases/tag/v1.0.3); on v1.0.4 release 2026-07-24 further unrelated fixes. There is no demonstrated published full 2D XY sediment advection + 5cm canopy storm benchmark despite patch.

**Original evidence:** [PR #939 diff](https://github.com/Deltares/Wflow.jl/commit/b9de064dda8027dfd5567af1b5ccef8c35d0c869), [Wflow official change log](https://github.com/Deltares/Wflow.jl/blob/main/docs/changelog.qmd), [model erosion source](https://github.com/Deltares/Wflow.jl/tree/main/Wflow/src/sediment/erosion).
