# Gounsa literature session handoff

날짜: 2026-09-21
브랜치: `gounsa-water-erosion-deep-review-2026-09-21`

## 이번 구간의 핵심 사용자 수정
1. 고운사 parent material은 sandstone.
2. tree throw / uprooting은 현재 필요하지 않음.
3. shallow landslide도 current production baseline에서 제외.

이 세 조건은 이후 작업에서 우선한다.

## 현재 production geomorphic scope

```
water erosion
+ residual background creep
+ root-growth/decay biogenic transport
+ postfire dry ravel
+ sandstone soil production
+ chemical dissolved weathering
+ fire spall/coarse fragments
```

Excluded:
```
tree throw / uprooting
shallow landslide
```

## water erosion
Baseline:
SWEHR / McGuire 2016, genuine 2D Hairsine-Rose.

Hourly rain is external forcing.
SWEHR integrates internally at sub-hourly CFL timesteps.

LPJ-GUESS native root states feed a new SWEHR resistance coupling.
Surface litter and root resistance remain separate.

## hillslope transport

```
q_hill
=
q_bg
+
q_rootgrowth
+
q_dryravel
```

### residual creep
```
q_bg
=
-D*_bg H_active grad(z)
```

Main lineage:
Furbish et al. 2009.

`D*_bg` is a residual local-creep coefficient, not total natural diffusivity.

### root-growth/decay transport
Gabet et al. 2003 exact recovered form:

```
q_sx
=
-[0.003 r tau / (rho_r log(beta))]
sin(theta) cos(theta)
```

Use LPJ-GUESS native root state/turnover/root distribution.

### dry ravel
Separate postfire process:
Lamb lineage with Roering-Gerber / Jackson-Roering support.

## sandstone soil production

Latest decision:
`decisions/2026-09-21_SANDSTONE_WEATHERING_BASELINE.md`

Baseline:

```
P_sand(h)
=
P0_sand exp(-h/gamma_sand)
```

Key sandstone evidence:

### Evans et al. 2019
Temperate sandstone:
```
0.026-0.096 mm yr^-1
```

Conifer woodland mean:
```
0.070 +/- 0.010 mm yr^-1
```

### Evans et al. 2021
Fitted sandstone analogues:

```
P0_sand
=
0.071-0.274 mm yr^-1
```

```
gamma_sand
=
0.80-4.50 m
```

These are analogue/sensitivity bounds only.

Final Gounsa parameters require sandstone petrography:
- matrix abundance
- cement type
- grain composition
- permeability
- tensile strength
- fracture density

Uiseong regional sedimentary studies can constrain context, but exact Gounsa formation/petrography is not yet verified.

## timescale warning
Heimsath/Evans production functions are cosmogenic long-term averages.

Annual evaluation of `P_sand(h)` is bookkeeping for a slow process.
It does not turn the equation into a year-to-year climate-response model.

Role split:

```
P_sand(h)
 -> slow parent-material to mobile-soil production

LPJ-GUESS/Hartmann
 -> daily climate/hydrology-sensitive chemical dissolved loss
```

Do not add climate or biomass multipliers to `P_sand` without separate evidence.

## mobile-soil mass balance

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

Use consistent density/porosity units.

## chemical weathering
Hartmann / LPJ-GUESS-CNP supplies bulk chemical dissolved-loss forcing.

Keep:
```
P_sand
!=
W_chem
```

P release and bulk weathering are separate variables.

## advanced optional models
DynSoil/MErSiM:
- optional transient mineral-age/deeper-regolith state
- not production baseline

Braun 2016:
- optional groundwater-driven weathering-front model

Granite papers:
- cross-lithology comparison only
- not parameter constraints for Gounsa

## sandstone/root paper
Pawlik et al. 2023:
- roots penetrate sandstone fractures and contribute to fragment separation/rhizosphere alteration
- mechanism support only
- no universal root biomass -> soil-production coefficient
- do not multiply `P_sand` by LPJ-GUESS roots in baseline

## key updated files

### decisions
- `decisions/2026-09-21_GEOMORPH_SCOPE_CORRECTION.md`
- `decisions/2026-09-21_BACKGROUND_CREEP.md`
- `decisions/2026-09-21_WEATHERING_MASS_BALANCE.md`
- `decisions/2026-09-21_SANDSTONE_WEATHERING_BASELINE.md`

### models
- `models/Short_Timestep_Weathering_HillslopeTransport.md`
- `models/Residual_Background_Creep.md`
- `models/Sandstone_Soil_Production.md`
- `models/Weathering_MassBalance_Regolith.md`
- `models/DynSoil_MErSiM.md`

### key papers
- `papers/2003_Gabet_BioturbationSedimentTransport.md`
- `papers/2001_Heimsath_OregonCoast_Sandstone_SoilProduction.md`
- `papers/2014_Marshall_OregonSandstone_RockStrength_SoilProduction.md`
- `papers/2019_Evans_Sandstone_SoilFormation_UK.md`
- `papers/2021_Evans_Sandstone_Matrix_SoilFormation.md`
- `papers/2023_Pawlik_SandstoneRootsSoilProduction.md`
- `papers/2015_Lee_Uiseong_Cretaceous_Sandstone_Petrography.md`

## INDEX state before adding this handoff
- Papers 312
- Models 37
- Decisions 16
- Sessions 5

After this handoff, regenerate INDEX so Sessions becomes 6.

## next priority
Do not return to uprooting or shallow-landslide work.

Best next tasks:
1. exact Gounsa sandstone petrography / formation identification
2. select a defensible `P0_sand`, `gamma_sand` sensitivity set
3. fire-spall production on sandstone
4. coarse-fragment supply versus armour
5. after that, implementation integration


## shallow-soil correction

User clarified:
```
sandstone + shallow soil
```

Required sandstone-production sensitivity:
```
mode A = Evans exponential
mode B = finite-depth shallow-soil peak / zero-depth suppression
```

Oregon sandstone evidence permits peak production around roughly 15-30 cm and lower production nearer exposed bedrock.

For Evans et al. 2021 site-specific exponential fits and H_AB = 0.05-0.30 m, simple 100-year analogue production is approximately:
- Comer: 7.2-7.6 mm
- Hilton: 15.7-17.2 mm
- Rufford: 6.2-6.9 mm
- Woburn: 18.8-25.7 mm

These are sensitivity values, not Gounsa predictions.

Shallow soil also directly limits:
```
q_bg = -D*_bg H_active grad(z)
```

Current hillslope production baseline remains:
```
q_hill = q_bg + q_rootgrowth + q_dryravel
```

Tree throw/uprooting and shallow landslide remain excluded.
