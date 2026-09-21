# Hillslope vegetation-weathering model lineage

## 목적

고운사 100년 postfire simulation에서 다음 feedback을 하나의 명시적 구조로 정리한다.

```
vegetation
<-> hillslope hydrology
<-> chemical weathering
<-> soil/regolith production
<-> erosion/deposition
<-> topography
<-> vegetation
```

이 문서는 하나의 published monolithic model을 주장하지 않는다.

각 process는 published lineage를 사용하고, 서로 다른 lineage 사이의 interface는 **NEW COUPLING**으로 명시한다.

---

## 1. 핵심 published lineages

### A. hillslope chemical mass balance

- Mudd & Furbish 2004
- Yoo et al. 2007
- Yoo & Mudd 2008
- Yoo et al. 2009
- Green et al. 2006
- Brosens et al. 2020

핵심:

```
soil production
+ upslope sediment input
- downslope sediment export
- chemical mass loss
= local soil/regolith mass change
```

Chemical weathering은 local cell chemistry만으로 결정되지 않고:
- material supply
- mineral residence
- erosion/deposition history
에 의존한다.

### B. hillslope hydrology and reactive transport

- Anderson et al. 2018
- Xiao et al. 2021
- Wen et al. 2022
- BioRT-Flux-PIHM 2022
- Erlandsson et al. 2016
- Stolze et al. 2026

핵심:

```
topography
 -> flow path
 -> vertical connectivity
 -> saturation
 -> residence time
 -> gas/solute delivery
 -> mineral reaction
```

Runoff total alone is not sufficient.

### C. vegetation-controlled deep hydrology

- Brantley et al. 2017
- Rempe & Dietrich 2018
- Hahm et al. 2022
- Barling et al. 2025
- Tune et al. 2020/2023
- Lapides et al. 2024
- Osorio-Leon et al. 2025

핵심:

```
root depth/distribution
 -> soil + weathered-bedrock water uptake
 -> rock-moisture storage/depletion
 -> recharge/drainage/residence
 -> weathering environment
```

따라서:

```
root access depth
>
mobile-soil thickness
```

를 허용한다.

### D. vegetation-sensitive soil production

- Pelak et al. 2016
- Amundson et al. 2015
- Schaller & Ehlers 2022
- Rossi et al. 2026
- Roering et al. 2010
- Heimsath et al. 2009

Pelak explicit structural precedent:

```
P(h,b)
=
[P0 + Pv b(h)] exp(-ks h)
```

with:

```
b(h)
=
(r/m)[1-exp(-kg h)]
```

This is not a sandstone calibration.

Rossi 2026 gives a forested-mountain Landlab precedent in which humped soil production plus depth-dependent creep reproduces aspect-dependent bedrock exposure and patchy soils.

Schaller & Ehlers 2022 find that observed soil-production variations most closely resemble formulations including both soil thickness and biomass.

### E. reverse geomorphology-to-vegetation feedback

- Hahm et al. 2014
- Milodowski et al. 2015
- Chadwick & Asner 2016

```
bedrock/weathering/erosion
 -> soil depth
 -> water/nutrient storage
 -> vegetation structure/productivity
```

This supports returning geomorphic and weathering state to LPJ-GUESS-CNP.

### F. current-state vs inherited weathering profile

- Rasmussen et al. 2023
- Donaldson et al. 2026
- Anderson et al. 2011/2021

Current vegetation/aspect can differ strongly while inherited saprolite/weathering-zone architecture retains older climate/vegetation/structural signals.

Therefore:

```
current vegetation
!=
equilibrium inherited weathering-profile thickness
```

### G. sandstone / sedimentary-rock constraints

Especially relevant:
- Yoo et al. 2009: sedimentary sandstone transient hillslope
- Donaldson et al. 2026: metagreywacke sandstone ridgetops
- Cooper et al. 2023: sandstone plantation regolith
- Potysz & Bartz 2024: sandstone biogeochemical weathering
- Pawlik et al. 2023: sandstone-root weathering field evidence
- Jo et al. 2007: Korean Jinju sandstone root/discontinuity/infiltration evidence
- Luo et al. 2024: East Asian mudstone toposequence

---

## 2. vertical profile architecture

Adopt a three-domain state inspired by Yoo & Mudd 2008.

```
surface
|
| mobile soil / PDZ
| H_AB
|
| chemically altered but largely immobile zone / CAZ
| H_CAZ or Z_weathered - H_AB
|
| fresh or weakly altered sandstone
|
bedrock
```

Gounsa mapping:

```
PDZ
~ mobile A/B soil

CAZ
~ C/Cr weathered zone / saprolitic material

fresh parent
~ sandstone below active weathering front
```

