# LANDIS-II + NECN for Gounsa

## 현재 판정
고운사 100년 산불 후 식생천이의 강한 raster-cohort 후보. 다만 event-driven geomorph coupling을 위해 시간구조를 엄격하게 재검토해야 한다.

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
FineRootBiomass = FoliarBiomass * FineRootFraction_species
```

Coarse root:
```
CoarseRootBiomass = WoodBiomass * CoarseRootFraction_species
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

따라서 산불 후 live-root mortality, dead-root decomposition, litter/CWD 변화를 기존 ecosystem model 안에서 추적할 수 있다.

## 하층식생 및 천이
최신 NECN 계보의 중요한 장점:
- `Grass` species type 존재
- trees, shrubs, grasses를 species/cohort로 취급 가능
- woody regeneration은 기존 woody biomass뿐 아니라 grass biomass에 의한 light competition도 받음
- growth, mortality, reproduction, dispersal, regeneration이 succession extension 안에 존재
- species별 wood/leaf/root C:N 및 above/belowground biomass를 계산

따라서 PnET-Succession보다 고운사 초기 postfire herbaceous stage를 표현할 구조가 더 명확하다.

## 시간 구조
NECN의 ecosystem production, water, C/N dynamics는 월 단위가 핵심이다.
LANDIS-II disturbance/succession framework의 상태 갱신 역시 event-scale ecohydrology를 위해 설계된 것은 아니다.

고운사에서 가장 큰 문제:
```
폭우 6시간
 -> erosion / deposition / soil-depth change
 -> 즉시 vegetation environment change
```
를 같은 달 중간에 NECN이 자연스럽게 반영하는 표준 구조가 확인되지 않았다.

따라서 monthly ecology 자체보다 중요한 것은:
- arbitrary-event restart
- soil-depth/moisture map replacement
- carbon/nitrogen pool remapping
- cohort mortality due to burial/root exposure
을 wrapper 또는 core modification 없이 가능한지 여부이다.

이 부분이 해결되지 않으면 NECN은 spatial representation은 가장 좋지만 Gounsa 양방향 event coupling에는 시간적으로 너무 거칠다.

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
- grass/shrub/woody biomass
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

## Hotta et al. 2026 precedent
Hotta et al. modified NECN to simulate post-landslide forest recovery.
Confirmed inputs include slope angle, soil depth and soil moisture maps and slope-dependent establishment.
Soil depth affects water storage capacity.

This is a precedent for:
```
geomorphic state -> LANDIS-II vegetation recovery
```
not yet for dynamic event-by-event two-way geomorphic coupling.

## root/litter conversion
Safest current interface remains:
```
NECN fine-root biomass
 -> species-specific SRL
 -> RLD
 -> forest erosion-resistance relation

NECN surface litter mass
 -> species-specific SSA
 -> measured/validated cover-contact state
 -> rainfall/splash/runoff protection

NECN dead fine-root / soil litter
 -> belowground RLD/RSAD/LSAD-type resistance
```

For shallow landslide reinforcement use a separate root-mechanics lineage. Do not equate erosion resistance with root cohesion.

## current comparison
NECN advantages:
- genuine raster landscape cells
- built-in seed dispersal and succession
- trees/shrubs/grasses
- live/dead roots
- litter/CWD
- fire integration
- simpler than ED/FATES

NECN disadvantages:
- monthly ecological time scale
- event-time state injection is not a standard strength
- small Gounsa domain may suffer edge/seed-source effects

## 최종 판정
**Strong simple spatial cohort candidate, but not yet selected.**

If storm-time bidirectional coupling can be implemented defensibly, NECN becomes extremely attractive. If not, BiomeE/ED/FATES provide better temporal process resolution but need external spatial tiling.
