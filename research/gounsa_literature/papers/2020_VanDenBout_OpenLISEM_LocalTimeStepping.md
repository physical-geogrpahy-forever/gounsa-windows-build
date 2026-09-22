# 서지정보
Van den Bout, B., & Jetten, V. G. (2020). Catchment-scale multi-process modeling with local time stepping. *Environmental Earth Sciences, 79*(8), 184. https://doi.org/10.1007/s12665-020-08914-7

# 이 논문을 찾은 이유
현대 OpenLISEM이 2D surface hydrodynamics, infiltration/soil water 및 여러 지표과정을 실제로 통합하는지 검토하기 위해 찾았다.

# 연구 유형
- numerical model development
- multi-process catchment model
- OpenLISEM

# 공간 구조
- catchment-scale raster
- MUSCL-based 2D surface flow extension
- local time stepping

# 적용 환경
- flash-flood and multi-process catchments

# 핵심 과정
- rainfall-runoff
- infiltration
- 2D surface flow
- soil water
- slope stability/runout in multi-hazard extension

# 식생 입력
- land-cover/roughness and hydrological properties
- dynamic LPJ-GUESS vegetation state는 아님

# 핵심 식
OpenLISEM은 여러 infiltration option을 제공하며, full vertical soil-water balance에는 SWATRE를 사용한다.
SWATRE는 Richards-equation 계열이다.
논문의 계산사례는 Green-Ampt를 사용하지만 SWATRE가 model option으로 명시되어 있다.

2D surface flow는 TVD/MUSCL 계열 수치해법을 사용한다.

# 파라미터와 단위
- Ksat 또는 full soil hydraulic profile depending infiltration option
- soil moisture
- surface water depth
- velocity/discharge
- topographic and roughness parameters

# 원 논문의 구현 범위
OpenLISEM의 hydrology/flooding/multi-process 구조와 현대 2D 계산체계를 보여준다.

# 고운사에 직접 사용할 수 있는 부분
- SWATRE soil water와 2D surface hydrodynamics가 동일 OpenLISEM framework에 공존한다는 peer-reviewed 근거
- 별도 DREAM/HYDRUS-Iber software coupling을 피할 수 있는 모델 기반

# 새로운 coupling이 필요한 부분
LPJ-GUESS root/litter dynamics, fire-spall production, dynamic coarse armour evolution은 별도이다.

# 한계
이 논문의 demonstration 자체는 Green-Ampt를 사용하며, SWATRE+2D+erosion 조합을 고운사와 동일 조건에서 검증한 연구는 아니다.

# 최종 판정
- 핵심 채택
- 현대 OpenLISEM integrated framework의 peer-reviewed 근거

# 참고 링크 / DOI
https://doi.org/10.1007/s12665-020-08914-7
