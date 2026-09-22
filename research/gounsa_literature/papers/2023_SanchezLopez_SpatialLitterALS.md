# 서지정보
Sánchez-López, N., Hudak, A. T., Boschetti, L., Silva, C. A., Robertson, K., Loudermilk, E. L., Bright, B. C., Callaham, M. A., & Taylor, M. (2023). A spatially explicit model of tree leaf litter accumulation in fire maintained longleaf pine forests of the southeastern US. Ecological Modelling, 481, 110369. DOI: 10.1016/j.ecolmodel.2023.110369

# 이 논문을 찾은 이유
HETEROFOR 또는 다른 개체목 식생모델의 연간 litterfall을 LiDAR 기반 1-5 m 지형격자에 어떻게 공간적으로 분배할지 published method를 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- ALS/LiDAR 기반 spatial litter model
- 산불 후 litter accumulation

# 공간 구조
- individual tree crowns from ALS segmentation
- litter maps at 5 m x 5 m
- wall-to-wall spatial distribution

# 적용 환경
- fire-maintained longleaf pine forests
- southeastern USA
- repeated prescribed fire

# 핵심 과정
- foliage biomass estimation
- annual leaf litter production
- litter deposition
- decomposition
- time since fire
- residual litter after fire

# 식생 입력
- crown objects from ALS
- foliage biomass
- leaf turnover/lifespan
- annual litterfall
- fire history
- AET/climate-related decomposition

# 핵심 식
Spatial Olson accumulation:
```
B_x(t)
= (L_x / k_x) * [1 - exp(-k_x (t - T0_x))]
  + B0_x * exp(-k_x (t - T0_x))
```

- B_x(t): litter biomass at pixel x
- L_x: annual litter production
- k_x: decomposition rate
- T0_x: last-fire timing
- B0_x: residual unburned litter immediately after fire

# 파라미터와 단위
- resolution: 5 m
- litter biomass: kg m-2
- annual production: kg m-2 yr-1
- decomposition: yr-1

# 원 논문의 구현 범위
LiDAR crown structure and fire history from remote sensing are used to create spatially and temporally explicit litter maps.

# 고운사에 직접 사용할 수 있는 부분
Very strong interface:
```
HETEROFOR individual-tree leaf litterfall
+ LiDAR crown footprint
 -> 1-5 m litterfall raster
 -> postfire accumulation/decomposition
 -> Iber rainfall-detachment protection / roughness
```

This avoids collapsing litter mass into a single stand-level vegetation-cover factor.

# 새로운 coupling이 필요한 부분
- Korean deciduous/conifer litterfall traits
- HETEROFOR litter output to spatial crown deposition kernel
- slope-driven lateral litter movement after deposition
- litter -> erosion resistance/protection

# 한계
longleaf-pine/fire-maintained system에서 검증되었다. fine-root litter는 surface-litter map으로 보내면 안 된다. root litter remains belowground.

# 최종 판정
- 채택 후보: spatial surface-litter helper
- 주 식생모델이 아니라 HETEROFOR-LiDAR-geomorph interface 근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.ecolmodel.2023.110369
