# WoodS / LandS model lineage

업데이트: 2026-09-23

# 왜 이 계열을 검토했는가
고운사 vegetation engine 검색에서 반복적으로 나타난 trade-off는 다음과 같다.

- 실제 raster를 쓰는 forest landscape model은 초본/관목을 단순화하는 경우가 많음
- explicit herb/shrub/tree succession model은 annual timestep이 많음
- daily ecohydrology model은 demographic understory가 약함

WoodS는 이 중 `spatial raster + explicit herb/shrub/tree interaction + daily iteration`을 동시에 갖는 드문 사례이므로 신규 후보로 검토했다. 2023년 LandS는 이 계열의 최신 후속 모델이다.

# 계보

```text
GraS Model
  -> WoodS Model (2014)
       herbaceous compartment model
       + individual bushes/trees
       + spatial raster
  -> LandS Model (2023)
       expanded environmental EIVs
       + flexible site/species initialization
       + inherited optional woody module
```

# WoodS 2014

## 공간구조
- spatially explicit raster landscape
- 실제 application에서 약 1,500 ha, 150,000 cells
- 대략 10 x 10 m cell
- herbaceous species는 cell-level population/cover
- bushes and trees는 individual agents

## succession biology
WoodS가 중요한 이유는 단순 cover correction이 아니라 서로 다른 life-form의 천이 상호작용을 직접 계산한다는 점이다.

- herbaceous cover growth
- herb layer inhibits woody seed access/germination
- tree/bush germination
- individual growth
- seed production and dispersal
- mortality
- browsing
- self-thinning
- woody expansion reduces area available to herbs

따라서 초기 `herb -> shrub -> tree` 전이의 공간적 메커니즘은 상당히 명시적이다.

## 시간해상도
- processes are iterated in daily increments
- 100-year runs demonstrated

그러나 이것을 mechanistic daily ecophysiology와 혼동하면 안 된다.

- no daily meteorological forcing
- no seasonal plant physiology
- landscape development interpreted/updated on annual scale
- space acts as a proxy for light, nutrients and water

# LandS 2023

LandS는 GraS/WoodS 계열을 현재화한 후속 모델이다.

## 추가된 환경축
Ellenberg-style indicator values:
- light
- moisture
- temperature
- soil reaction/pH
- nitrogen
- cutting
- grazing
- trampling

site EIV는 soil maps, DTM, observations and expert knowledge에서 구성할 수 있다.

## timestep
- one-day or one-week internal timestep selectable
- spread and growth scheduling occurs within the year

## 중요한 제한
- current publication/tests are herbaceous-focused
- woody module is optional/inherited
- moisture is an ecological indicator, not volumetric soil water or matric potential
- no published root-zone hydraulic model
- no published external soil-state overwrite
- paper provides executable/user guide/input files but explicitly states no permission to share source code

# strict five-criteria assessment

| criterion | WoodS | LandS current | Gounsa implication |
|---|---|---|---|
| 1 spatial cohort/hybrid | **STRONG-PARTIAL**: real raster + woody individuals + herb populations | PARTIAL/STRONG spatial raster, optional woody | spatial architecture useful |
| 2 explicit understory succession | **STRONG** | STRONG herb / woody current test partial | biological benchmark |
| 3 external soil/terrain state coupling | **FAIL** | FAIL/PARTIAL static EIV maps only | major blocker |
| 4 terrain/catchment precedent | PARTIAL landscape GIS, no routed hydro | PARTIAL DTM/site maps | not a watershed engine |
| 5 <=daily | PARTIAL: daily iteration but not daily meteorological physiology | daily/week scheduling | weaker than FATES/LPJ/MEDFATE physiology |

# 비교: 왜 top tier를 대체하지 않는가

## vs MEDFATE + medfateland
WoodS/LandS가 우세:
- herb layer recruitment/inhibition logic가 더 직접적
- very simple early-succession representation

MEDFATE가 우세:
- mechanistic daily water and carbon balance
- root depth and layered soil water
- direct `lateralFlows`, `waterTableDepth`
- external soil-domain option
- open R package ecosystem and editable state objects
- connected watershed hydrology

따라서 `MEDFATE + WoodS-like herb recruitment logic`가 WoodS 자체를 hydrology engine으로 개조하는 것보다 현실적인 development route다.

## vs LPJ-GUESS SEC + external hydro
WoodS/LandS가 우세:
- literal raster occupation and explicit herb inhibition is intuitive

LPJ-GUESS가 우세:
- daily mechanistic ecophysiology
- PFT water competition
- cohort forest dynamics
- published 50 m catchment branch
- ParFlow coupling precedent
- more mature C/N/root representation

## vs FATES
WoodS/LandS가 우세:
- internal space is literal x-y raster, not statistical disturbance patches
- initial herb-to-woody succession rules are computationally simple

FATES가 우세:
- full demographic tree/shrub/grass PFTs
- seed-bank/recruitment processes
- half-hourly host biophysics and daily demography
- 3-D hillslope hydrology coupling already published
- roots/litter/C pools available for geomorphic coupling

# 실제 고운사 활용 가치
WoodS/LandS를 production vegetation engine으로 채택하는 것보다 다음 세 가지를 가져오는 편이 타당하다.

1. **초본 억제형 woody recruitment**
   - postfire herb biomass/litter가 woody seed arrival or establishment probability를 억제
2. **저비용 hybrid spatial representation**
   - herb species/PFT는 cell-level cover/biomass
   - woody vegetation은 cohort 또는 simplified individual/super-individual
3. **초기 0–20 yr succession benchmark**
   - top-tier model의 초기 herb/shrub/tree trajectory가 비현실적이지 않은지 구조 비교

# external geomorphology coupling에 필요한 새 개발
WoodS/LandS에서 직접 고운사 생산모델을 만들 경우 최소 다음이 필요하다.

```text
external hydrology/geomorphology
 -> layer soil water / potential
 -> active soil depth
 -> root exposure/burial
 -> slope/aspect/microclimate
 -> vegetation water stress
 -> herb/woody growth and recruitment
```

하지만 이 interface는 published WoodS/LandS에 없다.
또한 source availability가 제한되어 있어 직접 확장 자체가 불리하다.

# 최종 판정
**production shortlist 승격 안 함.**

역할:
- spatial early-succession benchmark
- herb/shrub/tree interaction design reference
- MEDFATE herb recruitment extension에 특히 유용

다시 broad-search하지 않는다. 다음 중 하나가 새로 확인될 때만 재검토한다.
- source release
- mechanistic soil-water module
- external hydrology state interface
- forest application with simultaneous modern LandS herb + woody module

# 관련 문헌
- `papers/2014_Hudjetz_WoodS.md`
- `papers/2023_Rumohr_LandS.md`
