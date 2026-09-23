# Spatially explicit cohort vegetation precedents

Date: 2026-09-23

## Question
Are there published/model precedents where BiomeE/BiomeEP-like cohort vegetation dynamics are embedded in actual geographic cells rather than individual-tree coordinates or spatially implicit patches?

## Answer
Yes. There are three distinct levels of spatial explicitness.

### 1. Georeferenced but weakly linked cells: ModelE-BiomeE
- BiomeE cohorts are embedded in NASA GISS ModelE grid cells.
- 2022 global test used 2.0° x 2.5° grid cells.
- physiology: half-hour/hour
- growth/phenology: daily
- demography: annual
- trees, shrubs and grasses represented.
- However, no explicit intercell seed-dispersal landscape process was identified.

Role: proves BiomeE can be tiled geographically, but is much too coarse and not a fine landscape analogue.

### 2. Native spatial cohort forest landscape models: LandClim and TreeMig
LandClim:
- 25 m x 25 m geographic cells
- species-age cohorts
- annual stand dynamics
- monthly climate/drought forcing
- cells linked through seed dispersal and disturbances

TreeMig:
- geographic rectangular grid
- species/height classes instead of individual stems
- seed bank and intercell seed dispersal
- cell sizes documented from about 25 m to 1 km
- annual demography

Role: strong precedent that fine geographic cells and cohort succession can be directly linked, but belowground/litter/understory physiology are too weak for Gounsa.

### 3. Cohort ecophysiology + actual spatial wrapper: MEDFATE + medfateland
This is the closest structural precedent to the Gounsa target.

MEDFATE:
- tree, shrub and optional herb cohorts
- daily water/carbon/growth
- cohort-specific fine-root vertical distribution
- mortality
- tree/shrub recruitment and resprouting

medfateland:
- actual sf point/cell spatial units
- terra raster topology
- user-defined grid cell size
- seed dispersal between stands/cells
- lateral surface/subsurface/groundwater flows
- daily one-day landscape functions
- distributed forest dynamics via `fordyn_land`
- continuation of state via `update_landscape()`

Published 2025 example:
Balaguer-Romano et al. used medfate + medfateland at 200 m resolution over the Barcelona Metropolitan Region, with each forest cell containing overstory trees and understory shrubs and with growth, mortality and succession simulated from 2015 to 2050. The authors explicitly identified computation as the reason for the 200 m minimum used in that application.

2026 package documentation demonstrates connected watershed grids with 100 m cells. No hard-coded minimum cell dimension was identified.

## 2026-09-23 code audit: herbaceous dynamics
Newer medfate versions do more with herbs than initially assumed:
- `herbData` can contain species-specific herb cohorts.
- `growthInput()` includes herb root-depth information.
- package tests explicitly run `growth()` and `fordyn()` with herb cohorts.

But the demographic regeneration code remains woody-focused:
- seed production/recruitment branches into tree vs shrub recruits.
- new recruits are created only as tree/shrub cohorts.
- `herbData` is removed from recruit/resprout objects.

Therefore:
- existing herb cohorts can undergo physiological/growth simulation,
- complete endogenous herb seed-recruitment succession is not implemented at the same level as tree/shrub succession.

This distinction is important for the first postfire years at Gounsa.

## 10–25 m vegetation grid decision
A 10–25 m medfateland raster is **structurally allowed**, because grid resolution is user-defined via `terra::SpatRaster`; there is no identified hard lower-resolution guard.

However:
- published medfateland landscape applications identified here use 200–500 m,
- official connected-watershed example uses 100 m,
- therefore 10–25 m should not be described as validated medfateland scale.

Cell-count scaling per km²:
- 200 m: 25 cells
- 100 m: 100 cells
- 25 m: 1,600 cells
- 10 m: 10,000 cells

Relative to 200 m, 25 m is 64x more cells and 10 m is 400x more cells per area.

Recommended test strategy:
1. 25 m vegetation grid as first production benchmark.
2. 10 m only on a small subcatchment initially.
3. Keep geomorphic DEM/grid finer, e.g. 1–5 m, and exchange aggregated/disaggregated states.
4. Adopt 10 m vegetation only if it materially changes vegetation/geomorphic feedback relative to 25 m.

## Event-driven geomorphic feedback decision
medfateland state continuation is a real advantage, but dynamic soil-depth coupling is not native.

Changing soil-layer widths with `soil_redefineLayers()` causes initialized soil state variables to be lost/recomputed. A `growthInput` additionally stores root fractions by soil layer, rhizosphere water state, internal carbon, litter and soil-carbon pools.

Therefore storm erosion/deposition requires a new conservative remapping layer:
```
geomorph event
 -> new soil thickness / DEM / water
 -> remap soil water + C/N
 -> recompute root fractions by layer
 -> preserve plant internal states
 -> resume daily medfate/medfateland
```

This is a **new coupling**, not an existing medfateland feature.

## Key distinction
`spatially explicit` must not be used as a single undifferentiated label.

For Gounsa distinguish:
1. **georeferenced independent tiles**: ModelE-BiomeE
2. **spatially linked demographic cells**: LandClim, TreeMig, LANDIS-II
3. **spatially linked cohort ecophysiology/hydrology cells**: MEDFATE + medfateland

The third category is the closest architectural match.

## Revised shortlist implication
MEDFATE + medfateland remains in the direct technical-test shortlist alongside BiomeE/BiomeEP, ED2 and FATES.

Current special advantage over BiomeE:
- spatial wrapper already implemented
- seed dispersal already implemented
- lateral water transfer already implemented
- one-day state stepping already implemented
- tree + shrub understory dynamics already implemented
- herb cohorts can already enter growth calculations

Remaining problems:
- Mediterranean parameterization
- no complete endogenous herb recruitment succession
- 10–25 m not yet validated in published landscape applications
- geomorphic soil-depth/root-exposure feedback requires new state remapping

## Decision
Do not reject MEDFATE + medfateland on spatial-resolution grounds: 10–25 m is structurally possible. Do not claim it is validated at that scale either.

Do not claim that MEDFATE has complete herbaceous succession: existing herb cohorts can be simulated, but tree/shrub recruitment is more complete than herb recruitment.

MEDFATE + medfateland remains the strongest direct precedent for the desired architecture, but BiomeE/FATES retain an advantage if autonomous grass/herb recruitment and replacement are mandatory.