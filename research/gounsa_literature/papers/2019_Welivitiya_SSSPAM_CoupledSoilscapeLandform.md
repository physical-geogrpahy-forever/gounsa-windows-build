# 서지정보
Welivitiya, W. D. D. P., Willgoose, G. R., & Hancock, G. R. (2019). *A coupled soilscape–landform evolution model: model formulation and initial results*. Earth Surface Dynamics, 7, 591-607. DOI: 10.5194/esurf-7-591-2019.

# 이 논문을 찾은 이유
Pelletier 2013보다 직접적으로 soil profile, physical weathering, diffusion/erosion/deposition과 evolving landform을 함께 계산하는 모델이 있는지 확인하고, 100년 고운사 soil/weathering module의 대안 가능성을 평가하기 위해 검토했다.

# 연구 유형
- process-based numerical soilscape-landform evolution model
- state-space matrix pedogenesis + landform evolution

# 공간 구조
- DEM-based landform
- multilayer soil profile at each node/cell
- linear-hillslope test in the paper
- evolving elevation, slope, contributing area and soil grading

# 적용 환경
- generic hillslope / soilscape evolution
- developed largely from post-mining/pedogenesis modeling lineage

# 핵심 과정
- fluvial erosion
- deposition
- physical weathering
- surface armouring
- profile particle-size evolution
- landform elevation change
- coupled soil-landform feedback

# 식생 입력
Dynamic vegetation/root biomass is absent.

The 2019 formulation explicitly notes that soil organic carbon and vegetation/decomposition coupling are not yet represented.

# 핵심 구조
SSSPAM tracks the particle-size distribution through the soil profile and the sediment grading in transport.

At every model step:
```
erosion/deposition
 -> soil grading change
 -> elevation change
 -> topographic attributes change
 -> next erosion/weathering response
```

Weathering is represented through depth-dependent physical fragmentation functions.

# 파라미터와 단위
- layer particle-size distributions
- physical weathering rates
- depth-dependent weathering function
- erosion/deposition transition matrices
- DEM slope/contributing area

Exact site coefficients require model-specific calibration.

# 원 논문의 구현 범위
This is a genuine coupled soil-profile + landform model, not merely a fixed soil-production function.

However the weathering is **physical fragmentation**, not chemical weathering.

# 고운사에 직접 사용할 수 있는 부분
Important comparison for:
- physical soil/regolith profile bookkeeping
- coarse-fragment evolution
- armouring
- depth-dependent weathering
- coupling physical weathering to changing topography

Potentially useful later for the Gounsa:
```
coarse-fragment supply <-> armour
```
problem.

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation/root state -> SSSPAM weathering parameters would be a new coupling.

Using SSSPAM physical-weathering/profile state alongside SWEHR would also require state reconciliation because both models can alter surface sediment grading/elevation.

# 한계
- no dynamic vegetation
- no root fracture/tree throw
- no chemical transformations in the 2019 formulation
- not postfire forest
- overlapping erosion/armouring state with SWEHR could complicate coupling

# 최종 판정
**Strong comparison / possible physical-profile module, not first-choice Gounsa core.**

For the first implementation, Gabet-Mudd + Roering + SWEHR give a cleaner process separation with LPJ-GUESS.

# 참고 링크 / DOI
https://doi.org/10.5194/esurf-7-591-2019
