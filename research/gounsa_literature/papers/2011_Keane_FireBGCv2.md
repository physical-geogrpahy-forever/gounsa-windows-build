# Keane et al. (2011) FireBGCv2

## 서지정보
Keane, R. E., Loehman, R. A., & Holsinger, L. M. (2011). *The FireBGCv2 landscape fire and succession model: a research simulation platform for exploring fire and vegetation dynamics*. USDA Forest Service, Rocky Mountain Research Station, General Technical Report RMRS-GTR-255. https://doi.org/10.2737/RMRS-GTR-255

## 이 문헌을 검색한 이유
고운사 식생모델 후보를 `공간명시 + 하층식생/천이 + 토양-지형 결합 가능 + 유역/지형 선례 + 일 이하 과정`의 다섯 조건으로 다시 검색하면서, FireBGCv2가 산불모델을 넘어 하층식생, 일별 물·탄소, 실제 산악 경관을 함께 모의하는지 확인하기 위해 검토했다.

## 연구 유형
모델 기술 보고서 / 알고리즘 문서 / landscape fire-succession model documentation.

## 공간구조
- landscape -> site -> stand -> tree / undergrowth guild hierarchy
- mapped stands/polygons and raster spatial layers
- tree stratum: individual tree
- non-tree undergrowth: species/guild biomass compartments
- sites defined by biophysical setting including elevation, slope, aspect, soil

## 적용환경
주요 개발·검증 환경은 미국 북부 Rocky Mountains와 Glacier National Park 계열 산악 산림경관이다. 문서와 관련 선행 적용에서 McDonald Drainage 같은 실제 유역이 사용되었다.

## 핵심과정
- daily weather and phenology
- daily photosynthesis, respiration, evapotranspiration and soil-water balance
- annual tree carbon allocation, growth realization and demographic updates
- seed production/dispersal
- tree regeneration and mortality
- undergrowth guild biomass dynamics
- litter, duff, coarse woody debris and soil C/N
- fire ignition, spread, severity and mortality
- surface/subsurface runoff generation and catchment routing

## 식생입력
### 수목
개별 tree state including species, DBH, height, age and associated physiological parameters.

### 하층식생
각 site의 plant model에 여러 guild를 정의한다.
- herbaceous guilds
- shrub guilds
- 필요하면 개별 비수목 종을 guild처럼 정의 가능
- guild별 biomass, height, leaf-area and ecophysiological controls

개발문서는 4–20 undergrowth guild가 실용적이라고 제안하며 최대 100 guild 입력을 허용한다고 설명한다.

## 핵심식
하층 guild 생장은 전년도 biomass와 최대 biomass에 의해 제한되는 deterministic logistic-type growth에 shade reduction을 곱하는 구조이다. 문서의 대표식은 개념적으로:

```math
UGROWTH \propto r_{SHADE}\,n\,B_{t-1}\left(1-\frac{B_{t-1}}{B_{max}}\right)
```

where:
- `UGROWTH`: undergrowth biomass growth
- `rSHADE`: shade reduction factor
- `n`: annual guild growth constant
- `B`: undergrowth biomass, kg biomass m^-2

수문에서 soil water는 일별 precipitation input, ET/evaporation loss, field-capacity exceedance runoff로 갱신된다. 토양 hydraulic conductivity는 문서에서 soil clay percentage의 함수로 parameterized되고, excess water는 surface/subsurface runoff로 분배된다.

## 파라미터와 단위
대표 state/input:
- elevation: m
- slope: percent
- aspect: degrees azimuth
- soil water: kg water m^-2
- litter/duff/downed woody biomass: kg m^-2
- undergrowth guild biomass: kg m^-2
- daily runoff / water fluxes: kg water day^-1 or area-normalized equivalents depending module
- undergrowth growth constant: year^-1

## 고운사에 사용할 수 있는 부분
1. postfire herb/shrub biomass를 명시적인 상태변수로 보유
2. 하층식생이 tree regeneration, light, water and fire에 직접 영향
3. litter/duff/CWD를 따로 추적하여 postfire ground cover와 fuel/litter coupling에 유리
4. daily soil-water and ET response
5. real mountain landscape and catchment precedent
6. vegetation amount를 Gounsa erosion/root-disturbance equations에 전달 가능

## 토양-지형모델 coupling 평가
### 장점
- soil water is explicit daily state
- elevation/slope/aspect/soil define spatial site condition
- catchment routing exists

### 문제
FireBGCv2 native stand hydrology assumes no stand-to-stand soil-water exchange. Generated runoff is routed after local water-balance calculation and does not constitute bidirectional lateral soil-moisture redistribution.

Therefore:
- external soil-water overwrite: technically conceivable but custom source/state interface needed
- dynamic soil-depth/layer change: not native
- geomorphic erosion/deposition remapping: **새로운 coupling**

## 한계
1. individual-tree woody layer increases computation and parameter burden
2. undergrowth demographic cycle is less explicit than tree demography; guild biomass dynamics are not a complete seed-bank/age-cohort system
3. major structural changes are annual even though physiology/hydrology is daily
4. model is complex and developer documentation itself warns of substantial training burden
5. soil-water routing is not a modern fully coupled lateral groundwater scheme

## 최종 판정
**유지: serious secondary candidate / mountain-fire benchmark.**

Five criteria:
- spatial: YES
- understory succession: STRONG-PARTIAL
- soil/geomorph connectivity: MODERATE
- watershed/topography precedent: STRONG
- <=daily response: YES for physiology/hydrology; annual structural update

MEDFATE보다 외부 상태결합과 구현성이 불리하지만, 실제 산악 경관 + herb/shrub undergrowth + fire succession + daily ecohydrology의 조합 때문에 반드시 비교군으로 유지할 가치가 있다.
