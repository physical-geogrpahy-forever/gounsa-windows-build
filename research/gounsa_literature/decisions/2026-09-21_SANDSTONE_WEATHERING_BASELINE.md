# 결정: 고운사 sandstone soil-production / weathering baseline

날짜: 2026-09-21

## 범위 수정
고운사 parent material은 현재 프로젝트 기준 **sandstone**으로 취급한다.

따라서 이전에 검토한 granite 생산률은 cross-lithology comparison으로만 유지한다.

Production parameterization은 sandstone literature를 우선한다.

---

## 1. 핵심 결정

100년 고운사 baseline에서 full DynSoil/MErSiM transient mineral-age model을 기본으로 사용하지 않는다.

Bedrock/saprolite -> mobile soil production은 sandstone-specific soil-production function으로 둔다:

```
P_sand(h)
=
P0_sand
exp(-h/gamma_sand)
```

where:
- `P_sand`: soil-production rate [m yr^-1]
- `P0_sand`: zero-soil-thickness production rate [m yr^-1]
- `h`: mobile soil thickness [m]
- `gamma_sand`: e-folding soil-depth scale [m]

이 식은 annual geomorphic step에서 평가한다.

---

## 2. sandstone data envelope

### Evans et al. 2019
Triassic sandstone, temperate UK:
```
0.026-0.096 mm yr^-1
```

Coniferous Comer Wood mean:
```
0.070 +/- 0.010 mm yr^-1
```

100-year woodland mean equivalent:
```
about 7 mm / 100 yr
```

### Evans et al. 2021
Four sandstone sites:

Observed ranges:
- Comer: 0.053-0.096 mm yr^-1
- Hilton: 0.065-0.193 mm yr^-1
- Rufford: 0.026-0.084 mm yr^-1
- Woburn: 0.031-0.150 mm yr^-1

Zero-thickness fitted production:
- Comer: 0.077 +/- 0.009 mm yr^-1
- Hilton: 0.175 +/- 0.039 mm yr^-1
- Rufford: 0.071 +/- 0.006 mm yr^-1
- Woburn: 0.274 +/- 0.045 mm yr^-1

Gamma:
- Comer: 4.50 +/- 1.80 m
- Hilton: 2.70 +/- 1.20 m
- Rufford: 2.27 +/- 0.38 m
- Woburn: 0.80 +/- 0.10 m

Thus sandstone production varies strongly with lithology/cementation.

### Heimsath et al. 2001
Forested Oregon Coast Range sandstone provides the classic soil-production-function lineage.

Later synthesis gives a high thin-soil production of order:
```
~0.268 mm yr^-1
```
for that setting.

At about 1 m soil thickness, the Coos Bay sandstone rate is cited near:
```
0.014 mm yr^-1
```

This reinforces the strong soil-thickness shielding effect.

---

## 3. lithological control

Sandstone cannot be parameterized by rock name alone.

Evans 2021 and Marshall 2014 show importance of:
- matrix abundance
- cement type
- quartz/feldspar overgrowth
- iron-oxide cement
- permeability
- tensile strength
- fracture density
- diagenetic history

Therefore final Gounsa `P0_sand` and `gamma_sand` require local/regional sandstone characterization.

### Uiseong regional context
Uiseong Cretaceous sedimentary rocks include sandstone-rich Hayang Group units.

Regional Uiseong sandstone studies report lithic arkose and feldspathic wacke among common sandstone types.

This is **regional context only** and is not yet treated as exact Gounsa-site petrography.

Exact Gounsa parent-rock classification must be confirmed from:
- geological map / field outcrop
- thin section or published local geology
- matrix/cement/fracture observations

---

## 4. chemical weathering stays separate

Do not identify soil production with dissolved chemical loss.

Keep:

```
P_sand(h)
=
bedrock/saprolite -> mobile soil production
```

separate from:

```
W_chem
=
chemical dissolved mass loss
```

The A/B mass balance remains:

```
dM_AB/dt
=
rho_parent P_sand
+
D_phys
-
E_phys
-
W_AB
```

with density conversion implemented consistently.

Hartmann/LPJ-GUESS supplies a chemical-weathering forcing for `W_chem`, not `P_sand`.

---

## 5. postfire behavior

