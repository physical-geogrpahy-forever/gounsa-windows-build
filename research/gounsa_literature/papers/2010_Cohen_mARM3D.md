# 서지정보
Cohen, S., Willgoose, G., & Hancock, G. (2010). The mARM3D spatially distributed soil evolution model: Three-dimensional model framework and analysis of hillslope and landform responses. *Journal of Geophysical Research: Earth Surface, 115*, F04013. https://doi.org/10.1029/2009JF001536

# 이 논문을 찾은 이유
고운사의 매립 석력과 깊이에 따른 PSD, 풍화 및 soil-depth 변화까지 기존 armour model이 추적할 수 있는지 검토하기 위해 찾았다.

# 연구 유형
- 3D soil-profile evolution model
- state-space numerical framework

# 공간 구조
- 수천-수만 spatial pixels
- 각 pixel에서 수십 soil layers
- 각 layer에서 수십 particle-size classes

# 적용 환경
- stony soil/regolith evolution

# 핵심 과정
- surface selective erosion
- armouring
- physical weathering
- vertical profile resupply
- particle-size evolution with depth

# 식생 입력
- 없음

# 핵심 식
각 soil layer의 grading vector와 process transition matrices로 profile evolution을 계산한다.
논문은 matrix formulation이 특정 erosion equation에 묶이지 않고 다른 erosion physics와 결합 가능한 modular framework임을 강조한다.

# 파라미터와 단위
- layer thickness
- armour-layer depth
- particle-size classes
- weathering rate/transition
- erosion transition

# 원 논문의 구현 범위
mARM surface model을 다층 soil profile로 확장해 장기간 고해상도 particle grading을 계산한다.

# 고운사에 직접 사용할 수 있는 부분
- **매립 석력비와 입도분포를 깊이별 상태로 추적**
- 표면 fine removal 시 아래층 material resupply
- weathering으로 각 layer의 coarse fraction이 smaller classes로 이동
- armour와 soil depth를 같은 mass-conserving state-space structure에서 처리 가능

# 새로운 coupling이 필요한 부분
OpenLISEM/Iber+에서 계산한 2D event erosion/deposition mass를 transition input으로 전달하는 것은 new coupling이지만, mARM3D 자체가 특정 erosion physics에 종속되지 않는다는 원 논문의 modularity와 부합한다.

# 한계
논문 예시에서는 고정 elevation을 사용하여 process interpretation에 집중.
hydrology는 별도 모델 필요.

# 최종 판정
- **embedded stoniness/profile armour의 핵심 모델 후보**

# 참고 링크 / DOI
https://doi.org/10.1029/2009JF001536
