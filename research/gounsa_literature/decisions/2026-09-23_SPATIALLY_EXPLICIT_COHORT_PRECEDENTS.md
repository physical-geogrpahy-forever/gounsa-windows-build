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
- tree and shrub cohorts
- optional herb layer
- daily water/carbon/growth
- cohort-specific fine-root vertical distribution
- mortality and annual recruitment

medfateland:
- actual sf point/cell spatial units
- terra raster topology
- seed dispersal between stands
- lateral surface/subsurface/groundwater flows
- daily one-day landscape functions
- distributed forest dynamics via `fordyn_land`

Published 2025 example:
Balaguer-Romano et al. used medfate + medfateland at 200 m resolution over the Barcelona Metropolitan Region, with each forest cell containing overstory trees and understory shrubs and with growth, mortality and succession simulated from 2015 to 2050.

2026 package documentation demonstrates connected watershed grids and one-day functions; example grids include 100 and 200 m cells. Cell size is user-defined, though computation increases strongly at fine resolution.

## Key distinction
`spatially explicit` must not be used as a single undifferentiated label.

For Gounsa distinguish:
1. **georeferenced independent tiles**: ModelE-BiomeE
2. **spatially linked demographic cells**: LandClim, TreeMig, LANDIS-II
3. **spatially linked cohort ecophysiology/hydrology cells**: MEDFATE + medfateland

The third category is the closest architectural match.

## Revised shortlist implication
MEDFATE + medfateland must be added to the direct technical-test shortlist alongside BiomeE/BiomeEP, ED2 and FATES.

Current special advantage over BiomeE:
- spatial wrapper already implemented
- seed dispersal already implemented
- lateral water transfer already implemented
- one-day state stepping already implemented
- tree + shrub understory dynamics already implemented

Remaining problems:
- Mediterranean species parameterization
- fully dynamic herbaceous succession is not yet demonstrated at the same level as woody cohorts
- published applications are currently much coarser (200-500 m) than desired Gounsa cells
- geomorphic soil-depth/root-exposure feedback remains new coupling

## Decision
Do not assume that a BiomeE-like cohort model must be spatially implicit. Published implementations show that the local cohort engine + GIS grid wrapper architecture is viable. MEDFATE + medfateland is currently the strongest direct precedent for that architecture and should be tested before building a custom spatial wrapper around BiomeE.
