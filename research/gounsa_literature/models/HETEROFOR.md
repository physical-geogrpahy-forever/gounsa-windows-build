# HETEROFOR model lineage

## 현재 검토 목적
LiDAR 기반 1-5 m급 지형모델과 결합할 주 식생엔진 후보로 HETEROFOR를 평가한다.

## 모델 성격
- spatially explicit
- individual-tree process-based forest model
- Capsis platform
- stand scale roughly 0.5-5 ha
- decadal to century forest dynamics
- current public installer exists through January 2026
- HETEROFOR source/modules use LGPL in published documentation

## spatial representation

### Adult trees
Each tree can be initialized with:
- x, y, z
- girth/DBH
- height
- crown-base height
- height of largest crown extension
- crown radii in four cardinal directions

This is exceptionally compatible with LiDAR individual-tree segmentation.

### Regeneration and ground vegetation
The inventory file defines a configurable spatial cell size used for:
- radiation transfer
- regeneration cohorts
- ground vegetation layers

Regeneration cells are 10 m x 10 m by default in published validation, but the current manual treats cell size as an input.

Since December 2022 Capsis development records document a HETEROFOR seed approach with:
- global seed dispersion
- local seed dispersion
- seed rain
- seed banks
- creation of regeneration cohorts from seed banks

Thus older assessments that HETEROFOR lacks spatial seed dispersal are obsolete for the current implementation.

Ground vegetation layers can be initialized cell-by-cell with:
- species
- height
- cover
- SLA
- water-storage traits
- light-demand traits
and the water-cycle lineage includes ground-vegetation transpiration.

## time structure
- meteorological forcing: hourly
- water balance: hourly
- GPP: hourly/daily depending option
- phenology: daily
- water/hydraulic stress: fine time step
- carbon allocation/tree dimensional update: yearly
- regeneration/mortality state: yearly scale, with some disturbances such as wind checked daily

For Gounsa this is much more compatible with an hourly/event geomorph engine than LANDIS-II's coarse vegetation update.

## roots

### Fine roots
Per individual tree:
```
b_fine_root = b_leaf * r_fine_root_leaf
```
with the ratio responding to nutrient status.

Fine-root litter:
```
s_fine_root
= b_fine_root * delta_fine_root * (1 - retranslocation)
```

### Structural roots
Structural belowground biomass is explicitly allocated.
Structural-root mortality is represented with a turnover term.
Root biomass can be output in size classes, but those size classes were not functional model states in HETEROFOR 1.0.

### Vertical distribution
Soil input includes fine-root proportion by horizon.
Hourly root-water uptake is distributed among horizons according to:
- fine-root proportion
- soil water potential
- compensatory uptake

### Horizontal distribution
There is no explicit branched root architecture around each tree.
Fine-scale water mode uses an individual pedon for each tree.
This provides a defensible horizontal support area, but converting it into RLD/RSAD or root-reinforcement maps remains a new coupling.

## water
Two modes:
1. stand-scale water balance
2. individual-tree pedon water balance

Water balance is hourly.
Pedon mode has no lateral redistribution between pedons.

Therefore HETEROFOR is not the Gounsa 2D runoff engine.
Preferred architecture:
```
LiDAR/geomorph hydrology
 -> local soil moisture / soil depth
 -> HETEROFOR pedon/tree stress
 -> vegetation state
 -> geomorph resistance/storage
```

## litter and dead organic matter
Published 1.0:
- leaf litter flux
- fine-root litter flux
- structural root mortality

Newer HETEROFOR soil-carbon lineage additionally distinguishes:
- standing deadwood/snags
- lying deadwood
- belowground deadwood
- aboveground decaying litter
- belowground decaying litter

This is highly relevant for postfire Gounsa.

## regeneration and dispersal
Current Capsis development record confirms:
- seed production context via fruit production
- global/local seed dispersion
- seed rain
- seed bank
- germination/mortality
- cohort generation
- spatialization of recruits

This directly addresses one of the main weaknesses that eliminated standard LPJ-GUESS.

## disturbances
Current documented mechanisms include:
- carbon-starvation/drought/light mortality
- wind damage / ForestGALES-TMC
- impact of falling trees on neighbours/seedlings
- beech bark disease
- resprouting option for American beech
- silvicultural removals

### Wildfire gap
As of the May 2025 HETEROFOR 1.2 manual and 2026 Capsis documentation checked in this review, a native wildfire combustion/fire-spread module was not documented.

Therefore do not claim:
```
HETEROFOR simulates wildfire
```

