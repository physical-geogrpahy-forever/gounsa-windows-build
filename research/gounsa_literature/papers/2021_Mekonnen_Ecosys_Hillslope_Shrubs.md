# 서지정보
Mekonnen, Z. A., Riley, W. J., Grant, R. F., Salmon, V. G., Iversen, C. M., Biraud, S. C., Breen, A. L., & Lara, M. J. (2021). Topographical Controls on Hillslope-Scale Hydrology Drive Shrub Distributions on the Seward Peninsula, Alaska. Journal of Geophysical Research: Biogeosciences, 126. https://doi.org/10.1029/2020JG005823

# 이 논문을 찾은 이유
고운사 식생엔진 후보가 실제 사면 지형, 서로 다른 토심과 배수조건, 연결된 측방수문을 식생 PFT 경쟁에 반영한 published precedent가 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- ecosys coupled hillslope transect
- 현장 관측 검증

# 공간 구조
- 연결된 hillslope transect
- crest, midslope, lower-slope를 포함하는 실제 지형 위치
- grid cell 사이 수문 연결
- 각 cell 안에 다층 토양과 다층 수관

# 적용 환경
- Seward Peninsula, Alaska
- Kougarok Hillslope
- tundra hillslope
- 얕고 건조한 능선부터 습윤/포화 하부사면까지의 수문구배

# 핵심 과정
- 지형에 따른 drainage와 soil-water redistribution
- soil moisture
- canopy water potential
- microbial N mineralization
- root N uptake
- biological N2 fixation
- shrub, graminoid, nonvascular PFT competition

# 식생 입력
- deciduous shrub
- evergreen shrub
- graminoid
- moss/lichen 계열 nonvascular vegetation
- PFT별 leaf/root functional traits
- 다층 leaf area
- 다층 root length

# 핵심 식
논문의 핵심은 하나의 단순 지형지수식보다 ecosys의 연결된 수문-토양-식생 방정식을 이용해 사면 위치별 수분상태가 식생 생리와 경쟁을 직접 바꾸는 것이다.

개념적 연결은 다음과 같다.

```text
topography / soil depth
 -> drainage and lateral water redistribution
 -> soil water + oxygen
 -> canopy water potential + microbial mineralization
 -> root water/N uptake
 -> PFT growth and competition
 -> shrub distribution
```

# 파라미터와 단위
- soil depth: 공간별 상이
- soil water content: m3 m-3 계열
- canopy water potential: MPa
- biomass: PFT별 지상부 biomass
- model timestep: ecosys hourly class

# 원 논문의 구현 범위
Kougarok 사면의 여러 지형위치에서 PFT별 biomass를 관측과 비교했다.

주요 결과:
- modeled PFT aboveground biomass와 관측값의 R2 약 0.89
- well-drained, shallower-soil crest에서 water stress가 크고 shrub biomass가 낮음
- midslope의 중간 수준 soil moisture가 N mineralization과 plant N uptake를 증가시켜 shrub growth를 강화
- lower slope에서는 과습 및 산소 제한이 발생 가능

# 고운사에 직접 사용할 수 있는 부분
1. 실제 사면 위치에 따른 soil depth/drainage 차이가 식생 biomass와 조성을 바꾸는 published precedent
2. 토심 자체보다 토심이 만드는 soil-water storage와 drainage를 식생에 연결하는 구조
3. 지형모델의 soil-water/soil-depth state를 식생 생리에 feedback하는 설계 근거
4. shrub 및 herbaceous/graminoid competition을 지형수문과 함께 계산하는 근거
5. hourly class process model을 사면에 적용할 수 있다는 근거

# 새로운 coupling이 필요한 부분
- 고운사 산불 후 온대림 PFT parameterization
- geomorph engine의 erosion/deposition으로 토양층 두께가 동적으로 바뀌었을 때 ecosys layer state remapping
- 수목 age/size cohort 또는 개별목 구조가 필요하다면 별도 demographic representation
- 고운사 1-5 m 지형격자와 ecosys vegetation grid 사이 scale bridge

# 한계
1. tundra/shrub-dominated 환경이며 온대 산림 직접 적용은 아니다.
2. ecosys plant population은 LPJ-GUESS식 age cohort가 아니다.
3. 본 논문의 핵심은 topographic control과 PFT competition이며 수목 stand structure 재현이 아니다.
4. 산불 후 tree-shrub-herb succession을 직접 검증한 논문은 아니다.

# 최종 판정
- **채택: 지형-수문-하층식생 coupling의 핵심 published precedent**
- 최종 vegetation demographic engine 단독 근거라기보다는 ecosys 계열의 조건 3, 4, 5를 강하게 지지하는 논문

# 참고 링크 / DOI
https://doi.org/10.1029/2020JG005823
