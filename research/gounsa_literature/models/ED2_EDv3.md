# ED2 / EDv3 model lineage

업데이트: 2026-09-23 source audit

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
- succession and disturbance

## Gounsa weaknesses
1. internal patches have no x-y coordinate
2. **no canonical shrub PFT/demographic layer in current source**
3. terrain hydrology is TOPMODEL-style rather than explicit fine 3-D hillslope flow
4. dynamic erosion/deposition soil-layer remapping remains new coupling
5. Korea-specific parameterization would be substantial

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

## five-criteria verdict after source audit
| criterion | verdict |
|---|---|
| 1 spatial cohort | PARTIAL-STRONG: geographic site + demographic cohorts, but internal patches implicit |
| 2 understory succession | **PARTIAL: grass + tree strong, shrub missing natively** |
| 3 soil/geomorph coupling readiness | STRONG-PARTIAL: variable soil depth, layered water, TOPMODEL, restartable state; geomorphic remapping custom |
| 4 catchment/topography | STRONG-PARTIAL: terrain/TOPMODEL precedent, not explicit ParFlow-class hillslope flow |
| 5 <= daily | STRONG: subhourly biophysics, slower demographic schedules |

## current verdict
**Downgraded from top-tier to strong comparator.**

ED2 remains scientifically relevant because it combines cohort demography, grass, roots, subhourly ecohydrology and topographic hydrology in one mature code base. However, under the user's strict criterion 2, the absence of a canonical shrub demographic PFT makes it a poorer direct match than FATES and the LPJ-GUESS lineage for Gounsa postfire succession.

Compared with FATES:
- potentially less host-stack complexity
- similarly implicit internal patch spatiality
- weaker ready understory life-form coverage because shrub is absent in canonical PFT set

Compared with LPJ-GUESS:
- stronger native subhourly biophysics and TOPMODEL heritage
- weaker modern shrub/herb/tree succession coverage and weaker recent fine-catchment/external-hydrology coupling precedent

## related papers
- `papers/2019_Longo_ED2_2_ModelDescription.md`
- `papers/2025_EckesShephard_DemographyModels.md`

## source audit
- `EDmodel/ED2`, current default branch, 2026-09-23
- `ED/src/memory/pft_coms.f90`
- `ED/src/dynamics/lsm_hyd.f90`
- `EDTS/Templates/ED2IN-*`
