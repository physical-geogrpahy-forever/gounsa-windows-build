# EDYS / TerreSIM lineage

업데이트: 2026-09-23

## 왜 검토했는가
고운사 vegetation-geomorph coupling 후보를 넓혀 찾는 과정에서, EDYS가 다음 조합을 이미 오래전에 구현한 계열임을 확인했다.

- 종별 식생동태
- grass / forb / shrub / tree 생활형
- seed bank, seedling, adult stage
- 일 단위 생장과 토양수분
- 실제 GIS 격자 landscape
- cell-to-cell surface runoff
- sediment / litter / N transport
- erosion/deposition에 따른 surface elevation change
- erosion/deposition에 따른 soil-layer thickness change
- fire and physical disturbance
- watershed application and hydrologic-model coupling

따라서 단순 옛 관리모델이 아니라 고운사 요구와 구조적으로 매우 가까운 ecogeomorphic ecosystem-model lineage로 재평가한다.

---

## 1. 모델 구조
EDYS = Ecological DYnamics Simulation model.

공간 계층:
```text
landscape grid
 -> community / plot type
 -> soil profile
 -> species populations
```

plot-level ecological processes는 매일 계산되고, 그 결과가 해당 plot type에 속한 실제 landscape cells에 적용된다.
그 다음 landscape-level runoff, erosion/deposition, fire 등 공간과정이 실제 격자에서 수행된다.

1999 CERL TR 99/55는 quadrat-community-landscape 계층을 명시하고, 1 m2 quadrat부터 watershed/landscape까지 확장하는 구조를 설명한다.

---

## 2. 식생 표현
EDYS는 종별 또는 composite species 단위로 식물을 표현한다.

확인된 growth forms:
- annual grass
- perennial grass
- annual forb
- perennial forb
- deciduous woody
- evergreen woody
- woody plants can be parameterized as shrub/tree types

species parameterization에는 다음 계열이 포함된다.
- growth form
- green-up timing
- seed production timing
- dieback timing
- growth rates
- root-to-shoot ratio
- water use
- N concentration
- canopy / bare-ground effects
- light-competition matrix
- seed sprouting properties
- root uptake capacities
- fire and herbivory response

### stage structure
EDYS는 적어도 다음 stage를 별도 상태로 둔다.
```text
seed bank
 -> germination / seedlings
 -> adult plant biomass
```

따라서 단순 cover-fraction 모델이 아니다.

그러나 woody vegetation을 DBH/age/height cohort로 세분하는 FATES/LPJ-GUESS/RED식 demographic cohort model도 아니다.
정확한 분류는:

**species-level stage-structured biomass population model**

이다.

---

## 3. postfire succession evidence
Mata-González et al. (2007)는 Yakima Training Center의 burned/unburned sagebrush-steppe에서 EDYS를 검증했다.

핵심 결과:
- 초기에는 annual Bromus tectorum이 우점
- 장기 모의에서 annuals가 약 13-15년 후 perennial species로 교체
- 주요 후속종은 Chrysothamnus nauseosus, Artemisia tridentata, Agropyron cristatum
- fire는 B. tectorum의 우점 지속기간을 연장
- 50년 plant-production succession을 모의

즉 EDYS는 실제로 fire 이후 annual herb -> perennial herb/shrub replacement를 내생적인 종별 성장/경쟁 구조로 모의한 published precedent가 있다.

이는 고운사의 산불 후 초기 천이에 매우 직접적이다.

---

## 4. 토양과 뿌리
EDYS soil profile은 여러 토양층으로 구성된다.

layer별 상태:
- thickness
- water content
- saturation / field capacity / wilting level
- N and other nutrients
- organic matter
- salinity
- contaminants

soil water와 plant water uptake는 일별로 변한다.

Plant parameter/state에는 root-to-shoot ratio와 root uptake capacity가 있으며, EDYS 응용문서에서는 root architecture와 soil water depth의 관계가 plant water uptake를 결정한다고 설명한다.

고운사 관점에서 중요한 점:
- 토양깊이와 WHC가 layer state로 명시적
- 식물수분흡수와 토층수분이 직접 연결
- 토양층 자체의 두께가 erosion/deposition에 의해 동적으로 변함

---

## 5. erosion/deposition이 실제 soil depth를 바꿈
Goliad County EDYS report의 명시적 설명:

- 평상시 soil-layer thickness는 일정
- deposition 발생 시 top layer thickness 증가
- erosion 발생 시 top layer thickness 감소
- top layer가 완전히 제거되면 다음 soil layer를 계속 침식

