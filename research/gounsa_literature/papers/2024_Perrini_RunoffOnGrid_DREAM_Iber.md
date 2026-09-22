# 서지정보
Perrini, P., Cea, L., et al. (2024). A Runoff-On-Grid Approach to Embed Hydrological Processes in Shallow Water Models. *Water Resources Research*. https://doi.org/10.1029/2023WR036421

# 이 논문을 찾은 이유
고운사에서 full soil-hydrology model과 Iber+ 2D surface-flow/erosion engine을 연결할 때 Green-Ampt로 모든 subsurface physics를 축약하지 않고, 별도 process-based hydrological model 출력을 Iber+로 넘기는 published coupling architecture가 있는지 확인하기 위해 검토했다.

# 연구 유형
- coupled distributed hydrological-hydrodynamic modeling
- DREAM + Iber+

# 공간 구조
- DREAM raster hydrology
- Iber+ unstructured 2D SWE mesh

# 적용 환경
- Crotone, Italy catchment flood hindcast
- vegetated/semi-humid catchment application

# 핵심 과정
- antecedent soil moisture
- infiltration excess
- saturation excess
- evapotranspiration/interception/storage
- distributed total runoff generation
- 2D surface routing

# 식생 입력
- DREAM land use / vegetation parameters
- dynamic ecological model은 아님

# 핵심 식
핵심은 새 infiltration식을 만드는 것이 아니라 hydrological model이 시간별 공간분포 total runoff를 계산하고, 이를 Iber+ 2D mass-conservation equation의 source term으로 전달하는 것이다.

```
distributed hydrological model
 -> R_tot(x,y,t)
 -> Iber+ 2D SWE source term
 -> 2D routing/hydrodynamics
```

# 파라미터와 단위
- distributed runoff depth/rate
- soil-water state
- rainfall
- Iber mesh/source terms

# 원 논문의 구현 범위
DREAM의 subsurface/topsoil hydrology와 Iber+의 2D routing을 명시적으로 분리하여 coupling했다.
저자들은 이 Runoff-On-Grid 방법이 DREAM-Iber에만 한정된 구조가 아니라고 명시한다.

# 고운사에 직접 사용할 수 있는 부분
- HYDRUS/Richards 또는 다른 stony-soil hydrology와 Iber+를 역할분담시키는 published architectural precedent
- Green-Ampt event loss model로 full soil-moisture dynamics를 축약하지 않고 2D erosion engine을 유지할 수 있는 경로

# 새로운 coupling이 필요한 부분
HYDRUS 또는 LPJ-GUESS soil hydrology를 DREAM 대신 Iber+에 연결하는 것은 **새로운 coupling**이다.
그러나 interface variable은 published 구조와 동일하게 distributed runoff source이다.

# 한계
- 실제 논문은 DREAM-Iber coupling이며 HYDRUS-Iber가 아님
- 단일 홍수 hindcast 중심
- erosion/sediment feedback은 이 논문의 주목적이 아님

# 최종 판정
- 핵심 coupling-architecture 근거
- 장기 soil moisture feedback까지 중요할 경우 Green-Ampt direct coupling보다 더 물리적인 대안

# 참고 링크 / DOI
https://doi.org/10.1029/2023WR036421
