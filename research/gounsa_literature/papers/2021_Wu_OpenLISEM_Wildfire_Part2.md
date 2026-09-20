# 서지정보
Wu, J., Baartman, J. E. M., & Nunes, J. P. (2021). *Testing the impacts of wildfire on hydrological and sediment response using the OpenLISEM model. Part 2: Analyzing the effects of storm return period and extreme events*. Catena, 207, 105620. DOI: 10.1016/j.catena.2021.105620.

# 이 논문을 찾은 이유
OpenLISEM wildfire application에서 storm severity와 postfire erosion source 변화까지 확인하기 위해 검토했다.

# 연구 유형
- distributed numerical-model application

# 공간 구조
- OpenLISEM spatially explicit catchment model

# 적용 환경
- burned catchment, southern Portugal
- forest/natural upper slopes and cropland

# 핵심 과정
- wildfire hydrologic response
- splash erosion
- runoff erosion
- sediment source shift
- extreme rainfall

# 식생 입력
동적 root biomass/RLD 직접입력은 확인되지 않았고 fire/land-cover parameterization 중심.

# 핵심 식
Part 1/OpenLISEM 계보 파일 참조.

# 파라미터와 단위
storm return period and model parameterization. exact tables are retained in original paper.

# 원 논문의 구현 범위
pre/post-fire storm response and erosion-source redistribution.

# 고운사에 직접 사용할 수 있는 부분
postfire erosion이 splash/runoff components와 rainfall severity에 따라 달라질 수 있음을 보여주는 model-application precedent.

# 새로운 coupling이 필요한 부분
LPJ-GUESS dynamic vegetation quantities와 직접 연결하면 **새로운 coupling**.

# 한계
strict quantitative root/litter state requirement 미충족.

# 최종 판정
**보조근거.**

# 참고 링크 / DOI
10.1016/j.catena.2021.105620
