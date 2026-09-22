# 서지정보
de Vries, J., Meijers, E., Vos, M. A. E., & Sterck, F. J. (2026). Spatial and physiological detail in crown representation matters when simulating tree growth. Ecological Modelling, 511, 111358. DOI: 10.1016/j.ecolmodel.2025.111358

# 이 논문을 찾은 이유
LiDAR와 직접 맞는 초세밀 수관구조를 가진 최신 spatially explicit individual-based model이 고운사 100년 산불 후 천이를 대신할 수 있는지 검토했다.

# 연구 유형
- 수치모델
- spatially explicit individual tree ecophysiology

# 공간 구조
- stems and leaves explicitly located in 3D
- leaf-level radiative transfer
- GroImp platform

# 적용 환경
- 네덜란드 산림
- Pseudotsuga menziesii
- Pinus sylvestris
- Fagus sylvatica

# 핵심 과정
- canopy structure
- leaf physiology
- microclimate
- individual tree growth

# 식생 입력
- individual tree structure
- explicit leaves/stems
- physiological traits

# 핵심 식
광선추적 기반 leaf-level radiation과 생리과정을 결합해 개체목 생장을 예측한다.

# 파라미터와 단위
- crown/leaf explicit 3D geometry
- multiannual growth validation

# 원 논문의 구현 범위
수관 공간구조와 생리 상세도가 생장예측에 미치는 효과를 평가한다.

# 고운사에 직접 사용할 수 있는 부분
- LiDAR-based crown structure benchmark
- aboveground canopy process validation

# 새로운 coupling이 필요한 부분
- regeneration
- mortality
- seed dispersal
- root biomass/turnover
- litter/deadwood
- wildfire/postfire succession
- geomorphic soil feedback

# 한계
논문이 연구목적상 장기 vegetation dynamics인 regeneration과 mortality를 의도적으로 제외한다. 따라서 산불 후 100년 천이의 주 모델로 사용할 수 없다.

# 최종 판정
- 탈락: 주 식생엔진
- 보조근거: LiDAR 수관구조 및 광환경 benchmark

# 참고 링크 / DOI
https://doi.org/10.1016/j.ecolmodel.2025.111358
