# Gounsa cohort vegetation model screen: five fixed criteria

Date: 2026-09-23

## Fixed requirements
Candidate vegetation models are now screened against five requirements.

1. Spatially explicit cohort structure. A finely resolved landscape structure can also be considered, but an individual-tree burden is undesirable.
2. Understory vegetation and succession must be represented explicitly, preferably herbs/grasses, shrubs and trees with recruitment/competition/mortality.
3. Soil depth must be represented, or at minimum WHC / field capacity / wilting point / multilayer soil-water storage must be explicit.
4. Published application to a watershed, hillslope, mountain terrain or explicit topography must exist.
5. Ecophysiological/hydrological time step must be no coarser than daily; hourly/subhourly is preferred.

A model is not considered a full solution merely because it is a cohort model. Geographic cells must be distinguished from statistical subgrid patches, and understory physiology must be distinguished from true understory demography/succession.

## Current strict screen

| Model | 1 spatial cohort | 2 understory + succession | 3 soil depth / WHC | 4 terrain/watershed precedent | 5 <= daily | Current role |
|---|---|---|---|---|---|---|
| MEDFATE + medfateland | Strong | Medium-Strong | Strong | Strong | Strong | closest lightweight architecture |
| ELM + ParFlow + FATES | Partial | Strong | Strong | Strong | Strong | strongest process-complete heavy option |
| LandscapeDNDC / PSIM | Strong | Partial | Strong | Strong | Strong | hourly mountain benchmark, succession gap |
| LANDIS-II NECN + Haga understory | Strong | Strong | Strong | Strong | Weak | strongest East-Asian fine-grid succession precedent, timestep gap |
| BiomeE / BiomeEP | Weak-Partial | Strong | Medium | Weak-Partial | Strong | strong biology, spatial wrapper required |
| ED2 | Partial | Strong | Strong | Medium | Strong | spatially implicit patch problem |
| RHESSys / RHESSys-WMFire | Strong | Weak | Strong | Strong | Strong | watershed architecture precedent only |
| 4C | Weak | Medium | Strong | Weak | Strong | stand comparison model |
| PREBAS | Medium | Weak | Strong | Weak-Medium | Strong for fluxes | empirical ground vegetation, no dynamic vegetation |
| WoodPaM | Strong | Strong | Medium-Strong | Strong | Weak | strong criteria 1-4 precedent, annual timestep |
| FireBGCv2 | individual-tree, not cohort | Strong | Strong | Strong | Strong | complex landscape comparator only |

## MEDFATE + medfateland
### Why it survives
- local state is cohort-based rather than individual-tree
- medfateland puts forest states in actual GIS units and connected raster topology
- seed dispersal and lateral surface/subsurface water transfer are implemented
- daily growth/water/carbon functions exist
- tree and shrub recruitment are endogenous
- herb cohorts participate in physiology/growth
- cohort-specific fine-root depth distributions and layered soil hydraulics are explicit
- published landscape and catchment applications exist

### Remaining gap
Natural demographic regeneration is asymmetric: new recruits are generated for tree/shrub cohorts, while full herb seed -> recruitment -> new herb cohort succession is not implemented at the same level. Dynamic geomorphic soil-depth change also needs conservative state remapping.

## ELM + ParFlow + FATES
### Why it survives
- full tree/shrub/grass cohort demography
- explicit upper canopy and understory organization
- recruitment, growth, mortality and disturbance
- fine roots, root litter, CWD and fire
- half-hourly biophysics and daily vegetation dynamics
- 3-D ParFlow hillslope hydrology has been coupled to FATES through ELM
- real DEM/topographic slopes and lateral water redistribution demonstrated

### Remaining gap
FATES disturbance patches within each geographic column have no x-y locations. Therefore cohort patches are statistical subgrid areas even though the host ELM/ParFlow grid is geographic. This is a conceptual mismatch for direct rill/hollow/deposition coupling. The technical stack is also heavy.

