# Gounsa hillslope vegetation-weathering handoff

날짜: 2026-09-21
브랜치: `gounsa-water-erosion-deep-review-2026-09-21`

## 이번 세션의 질문

고운사 100년 postfire model에서:

```
사면 위치
+
식생
+
수문
+
화학풍화
+
토양생산
+
침식/퇴적
```

을 어떻게 완전한 feedback으로 연결할 것인가?

---

## 핵심 결론

Chemical weathering은 더 이상 cell-local sink가 아니다.

현재 authoritative structure:

```
vegetation
 -> root water uptake / respiration / nutrient cycling
 -> hillslope hydrology / residence time / CO2
 -> chemical weathering
 -> nutrient release / mass loss
 -> soil-regolith state
 -> erosion/deposition / fresh-mineral supply
 -> chemical weathering
 -> vegetation
```

Topography is active through:
- slope
- hillslope length
- divide/channel position
- shallow/deep flow
- vertical connectivity
- saturation
- water table / deep drainage
- erosional vs depositional state

No direct aspect or hillslope-position multiplier is used.

---

## vertical profile architecture

Yoo & Mudd 2008 lineage:

```
PDZ
~ mobile A/B soil

CAZ
~ chemically altered but relatively immobile C/Cr

fresh parent
~ sandstone
```

Therefore:

```
H_AB != Z_weathered
```

and generally:

```
Z_water_table != Z_weathering_front
```

Initial subsurface weathering architecture is inherited.

The 100-year model simulates incremental change only.

---

## vegetation-weathering core pathways

### 1. root water uptake

Druhan & Bouchez 2024:

```
root water uptake
 -> lower drainage
 -> altered residence/reaction time
 -> weathering
```

### 2. root respiration

Tune 2020/2023, Osorio-Leon 2025, Stolze 2026:

```
root/belowground respiration
 -> pCO2
 -> carbonic-acid chemistry
 -> W_chem
```

Stolze 2026 provides an explicit intermediate structure:

```
R_root = k f(T) f(S_w)
```

but its original 0.2 m root zone is meadow-specific and not transferable.

Gounsa candidate:
```
LPJ-GUESS FineRootC(z)
 -> spatial root-respiration source
```
as NEW COUPLING.

### 3. nutrient uptake / litter return

Druhan & Bouchez 2024:

```
mineral weathering
 -> dissolved nutrient
 -> root uptake
 -> vegetation pool
 -> litter return
 -> upper-soil solution chemistry
```

This supports the intended return:
```
W_chem nutrient release
 -> LPJ-GUESS-CNP
```

### 4. geomorphic fresh-mineral supply

Yoo 2007/2009, Larsen 2023:

```
erosion/deposition
 -> fresh-mineral supply
 -> mineral residence
 -> W_chem
```

This pathway can dominate or mask vegetation effects.

---

## hillslope hydrology

Mandatory production/sensitivity states:

```
infiltration/recharge
shallow/deep flow partition
vertical connectivity
water residence time
saturation state
rock-moisture storage
optional groundwater/deep-flow state
```

Key papers:
- Maher 2010
- Anderson et al. 2018
- Xiao et al. 2021
- Wen et al. 2022
- Rempe & Dietrich 2018
- Hahm et al. 2022
- Barling et al. 2025
- Stolze et al. 2026

---

## weathering-front controls

### top-down

```
infiltration / O2 / reactive water
 -> downward weathering
```

Vegetation affects this through:
- root water uptake
- infiltration/permeability
- root respiration/CO2

### bottom-up

Rempe & Dietrich 2014:

```
channel incision
 -> fresh-bedrock drainage
 -> access by reactive fluids/gases
 -> weathering
```

### coevolution

Wang et al. 2021:

```
weathering front
!=
water table
```

in general.

Therefore:
- keep separate states
- do not hard-code one universal front-control mechanism

---

## hillslope response time

Ferrier & Perron 2020:

```
tau_diffusion ~ L^2 / D
```

Hillslope length can dominate chemical-erosion transient response time.

Thus:
- local slope is not enough
- divide/channel distance matters
- 100-year postfire weathering response is transient incremental change, not equilibrium

---

## sandstone/sedimentary hillslope evidence

### Yoo et al. 2009
Re-audited as a **sedimentary sandstone hillslope** study.

Key:
```
upper eroding slope
 -> colluvial mineral supply
 -> higher weathering

lower depositional slope
 -> thicker soil / longer residence
 -> equilibrium limitation
 -> lower weathering
```

### Donaldson et al. 2026
Metagreywacke sandstone with shale interbeds.

Current oak vs grass contrasts did not produce major differences in shallow cumulative chemical weathering.

Interpretation:
- inherited/paleo weathering matters
- deeper weathering differences track fracture density
- weathering base relates to water-table/stream elevation

Therefore current vegetation must not reset inherited weathering depth.

### Cooper et al. 2023
Sandstone plantation:
- deep roots use saprolite/saprock
- thicker lower-slope regolith can reflect colluvial deposition rather than deeper in-situ weathering

