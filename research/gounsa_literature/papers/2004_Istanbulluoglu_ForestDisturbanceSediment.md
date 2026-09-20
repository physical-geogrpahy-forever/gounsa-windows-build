# 서지정보
Istanbulluoglu, E., Tarboton, D. G., Pack, R. T., & Luce, C. H. (2004). Modeling of the interactions between forest vegetation, disturbances, and sediment yields. *Journal of Geophysical Research: Earth Surface, 109*, F01009.

# 이 논문을 찾은 이유
산불 후 overstory와 understory를 분리해 침식과 사면안정을 연결한 모델을 찾기 위해 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- distributed terrain / drainage routing

# 적용 환경
- 산림 산지
- 교란 후

# 핵심 과정
- 표면침식
- roughness partition
- root cohesion
- sediment yield

# 식생 입력
- overstory tree root cohesion
- understory biomass/roughness

# 핵심 식
유효전단응력 roughness partition 예: `f_s=(n_s/n_t)^1.5`. overstory는 deep root cohesion, understory는 surface resistance 역할.

# 파라미터와 단위
Manning roughness, root cohesion, 회복시간. 구체값은 원문 재확인 필요.

# 원 논문의 구현 범위
상층과 하층 식생을 서로 다른 지형기능으로 분리하고 disturbance/recovery를 모의한다.

# 고운사에 직접 사용할 수 있는 부분
고운사 산불 후 0-100년 천이에서 상층/하층 회복속도 차이를 반영하는 구조.

# 새로운 coupling이 필요한 부분
LPJ-GUESS biomass를 root cohesion/roughness로 변환하는 부분은 새로운 coupling.

# 한계
하층 biomass가 최종적으로 cover/roughness로 매핑된다.

# 최종 판정
- 채택 구조의 핵심 참고

# 참고 링크 / DOI
https://doi.org/10.1029/2003JF000041
