# 서지정보
Roberge, L. O., Gasparini, N. M., Campforts, B., & Tucker, G. E. (2026). *ConcentrationTracker: Landlab components for tracking material concentrations in sediment*. Geoscientific Model Development, 19, 1387-1404. DOI: 10.5194/gmd-19-1387-2026.

# 이 논문을 찾은 이유
Landlab의 depth-dependent creep와 soil-production components가 실제 2D mobile-regolith mass balance에서 현재 사용되고 있는지, 그리고 고운사 구현에 재사용할 수 있는 공개 framework인지 확인하기 위해 검토했다.

# 연구 유형
- numerical model-development paper
- open-source Landlab components
- gridded sediment/regolith mass balance

# 공간 구조
- 2D raster/irregular grids
- mobile regolith over bedrock
- sediment flux between adjacent grid nodes

# 핵심 과정
- mobile-regolith mass conservation
- hillslope sediment flux
- bedrock/regolith source
- spatial tracer/material tracking

# relevant implementation
The paper demonstrates Landlab coupling among:
- ExponentialWeatherer
- DepthDependentDiffuser
- mobile-regolith state

Exponential soil production:

```
P_s
=
P_0 exp(-H_s/H_d)
```

Depth-dependent hillslope transport:

```
Q_s
=
-D S H_* (1-exp(-H_s/H_*))
```

The paper uses a mass-balance approach to update mobile regolith and tracked sediment properties.

# 고운사에 직접 사용할 수 있는 부분
This is a current published implementation precedent for exactly the numerical bookkeeping Gounsa needs:

```
bedrock / parent material
 -> soil production
 -> mobile soil layer
 -> depth-limited hillslope flux
 -> spatial mass balance
```

The empirical Gounsa process laws do not have to equal Landlab defaults.

Recommended use:
- keep Landlab grid/state/mass-conservation machinery
- replace/default-tune soil production with the Gounsa sandstone shallow-soil scenarios
- use DepthDependentDiffuser for residual creep
- add Gabet root-growth flux as a separate component
- add dry-ravel and SWEHR coupling separately

# important limitation
Landlab ExponentialWeatherer itself assumes monotonic exponential production with maximum at zero soil thickness.

Because Gounsa has shallow sandstone and Oregon sandstone evidence permits a finite-depth production peak, the default ExponentialWeatherer should not be hard-locked as the only production law.

A custom shallow-hump weatherer may be required for sensitivity mode B.

# source / implementation value
Landlab is modular and open source.

It is therefore a better software scaffold than rewriting a long-term Pelletier landscape-evolution model for a 100-year multi-rate application.

# final judgment
**채택: preferred numerical implementation framework for weathering + residual hillslope diffusion bookkeeping.**

Not a source of Gounsa empirical parameter values.

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-19-1387-2026