No arbitrary fire multiplier is added to `P_sand`.

Fire affects production naturally if soil cover thins:

```
fire + erosion
 -> h decreases
 -> P_sand(h) increases
```

This is a published soil-thickness feedback.

Additional:
```
fire severity -> P0 multiplier
```
is not adopted without direct sandstone evidence.

Fire spall remains a separate physical-fragment production process.

---

## 6. vegetation/root effect

Pawlik et al. 2023 shows that living tree roots:
- penetrate sandstone fractures
- wedge sandstone fragments
- alter rhizosphere properties
- contribute to soil formation

But no universal quantitative:
```
root biomass -> P_sand
```
law is established.

Therefore production baseline does not multiply `P_sand` by LPJ-GUESS biomass/root state.

If later added, it must be marked as a new coupling and calibrated.

---

## 7. role of DynSoil/MErSiM

Demoted from production baseline to optional sensitivity/advanced module.

Use it only if needed to represent:
- primary-mineral depletion
- residence time / exposure age
- transient deep regolith chemistry

For the initial 100-year geomorphic model, the sandstone-specific empirical production function is simpler and more lithologically defensible.

---

## 8. role of granite papers

Shiroya 2010, Matsushi 2016 and Ouyang 2026 remain:
- cross-lithology comparison
- method/timescale references

They are not Gounsa parameter constraints.

The previous granite-based inference that front production would likely be sub-mm to a few mm per 100 yr is withdrawn for Gounsa.

Sandstone evidence supports a broader and often larger century-scale range:
```
several mm to roughly 1-3 cm / 100 yr
```
depending on soil thickness and cementation.

---

## 9. current production baseline

```
annual:
P_sand(h)
=
P0_sand exp(-h/gamma_sand)
```

```
daily/annual accumulated:
W_chem
=
Hartmann / LPJ-GUESS chemical weathering
```

```
A/B mass balance:
dM_AB/dt
=
production + deposition - erosion - chemical loss
```

This is now the preferred weathering/soil-production structure.

---

## unresolved

1. exact Gounsa sandstone formation and petrography
2. local `P0_sand`
3. local `gamma_sand`
4. parent-rock and soil bulk density
5. partition of dissolved chemical loss between A/B and deeper weathered material
6. fire-spall production from sandstone
7. whether a root-dependent modification to `P_sand` is needed after validation

## final judgment
**Sandstone-specific soil-production function replaces granite-based magnitude reasoning and supersedes full MErSiM as the initial production baseline.**


## timescale caveat

Heimsath/Evans sandstone production functions are derived from cosmogenic-nuclide long-term average soil-production rates.

Therefore evaluating `P_sand(h)` every year is a numerical bookkeeping choice for a slowly varying background process. It does **not** imply that the published relation resolves year-to-year climate or vegetation fluctuations.

Current division of roles:

```text
P_sand(h)
 -> slow background parent-material to soil production

LPJ-GUESS/Hartmann
 -> daily climate/hydrology-sensitive chemical dissolved loss
```

Do not add annual climate or biomass multipliers to `P_sand` without a separate published/local relation.


---

## 10. shallow-soil correction

Project condition:
```
sandstone
+ shallow soil
```

supersedes any interpretation that treats Gounsa as a generic thick-soil sandstone hillslope.

The previous single-mode baseline:

```
P_sand(h) = P0_sand exp(-h/gamma_sand)
```

is retained as **mode A**, not as the only production function.

Mandatory sensitivity **mode B** must allow a finite-depth production peak because the Oregon sandstone lineage indicates:
- high production at about 15-30 cm
- possible lower production at <15 cm
- resistant/less-weathered bedrock near bare exposure

Thus no production code may assume:
```
less soil always -> faster production
```
all the way to h = 0.

See:
`decisions/2026-09-21_SHALLOW_SANDSTONE_PRODUCTION.md`

### implication for 100-year magnitude
Because soil is shallow, the site may lie near the upper production regime, so century-scale production should be retained and compared quantitatively against erosion, dry ravel and fire-spall rather than pre-judged negligible.

### implication for creep
Shallow `H_active` directly limits:
```
q_bg = -D*_bg H_active grad(z)
```

and all mobile-soil transport modules must include an availability cap.
