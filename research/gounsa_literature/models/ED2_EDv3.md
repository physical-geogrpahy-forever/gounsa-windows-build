# ED2 / EDv3 model lineage

업데이트: 2026-09-23 source audit + ED2+R routing audit

## 성격
- Ecosystem Demography cohort model
- cohort = PFT + size/height class
- patch = common disturbance history
- individual tree coordinates are not tracked

## hierarchy
```text
grid
 -> polygon
 -> site
 -> patch
 -> cohort
```

Important: ED patches are spatial fractions, not georeferenced x-y patches.

## time structure
- surface/plant biophysics can run at minutes-scale/subhourly timesteps
- subhourly meteorology supported
- carbon allocation, phenology, growth, recruitment and mortality use hierarchical slower schedules

This is highly compatible with event-scale ecohydrological response.

## vegetation: corrected source-level assessment
Current official `EDmodel/ED2` source defines the default PFT set explicitly in `ED/src/memory/pft_coms.f90`.

Relevant current PFTs include:
- C4 grass
- temperate C3 grass
- northern pines
- southern pines
- late conifers
- early temperate deciduous
- mid temperate deciduous
- late temperate deciduous
- additional tropical/savanna/liana PFTs

However, the official current PFT table does **not** contain an explicit shrub PFT or an `is_shrub` life-form flag. A repository-level search for `is_shrub`, `shrub_pft`, or equivalent native shrub-PFT machinery returned no direct implementation.

This corrects the previous broad statement that ED2 should be treated as having standardized grass + shrub + tree understory demography. Dryland or external research extensions may introduce shrub-like parameterizations, but they are not part of the current canonical PFT machinery and must not be counted as a ready native feature without a specific implementation.

Therefore criterion 2 for Gounsa is now:
- grass demography: YES
- tree cohort succession: YES
- explicit shrub demographic layer: **NO in current canonical source / requires extension or surrogate PFT**

This is a major disadvantage for a postfire `herb -> shrub -> tree` trajectory.

## roots and soil
- root biomass/allocation
- soil-layer hydrology
- water stress
- soil biogeochemistry
- variable soil-depth initialization exists (`ISOILDEPTHFLG` can read a soil-depth database)
- site state includes elevation, slope, aspect and topographic moisture index
- water-table/baseflow logic exists in `lsm_hyd.f90`

Current source retains explicit TOPMODEL-related hydrology. `lsm_hyd.f90` computes topographic water depth from site/polygon moisture-index terms, and templates/history readers retain multiple-site TOPMODEL initialization pathways.

Thus criterion 3 is stronger than an ordinary stand-only forest model even though storm-driven erosion/deposition remapping of soil geometry is not native.

## topography and hydrology
Current source evidence:
- geographic polygon/site hierarchy
- elevation, slope and aspect per site
- topographic moisture index
- TOPMODEL water-depth calculations
- free-drainage/aquifer lower soil boundary options
- variable soil depth at initialization

Therefore ED2 has meaningful terrain-hydrology structure, not only site metadata.

However, this should not be overstated as the same thing as a modern 2-D/3-D explicit hillslope groundwater solver such as ParFlow. The TOPMODEL representation remains an aggregated topographic redistribution approach.

## ED2+R catchment routing precedent
Pereira et al. (2017) integrated ED2 with a routing scheme and evaluated the resulting **ED2+R** in the Tapajós River basin, Brazilian Amazon.

Published capability:
```text
ED2 surface runoff
 + ED2 subsurface runoff
 -> lateral propagation through routing network
 -> river flow
```

This is direct evidence that ED2 output has been connected across a real catchment and routed laterally at basin scale.

Important limitation for Gounsa:
- ED2+R routes runoff produced by the terrestrial biosphere model.
- It should **not** be interpreted as evidence that neighboring-cell lateral groundwater/soil-water redistribution is fed back into each cohort root zone in the same manner as ParFlow-FATES.
- Therefore it strengthens criterion 4 but does not remove the hydrologic-coupling advantage of FATES+ParFlow or medfateland.

