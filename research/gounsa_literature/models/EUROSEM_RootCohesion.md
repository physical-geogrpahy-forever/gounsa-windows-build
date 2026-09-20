# EUROSEM root-cohesion lineage

## 핵심 논문
- Morgan et al. (1998), EUROSEM dynamic erosion model
- De Baets et al. (2008), DOI 10.1002/esp.1647
- De Baets et al. (2020), DOI 10.1038/s42003-020-0886-4

## 고운사에서 조사한 이유
Quantitative roots may alter concentrated-flow erosion through **erosion-specific soil cohesion**, rather than only through a generic vegetation cover or erodibility multiplier.

## EUROSEM base
EUROSEM explicitly simulates:
- interrill and rill flow
- rainfall detachment
- flow detachment
- sediment transport/deposition
- dynamic rill geometry

But its spatial routing is linked slope/channel elements, not genuine 2D SWE.

## De Baets 2008 modification
```
root density / root architecture
 -> calculated soil cohesion
 -> EUROSEM flow detachment
```

The modified model performs scenario simulations with root-dependent cohesion.

## De Baets 2020 mechanistic extension
RLD and root micro-traits determine heterogeneous local soil cohesion.

```
c_Max = c_Bare [1 + gamma(RLD_T) R]
c_Min = c_Bare [1 + gamma(RLD_T) r]
gamma(x) = M_max tanh(M1 x / M_max)
```

Erosion is controlled by comparison of hydraulic shear and root-reinforced soil mechanical resistance.

## importance for Gounsa
This lineage gives a published mechanism for:
```
quantitative root amount
 -> erosion-specific mechanical resistance
```

It is conceptually distinct from:
- landslide root tensile reinforcement
- WEPP Kr/Ki root multipliers
- vegetation cover factors

## limitation
- no genuine 2D catchment hydrodynamics
- species/soil-specific root-cohesion parameterization
- rainfall/interrill root effects remain less directly resolved

## current judgement
**Core root-resistance submodel lineage, not final hydrodynamic engine.**

A Gounsa 2D engine using this root-cohesion relation would be a **new coupling**.
