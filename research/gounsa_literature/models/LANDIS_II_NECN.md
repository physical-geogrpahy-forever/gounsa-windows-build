# LANDIS-II + NECN for Gounsa

## 현재 판정
고운사 100년 산불 후 식생천이의 **최우선 식생모델 후보**.

기준 구성:
- LANDIS-II Core v8
- NECN Succession v8.x
- Dynamic Fire / fuels extension as needed

## LANDIS-II가 고운사에 주는 핵심 상태
NECN source inspection에서 확인:

### live vegetation
- species/cohort state
- aboveground wood biomass
- leaf biomass
- fine-root biomass
- coarse-root biomass
- LAI
- AGNPP/BGNPP

Fine root:
```
FineRootBiomass
=
FoliarBiomass * FineRootFraction_species
```

Coarse root:
```
CoarseRootBiomass
=
WoodBiomass * CoarseRootFraction_species
```

### dead biomass / litter
NECN은 다음을 별도 pool로 추적한다.
- surface wood
- soil wood = dead coarse roots
- surface litter = dead leaves
- soil litter = dead fine roots
- SOM1 surface/soil
- SOM2
- SOM3

따라서 산불 후:
```
live roots
 -> mortality
 -> dead fine/coarse root pools
 -> decomposition
```
과
```
leaf/wood mortality
 -> litter/CWD
 -> fire reduction
 -> decomposition
```
을 기존 ecosystem model 안에서 추적할 수 있다.

## fire effects
NECN source에는 fire severity별:
- coarse litter reduction
- fine litter reduction
- cohort wood reduction
- cohort leaf reduction
- SOM reduction
이 구현되어 있다.

## geomorphology에 직접 줄 수 있는 값
- species/cohort age/state
- live fine-root biomass
- live coarse-root biomass
- dead fine-root pool
- dead coarse-root pool
- surface litter
- surface dead wood
- LAI
- living biomass
- fire severity
- soil depth input state
- soil water-related state

## 직접 주지 않는 값
- RLD
- root diameter distribution
- root tensile strength
- RAR
- root cohesion
- litter contact area / LSAD
- geomorphic sediment flux
- erosion/deposition
- dynamic soil-depth loss by geomorphic erosion

따라서 LANDIS-II는 **vegetation driver**이고 geomorphic process model 자체는 아니다.

## Hotta et al. 2026 precedent
Hotta et al. modified NECN to simulate post-landslide forest recovery.

Source inspection of branch `ForLandslide` confirms:
- slope angle input map
- soil depth input map
- soil moisture input map
- slope-dependent establishment probability
- biomass threshold controlling recovery from slope limitation

Example:
```
site biomass
+ slope angle
 -> establishment probability adjustment
```

Soil depth is read from an input map and used in NECN water balance:
```
waterFull = soilDepth * fieldCapacity
waterEmpty = wiltingPoint * soilDepth
```

No evidence was found that the branch dynamically erodes soil depth or updates slope from geomorphic processes.

Therefore Hotta et al. is a published precedent for:
```
geomorphic state -> LANDIS-II vegetation recovery
```

but not yet for:
```
LANDIS-II vegetation -> geomorphic change -> LANDIS-II
```

## 고운사에서의 의미
고운사 coupling should preserve this direction:
```
geomorphic model
 -> updated soil depth / moisture / slope
 -> LANDIS-II NECN
```

The reverse direction should use independent published geomorphic process models fed by NECN vegetation states.

## 현재 지형모델 연결 우선순위
- water erosion: Iber+ candidate
- armour/profile/weathering: SSSPAM/mARM candidate
- postfire dry ravel: Lamb et al. 2011
- tree throw/root-fracture soil production: Gabet & Mudd 2010
- shallow-landslide root mechanics: Schwarz root-bundle lineage
- fire-spall source: unresolved

## 최종 판정
**식생모델로는 매우 유망.**
특히 LPJ-GUESS보다:
- explicit species/cohort succession
- landscape fire disturbance
- dead-root pools
- litter/CWD pools
- post-disturbance regeneration
을 고운사 100년 문제에 직접적으로 제공한다.

단, root geometry와 geomorphic resistance는 별도 published relation/model이 필요하다.


---

## 2026-09-22 Korean postfire applicability and geomorphic model interfaces

### Korean precedent
Lim & Choi (2025) applied LANDIS-II + PnET-Succession to the 2000 East Coast wildfire natural-restoration site in Goseong over 25 years.

Important:
- Quercus-dominated recovery was broadly reproduced.
- The authors explicitly warn that the 82 ha study area is much smaller than LANDIS-II's recommended >10,000 ha scale.
- Small-domain edge effects and seed dispersal can therefore be problematic.

For Gounsa, domain size must be treated as a model-validity issue, not merely a technical setting.

### geomorphic interfaces currently supported by literature

```
LANDIS-II / NECN
├─ cohort / wood / mortality
│    -> Gabet & Mudd 2010
│       root fracture + tree throw + soil production
│
├─ fire + vegetation recovery
│    -> Lamb et al. 2011
│       postfire dry-ravel storage/release
│
├─ fine/coarse root biomass
│    -> root allometry
│    -> Schwarz et al. 2010 RBM
│       shallow-landslide reinforcement
│
├─ fine-root + litter state
│    -> forest erosion-resistance relation [still unresolved]
│    -> Iber+ event erosion candidate
│
└─ soil depth / slope / moisture from geomorphic model
     -> Hotta et al. 2026 precedent
     -> LANDIS-II establishment and water balance
```

### key unresolved variable mappings
1. coarse-root biomass -> rootwad volume / tree-throw mechanics
2. fine/coarse-root biomass -> root diameter-class distribution
3. surface litter biomass -> litter cover/contact area
4. fine-root biomass -> rill erodibility
5. geomorphic soil-depth change -> NECN soil carbon/nitrogen pool remapping
