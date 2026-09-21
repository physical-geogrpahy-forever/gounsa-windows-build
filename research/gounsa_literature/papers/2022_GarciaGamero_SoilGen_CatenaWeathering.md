# 서지정보
García-Gamero, V., Vanwalleghem, T., Peña, A., Román-Sánchez, A., & Finke, P. A. (2022). Modelling the effect of catena position and hydrology on soil chemical weathering. SOIL, 8, 319-335.
DOI: 10.5194/soil-8-319-2022

# 이 논문을 찾은 이유
사면 위치와 hydrology를 chemical weathering과 soil-profile evolution에 실제 수치적으로 연결한 모델을 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- long-term pedogenesis / chemical weathering
- field validation 포함

# 공간 구조
- SoilGen 1D pedon
- 대표 면적 약 1 m2
- 5 cm vertical compartments
- 7개 catena position을 각각 독립 모의
- 20,000 yr simulation
- pedon 사이 lateral water flux 없음

# 적용 환경
- southern Spain Mediterranean catchment
- north-facing / south-facing catena
- granitic parent material

# 핵심 과정
- Richards-equation water flow
- heat flow
- gas diffusion
- solute advection/dispersion
- physical weathering
- chemical weathering
- carbon cycling
- clay migration
- bioturbation
- deposition/erosion as boundary forcing

# 식생 입력
- vegetation은 time-dependent soil-forming boundary/driver
- dynamic forest competition/succession engine은 아님
- LPJ-GUESS 같은 quantitative forest state와의 양방향 feedback 없음

# 핵심 식
각 5 cm compartment에서 water, heat, gas, solute transport PDE와 pedogenic processes를 함께 계산한다.

catena position -> hydrologic state -> chemical depletion

가 핵심 구조이며, 실제 결과에서는 catena label 또는 slope gradient보다 soil moisture와 infiltration 같은 hydrological variables가 CDF 변이를 더 잘 설명했다.

# 파라미터와 단위
- layer thickness: 5 cm
- simulation: 20,000 yr
- precipitation sensitivity: 200-1200 mm yr-1
- measured vs modeled CDF agreement: R2 = 0.47

# 원 논문의 구현 범위
- 7개 catena positions의 pedogenesis와 chemical depletion fraction을 모의
- soil moisture와 infiltration은 CDF와 양의 관계
- residence/transit condition과 weathering의 관계가 단순 단조식이 아님
- profile-average weathering은 sensitivity에서 약 800 mm yr-1 부근에서 최대
- authors가 lateral water flux omission을 명시적 한계로 지적

# 고운사에 직접 사용할 수 있는 부분
1. hillslope-position multiplier 대신 hydrologic state로 weathering을 계산해야 한다는 실제 model evidence.
2. vertical soil profile에서 water + gas + solute + chemical/physical weathering을 함께 계산하는 구조.
3. H_AB 및 weathered-zone vertical discretization 설계 참고.

# 새로운 coupling이 필요한 부분
- pedon 사이 lateral flow/convergence/shallow-deep routing은 NEW COUPLING.
- LPJ-GUESS dynamic vegetation과 양방향 연결도 NEW COUPLING.
- 2D evolving terrain과 연결도 별도 coupling.

# 한계
- genuine 2D hillslope model 아님.
- lateral water flux 없음.
- terrain evolution 없음.
- 20 kyr 중심이라 100 yr postfire transient를 그대로 적용할 수 없음.
- granite parameter를 sandstone에 전이할 수 없음.

# 최종 판정
- 채택
- 역할: vertical pedogenesis + hydrology + chemical weathering model reference.
- full Gounsa hillslope engine으로 단독 채택하지 않음.

# 참고 링크 / DOI
- https://doi.org/10.5194/soil-8-319-2022