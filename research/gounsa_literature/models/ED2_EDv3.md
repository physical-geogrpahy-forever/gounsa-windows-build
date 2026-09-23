# ED2 / EDv3 model lineage

## 성격
- Ecosystem Demography cohort model
- cohort = PFT + size/height class
- patch = common disturbance history
- individual tree coordinates are not tracked

## hierarchy
```
grid
 -> polygon
 -> site
 -> patch
 -> cohort
```

Important: ED patches are spatial fractions, not georeferenced x-y patches.

## time structure
- surface/plant biophysics can run at minutes-scale timesteps
- subhourly meteorology supported
- carbon allocation, phenology, growth, recruitment and mortality use hierarchical slower schedules

This is highly compatible with event-scale ecohydrological response.

## vegetation
- woody PFT cohorts
- C3/C4 grass PFTs
- shrub PFT implementations exist in dryland extensions
- cohorts compete for light and belowground resources
- succession emerges from growth, mortality, recruitment and disturbance

## roots and soil
- root biomass/allocation
- soil-layer hydrology
- water stress
- soil biogeochemistry
- site metadata can include soil depth, slope, aspect, elevation and topographic moisture index

## understory
Small/short cohorts occupy shaded lower canopy environments. Grass and shrub PFTs can coexist with woody cohorts when parameterized.

## fire/disturbance
ED lineage contains disturbance and fire implementations. Post-disturbance patches and cohort recovery are intrinsic parts of the demographic framework.

## Gounsa strength
- cohort, not individual tree
- subhourly physiology/hydrology
- roots and soil state
- succession
- grass/shrub extensions
- soil depth/topographic inputs

## Gounsa spatial problem
Internal patches have no x-y coordinate.

Therefore the defensible spatial architecture would be external:
```
LiDAR/geomorph GIS tile
 -> one ED site/grid element
 -> internal ED cohorts/patch fractions
```

If used this way, each tile has real location but internal disturbance fractions remain non-georeferenced.

## storm coupling
Much stronger temporal basis than LANDIS-II NECN. Still must verify:
- restart at arbitrary storm endpoint
- dynamic replacement of soil depth
- remapping soil pools after erosion/deposition
- whether each geomorph tile can be restarted independently at acceptable cost

## current verdict
**Strong candidate if process fidelity is prioritized over implementation simplicity.**

Compared with BiomeE:
- stronger subhourly ecohydrology and mature disturbance framework
- heavier implementation
- similarly lacks native fine-scale x-y patch positions

Compared with FATES:
- standalone ED code lineage is less dependent on a full host land model
- understory grass/shrub parameterizations are less standardized than current FATES PFT machinery

## related papers
- `papers/2019_Longo_ED2_2_ModelDescription.md`
- `papers/2025_EckesShephard_DemographyModels.md`
