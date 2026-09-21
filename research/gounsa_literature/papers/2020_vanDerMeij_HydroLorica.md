# 서지정보
van der Meij, W. M., Temme, A. J. A. M., Wallinga, J., & Sommer, M. (2020). *Modeling soil and landscape evolution: The effect of rainfall and land-use change on soil and landscape patterns*. SOIL, 6, 337-358. DOI: 10.5194/soil-6-337-2020.

# 이 논문을 찾은 이유
Pelletier보다 작은 hydrologic timestep을 가진 soil-landscape model이 100년 고운사에서 forest/grassland, creep, tree throw와 weathering을 직접 대체할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- reduced-complexity soil-landscape evolution model
- raster numerical model

# 공간 구조
- DEM raster
- multiple soil layers per raster cell
- spatial water routing
- lateral soil transport

# 적용 환경
- natural forest/grassland
- agricultural land-use transition
- long-term soil-landscape evolution

# 핵심 과정
- daily/monthly/yearly hydrology
- water erosion/deposition
- creep
- bioturbation
- tree throw
- clay translocation
- organic matter
- vegetation-type feedback

# 식생 입력
- forest / grassland / arable vegetation class
- vegetation determined from water availability
- not quantitative LPJ-GUESS cohorts/biomass

# 시간간격
HydroLorica uses **dynamic hydrologic timesteps**:
- daily
- monthly
- yearly
with smaller timesteps in wetter periods.

However, annual sums of infiltration and overland flow drive the geomorphic/pedogenic processes.

More importantly, the authors explicitly state that their simplified vegetation type can change annually because succession/resilience are omitted, and that the vegetation distribution should be interpreted only after aggregation over >100 years.

They explicitly warn that the vegetation implementation:
```
should not be used to study systems on annual to decadal timescales
```

Therefore small hydrologic timesteps do **not** make HydroLorica a suitable direct dynamic vegetation model for Gounsa's 100-year postfire succession.

# 핵심 구조
Texture/soil-state changes are decomposed among:
- chemical/physical soil formation
- water erosion
- tree throw
- tillage
- clay translocation
- bioturbation

Surface-water routing is spatial and the annual surface-flow total drives erosion/deposition.

Tree throw is treated stochastically; the example uses about:
```
0.2 trees ha^-1 yr^-1
```
for its study setting.

# 고운사에 직접 사용할 수 있는 부분
- useful architecture for separating creep, tree throw, water erosion and vertical mixing
- dynamic hydrologic timestep precedent
- raster soil-layer bookkeeping precedent

# 새로운 coupling이 필요한 부분
Replacing forest/grassland classes with LPJ-GUESS cohort states would be a major new coupling.

# 한계
- vegetation module intentionally too simple for annual-decadal ecological transitions
- long simulations: 14,500-year natural phase + 500-year agricultural phase
- not a postfire succession model
- biomass/root-state coupling absent

# 최종 판정
**보조 구조근거, not primary 100-year Gounsa process model.**

The paper is a useful warning that a short hydrologic timestep alone does not guarantee a model is appropriate at annual ecological timescales.

# 참고 링크 / DOI
https://doi.org/10.5194/soil-6-337-2020


## 2026-09-21 hillslope-weathering re-audit

추가 원문 검토에서 HydroLorica의 중요한 장점은:
```
spatial water balance
 -> local infiltration
 -> infiltration-dependent pedogenesis
```
구조임을 다시 확인했다.

따라서 고운사에 직접 쓸 수 있는 구조적 선례:
- 사면 위치별 infiltration 차이
- surface water routing
- soil-layer bookkeeping
- hydrology-dependent pedogenesis

하지만 current production에서 사용하지 않는 항:
- tree throw
- simplified annual forest/grass succession state

특히 저자들이 vegetation implementation을 annual-decadal study에 쓰지 말라고 명시하므로, 고운사 vegetation은 반드시 LPJ-GUESS가 담당한다.

현재 역할:
```
HydroLorica
= hydrology-dependent pedogenesis / soilscape architecture reference

NOT
= vegetation engine
```

관련 최신 decision에서는 tree throw를 제외한 infiltration/pedogenesis 구조만 참고한다.