즉 EDYS는 고운사에서 다른 vegetation models에 새로 붙이려던

```text
erosion/deposition
 -> dynamic soil depth
 -> layer geometry change
```

를 native process로 이미 갖는다.

이 점은 현재 조사된 vegetation-dynamics 후보 중 매우 드물다.

---

## 6. actual spatial landscape and runoff
EDYS User Guide는 실제 landscape를 multiple grids로 표현한다.
최소 grid:
- vegetation / plot-type grid
- elevation grid
- management-unit grid

plot-level process가 각 cell의 runoff amount를 결정한 뒤, landscape runoff procedure가 실제 격자를 따라 물과 물질을 이동시킨다.

1999 source/pseudocode에는 runoff procedure가 다음을 수행한다고 설명된다.
- grid scan
- water/material movement by rows/cells
- sediment/litter carrying capacity
- sediment/litter mobilization and deposition
- erosion losses reflected in soil profiles

응용보고서는 elevation difference를 이용하여 slope/aspect와 downslope flow를 계산한다고 설명한다.

따라서 EDYS spatiality는 FATES/ED2처럼 statistical patch만 있는 형태가 아니라 **actual geographic raster-cell landscape**이다.

---

## 7. geomorphic feedback
중요한 coupling chain:

```text
vegetation / bare ground / soil state
 -> daily infiltration and runoff generation
 -> cell-to-cell runoff
 -> sediment erosion / deposition
 -> soil-layer thickness change
 -> elevation/topographic state change
 -> next event flow path / soil-water state
 -> plant water/nutrient competition
```

고운사에서 원하는 vegetation-geomorph feedback과 구조적으로 매우 가깝다.

다만 현재 확인해야 할 세부사항:
- erosion으로 soil layer가 잘릴 때 root biomass가 정확히 어떻게 삭제/remap되는가
- deposition으로 root burial이 생장/사망에 직접 연결되는가
- rill/channel incision을 어떤 수준까지 해석하는가

---

## 8. hydrologic coupling precedent
EDYS는 자체 hydrology 외에도 외부 hydrologic models와 연결된 계보가 있다.

보고된 coupling/links:
- MODFLOW
- GSSHA
- CASC2D
- HSPF

1999 CERL report에는 EDYS-CASC2D-WMS linkage가 명시되어 있다.
2009 Honey Creek report는 EDYS가 groundwater 및 surface-runoff models와 결합되어 integrated watershed management simulation system으로 사용되었다고 정리한다.

따라서 외부 고해상도 hydrology engine을 붙이는 것 자체도 precedent가 있다.

---

## 9. time structure
EDYS는 기본적으로 **daily dynamic model**이다.

- plant growth / uptake / soil nutrient-water processes: daily
- landscape runoff/erosion: precipitation-event / daily process chain
- long-term simulation: months to centuries

따라서 criterion 5의 최소 요구 `<= 1 day`는 충족한다.

완전 hourly plant physiology는 아니다.
고운사에서 6-hour storm geomorphology를 별도 시간단위로 계산하고 하루 종료 시 vegetation state를 갱신하는 architecture와 잘 맞는다.

---

## 10. actual watershed precedent
McLendon et al. (2009): Honey Creek Watershed, Texas.

- EDYS and EDYS-L comparison
- vegetation and hydrological dynamics
- EDYS described as mechanistic and spatially explicit
- scale from <=1 m2 to landscape/watershed
- daily dynamics over months to centuries

Gonzales County 및 여러 Texas watershed applications에서도 DEM, groundwater depth, vegetation and soil grids를 사용했다.

---

## 11. software/code availability
여기가 가장 큰 위험이다.

1999 implementation:
- Turbo Pascal 7
- PC standalone architecture
- report contains module listing and pseudocode/data structures

현재 2026:
- ERDC fact sheet remains online
- Texas Tech Cade Coldren profile states continued use of EDYS over roughly two decades
- Texas agency still hosts EDYS user guides and application reports

그러나:
- modern public source repository는 확인되지 않음
- distribution model은 executable/request 기반 계보로 보임
- maintainable modern source availability가 불확실

따라서 scientific fit은 매우 높지만 software-risk도 매우 높다.

---

## 12. TerreSIM lineage
TerreSIM은 EDYS의 successor/next-generation 계열로 개발되었다.

확인되는 확장:
- mechanistic spatial terrestrial ecosystem simulation
- soil/water/plant/animal/landscape components
- surface and subsurface movement
- sediment / nutrient / contaminant transport
- species-level plant module
- spatial module capable of explicit plant/tree positions when desired

