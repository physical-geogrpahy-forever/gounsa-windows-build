# LandClim + herbaceous-understorey extension

업데이트: 2026-09-23

## 현재 판정
**공간적 산불후 천이 비교모델로 매우 좋지만 시간해상도 때문에 strict shortlist 탈락.**

LandClim 자체는 25 x 25 m geographic cells에서 tree age cohorts, climate/soil/topography, seed dispersal and disturbance를 계산한다. Thrippleton et al. (2016, 2018) 계열은 여기에 grasses, forbs, ferns, small herbs, shrubs 등 동적 하층식생을 추가해 post-disturbance overstory-understory succession을 연구했다.

이는 고운사 criterion 1, 2, 4에는 매우 잘 맞지만 criterion 5가 결정적으로 맞지 않는다.

## spatial/cohort structure
- 25 x 25 m actual landscape grid
- tree state = species x age cohorts
- cohort stem number + biomass
- seed dispersal links cells
- fire/wind/bark-beetle disturbances spatially explicit
- climate, topography, soil WHC differ among cells

## understory extension
Thrippleton et al. added a dynamic herbaceous understory layer with PFTs such as:
- grasses
- forbs/tall forbs
- ferns
- small herbs
- shrubs

Understory biomass/light interception affects tree establishment.
Overstory shading in turn controls understory abundance/composition.

Published experiments started from disturbance/open conditions and reproduced delayed or, under some conditions, arrested tree succession.

This is strong evidence that:
```text
post-disturbance herb/shrub layer
 <->
 tree regeneration
```
can be embedded in a spatial cohort forest landscape model.

## time structure
This is the decisive weakness.

- stand recruitment/growth/mortality: annual
- monthly climate/drought drivers
- some landscape processes including seed dispersal/disturbance operate at coarser/decadal scheduling in classic configurations

Therefore storm-scale geomorphic feedback such as:
```text
6-hour extreme rainfall
 -> erosion / soil-depth loss
 -> immediate soil-water/root-state response
```
is outside native LandClim temporal design.

## soil / hydrology
Tree growth responds to climatic drought calculated using temperature, precipitation and soil water-holding capacity.

This provides soil moisture limitation but not a detailed layered root-zone hydrology comparable to FATES-ParFlow, LandscapeDNDC or MEDFATE.

## topography
Strong:
- actual DEM-derived spatial landscape
- mountain/alpine applications
- elevational gradients
- soil/topographic variability
- spatial disturbance and dispersal

## Gounsa 5 criteria
| criterion | verdict |
|---|---|
| 1 spatial cohort | VERY STRONG |
| 2 explicit understory succession | VERY STRONG in Thrippleton extension |
| 3 soil/root coupling | PARTIAL: WHC/drought strong, layered roots weak |
| 4 terrain/landscape precedent | VERY STRONG |
| 5 <=daily | FAIL: annual forest dynamics |

## 고운사에서의 역할
LandClim-understory is an excellent benchmark for:
- herbaceous competition delaying tree regeneration
- post-disturbance grass/forb/fern/shrub trajectories
- geographic 25 m cohort cells
- spatial dispersal/disturbance

But it should not be the production vegetation engine for an event-driven hourly geomorphology coupling.

## key references
- Schumacher et al. (2004). Ecological Modelling 180, 175–194.
- Thrippleton, T., Bugmann, H., Kramer-Priewasser, K., & Snell, R. S. (2016). Herbaceous Understorey: An Overlooked Player in Forest Landscape Dynamics? Ecosystems, 19, 1240–1254.
- Thrippleton et al. (2018). Herbaceous competition and browsing may induce arrested succession in central European forests. Journal of Ecology. https://doi.org/10.1111/1365-2745.12889
