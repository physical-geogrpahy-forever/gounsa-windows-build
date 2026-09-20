# 서지정보
Francipane, A., Ivanov, V. Y., Noto, L. V., Istanbulluoglu, E., Arnone, E., & Bras, R. L. (2012). *tRIBS-Erosion: A parsimonious physically-based model for studying catchment hydro-geomorphic response*. CATENA, 92, 216-231. DOI: 10.1016/j.catena.2011.10.005.

# 이 논문을 찾은 이유
tRIBS family가 event-scale erosion뿐 아니라 100-year landscape hydro-geomorphic response를 실제로 계산한 선례인지 확인하고, FEaST/Hairsine-Rose 계열과 비교하기 위해 검토했다.

# 연구 유형
- physically based distributed hydro-geomorphic numerical model
- catchment erosion and long-term landscape-response model

# 공간 구조
- tRIBS TIN hydrology
- coupled hillslope/channel geomorphic component
- distributed catchment
- not the same full 2D Hairsine-Rose FEaST formulation

# 적용 환경
- catchment applications
- synthetic first-order basins
- stationary-climate long-term experiment

# 핵심 과정
Hillslopes:
- raindrop impact detachment
- overland-flow entrainment
- diffusive processes

Channels:
- flow erosion
- deposition

Topography and hydro-geomorphic response are coupled.

# 식생 입력
This paper is not a quantitative root/litter erosion-resistance study.
Vegetation dynamics are not the central erosion-state control.

# 핵심 식
A parsimonious geomorphic component is integrated into tRIBS hydrology to represent hillslope and channel erosion/deposition.

Exact equations should be taken from the original article before any implementation.

# 파라미터와 단위
- raindrop detachability
- flow entrainment
- hillslope diffusion
- channel erosion/deposition parameters
Exact units in the original paper.

# 원 논문의 구현 범위
The model was tested for catchment hydro-geomorphic response and also run for **100 years** under stationary climate in two synthetic first-order basins dominated by contrasting fluvial/diffusive processes.

# 고운사에 직접 사용할 수 있는 부분
1. Direct proof that the tRIBS model family can support 100-year hydro-geomorphic experiments.
2. Long-term coupling of hydrology and evolving topography is computationally feasible in this lineage.
3. Provides an alternative strategy for separating event erosion physics from slower diffusive geomorphic processes.

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation/root/litter control remains a new coupling.

# 한계
- parsimonious erosion formulation is less detailed than FEaST/Hairsine-Rose for original/deposited layers and multiclass sediment
- quantitative vegetation state absent
- not a postfire forest model

# 최종 판정
- **important 100-year feasibility precedent**
- not preferred as final erosion formulation if FEaST/SWEHR can be adapted for long-term event sequencing
- useful architecture reference for coupling event erosion with slower geomorphic processes

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2011.10.005
