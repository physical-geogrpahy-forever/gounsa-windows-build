# Pelletier et al. (2013)

# 서지정보
Pelletier, J. D., Barron-Gafford, G. A., Breshears, D. D., et al. (2013). *Coevolution of nonlinear trends in vegetation, soils, and topography with elevation and slope aspect: A case study in the sky islands of southern Arizona*. Journal of Geophysical Research: Earth Surface, 118, 741-758. DOI: 10.1002/jgrf.20046.

# 이 논문을 찾은 이유
AGB/EEMT를 soil production, colluvial transport and landscape evolution에 연결한 model을 100-year Gounsa의 주 모델로 쓸 수 있는지 재검토하기 위해 확인했다.

# 연구 유형
- numerical landscape-evolution model
- field-calibrated eco-pedo-geomorphic framework

# 공간 구조
- 10 m raster
- 101 x 201 cells
- soil thickness + topography
- colluvial and fluvial transport

# 적용 환경
- southern Arizona sky-island mountains
- water-limited elevation/climate gradient
- granitic terrain

# 핵심 과정
- vegetation-soil-topography coevolution
- soil production
- colluvial transport
- fluvial/slope-wash erosion
- soil-thickness feedback

# 식생 입력
- EEMT as primary prescribed environmental/biological gradient
- observed above-ground biomass relationships
- vegetation-dependent geomorphic parameters

# 시간척도: 핵심 재판정

The paper explicitly develops a model for **geologic-time-scale** coevolution.

Each model run is driven by a prescribed, spatially uniform EEMT value representing a climatic/elevational condition.

Reported model landscapes are shown after:
```
10 Myr of uplift/evolution
```
to approach dynamic topographic steady state.

The numerical solver itself uses a much smaller explicit timestep for stability:
```
dt_default
=
0.01 * Dx^2 / (2*kappa_d)
```
with additional dynamic reduction when erosion/deposition per step is too large.

This is a critical distinction:

```
small numerical dt
!=
short-timescale ecological parameterization
```

The vegetation/weathering/transport relationships are calibrated and interpreted as long-term spatial/steady relationships, not annual LPJ-GUESS succession responses.

# 핵심 식
The model includes depth- and slope-dependent colluvial transport and soil production with vegetation/EEMT dependence.

The important Gounsa conclusion is not the exact finite-difference timestep but the calibration timescale of the constitutive relations.

# 원 논문의 구현 범위
Long-term landscape self-organization under different prescribed EEMT/climate states.

# 고운사에 직접 사용할 수 있는 부분
- structural precedent that vegetation, soil depth and topography coevolve
- long-term sensitivity/steady-state benchmark
- useful check on signs and broad magnitude of eco-geomorphic feedbacks

# 새로운 coupling이 필요한 부분
Directly inserting annual LPJ-GUESS biomass into Pelletier's vegetation-dependent diffusivity or soil-production parameter would be a time-scale transfer and a new coupling.

# 한계
- geologic-time-scale target
- 10 Myr reported model states
- EEMT prescribed between model runs rather than annual vegetation succession
- no explicit annual tree-throw/root-turnover state
- no event-scale postfire recovery structure

# 최종 판정
**보조근거 only. Do not use as the primary 100-year Gounsa weathering or hillslope-transport engine.**

A small internal solver timestep does not remove the constitutive-timescale mismatch.

# 참고 링크 / DOI
https://doi.org/10.1002/jgrf.20046
