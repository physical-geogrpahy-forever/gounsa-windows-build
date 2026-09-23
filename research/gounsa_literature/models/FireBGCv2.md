# FireBGCv2

## 왜 다시 검토했는가
고운사 식생모델의 다섯 조건을 엄격히 적용하던 중, FireBGCv2가 단순한 산불 확산모델이 아니라 실제 공간 경관에서 수목, 비수목 하층식생, 일별 물·탄소 과정, 화재, 종자분산을 함께 계산하는 landscape succession platform임을 재확인했다. 특히 사용자 기준이 완전한 cohort만 고집하지 않고 비교적 단순한 individual-tree / cohort-hybrid도 허용하므로 정식 후보로 재평가했다.

## 모델 성격
- spatially explicit landscape fire and succession model
- C++
- hierarchy: landscape -> site -> stand -> tree / undergrowth guild
- tree layer: individual trees
- undergrowth: herb/shrub species or functional guild biomass compartments
- fire, seed dispersal and other landscape disturbances are spatially simulated
- stand processes combine daily mechanistic ecosystem calculations with annual structural updates

## 1. 공간명시 구조
**STRONG, but not cohort-pure.**

- actual mapped stands/polygons and raster landscape layers
- each stand belongs to a biophysical site
- tree stratum is individual-tree based
- undergrowth is guild/functional-group biomass rather than individual plants
- landscape applications commonly use tens to hundreds of metres spatial resolution

Thus it is spatially much more literal than ED/FATES disturbance patches, but more computationally complex because woody vegetation is represented by individual trees.

## 2. 하층식생과 천이
**STRONG-PARTIAL to STRONG.**

FireBGCv2 explicitly represents an `undergrowth` layer as non-tree vegetation.
- shrub and herbaceous guilds can be separated
- documentation allows many guilds; individual undergrowth species can also be represented
- guild biomass, height, leaf area and ecophysiological parameters influence stand processes
- undergrowth interacts with water, light, tree regeneration, fire ignition and fire spread
- plant succession emerges from changing biomass composition of tree and undergrowth layers

Important limitation:
- woody-tree establishment/dispersal is considerably more mechanistic than herb/shrub population demography
- undergrowth biomass growth is represented by deterministic guild-level equations and reduction factors rather than a full seed-bank -> germination -> age/size cohort cycle comparable to FATE-HD or FATES

Therefore it is substantially stronger than HETEROFOR/iLand for explicit non-tree undergrowth, but still weaker than a model with explicit herbaceous demographic cohorts.

## 3. soil-topography coupling readiness
### 3A soil-hydrology state coupling: MODERATE
Native FireBGCv2 calculates daily stand soil water, ET and runoff. Soil and site state can vary by biophysical site/stand and soil water is an explicit state variable.

However:
- native model assumes no water flow from stand to stand while calculating stand soil water
- generated surface/subsurface runoff is subsequently routed to streams for catchment discharge
- therefore lateral water redistribution does not feed back into upslope/downstream stand soil moisture in the way medfateland or ParFlow couplings can
- no clean documented external-soil-domain switch analogous to MEDFATE `soilDomains="none"` was identified

External overwrite of soil state or soil properties is conceptually possible by modifying source/state handling, but would be a **new coupling** and likely more invasive than MEDFATE.

### 3B dynamic soil geometry: NEW COUPLING
Erosion/deposition-driven layer-thickness or soil-depth changes are not a native dynamic process. Conservative remapping of soil water, C/N and roots would need custom implementation.

## 4. 유역 / 지형 선례
**STRONG.**

- McDonald Drainage, Glacier National Park is a classic application
- explicit catchment simulation and streamflow routing exist
- later Yellowstone and western US applications classify sites using elevation, slope, aspect and soils
- topography, soils and weather define biophysical sites controlling productivity and species composition

This criterion is considerably stronger than for PICUS, 4C, HETEROFOR or iLand.

## 5. 시간해상도
**STRONG for physiology/ecohydrology; annual for major structural succession.**

Daily:
- weather
- species phenology
- photosynthesis
- respiration
- soil-water budget
- transpiration/evaporation
- some litter/decomposition processes

Annual or end-of-year:
- carbon allocation to trees
- diameter/height growth realization
- major tree establishment/mortality scheduling
- cone crop and seed dispersal
- landscape fire events/routing bookkeeping depending on module

Hence it satisfies the revised criterion 5 in the same broad sense as LPJ-GUESS/FATES: fast environmental response is daily, while demographic structure is slower.

## 고운사에서 사용할 수 있는 부분
Potentially useful outputs/state:
- tree biomass and structure
- shrub/herb guild biomass
- LAI by vegetation stratum
- fine-root and litter pools
- daily soil water, AET, runoff
- fire mortality and postfire succession
- site-specific elevation/slope/aspect/soil controls

For geomorph coupling, undergrowth biomass and root/litter terms are especially attractive because current Gounsa erosion/diffusion formulations need vegetation **amount**, not merely cover class.

## 필요한 새로운 coupling
1. external geomorphic model -> stand soil-water/state overwrite at event/daily boundaries
2. erosion/deposition -> dynamic soil-depth/layer remapping
3. root exposure/burial response
4. if required, replace/simple undergrowth guild biomass dynamics with explicit herb recruitment/turnover
5. possibly decouple fine geomorph grid from coarser stand grid

## 계산성과 구현성
Major disadvantage:
- model is explicitly described by its developers as complex and difficult to use without substantial training
- individual-tree representation raises runtime and parameter burden
- current public distribution/workflow is less convenient than MEDFATE R/C++ for frequent external state editing

The fact that it has been used for very large landscapes demonstrates feasibility at landscape scale, but not necessarily suitability for a 10–25 m, 100-year, storm-event coupled geomorphic simulation.

## five-criteria verdict
| criterion | verdict |
|---|---|
| 1 spatial cohort/hybrid | YES, explicit stands + individual trees + undergrowth guilds |
| 2 explicit understory succession | STRONG-PARTIAL |
| 3 soil/geomorph coupling readiness | MODERATE, custom coupling needed |
| 4 watershed/topography precedent | YES, STRONG |
| 5 <= daily process response | YES daily physiology/hydrology, annual structure |

## current role
**Serious secondary candidate / benchmark, newly promoted.**

FireBGCv2 is the first newly re-screened model in this round that genuinely satisfies enough of the five criteria to merit keeping. It does not displace MEDFATE + medfateland because external soil-state coupling and computational simplicity are worse, and it does not displace FATES biologically because herbaceous demographic cohorts are less complete. Nevertheless it is a uniquely relevant precedent because it combines:

```
actual mountain landscape
+ explicit tree layer
+ explicit herb/shrub undergrowth guilds
+ daily water/carbon processes
+ fire succession
+ catchment routing
```

## key references
- Keane, R. E., Morgan, P., & Running, S. W. (1996). Fire-BGC: a mechanistic ecological process model for simulating fire succession on coniferous forest landscapes of the Northern Rocky Mountains. USDA Forest Service Research Paper INT-RP-484.
- Keane, R. E., Loehman, R. A., & Holsinger, L. M. (2011). The FireBGCv2 landscape fire and succession model: a research simulation platform for exploring fire and vegetation dynamics. RMRS-GTR-255. https://doi.org/10.2737/RMRS-GTR-255
- Clark et al. (2017). Climate changes and wildfire alter vegetation of Yellowstone National Park, but forest cover persists. Ecosphere.
