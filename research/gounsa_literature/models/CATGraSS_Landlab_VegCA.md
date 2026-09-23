# CATGraSS / Landlab VegCA

업데이트: 2026-09-23

## 현재 판정
**보조 후보 / 탈락에 가까운 비교모델.**

고운사 기준에서 공간성과 짧은 수문 시간간격은 매우 강하지만, 한 격자에 하나의 식생형만 존재하므로 상층 교목 아래 관목·초본이 공존하는 산림 하층구조를 표현할 수 없다.

## 계보
- Zhou, Istanbulluoglu & Vivoni (2013): CATGraSS
- Nudurupati et al. (2023): Landlab SoilMoisture + Vegetation + VegCA를 이용한 공간 식생 전이
- Landlab 현재 공개 Python component: `VegCA`

## 공간 구조
DEM raster의 각 cell은 다음 중 하나를 점유한다.
- grass
- shrub
- tree
- shrub seedling
- tree seedling
- bare soil

인접 cell로 seed dispersal/establishment가 일어나고, 누적 수분스트레스에 따라 정착·사망 확률이 변한다.

## 시간 구조
- rainfall: pulse/event
- soil moisture: subdaily, daily 또는 interstorm
- biomass/NPP: 수분상태에 반응
- PFT establishment/mortality CA: 주로 annual update

## 수문
Landlab `SoilMoisture`는 root-zone 평균 수분을 계산한다.
- 단일 soil-moisture layer
- ET
- bare-soil evaporation
- leakage
- rainfall pulse

Nudurupati et al. 계열에서는 upstream runon을 받을 수 있고, runoff를 downstream으로 routing할 수 있다.

## 식생 상태
CATGraSS 원 논문은 cell마다 다음을 추적한다.
- PFT
- age
- root-zone soil moisture
- live/dead aboveground biomass
- live/dead belowground biomass
- establishment
- mortality

## 지형
- DEM 사용
- slope/aspect에 따른 incoming shortwave radiation
- 이에 따른 PET와 soil-moisture stress의 공간차
- small basin application 존재

## 고운사 5조건
1. 공간명시 cohort/개체 구조: **PARTIAL**
   - 실제 2D vegetation cells이나 cohort/size-class 구조는 아님
2. 하층식생과 천이: **FAIL-PARTIAL**
   - grass/shrub/tree/seedling 전이는 매우 명시적
   - 그러나 한 cell에 한 PFT만 존재하므로 forest overstory + understory 공존 불가
3. 토심/WHC/root: **WEAK-PARTIAL**
   - root-zone soil water와 belowground biomass는 있음
   - native SoilMoisture는 single-layer depth-averaged
4. 지형/유역: **STRONG**
   - DEM, slope/aspect, basin application, Landlab routing 가능
5. <= daily: **STRONG for hydrology / annual for structural turnover**

## 고운사에서의 가치
- postfire bare → grass/shrub/tree mosaic의 공간전파 benchmark
- geomorphology와 vegetation CA를 같은 Landlab grid에서 연결하는 설계 참고
- 실제 rill/erosion Landlab components와 같은 framework에서 결합 가능

## 결정적 한계
고운사에서 필요한
```text
tree canopy
 + shrub understory
 + herb layer
```
가 한 지점에서 동시에 존재하지 않는다.

따라서 생산 식생모델로는 FATES, MEDFATE, LandscapeDNDC보다 아래에 둔다.

## 핵심 참고문헌
- Zhou, X., Istanbulluoglu, E., & Vivoni, E. R. (2013). Modeling the ecohydrological role of aspect-controlled radiation on tree-grass-shrub coexistence in a semiarid climate. Water Resources Research, 49(5), 2872–2895. https://doi.org/10.1002/wrcr.20259
- Nudurupati et al. (2023). On Transient Semi-Arid Ecosystem Dynamics Using Landlab: Vegetation Shifts, Topographic Refugia, and Response to Climate. Water Resources Research. https://doi.org/10.1029/2021WR031179
- Landlab `VegCA`, `SoilMoisture`, `Vegetation` documentation/source.
