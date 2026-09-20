# 서지정보
Gabet, E. J., & Mudd, S. M. (2009). *A theoretical model coupling chemical weathering rates with denudation rates*. Geology, 37(2), 151-154. DOI: 10.1130/G25270A.1.

# 이 논문을 찾은 이유
최근 DynSoil/MErSiM의 원형이 되는 regolith weathering model을 직접 확인하고, chemical weathering, erosion, regolith thickness의 역할을 구분하기 위해 검토했다.

# 연구 유형
- theoretical process model
- chemical-weathering/denudation mass balance

# 공간 구조
- 1D regolith column

# 적용 환경
- generic weathering systems across supply-limited and kinetically limited regimes

# 핵심 과정
- weathering-front material supply
- mineral residence time
- chemical dissolution
- physical erosion
- regolith thickness feedback

# 핵심 질량수지
At steady regolith thickness, chemical weathering mass flux is the difference between weatherable mineral mass entering from the advancing weathering front and weatherable mineral mass leaving by physical erosion:

```
W
=
(m_C - m_E) / Delta t
```

where:
- `W`: chemical weathering mass flux [M L^-2 T^-1]
- `m_C`: weatherable-mineral mass entering the regolith column
- `m_E`: weatherable-mineral mass physically exported

# 핵심 개념
The model resolves the transition between:
- supply-limited weathering
- kinetically limited weathering

As erosion rises, fresh-mineral supply rises, but thinner regolith and shorter residence time can limit total weathering.

Thus:
```
more erosion
!= indefinitely more chemical weathering
```

# 고운사에 직접 사용할 수 있는 부분
Important conceptual and mathematical parent of DynSoil.

It supports keeping separate:
```
regolith production/front advance
physical erosion
chemical dissolution
```

rather than treating chemical weathering as a simple thickness-production coefficient.

# 새로운 coupling이 필요한 부분
The original model is not LPJ-GUESS-driven and is not calibrated for 100-year postfire forest dynamics.

Using LPJ-GUESS runoff/temperature/root states to alter its rates is a new coupling unless inherited through a later published implementation.

# 한계
- original formulation focused on long-term weathering-denudation relationships
- simple 1D column
- no explicit vegetation dynamics
- original paper emphasizes steady-state regolith thickness

# 최종 판정
**핵심 lineage source for regolith weathering and DynSoil/MErSiM.**

Use mainly through its later transient implementations, not alone as the production code for Gounsa.

# 참고 링크 / DOI
https://doi.org/10.1130/G25270A.1
