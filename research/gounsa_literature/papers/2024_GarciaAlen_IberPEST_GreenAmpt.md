# 서지정보
García-Alén, G., Montalvo, C., Cea, L., & Puertas, J. (2024). Iber-PEST: Automatic calibration in fully distributed hydrological models based on the 2D shallow water equations. *Environmental Modelling & Software, 177*, 106047. https://doi.org/10.1016/j.envsoft.2024.106047

# 이 논문을 찾은 이유
Iber+ Green-Ampt가 실제로 요구하는 입력을 정확히 확인하여 GEM/HYDRUS stony-soil hydraulic properties와 임의 변환 없이 연결 가능한지 판정하기 위해 검토했다.

# 연구 유형
- Iber+ hydrological model
- automatic calibration framework
- 2D-SWE

# 공간 구조
- fully distributed 2D unstructured mesh

# 적용 환경
- two catchments in NW Spain
- eight storm events

# 핵심 과정
- rainfall
- Green-Ampt infiltration
- 2D overland flow
- calibration

# 식생 입력
- Manning/land-use parameters
- dynamic vegetation 없음

# 핵심 식
Iber Green-Ampt 구현은 6개 입력을 명시한다.
1. total soil-layer thickness ds
2. soil porosity phi
3. initial soil saturation Sr,0
4. saturated hydraulic conductivity/permeability ks
5. soil suction psi
6. initial losses Ia

논문의 특정 case study에서는 일부 값을 고정하고 Sr,0, ks, Ia 등을 calibration했지만 그 수치는 해당 유역 사례값이며 고운사에 이식하지 않는다.

# 파라미터와 단위
- ds: length
- phi: volumetric fraction
- Sr,0: saturation ratio
- ks: length/time
- psi: length
- Ia: rainfall-depth equivalent

# 원 논문의 구현 범위
Iber+ native Green-Ampt parameter structure를 명확히 문서화한다.

# 고운사에 직접 사용할 수 있는 부분
stony-soil hydraulic properties와 다음처럼 직접 대응 가능하다.
- ks <- measured/effective Ksat
- phi <- effective saturated volumetric water capacity/porosity
- Sr,0 <- initial effective water content / phi
- ds <- measured soil depth
- psi <- published Green-Ampt wetting-front relation에서 K(h)/WRC로 산정
- Ia <- 별도 surface storage/interception으로 관측 또는 명시적으로 0 처리할 조건을 정의

# 새로운 coupling이 필요한 부분
parameter files를 생성하는 workflow는 새로운 software coupling이나 새 경험식은 필요하지 않는다.

# 한계
Green-Ampt는 sharp wetting-front approximation이며 full WRC/HCC를 시간적 Richards solution으로 그대로 쓰지는 않는다.

# 최종 판정
- 핵심 채택
- GEM/HYDRUS -> Iber Green-Ampt interface의 정확한 target definition

# 참고 링크 / DOI
https://doi.org/10.1016/j.envsoft.2024.106047
