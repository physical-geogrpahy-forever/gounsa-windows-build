# ForestGALES / fgr windthrow-risk lineage

## 목적
LPJ-GUESS woody cohort의 DBH, height, density/spacing, species state를 live-tree windthrow probability로 변환할 published mechanistic engine을 관리한다.

## 핵심 문헌
- Hale et al. 2012, European Journal of Forest Research 131, 203-217, DOI 10.1007/s10342-010-0448-2
- Hale et al. 2015, Environmental Modelling & Software 68, 27-41, DOI 10.1016/j.envsoft.2015.01.016
- ForestGALES 2.5 user manual, Forestry Commission / Forest Research
- public R implementation: `tom-locatelli/fgr`

## model type
ForestGALES is a hybrid mechanistic wind-risk model.

It calculates separately:
```
critical wind speed for overturning
critical wind speed for stem breakage
```

and combines critical wind speed with a wind-climate distribution to estimate:
- annual exceedance probability
- return period
- damage risk

## important inputs
Depending on method/version:
- species
- DBH
- tree height
- spacing / stand density
- crown geometry
- competition
- tree mechanical properties
- soil/rooting class or rooting depth
- exposure / wind climate
- edge/gap state

These inputs are unusually well aligned with LPJ-GUESS woody cohort states.

## overturning structure
ForestGALES balances wind-induced turning moment against root/soil anchorage.

The 2.5 technical appendix expresses critical wind speed for overturning in a form proportional to:

```
u_crit,over
~
sqrt(
  C_reg * SW
  /
  [wind-loading and aerodynamic terms]
)
```

where:
- `C_reg`: regression/anchorage coefficient
- `SW`: tree weight
- aerodynamic terms depend on spacing, height, gustiness, roughness and canopy properties

Stem breakage has a separate mechanical-resistance equation involving:
- MOR
- DBH^3
- knot factor
- aerodynamic loading

This distinction is essential for geomorphology:

```
overturning -> root plate / pit-mound event
stem breakage -> no root-plate excavation
```

Stem breakage belongs instead to CWD/deadwood pathways.

## wind probability
ForestGALES converts critical wind speed to a standardized 10-m wind speed and uses a Weibull/extreme-value formulation to estimate annual exceedance probability.

Therefore the model can provide a physically based event probability instead of an arbitrary annual uprooting rate.

For Gounsa, British DAMS calibration should not be used directly if local wind data are available.

Prefer:
```
local Korean wind distribution
or
event wind/gust forcing
```
with the mechanistic CWS model.

## individual-tree lineage
Hale et al. 2012 developed turning-moment-coefficient methods that incorporate:
- individual tree size
- competition
- local sheltering

This is suitable in principle for heterogeneous LPJ-GUESS woody cohorts, although cohort-to-individual representation is still required.

## validation
Hale et al. 2015 validates three ForestGALES versions against observed Scottish storm damage.

Tree height and local wind speed were major predictors of damage.

The mechanistic versions showed useful discrimination between damaged and undamaged stands, with differences in bias among versions.

## fgr public implementation
Repository:
`tom-locatelli/fgr`

DESCRIPTION reports:
- R implementation of ForestGALES
- traditional roughness stand method
- turning-moment-coefficient single-tree method
- critical wind speed for stem breakage and uprooting
- probability of damage when local wind-climate information is supplied
- parameterization for 23 tree species in the archived package version
- custom species parameters can be supplied

## source/license caution
The repository is public, but the licensing is **not simply unrestricted GPL**.

DESCRIPTION states:
```
GPLv3 + LICENCE.txt
```

The accompanying LICENCE adds a Commons Clause / non-commercial restriction and states that commercial use requires licensor consent.

Therefore:
```
public source
!= unrestricted FOSS license
```

For academic Gounsa research, use appears compatible with the stated non-commercial terms, but redistribution/commercialization must respect the additional licence.

The repository README also labels the archived fgr release as beta/testing software.

## Gounsa live-tree interface
Preferred:

```
LPJ-GUESS woody cohort
  DBH
  height
  density / spacing
  PFT/species
  rooting / soil state
        |
        v
ForestGALES / fgr
        |
        +--> CWS_overturn
        +--> CWS_break
        |
local/event wind
        |
        v
p_overturn
p_break
```

Only:
```
overturning
```
feeds the tree-throw pit/root-plate module.

## species issue
Current ForestGALES parameter sets are not a direct Korean-species calibration.

Do not silently map:
- Pinus densiflora
- Pinus koraiensis
- Quercus spp.
- other Gounsa woody PFTs

to a British species without sensitivity/calibration.

Local root-plate geometry can be constrained by Kim et al. 2014, but anchorage/mechanical parameters remain separate.

## postfire limitation
ForestGALES is mainly a live-standing-tree wind-risk model.

It does not by itself update:
- dead-root mechanical integrity
- fire-killed stem deterioration
- canopy combustion
- postfire snag decay

Therefore fire-killed standing trees use a separate Gallaway-type delayed-toppling pathway.

A future dead-tree wind model could multiply/modify anchorage resistance using the postfire root-integrity state, but that would be a **new coupling**.

## snow
ForestGALES 2.5 includes snow-related constants/inputs in its broader parameter framework, but the Gounsa snow-uprooting pathway is not yet adopted as a production module.

Park 2026 is retained as Korean susceptibility evidence.

## current judgment
**Adopt as the primary candidate for live-tree wind-driven overturning probability.**

Do not use it for:
- postfire snag decay
- root-plate volume
- sediment travel distance

Those are handled by separate published lineages.

## source files
- ForestGALES 2.5 user manual
- `tom-locatelli/fgr/DESCRIPTION`
- `tom-locatelli/fgr/LICENCE.txt`
