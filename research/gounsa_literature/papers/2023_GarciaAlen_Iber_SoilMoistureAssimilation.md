# 서지정보
García-Alén, G., Hostache, R., Cea, L., & Puertas, J. (2023). Joint assimilation of satellite soil moisture and streamflow data for the hydrological application of a two-dimensional shallow water model. *Journal of Hydrology, 621*, 129667. https://doi.org/10.1016/j.jhydrol.2023.129667

# 이 논문을 찾은 이유
Iber+가 soil moisture를 상태변수로 다루며 Green-Ampt infiltration을 어떤 방식으로 hydrological application에 쓰는지 확인하기 위해 검토했다.

# 연구 유형
- fully distributed hydrological-hydrodynamic modeling
- data assimilation
- Iber+ 2D-SWE

# 공간 구조
- 2D unstructured mesh
- catchment scale

# 적용 환경
- NW Spain, 199 km2 catchment
- 12 storm events

# 핵심 과정
- rainfall-runoff
- Green-Ampt infiltration
- soil moisture
- streamflow
- data assimilation

# 식생 입력
- land-use roughness 등
- dynamic vegetation model은 아님

# 핵심 식
Iber+ 2D SWE에 rainfall과 infiltration source/sink를 포함하고 Green-Ampt를 이용한다.
soil moisture와 discharge를 동시에 assimilation하여 parameter/state plausibility를 개선한다.

# 파라미터와 단위
Iber Green-Ampt 구조는 후속 Iber-PEST 논문에서 명확히 정리됨:
- soil depth ds
- porosity phi
- initial saturation Sr,0
- saturated hydraulic conductivity/permeability ks
- suction psi
- initial abstraction Ia

# 원 논문의 구현 범위
Iber+를 단순 flood-routing이 아니라 soil-moisture-aware hydrological model로 사용한 published precedent.

# 고운사에 직접 사용할 수 있는 부분
- spatial soil moisture state와 2D runoff를 Iber+ 안에서 함께 처리하는 근거
- measured/remote soil moisture를 초기상태 검증에 사용할 근거

# 새로운 coupling이 필요한 부분
stony-soil effective WRC/HCC에서 Iber Green-Ampt parameter를 생성하는 것은 별도 published relation을 이용한 coupling이 필요하다.

# 한계
고석력 산림토양 전용 연구가 아니고 event-based storm simulations이다.

# 최종 판정
- 핵심 Iber hydrology 근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.jhydrol.2023.129667
