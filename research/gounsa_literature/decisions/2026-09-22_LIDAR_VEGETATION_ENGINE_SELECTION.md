# LiDAR 기반 고운사 식생모델 재선정

날짜: 2026-09-22

## 배경

기존 식생축은 다음 순서로 검토되었다.

1. LPJ-GUESS
   - daily physiology와 root/litter state는 강함
   - standard grid/patch 간 명시적 공간연결 부족

2. LANDIS-II + NECN
   - landscape succession과 disturbance는 강함
   - 고운사 event/hourly geomorph model에 비해 vegetation exchange가 거침
   - individual-tree LiDAR initialization과 직접 맞지 않음

3. iLand
   - individual trees와 2 m light/regeneration grid는 강함
   - water/NPP/soil processes의 핵심 resource unit가 100 m x 100 m
   - 1-5 m LiDAR geomorph feedback과 scale mismatch

4. LPJ-GM
   - LPJ-GUESS의 seed migration 문제를 해결
   - published local vegetation cells are 1 km
   - LiDAR fine-scale site application에는 너무 거침

5. SEIB-DGVM
   - 30 m virtual forest, internal 1 m establishment mesh
   - individual trees, fine-root biomass, litter, daily physiology
   - cold-temperate PFT lineage, native wildfire/SPITFIRE lineage
   - topographic-hydrology coupling precedent
   - 그러나 standard public version은 one virtual forest point simulation이고 inter-plot seed dispersal 및 horizontal root geometry가 약함

사용자가 LiDAR를 활용하고 vegetation-geomorph coupling을 30 m보다 세밀하게 구성할 수 있음을 명확히 했다.

따라서 최종 기준을 다음으로 수정한다.

## 최종 평가 기준

1. LiDAR 개체목/수관 구조를 직접 초기화 가능
2. 1-10 m 이하 공간상태와 자연스럽게 연결
3. 100년 forest succession
4. seed production/dispersal/regeneration
5. fine-root biomass 및 turnover
6. litter/dead organic matter
7. hourly/daily ecohydrology 또는 최소한 fine-time-step climate response
8. soil depth/moisture feedback 가능
9. postfire recovery
10. open/modifiable implementation

## 현재 최우선: HETEROFOR + helper models

### HETEROFOR가 올라온 이유

Current HETEROFOR 1.2 manual and Capsis records confirm:

- adult tree x,y,z initialization
- DBH/girth
- total height
- crown-base height
- crown extension height
- crown radii in four directions
- user-defined cell size for radiation, regeneration cohorts and ground vegetation
- cell-by-cell regeneration cohorts
- cell-by-cell ground-vegetation layers
- hourly meteorology
- hourly water balance
- optional tree-level water balance
- fine-root proportion by soil horizon
- fine-root allocation and turnover
- structural/coarse-root biomass
- soil-carbon dynamics
- annually generated litter cohorts
- seed-bank regeneration
- annual seed production, germination and mortality
- Capsis 2022 seed approach with global/local seed dispersion and seed rain
- 0.5-5 ha intended stand scale
- decade-to-century simulations
- temperate mixed-forest calibration and 120-year validation

This combination is currently the closest to the Gounsa coupling target.

## HETEROFOR root spatialization

HETEROFOR does not explicitly grow branched horizontal root systems.

Preferred helper:

### ChaMRoots, Mao et al. 2015

Inputs:
- tree position
- species
- breast-height basal area / DBH
- distance to each evaluation point
- obstacles such as stones

Outputs:
- fine-root RID in topsoil
- root diameter spectrum up to coarse roots
- vertical root-density profile

Architecture:

```
LiDAR
  |
  v
HETEROFOR adult trees
(x,y,z, DBH, crown, species)
  |
  +--> dynamic tree biomass / fine roots / structural roots
  |
  v
ChaMRoots
  |
  +--> x,y,z root-density field
  +--> diameter classes
  +--> depth profile
```

This is a new coupling, but ChaMRoots itself explicitly states that it can be coupled with spatially explicit individual-based forest-dynamics models.

## process-specific use of roots

Do not force one root variable into every geomorphic process.

### Water erosion
Use:
- forest-specific RLD/RID/RSAD relation
- erosion resistance parameterization

Do not use root cohesion automatically.

### Shallow landslide
Use:
- spatial root-distribution model
- Schwarz Root Bundle Model lineage
- progressive pullout/failure
- spatial reinforcement field