Important:

```
H_AB
!=
Z_weathered
```

and:

```
regolith thickness
!=
in-situ weathering depth
```

because depositional lower slopes may contain imported colluvium.

---

## 3. mandatory initial states

The 100-year postfire model does not build the full Critical Zone from zero.

Initialize:

```
H_AB(x,y,t0)
Z_weathered(x,y,t0)
z_bedrock(x,y,t0)
fracture/permeability state(x,y,t0)
coarse-fragment state(x,y,t0)
soil/rock moisture state
optional groundwater-depth state
mineral inventory / lithology
```

Donaldson 2026 and Rasmussen 2023 require an inherited-profile approach.

Do not impose:

```
Z_weathered(t0)
=
f(current LPJ-GUESS vegetation)
```

---

## 4. LPJ-GUESS interface

Required dynamic vegetation states:

```
PFT/cohort state
NPP
FineRootC(z)
root fraction by layer
root access depth
root water uptake by layer
root/belowground respiration
litter/SOM
nutrient uptake/return
soil temperature
soil water / runoff / drainage
```

No mycorrhizal state.

Optional sensitivity:
```
non-mycorrhizal root-derived DOC / organic ligand
```

---

## 5. hillslope hydrology interface

Production/sensitivity states should include:

```
infiltration/recharge
shallow vs deep flow partition
vertical connectivity
saturation state
water residence time
rock-moisture storage
gas transport / pCO2 where represented
```

### aspect rule

Do not use:

```
W = W0 * f(aspect)
```

Instead:

```
aspect
 -> radiation / snow / microclimate
 -> LPJ-GUESS vegetation and ET
 -> recharge / root uptake
 -> rock moisture / residence time
 -> W_chem
```

Barling 2025 shows that pole-facing oak slopes can withdraw more and deeper rock moisture than equator-facing grassy slopes despite lower insolation.

### hillslope-position rule

Do not use:

```
W = W0 * f(ridge/midslope/footslope)
```

Instead calculate/interpolate:
- erosion/deposition
- convergence
- saturation
- residence time
- imported sediment
- mineral freshness

Molina 2019 and Luo 2024 show why.

---

## 6. chemical-weathering engine

Primary first candidate remains:

```
LPJ-GUESS vegetation/hydrology
 -> WITCH / PROFILE-style mineral kinetics
```

Spatial alternatives/validation:
- BioRT-Flux-PIHM
- PFLOTRAN mountain-hillslope model of Stolze 2026
- Wen 2022 hillslope RTM
- Xiao 2021 vertical-connectivity RTM

Outputs:

```
W_chem [mass area^-1 time^-1]
nutrient release
secondary-mineral state
solute export
```

Important:
```
W_chem
!=
P_sand
```

---

## 7. transport-to-weathering feedback

SWEHR/Landlab updates:

```
physical erosion
deposition
soil depth
topography
surface coarse fragments
```

These must feed the weathering state.

At minimum derive:

```
erosional / depositional status
fresh-mineral exposure fraction
imported-sediment fraction
effective mineral-residence proxy
```

Published basis:
- Yoo 2007
- Yoo & Mudd 2008
- Yoo 2009
- Larsen 2023
- Green 2006

Full particle-age tracking is not mandatory for first implementation.

---

## 8. soil-production modes

### Mode A: exponential baseline

```
P_A(H)
=
P0 exp(-H/gamma)
```

Role:
- simple background sandstone-production benchmark

### Mode B: humped depth-dependent production

Required sensitivity:

```
P_B(H)
```

with:
```
P_B(0)
<
P_B(H_peak)
```

and decline at large H.

Field/model precedent:
- Heimsath 2009
- Rossi 2026
- SSSPAM 2025

Final Gounsa equation/parameters remain unresolved.

### Mode C: vegetation-sensitive production sensitivity

Candidate only:

```
P_C(H,V)
```

Published structural precedent:

```
P(h,b)
=
[P0 + Pv b] exp(-ks h)
```

from Pelak lineage.

For Gounsa:

```
V
```
is not yet defined.

Possible candidates:
- total root-zone biomass
- FineRootC in weathering-accessible layers
- a root-access weighted vegetation state

Do not use AGB by default.

Do not copy Pelak coefficients.

Mode C is a **NEW COUPLING sensitivity**, not baseline production.

---

## 9. chemical weathering to profile change

Mudd & Furbish 2004 supports:

```
W_chem
 -> soil mass loss
 -> H/z change
```

Yoo & Mudd 2008 supports a stronger future profile coupling:

