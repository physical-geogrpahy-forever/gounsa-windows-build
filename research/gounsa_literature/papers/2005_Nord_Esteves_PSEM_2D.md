# 서지정보
Nord, G., & Esteves, M. (2005). *PSEM_2D: A physically based model of erosion processes at the plot scale*. Water Resources Research, 41(8). DOI: 10.1029/2004WR003690.

# 이 논문을 찾은 이유
고운사에서 사용할 genuine 2D rainfall-runoff/erosion 엔진 후보를 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- physically based plot-scale erosion model

# 공간 구조
- genuine 2D
- depth-averaged 2D Saint-Venant equations
- explicit finite-difference scheme

# 적용 환경
- plot/hillslope
- natural nonplanar surface 적용 사례
- 산림 산지 검증은 아님

# 핵심 과정
- Green-Ampt infiltration
- rainfall detachment
- rainfall redetachment
- runoff detachment
- deposited-layer entrainment/deposition
- sediment mass conservation

# 식생 입력
- root biomass/RLD 직접입력 없음
- vegetation module 없음

# 핵심 식
원 논문은 rainfall-driven erosion과 flow-driven erosion을 같은 2D domain에서 계산한다.
원 논문은 rill/interrill을 고정 mask로 나누지 않으며 microtopography와 hydraulics가 rainfall-dominated/flow-dominated 영역을 결정한다.

# 파라미터와 단위
- rainfall erodibility alpha
- critical shear stress
- transport capacity / detachment parameters
정확한 단위는 원문 식/notation 기준으로 구현한다.

# 원 논문의 구현 범위
2D water flow와 erosion/deposition을 결합하며 natural surface에 공간분포 침식/퇴적을 계산한다.

# 고운사에 직접 사용할 수 있는 부분
- genuine 2D hydraulic/erosion engine의 핵심 비교후보
- rainfall-driven과 runoff-driven process를 분리하는 구조

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC, litter biomass 또는 WEPP root-dependent erodibility를 PSEM_2D erodibility parameter에 연결하면 **새로운 coupling**이다.

# 한계
- vegetation/root representation 없음
- 산불 산림 산지 적용 선례 없음
- 원 논문에서 rill/interrill을 명시적 class로 구분하지 않음

# 최종 판정
**보조 채택: genuine 2D erosion-engine 계보.** 식생량 coupling의 단독 해법은 아님.

# 참고 링크 / DOI
10.1029/2004WR003690
