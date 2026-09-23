# Strict spatial cohort vegetation model screen

Date: 2026-09-23

## 고정 기준
향후 고운사 vegetation engine 후보는 다음 다섯 조건을 각각 판정한다.

1. 실제 geographic x-y cell 또는 terrain unit 안에서 cohort/size/age structured vegetation을 계산할 것. 단순 statistical patch만으로는 부분 충족.
2. understory herb/grass/shrub와 succession을 매우 명시적으로 고려할 것. 단순 cover correction은 불충족.
3. soil depth를 직접 고려하거나 최소한 WHC/field capacity/wilting point/soil-water-storage가 vegetation growth에 직접 feedback할 것.
4. 실제 catchment, hillslope, terrain 또는 topographic redistribution 적용 선례가 있을 것.
5. vegetation physiology/ecohydrology의 operational timestep이 <=1 day, 가급적 hourly/subhourly일 것. Annual demography는 허용하되 환경반응이 월 단위뿐이면 불충족.

## 현재 strict comparison

| Model lineage | 1 spatial cohort | 2 understory succession | 3 soil depth/WHC | 4 catchment/topography | 5 <=daily | 현재 판단 |
|---|---|---|---|---|---|---|
| LPJ-DH / LPJG-WHyMe-TFM | YES | YES | YES via WHC | YES | YES daily | 현재 가장 직접적인 published fine-catchment precedent |
| PF-LPJG 2026 | YES at geographic grid; published at 10 km | model architecture YES, explicit understory not demonstrated in Danube case | YES, 3D soil moisture and groundwater | YES | YES, ParFlow hourly + LPJ daily | strongest modern open coupled framework; fine-scale validation missing |
| MEDFATE + medfateland | YES | PARTIAL: tree/shrub full, herb physiology YES but herb recruitment incomplete | YES | YES | YES daily, subdaily physiology available | implementation-friendly direct candidate |
| LandscapeDNDC / PSIM | YES | PARTIAL: ground vegetation + regeneration cohorts but cohort set fixed in key application | YES | YES alpine terrain | YES hourly | strongest hourly mountain precedent but autonomous succession incomplete |
| ELM-ParFlow-FATES | PARTIAL: actual terrain columns but FATES internal disturbance patches statistical | framework YES, hillslope case used tropical tree PFT mainly | YES | YES hillslope | YES half-hour/day | ecologically complete but heavy and explicit understory terrain precedent weak |
| Haga LANDIS-II NECN | YES, 10 m | YES, Sasa is real species-age biomass cohort with regeneration/resprout | YES | YES landscape/topographic raster | NO, monthly ecosystem process | excellent spatial/understory precedent, fails timestep criterion |
| 4C | NO native landscape x-y | PARTIAL generic grass ground vegetation + tree regeneration | YES | site/patch, not catchment | YES daily water, weekly photosynthesis | fails spatial criterion |
| BiomeE/BiomeEP | external tiling needed | YES | YES | weak native catchment precedent | YES subdaily/daily | ecology strong, spatial wrapper required |
| ED2 | geographic sites possible but internal patches statistical | YES/variant dependent | YES | catchment routing variants exist but generally coarse | YES subhourly | spatial interpretation weak for hillslope geomorph coupling |
| RHESSys | actual spatial hierarchy | NO strict age/size cohort demography | YES | YES | YES daily | excellent ecohydrology but fails strict cohort criterion |
| tRIBS+VEGGIE | actual terrain/TIN but PFT-average, not cohort | PARTIAL dynamic PFT fractions | YES | YES | YES hourly/minutes | strong non-cohort comparator |

## LPJ-DH key evidence
Tang et al. 2014:
- Stordalen catchment about 16 km2
- actual 50 m grid
- DEM-derived drainage area, flow direction and slope
- daily grid-cell water redistribution
- standard LPJ-GUESS age-cohort vegetation dynamics retained
- tree PFTs plus tall shrubs, low shrubs and C3 grass
- soil-water state represented relative to WHC
- runoff validated at six outlets
- monthly runoff adjusted R2 increased from about 0.43 in standard LPJ-GUESS to about 0.87 in LPJ-DH

Tang et al. 2015 follow-ups:
- multiple-flow TFM routing evaluated
- LPJG-WHyMe-TFM used for long-term 50 m catchment carbon budget
- birch densification and encroachment into tundra heath simulated to 2080

Critical weaknesses:
- old branch is not presently identified as a public maintained repository
- lateral hydrology is simpler than modern ParFlow and was primarily surface-flow routing
- old soil profile is less flexible than LPJ-GUESS-RE
- process timestep is daily, not hourly

## PF-LPJG 2026 key evidence
- published GMD 2026 and code archived on Zenodo
- LPJ-GUESS age-based cohorts with establishment, competition and mortality
- ParFlow 3D Richards + overland flow + groundwater
- ParFlow hourly, LPJ-GUESS daily exchange
- actual basin-scale topographic hydrology
- soil moisture from ParFlow overwrites LPJ-GUESS state daily

Critical weakness for Gounsa:
- published Danube experiment is 10 km, not a fine hillslope validation
- explicit shrub/herb understory configuration was not documented as a central feature of the Danube application

## Modern LPJ soil-depth option
LPJ-GUESS-RE v1.0 (2025):
- 15-layer Richards soil hydrology
- user-defined layer thicknesses and therefore variable total soil depth
- bedrock, aquifer and free-drainage bottom boundaries
- public code on Zenodo
- no native lateral x-y flow

Combining LPJ-GUESS-RE with LPJ-DH routing or PF-LPJG fine-grid setup would be a **새로운 coupling** unless an existing published implementation is identified.

## Current research direction
Do not choose a final model yet. Next priority is to test whether a modern LPJ-GUESS spatial-hydrology branch can be made fine enough for Gounsa without rebuilding the entire model:
1. inspect PF-LPJG open code for grid-size assumptions and restart/state exchange,
2. inspect LPJ-GUESS-RE public code for dynamic/custom soil depth and root-layer state,
3. determine whether explicit Korean tree/shrub/herb PFT or species parameterization is feasible,
4. compare computational cost against MEDFATE/medfateland at 10, 25 and 50 m,
5. keep LandscapeDNDC as the hourly mountain benchmark.

## Decision
The search no longer treats LANDIS-II or generic forest landscape models as the default target. The current strongest structural lineage is:

```
actual geographic catchment grid
+ LPJ-GUESS age cohorts and herbaceous understory
+ daily or subdaily physiology
+ terrain-driven lateral hydrology
+ explicit soil water / variable soil-depth capable soil module
```

LPJ-DH is the strongest published fine-resolution precedent; PF-LPJG is the strongest modern open hydrological coupling; MEDFATE remains the easiest direct spatial implementation candidate.
