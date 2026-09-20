# 서지정보
Roque-Malo, S., Druhan, J. L., & Kumar, P. (2022). REWTCrunch: A modeling framework for vegetation induced reactive zone processes in the Critical Zone. *Journal of Geophysical Research: Biogeosciences, 127*, e2021JG006562.

# 이 논문을 찾은 이유
root biomass와 exudation을 reactive transport와 직접 결합한 process model을 찾기 위해 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- vertically resolved Critical Zone reactive transport

# 적용 환경
- 토양-풍화대

# 핵심 과정
- root exudation
- microbial activity
- mineral dissolution
- reactive transport

# 식생 입력
- 수직분포 root biomass
- root exudation

# 핵심 식
`RootBiomass(z,t) -> RootExudation -> microbial/chemical reactions -> mineral dissolution`.

# 파라미터와 단위
root biomass depth profile, exudation, reaction parameters. 세부값 원문 재확인 필요.

# 원 논문의 구현 범위
일 단위 식물-뿌리-광물반응을 결합한다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS FineRootC(z,t)를 C/Cr chemical weathering에 연결할 직접 선례.

# 새로운 coupling이 필요한 부분
광물용해 flux를 soil/regolith production thickness로 변환하면 새로운 coupling.

# 한계
geomorphic LEM 자체가 아니라 reactive transport model.

# 최종 판정
- 채택 후보의 화학풍화 보조모듈

# 참고 링크 / DOI
https://doi.org/10.1029/2021JG006562
