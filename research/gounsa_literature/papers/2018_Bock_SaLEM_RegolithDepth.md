# 서지정보
Bock, M., Conrad, O., Guenther, A., Gehrt, E., Baritz, R., & Boehner, J. (2018). *SaLEM (v1.0) – the Soil and Landscape Evolution Model (SaLEM) for simulation of regolith depth in periglacial environments*. Geoscientific Model Development, 11, 1641-1659. DOI: 10.5194/gmd-11-1641-2018.

# 이 논문을 찾은 이유
Pelletier보다 process-explicit하고 GIS 기반인 regolith-depth model이 고운사 100년 풍화/사면확산에 적합한지 검토하기 위해 확인했다.

# 연구 유형
- process-based soil-landscape evolution model
- SAGA GIS implementation
- open-source model

# 공간 구조
- raster DEM
- lithologically differentiated regolith
- erosion, transport, accumulation and weathering

# 핵심 과정
- bedrock weathering
- regolith-depth evolution
- diffusive transport
- erosion/deposition
- allochthonous input
- climate forcing

# 시간간격
This distinction is critical.

SaLEM:
- evaluates weathering rates using monthly climate within an annual climate scenario
- but the landscape model timestep is typically around:

```
100 years
```

The paper targets the last:
```
50,000 years
```
in periglacial northern Germany.

Therefore:
```
monthly weathering calculation
!=
annual landscape-state update
```

# 고운사에 직접 사용할 수 있는 부분
- open-source raster architecture
- explicit regolith-depth state
- lithology-specific weathering
- climate-sensitive weathering
- transport/accumulation bookkeeping

# 왜 현재 본체가 아닌가
For a 100-year Gounsa simulation, the default SaLEM landscape timestep is of the same order as the entire target horizon.

Its process calibration and target setting are also periglacial and late-Pleistocene.

Thus it does not solve the short-timescale coupling problem as cleanly as MErSiM's transient state equations.

# source availability
SaLEM is included in the open-source SAGA GIS codebase.

# 한계
- periglacial calibration
- typically 100-year timestep
- no dynamic LPJ-GUESS vegetation/root state
- no postfire succession

# 최종 판정
**comparison/open-source architecture reference, not current 100-year Gounsa core.**

MErSiM is preferred for transient regolith-state equations.

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-11-1641-2018
