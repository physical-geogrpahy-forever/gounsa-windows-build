# FORHYCS v1.0 / TreeMig + PREVAH

업데이트: 2026-09-23

## 왜 검토했는가
고운사 조건과 이름 및 목적이 직접적으로 겹치는 `spatially distributed model combining hydrology and forest dynamics` 계열이므로 재검토했다.

## 구조
FORHYCS는 두 기존 모델을 양방향으로 결합한다.
- TreeMig: 공간명시 forest landscape model
- PREVAH: fully distributed hydrological model

TreeMig는 각 격자에서 종별, 수고계급별 수목 수를 계산하고 establishment, growth, mortality, seed dispersal을 모의한다.
PREVAH는 각 격자의 증발산, 토양수분, runoff generation을 subdaily 내부 timestep으로 계산하고 유출을 routing한다.

## 공간
- regular geographic grid
- parent models intended for 약 100 m–1 km cell size
- Swiss Central Alps Navizence catchment의 5개 subcatchment, 약 27–87 km2에 적용
- published evaluation examples used 200 m x 200 m model cells
- elevation, aspect, land cover와 catchment routing이 실제 공간에 연결됨

## 시간구조
- PREVAH internal hydrology: 1 h
- hydrological output/exchange: daily
- TreeMig forest dynamics: annual

핵심 coupling:
```text
TreeMig previous-year forest structure
 -> daily canopy/LAI/root-zone properties
 -> PREVAH hourly/daily hydrology
 -> annual transpiration-derived drought index
 -> TreeMig annual growth/mortality/establishment
```

따라서 폭우 뒤 수문 상태가 즉시 forest demography에 들어가는 구조는 아니다.

## 식생
TreeMig:
- tree species
- height/size classes
- establishment
- growth
- mortality
- migration/seed dispersal
- canopy light competition

이는 woody forest succession에는 강하다.

그러나 understory는 독립적인 herb/shrub demographic community라기보다 수문 모듈에서 overstory와 understory의 effective rooting depth와 storage capacity를 분리해 표현하는 수준이다. 독립적인 초본/관목 recruitment-growth-mortality succession engine은 확인되지 않았다.

## 토양/뿌리
- soil depth와 water holding capacity로 rooting-zone storage capacity 계산 가능
- overstory와 understory의 effective rooting depth를 별도 최적화
- rooting depth가 기후와 potential transpiration에 따라 동적으로 변할 수 있음

이는 root-zone hydrology 선례로는 흥미롭지만, 토층별 root biomass/RLD 또는 침식 후 root exposure remapping 구조는 아니다.

## 고운사 5조건
| 기준 | 판정 | 이유 |
|---|---|---|
| 1 spatial cohort/hybrid | STRONG-PARTIAL | 실제 지리격자 + species-height classes, 개별목보다 가벼움 |
| 2 explicit understory succession | WEAK | woody succession은 강하지만 herb/shrub understory demography 없음 |
| 3 soil/root coupling | MODERATE-STRONG | dynamic effective root-zone storage, soil depth/WHC 반영. layer root state는 약함 |
| 4 catchment/topography | VERY STRONG | 실제 Alpine catchment + distributed PREVAH + routing |
| 5 <=daily response | HYDRO STRONG / DEMOGRAPHY FAIL | hydro 1 h, tree response annual through drought index |

## 고운사 판정
**유역-산림 coupling 선례로 매우 가치가 크지만 production vegetation engine에서는 탈락.**

특히 고운사에서 피해야 할 coupling architecture를 명확히 보여준다.
```text
storm hydrology
 -> annual drought index only
 -> annual forest response
```
보다
```text
storm/event soil state
 -> daily vegetation physiology/mortality state
```
가 필요하다.

따라서 FORHYCS는 criterion 4의 강한 benchmark이지만 FATES-ParFlow, PF-LPJG 또는 daily-state MEDFATE 구조를 대체하지 못한다.

## 핵심 문헌
Speich, M. J. R., Zappa, M., Scherstjanoi, M., Lischke, H. et al. (2020). FORests and HYdrology under Climate Change in Switzerland v1.0: a spatially distributed model combining hydrology and forest dynamics. Geoscientific Model Development, 13, 537–564. https://doi.org/10.5194/gmd-13-537-2020
