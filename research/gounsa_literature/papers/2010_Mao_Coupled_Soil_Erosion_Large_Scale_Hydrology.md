# 서지정보
Mao, D., Cherkauer, K. A., & Flanagan, D. C. (2010). *Development of a coupled soil erosion and large-scale hydrology modeling system*. Water Resources Research, 46, W08543. DOI: 10.1029/2009WR008268.

# 이 논문을 찾은 이유
large-scale hydrology model과 WEPP 계열 erosion physics를 실제로 결합하고 vegetation state를 erodibility에 전달한 published precedent를 찾기 위해 검토했다.

# 연구 유형
- coupled numerical model
- VIC-WEPP/WEPP-HE 계열

# 공간 구조
- distributed large-scale hydrology
- representative process erosion parameterization
- genuine 2D shallow-water는 아님

# 적용 환경
- forest
- wooded grassland
- prairie grassland
- cropland 등 vegetation type을 포함한 대규모 유역

# 핵심 과정
- hydrology
- interrill/rill erodibility adjustment
- sediment production
- large-scale sediment-yield estimation

# 식생 입력
full WEPP에서 다음 상태를 가져와 erodibility adjustment에 사용한 것으로 이 채팅에서 원문 확인:
- ground cover
- live root biomass
- dead root biomass
- residue

# 핵심 식
VIC hydrology와 WEPP hillslope erosion routines를 연결하여 soil erodibility parameters를 vegetation/soil state에 따라 조정한다.
개별 root-mass multiplier는 WEPP model lineage 파일과 Lee et al. (2022) 파일에서 관리한다.

# 파라미터와 단위
WEPP erodibility와 vegetation-state parameters. 구현 시 원문/WEPP technical documentation의 단위를 그대로 따른다.

# 원 논문의 구현 범위
대규모 hydrology와 process-based soil erosion parameterization의 published coupling.

# 고운사에 직접 사용할 수 있는 부분
- `dynamic vegetation state -> erodibility adjustment`라는 coupling 선례
- forest/wooded vegetation에서도 root biomass와 residue가 erosion-resistance parameterization에 관여하는 근거
- 대규모 hydrology와 WEPP process formulation을 연결한 선례

# 새로운 coupling이 필요한 부분
LPJ-GUESS를 VIC/WEPP 대신 연결하거나 genuine 2D 엔진에 넘기면 **새로운 coupling**이다.

# 한계
- genuine 2D surface-flow model이 아님
- 고운사 hillslope-scale 2D hydraulics를 직접 해결하지 않음

# 최종 판정
**채택: quantitative vegetation -> erosion-resistance coupling의 핵심 선례.**

# 참고 링크 / DOI
10.1029/2009WR008268
