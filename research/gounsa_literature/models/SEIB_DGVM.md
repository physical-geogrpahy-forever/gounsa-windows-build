# SEIB-DGVM model lineage

## 목적
LiDAR 기반 세밀 지형과 결합 가능한 spatially explicit individual-based vegetation model 후보로 검토한다.

## 기본 계보

### Sato et al. 2007
- 기본 virtual forest: 30 m x 30 m
- 1 m establishment mesh
- individual woody PFTs + grasses
- individual tree positions, crown competition, gap dynamics
- fine roots represented by biomass

### Sato & Ise 2012
- Africa 0.5° geographic cells
- each geographic cell represented by 30 m x 30 m virtual forest
- fire, root biomass, litter/fuel pools
- coarse inter-grid dispersal precedent:
  - 90% of establishment opportunities from local woody biomass
  - 10% from environmentally eligible PFTs occurring in adjacent geographic cells
- this is not a mechanistic distance-resolved seed kernel

### Sato et al. 2023
- Hokkaido cold-temperate conifer-broadleaf mixed forest
- East Asian cold-temperate PFTs
- elevation / terrestrial-wetness gradient
- drought and excessive-soil-moisture tolerance
- catastrophic-disturbance succession

### Sato & Sumida 2025
- 100 m x 100 m virtual forest
- cold-temperate conifer/broadleaf crown allometry and competition

### SEIB-DGVM-NSC / SEIB-NOAH lineages
- root NSC and root turnover available in the NSC lineage
- NOAH-LSM provides subdaily soil heat/water physics in the current main line

## 최신 공개 코드 상태
2026-09-22 official page check:
- latest public major version: 3.30
- model description modified 2026-08-16
- Apache License 2.0
- Fortran90
- gfortran/MinGW-w64 execution confirmed by official page
- base distribution is a one-virtual-forest point simulation
- virtual-forest area is configurable
- `code>mpi` provides multi-grid parallel execution

## v3.30 spatial structure

### Virtual forest
- square stand
- side length = `Max_loc`
- standard v3.30 parameter file: `Max_loc = 100 m`

### Internal horizontal grids
- woody establishment: `Dived x Dived`
- grass: `DivedG x DivedG`
- v3.30 standard: `Dived = DivedG = 50`

Therefore the standard 100 m stand has a 2 m establishment-cell edge.

The probability applied to one establishment mesh cell is:
```
P_establish(p) * (Max_loc / Dived)^2
```

Important:
changing `Max_loc` changes the internal spacing if `Dived` is unchanged, but that does not mean every finer spacing has ecological validation.

## v3.30 temporal structure
- NOAH-LSM land-surface physics: 30 min
- most physiology: daily
- biomass growth: daily
- litter decomposition: daily
- fire: daily
- direct-radiation spatial redistribution: every 14 days
- mortality: annual
- self-pruning: annual
- crown movement: annual
- establishment: annual

This temporal architecture is substantially easier to interface with storm/event geomorphology than a succession model whose biological state changes only every several years.

## Plant state

### Woody individuals
- `mass_leaf`
- leaf area
- crown diameter
- crown depth
- `mass_trunk`
- height
- sapwood and heartwood diameter
- fine-root biomass `mass_root`
- stock and available resource pools

### Roots
Fine roots have no explicit spatial geometry in v3.30. They are represented by individual-tree biomass.

Also:
```
mass_trunk = stem + branches + coarse-root biomass
```

Therefore coarse roots are not an independent state.

This distinction is critical:
```
fine individual-tree canopy geometry
!=
fine individual-tree root geometry
```

## Litter and dead biomass
Living biomass enters litter pools via:
- turnover
- seasonal leaf shedding
- self-pruning
- carbon starvation
- mortality

v3.30 records aboveground and belowground litter inputs separately.

Daily decomposition includes:
- woody debris
- leaf litter
- fine-root litter
- grass litter

Fire can consume living vegetation and litter according to the selected fire module.

This is a major advantage over fine-spatial forest models that lack mature litter/deadwood turnover.

## Water and soil
The standard v3.30 configuration activates NOAH-LSM.

- land physics at 30 min
- updated soil temperature and soil-water states are returned to daily SEIB biology
- original SEIB profile: 20 layers x 0.1 m
- outputs include layer soil water, surface runoff, subsurface runoff, transpiration, evaporation, snow and related variables

### Critical within-stand limitation
The internal vegetation grid is not a matching fine hydrological grid.

Official v3.30 documentation states:
- all grass cells share the same stand-level soil-water pools
- temperature, atmospheric CO2 and physiological soil-water status are spatially uniform within a stand on a given day
- PAR varies spatially among crown disks and grass cells

Therefore:
```
2 m establishment mesh != 2 m soil-water grid
```

LiDAR-scale soil-water heterogeneity cannot simply be supplied to individual 2 m cells inside one large virtual forest.