그러나:
- ©2003 MFG Inc. proprietary lineage
- modern public source not identified
- 개별식물 공간표현까지 가면 고운사의 desired cohort middle-ground보다 복잡할 수 있음

따라서 TerreSIM 자체보다는 EDYS의 공개 알고리즘 구조가 현재 연구설계 참고에 더 유용하다.

---

## 13. 고운사 5조건 평가
| 기준 | 판정 | 근거 |
|---|---|---|
| 1. 공간명시 cohort/hybrid | **STRONG spatial / PARTIAL cohort** | actual raster cells and plot types, species/stage populations; woody DBH-age cohorts는 없음 |
| 2. explicit understory + succession | **VERY STRONG** | grass, forb, shrub, tree species; seed bank/seedling/adult; published postfire annual->perennial shrub/herb succession |
| 3. soil depth / WHC / geomorph coupling | **VERY STRONG** | multilayer soil, water state, erosion/deposition directly changes layer thickness |
| 4. watershed / topography | **VERY STRONG** | DEM grid, cell runoff, sediment transport, watershed applications, MODFLOW/GSSHA/CASC2D/HSPF links |
| 5. <= daily | **STRONG** | daily ecological dynamics and event/daily runoff chain |

---

## 14. 현재 판정
**Scientific top-tier / software-risk top-tier.**

EDYS는 지금까지 조사한 후보 중 고운사 ecogeomorphic architecture와 가장 직접적으로 닮은 모델 중 하나다.

특히 다른 top candidates와 비교하면:

### EDYS가 더 강한 점
- actual geographic cells
- native cell-to-cell runoff
- native sediment transport
- native erosion/deposition soil-depth change
- explicit herb/forb/shrub/tree species competition
- demonstrated postfire succession
- daily operation

### EDYS가 약한 점
- woody DBH/age cohorts 없음
- canopy vertical structure/light competition은 SEC/FATES보다 단순
- modern plant hydraulics는 약함
- public modern source code 부재
- Turbo Pascal legacy
- Korean temperate parameterization 필요

따라서 두 가지 전략이 가능하다.

```text
A. EDYS를 직접 확보/포팅
 -> 가장 통합적인 구조
 -> software access/maintenance risk 큼

B. EDYS architecture를 설계 benchmark로 사용
 -> modern vegetation cohort model + geomorph engine에
    EDYS식 daily landscape coupling을 재구현
```

현재로서는 B가 더 현실적이지만, source/executable 확보 가능성을 먼저 끝까지 확인할 가치가 있다.

---

## 다음 확인 우선순위
1. EDYS 최신 executable/source 요청 경로와 라이선스 확인
2. EDYS-L 4.6.4와 full EDYS의 차이 확인
3. erosion 시 root biomass truncation/remap routine 확인
4. deposition 시 root burial / plant mortality 반응 확인
5. woody plants의 age/size/state representation 상세 확인
6. forest application에서 overstory-understory competition 방식 확인
7. surface runoff routing이 multiple-neighbor / D8 / row-scan 중 실제 어떤 algorithm인지 최신 버전 확인
8. 고운사 1-10 m cell 규모 계산비용 추정

## 핵심 문헌/문서
- Childress, W. M., Price, D. L., Coldren, C. L., & McLendon, T. (1999). A Functional Description of the Ecological Dynamics Simulation (EDYS) Model, With Applications for Army and Other Federal Land Managers. CERL TR 99/55.
- Childress et al. (2002). Applying a complex, general ecosystem model (EDYS) in large-scale land management. Ecological Modelling 153:97-108. DOI 10.1016/S0304-3800(01)00504-X.
- Mata-González, R., Hunter, R., Coldren, C., & Paschke, M. (2007). Modelling plant growth dynamics in sagebrush steppe communities affected by fire. Journal of Arid Environments.
- McLendon, T., Coldren, C. L., & Price, D. L. (2009). Comparison of Results from the EDYS and EDYS-L Ecological Simulation Models as Applied to Vegetation and Hydrological Dynamics on the Honey Creek Watershed, Texas. ERDC TN-SWWRP-09-7.
- Coldren, C. L., McLendon, T., Childress, W. M., Price, D. L., & Graves, M. R. (2011). Ecological DYnamics Simulation Model - Light (EDYS-L): User's Guide Version 4.6.4. ERDC/EL SR-11-1.
- Goliad County EDYS Model Final Report (2016).
