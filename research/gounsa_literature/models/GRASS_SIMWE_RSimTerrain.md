# GRASS GIS SIMWE and r.sim.terrain 1.0 original public source

## Research source
Harmon, Mitasova, Petrasova, & Petras (2019), GMD 12:2837–2854 DOI 10.5194/gmd-12-2837-2019. Open GRASS addon `baharmon/landscape_evolution` GPL2 source, complete example LiDAR and raster datasets.

## Genuine spatial hydrodynamic process
`r.sim.water` is two-dimensional path-sampling (SIMWE), `r.sim.sediment` computes two-dimensional erosion/deposition from spatially varying water depths, detachment/transport capacity and sediment source. `r.sim.terrain` iterates events, changes elevation and can generate rill/gully forms. The actual stochastic Green-function Monte-Carlo solver is **not 2D classical finite-volume SWE**, no false equivalence.

## Native input actual GRASS commands
`elevation`, `rain_intensity` and `precipitation`, `runoff`, `mannings`, `detachment`, `transport`, `shearstress`, `density`, `c_factor`, `k_factor`, `walkers`; user can use land-cover spatial maps. Example 50mm/h rain, 120min at 1m grid supported. LAI, plant canopy water store and drip KE **not native demonstrated in script/model arguments**.

## Validation
Patterson Branch (Fort Bragg, North Carolina), 450m², LiDAR time-series benchmark, 2019 field case. Publication claims emergent fine morphology and terrain feedback, not proof native dynamic canopy or finite soil stock.

## Assessment
**Excluded from all-in-one native Gounsa LAI canopy + 2D rainfall/runoff erosion requirement.** Very strong **secondary independent spatial DEM/rill morphodynamic benchmark**. No running code, no mass/dt numerical convergence proof. A new dynamic canopy coupling would be an original research implementation and cannot be presented as a bundled feature.

## Sources
https://github.com/baharmon/landscape_evolution
https://grass.osgeo.org/grass-stable/manuals/r.sim.sediment.html
https://grass.osgeo.org/grass-stable/manuals/addons/r.sim.terrain.html
https://gmd.copernicus.org/articles/12/2837/2019/gmd-12-2837-2019.html

## 2026-10-27 새 고해상도 식생지-나지 실제 산사태 사면 검증 사례
- **[Adiprana & Samodra (2026)](../papers/2026_Adiprana_Samodra_SIMWE_Lidar_Vegetated_Landslide_Erosion.md)** DOI10.1002/esp.70329, Wiley ESPL 51(7) e70329, 2026-06-25 출판. Indonesia Kalisari steep active landslide zone, vegetation/bare patch, actual UAV LiDAR DTM plus field infiltration + video-depth, explicit erosion/deposition maps in published original SIMWE experiment. Two rainfall scenarios 84mm/h 30min, 38.2mm/h 65min. Soil infiltration vegetated72 vs bare30mm/h; swap test shows hydraulic/infiltration-driven erosion response. Observed/estimated overland water depth under 84mm/h ~1cm vegetated/~4cm bare. **Distinct from LAI canopy interception**; site roughness/infiltration contrast is not canopy water budget.
- Wiley publisher [data availability](https://onlinelibrary.wiley.com/doi/10.1002/esp.70329) says rainfall, DTM, GRASS scripts, infiltration measurements and erosion pins **author request** only; paper computational raster Δx unspecified in accessible abstract. No proof 5/10cm or exact executable settings preserved.
- GRASS SIMWE Green-function Monte-Carlo approach computes 2D spatial hydrology and erosion/deposition under quasi-steady approximations, **not full transient 2D momentum SWE**. 2026 article itself cautions absolute erosion rates affected by steady-state assumptions and parameter uncertainty. Thus new good vegetation+steep slope *spatial sediment map* academic precedent but **full original high-res LAI canopy and drop impact main model remains NO-GO**.