### Jo et al. 2007
Korean Jinju sandstone:
- root pressure
- joints
- infiltration
- physical and chemical weathering
co-occur.

### Potysz & Bartz 2024
Biotic chemical weathering sensitivity depends strongly on sandstone cement/mineralogy.

---

## vegetation-sensitive soil production

### Mode A
```
P_A(H)=P0 exp(-H/gamma)
```

baseline.

### Mode B
finite-depth hump / zero-depth suppression.

mandatory sensitivity.

Support:
- Heimsath 2009
- Rossi 2026
- SSSPAM 2025

### Mode C
optional vegetation-sensitive sensitivity.

Pelak 2016 structural precedent:

```
P(h,b)
=
[P0 + Pv b] exp(-ks h)
```

Schaller & Ehlers 2022 found broad soil-production variation was most consistent with soil-thickness + biomass formulations.

Rossi 2026 adds forested-mountain humped-production support.

Gounsa rule:
- no Pelak coefficient transfer
- no direct FineRootC multiplier
- Mode C is NEW COUPLING only

---

## strongest advanced spatial chemistry engine found

### Stolze et al. 2026 / PFLOTRAN

Published 2D mountain hillslope:
- 92,880 active cells
- 1 m horizontal
- 0.2 m vertical
- variably saturated flow
- gas-water exchange
- root respiration
- root exudates
- soil respiration
- transient climate
- multiple mineral kinetics
- slope/topography sensitivity

Current role:
- strongest advanced validation/alternative engine
- not immediately replacing WITCH/PROFILE first candidate due computational cost

Model file:
`models/PFLOTRAN_Mountain_Hillslope_Weathering.md`

---

## transport-weathering state

At minimum chemistry receives from SWEHR/Landlab:

```
erosional/depositional state
fresh-mineral fraction
imported-sediment fraction
effective mineral-residence proxy
```

Important:

```
soil age != mineral residence time
```

from Yoo & Mudd 2008.

---

## strongest new papers added in this pass

- 2000 Moulton et al.
- 2004 Mudd & Furbish
- 2007 Yoo et al.
- 2008 Yoo & Mudd geochemical soil formation
- 2008 Yoo & Mudd mineral residence
- 2009 Heimsath humped production
- 2010 Roering et al. biotic controls
- 2011 Anderson et al. Gordon Gulch
- 2014 Anderson et al. aspect CZ
- 2014 Hahm et al.
- 2014 Rempe & Dietrich
- 2015 Amundson et al.
- 2015 Milodowski et al.
- 2016 Chadwick & Asner
- 2016 Erlandsson et al.
- 2018 Anderson et al.
- 2018 Rempe & Dietrich
- 2019 Molina et al.
- 2020 Ferrier & Perron
- 2021 Anderson et al. Gordon Gulch
- 2021 Nielson et al.
- 2021 Smith & Bookhagen
- 2021 Wang et al.
- 2021 Xiao et al.
- 2022 Hahm et al.
- 2022 Meng et al.
- 2022 Schaller & Ehlers
- 2023 Cooper et al.
- 2023 Larsen et al.
- 2023 Rasmussen et al.
- 2024 Druhan & Bouchez
- 2024 Luo et al.
- 2025 Barling et al.
- 2025 Welivitiya et al.
- 2026 Donaldson et al.
- 2026 Rossi et al.
- 2026 Stolze et al.

---

## authoritative files

### decisions
- `decisions/2026-09-21_MYCORRHIZA_EXCLUSION.md`
- `decisions/2026-09-21_SOIL_WEATHERING_FOURTH_PASS_NON_MYCORRHIZAL.md`
- `decisions/2026-09-21_HILLSLOPE_VEGETATION_WEATHERING.md`

### models
- `models/Hillslope_Vegetation_Weathering.md`
- `models/Vegetation_Weathering_Coupling.md`
- `models/PFLOTRAN_Mountain_Hillslope_Weathering.md`
- `models/BioRT.md`
- `models/Sandstone_Soil_Production.md`
- `models/Landlab_ShallowSoil_Weathering_Creep.md`

---

## next work

1. LPJ-GUESS source/output audit:
   - root respiration
   - layer-wise root water uptake
   - FineRootC vertical profile
   - nutrient uptake / litter return

2. Gounsa site characterization:
   - sandstone petrography
   - cement type
   - fracture density
   - actual H_AB distribution
   - C/Cr/weathered-zone depth if data exist

3. hillslope hydrology implementation:
   - residence time
   - shallow/deep flow
   - rock moisture
   - optional groundwater/deep flow

4. chemical engine practicality:
   - WITCH/PROFILE
   - BioRT
   - reduced PFLOTRAN/Stolze

5. Mode C vegetation-sensitive soil-production sensitivity design

6. fire-spall + coarse-fragment supply/armour


---

## post-handoff continuation

추가로 검토/저장한 핵심 논문:

