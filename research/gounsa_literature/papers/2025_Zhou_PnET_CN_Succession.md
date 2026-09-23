# 서지정보
Zhou, Z., Gustafson, E. J., Ollinger, S. V., Ouimette, A. P., Miranda, B. R., Duveneck, M., Foster, J. R., Sturtevant, B. R., Bronson, D., & Laflower, D. (2025). Integrating nitrogen and carbon cycling into LANDIS-II/PnET-Succession to improve forest landscape modeling: methods and sensitivity analyses. Ecological Modelling, 510, 111285. DOI: 10.1016/j.ecolmodel.2025.111285

# 이 논문을 찾은 이유
개체목 모델보다 단순하지만 일반적인 경관모델보다 시간적 생리과정과 공간격자 해상도가 세밀한 중간급 식생모델을 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- cohort-based forest succession / ecophysiology

# 공간 구조
- LANDIS-II grid cell
- cell마다 수종-연령 cohort 1개 이상
- 개체목 위치는 추적하지 않음
- cell size는 LANDIS-II에서 사용자 정의

# 적용 환경
- 온대 낙엽수림 및 상록수림
- Harvard Forest 검증

# 핵심 과정
- cohort competition for light, water, nutrients
- monthly photosynthesis and soil-water balance
- C/N cycling
- establishment
- growth
- mortality
- disturbance coupling

# 식생 입력 / 상태
- foliage C/N
- live wood C/N
- fine-root C/N
- plant C/N
- root litter
- foliar litter
- dead wood
- soil organic C/N
- NH4+, NO3-

# 핵심 식
C와 N pool을 cohort scale과 site(cell) scale에서 분리하여 계산한다. 각 cohort는 광, 수분, 질소를 경쟁하고 fine-root, foliage, wood로 탄소를 배분한다.

# 파라미터와 단위
- internal process timestep: monthly
- cohort state per cell
- C/N pools: mass per area or cohort state

# 원 논문의 구현 범위
PnET-Succession에 PnET-CN의 탄소-질소 순환을 통합하여 생장과 천이를 모의한다.

# 고운사에 직접 사용할 수 있는 부분
- 개체목을 추적하지 않는 cohort representation
- monthly physiology
- fine-root biomass
- root litter
- dead wood
- soil organic C/N
- spatial LANDIS grid
- fire/disturbance extension과 결합 가능

# 새로운 coupling이 필요한 부분
- hourly/event geomorph model과 monthly vegetation state exchange
- LiDAR DEM 기반 5-20 m cell에서의 calibration
- root biomass -> RLD/RID/root reinforcement
- litter -> erosion protection
- geomorphic soil-depth changes -> PnET soil-water/root-zone state

# 한계
- 한 cell 내부의 개체목 위치는 없음
- cell 내부 환경은 기본적으로 균질하게 취급
- 내부 생리 time step은 monthly로 hourly geomorph process보다 거침

# 최종 판정
- 최우선 중간복잡도 후보
- HETEROFOR보다 단순하고 LANDIS-II NECN보다 생리적으로 세밀함

# 참고 링크 / DOI
https://doi.org/10.1016/j.ecolmodel.2025.111285
