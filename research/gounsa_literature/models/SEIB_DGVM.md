# SEIB-DGVM model lineage

## 목적
LiDAR 기반 세밀 지형과 결합 가능한 spatially explicit individual-based vegetation model 후보로 검토한다.

## 기본 구조
Sato et al. 2007.
- 기본 virtual forest: 30 m x 30 m
- forest-floor establishment mesh: 1 m x 1 m
- individual woody PFTs + grasses
- individual tree positions, crown competition, gap dynamics
- physical/physiological processes: daily
- trunk growth: monthly
- establishment, mortality, disturbance including wildfire: annual

SEIB-DGVM-NSC:
- leaf, trunk, root NSC pools
- root NSC and root turnover included
- daily root turnover

SEIB-NOAH:
- soil heat/water calculation can operate at subdaily step
- published coupling exchanges soil moisture/temperature and vegetation variables daily

## 최신 공개 코드 상태
2026-09-22 확인:
- official download page updated 12 Sep 2026
- latest public version: 3.30
- Apache License 2.0
- Fortran90
- gfortran/MinGW-w64 실행 확인
- default distribution is one virtual forest point simulation
- forest area can be modified in configuration
- multi-plot/regional code and information are provided in code>mpi

Version 3.30 was released 9 Aug 2026 and its distribution was subsequently replaced after restart/reproducibility fixes in August 2026. Use the current package, not an early August copy.

## spatial scale nuance
SEIB is spatially explicit primarily for aboveground individual trees and recruitment space.

Important limitations:
- fine roots are represented as a biomass organ but are described as formless in the cold-temperate implementation
- standard SEIB does not provide explicit horizontal root architecture around each tree
- the main model does not mechanistically simulate long-distance seed dispersal
- large-scale applications often treat one virtual forest as representative of a larger grid

Therefore:
```
1 m tree/recruitment mesh != 1 m fully distributed soil/root model
```

## LiDAR relevance
Strengths:
- individual x-y tree positions
- individual crown dimensions
- 1 m establishment mesh
- plot area is configurable
- 2025 cold-temperate work used a 100 m x 100 m virtual forest
- outputs of individual tree properties are supported in current 3.21+ viewer format
- direct comparison with LiDAR-derived tree/canopy structure is conceptually straightforward

LiDAR can be used to initialize or constrain:
- tree positions
- height
- crown dimensions
- density/gap structure
- canopy height surface

However direct LiDAR-to-SEIB initialization is not treated here as an existing published automatic assimilation routine. Such initialization would need a documented preprocessing interface.

## cold-temperate applicability
Sato et al. 2023 and Sato & Sumida 2025:
- mixed conifer-broadleaf forest
- revised allometry/allocation for cold-temperate woody PFTs
- 2025 study used 100 m x 100 m virtual forest
This is substantially closer to Gounsa than tropical-only individual-tree models.

## root and litter
Represented:
- woody fine-root biomass
- grass fine-root biomass
- fine-root turnover
- litter carbon pool
- standing dead tree-leaf mass
- standing dead grass mass
- lying dead mass in the fire lineage
- soil organic carbon pools

Important limitation:
- soil carbon vertical distribution is not represented in the cited SEIB soil-C formulation
- horizontal fine-root geometry is not explicitly represented

Geomorph interface therefore should be:
```
individual/tree or PFT root biomass
 -> species/PFT-specific vertical and horizontal root architecture helper
 -> LiDAR/DEM geomorph raster
```
not direct use of a SEIB 1 m root map.

## wildfire and succession
Published SEIB studies explicitly induce fire and follow postfire succession.
The fire lineage uses fuel load, fuel moisture and wind and tracks litter fuel pools.
Vegetation dynamics and disturbance are assessed annually while physiological processes are daily.

## topographic coupling precedent
Sato et al. 2020 coupled SEIB-DGVM + NOAH-LSM with a TOPMODEL-type representation of within-grid topographic heterogeneity.
The model represented:
- elevation heterogeneity
- topographic index / CTI
- soil-water redistribution
- drought and over-wet stress
- vegetation feedback

This is important for Gounsa because it demonstrates an existing published:
```
topography
 -> soil moisture redistribution
 -> tree abundance / mortality
```
coupling in the SEIB lineage.

But this is not a LiDAR-scale lateral hydrology solver. It is a topographic-index parameterization.

## comparison with iLand under LiDAR criterion
iLand has:
- individual trees
- 2 m light grid
- 2 m regeneration grid
- 20 m seed grid

but:
- core water balance, production and many soil processes use 100 m x 100 m (1 ha) resource units.

Thus for a 1-5 m LiDAR geomorph grid, iLand has a stronger scale mismatch in belowground/eco-hydrological feedback than SEIB.

## comparison with TROLL 4.0
TROLL 4.0:
- trees explicit at 1 m
- fine-root biomass and vertical root distribution
- belowground voxels
- LiDAR validation is excellent

but:
- current model is primarily tropical
- total fine-root biomass is assumed equal to leaf biomass
- roots do not spread horizontally between belowground voxels
- litter decomposition and wood decay are explicitly future developments
- no mature wildfire module in TROLL 4.0 description

Therefore TROLL is an important structural/LiDAR benchmark, but not currently a better whole-process Gounsa vegetation engine.

## remaining SEIB problems
1. explicit horizontal root spread
2. direct litter surface distribution at LiDAR/DEM resolution
3. explicit inter-plot seed dispersal if multiple virtual forests are tiled
4. mapping geomorphic soil-depth change into SEIB/NOAH soil layers
5. determining whether one large virtual forest or multiple coupled subplots is computationally preferable
6. Korea-specific PFT/species calibration
7. LiDAR-based initialization workflow

## current verdict
Provisional first-choice vegetation engine for further technical testing under the LiDAR criterion.

Not because every process is already spatially explicit at 1 m, but because it currently provides the best combination of:
- fine aboveground spatial structure
- cold-temperate applicability
- root biomass
- litter
- fire/postfire succession
- daily physiology
- subdaily soil physics
- topographic-hydrology coupling precedent
- open modifiable code

## related papers
- papers/2007_Sato_SEIB_DGVM.md
- papers/2020_Sato_SEIB_TOPMODEL.md
- papers/2023_Ninomiya_SEIB_DGVM_NSC.md
- papers/2025_Sato_Sumida_SEIB_Crown.md
