# 서지정보
Hales (2018). DOI: 10.1002/esp.4381. 정확한 제목은 원문 재검증 필요.

# 이 논문을 찾은 이유
root biomass를 지반의 root mechanical reinforcement와 연결하는 bridge 확인.

# 연구 유형
- 수치/통계 모델

# 공간 구조
- depth-dependent parameterization

# 적용 환경
- 여러 biome, 산림 포함

# 핵심 과정
- root mechanical reinforcement

# 식생 입력
- root biomass
- root depth distribution
- root traits

# 핵심 식
root biomass와 tensile properties를 결합해 depth-dependent reinforcement를 계산한다. 세부식은 원문 재검증 필요.

# 파라미터와 단위
root biomass, tissue density, tensile strength. 세부 단위 원문 재검증 필요.

# 원 논문의 구현 범위
biome-level root biomass와 mechanical properties 연결.

# 고운사에 직접 사용할 수 있는 부분
FineRootC를 depth-dependent root reinforcement로 변환하는 bridge.

# 새로운 coupling이 필요한 부분
LPJ-GUESS PFT별 root traits 연결은 새로운 coupling.

# 한계
dynamic vegetation model 자체는 아님.

# 최종 판정
- 채택 보조근거
