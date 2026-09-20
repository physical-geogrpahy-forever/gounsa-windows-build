# 서지정보
Li, W., Liu, B., & Hu, P. (2023). *Fast modeling of vegetated flow and sediment transport over mobile beds using shallow water equations with anisotropic porosity*. Water Resources Research, 59, e2021WR031896. DOI: 10.1029/2021WR031896.

# 이 논문을 찾은 이유
genuine 2D finite-volume morphodynamics에서 vegetation structure 자체를 명시적으로 flow and sediment transport에 넣는 최신 모델이 고운사 2D 엔진보다 나은지 확인하기 위해 검토했다.

# 연구 유형
- 2D hydromorphodynamic numerical model
- finite-volume model

# 공간 구조
- genuine 2D shallow-water equations
- anisotropic porosity formulation
- finite volume
- OpenMP parallelization
- mobile bed

# 적용 환경
- flume/channel
- rigid emergent vegetation patches
- riverine/estuarine/coastal morphodynamics

# 핵심 과정
- 2D flow
- vegetation drag
- preferential flow around vegetation
- sediment transport
- deposition
- mobile-bed morphology

# 식생 입력
- stem diameter
- vegetation density
- geometrical occupation/porosity
- drag coefficient

즉 vegetation **structure/geometry**를 직접 사용하지만 root biomass 또는 litter biomass는 사용하지 않는다.

# 핵심 식
Vegetation is represented through:
- cell-based porosity for volumetric occupation
- edge-based porosity for flux exchange
- explicit vegetation drag force

The model predicts flow, sediment transport and bed morphological change.

# 파라미터와 단위
- stem diameter
- patch density
- drag coefficient
- Manning roughness
- sediment grain-size classes
- active-bed-layer thickness

# 원 논문의 구현 범위
rigid emergent vegetation이 2D flow routing, turbulence-related sediment transport, deposition pattern을 어떻게 바꾸는지 계산한다.

# 고운사에 직접 사용할 수 있는 부분
- 목본 stem geometry가 집중류 routing과 sediment transport에 미치는 효과를 explicit 2D resistance로 표현하는 선례
- 향후 LPJ-GUESS woody density/DBH를 hydraulic roughness보다 더 물리적으로 연결할 후보

# 새로운 coupling이 필요한 부분
LPJ-GUESS woody cohort -> stem density/diameter/porosity map은 새로운 coupling이다.

# 한계
- rainfall-generated hillslope erosion 아님
- root biomass 없음
- litter 없음
- sediment detachment resistance보다 transport/deposition과 stem drag 중심
- channel/flume geometry

# 최종 판정
- **보조근거**
- Iber+/SERGHEI-SE보다 고운사 유수침식 본체로 우월하지 않음
- aboveground woody hydraulic effect의 향후 서브모듈 후보

# 참고 링크 / DOI
https://doi.org/10.1029/2021WR031896
