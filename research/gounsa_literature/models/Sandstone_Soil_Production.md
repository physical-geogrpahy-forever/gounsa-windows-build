# Sandstone soil-production lineage for Gounsa

## 목적
고운사 parent material을 sandstone으로 두고, 100년 model에서 bedrock/saprolite -> mobile soil production을 연 단위로 계산하는 baseline 계보를 정리한다.

## production equation

Primary baseline:

```
P_sand(h)
=
P0_sand exp(-h/gamma_sand)
```

where:
- `P_sand`: soil-production rate [m yr^-1]
- `P0_sand`: zero-soil-thickness production rate [m yr^-1]
- `h`: mobile-soil thickness [m]
- `gamma_sand`: e-folding soil-depth scale [m]

This is evaluated on the annual geomorphic timestep.

## 핵심 sandstone literature

### Heimsath et al. 2001
Forested Oregon Coast Range sandstone.

Key role:
- empirical soil-production-function lineage
- production declines strongly with soil thickness
- thin-soil production can be high in sandstone forest terrain

Use as structural precedent, not a direct Gounsa coefficient.

### Evans et al. 2019
Temperate Triassic sandstone sites, including coniferous Comer Wood.

Observed:
```
0.026-0.096 mm yr^-1
```

Conifer woodland mean:
```
0.070 +/- 0.010 mm yr^-1
```

100-year simple equivalent:
```
about 7 mm / 100 yr
```
for the woodland mean.

### Evans et al. 2021
Four contrasting sandstone sites.

Observed ranges:
- Comer: 0.053-0.096 mm yr^-1
- Hilton: 0.065-0.193 mm yr^-1
- Rufford: 0.026-0.084 mm yr^-1
- Woburn: 0.031-0.150 mm yr^-1

Fitted zero-thickness production:
- Comer: 0.077 +/- 0.009 mm yr^-1
- Hilton: 0.175 +/- 0.039 mm yr^-1
- Rufford: 0.071 +/- 0.006 mm yr^-1
- Woburn: 0.274 +/- 0.045 mm yr^-1

E-folding depth:
- Comer: 4.50 +/- 1.80 m
- Hilton: 2.70 +/- 1.20 m
- Rufford: 2.27 +/- 0.38 m
- Woburn: 0.80 +/- 0.10 m

This demonstrates that sandstone production parameters vary by several fold.

## lithological controls

Important:
```
sandstone != one weathering class
```

Key controls:
- matrix abundance
- cement type
- quartz overgrowth
- feldspar overgrowth
- Fe-oxide cement
- grain size
- permeability
- tensile strength
- fracture density
- burial/diagenetic history

Evans et al. 2021:
lower cementation generally increases soil-production susceptibility.

Marshall et al. 2014:
resistant sandstone beds can have about 2.5 times greater tensile strength than adjacent typical sandstone and show slower geomorphic response.

## Uiseong regional context

Regional Uiseong Cretaceous sandstone studies report common:
- lithic arkose
- feldspathic wacke

This is not yet a site-specific Gounsa petrographic classification.

Final Gounsa `P0_sand` and `gamma_sand` require:
- field/outcrop check
- local geological map
- ideally thin section or existing local petrography

## postfire coupling

No arbitrary fire multiplier.

Published thickness feedback gives:

```
fire / erosion
 -> H_AB decreases
 -> P_sand increases
```

because:

```
P_sand(h)
=
P0_sand exp(-h/gamma_sand)
```

If soil is stripped, the exponential mode approaches `P0_sand`, but this is **not** assumed universally. In the shallow-soil sensitivity mode, production may decline again toward exposed bedrock.

This is preferable to:

```
P_afterfire = k_fire * P_beforefire
```

without evidence.

## roots

Pawlik et al. 2023 shows roots can:
- enter sandstone fractures
- wedge fragments
- alter local soil formation

But no validated universal:
```
root biomass -> P_sand
```
rate law exists.

Therefore root biomass does not directly multiply `P_sand` in the production baseline.

## chemical mass loss

Soil production and chemical dissolved loss remain separate:

```
P_sand
!=
W_chem
```

Use:
- `P_sand` for parent-material to mobile-soil production
- Hartmann/LPJ-GUESS for bulk chemical dissolved loss
- Yoo/Brosens mass balance for mobile-soil thickness

## mobile soil balance

```
M_AB
=
rho_AB H_AB
```

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

with consistent density/porosity conversion.

## relation to DynSoil/MErSiM

DynSoil/MErSiM is no longer the first production baseline.

Use only when:
- mineral depletion profile matters
- exposure/residence age matters
- deeper regolith chemistry materially changes 100-year results

## relation to granite papers

Granite papers are cross-lithology comparison only.

Do not use granite-derived production magnitude to tune Gounsa.

## current parameter hierarchy

### production
Final values:
```
P0_sand, Gounsa
gamma_sand, Gounsa
```
are unresolved.

### sensitivity envelope
Sandstone literature gives approximate analogue range:

```
P0_sand
~ 0.071-0.274 mm yr^-1
```

```
gamma_sand
~ 0.80-4.50 m
```

These are not a final prior distribution until Gounsa petrography is identified.

## final judgment
**Shallow-soil sandstone baseline adopted with two mandatory sensitivity modes.**

```text
mode A: exponential
P_A(h) = P0_sand exp(-h/gamma_sand)

mode B: shallow-soil hump / zero-depth suppression
P_B(h) = published-constrained sensitivity form
```

Mode B is required because Oregon sandstone data permit a production peak at finite shallow soil thickness rather than forcing maximum production at bare bedrock.

This replaces:
- granite-based century-scale magnitude reasoning
- full DynSoil/MErSiM as default front-production engine


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


## shallow-soil correction

Project condition:
```
sandstone + shallow mobile soil
```

This makes the thin-soil regime the primary uncertainty.

Oregon Coast Range sandstone evidence:
- very rapid rates can occur around roughly 15-30 cm soil
- very thin soils below roughly 15 cm can show lower rates
- exposed/nearly exposed bedrock may be less weathered and more resistant than the finite-depth peak zone

Therefore:

```
h -> 0
does not automatically imply
P -> universal maximum
```

The Evans 2021 exponential form remains a required sensitivity case, but it is not hard-locked at very small `h`.

### transport consequence

Residual creep production baseline uses:

```
q_bg
=
-K_bg H_* [1-exp(-H_active/H_*)] grad(z)
```

For shallow soil:

```
q_bg
approx
-K_bg H_active grad(z)
```

so shallow soil automatically reduces the available creep flux.

Root-growth transport and dry-ravel export must also respect available mobile-soil mass.

### production priority

For Gounsa, prioritize:
1. actual `H_AB` distribution
2. shallow production behavior
3. sandstone matrix/cementation
4. fire-spall supply

over deep-regolith mineral-age complexity.


## Landlab implementation status

Current production scaffold:

```
Landlab grid
├─ soil__depth
├─ bedrock__elevation
├─ topographic__elevation
├─ custom sandstone production
│  ├─ Mode A: P0 exp(-H/gamma)
│  └─ Mode B: shallow finite-depth hump / zero-depth suppression sensitivity
└─ DepthDependentDiffuser
   └─ q_bg
```

The Landlab numerical scaffold is adopted for implementation convenience and mass-conserved state handling.

It is **not** the source of final Gounsa sandstone parameter values.

Root-growth/decay transport and dry ravel remain separate fluxes outside the residual-diffusion coefficient.

Tree throw/uprooting and shallow landslide remain outside the production baseline.
