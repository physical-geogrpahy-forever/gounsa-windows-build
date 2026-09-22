# 서지정보
Schwarz, M., Cohen, D., & Or, D. (2012). Spatial characterization of root reinforcement at stand scale: Theory and case study. Geomorphology, 171-172, 190-200. DOI: 10.1016/j.geomorph.2012.05.020

# 이 논문을 찾은 이유
LiDAR/HETEROFOR/ChaMRoots로 얻는 개체목 공간정보를 shallow-landslide root reinforcement로 물리적으로 연결할 published spatial model을 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- 현장검증
- spatial root reinforcement / shallow-landslide mechanics

# 공간 구조
- stand-scale spatially explicit root-distribution model
- 개별목 root system의 공간 중첩
- spatial Root Bundle Model(RBM)

# 적용 환경
- forested hillslope
- northern Switzerland
- rainfall-triggered artificial landslide case

# 핵심 과정
1. lateral root distribution around individual trees
2. overlap of root systems among trees
3. root diameter distribution
4. root mechanical behaviour
5. progressive root-bundle pullout/failure
6. spatial reinforcement field on the hillslope

# 식생 입력
- individual tree positions
- tree/root-system dimensions
- root diameter and density distribution
- root tensile/pullout properties

# 핵심 출력
- maximum root reinforcement
- displacement at maximum reinforcement
- spatial variation of reinforcement within stand

Case-study estimates showed strong within-stand variability, approximately 0-20 kPa for maximum reinforcement.

# 고운사에 직접 사용할 수 있는 부분
```
LiDAR/HETEROFOR tree map
     |
ChaMRoots / root-distribution helper
     |
Schwarz spatial root distribution
     |
Root Bundle Model
     |
spatial root reinforcement
     |
shallow-landslide factor of safety
```

개별목 위치를 알고 있는 LiDAR 기반 고운사에는 stand-average apparent cohesion보다 훨씬 적합하다.

# 새로운 coupling이 필요한 부분
- Korean species tensile/pullout properties
- HETEROFOR annual root biomass -> root diameter/density update
- postfire live/dead root strength decay
- LiDAR DEM의 potential slip-surface geometry와 root reinforcement field 결합

# 한계
- shallow landslide/root reinforcement 모델이며 water erosion resistance 모델이 아님
- root erosion effect와 동일 parameter로 사용하면 안 됨
- 수종별 기계특성 현지화 필요

# 최종 판정
- 채택
- shallow-landslide root reinforcement의 우선 모델 계보
- ChaMRoots와 역할을 구분하여 사용

# 참고 링크 / DOI
https://doi.org/10.1016/j.geomorph.2012.05.020
