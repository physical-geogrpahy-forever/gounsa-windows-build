# 서지정보
Mao et al. (2010). *Development of a coupled soil erosion and large-scale hydrology modeling system*. 세부 저널/권호/DOI는 현재 복구자료에서 완전하지 않아 **원문 재검증 필요**.

# 이 논문을 찾은 이유
large-scale hydrology model과 WEPP 계열 erosion physics를 실제로 결합하고 vegetation state를 erodibility에 전달한 published precedent를 찾기 위해 검토했다.

# 연구 유형
- coupled numerical model
- VIC-WEPP/WEPP-HE 계열

# 공간 구조
- distributed large-scale hydrology
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

# 식생 입력
full WEPP에서 다음 상태를 가져와 erodibility 조정에 사용한 것으로 채팅에서 원문 확인:
- ground cover
- live root biomass
- dead root biomass
- residue

# 핵심 식
정확한 coupling 식 전체는 원문 재검증 필요. 중요한 확인점은 vegetation/root/residue 상태를 erosion parameter adjustment에 실제 사용했다는 것이다.

# 파라미터와 단위
원문 표 재검증 필요.

# 원 논문의 구현 범위
대규모 hydrology와 process-based soil erosion parameterization의 published coupling.

# 고운사에 직접 사용할 수 있는 부분
- `dynamic vegetation state -> erodibility adjustment`라는 coupling 선례
- forest/wooded vegetation에서도 root biomass-dependent erosion resistance를 사용한 근거

# 새로운 coupling이 필요한 부분
LPJ-GUESS를 VIC/WEPP 대신 연결하거나 genuine 2D 엔진에 넘기면 **새로운 coupling**.

# 한계
genuine 2D surface-flow model이 아님.

# 최종 판정
**채택: quantitative vegetation -> erosion-resistance coupling의 핵심 선례.**
