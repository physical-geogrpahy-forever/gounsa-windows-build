# 서지정보
Glückler, R., Gloy, J., Dietze, E., Herzschuh, U., et al. (2024). Simulating long-term wildfire impacts on boreal forest structure in Central Yakutia, Siberia, since the Last Glacial Maximum. Fire Ecology, 20, 1. DOI: 10.1186/s42408-023-00238-8

# 이 논문을 찾은 이유
고운사처럼 산불 후 수십-100년 식생회복을 매우 세밀한 2D 공간에서 모의하는 개체기반 모델을 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- spatially explicit individual-based wildfire vegetation model

# 공간 구조
- 개별 나무와 종자를 x,y 좌표로 추적
- 환경 sub-grid 0.2 m x 0.2 m
- 사용자 정의 plot 규모
- topography, slope, TWI 등을 반영 가능

# 적용 환경
- 중앙 Yakutia boreal forest
- 장기 산불-식생 상호작용

# 핵심 과정
- annual establishment
- growth
- competition
- mortality
- seed production and wind dispersal
- climate-driven fire probability
- fire-caused tree/seed mortality
- litter-layer reduction
- postfire regeneration pathways

# 식생 입력/상태
- individual trees
- seeds
- local tree density
- litter-layer height
- active-layer-related environment
- fine-root biomass/dead-root pool은 명시적 핵심 상태로 확인되지 않음

# 핵심 식
산불은 월별 기상에 따른 발생확률과 지역적 intensity를 통해 개별 나무, 종자, litter layer에 영향을 준다. 식생 생활사는 연 단위로 갱신된다.

# 파라미터와 단위
- environment grid: 0.2 m x 0.2 m
- vegetation cycle: annual
- climate forcing: monthly temperature/precipitation plus wind

# 원 논문의 구현 범위
세밀한 공간에서 산불과 개별목 재생/경쟁/사망을 장기적으로 모의.

# 고운사에 직접 사용할 수 있는 부분
- 산불 후 실제 공간적 재생
- 개별목과 종자 위치
- litter layer의 공간적 소실과 회복
- slope/topographic wetness 같은 지형변수와 식생상태 연결

# 새로운 coupling이 필요한 부분
- 한국 온대림 수종 parameterization
- fine/coarse root biomass와 turnover
- erosion/soil production interface
- 0.2 m 내부격자를 고운사 30 m geomorph grid에 집계하는 방법

# 한계
현재 공개 모델은 boreal/permafrost 환경과 제한된 수종에 특화되어 있다. 특히 고운사에서 가장 중요한 quantitative root state가 부족하다.

# 최종 판정
- 강한 보조후보
- 공간과 산불 후 천이는 매우 강함
- root coupling 때문에 주 식생모델로는 현재 보류

# 참고 링크 / DOI
https://doi.org/10.1186/s42408-023-00238-8
https://doi.org/10.5281/zenodo.17477084
