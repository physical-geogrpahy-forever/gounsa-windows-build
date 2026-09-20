# 서지정보
Hales, T. C. (2018). *Modelling biome-scale root reinforcement and slope stability*. Earth Surface Processes and Landforms, 43(10), 2157-2166. DOI: 10.1002/esp.4381.

# 이 논문을 찾은 이유
LPJ-GUESS의 root biomass를 shallow-landslide mechanics의 root reinforcement/root cohesion으로 연결할 biome-scale mechanistic bridge를 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- root-reinforcement model
- biome-scale parameterization
- Monte Carlo uncertainty propagation

# 공간 구조
- biome-scale root-depth distribution
- depth-dependent reinforcement/cohesion profile
- slope-stability input용 mechanics

# 적용 환경
- 산지
- 산림
- 관목
- 초본 biome

# 핵심 과정
- root biomass distribution
- root tensile/material properties
- root reinforcement
- shallow landslide resistance

# 식생 입력
- root biomass
- root biomass depth distribution
- root tissue density
- root tensile strength
- root traits / plant functional group

# 핵심 식
개념적 연결:
```
root biomass
 -> root cross-sectional area
 -> tensile failure force
 -> root cohesion
```

채팅에서 복구된 modified Wu/Waldron 형태:
```
C_r = r F / D_s
```
정확한 기호 정의와 전체 식은 원문을 기준으로 한다.

# 파라미터와 단위
- root biomass: M L^-2
- root tissue density: kg m^-3 계열
- tensile strength: Pa
- root cohesion: Pa 또는 kPa
- soil depth: m

# 원 논문의 구현 범위
biome-level biomass distribution과 root mechanical properties를 이용해 depth-dependent root reinforcement와 불확실성을 계산한다.

# 고운사에 직접 사용할 수 있는 부분
```
LPJ-GUESS FineRootC
 -> root distribution / architecture
 -> root reinforcement or c_r
 -> factor of safety
```
의 핵심 mechanistic bridge.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC를 Hales가 요구하는 root dry mass, diameter/area distribution, depth profile, tensile properties로 변환하는 과정은 **새로운 coupling 또는 별도 문헌식이 필요**하다.

# 한계
- dynamic vegetation model 자체는 아님
- root-trait uncertainty가 큼
- 유수침식 Ki/Kr용 root effect와 동일 parameter로 사용하면 안 됨

# 최종 판정
- 채택 후보
- shallow-landslide 모듈 활성화 시 핵심 근거
- root biomass -> mechanics bridge로 유지

# 참고 링크 / DOI
https://doi.org/10.1002/esp.4381