```
chemical alteration
 -> CAZ evolution
 -> weathering-front advance

physical conversion
 -> CAZ to PDZ
```

For first implementation:
- retain W_chem as explicit dissolved mass loss
- retain P_sand separately

Future mechanistic sensitivity:
- couple RTM mineral depletion to weathering-front migration
- repartition P_sand to avoid double counting

---

## 10. vegetation feedback back from geomorphology

Return to LPJ-GUESS:

```
H_AB
root-accessible weathered depth
soil/rock moisture storage
nutrient pools
surface coarse fragments
local topography / drainage
```

Milodowski 2015 and Hahm 2014 support the direction:

```
geomorphic/weathering state
 -> water/nutrient availability
 -> forest structure/productivity
```

The exact LPJ-GUESS interface is NEW COUPLING.

---

## 10.1 non-mycorrhizal ecological interface after Druhan & Bouchez 2024

Druhan & Bouchez 2024 provides a direct published theoretical framework for ecological regulation of chemical weathering without requiring a biomass multiplier.

Three vegetation pathways are elevated to core interface status.

### A. root water uptake

```
root water uptake
 -> reduced drainage
 -> altered residence/reaction time
 -> altered weathering
```

This makes LPJ-GUESS layer-wise root water uptake a chemical-weathering input, not only an ecosystem water-balance output.

### B. root respiration

Use LPJ-GUESS root/belowground respiration if available.

If a direct suitable output is unavailable, Stolze 2026 provides a published kinetic intermediate form:

```
R_root
=
k * f(T) * f(S_w)
```

with spatial root distribution supplied by LPJ-GUESS.

Replacing Stolze's fixed 0.2 m rooting domain with LPJ-GUESS `FineRootC(z)` is NEW COUPLING.

### C. nutrient uptake and litter return

```
mineral dissolution
 -> dissolved nutrient

root nutrient uptake
 -> vegetation pool

litter turnover
 -> topsoil return / resolubilization
```

Nutrient uptake is therefore not treated as permanent export from the modeled Critical Zone.

This is directly compatible with the intended:

```
W_chem nutrient release
 -> LPJ-GUESS-CNP
 -> uptake / biomass / litter
 -> soil chemistry
```

return loop.

### D. geomorphic mineral-supply control

Separate from the three ecological pathways:

```
erosion / deposition
 -> fresh-mineral supply
 -> mineral residence
 -> W_chem
```

This pathway can dominate or mask vegetation effects, as Larsen 2023 demonstrates.

### first-production interface

```
LPJ-GUESS
├─ root water uptake(z,t)
├─ root respiration(z,t)
├─ nutrient uptake(z,t)
├─ litter return(t)
└─ FineRootC(z,t)

Landlab/SWEHR
├─ erosion/deposition
├─ H_AB
└─ fresh/imported material state

Hillslope hydrology
├─ drainage
├─ residence time
├─ saturation
└─ deep/shallow flow

        |
        v

WITCH / PROFILE
or advanced PFLOTRAN/BioRT
        |
        v
W_chem + nutrient release
```


## 11. key negative constraints

Do not use:
```
W_chem *= biomass multiplier
```

Do not use:
```
W_chem *= aspect multiplier
```

Do not use:
```
P_sand *= FineRootC multiplier
```
as baseline.

Do not set:
```
current vegetation -> entire inherited weathering depth
```

Do not infer:
```
footslope thicker regolith -> greater in-situ weathering depth
```

Do not equate:
```
soil age = mineral residence time
```

Do not include:
- mycorrhiza
- tree throw/uprooting
- shallow landslide

---

## 12. current production interpretation

For the first 100-year production implementation:

```
INHERITED PROFILE
H_AB + H_CAZ/Z_weathered + fracture/permeability

LPJ-GUESS
 -> vegetation/root/hydrology forcing

HILLSLOPE HYDROLOGY
 -> recharge
 -> shallow/deep partition
 -> residence time
 -> saturation / rock moisture

CHEMISTRY
 -> WITCH/PROFILE
 -> W_chem + nutrient release

GEOMORPHOLOGY
 -> SWEHR + Landlab
 -> erosion/deposition + H/z

SOIL PRODUCTION
 -> Mode A baseline
 -> Mode B mandatory sensitivity

VEGETATION-SENSITIVE PRODUCTION
 -> Mode C optional sensitivity only
```

---

## 12.1 hillslope length and response-time constraint

Ferrier & Perron 2020 couples:
- 3D topography
- soil thickness
- soil mineral abundance
- soil production
- soil transport
- mineral dissolution

and shows that transient chemical-erosion response time can be controlled primarily by hillslope length.

