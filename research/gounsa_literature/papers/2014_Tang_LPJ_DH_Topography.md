# Tang et al. (2014) LPJ-DH topographic hydrology

## 서지정보
Tang, J., Pilesjö, P., Miller, P. A., Persson, A., Yang, Z., Hanna, E., & Callaghan, T. V. (2014). Incorporating topographic indices into dynamic ecosystem modelling using LPJ-GUESS. *Ecohydrology*, 7(4), 1147–1162. https://doi.org/10.1002/eco.1446

## 이 논문을 검색한 이유
LPJ-GUESS 같은 cohort vegetation model이 단순 독립 grid가 아니라 실제 DEM 기반 유역에서 lateral water redistribution을 받으며 세밀한 공간해상도로 운용된 선례가 있는지 확인하기 위해 검토했다.

## 연구 유형
Dynamic ecosystem model extension + distributed hydrology + catchment evaluation.

## 공간구조
- LPJ-GUESS ecology embedded in geographic grid
- actual 50 m grid in Stordalen catchment, northern Sweden
- topographic indices extracted from DEM
- surface routing and lateral water flux between grid cells
- within-grid LPJ-GUESS stand/patch/cohort structure itself remains statistical rather than mapped x-y individual cohorts

## 적용환경
고위도 북부 스웨덴 Stordalen catchment. Birch treeline, tundra/low vegetation and catchment runoff were evaluated.

## 핵심과정
- LPJ-GUESS vegetation growth and competition
- soil-water balance
- DEM-derived drainage/topographic indices
- surface water routing
- lateral water redistribution among cells
- vegetation biomass and carbon-flux response to redistributed water

## 식생입력
LPJ-GUESS plant functional types and cohort/individual-mode vegetation architecture. The application examined birch treeline/biomass and low vegetation in a heterogeneous catchment.

## 핵심식/알고리즘
The study adds topographic routing and inter-cell lateral water fluxes to standard LPJ-GUESS. Exact routing equations should be taken from the paper if implementation is reproduced; the key conceptual addition is:

```text
local vertical water balance
+ DEM/topographic-index controlled lateral redistribution
-> updated grid-cell water availability
-> LPJ-GUESS vegetation response
```

## 파라미터와 단위
Key spatial/validation quantities:
- grid resolution: 50 m
- runoff evaluation: six catchment outlet points
- evaluation period: 2007–2009
- monthly runoff adjusted R2: LPJ-DH ~0.8713 vs standard LPJ-GUESS ~0.4277

## 고운사에 사용할 수 있는 부분
1. cohort/DGVM ecology를 실제 fine catchment grid에 배치할 수 있다는 published precedent
2. DEM-derived water redistribution이 vegetation biomass와 treeline을 바꿀 수 있음을 보여줌
3. 고운사에서 `geomorph/topography -> lateral water -> vegetation` 연결의 가장 직접적인 고해상도 선례 중 하나
4. vegetation grid를 geomorph grid보다 굵게 두고 지형·수문 정보를 전달하는 구조의 근거

## 필요한 새로운 coupling
- storm-driven DEM/soil-depth update
- erosion/deposition layer remapping
- potentially modern LPJ-GUESS soil hydrology or ParFlow-type subsurface module
- Korean postfire PFT/species parameterization

These are **새로운 coupling** unless another published implementation is found.

## 한계
1. LPJ-DH is a legacy branch and current maintained public implementation is not clearly established.
2. Lateral hydrology is simpler than modern 3-D Richards/groundwater models.
3. Within-cell demographic patches are not geographic subpixels.
4. Physiology/ecohydrology is daily rather than hourly.
5. Fine-scale explicit herb species succession is not demonstrated at MEDFATE/FATE-HD detail.

## 최종 판정
**강하게 유지: strongest published fine-resolution catchment precedent for LPJ-GUESS lineage.**

Five criteria:
- spatial cohort/grid: YES at geographic cell level, internal patch space implicit
- understory succession: GOOD at PFT/cohort level
- soil/geomorph connectivity: STRONG
- watershed/topography: EXCELLENT
- <=daily: YES daily ecohydrology