For Gounsa, a viable new coupling is:
```
observed/prescribed 2025 fire severity
 -> tree/seedling/ground vegetation mortality
 -> leaf/fine-root/structural-root/CWD pool initialization
 -> HETEROFOR postfire regeneration and succession
```

Because the target study begins from an observed fire, lack of endogenous fire ignition/spread is less damaging than it would be for a stochastic fire-regime study.

## LiDAR interface
Potential direct inputs:
- tree x,y,z
- height
- DBH where field/allometric support exists
- crown base
- crown radius in cardinal directions
- stand boundary/shape

Potential LiDAR-derived validation:
- canopy height
- crown size
- gap pattern
- tree density
- postfire mortality/survivor map

LiDAR cannot directly provide root biomass, so root calibration still requires field/allometric literature.

## comparison with SEIB-DGVM
HETEROFOR advantages:
- exact individual tree coordinates as standard initialization
- configurable regeneration/ground-vegetation cell size
- hourly water balance
- individual-tree pedon option
- current global/local seed dispersion + seed bank
- explicit fine-root turnover/litter
- newer belowground deadwood and soil-carbon states
- temperate mixed-forest calibration and 120-year validation

SEIB advantages:
- native wildfire lineage
- standard DGVM carbon/vegetation disturbance integration
- more self-contained postfire model lineage

SEIB disadvantages under LiDAR criterion:
- main explicit space is within virtual forest aboveground structure
- fine roots are not horizontally structured
- standard seed dispersal limitations
- regional tiling/interplot exchange requires care

## current verdict
Under the LiDAR criterion, HETEROFOR is now a **co-first-choice or potentially first-choice** vegetation engine, ahead of iLand and LPJ-GM.

Final choice versus SEIB depends primarily on whether Gounsa requires:
A. only the observed initial wildfire -> HETEROFOR has the stronger LiDAR/geomorph interface
B. endogenous repeated wildfire within the 100-year run -> SEIB retains a major advantage

## related records
- papers/2020_Jonard_HETEROFOR_CarbonGrowth.md
- papers/2020_deWergifosse_HETEROFOR_Water.md
- papers/2023_Guignabert_HETEROFOR_Validation.md
- papers/2025_REGE_HETEROFOR_SoilCarbon.md


## 2026-09-22 LiDAR/root-interface refinement

Current HETEROFOR 1.2 manual confirms that the inventory explicitly accepts:
- a user-defined spatial cell size for radiation, regeneration cohorts and ground-vegetation layers
- each adult tree's relative x, y, z
- girth/DBH, height, crown-base height and four crown radii
- cell-by-cell regeneration cohorts
- cell-by-cell ground-vegetation layers
- fine-root proportion by soil horizon
- hourly meteorological forcing

The same manual confirms:
- stand-level or tree-level water-balance option
- soil-carbon dynamics with annually generated litter cohorts
- regeneration from an annually updated seed bank
- seed production, germination and mortality in the seed-bank option

No native wildfire/fire-spread option was found in the May 2025 HETEROFOR 1.2 manual. Therefore fire remains an external initial-disturbance coupling for the current Gounsa design.

### Spatial root helper

HETEROFOR itself does not provide a full branched horizontal root architecture. The preferred published helper is now ChaMRoots (Mao et al. 2015).

```
HETEROFOR / LiDAR
 tree x,y
 DBH / basal area
 species
     |
     v
ChaMRoots
     |
     +--> RID by x,y,z
     +--> root diameter spectrum
     +--> vertical root profile
```

ChaMRoots was explicitly designed to be coupled with spatially explicit individual-based forest dynamics models.

For shallow landslides, do not convert this to a single apparent cohesion. Use the Schwarz spatial root-distribution + Root Bundle Model lineage:

```
ChaMRoots/root map
  -> root diameter and density field
  -> Root Bundle Model
  -> spatial root reinforcement
  -> slope stability
```

For water erosion, use a separate forest-root erosion-resistance interface. Root reinforcement and erosion resistance remain different processes.

### Current provisional ranking under LiDAR criterion

1. HETEROFOR + spatial root helper
2. SEIB-DGVM
3. LANDIS-II + NECN
4. iLand
5. LPJ-GM

This is not a generic ranking of forest models. It applies specifically to Gounsa's observed-fire, LiDAR-initialized, fine-scale vegetation-geomorph coupling problem.

HETEROFOR's main unresolved weakness is absence of a documented native wildfire module. If repeated endogenous fire is required inside the 100-year simulation, SEIB-DGVM must be reconsidered.
