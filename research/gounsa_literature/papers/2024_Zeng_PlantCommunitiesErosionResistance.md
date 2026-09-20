# 서지정보
Zeng, R., Zhang, G., Su, X., & Wang, C. (2024). Soil erosion resistance of gully system under different plant communities on the Loess Plateau of China. Earth Surface Processes and Landforms, 49(6), 1748-1761. https://doi.org/10.1002/esp.5795

# 이 논문을 찾은 이유
grass, shrub, forest가 같은 flowing-water 조건에서 rill detachment와 erodibility에 서로 다른 효과를 주는지 확인하기 위해 검토했다.

# 연구 유형
- 현장/실험
- concentrated-flow detachment test

# 공간 구조
- plot/sample scale

# 적용 환경
- gully system
- grass, shrub, forest communities

# 핵심 과정
- soil detachment capacity
- rill erodibility
- critical shear stress

# 식생 입력
- plant community
- root mass density
- biological soil crust thickness
- soil cohesion
- water-stable aggregates

# 핵심 식
현재 채팅에서 확인한 정량관계:
Dc(grass) 약 0.15 * Dc(forest)
Dc(shrub) 약 0.37 * Dc(forest)
rill erodibility는 cohesion, aggregate stability, RMD 증가에 따라 감소하고 critical shear stress는 cohesion과 RMD 증가에 따라 증가했다.

# 파라미터와 단위
critical shear stress는 Pa. 나머지 세부회귀식과 단위는 원문 재검증 필요.

# 원 논문의 구현 범위
동일 지역에서 서로 다른 plant community의 soil erosion resistance를 직접 비교한다.

# 고운사에 직접 사용할 수 있는 부분
forest biomass 증가가 erosion resistance의 단조증가를 의미하지 않는다는 강한 반례. PFT/root traits와 soil structure를 함께 봐야 한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS PFT별 root mass와 soil aggregate/cohesion을 erodibility로 연결하는 것은 새로운 coupling이다.

# 한계
수치모델이 아니라 실험연구이고 Loess Plateau 계수를 고운사에 직접 적용할 수 없다.

# 최종 판정
- 보조근거
- PFT별 유수침식 계수 설정에 매우 중요

# 참고 링크 / DOI
https://doi.org/10.1002/esp.5795