## LandscapeDNDC / PSIM
### Why it survives as benchmark
Published mountain landscape application used:
- 100 m x 100 m actual grid
- 15,793 units
- hourly simulation for 15 years
- up to seven vegetation cohorts per cell
- one herb/grass ground-vegetation cohort
- two tree-regeneration cohorts
- four overstory cohorts
- foliage and fine-root biomass
- explicit total soil depth and fine vertical soil layers
- light, water and N competition

### Decisive gap
The paper explicitly states that LandscapeDNDC lacked a dynamic regeneration module. Tree regeneration cohorts were initialized rather than generated endogenously. Thus physiology and competition are excellent but autonomous succession is incomplete.

## LANDIS-II NECN + Haga understory
### Major new evidence
Haga et al. (2022) implemented Sasa kurilensis in NECN as a real species-age biomass cohort at 10 m x 10 m spatial resolution in southern Hokkaido.

Repository inspection confirms `sasa_spp` carries:
- cohort age and biomass
- longevity/maturity
- seed dispersal
- vegetative reproduction
- fire tolerance and postfire resprout
- fine/coarse root fractions
- fine/coarse-root C:N and lignin
- NECN litter and belowground pathways

This is not a simple cover multiplier. It is the strongest identified direct precedent for a dense East Asian understory species participating in full spatial forest succession.

### Decisive gap
NECN ecosystem calculations are monthly. This does not satisfy the strict daily/hourly requirement for storm-event geomorphic feedback.

## RHESSys
RHESSys is nearly ideal in spatial hydrology:
- basin -> hillslope -> zone -> patch -> canopy strata
- actual GIS patches
- overstory and understory strata
- fine roots and litter
- soil depth and storage capacity
- lateral downslope water redistribution
- daily ecosystem processes
- many mountain watershed applications
- RHESSys-WMFire adds daily fire/fuel coupling

However published RHESSys geomorphic work explicitly states that community composition, mortality and succession are not included and may be prescribed. Therefore RHESSys is not the required succession engine.

## PREBAS
PREBAS has daily GPP, ET and soil-water calculations and recent inputs include soil depth, effective field capacity and permanent wilting point. Multi-layer/size-class stand applications exist. However ground vegetation is an empirical biomass module based largely on site type and below-canopy light, and model metadata identify dynamic vegetation as absent. It does not meet criterion 2.

## FireBGCv2
FireBGCv2 is spatially explicit, daily, has explicit understory shrub/herb guilds, succession, soil depth and watershed hydrology. It is relevant because the user allows finely resolved landscape models as a secondary route. However its finest vegetation dynamics are individual-tree based, so it does not meet the preferred cohort architecture and is computationally complex.

## Current conclusion
No identified lightweight model satisfies all five requirements natively without an important caveat.

The closest architectures are:

### A. MEDFATE + medfateland
Best compromise if an explicit geographic grid, daily process coupling, soil/root detail and moderate implementation complexity are prioritized. Main custom work: herb recruitment/succession and geomorphic soil-depth state remapping.

### B. ELM + ParFlow + FATES
Best process-complete option if heavy infrastructure is acceptable. Main conceptual issue: internal cohort patches are spatially implicit even though the hydrologic columns are geographic.

### C. LANDIS-II NECN + Haga understory
Best precedent for 10 m East Asian spatial understory succession and roots/litter. Main blocking issue: monthly ecosystem timestep.

### D. LandscapeDNDC / PSIM
Best hourly spatial mountain-forest physiology benchmark. Main blocking issue: no endogenous dynamic regeneration module in the key application/version.

## Search priority from now on
Do not spend time on additional annual forest landscape models unless they contain a unique understory mechanism.
Search specifically for a model that improves on the remaining gap:

```
actual GIS grid
+ species/size/age cohorts
+ herb/shrub/tree endogenous recruitment and succession
+ soil depth or multilayer WHC
+ watershed/hillslope precedent
+ hourly/subdaily or daily process loop
```

If no such existing model is found, compare the engineering burden of:
1. adding herb demographic recruitment to MEDFATE/medfateland,
2. spatially interpreting FATES through sufficiently fine ELM/ParFlow columns,
3. introducing event-state updates into NECN,
4. adding a published recruitment module to LandscapeDNDC.
