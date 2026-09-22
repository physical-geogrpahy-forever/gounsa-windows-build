# 서지정보
Kruse, S., Stuenzi, S. M., Boike, J., Langer, M., Gloy, J., & Herzschuh, U. (2022). Novel coupled permafrost-forest model (LAVESI-CryoGrid v1.0) revealing the interplay between permafrost, vegetation, and climate across eastern Siberia. Geoscientific Model Development, 15, 2395-2422. DOI: 10.5194/gmd-15-2395-2022

# 이 논문을 찾은 이유
지형 및 토양상태와 명시적 개체목 공간모델을 양방향 결합한 선례가 고운사 구조에 도움이 되는지 검토했다.

# 연구 유형
- 수치모델 coupling
- 공간명시적 개체기반 산림모델 + 토양열수문모델

# 공간 구조
- LAVESI 개별 나무와 종자의 x,y 위치 명시
- environment grid 0.2 m x 0.2 m
- CryoGrid는 1D column ensemble로 결합
- LAVESI update는 yearly

# 적용 환경
- 동시베리아 permafrost larch forest
- treeline and forest dynamics

# 핵심 과정
- seed dispersal
- establishment
- growth
- competition
- mortality
- litter-layer height
- soil thermal/hydrological feedback

# 식생 입력/상태
- tree density
- LAI
- SAI
- tree height
- litter-layer height
- soil moisture
- 개별목/종자 위치
- 정량 fine-root biomass pool은 LAVESI 핵심 상태로 확인되지 않음

# 핵심 식
LAVESI의 annual forest state를 CryoGrid에 전달하고 CryoGrid의 토양 열수문 상태를 다시 식생에 전달하는 양방향 coupling architecture가 핵심이다.

# 파라미터와 단위
- environment grid: 0.2 m
- vegetation update: yearly
- litter-layer height: cm

# 원 논문의 구현 범위
산림과 permafrost thermo-hydrology의 양방향 피드백.

# 고운사에 직접 사용할 수 있는 부분
- 공간명시적 개체목과 soil-state model의 coupling 선례
- soil moisture/active layer 등 물리환경이 식생 정착과 생장에 피드백하는 구조
- litter layer의 공간 상태화

# 새로운 coupling이 필요한 부분
- temperate forest species
- fine/coarse root biomass
- 지형침식과 soil depth
- 산불 후 root mortality
- litter mass와 erosion protection

# 한계
모델 생태계가 permafrost larch에 특화되어 있고, root biomass/turnover를 고운사 지형모델에 직접 넘길 상태량이 부족하다.

# 최종 판정
- 보조근거
- coupling architecture 참고
- 주 식생모델 후보로는 부적합

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-15-2395-2022
