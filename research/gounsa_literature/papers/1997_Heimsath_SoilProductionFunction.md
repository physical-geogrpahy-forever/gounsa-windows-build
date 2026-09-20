# 서지정보
Heimsath, A. M., Dietrich, W. E., Nishiizumi, K., & Finkel, R. C. (1997). *The soil production function and landscape equilibrium*. Nature, 388, 358-361. DOI: 10.1038/41056.

# 이 논문을 찾은 이유
고운사 100년 풍화/soil production에서 regolith/soil production을 soil thickness의 함수로 표현하는 가장 기본적인 field-calibrated production law를 확인하기 위해 검토했다.

# 연구 유형
- field-calibrated soil production study
- cosmogenic nuclide based
- empirical production function

# 핵심 과정
- bedrock to soil conversion
- soil-thickness control on production
- landscape equilibrium

# 핵심 식
The paper provides the classic exponential soil-production function:

```
P_s
=
P_0 exp(-h/h_0)
```

where:
- `P_s`: soil production rate [L T^-1]
- `P_0`: bare-bedrock or zero-soil production rate [L T^-1]
- `h`: soil thickness [L]
- `h_0`: characteristic damping depth [L]

The key empirical result is that production declines exponentially as soil cover thickens.

# 고운사에 직접 사용할 수 있는 부분
This provides the simplest possible production law if the more detailed climate-driven regolith models prove unnecessary over 100 years.

A Gounsa fallback could use:

```
P_front
=
P_0 exp(-H_reg/h_0)
```

with local calibration.

# 중요한 한계
- vegetation is not a dynamic state variable
- climate is not explicit
- production is long-term field inferred
- does not separate chemical and mechanical production
- not postfire specific

# 최종 판정
**baseline/fallback production-law reference, not the first-choice full model.**

Use as a sensitivity or reduced-complexity alternative to MErSiM/Braun.

# 참고 링크 / DOI
https://doi.org/10.1038/41056