Characteristic transport context:

```
tau_diffusion
=
L^2 / D
```

Therefore:
```
local reaction rate
!=
landscape chemical-weathering response time
```

Gounsa implication:
- preserve divide-to-channel distance/hillslope length as spatial context
- do not interpret a 100-year run as new weathering equilibrium
- treat postfire change as incremental transient response

Vegetation can influence this response indirectly through hydrology, production and transport, but Ferrier & Perron does not provide a vegetation coefficient.

## 12.2 top-down and bottom-up weathering-front controls

### top-down
```
infiltration / O2 / reactive water
 -> downward reaction
 -> weathering-front advance
```

Vegetation can modify this through:
- ET/root water uptake
- infiltration
- root respiration/CO2
- root-zone permeability

### bottom-up
Rempe & Dietrich 2014:

```
channel incision
 -> fresh-bedrock drainage
 -> loss of stagnant equilibrated water
 -> access of reactive fluids/gases
 -> weathering
```

The groundwater/drainage geometry can therefore constrain the lower weathering boundary.

### coevolution
Wang et al. 2021 shows:

```
Z_water_table
!=
Z_weathering_front
```

in general, especially during transient evolution.

Weathering-induced porosity/permeability can feed back on infiltration and hydrology.

### Gounsa rule

Maintain separate states:
```
Z_weathered
Z_water_table or deep-flow state
fracture/permeability state
```

Do not hard-code either:
```
weathering front = water table
```
or:
```
weathering front = top-down infiltration depth
```

Use both as end-member/sensitivity controls until site hydrology is constrained.


## 12.3 direct hillslope hydrology + WITCH + vegetation precedent

Sullivan et al. 2019 is a direct published coupling of:

```
Flux-PIHM hydrology
+
WITCH mineral weathering
+
vegetation nutrient uptake / litter return
```

on opposing forested hillslopes.

This is especially important because vegetation cycling did not simply increase weathering.

Published result:
- adding vegetation cycling improved depth-dependent solute behavior
- net shale weathering decreased by about 10%

Therefore:

```
vegetation nutrient cycling
 -> weathering
```

can have a negative net effect even within a mechanistic hydrology-weathering model.

This strongly supports keeping:
- nutrient uptake
- litter return
- hydrology
- mineral kinetics

as separate fluxes rather than a positive vegetation multiplier.

For Gounsa:

```
Flux-PIHM vegetation term
 ->
LPJ-GUESS nutrient uptake / litter return
```

is a NEW COUPLING.

## 12.4 CO2 production versus pCO2 state

Hasenmueller et al. 2015 and Kopp et al. 2023 show that:

```
CO2 production rate
!=
soil pCO2
```

because pCO2 also depends on:
- soil depth
- moisture
- porosity
- gas diffusivity
- topographic convergence
- oxygen limitation

Thus the Gounsa chemistry interface should conceptually separate:

```
CO2 source
=
root + heterotrophic respiration

from

pCO2 state
=
source
+ gas transport / retention
```

Minimum sensitivity variables:
- local saturation
- soil depth
- porosity/gas diffusivity
- convergent vs divergent position

Kopp 2023 further indicates the moisture response is non-monotonic:
- dry ridges can be water-limited
- wet valleys can be oxygen-limited

Therefore:

```
R_CO2 = f(T, moisture, saturation, vegetation)
```

should permit suppression under excessive saturation.

## 12.5 sandstone preferential-flow constraint

Tang et al. 2020 directly compared neighboring temperate-forest shale and sandstone catchments.

In the sandstone catchment, preferential-flow frequency and vertical pathway depended on:
- hillslope position
- antecedent moisture
- soil horizon structure
- lithology

This means:

```
deep flow fraction
!=
f(TWI or aspect alone)
```

For Gounsa, shallow/deep flow partition should include sandstone profile/horizon and permeability/fracture information.


## 12.6 vegetation-fracture preferential flow

Uhlemann et al. 2024 provides direct mountain-hillslope evidence that:

```
tree locations
+ fractures
 -> vertical preferential flow
 -> deeper rock-moisture recharge
```

while adjacent steep shallow-bedrock zones can otherwise be dominated by shallow lateral flow.

Gounsa implication:

```
vertical connectivity
!= function of slope alone
```

It may require:
- root presence/depth
- fracture/permeability state
- vegetation cover

as joint controls.

This is a NEW COUPLING if LPJ-GUESS root state modifies deep-flow partition.

## 12.7 lateral forest-soil weathering

Bower et al. 2023 shows strong hillslope-scale chemical-weathering gradients in temperate forested podzols.

