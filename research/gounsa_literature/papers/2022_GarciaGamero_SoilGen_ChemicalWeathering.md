# 서지정보
García-Gamero, V., Vanwalleghem, T., Peña, A., Román-Sánchez, A., & Finke, P. A. (2022). *Modelling the effect of catena position and hydrology on soil chemical weathering*. SOIL, 8, 319-335. DOI: 10.5194/soil-8-319-2022.

# 이 논문을 찾은 이유
Pelletier보다 작은 forcing interval에서 hydrology와 chemical weathering을 계산하고 soil-profile change를 추적하는 모델이 있는지 확인하기 위해 검토했다.

# 연구 유형
- 1D process-based soil/pedogenesis model
- SoilGen application
- hydrology + chemical weathering

# 공간 구조
- one-dimensional soil profile
- layered soil compartments
- no lateral water or sediment transfer

# 적용 환경
- soil catena
- Mediterranean climate
- long-term pedogenesis with daily hydrological forcing

# 핵심 과정
- soil moisture
- infiltration/percolation
- mineral chemical weathering
- solute transport
- profile chemical depletion
- vegetation interception as boundary forcing

# 식생 입력
This application uses vegetation/interception boundary conditions rather than LPJ-GUESS-like dynamic cohorts.

# 시간간격
Daily precipitation is used and modelled soil moisture is evaluated at daily scale.

The model can integrate fast hydrological/chemical processes internally while accumulating pedogenic change over long periods.

The application itself simulates 20,000 years, but the weathering/hydrology mechanism is not restricted to a geologic forcing interval.

# 핵심 식 / 상태
The paper evaluates chemical weathering using chemical depletion fraction:

```
CDF
=
1 - Zr_ROCK / Zr_SOIL
```

The SoilGen framework resolves mineral reactions and profile transport rather than representing weathering solely by a vegetation proxy.

# 파라미터와 단위
- daily precipitation / ET
- layer soil moisture
- mineral composition and kinetic parameters
- chemical depletion fraction

Detailed reaction parameters are SoilGen-specific and not copied here without the model documentation.

# 원 논문의 구현 범위
Hydrology and chemical weathering are simulated in a vertically resolved soil profile.

# 고운사에 직접 사용할 수 있는 부분
Useful as an independent **short-timescale/profile-weathering benchmark** against the simpler LPJ-GUESS-CNP weathering formulation.

It demonstrates that chemical weathering can be forced with daily hydrology even if geomorphic soil formation accumulates slowly.

# 새로운 coupling이 필요한 부분
Connecting LPJ-GUESS vegetation/root states to SoilGen would be a new coupling.

Coupling SoilGen profile weathering to a 2D/DEM hillslope model would also be new because this model lacks lateral fluxes.

# 한계
- 1D
- explicitly omits lateral water fluxes
- no topographic sediment transport
- vegetation representation is not a DGVM/cohort model
- computational and parameter burden is much higher than LPJ-GUESS-CNP

# 최종 판정
**보조/검증 후보, not primary Gounsa weathering engine.**

LPJ-GUESS-CNP is preferred for the first implementation because it is already dynamically coupled to the vegetation/hydrology model.

# 참고 링크 / DOI
https://doi.org/10.5194/soil-8-319-2022