Reference:
Pereira, F. F., Farinosi, F., Arias, M. E., Lee, E., Briscoe, J., & Moorcroft, P. R. (2017). Technical note: A hydrological routing scheme for the Ecosystem Demography model (ED2+R) tested in the Tapajós River basin in the Brazilian Amazon. Hydrology and Earth System Sciences, 21, 4629–4648. https://doi.org/10.5194/hess-21-4629-2017

## understory
Small/short tree cohorts and grass PFTs can occupy lower-light environments and coexist with taller woody cohorts.

But for Gounsa the missing native shrub demographic PFT is decisive. The model does not currently offer the same ready tree + shrub + grass life-form set as FATES or LPJ-GUESS.

## fire/disturbance
ED lineage contains disturbance/fire implementations. Post-disturbance patches and cohort recovery are intrinsic parts of the demographic framework.

## Gounsa strengths
- true cohort demography rather than individual-tree tracking
- subhourly physiology/hydrology
- grass + temperate tree PFTs
- roots and layered soil state
- variable soil-depth initialization
- topographic moisture/TOPMODEL structure
- published catchment runoff-routing coupling in ED2+R
- succession and disturbance

## Gounsa weaknesses
1. internal patches have no x-y coordinate
2. **no canonical shrub PFT/demographic layer in current source**
3. terrain hydrology is TOPMODEL-style rather than explicit fine 3-D hillslope flow
4. ED2+R routes generated runoff but does not prove ParFlow-class lateral root-zone soil-water feedback
5. dynamic erosion/deposition soil-layer remapping remains new coupling
6. Korea-specific parameterization would be substantial

## spatial architecture if retained as comparator
```text
LiDAR/geomorph GIS tile
 -> one ED site/grid element
 -> internal ED cohorts/patch fractions
```

Each tile can have a real map location, but internal disturbance-history patches remain non-georeferenced.

## storm coupling
Temporal basis is much stronger than LANDIS-II NECN. Still must verify/implement:
- restart at arbitrary storm endpoint
- dynamic replacement/remapping of soil depth
- conservative remapping of soil water/C/N/root pools after erosion/deposition
- external geomorphic state exchange at acceptable cost

## five-criteria verdict after source + routing audit
| criterion | verdict |
|---|---|
| 1 spatial cohort | PARTIAL-STRONG: geographic site + demographic cohorts, but internal patches implicit |
| 2 understory succession | **PARTIAL: grass + tree strong, shrub missing natively** |
| 3 soil/geomorph coupling readiness | STRONG-PARTIAL: variable soil depth, layered water, TOPMODEL, restartable state; geomorphic remapping custom |
| 4 catchment/topography | **STRONG:** terrain/TOPMODEL plus published ED2+R basin routing, but not explicit ParFlow-class lateral soil-water feedback |
| 5 <= daily | STRONG: subhourly biophysics, slower demographic schedules |

## current verdict
**Strong comparator, but below FATES under the strict understory criterion.**

ED2 remains scientifically relevant because it combines cohort demography, grass, roots, subhourly ecohydrology, topographic hydrology, and now a documented catchment-routing coupling in one mature lineage. However, the absence of a canonical shrub demographic PFT remains a decisive mismatch for the intended postfire herb -> shrub -> tree trajectory.

Compared with FATES:
- potentially less host-stack complexity
- similarly implicit internal patch spatiality
- weaker ready understory life-form coverage because shrub is absent in canonical PFT set
- ED2+R catchment routing exists, but FATES+ParFlow offers more explicit lateral subsurface hydrology feedback

Compared with LPJ-GUESS:
- stronger native subhourly biophysics and TOPMODEL/routing heritage
- weaker modern shrub/herb/tree succession coverage

## related papers
- `papers/2019_Longo_ED2_2_ModelDescription.md`
- `papers/2025_EckesShephard_DemographyModels.md`

## source audit
- `EDmodel/ED2`, current default branch, 2026-09-23
- `ED/src/memory/pft_coms.f90`
- `ED/src/dynamics/lsm_hyd.f90`
- `EDTS/Templates/ED2IN-*`