Reported plagioclase loss:
- lateral eluvial: ~74%
- lateral illuvial: ~39%
- vertical podzol: ~23%

Thus:
```
lateral flushing
 -> substantially greater mineral depletion
```

can occur over short hillslope distances.

This strengthens the requirement to preserve:
- upslope water delivery
- lateral throughflow
- depth to bedrock
- flow-path history

in spatial weathering sensitivity.

## 12.8 hillslope hydrology evolves with soil and vegetation

Hartmann & Blume 2024 shows in glacial chronosequences that:

```
soil formation + vegetation succession
 -> changing preferential/lateral flow
 -> changing water storage
```

and that geology strongly controls this trajectory.

For Gounsa:
- first implementation may hold hydraulic structure mostly prescribed
- sensitivity should allow gradual postfire/recovery modification of infiltration partition and organic-layer effects

## 12.9 hillslope length to weathering-depth field evidence

Pedrazas et al. 2021 confirms that deeper weathering fronts can scale with ridge-valley spacing.

Observed:
- shallow weathering front near ~7 m under ridges
- deeper front ~11 m under similar ridges
- ~17.5 m under a ridge with nearly twice the ridge-valley spacing

This field evidence supports:
```
hillslope length / relief
 -> inherited weathering depth
 -> rock-moisture storage
```

and complements Ferrier & Perron 2020.


## 12.10 sandstone hydrologic architecture after Xiao 2019 and Hoagland 2017

Xiao et al. 2019 shows that the forested sandstone Garner Run catchment differs from neighboring shale not only in mineralogy but in:
- hillslope length
- drainage density
- bouldery/macroporous soils
- riparian-zone fraction
- water-storage capacity
- subsurface connectivity

Thus sandstone enters the weathering model through two distinct pathways:

```
sandstone mineralogy
 -> reaction kinetics

sandstone-derived geomorphic / soil architecture
 -> infiltration / storage / flow paths
 -> residence time
 -> W_chem
```

Do not collapse these into a single lithology factor.

Hoagland et al. 2017 further shows that sandstone headwater chemistry mixes distinct contributions from:
- shallow/interflow water
- spring water
- groundwater
- hyporheic/lateral exchange

For the Gounsa hillslope core, use the reduced distinction:

```
shallow flow
deep flow
lateral residence / mixing
```

rather than one bulk drainage flux.

The hyporheic-zone module itself is optional.

## 12.11 decadal sandstone vegetation-pedogenesis feedback

Phillips et al. 2008 observed rapid soil-cover development on newly exposed resistant sandstone over less than three decades.

The important sequence is:

```
fracture weathering
+ debris/moisture trapping
 -> pedogenic preparation
 -> vegetation establishment
 -> organic/root effects
 -> faster local soil development
```

This demonstrates that vegetation-soil feedback can operate on decadal timescales relevant to the 100-year Gounsa simulation.

However the reported soil-cover thickening:
```
~5-10 mm yr^-1
```
is NOT a pure bedrock-to-soil production rate because it includes accumulation, organic material, fracture infill and local trapping.

Therefore it cannot parameterize `P_sand`.

Use it only as:
- timescale evidence
- qualitative support for Mode B/Mode C sensitivity
- support for explicit debris/organic accumulation separation


## 13. strongest papers for Gounsa

### direct sandstone/sedimentary hillslope relevance
1. Yoo et al. 2009
2. Donaldson et al. 2026
3. Cooper et al. 2023
4. Jo et al. 2007
5. Potysz & Bartz 2024

### strongest hillslope hydrology-weathering models
1. Stolze et al. 2026
2. Anderson et al. 2018
3. Xiao et al. 2021
4. Wen et al. 2022
5. BioRT-Flux-PIHM

### strongest vegetation-sensitive soil-production evidence
1. Pelak et al. 2016
2. Schaller & Ehlers 2022
3. Rossi et al. 2026
4. Amundson et al. 2015
5. Roering et al. 2010

### strongest caution / limiting-process evidence
1. Larsen et al. 2023
2. Donaldson et al. 2026
3. Rasmussen et al. 2023
4. Anderson et al. 2021
5. Oeser & von Blanckenburg 2020

## final judgment

No single published model currently satisfies:

```
dynamic forest vegetation
+
hillslope-position hydrology
+
reactive chemical weathering
+
sandstone soil production
+
erosion/deposition
+
100-year postfire disturbance
```

The Gounsa model therefore remains modular.

This is consistent with Meng et al. 2022, which identifies underrepresentation of biotic processes in existing soil-landscape evolution models.

The current best architecture is a process-constrained NEW COUPLING, not a claim that one published model already does everything.
