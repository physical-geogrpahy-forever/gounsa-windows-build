# Strict spatial cohort vegetation model screen

Date: 2026-09-23
Updated: 2026-09-23, user clarification of criterion 3 incorporated

## 고정 기준
향후 고운사 vegetation engine 후보는 다음 다섯 조건을 각각 판정한다.

1. 실제 geographic x-y cell 또는 terrain unit 안에서 cohort/size/age structured vegetation을 계산할 것. 단순 statistical patch만으로는 부분 충족. 단, 지나치게 무거운 완전 개체목 모델만을 고집하지 않으며, 세밀한 landscape model 또는 개별목을 단순화한 cohort-hybrid도 허용한다.
2. understory herb/grass/shrub와 succession을 매우 명시적으로 고려할 것. 단순 ground-cover correction이나 regeneration blocker만으로는 불충족.
3. **soil depth 자체가 모델 내부에 동적으로 구현되어 있을 필요는 없다.** 핵심은 토양-지형모델과 양방향 또는 최소 단방향으로 결합할 수 있는가이다. 외부 모델이 계산한 soil-layer thickness, WHC/field capacity/wilting point, soil-water content/potential, water-table depth, lateral source/sink, hydraulic properties 등을 vegetation model이 받아 생장, 수분스트레스, 경쟁, 정착, 고사에 반영할 수 있으면 충족 가능하다. `soilDepth` 내장 여부보다 **state exchange / restart / soil-state overwrite 가능성**을 우선 평가한다.
4. 실제 catchment, hillslope, terrain 또는 topographic redistribution 적용 선례가 있을 것.
5. vegetation physiology/ecohydrology의 operational timestep이 <=1 day, 가급적 hourly/subhourly일 것. Demographic scheduling이 연 단위인 경우에는 별도로 표시한다. 환경반응 자체가 월 단위뿐이면 불충족.

## 기준 3의 세부 판정
두 수준을 구분한다.

- **3A soil-hydrology state coupling**: 외부 모델의 soil moisture, water potential, water table, lateral flow, WHC 관련 상태를 식생 계산에 주입 가능. 이것이 최소 요구조건이다.
- **3B dynamic soil geometry coupling**: 침식/퇴적으로 soil depth 또는 layer thickness 자체가 바뀔 때 물, C/N, 뿌리 분율을 새 층 구조로 재매핑하고 식생에 연속적으로 전달 가능.

3A가 문헌상 구현되어 있으면 기준 3을 충족으로 본다. 3B까지 기존 문헌에 구현되어 있지 않으면 고운사에서의 해당 부분은 **새로운 coupling**으로 명시한다.

## 현재 strict comparison

