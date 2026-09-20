# 서지정보
Hales, T. C. (2018). Modelling biome-scale root reinforcement and slope stability. *Earth Surface Processes and Landforms, 43*, 2157-2166. https://doi.org/10.1002/esp.4381

# 이 논문을 찾은 이유
root biomass를 root cohesion으로 바꾸는 실제 mechanics bridge를 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- root-reinforcement model
- biome-scale parameterization

# 공간 구조
- biome-scale root-depth distribution
- Monte Carlo uncertainty propagation
- slope-stability input용 cohesion profile

# 적용 환경
- 산지
- 산림, 관목, 초본 biome

# 핵심 과정
- root reinforcement
- shallow landslide resistance

# 식생 입력
- root biomass
- root biomass depth distribution
- root tissue density
- root tensile strength
- plant functional group

# 핵심 식
개념적 연결:
`root biomass -> root cross-sectional area -> tensile failure force -> root cohesion`

modified Wu/Waldron:
`Cr = r * F / Ds`

# 파라미터와 단위
- root biomass: M L-2
- root density: kg m-3 계열
- tensile strength: Pa
- root cohesion: Pa 또는 kPa
- soil depth: m

# 원 논문의 구현 범위
biome-level biomass distribution과 root mechanical properties를 사용해 depth-dependent root cohesion 및 불확실성을 계산한다.

# 고운사에 직접 사용할 수 있는 부분
FineRootC에서 slope-stability용 root cohesion으로 가는 bridge model.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC를 Hales가 요구하는 root dry mass, depth profile, area distribution으로 변환하는 부분은 `새로운 coupling`이다.

# 한계
root tensile strength와 root density 불확실성이 크며 유수침식 저감식이 아니라 slope stability용 모델이다.

# 최종 판정
- 보류
- shallow landslide 모듈 활성화 시 채택 후보

# 참고 링크 / DOI
https://doi.org/10.1002/esp.4381
