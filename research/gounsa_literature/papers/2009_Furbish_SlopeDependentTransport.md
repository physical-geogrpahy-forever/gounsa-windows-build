# 서지정보
Furbish, D. J., Haff, P. K., Dietrich, W. E., & Heimsath, A. M. (2009). *Statistical description of slope-dependent soil transport and the diffusion-like coefficient*. Journal of Geophysical Research: Earth Surface, 114, F00A05. DOI: 10.1029/2009JF001267.

# 이 논문을 찾은 이유
tree throw, root-growth transport, dry ravel을 별도로 계산한 뒤 남는 background creep를 constant diffusivity로 둘지, active-soil thickness를 포함한 더 물리적인 residual transport law를 쓸지 확인하기 위해 검토했다.

# 연구 유형
- statistical-mechanical / kinematic transport theory
- field-data comparison

# 공간 구조
- local soil column + hillslope
- vertically integrated sediment flux

# 적용 환경
- soil-mantled hillslopes
- field comparisons in California/Australia

# 핵심 과정
- small-scale biomechanical mixing
- soil dilation
- particle settling under gravity
- slope-dependent creep
- active-soil-depth dependence

# 핵심 결과
The standard diffusion-like coefficient `D [L2 T-1]` is not a primitive constant.

It contains information about:
- active soil thickness
- particle size
- excess porosity
- particle-activation frequency with depth

The analysis supports:

```
soil flux
proportional to
active soil thickness
x slope
```

with a geometric `cos^2(theta)` factor in the derived formulation.

A convenient functional form for Gounsa bookkeeping is therefore:

```
q_bg
~ -D*_bg H_active grad(z) cos^2(theta)
```

where:
- `D*_bg`: quasi-local transport coefficient [L T-1]
- `H_active`: active mobile-soil thickness [L]

This expression records the published **depth-slope functional dependence**. Exact sign/geometric convention must follow the implementation coordinates.

# 중요한 장점
As:
```
H_active -> 0
```
then:
```
q_bg -> 0
```

This is important for a postfire model in which A/B soil thickness can become very small.

A constant:
```
q = -D grad(z)
```
does not enforce this unless D is itself changed with soil thickness.

# process meaning
The paper focuses on small-scale, local creep-like motions.

It does not require tree throw, dry ravel and long-travel surface disturbances to be hidden in the same coefficient.

# 고운사에 직접 사용할 수 있는 부분
Preferred mathematical structure for **residual local creep**:

```
q_bg
=
-D*_bg H_active grad(z)
```

with optional geometric correction.

This is cleaner than a total natural-landscape diffusivity because Gounsa already represents several large-disturbance processes explicitly.

# 새로운 coupling이 필요한 부분
The value of `D*_bg` for Gounsa must be calibrated or constrained.

Do not make it a direct LPJ-GUESS biomass multiplier without independent evidence.

# 한계
- kinematic/statistical theory rather than a site-specific forest model
- authors note strongest applicability where significant long-distance surface transport is absent
- steep-slope nonlocal motion requires separate treatment

# 최종 판정
**채택: baseline functional form for residual local creep.**

Use with explicit tree throw/root-growth/dry-ravel/landslide modules.

# 참고 링크 / DOI
https://doi.org/10.1029/2009JF001267
