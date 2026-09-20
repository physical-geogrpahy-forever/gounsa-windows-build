# 서지정보
Wei, S., Zhang, K., Liu, C., Cen, Y., Xia, J., et al. (2024). Effects of different vegetation components on soil erosion and response to rainfall intensity under simulated rainfall. *CATENA, 235*, 107652.

# 이 논문을 찾은 이유
canopy, roots, litter의 침식저감 기여를 분리한 최신 실험근거로 검토했다.

# 연구 유형
- simulated-rainfall experiment

# 공간 구조
- plot

# 적용 환경
- grass vegetation components

# 핵심 과정
- runoff
- sediment
- flow velocity

# 식생 입력
- canopy
- roots
- litter

# 핵심 식
기관별 처리구를 분리해 contribution을 산정. 이 채팅 정리에는 canopy contribution이 velocity 약 11.4%, runoff 약 8.0%, sediment 약 7.3%로 기록됨.

# 파라미터와 단위
rainfall intensity 60, 90, 120 mm h^-1.

# 원 논문의 구현 범위
식생기관별 침식제어효과를 실험적으로 분리.

# 고운사에 직접 사용할 수 있는 부분
기관별 biomass pool을 서로 다른 물리경로로 처리해야 한다는 근거.

# 새로운 coupling이 필요한 부분
LeafC, FineRootC, LitterC를 각 hydraulic/erodibility 항에 연결하면 새로운 coupling.

# 한계
수치모델 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2023.107652
