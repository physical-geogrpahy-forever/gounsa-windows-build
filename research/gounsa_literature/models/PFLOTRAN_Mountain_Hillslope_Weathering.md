# PFLOTRAN mountain-hillslope weathering lineage

## 핵심 논문
Stolze et al. (2026). *Model-Based Interpretation of Solute Exports and Carbon Partitioning During Shale Weathering in a Mountainous Hillslope*. Water Resources Research 62, e2025WR041597. DOI: 10.1029/2025WR041597.

## 고운사에서 검토한 이유
사면 geometry, variably saturated flow, soil/root respiration, gas exchange, transient climate forcing, mineral dissolution을 한 2D model에서 동시에 계산하는 published engine이 있는지 확인하기 위해 검토했다.

## 공간 구조
PFLOTRAN 기반 2D hillslope.

Published model:
```
92,880 active elements
dx = 1 m
dz = 0.2 m
```

continuous domain:
- soil
- saprolite/regolith
- bedrock
- hillslope to floodplain/toe

## 수문
Variably saturated flow uses Richards equation.

Conceptually:
```
porosity * dS_w/dt
=
div(K * k_r * hydraulic gradient)
+
source/sink
```

The source/sink includes:
- infiltration
- evapotranspiration

Subsurface hydraulic properties use van Genuchten-Mualem relationships.

## biological forcing

### soil respiration
The model separates:
- heterotrophic soil-OM respiration
- autotrophic root respiration

### root respiration
Published root-respiration/exudation source:

```
R_root
=
k
* Arrhenius(T)
* f(S_w)
```

where:
- k differs for CO2 release and exudate release
- T is local temperature
- S_w is local liquid saturation

Published activation energy for root respiration:
```
Ea = 75 kJ mol^-1
```

reported as approximately:
```
Q10 = 3.1
```

In the original meadow application, this source was applied over:
```
rooting depth = 0.2 m
```

This depth is site-specific and is NOT transferred to Gounsa.

## organic matter
Soil DOM comes from:
- litter in infiltrating water
- depolymerization of soil OM
- root exudates

Release/mobilization depends on water saturation.

This is useful because:
```
drying / rewetting
 -> DOM availability
 -> respiration / chemistry
```
is explicitly represented.

For Gounsa, explicit root-exudate chemistry remains optional sensitivity.

## mineral reactions
Original model includes:
- dolomite
- albite
- quartz
- pyrite
- Fe hydroxide
- calcite
- chlorite
- illite

Silicate/carbonate/clay dissolution uses a TST-style parallel-rate formulation.

Conceptually:

```
R_m
=
A_m
[
k_H2O(T)
+ k_H+(T) a_H+^x
+ k_OH-(T) a_OH-^y
+ k_CO2(T) a_CO2^z
]
(1 - IAP/K_eq)
```

Thus mineral reactions respond explicitly to:
- reactive surface area
- temperature
- pH
- aqueous CO2
- saturation state

## multiphase gas transport
The model explicitly handles:
- CO2 gas
- O2 gas
- gas-water exchange
- diffusion through unsaturated pores

This matters because:
```
higher water saturation
 -> lower gas diffusion

lower water saturation
 -> deeper O2 penetration
```

## slope/topography effect
Stolze et al. tested synthetic average slopes from:
```
14% to 55%
```

Steeper slopes:
- enhanced drainage
- lowered near-surface saturation
- increased deep reactant delivery
- increased O2 diffusion
- changed CO2 transfer
- increased several mineral reaction rates

Original shale results, for example:
- soil CO2 retained belowground rose from 1.36% to 4.45%
- dolomite dissolution rose 0.38 to 0.92 mol m^-2 yr^-1
- albite dissolution rose more modestly 2.36 to 2.88 mol m^-2 yr^-1

These values are site-specific and MUST NOT be transferred to Gounsa.

Important:
```
slope
 -> hydrology
 -> reaction environment
```
not:
```
slope -> direct weathering multiplier
```

## local topography
Sharp terrain features caused streamline divergence and localized deeper delivery of dissolved O2/CO2.

Thus:
```
mean slope alone
!=
full topographic weathering control
```

## transient forcing
The paper explicitly compares transient vs steady hydrologic/thermal forcing.

Hydrologic pulses changed reaction pathways strongly.

This supports preserving:
- seasonal infiltration
- soil moisture
- temperature
- respiration
rather than using only annual mean forcing.

## vegetation interpretation for Gounsa

Original:
```
fixed shallow rooting domain
+
prescribed/calibrated root respiration
```

Gounsa candidate:

```
LPJ-GUESS
├─ FineRootC(z)
├─ root fraction by layer
├─ root access depth
├─ root respiration / root C flux
├─ root water uptake
└─ soil T / moisture
        |
        v
PFLOTRAN root/soil respiration source field
        |
        v
2D multiphase reactive transport
```

This replacement is a **NEW COUPLING**.

## relation to BioRT / WITCH

### WITCH / PROFILE
Pros:
- vegetation/forest coupling precedent strongest
- lighter chemistry architecture

Cons:
- less complete spatial multiphase hillslope hydrology

### BioRT
Pros:
- watershed spatial hydrology
- plant uptake / respiration
- lighter than full PFLOTRAN

### PFLOTRAN / Stolze
Pros:
- strongest current hillslope-scale mechanistic structure
- transient 2D unsaturated flow
- gas transport
- soil/root respiration
- multiple mineral reactions
- slope/local-topography sensitivity
- public reproducible code/data

Cons:
- high computational cost
- shale-specific original reaction network
- vegetation succession not prognostic
- topography does not evolve internally

## relation to Landlab/SWEHR

Potential advanced architecture:

```
Landlab
 -> topography / H / weathered depth

LPJ-GUESS
 -> roots / ET / respiration

SWEHR
 -> surface erosion/deposition

        all
        |
        v

PFLOTRAN
 -> subsurface water/gas/reactive transport
 -> W_chem / nutrients
```

Required reconciliation:
- avoid double-counting hydrology
- avoid duplicated ET
- synchronize changing topography
- map erosion/deposition to mineral inventory
- mass-conserve W_chem

## current judgment

**Strongest advanced spatial chemical-weathering validation/alternative engine found so far.**

For first production:
- do not immediately replace WITCH/PROFILE
- preserve Stolze root-respiration and multiphase-hydrology equations as implementation candidates
- test a reduced hillslope version before domain-wide 100-year runs

The most attractive transferable component is:

```
root respiration source
=
temperature response
x saturation response
x spatial root state
```

with LPJ-GUESS providing the spatial root state.

## code/data
The paper reports:
- input and simulation results on ESS-DIVE
- augmented PFLOTRAN source archived on Zenodo
- code modifications include depth-dependent temperature and Reaction Sandboxes

## exclusions
No mycorrhiza.
No tree throw.
No shallow landslide.

## references
https://doi.org/10.1029/2025WR041597
