# 서지정보
Norton, K. P., Molnar, P., & Schlunegger, F. (2014). *The role of climate-driven chemical weathering on soil production*. Geomorphology, 204, 510-517. DOI: 10.1016/j.geomorph.2013.08.030.

# 이 논문을 찾은 이유
soil/regolith production을 단순 depth-only law가 아니라 precipitation과 temperature에 반응시키는 published numerical formulation이 있는지 확인하기 위해 검토했다.

# 연구 유형
- climate-dependent soil/regolith production model
- numerical sensitivity analysis

# 핵심 과정
- chemical weathering
- soil/regolith production
- precipitation control
- temperature control
- erosion-production balance

# 핵심 개념
The model modifies soil/regolith production using climate-driven chemical-weathering controls.

It predicts:
- low denudation: relative soil thickness less sensitive to precipitation
- high denudation: small climatic changes can cause strong soil-thickness response or stripping
- response time depends on climate and erosion regime

# 고운사에 직접 사용할 수 있는 부분
Important support for using:
```
temperature + water availability
 -> production-rate modifier
```
rather than a static Pelletier-style long-term vegetation proxy.

It provides an intermediate-complexity option between:
- simple Heimsath depth-only production
- more detailed MErSiM/Braun transient regolith models

# 한계
- not LPJ-GUESS coupled
- no root-state dynamics
- calibrated/interpreted over geomorphic timescales
- not a complete 2D soil-landscape model

# 최종 판정
**useful climate-sensitive fallback/reference.**

If MErSiM is too complex for the 100-year signal, this model gives a simpler climate-responsive production law.

# 참고 링크 / DOI
https://doi.org/10.1016/j.geomorph.2013.08.030