## Topographic coupling precedent
Cold-temperate SEIB work and the TOPMODEL lineage provide a precedent for:
```
topographic wetness / CTI
 -> plot or grid soil-water environment
 -> PFT photosynthesis, establishment and mortality
 -> biomass and species composition
```

The code-history for cold-temperate PFTs includes `CTI_dif` so that site CTI can differ from a grid-average CTI.

This is useful, but it is not a genuine within-stand 2D lateral hydrology solver.

## MPI multi-plot architecture
The official MPI package:
- computes multiple grid cells in parallel
- substitutes `start_mpi.f90` and `main.f90` for point-simulation drivers
- shares the main physiology/spatial/population code
- distributed sample uses coarse 0.5° Siberian grids

Thus multi-plot execution exists. However:
```
MPI multi-plot computation != automatic inter-plot ecological interaction
```

Fine-scale annual seed exchange among Gounsa plots would still require an explicit coupling layer.

## LiDAR relevance
Strong points:
- individual x-y tree positions
- individual crown dimensions
- meter-scale establishment mesh
- configurable stand size
- cold-temperate East Asian PFT lineage
- individual fine-root biomass
- above/belowground litter
- fire/postfire succession
- 30-min land physics
- daily biology/decomposition/fire
- current output includes individual-tree properties

LiDAR can potentially constrain or validate:
- tree positions
- height
- crown dimensions
- density
- canopy gaps
- canopy-height surface

Direct LiDAR-to-SEIB state assimilation is not treated here as an existing published automatic routine. A preprocessing/restart interface would be a new implementation.

## Recommended Gounsa scale architecture
Do not force vegetation and geomorphology to have identical horizontal discretization.

A defensible architecture to test is:
```
LiDAR DEM / geomorph grid
1-5 m
    |
    | aggregate terrain / soil state
    v
SEIB virtual-forest tiles
initially test ~10-50 m and 20-50 m ranges
    |
    | individual x,y + crown + mass_root + litter
    v
spatial disaggregation / rasterization
back to 1-5 m geomorph grid
```

The vegetation tile size must be chosen by sensitivity tests involving:
- crown radius relative to tile size
- tree density
- periodic boundaries
- stand-level soil-water homogenization
- computational cost
- topographic variability

Making every LiDAR cell an independent SEIB stand would destroy local tree competition and is not recommended.

## Root and litter geomorph interfaces
Because SEIB does not contain explicit root geometry:
```
individual mass_root
 -> species/PFT-specific vertical root distribution
 -> horizontal root-spread helper
 -> RLD / RSAD / root mass per geomorph cell
```
must be a documented new coupling.

Likewise:
```
litter mass
 -> physical surface litter/contact/storage state
```
requires a separate defensible interface.

## Comparison with other current candidates

### iLand
- excellent individual trees and root/litter outputs
- 2 m light grid
- but core production/water/soil processes operate largely at 1 ha / 100 m resource-unit scale
- LiDAR does not remove that belowground scale mismatch

### TROLL 4.0
- 1 m aboveground voxels
- explicit fine-root depth distribution and root-length-related water uptake
- spatial 1 m seedling bank
- excellent remote-sensing compatibility
- but current model is tropical, assumes flat within-stand topography, lacks mature litter decomposition/wood decay and fire modules

### LPJ-GM
- strongest explicit landscape migration extension of LPJ-GUESS
- but published local vegetation dynamics remain kilometer-scale
- under a LiDAR fine-scale objective this becomes a much larger disadvantage

### LANDIS-II
- strong landscape connectivity and root/litter pools in some succession extensions
- but cohort/raster abstraction and succession timestep remain less aligned with fine event-driven geomorph feedback

## Remaining SEIB problems
1. explicit horizontal and vertical root architecture
2. stand-level soil-water homogenization
3. explicit fine-scale inter-plot seed dispersal
4. geomorphic soil-depth changes mapped to SEIB/NOAH soil layers
5. Korea-specific PFT/species calibration
6. LiDAR initialization workflow
7. optimum tile size and periodic-boundary sensitivity
8. fire module choice and calibration for Korean temperate forest

## Current verdict
**Provisional first-choice vegetation engine for technical testing under the LiDAR criterion.**

It is not a complete 1-5 m ecohydrological model. Its advantage is the current combination of:
- fine individual-tree aboveground structure
- East Asian cold-temperate applicability
- root biomass
- litter/dead biomass
- fire
- daily biological processes
- subdaily land physics
- configurable open source code

## Related papers
- `papers/2007_Sato_SEIB_DGVM.md`
- `papers/2012_Sato_Ise_SEIB_Africa_Dispersal.md`
- `papers/2020_Sato_SEIB_TOPMODEL.md`
- `papers/2023_Sato_SEIB_Hokkaido_MixedForest.md`
- `papers/2023_Ninomiya_SEIB_DGVM_NSC.md`
- `papers/2025_Sato_Sumida_SEIB_Crown.md`
- `papers/2025_Sato_Sumida_SEIB_Crown_MixedForest.md`
