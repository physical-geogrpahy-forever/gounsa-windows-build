# 서지정보
Argles, A. P. K., Moore, J. R., Huntingford, C., Wiltshire, A. J., Harper, A. B., Jones, C. D., & Cox, P. M. (2020). Robust Ecosystem Demography (RED version 1.0): a parsimonious approach to modelling vegetation dynamics in Earth system models. *Geoscientific Model Development*, 13, 4067-4089. https://doi.org/10.5194/gmd-13-4067-2020

# 이 논문을 찾은 이유
고운사 5조건에서 개별목보다 가볍고 size-cohort를 유지하면서 초본, 관목, 교목의 명시적 천이를 다룰 수 있는 모델을 찾기 위해 검토했다.

# 연구 유형
- 수치모델 개발
- demographic DGVM / cohort model

# 공간 구조
- 각 spatial location/grid cell에서 PFT별 plant number-density distribution을 mass 축으로 이산화
- tree 10 mass classes, shrub 8 mass classes, grass 1 mass class를 사용한 실험
- 개별 식물 x-y 위치 및 disturbance-patch age는 추적하지 않음

# 적용환경
- 이론 및 전지구 실험
- bare-soil succession local experiment
- UKESM/JULES PFT 체계와 결합 가능하도록 설계

# 핵심과정
- PFT별 net assimilate
- reproduction allocation
- seedling production
- gap-limited recruitment
- mass-class growth transition
- baseline/disturbance mortality
- tree-shrub-grass competition
- succession

# 식생입력
- PFT net carbon assimilate
- seedling allocation fraction
- minimum mass
- mass-class ratio/range
- crown-area allometry
- height allometry
- mortality
- competition hierarchy

# 핵심식
RED의 연속식은 PFT별 plant number density n(m,t)의 질량축 continuity equation이다.

Discrete form에서는 각 mass class의 plant number가 이전 mass class로부터의 growth flux, 다음 class로 나가는 flux, mortality로 갱신된다.

최저 mass class의 recruitment flux는 PFT carbon assimilate 중 reproduction에 배분되는 양과 seedling mass, 그리고 available gap fraction으로 계산한다.

경쟁 hierarchy:
```text
tree shades tree + shrub + grass
shrub shades shrub + grass
grass shades grass
```

# 파라미터와 단위
- mass [kg C plant-1]
- plant number density [plants area-1]
- mortality [time-1]
- crown area [m2]
- height [m]
- reproductive fraction alpha
- RED 논문의 numerical experiment timestep: 1 month

# 원 논문의 구현 범위
Bare soil에서 시작한 local succession experiment에서 빠른 grass가 먼저 우점하고 약 12년 이후 evergreen shrub가 grass seedling을 차광하며 대체한 뒤 broadleaf tree가 shrub와 grass를 추가로 대체했다. 약 20년경 vegetation fraction이 평형에 가까워졌고 biomass equilibration은 훨씬 오래 걸렸다.

# 고운사에 직접 사용할 수 있는 부분
- 초본 -> 관목 -> 교목이라는 postfire 초기천이 구조의 직접 precedent
- woody vegetation을 individual tree가 아닌 mass cohorts로 단순화
- root/litter/hydrology를 JULES 쪽과 결합할 수 있는 demographic skeleton
- disturbance mortality를 PFT/size class별로 추가할 수 있는 구조

# 필요한 새로운 coupling
- 고운사 GIS cell 및 fine geomorph grid 연결
- geomorphic soil-depth change remapping
- Korea temperate PFT parameterization
- 필요한 경우 더 명시적인 understory canopy/light competition

# 한계
1. cohort 내 x-y 위치 없음
2. competition은 lowest seedling mass class의 gap availability에 집중됨
3. grass는 논문 기본 설정에서 1 mass class
4. 각 functional-group 내부에서는 장기적으로 subdominant PFT competitive exclusion 경향
5. original numerical experiment의 demographic timestep은 1 month

# 최종 판정
**채택 후보 / 핵심 demographic reference.**

JULES v8.1에 RED가 정식 옵션으로 존재하고 dynamic vegetation 호출주기가 1일까지 허용되므로, 원 논문의 1-month timestep을 현행 구현의 절대 하한으로 해석하지 않는다.

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-13-4067-2020
