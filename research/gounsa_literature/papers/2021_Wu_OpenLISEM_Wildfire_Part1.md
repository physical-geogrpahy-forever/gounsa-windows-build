# 서지정보
Wu, J., Nunes, J. P., Baartman, J. E. M., & Faúndez Urbina, C. A. (2021). *Testing the impacts of wildfire on hydrological and sediment response using the OpenLISEM model. Part 1: Calibration and evaluation for a burned Mediterranean forest catchment*. Catena, 207, 105658. DOI: 10.1016/j.catena.2021.105658.

# 이 논문을 찾은 이유
OpenLISEM이 실제 burned forest catchment에 적용 가능한 spatial erosion framework인지 확인하기 위해 검토했다.

# 연구 유형
- physically based distributed model application

# 공간 구조
- spatially distributed OpenLISEM
- meso-scale catchment 18.5 km2
- OpenLISEM의 2D flow option/erosion framework 계보

# 적용 환경
- burned Mediterranean forest catchment
- southern Portugal

# 핵심 과정
- runoff
- infiltration
- splash erosion
- flow erosion
- sediment transport/deposition
- pre/post wildfire parameterization

# 식생 입력
이 채팅에서 코드까지 확인한 OpenLISEM 구조는 root cohesion map을 받을 수 있으나 현재 구현은
```
CohesionSoil = Cohesion + Cover * RootCohesion
```
계열이며 root biomass/RLD에서 동적으로 계산하지 않는다.
본 wildfire application도 land-use/fire-state parameterization 중심이다.

# 핵심 식
OpenLISEM 상세 erosion equation은 model 계보 파일에서 관리한다.

# 파라미터와 단위
논문은 burned-area용 roughness, Manning n, Ksat, d50 등의 parameter ratios를 제시한다.

# 원 논문의 구현 범위
burned Mediterranean forest catchment의 event runoff와 sediment response.

# 고운사에 직접 사용할 수 있는 부분
- 산불 산림 유역에 OpenLISEM을 실제 적용한 선례
- spatial hydrology-erosion framework의 검증 근거

# 새로운 coupling이 필요한 부분
LPJ-GUESS root biomass/RLD를 OpenLISEM root cohesion으로 동적 변환하면 **새로운 coupling**.

# 한계
- root cohesion은 quantity-based dynamic vegetation state가 아님
- cover weighting이 남아 있어 strict 조건 미충족

# 최종 판정
**보조근거.** 산불 산지 적용 선례는 강하지만 quantitative vegetation 조건에서는 탈락.

# 참고 링크 / DOI
10.1016/j.catena.2021.105658
