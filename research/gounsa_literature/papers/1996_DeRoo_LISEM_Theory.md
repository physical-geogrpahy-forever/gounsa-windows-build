# 서지정보
De Roo, A. P. J., Wesseling, C. G., & Ritsema, C. J. (1996). LISEM: A single-event physically based hydrological and soil erosion model for drainage basins. I: Theory, input and output. *Hydrological Processes, 10*(8), 1107-1117. https://doi.org/10.1002/(SICI)1099-1085(199608)10:8<1107::AID-HYP415>3.0.CO;2-4

# 이 논문을 찾은 이유
고운사의 매립 석력 토양수문과 runoff erosion을 서로 다른 모델로 임의 결합하지 않고, Richards-equation soil water와 erosion을 하나의 기존 모델 체계에서 계산할 수 있는지 검토하기 위해 찾았다.

# 연구 유형
- physically based distributed hydrology and erosion model
- raster GIS model
- numerical model

# 공간 구조
- raster distributed catchment model
- original routing은 finite-difference kinematic-wave 계열
- 현재 OpenLISEM에서는 2D SWOF dynamic-wave 계열로 확장됨

# 적용 환경
- drainage basin
- rainfall-runoff and erosion events

# 핵심 과정
- rainfall
- interception
- surface depression storage
- infiltration
- vertical soil-water movement
- overland flow
- channel flow
- rainfall/throughfall detachment
- flow detachment
- sediment transport

# 식생 입력
- canopy/interception
- surface cover
- root cohesion 계열은 후속 OpenLISEM에서 입력 가능
- dynamic quantitative root biomass는 기본 모델에 없음

# 핵심 식
vertical water movement는 Richards equation을 푸는 SWATRE를 사용 가능하다.
대안으로 Green-Ampt와 Holtan infiltration도 선택 가능하다.

SWATRE는 토양수분 보존과 Darcy/Richards 구조를 사용한다.

# 파라미터와 단위
- measured water-retention curve theta(h)
- unsaturated hydraulic conductivity K(h)
- soil profile/horizon geometry
- initial matric head
- rainfall/runoff/erosion properties

# 원 논문의 구현 범위
LISEM 안에서 soil water/infiltration과 runoff/erosion을 같은 model execution에 포함한다.

# 고운사에 직접 사용할 수 있는 부분
- stony soil의 measured effective theta-h-K curve를 SWATRE에 직접 넣을 수 있는 LISEM 계보의 기본근거
- 별도 Green-Ampt parameter conversion 없이 Richards-equation soil water를 erosion model과 함께 계산할 수 있음
- 고운사에서 'hydraulic model -> erosion model' 사이 임의 경험식을 만들 필요를 줄임

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation biomass/root/litter state와 LISEM erosion resistance의 연결은 별도 검증이 필요하다.
fire-spall 및 dynamic armour state도 원 LISEM에는 없음.

# 한계
1996 원형의 surface routing은 현재 요구의 genuine 2D solver가 아니므로 현대 OpenLISEM 구현과 함께 사용해야 한다.

# 최종 판정
- 핵심 채택 계보
- OpenLISEM+SWATRE 통합모델 후보의 원 논문

# 참고 링크 / DOI
https://doi.org/10.1002/(SICI)1099-1085(199608)10:8<1107::AID-HYP415>3.0.CO;2-4
