# WoodS / LandS / DynaFORb new-candidate screen

Date: 2026-09-23

## 목적
기존 후보를 반복 검색하지 않고 repository에 없던 계열 중 `explicit herb/shrub/tree interaction + spatial representation + <=daily response` 조합을 확인했다.

이번 batch:
- WoodS 2014
- LandS 2023
- DynaFORb 2024
- Moustakas et al. 2009 savanna landscape model

## strict result

| lineage | 1 spatial hybrid | 2 understory succession | 3 external soil-state coupling | 4 terrain/catchment | 5 <=daily | verdict |
|---|---|---|---|---|---|---|
| WoodS | STRONG-PARTIAL: ~10 m raster + woody individuals + herb populations | STRONG | FAIL | PARTIAL landscape GIS | PARTIAL: daily iteration, no daily meteorological physiology | biological/spatial benchmark |
| LandS | PARTIAL/STRONG raster | STRONG herb, optional woody inherited | FAIL/PARTIAL: EIV moisture only | PARTIAL DTM/site maps | YES scheduling, weak physiology | benchmark |
| DynaFORb | WEAK-PARTIAL cover-based | STRONG-PARTIAL temperate herbs | FAIL: water/nutrient competition absent | FAIL | PARTIAL: daily internal, annual cover | understorey biology benchmark |
| Moustakas 2009 | STRONG-PARTIAL grid + woody individuals + grass biomass | STRONG life-form level | MODERATE local soil moisture | FAIL/PARTIAL | YES daily | savanna benchmark |

## 핵심 발견 1: WoodS
WoodS는 spatial raster에서 herbaceous population layer와 individual shrub/tree recruitment를 직접 상호작용시킨다. 약 1,500 ha, 150,000 cells, 100 yr를 daily increments로 모의한 선례가 있다.

초본은 woody seed arrival/germination을 억제하고 woody expansion은 herbaceous available area를 줄인다. 따라서 고운사 초기 0–20 yr succession의 저비용 hybrid representation benchmark로 매우 유용하다.

그러나 daily timestep을 mechanistic daily ecophysiology와 동일시하면 안 된다.
- daily meteorological forcing 없음
- seasonal variability 없음
- mechanistic soil-water balance 없음
- space가 light/nutrients/water의 proxy 역할

따라서 `storm -> soil/terrain state change -> vegetation response` coupling에는 직접 사용할 수 없다.

## 핵심 발견 2: LandS
LandS 2023은 WoodS/GraS의 후속계열이다.
- one-day or one-week scheduling
- light, moisture, temperature, pH, nitrogen EIV
- soil maps and DTM 기반 site maps 가능

하지만 moisture는 mechanistic soil-water state가 아니라 Ellenberg-style indicator다. Current tests는 herbaceous-focused이고 woody module은 inherited/optional이다. 논문은 executable과 inputs는 공개하지만 source code 공유 permission이 없다고 명시한다. 외부 hydrology coupler를 삽입해야 하는 고운사에는 큰 engineering disadvantage다.

## 핵심 발견 3: DynaFORb
DynaFORb는 2024 temperate forest understorey-specific model이다.
- grasses, herbs, ferns, dwarf shrubs, tree saplings
- species-specific traits
- daily phenology, light competition, photosynthesis and carbon-demand performance
- cover-based low-cost representation

하지만 current version은 water/nutrient competition이 없고 main cover state update는 yearly다. Production engine보다 MEDFATE herb extension 또는 LPJ/FATES understorey refinement용 biology reference가 적합하다.

## Moustakas 2009
Tree, bush, grass, soil depth, porosity, soil moisture를 spatial grid에서 daily update한다. `daily soil water -> tree/shrub/grass dynamics`의 단순한 선례다.

하지만 cell 약 3 km, savanna ecology, no seed dispersal, fixed soil geometry, no routed hillslope hydrology이므로 aDGVM2보다 아래 benchmark다.

## shortlist 영향
**변경 없음.**

Production top tier:
1. LPJ-GUESS SEC/PPA + PF-style external hydrology
2. ELM-ParFlow-FATES
3. MEDFATE + medfateland

Conditional/secondary:
4. aDGVM2 lineage
5. FORMIND-mHM

이번 신규계열의 가장 큰 가치는 모델 교체가 아니라 top-tier의 criterion-2 gap 보완 설계다. 특히 `MEDFATE + WoodS-like herb inhibition/recruitment logic`가 WoodS에 새 hydrology를 붙이는 것보다 현실적이다.

## 재검색 금지
WoodS/LandS는 source release, mechanistic soil-water module, external hydrology interface 또는 modern herb+woody simultaneous forest application이 나올 때만 재검토한다.

DynaFORb는 water/nutrient competition, daily recruitment/cover update, overstorey direct coupling 또는 landscape/catchment implementation이 나올 때만 재검토한다.

Moustakas lineage는 fine-terrain/catchment descendant 또는 temperate-forest adaptation이 확인될 때만 재검토한다.

## 관련 파일
- `models/WoodS_LandS.md`
- `models/DynaFORb.md`
- `papers/2014_Hudjetz_WoodS.md`
- `papers/2023_Rumohr_LandS.md`
- `papers/2024_Landuyt_DynaFORb.md`
- `papers/2009_Moustakas_SavannaPatchDynamics.md`
