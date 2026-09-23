# PHOREAU v1.0

업데이트: 2026-09-23

## 현재 판정
**최신 tree ecohydraulics benchmark / strict production shortlist에서는 criterion 2와 공간수문 때문에 탈락.**

PHOREAU는 ForCEEPS forest dynamics + PHENOFIT phenology + SurEau plant hydraulics를 결합한 2025년 공개 process-based forest model이다.

강점은 일별/시간별 수목 생리, 다층 뿌리 수리학, 재생-생장-사망의 장기 forest dynamics를 같은 모델에 넣었다는 점이다.

그러나 독립적인 herb/shrub ground-layer demography 및 actual geographic hillslope/catchment lateral hydrology는 확인되지 않는다.

## vegetation structure
- individual-based forest gap model
- tree regeneration, growth, mortality
- explicit tree size and crowns
- competition for light and water
- species-specific hydraulic, allometric and phenological traits
- understory trees are represented as suppressed/short trees

For SurEau runtime reduction, individual trees can be aggregated by species and diameter/size class for hydraulic calculations, but PHOREAU forest demography itself remains individual-tree based.

## time structure
- hourly plant hydraulics / root-soil conductance-related calculations
- daily phenology/water-balance processes
- daily canopy/rainfall water accounting
- yearly demographic growth/regeneration/mortality integration

This is strong for rapid drought/storm physiological response, though structural demography remains slower.

## roots / soil
PHOREAU explicitly segments soil into layers.

For each tree or hydraulic aggregate:
- rooting depth determines accessible soil layers
- fine-root area is distributed among layers using a species-specific negative-exponential profile
- fine-root area in each layer determines soil-to-root conductance
- soil water potential and plant hydraulics control water uptake and drought stress

This is one of the strongest recent tree-root hydraulic formulations among forest dynamics models.

## forest-floor / shrub / herb
Important distinction:
- `understory` in PHOREAU literature primarily means smaller/shorter trees or understory tree species.
- no native demographic grass/herb layer was identified.
- no native independent shrub-to-tree postfire succession layer was identified in the standard v1.0 description.

Therefore criterion 2 is weak for Gounsa despite sophisticated vertical tree-canopy ecology.

## spatiality
PHOREAU preserves a gap/stand representation and improves canopy/light competition, but does not assign explicit x-y coordinates to every tree in the way PICUS, SORTIE or TROLL do.

Fine geographic raster linkage, seed dispersal among terrain cells and lateral hillslope hydrology are not native core features identified in this audit.

## hydrology
- daily rainfall interception / throughfall
- layered soil water
- hourly tree hydraulics
- drought/cavitation processes

But no published ParFlow-class or medfateland-class connected hillslope coupling was identified.

## Gounsa 5 criteria
| criterion | verdict |
|---|---|
| 1 spatial cohort/hybrid | PARTIAL: individual gap model, no actual fine GIS landscape topology |
| 2 explicit herb/shrub/tree understory succession | WEAK |
| 3 soil/root coupling | VERY STRONG local tree hydraulics |
| 4 hillslope/catchment precedent | WEAK-PARTIAL |
| 5 <=daily | VERY STRONG physiology, slower demography |

## 고운사 역할
PHOREAU is highly useful as a reference for:
- translating layer soil-water potential to tree physiological stress
- species-specific rooting depth and fine-root vertical distribution
- hourly soil-root-tree hydraulic conductance
- rapid drought response and mortality mechanisms

It does not replace FATES, JULES-RED, MEDFATE or LPJ-GUESS for full herb/shrub/tree postfire succession.

## code availability
Standalone PHOREAU v1.0 is publicly archived on Zenodo and the model is implemented in the Capsis platform.

## key reference
Postic, T., et al. (2025). PHOREAU v1.0: a new process-based model to predict forest functioning, from tree ecophysiology to forest dynamics and biogeography. Geoscientific Model Development, 18, 7603–7679. https://doi.org/10.5194/gmd-18-7603-2025
Model archive: https://doi.org/10.5281/zenodo.15260689
