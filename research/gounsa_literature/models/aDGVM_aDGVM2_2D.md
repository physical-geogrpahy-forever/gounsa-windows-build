# aDGVM / aDGVM2 / 2D-aDGVM

업데이트: 2026-09-23

# 왜 검토했는가
2025 vegetation-demography model review에서 grass demography의 중요한 별도 계열로 aDGVM이 언급되었고, 기존 고운사 저장소에서 아직 검토되지 않은 genuinely new lineage였기 때문이다.

고운사 기준에서 특히 중요한 질문:
- herb/grass, shrub, tree의 endogenous competition and succession
- daily vegetation response
- actual spatial/topographic implementation
- roots and soil-water feedback
- individual-tree보다 계산 부담이 허용 가능한가

# 계보를 반드시 구분해야 함
```
aDGVM 2009
  individual-based tropical grass-tree model
       |
       +--> 2D-aDGVM 2014
       |      spatially explicit topography
       |      seed dispersal
       |      fire spread
       |
       +--> aDGVM2 2013 onward
              trait-based individual community assembly
              later grass/tree/shrub growth forms
              daily individual ecophysiology
              improved plant hydraulics
```

중요:
**2D-aDGVM의 spatial machinery와 최신 aDGVM2의 trait/hydraulic machinery가 하나의 published ready-made model로 통합되었다고 확인된 것은 아니다.**

이를 고운사에서 합치면 새로운 coupling/code integration이다.

# aDGVM2 식생 구조
Current lineage evidence:
- individual plants
- growth
- reproduction
- mortality
- trait inheritance/mutation
- light and water competition
- grass growth form
- tree growth form
- shrub growth form in later applications
- perennial and annual grasses
- root and crown architecture
- fire response
- resprouting-related traits
- emergent community assembly

이 점에서 criterion 2는 매우 강하다.

# 시간해상도
Recent aDGVM2 applications:
- representative 1 ha stand
- daily time steps
- updated versions calculate leaf-level ecophysiology daily for individual plants
- reproduction can have annual scheduling, but plant state/ecophysiology is daily

따라서 criterion 5는 충족한다.

# 토양과 뿌리
aDGVM2 includes:
- root biomass/allocation
- root shape
- rooting depth
- multilayer soil-water availability
- plant water competition
- recent plant-hydraulic enhancement

그러나:
- published external hydrology state overwrite API를 확인하지 못함
- lateral hillslope flow를 aDGVM2가 직접 계산하지 않음
- erosion/deposition after-event layer remap 없음

따라서 criterion 3은 local physiology 측면에서는 강하지만 **external geomorphic coupling readiness는 MEDFATE/PF-LPJG/FATES-ParFlow보다 약하다**.

# 공간성
## aDGVM2 current applications
- 1 ha representative stands
- many stands can be simulated across regions/landscapes
- internal individual competition does not automatically imply geographic lateral coupling

## 2D-aDGVM 2014
- spatially explicit landscape
- topographic heterogeneity
- seed dispersal
- fire spread
- vegetation patch connectivity

따라서 model lineage에는 criterion 4의 distributed topographic precedent가 있다.

그러나:
- watershed water routing이 아니라 topography-fire-vegetation spatial dynamics
- latest aDGVM2 ecology/hydraulics와 same-code published integration 여부는 확인되지 않음

# 코드 가용성
Historical aDGVM project material은 source availability가 제한적이었던 시기가 있다.

하지만 2025 Langan et al. study에 사용된:
```
aDGVM2 v1.0-LL
DOI: 10.5281/zenodo.16265491
```
은 Zenodo에 Open software로 archive되어 있고 C++ source files를 포함한다.

주의:
- study-specific snapshot
- Zenodo는 development status를 Unsupported로 표시
- maintained universal mainline distribution과 동일하다고 가정하지 않는다.

# 고운사 5개 기준 판정