### Root bioturbation / weathering
Use:
- separate live-root abundance, turnover and woody-root terms

## litter spatialization

HETEROFOR provides leaf/fine-root litter flux and newer dead-organic pools.

Surface litter should be spatialized with a LiDAR crown/litterfall helper rather than collapsed into generic vegetation cover.

Preferred precedent:
Sanchez-Lopez et al. 2023:
- ALS individual crowns
- foliage biomass
- annual litterfall
- 5 m litter accumulation/decomposition map
- postfire residual litter

Architecture:

```
HETEROFOR leaf litterfall
+ LiDAR crown footprint
   |
   v
1-5 m surface-litter raster
   |
   +--> rainfall-detachment protection
   +--> surface roughness
   +--> sediment storage
```

Fine-root litter remains belowground and must not be sent to surface litter.

## main remaining HETEROFOR gaps

### 1. Native wildfire
No native wildfire/fire-spread module was identified in the May 2025 HETEROFOR 1.2 manual.

Therefore current Gounsa design is:

```
observed initial wildfire
 -> external fire-severity / mortality initialization
 -> HETEROFOR postfire succession
```

This is acceptable only if the 100-year experiment does not require endogenous repeated wildfire.

If repeated fire is required:
SEIB-DGVM + SPITFIRE becomes much more competitive.

### 2. Early postfire herb/shrub roots
HETEROFOR/Capsis has dynamic regeneration cohorts and vegetation-layer machinery, but current documentation does not yet establish a HETEROFOR state equivalent to:
- herb fine-root biomass
- shrub fine-root biomass
- herb/shrub root turnover
with the same confidence as adult-tree roots.

This is now the highest-priority vegetation gap.

### 3. Stand scale
HETEROFOR is designed primarily for 0.5-5 ha stands.

If the final Gounsa domain is substantially larger:
- one very large HETEROFOR stand must be performance-tested, or
- multiple stands must exchange seeds and geomorphic states through a wrapper.

Inter-stand coupling would be new coupling.

## SEIB-DGVM retained as second primary candidate

SEIB strengths:
- native fire lineage, including SEIB-DGVM SPITFIRE
- fine-root biomass
- litter
- grasses and woody PFTs
- daily physiology
- cold-temperate PFT implementation
- internal 1 m establishment mesh
- topographic hydrology precedent

SEIB weaknesses:
- standard distribution is a single virtual forest point simulation
- inter-plot seed exchange is not standard landscape succession
- fine roots are not a detailed horizontal root architecture
- direct LiDAR initialization is less straightforward than HETEROFOR

## SORTIE-ND retained as comparator

Current 7.06 strengths:
- individual tree positions
- fine-scale neighbourhood processes
- recruitment
- configurable grids
- litter/moss/fresh logs/decayed logs/tip-up substrate
- strong postfire 100-year application precedent
- open source

Weakness:
- no standard dynamic fine-root biomass/turnover/root-water-uptake state
- fire can be represented as episodic mortality, not mechanistic fire spread/combustion
- weaker physiological soil-water coupling

Therefore below HETEROFOR and SEIB for the geomorph coupling objective.

## Current Gounsa-specific order

This is not a general model ranking.

For:
- observed initial wildfire
- LiDAR tree map
- fine-scale hillslope geomorphology
- roots/litter as quantitative states
- 100-year succession

current order is:

1. HETEROFOR + ChaMRoots + spatial litter helper
2. SEIB-DGVM
3. SORTIE-ND + external root helper
4. LANDIS-II + NECN
5. iLand
6. LPJ-GM
7. standard LPJ-GUESS

## next mandatory checks before final lock

1. HETEROFOR ground-vegetation dynamics
   - confirm available vegetation-layer species
   - confirm dynamic height/cover/LAI
   - determine whether root biomass can be added without rewriting core physiology

2. HETEROFOR domain/performance
   - maximum practical plot size
   - 1 m, 2 m, 5 m cell runtime
   - multi-stand scripting

3. postfire initialization
   - surviving tree map from LiDAR
   - dead standing/fallen tree initialization
   - initial litter and seed-bank state
   - live/dead root pools immediately after fire

4. Korean species parameterization
   - Quercus mongolica and related oaks
   - Pinus densiflora
   - understory shrubs/herbs

5. one-to-one variable interface with geomorph model
   - hourly soil moisture
   - annual tree/root state
   - litter raster
   - CWD raster
   - root reinforcement raster
   - soil-depth update
