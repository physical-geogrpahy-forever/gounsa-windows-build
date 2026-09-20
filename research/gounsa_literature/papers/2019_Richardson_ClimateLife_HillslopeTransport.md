# 서지정보
Richardson, P. W., Perron, J. T., & Schurr, N. D. (2019). *Influences of climate and life on hillslope sediment transport*. Geology, 47(5), 423-426. DOI: 10.1130/G45305.1.

# 이 논문을 찾은 이유
background diffusivity의 가능한 magnitude와 climate/vegetation dependence를 전지구 자료에서 확인하되, 그것을 고운사 residual coefficient로 직접 이식해도 되는지 평가하기 위해 검토했다.

# 연구 유형
- global compilation of published transport coefficients
- new site estimates
- climate/vegetation synthesis

# 핵심 결과
Across compiled landscapes:
- `D` rises strongly with moisture among relatively dry sites
- the moisture dependence weakens among wetter sites
- vegetation type has a secondary effect among dry sites
- vegetation-type effect is much weaker among wetter sites

The authors interpret this as biological establishment greatly accelerating creep in dry environments, while in moist landscapes biological activity can both promote transport and stabilize slopes.

Published compilations span a very broad approximate range:
```
D ~ 10^-5 to 10^-1 m^2 yr^-1
```
across strongly contrasting settings.

A value around:
```
10^-2 m^2 yr^-1
```
is often used only as a broad representative magnitude in later theoretical examples, not as a universal forest value.

# 핵심 제약
The compiled `D` is an **effective total transport coefficient**.

It can contain contributions from:
- biological mixing
- tree throw
- moisture-driven creep
- freeze-thaw
- other local disturbance processes

Therefore it is not the same as Gounsa's:
```
D_bg,residual
```
after explicit process subtraction.

# 고운사에 직접 사용할 수 있는 부분
Use for:
- broad plausibility bounds
- sensitivity-range sanity checks
- rejecting values far outside known hillslope transport efficiency

Do **not** set Gounsa residual `D_bg` equal to the global climate/forest regression.

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation/moisture -> Richardson total D would be a new coupling and would double count explicit biological processes.

# 한계
- global heterogeneous compilation
- effective coefficient rather than mechanism-specific residual
- mostly long-term inferred values

# 최종 판정
**validation envelope only, not direct residual-D parameterization.**

# 참고 링크 / DOI
https://doi.org/10.1130/G45305.1