- `papers/2017_Hasenmueller_DeepRoots_BedrockFractures.md`
- `papers/2022_Primka_Hillslope_RootDynamics.md`
- `papers/2023_Donaldson_Aspect_Saprolite_Symmetry.md`
- `papers/2021_Wang_3DClimateTopography_Weathering.md`
- `papers/2015_Hasenmueller_Topographic_SoilCO2.md`
- `papers/2023_Kopp_Topography_SoilCO2_Efflux.md`
- `papers/2020_Tang_Sandstone_PreferentialFlow_Hillslope.md`
- `papers/2019_Sullivan_Aspect_FluxPIHM_WITCH_Vegetation.md`
- `papers/2023_Nudurupati_Landlab_TransientVegetationTopography.md`

핵심 추가결론:

### deep roots vary with hillslope position
Hasenmueller 2017:
```
hillslope hydrology
 -> fracture-root density / deep-root deployment
```

따라서 root access depth를 PFT 고정값으로만 보면 안 된다.

### root dynamics vary with moisture/topography
Primka 2022:
```
dry sites
 -> faster root-tip turnover

wetter/deeper soils
 -> larger standing crop / longer survival
```

이는 chemical weathering과 Gabet root transport 양쪽의 spatial vegetation state validation에 사용.

### current vegetation can be offset by hydrologic effects
Donaldson 2023:
```
north / woody
 -> deeper biological/root forcing
 -> stronger water withdrawal

south / grass
 -> more perched/lateral water
 -> stronger hydrologic weathering opportunity
```

결과적으로 saprolite thickness가 유사할 수 있음.

즉 vegetation effect 내부에도 반대부호 경로가 존재한다.

### CO2 source != pCO2
Hasenmueller 2015:
```
topography
 -> soil depth/moisture/gas diffusivity
 -> pCO2
```

Kopp 2023:
```
dry ridge
 -> water-limited respiration

wet valley
 -> oxygen-limited respiration
```

따라서:
```
R_CO2
!=
pCO2
```
를 유지한다.

### sandstone preferential flow
Tang 2020:
neighboring temperate-forest sandstone/shale catchments에서 preferential flow가 lithology, horizon structure, antecedent moisture, hillslope position에 따라 달랐다.

따라서:
```
deep flow fraction
!=
f(TWI)
```
단일식.

### direct hillslope hydrology + WITCH + vegetation precedent
Sullivan et al. 2019:
```
Flux-PIHM
+
WITCH
+
vegetation nutrient uptake / litter return
```

을 실제 결합.

Vegetation cycling inclusion improved solute-depth behavior but reduced net shale weathering by about 10%.

This is one of the strongest published integration precedents for the current Gounsa architecture.

### Landlab dynamic vegetation interface precedent
Nudurupati et al. 2023:
```
topography / climate
 -> dynamic tree-shrub-grass patterns
```
를 Landlab에서 구현.

Weathering engine은 아니므로 production source가 아니라 terrain-to-dynamic-vegetation implementation reference.

---

## current actual archive counts after continuation

```
Papers      397
Models       43
Decisions    23
Sessions     10
```

`INDEX.md` was regenerated from the actual branch tree.

Latest index commit:
`f734285051f11f6099d8fde0993ba2911da21e40`


---

## targeted sandstone mini-pass after timeout reduction

이번 패스는 전송시간 초과를 피하기 위해 3편만 확정했다.

### Xiao et al. 2019
파일:
`papers/2019_Xiao_SandstoneCatchment_Hydrology.md`

Garner Run sandstone forest catchment에서:
- longer hillslopes
- larger riparian zone
- bouldery/macroporous soils
- larger storage/connectivity

가 확인된다.

핵심:
```
sandstone mineralogy
 -> kinetics

sandstone-derived geomorphic/hydrologic architecture
 -> flow/residence
 -> W_chem
```

를 분리한다.

### Hoagland et al. 2017
파일:
`papers/2017_Hoagland_Sandstone_Flowpath_Geochemistry.md`

Garner Run stream chemistry는:
- shallow interflow
- spring
- groundwater
- hyporheic/lateral exchange

의 서로 다른 geochemical signatures를 혼합한다.

고운사 first production에서는 최소:
```
shallow
deep
lateral/mixed
```
weathering-water states로 축약한다.

### Phillips et al. 2008
파일:
`papers/2008_Phillips_Sandstone_EarlySoilFormation_Vegetation.md`

newly exposed resistant sandstone에서 <30 yr 동안 15-20 cm soil cover가 형성되었다.

reported 5-10 mm yr^-1는:
- in-situ weathering
- debris accumulation
- organic matter
- fracture infill
- microtopographic trapping

을 합한 soil-cover thickening이며 `P_sand`로 사용하지 않는다.

하지만:
```
thin sandstone/fracture state
 -> pedogenic preparation
 -> vegetation establishment
 -> faster local soil development
```

feedback이 decadal timescale에 가능하다는 강한 근거다.

### architecture updates

반영:
- `models/Hillslope_Vegetation_Weathering.md`
- `decisions/2026-09-21_HILLSLOPE_VEGETATION_WEATHERING.md`

이번 소묶음에서는 INDEX 전체 재생성을 하지 않았다. 다음 의미 있는 문헌묶음 종료 때만 재생성한다.