| Model lineage | 1 spatial cohort | 2 understory succession | 3 soil-topography coupling readiness | 4 catchment/topography | 5 fast timestep / demography | 현재 판단 |
|---|---|---|---|---|---|---|
| MEDFATE 5.x + medfateland 3.0 | YES: actual sf/grid units + tree/shrub/herb cohorts | STRONG-PARTIAL: tree/shrub recruitment, seed bank, resprout explicit; herb cohorts participate in growth but herb recruitment is not yet documented | **VERY STRONG**: layered soil, `lateralFlows`, `waterTableDepth`; `soilDomains="none"` explicitly allows external bulk-soil flow | **YES**: connected watershed grid, overland/subsurface/groundwater transfer + seed dispersal | daily growth/water; optional 24 substeps/day and subdaily hydraulics; `fordyn` top-level yearly but recruitment mode can be daily | easiest real-space prototype; herb recruitment remains the main gap |
| LPJ-DH / LPJG-WHyMe-TFM | YES at geographic 50 m cells; within-cell patches/cohorts are statistical | YES at PFT level including trees/shrubs/grass; species-level understory is less explicit than MEDFATE cohorts | STRONG: soil-water/WHC affects vegetation; architecture readily receives routed water | **YES**: Stordalen catchment, DEM routing, 50 m, six outlets | daily ecohydrology / slower demographic scheduling | strongest published fine-catchment precedent |
| PF-LPJG 2026 | YES at geographic grid; within-cell patches/cohorts statistical | architecture strong for PFT succession; explicit fine-scale understory not central in Danube test | **VERY STRONG DIRECT PRECEDENT**: ParFlow soil moisture overwrites LPJ state daily; root uptake/ET feeds back | **YES**: 3-D surface-subsurface hydrology; published Danube basin test | ParFlow hourly + LPJ daily / demographic events slower | strongest modern open external-soil-hydrology coupling precedent |
| ELM + ParFlow + FATES | PARTIAL: actual terrain columns, internal disturbance patches statistical | STRONG demographic cohorts, canopy competition, recruitment/seed processes; published BCI case tree-focused | **VERY STRONG DIRECT PRECEDENT**: ELM hydrology replaced by ParFlow; soil moisture passed every coupling step; root extraction feeds back | **YES**: explicit hillslope topography and 3-D lateral subsurface flow at BCI | ELM half-hourly; FATES vegetation dynamics daily | strongest mechanistic hillslope coupling, but heavy stack and strict within-cell spatiality partial |
| LandscapeDNDC / PSIM | YES landscape cells | PARTIAL: ground vegetation + regeneration cohorts, but autonomous full succession weak in key precedents | STRONG | YES alpine/mountain terrain | hourly ecosystem processes / regeneration scheduling variant dependent | strong hourly mountain benchmark |
| PICUS v2.0 | YES 10x10 m patches, but individual-tree heavy | WEAK-PARTIAL: tree regeneration explicit; herb/shrub competition and succession not explicit | STRONG local multi-layer soil, daily plant-water response | PARTIAL: alpine topography and terrain radiation, but not catchment lateral hydrology | daily C gain / annual allocation and tree demography | useful spatial forest comparator, fails criterion 2 and weak criterion 4 |
| HETEROFOR | YES but adult trees individual; seedlings cohorted | WEAK: understorey mainly tree regeneration | STRONG layered soil-water coupling | PARTIAL | hourly water / slower structure updates | too tree-centric for criterion 2 |
| iLand | YES spatial hybrid | WEAK: ground vegetation mostly aggregate light-driven cover/regen competition | STRONG | YES terrain inputs, but catchment hydrology not its core | daily water / annual tree dynamics | criterion 2 fails |
| Haga LANDIS-II NECN | YES, 10 m | **YES**: Sasa species-age biomass cohort with regeneration/resprout | coupling possible | YES landscape/topographic raster | **NO**: monthly ecosystem process | excellent spatial/understory precedent, fails timestep criterion |
| 4C | NO native landscape x-y; horizontally homogeneous patch | PARTIAL: tree regeneration explicit, no rich herb/shrub succession | STRONG layered soil/WHC | weak: stand/site rather than routed catchment | daily water, weekly photosynthesis / annual growth-demography | fails criterion 1 and 4 |
| BiomeE/BiomeEP | external geographic tiling needed | STRONG tree/shrub/grass demography | STRONG local soil-water response | weak native catchment precedent | subdaily physiology/daily processes / annual population dynamics | biology strong, spatial wrapper required |
| ED2 | geographic polygons possible, internal patches statistical | STRONG variant-dependent | STRONG | some terrain/catchment applications but not a simple direct hillslope engine | subhourly physiology / demographic scheduling slower | spatial interpretation weak for geomorphic coupling |
| RHESSys | actual spatial hierarchy | NO strict age/size cohort demography | VERY STRONG | YES | daily | ecohydrology comparator, fails strict cohort criterion |
| tRIBS+VEGGIE | actual terrain/TIN but PFT-average, not cohort | PARTIAL dynamic PFT fractions | VERY STRONG | YES | hourly/minutes | strong non-cohort comparator |
| SORTIE-ND | strong explicit tree space | tree regeneration/succession strong but herbaceous understory limited | connectable local soil variants | local/topographic applications exist | **NO for criterion 5**: fundamental vegetation step is long | reject for current target |
| ForHyM2 | NO vegetation cohort engine | NO | strong daily forest hydrology | YES watershed applications | daily | hydrology module only, not a vegetation-engine candidate |

## MEDFATE / medfateland finding after 2026 update
Current documentation materially strengthens this lineage relative to older assessments.

- A living plant cohort can be a **tree, shrub or herb cohort** with species, height, abundance/cover, root-depth descriptors (`Z50`, `Z95`).
- `growth_day()` performs one-day water and carbon balance and accepts elevation, slope, aspect, runon, layer-wise lateral flows and water-table depth.
- Default hydrology uses 24 steps/day; advanced Sperry/Sureau options resolve subdaily plant hydraulics.
- `medfateland::fordyn_land()` runs forest dynamics on connected watershed grid cells while accounting for lateral water transfer, seed dispersal, recruitment and resprouting.
- `soilDomains="none"` is explicitly documented for situations in which **bulk soil water flows are handled externally**. This is especially important for Gounsa coupling.
- Current `fordyn` recruitment parameters and output tables explicitly define tree and shrub recruits. Herb cohorts are valid dynamic plant cohorts, but a complete herb seed-bank -> germination -> new herb cohort demographic loop is not documented. This is the main criterion-2 gap.
- Current medfate documentation also states that soil physical structure and hydraulic properties are static during a native run. Therefore storm-driven erosion/deposition changing layer widths requires an external remapping/update step: **새로운 coupling**.

