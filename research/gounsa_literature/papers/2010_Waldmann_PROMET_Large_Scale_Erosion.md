# 서지정보
Waldmann, D. (2010). *Large-Scale Process-Oriented Modelling of Soil Erosion by Water in Complex Watersheds*. Dissertation, Ludwig-Maximilians-Universität München. DOI: 10.5282/edoc.11575.

관련 논문: Waldmann, D., & Mauser, W., *Large-scale modelling of soil erosion by water and potential Global Change impacts in the Upper Danube basin*. 정확한 journal/proceedings 서지는 **원문 재검증 필요**.

# 이 논문을 찾은 이유
PROMET/DANUBIA 계보에서 dynamic vegetation model이 root length density를 erosion resistance에 직접 전달하는지 확인하기 위해 검토했다.

# 연구 유형
- process-oriented distributed numerical model
- dissertation/model development

# 공간 구조
- PROMET proxel grid, Upper Danube basin
- erosion component spatial resolution 약 1 km2, temporal resolution 1 h
- 각 proxel sediment/runoff를 channel network로 전달
- genuine 2D shallow-water surface routing은 아님

# 적용 환경
- Upper Danube basin
- Alpine/mountain watershed 포함

# 핵심 과정
- rainfall/runoff erosion
- distributed hydrology
- vegetation/soil parameter dynamics
- sediment delivery to channel network

# 식생 입력
PROMET biological module에서 동적으로 계산된 root length density(RLD)가 erosion module의 root reinforcement/erosion resistance에 전달되는 구조를 검토했다.

# 핵심 식
이 채팅에서 확인된 대표 coupling은 root-density effect를 exponential soil-erosion parameter reduction/soil cohesion increase로 사용하는 계열이다.
원 논문의 정확한 final implementation 식은 dissertation 식 번호를 기준으로 재확인한다.

PROMET biological module은 root biomass growth에서 root length increment를 산출하고 토층별 RLD를 동적으로 갱신한다.

# 파라미터와 단위
- RLD: root length density
- root senescence rate
- soil cohesion/erosion resistance parameters
정확한 식별자와 단위는 dissertation 원문 기준.

# 원 논문의 구현 범위
dynamic vegetation and hydrology from PROMET를 erosion component에 전달해 Upper Danube에서 large-scale erosion을 계산한다.

# 고운사에 직접 사용할 수 있는 부분
- **dynamic vegetation -> RLD -> erosion resistance**의 실제 model implementation 선례
- LPJ-GUESS FineRootC/RLD coupling을 설계할 때 중요한 근거

# 새로운 coupling이 필요한 부분
PROMET RLD formulation을 LPJ-GUESS에 이식하거나 genuine 2D erosion engine에 적용하면 **새로운 coupling**.

# 한계
- genuine 2D surface flow가 아님
- 1 km2 proxel scale
- 각 proxel이 channel network로 직접 sediment를 보내는 구조여서 local hillslope routing과 다름

# 최종 판정
**채택: quantitative root-state -> erosion resistance 선례.**
2D engine 후보는 아님.

# 참고 링크 / DOI
10.5282/edoc.11575
