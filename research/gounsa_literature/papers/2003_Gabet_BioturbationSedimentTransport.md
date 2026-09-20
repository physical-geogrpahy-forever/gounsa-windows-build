# 서지정보
Gabet, E. J., Reichman, O. J., & Seabloom, E. W. (2003). *The effects of bioturbation on soil processes and sediment transport*. Annual Review of Earth and Planetary Sciences, 31, 249-273. DOI: 10.1146/annurev.earth.31.100901.141314.

# 이 논문을 찾은 이유
피복률이나 biomass-modified diffusivity 대신, 실제 root mass, root turnover, rooting-depth distribution으로 연간 root-growth/decay hillslope sediment flux를 계산하는 published process equation을 확정하기 위해 재검토했다.

# 연구 유형
- quantitative review
- mechanistic geometrical derivation
- complete landscape-evolution model은 아님

# 공간 구조
- local hillslope sediment-flux formulation
- horizontal volumetric flux per contour width

# 적용 환경
- grassland
- shrubland
- forest
- natural soil-mantled hillslopes

# 핵심 과정
Roots repeatedly:
1. grow and expand soil approximately normal to the surface
2. die/decay
3. leave a void
4. soil collapses vertically into that void

Because the expansion and collapse directions differ on a slope, a net downslope displacement remains.

# 식생 입력
- root mass per unit ground area `r` [kg m^-2]
- annual root turnover `tau` [yr^-1]
- root tissue density `rho_r` [kg m^-3]
- rooting-depth distribution parameter `beta`
- slope angle `theta`

# 핵심 식

## general flux
```
q_sx
=
x r tau / rho_r
```

where:
- `q_sx`: horizontal volumetric sediment flux [m3 m^-1 yr^-1]
- `x`: net horizontal displacement [m]

## net displacement
```
x
=
z_c sin(theta) cos(theta)
```

where:
- `z_c`: vertical depth of the root-system center of mass [m]

## root-depth distribution
Using the Gale-Grigal root-profile form:

```
z
=
log(1-Y)
/
(100 log(beta))
```

where:
- `Y`: cumulative root fraction from the surface to depth z
- `beta`: PFT/vegetation-specific root-distribution parameter

For the center of mass, the paper sets:
```
Y = 0.5
```

## root turnover
```
tau
=
annual belowground production
/
maximum belowground standing crop
```

## final root-growth/decay flux
Substituting the geometric and turnover relations gives:

```
q_sx
=
-[0.003 r tau / (rho_r log(beta))]
sin(theta) cos(theta)
```

The negative sign arises because `log(beta)` is negative for `0 < beta < 1`, so downslope flux magnitude is positive under the paper's sign convention.

The paper uses:
```
rho_r = 800 kg m^-3
```
for illustrative vegetation-class calculations.

Do not assume this root tissue density universally if LPJ-GUESS or species-specific values are available.

# published example values
For a temperate forest example the paper uses approximately:
- `beta = 0.976`
- `r = 4.4 kg m^-2`
- `tau = 0.56 yr^-1`

which yields:
```
q_sx
=
8.8e-4 sin(theta) cos(theta)
m3 m^-1 yr^-1
```

These are broad literature-derived example values, not Gounsa calibration values.

# LPJ-GUESS interface

LPJ-GUESS already represents:
- fine-root biomass/carbon
- vertical root distribution
- PFT-specific fine-root turnover

Therefore production coupling should use LPJ-GUESS-native root states/parameters rather than Gabet's global vegetation-class examples.

Conceptual interface:

```
LPJ-GUESS
 fine-root state r
 fine-root turnover tau
 vertical root distribution
       |
       v
z_c or equivalent center-of-mass depth
       |
       v
Gabet q_root
```

If LPJ-GUESS directly outputs layer-specific root distribution, derive `z_c` from those layer fractions rather than forcing the old single-beta profile.

# important assumptions
The derivation assumes:
1. soil displaced by root growth behaves rigidly rather than accommodating much strain through local compaction
2. growth-induced deformation is normal to the hillslope surface
3. collapse after root decay is vertical

The authors explicitly state this gives an upper-bound style estimate of possible root-induced displacement because some real root growth strain is accommodated by soil-density changes.

# current Gounsa role
This is the main **root-growth/decay biogenic transport equation**.

It is separate from:
- residual wet-dry/freeze-thaw/faunal creep
- postfire dry ravel
- water erosion

Tree throw/uprooting is not part of the current production baseline.

# numerical timescale
The equation is annual by construction because `tau` is in yr^-1.

It fits the 100-year Gounsa annual geomorphic step directly.

# new coupling
The exact combined implementation:

```
LPJ-GUESS native root states
 -> Gabet q_root
 -> raster flux divergence
 -> DEM/mobile-soil update
```

is a new coupling.

However, the root-to-flux equation itself is published and does not need a new empirical biomass multiplier.

# final judgment
**채택: primary annual root-growth/decay hillslope-transport equation.**

The remaining implementation issues are:
- exact LPJ-GUESS variable/unit mapping
- root tissue density if needed
- conversion from layer fractions to root center-of-mass depth
- mobile-soil availability cap so root transport cannot move more soil than exists

# 참고 링크 / DOI
https://doi.org/10.1146/annurev.earth.31.100901.141314