## LPJ-DH key evidence
Tang et al. (2014):
- Stordalen catchment
- actual 50 m grid
- DEM-derived routing and lateral water flux between cells
- LPJ-GUESS vegetation retained
- tree line and biomass evaluated
- runoff evaluated at six outlets
- monthly runoff adjusted R2 about 0.87 versus about 0.43 for standard LPJ-GUESS

Critical weaknesses:
- within-grid-cell demographic patches are statistical, not mapped x-y individuals/cohorts
- legacy hydrology is simpler than ParFlow
- daily rather than hourly ecological coupling

## PF-LPJG 2026 key evidence
Jia et al. (2026):
- ParFlow handles 3-D variably saturated subsurface and overland flow at hourly resolution.
- LPJ-GUESS handles vegetation at daily coupling intervals.
- ParFlow-derived soil water overwrites LPJ-GUESS soil state after 24 hourly ParFlow steps.
- vegetation water extraction / ET feeds back to hydrology.
- published Danube demonstration is coarse (10 km), so it proves architecture rather than Gounsa-scale spatial validity.

This is direct evidence that criterion 3 should be evaluated as **soil-state exchange capability**, not as a requirement that vegetation code itself owns soil depth.

## ELM-ParFlow-FATES key evidence
Fang et al. (2022):
- explicitly resolved hillslope topography and 3-D subsurface flow at Barro Colorado Island.
- ELM one-dimensional subsurface hydrology and runoff were replaced by ParFlow.
- ParFlow supplies soil moisture to ELM/FATES; FATES root water extraction returns through ELM.
- FATES supplies cohort-based vegetation dynamics with daily structural change while ELM biophysics is half-hourly.

This is the strongest published precedent for `terrain hydrology -> cohort vegetation -> root-water feedback` at hillslope scale, although FATES patch structure within each geographic column is statistical.

## PICUS screen
PICUS was checked as a possible overlooked spatial candidate.

Strengths:
- 10 x 10 m spatial patches, explicit 3-D crown/light environment.
- explicit seed production, dispersal and juvenile tree recruitment.
- v2.0 has an arbitrary-layer soil model with retention curves and hydraulic conductivity.
- carbon gain and physiological response are daily.
- applications in heterogeneous Alpine landscapes and topographic radiation exist.

Reasons it does not displace the shortlist:
- tree-individual architecture is relatively heavy.
- explicit understory succession remains tree-regeneration centric; herb/shrub population dynamics are not a comparable explicit component.
- lateral watershed hydrology is not the core spatial process.
- allocation and major tree structural dynamics remain annual.

## Implication for Gounsa soil-geomorphic coupling
The proposed exchange variables should be treated as an interface rather than requiring one monolithic model.

Geomorph/hydrology -> vegetation after each geomorphically meaningful event or daily synchronization:
- active soil depth and layer thickness
- soil water content or matric potential by layer
- field capacity / wilting point / porosity / Ksat where changed
- water-table depth and lateral source/sink
- erosion or deposition depth
- root exposure / burial or disturbance mask
- updated DEM, slope, aspect and cell connectivity when changes are large enough

Vegetation -> hydrology/geomorphology:
- LAI and cover by stratum/cohort
- fine-root biomass and depth distribution
- transpiration/root-water uptake
- interception
- litter and ground cover
- biomass relevant to erosion resistance and root disturbance

If erosion/deposition changes layer geometry, water, C/N and root mass must be conservatively remapped to the new layers. No screened candidate yet provides this full storm-driven geomorphic remapping natively; therefore this element is currently classified as **새로운 coupling**.

## Current decision
Do not select a final vegetation model yet, but the search is now narrowed to four serious lineages with distinct roles:

1. **MEDFATE 5.x + medfateland 3.0**: strongest implementation candidate for actual spatial units and easiest direct coupling to a custom Gounsa geomorphic model. Main task is to determine how much herbaceous recruitment/succession must be added.
2. **LPJ-DH / LPJG-WHyMe-TFM**: strongest published fine-resolution catchment precedent showing that LPJ-GUESS ecology can work on a 50 m routed terrain grid.
3. **PF-LPJG 2026**: strongest modern open precedent for external 3-D soil-hydrology state exchange with LPJ-GUESS.
4. **ELM-ParFlow-FATES**: strongest mechanistic hillslope ecohydrology + demographic cohort precedent, but computationally and technically much heavier.

Next research should compare these four on the exact post-fire Gounsa coupling task, rather than continue broad model-name collection.
