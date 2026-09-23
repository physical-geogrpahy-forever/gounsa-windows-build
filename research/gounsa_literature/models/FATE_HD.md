# FATE-HD

## 왜 검토했는가
고운사의 criterion 2인 `하층 초본/관목/교목 천이를 매우 명시적으로 고려`하는 모델 중 공간명시성과 산악 적용까지 강한 후보를 찾기 위해 검토했다.

## 식생 구조
- spatially and temporally explicit dynamic vegetation model
- regular geographic grid, typically 100 m in Ecrins applications
- 24 plant functional groups in key Alpine implementation
  - 10 herbaceous PFGs
  - 6 shrub/chamaephyte PFGs
  - 8 tree PFGs
- PFG population age structure
- five vertical height strata
- seed production, seed bank/dispersal, germination, recruitment, mortality
- shade competition and disturbance response

## 산악/지형 선례
Very strong.
- Écrins National Park, French Alps
- elevation about 669-4102 m
- 100 m mapped landscape
- forest-grassland ecotone
- grazing/mowing/drought/climate scenarios

## 하층 천이
**VERY STRONG.**
초본, 관목, 교목을 별도 PFG로 두고 demographic processes와 seed dispersal로 실제 landscape succession을 계산한다.

criterion 2만 보면 현재 검토한 모델 중 가장 명시적인 사례 중 하나다.

## 토양/수문
약점.
Abiotic filtering/habitat suitability and later drought modules affect demographic rates, but the base architecture is not a mechanistic subdaily soil-water/groundwater land-surface model comparable to ParFlow-FATES, MEDFATE, LPJ-GUESS-RE.

## 시간해상도
**FAIL for current criterion 5.**
FATE-HD vegetation dynamics runs at annual timesteps.

Drought/extreme-event extensions alter annual demographic response but do not turn the core model into a daily/hourly ecohydrology model.

## 5조건
| 기준 | 판정 |
|---|---|
| 1 spatial cohort | YES/STRONG: geographic grid + age-structured PFG populations |
| 2 understory succession | VERY STRONG |
| 3 soil/geomorph coupling | WEAK-PARTIAL |
| 4 watershed/topography | STRONG mountain terrain/landscape, but not process hydrology catchment |
| 5 <=daily | NO: annual |

## 현재 역할
**주 엔진 후보에서는 탈락, understory/succession architecture benchmark로 채택.**

고운사에서 향후 초본-관목-교목 succession module을 별도 설계해야 할 경우 FATE-HD가 어떤 demographic states를 명시해야 하는지 매우 좋은 참고가 된다.

## key references
- Boulangeat, I., Georges, D., & Thuiller, W. (2014). FATE-HD: A spatially and temporally explicit integrated model for predicting vegetation structure and diversity at regional scale. Global Change Biology / Methods in Ecology lineage.
- Boulangeat et al. (2014), Ecography, climate and land-use application in Écrins National Park.
- Barros et al. (2017), Journal of Applied Ecology, drought/extreme climate extension.
