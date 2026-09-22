# 서지정보
Zhang, Y., Zhang, M., Niu, J., Li, H., Xiao, R., Zheng, H., & Bech, J. (2016). Rock fragments and soil hydrological processes: Significance and progress. *CATENA, 147*, 153-166. https://doi.org/10.1016/j.catena.2016.07.012

# 이 논문을 찾은 이유
석력비율과 armour가 infiltration과 soil moisture를 어느 방향으로 바꾸는지 일반화할 수 있는지 검토하기 위해 찾았다.

# 연구 유형
- 종합 리뷰

# 공간 구조
- soil profile
- hillslope hydrology

# 적용 환경
- 다양한 stony soils

# 핵심 과정
- infiltration
- runoff
- evaporation
- soil-water storage
- preferential flow
- rock-fragment architecture

# 식생 입력
- 직접 없음

# 핵심 식
단일 보편식보다 가장 중요한 결론은 rock fragments의 hydrological effect가 양 또는 음으로 모두 나타난다는 점이다.
효과는 cover/content, size, vertical position, morphology, weathering, fine-earth properties 및 topography에 좌우된다.

# 파라미터와 단위
- fragment cover/content
- fragment size
- embeddedness/vertical position
- soil hydraulic properties

# 원 논문의 구현 범위
1960년대 이후 rock fragments와 soil hydrology 연구를 종합하고 RF architecture를 핵심 통제변수로 정리한다.

# 고운사에 직접 사용할 수 있는 부분
- 단일 `armour fraction -> infiltration multiplier`를 피할 근거
- 최소 상태변수로 cover, size distribution, embeddedness/position을 둘 근거
- weathering에 따라 hydrological role도 변할 수 있음을 고려할 근거

# 새로운 coupling이 필요한 부분
고운사 coarse-fragment architecture에서 LPJ-GUESS용 effective soil-water parameters를 산정하는 단계는 **새로운 coupling**이다.

# 한계
리뷰이며 고운사 사암 산불사면 전용 parameterization은 아니다.

# 최종 판정
- 핵심 채택 리뷰

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2016.07.012
