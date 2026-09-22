# 서지정보
Coulthard, T. J., Neal, J. C., Bates, P. D., Ramirez, J., de Almeida, G. A. M., & Hancock, G. R. (2013). Integrating the LISFLOOD-FP 2D hydrodynamic model with the CAESAR model: implications for modelling landscape evolution. *Earth Surface Processes and Landforms, 38*, 1897-1906. https://doi.org/10.1002/esp.3478

# 이 논문을 찾은 이유
고운사에서 2D hydrodynamics와 장기 sediment/armour/topography를 하나의 기존 model로 해결할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- coupled hydrodynamic-landscape evolution model
- model development and comparison

# 공간 구조
- regular raster grid
- LISFLOOD-FP reduced shallow-water 2D routing
- CAESAR geomorphic state update

# 핵심 과정
- nonsteady 2D flow
- sediment transport
- erosion/deposition
- topographic evolution
- active-layer sediment grading lineage

# 적용범위
- reach and catchment landscape evolution
- event to long-term morphodynamics

# 고운사에 사용할 수 있는 부분
- 2D hydrodynamics + morphodynamics를 하나의 existing codebase에서 구현
- long-term DEM evolution
- multiclass active-layer architecture

# 고운사에 부족한 부분
- quantitative root biomass/RLD
- litter biomass dynamics
- PFT-specific erosion resistance
- explicit stony-soil Richards hydrology

# 최종 판정
- **single-engine comparator**
- armour/profile component는 추가 정밀 비교 가치 높음
- vegetation-root requirement 때문에 현재 production 전체모델로 확정하지 않음

# 참고 링크
https://doi.org/10.1002/esp.3478
https://zenodo.org/records/321820
https://sourceforge.net/projects/caesar-lisflood/