| 기준 | 판정 | 이유 |
|---|---|---|
| 1 spatial cohort/hybrid | **PARTIAL-STRONG but mismatched** | full individual-based model이며 최신 aDGVM2는 1 ha stand 중심. 2D-aDGVM spatial branch는 존재하지만 구버전 계열 |
| 2 explicit understory succession | **VERY STRONG** | grass/tree/shrub, annual/perennial grasses, growth/reproduction/mortality/competition, trait assembly |
| 3 soil-topography coupling | **STRONG local / MODERATE external** | root depth/shape, soil-water, hydraulics 강함. external overwrite/lateral hydrology published coupling 없음 |
| 4 hillslope/topographic precedent | **YES-PARTIAL** | 2D-aDGVM actual spatial topography, seed dispersal, fire spread. watershed hydrology는 아님 |
| 5 <=daily | **YES** | modern aDGVM2 daily stand/ecophysiology |

# 기존 shortlist와 비교
## FATES보다 좋은 점
- individual trait-based community assembly가 매우 explicit
- grass/tree/shrub life-history differentiation과 reproduction/mortality가 강함

## FATES보다 불리한 점
- full individual model이라 계산량이 더 큼
- ELM-ParFlow 같은 direct hillslope hydrology coupling precedent 없음
- spatial branch와 modern hydraulic branch가 분리됨
- temperate Korean postfire validation 없음

## LPJ-GUESS SEC보다 좋은 점
- herb/woody demographic competition이 더 individual-explicit
- daily individual physiological response가 명확

## LPJ-GUESS SEC보다 불리한 점
- SEC가 원하는 cohort middle ground에 더 가까움
- LPJ-DH/PF-LPJG라는 direct catchment/external-hydrology lineage가 없음
- aDGVM2는 computationally heavier

## MEDFATE보다 좋은 점
- endogenous herb/shrub/tree community assembly가 훨씬 강함

## MEDFATE보다 불리한 점
- actual GIS watershed cells와 direct lateral hydrology/state-editing 구조가 약함
- implementation burden가 큼

# 가장 중요한 판단
aDGVM2는 이번 broad screen에서 **즉시 탈락하지 않은 첫 genuinely new lineage**이다.

그러나 production top tier로 바로 승격하지는 않는다.

현재 역할:
**conditional candidate + strongest biological benchmark for explicit herb/shrub/tree assembly**

이유:
1. criterion 2와 5는 매우 강함
2. roots/soil-water physiology도 강함
3. topographic 2D precedent는 존재
4. 그러나 full individual approach의 계산량이 큼
5. 2D spatial branch와 modern aDGVM2 branch가 분리
6. direct lateral hillslope hydrology/external soil-state coupling precedent가 없음
7. tropical/savanna development history로 Korean temperate parameterization burden가 큼

# 고운사에서 실제 채택하려면 필요한 새로운 coupling
```
modern aDGVM2 biology/hydraulics
+ 2D geographic cell framework
+ external terrain/hydrology state exchange
+ event-driven soil-layer remap
```

이는 published single model이 아니다.

# 재검토 조건
다음 중 하나가 새로 확인될 경우 top shortlist 승격을 재검토한다.
- modern aDGVM2의 spatially explicit 2D code
- aDGVM2 + distributed hydrology/catchment coupling
- cohort/super-individual mode reducing computation
- temperate forest postfire herb-shrub-tree application

# 관련 논문
- `papers/2009_Scheiter_aDGVM_Africa.md`
- `papers/2013_Scheiter_aDGVM2_CommunityEcology.md`
- `papers/2014_Blanco_2DaDGVM.md`
- `papers/2017_Langan_aDGVM2_SouthAmerica.md`
- `papers/2022_Pfeiffer_aDGVM2_LandscapeRangeland.md`
- `papers/2025_Langan_aDGVM2_HydraulicDiversity.md`

# 최종 판정
**조건부 후보 / biological benchmark**

현재 production shortlist:
1. LPJ-GUESS SEC/PPA + PF-style external hydrology
2. FATES + ELM/ParFlow
3. MEDFATE + medfateland

aDGVM2는 이 셋 바로 아래에서, criterion 2를 가장 강하게 만족하는 대안으로 유지한다.
