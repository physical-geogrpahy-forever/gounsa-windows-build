# 서지정보
Evans, D. L., Quinton, J. N., Tye, A. M., Rodés, Á., Rushton, J. C., Davies, J. A. C., & Mudd, S. M. (2021). *How the composition of sandstone matrices affects rates of soil formation*. Geoderma, 401, 115337. DOI: 10.1016/j.geoderma.2021.115337.

# 이 논문을 찾은 이유
고운사 사암의 soil-production rate를 암종 하나의 상수로 두지 않고, 사암의 matrix/cementation과 soil thickness에 따라 달라지는 production function으로 제약하기 위해 검토했다.

# 연구 유형
- cosmogenic 10Be soil-production study
- sandstone petrography / matrix-cement comparison
- hillslope catena analysis

# 적용 환경
- UK sandstone hillslopes
- arenite sandstone
- contrasting cementation histories

# 핵심 결과

Observed soil-formation rates:
- Hilton: `0.065-0.193 mm yr^-1`
- Woburn: `0.031-0.150 mm yr^-1`

Across all four sandstone sites compared in the paper:
- Comer Wood: `0.053-0.096 mm yr^-1`
- Hilton: `0.065-0.193 mm yr^-1`
- Rufford: `0.026-0.084 mm yr^-1`
- Woburn: `0.031-0.150 mm yr^-1`

# zero-soil-thickness production

The fitted soil-production function gives:

- Comer: `P0 = 0.077 +/- 0.009 mm yr^-1`
- Hilton: `P0 = 0.175 +/- 0.039 mm yr^-1`
- Rufford: `P0 = 0.071 +/- 0.006 mm yr^-1`
- Woburn: `P0 = 0.274 +/- 0.045 mm yr^-1`

100-year equivalent at zero soil thickness:
- about 7.1 to 27.4 mm per 100 years across the four sandstone sites

# soil-depth sensitivity

The paper defines a gamma depth at which formation falls to 1/e of `P0`.

Reported gamma:
- Comer: `4.50 +/- 1.80 m`
- Hilton: `2.70 +/- 1.20 m`
- Rufford: `2.27 +/- 0.38 m`
- Woburn: `0.80 +/- 0.10 m`

Thus sandstone sites vary strongly in how rapidly soil production declines with soil thickness.

# 핵심 식

The production relation is an exponential soil-production function:

```
P(h)
=
P0 exp(-h/gamma)
```

where:
- `P(h)`: soil-production rate [L T^-1]
- `P0`: production at zero soil thickness
- `h`: soil thickness
- `gamma`: e-folding soil-depth scale

# lithological control
The authors attribute faster weathering/soil formation to lower cementation and greater water transmission.

Important controls:
- quartz overgrowth
- K-feldspar overgrowth
- iron-oxide cement
- matrix abundance
- burial/diagenetic history
- permeability

Key conclusion:
```
sandstone lithology label alone is insufficient
```

Two sandstones can differ greatly in soil-production rate because of cementation and matrix properties.

# 고운사에 직접 사용할 수 있는 부분

For a sandstone Gounsa baseline, this is much more relevant than the previously used granite magnitude constraints.

Recommended production form:

```
P_front
=
P0,sandstone
exp(-H_cover/gamma)
```

with `P0` and `gamma` locally/regional calibrated.

The observed values above provide sensitivity bounds, not direct final parameters.

# postfire relevance
Because production increases as soil cover thins, strong postfire A/B loss can increase the exposed-parent-material production rate without imposing an arbitrary fire multiplier.

This is attractive for Gounsa:

```
fire/erosion
 -> H_AB decreases
 -> P_front increases through the published depth function
```

# 한계
- mostly arable UK sites; only Comer is conifer woodland in the comparison set
- lithology differs from Cretaceous Korean sandstone
- cosmogenic rates are long-term averages, not direct annual transient observations

# 최종 판정
**핵심 채택: sandstone-specific soil-production function and parameter envelope.**

This materially changes the previous granite-based century-scale interpretation.

# 참고 링크 / DOI
https://doi.org/10.1016/j.geoderma.2021.115337
