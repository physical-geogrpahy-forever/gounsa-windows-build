# 서지정보
Juez, C., Tena, A., Fernández-Pato, J., Batalla, R. J., & García-Navarro, P. (2018). *Application of a distributed 2D overland flow model for rainfall/runoff and erosion simulation in a Mediterranean watershed*. Cuadernos de Investigación Geográfica, 44(2), 615-640. DOI: 10.18172/cig.3320.

# 이 논문을 찾은 이유
2D dynamic-wave hydrodynamics에 HEM의 rill/interrill erosion coefficients를 실제 유역규모로 결합한 선례가 고운사에 적합한지 확인하기 위해 검토했다.

# 연구 유형
- distributed 2D catchment rainfall-runoff-erosion model
- finite-volume numerical model
- field event calibration/validation

# 공간 구조
- fully 2D dynamic-wave shallow-water equations
- unstructured triangular mesh
- Roe approximate Riemann solver
- about 158,000 cells in the real catchment application

# 적용 환경
- Algars Mediterranean watershed
- mixed agricultural/forested land use
- two storm/flood events

# 핵심 과정
- rainfall/runoff
- SCS-CN losses
- 2D flow
- Hillslope Erosion Model sediment continuity
- interrill erosion
- rill erosion/deposition

# 식생 입력
Land use is translated primarily into:
- Manning roughness
- hydrologic regions/parameters
- locally calibrated erosion parameters

No dynamic root biomass/RLD/litter direct state.

# 핵심 식
2D sediment continuity extends the Hillslope Erosion Model:
```
∂(h phi)/∂t + 2D advective sediment flux
= E_i + E_r
```

where:
- `E_i`: interrill erosion
- `E_r`: net rill erosion or deposition

Parameters:
- `K_i`: interrill erosion coefficient [kg m^-3]
- `K_r`: rill erosion coefficient [m^-1]
- `B`: transport capacity coefficient [kg s^-1 m^-8/3]

Example calibrated values:
event-specific `K_i`, `K_r`, `B` varied substantially.

# 파라미터와 단위
- Ki: kg m^-3
- Kr: m^-1
- B: kg s^-1 m^-8/3
- Manning n
- CN/SCS parameters

# 원 논문의 구현 범위
2D dynamic-wave runoff and HEM erosion are calibrated against discharge and suspended sediment concentration in a real Mediterranean catchment.

# 고운사에 직접 사용할 수 있는 부분
- mature 2D finite-volume catchment routing
- explicit interrill/rill terms
- real watershed calibration precedent

# 새로운 coupling이 필요한 부분
LPJ-GUESS root/litter quantities controlling Ki/Kr would be a **new coupling**.

# 한계
- no morphology update in this study because erosion was assumed not to cause net topographic change
- erosion coefficients strongly calibrated/event dependent
- quantitative vegetation states absent
- SCS-CN hydrology is not preferred for the final Gounsa coupling

# 최종 판정
- **comparison/implementation precedent**
- not preferred final Gounsa engine because morphology and vegetation dynamics are incomplete

# 참고 링크 / DOI
https://doi.org/10.18172/cig.3320
