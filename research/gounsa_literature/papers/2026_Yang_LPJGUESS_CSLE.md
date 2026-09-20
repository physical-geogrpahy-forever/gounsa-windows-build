# 서지정보
Yang et al. (2026). LPJ-GUESS v4.1과 CSLE vegetation factor를 결합한 soil erosion 연구. 정확한 전체 서지정보는 원문 재검증 필요.

# 이 논문을 찾은 이유
LPJ-GUESS를 실제 erosion model과 연결한 직접 선례가 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- DGVM-to-erosion coupling

# 공간 구조
- spatially distributed erosion assessment

# 적용 환경
- vegetation and soil erosion assessment

# 핵심 과정
- LPJ-GUESS vegetation dynamics
- LAI
- fractional vegetation cover
- CSLE soil erosion

# 식생 입력
- LPJ-GUESS LAI
- derived fractional vegetation cover

# 핵심 식
LPJ-GUESS -> LAI -> fractional vegetation cover -> CSLE vegetation B factor -> soil erosion.

# 파라미터와 단위
원문 재검증 필요.

# 원 논문의 구현 범위
LPJ-GUESS output을 erosion-factor model에 일방향으로 전달한다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS output을 geomorphic model input으로 사용하는 직접 선례.

# 새로운 coupling이 필요한 부분
고운사에서 PFT별 root biomass, understory, evolving DEM, bidirectional feedback을 넣는 것은 원 논문 밖의 새로운 coupling이다.

# 한계
- one-way coupling
- DEM evolution 없음
- canopy/fractional vegetation cover가 고운사 지표 ground cover를 대체하지 못함

# 최종 판정
- 보조근거
- 직접 채택 아님

# 참고 링크 / DOI
미복구, 원문 재검증 필요.
