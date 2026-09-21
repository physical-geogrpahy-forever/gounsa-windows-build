# 결정: 사면 위치 + 식생 + 풍화 production architecture

날짜: 2026-09-21

## 질문

고운사 100년 postfire model에서:

```
식생
+
사면 위치
+
화학풍화
+
토양생산
+
침식/퇴적
```

을 어떻게 함께 계산할 것인가?

---

## 결정 1. aspect와 hillslope position을 직접 weathering multiplier로 쓰지 않는다

금지:

```
W = W0 f(aspect)
```

금지:

```
W = W0 f(ridge/midslope/footslope)
```

근거:
- Anderson 2014/2018
- Molina 2019
- Rasmussen 2023
- Barling 2025
- Donaldson 2026
- Luo 2024

대신:

```
topography/aspect
 -> microclimate / radiation
 -> vegetation
 -> hydrology
 -> flow path / residence
 -> W_chem
```

및:

```
hillslope position
 -> erosion/deposition
 -> convergence/saturation
 -> sediment supply/residence
 -> W_chem
```

를 process-wise 계산한다.

---

## 결정 2. inherited weathering profile을 초기조건으로 둔다

100년 model에서 current vegetation으로 전체 saprolite/weathering profile을 equilibrium reset하지 않는다.

필수 initial states:

```
H_AB(t0)
Z_weathered(t0) or H_CAZ(t0)
bedrock elevation
fracture/permeability state
mineralogy
coarse-fragment state
rock-moisture / hydrologic state
```

근거:
- Rasmussen 2023
- Donaldson 2026
- Anderson 2011/2021

100년 동안 계산하는 것은:

```
incremental postfire change
```

이다.

---

## 결정 3. vertical profile을 mobile soil / chemically altered zone / fresh parent로 분리한다

Yoo & Mudd 2008 lineage 채택:

```
PDZ ~ mobile A/B soil
CAZ ~ C/Cr weathered but relatively immobile zone
fresh parent ~ sandstone
```

따라서:

```
H_AB
!=
Z_weathered
```

이다.

또:
```
regolith thickness
!=
in-situ weathering depth
```
이다.

Cooper 2023은 sandstone hillslope에서 lower-slope thick regolith가 colluvial accumulation일 수 있음을 보여준다.

---

## 결정 4. vegetation effect on chemical weathering은 process-specific core로 유지

Core:

```
FineRootC(z)
root access depth
root water uptake by layer
root/belowground respiration
litter/SOM
nutrient uptake/return
soil temperature
soil water/drainage
```

No mycorrhiza.

Optional only:
```
non-mycorrhizal DOC / organic ligand
```

No scalar biomass/NPP multiplier.

---

## 결정 5. hillslope hydrology에 residence time / connectivity를 추가한다

Mandatory production/sensitivity target:

```
infiltration/recharge
shallow/deep flow partition
vertical connectivity
water residence time
saturation
rock-moisture storage
```

근거:
- Maher 2010
- Anderson 2018
- Xiao 2021
- Wen 2022
- Rempe 2018
- Hahm 2022
- Barling 2025
- Stolze 2026

특히:
```
runoff total
!=
complete weathering hydrology
```

이다.

---

## 결정 6. erosion/deposition을 chemistry에 다시 연결한다

SWEHR/Landlab outputs:

```
physical erosion
deposition
soil-depth change
surface exposure
```

에서 최소:

```
erosional/depositional state
fresh-mineral fraction
imported-sediment fraction
mineral-residence proxy
```

를 chemistry interface에 전달한다.

근거:
- Green 2006
- Yoo 2007
- Yoo & Mudd 2008
- Yoo 2009 sandstone
- Larsen 2023

Full mineral-age distribution은 first implementation에 필수는 아니다.

---

## 결정 7. soil-production Mode A/B 유지, Mode C 추가 검토

### Mode A
```
P_A(H)=P0 exp(-H/gamma)
```

baseline.

### Mode B
humped finite-depth production.

mandatory sensitivity.

근거 강화:
- Heimsath 2009
- Rossi 2026
- Welivitiya 2025

### Mode C
vegetation-sensitive soil-production sensitivity.

Published structural precedent:
```
P(h,b)
=
[P0 + Pv b] exp(-ks h)
```
Pelak 2016.

Supporting:
- Schaller & Ehlers 2022
- Amundson 2015
- Rossi 2026
- Roering 2010

하지만:

```
LPJ-GUESS state -> b
```
mapping은 published하지 않은 NEW COUPLING이다.

따라서 Mode C는:
- optional sensitivity
- not baseline
- no coefficient transfer

로 제한한다.

---

## 결정 8. vegetation signal보다 erosion signal이 강할 수 있다

Larsen 2023:
forest / grassland / unvegetated contrast보다 erosion-rate contrast가 soil production and chemical weathering rates를 더 강하게 제어했다.

Moulton 2000:
slope/lithology/microclimate를 최대한 통제한 basalt setting에서는 trees가 weathering을 강하게 증가시켰다.

이 둘을 함께 보면:

```
vegetation effect
= real
but
= limiting-process dependent
```

이다.

따라서 고운사에서 universal vegetation factor를 만들지 않는다.

---

## 결정 9. sandstone-specific interpretation

핵심 sandstone/sedimentary lineage:

### Yoo 2009
sedimentary sandstone transient hillslope.
Weathering depends strongly on:
- colluvial mineral supply
- residence time
- erosional vs depositional state

### Donaldson 2026
metagreywacke sandstone ridgetops.
Current oak vs grass contrast가 커도 shallow cumulative weathering은 paleo legacy 때문에 비슷할 수 있음.
Deep differences become fracture-controlled.
Weathering base aligns with water-table/stream elevation.

### Cooper 2023
sandstone plantation.
Deep roots use saprolite/saprock.
Lower-slope regolith thickness can reflect colluvial addition, not deeper in-situ weathering.

### Potysz 2024
biotic chemical weathering sensitivity strongly depends on sandstone cement/mineralogy.

### Jo 2007
Korean Jinju sandstone:
root pressure, joints, infiltration, physical and chemical weathering co-occur.

결론:
Gounsa petrography/fracture state remains mandatory before final parameterization.

---

## 결정 10. reverse feedback to vegetation is required

Return variables to LPJ-GUESS:

```
mobile soil depth
root-accessible weathered depth
soil/rock moisture storage
nutrient pools
local drainage state
coarse-fragment surface state
```

근거:
- Hahm 2014
- Milodowski 2015
- Chadwick & Asner 2016

This return is a NEW COUPLING.

---

## 결정 11. current first implementation

```
INHERITED PROFILE
 -> H_AB + CAZ/Z_weathered + fractures

LPJ-GUESS
 -> roots / respiration / ET / litter / nutrients

HILLSLOPE HYDROLOGY
 -> infiltration / recharge
 -> shallow/deep flow
 -> residence time / rock moisture

CHEMISTRY
 -> WITCH/PROFILE first candidate
 -> W_chem + nutrient release

GEOMORPHOLOGY
 -> SWEHR + Landlab
 -> erosion/deposition + H/z

SOIL PRODUCTION
 -> Mode A baseline
 -> Mode B mandatory sensitivity
 -> Mode C optional vegetation-sensitive sensitivity
```

BioRT/PFLOTRAN/Stolze lineage is the main spatial validation/advanced alternative.

---

## 결정 12. vegetation-weathering interface를 세 개의 직접 생태경로로 고정

Druhan & Bouchez 2024와 Stolze 2026 원문 재검토를 반영한다.

### root water uptake
```
LPJ-GUESS root water uptake
 -> drainage / residence-time modification
 -> W_chem
```

### root respiration
```
LPJ-GUESS root/belowground respiration
 -> pCO2 / carbonic acid
 -> W_chem
```

직접 출력 사용이 어려울 경우 Stolze 2026의:
```
R_root = k f(T) f(S_w)
```
형태를 intermediate process candidate로 검토한다.

단, Stolze의 0.2 m root zone은 고운사에 전이하지 않는다.

### nutrient uptake / litter recycling
```
weathering nutrient release
 -> plant uptake
 -> vegetation pool
 -> litter return
 -> upper-soil solution chemistry
```

이 순환을 mass-conserved coupling으로 구현한다.

### geomorphic fourth pathway
```
erosion/deposition
 -> fresh-mineral supply / mineral residence
 -> W_chem
```

이 네 경로를 하나의 biomass multiplier로 합치지 않는다.


## 결정 13. hillslope length를 chemical-weathering response context로 추가

Ferrier & Perron 2020에 따라:

```
tau_hillslope
~ L^2 / D
```

형태의 hillslope transport timescale이 chemical-erosion transient response를 강하게 제약할 수 있다.

따라서 weathering state/sensitivity에는:
- distance to divide/channel
- characteristic hillslope length
- transport timescale context

를 포함한다.

100년 postfire run은 전체 weathering system의 equilibrium run이 아니라 incremental transient run으로 해석한다.

## 결정 14. weathering front와 water table을 분리

Rempe & Dietrich 2014의 bottom-up model과 Wang et al. 2021의 coevolution evidence를 반영한다.

상태:

```
Z_weathered
!=
Z_water_table
```

가능.

Top-down:
```
infiltration / roots / CO2
 -> weathering
```

Bottom-up:
```
channel incision / drainage
 -> fresh-bedrock exposure to reactive fluids
 -> weathering
```

둘 중 하나를 universal rule로 고정하지 않는다.

첫 구현:
- inherited `Z_weathered(t0)`
- optional water-table/deep-flow state
- fracture/permeability state

를 분리하고 100년 증분만 갱신한다.


## 결정 15. Flux-PIHM + WITCH + vegetation cycling 선례를 최상위 integration evidence로 추가

Sullivan et al. 2019은 opposing forested hillslopes에서:

```
Flux-PIHM
+
WITCH
+
vegetation nutrient uptake / litter return
```

을 실제로 결합했다.

따라서 고운사:
```
LPJ-GUESS
 -> hydrology
 -> nutrient uptake
 -> litter return

WITCH/PROFILE
 -> mineral weathering
```

구조는 단순 개념조합이 아니라 published integration precedent를 가진다.

중요:
vegetation cycling을 넣은 경우 shale weathering이 약 10% 감소했다.

따라서:
```
vegetation
!= positive weathering multiplier
```
금지를 다시 확인한다.

## 결정 16. respiration source와 soil pCO2를 분리

Hasenmueller 2015:

```
topographic position
 -> soil depth/moisture/gas diffusion
 -> pCO2
```

Kopp 2023:

```
dry ridge
 -> water-limited respiration

wet valley
 -> oxygen-limited respiration
```

따라서 first implementation에서도 개념적으로:

```
R_CO2
!=
pCO2
```

로 둔다.

가능한 reduced formulation:

```
R_CO2
=
f(T, moisture, saturation, vegetation state)

pCO2
=
g(R_CO2, porosity, gas diffusivity, soil depth, saturation)
```

full gas transport는 PFLOTRAN advanced model에서 검증한다.

## 결정 17. sandstone preferential flow를 lithology/horizon-dependent하게 본다

Tang et al. 2020 temperate-forest sandstone catchment:

```
preferential-flow frequency
=
f(hillslope position, antecedent moisture, soil profile, lithology)
```

따라서 Gounsa에서:

```
deep-flow fraction
=
f(TWI)
```

같은 단일 topographic rule은 사용하지 않는다.

최소:
- antecedent moisture
- profile/horizon state
- fracture/permeability proxy
- hillslope position

를 함께 고려한다.


## 결정 18. lateral flow를 chemical-weathering spatial state로 명시

Bower et al. 2023 forested podzols에서 lateral-flow affected horizons는 vertically developed profiles보다 훨씬 강한 plagioclase depletion을 보였다.

따라서 mandatory spatial sensitivity:

```
upslope contributing water
lateral throughflow
depth to bedrock
flow-path history
```

를 포함한다.

각 grid cell을 완전히 독립된 vertical weathering column으로만 계산하지 않는다.

## 결정 19. tree-root/fracture vertical connectivity를 별도 sensitivity로 둔다

Uhlemann et al. 2024:

```
tree location
+ fracture zone
 -> deeper vertical infiltration
```

가능.

따라서:

```
vertical connectivity
=
f(fracture state, root state, antecedent moisture)
```

형태의 sensitivity를 허용한다.

단, root presence가 직접 fracture permeability를 얼마나 변화시키는지는 separate NEW COUPLING이며 coefficient를 임의 생성하지 않는다.

## 결정 20. hillslope hydrologic structure의 점진적 공진화를 sensitivity에 둔다

Hartmann & Blume 2024는 수십~수천년 동안:

```
soil formation
+ vegetation development
 -> preferential/lateral flow structure
```

가 변화함을 보여준다.

100년 고운사 first production에서는 hydrologic structure를 완전 동적화하지 않더라도, 다음 변화는 sensitivity 후보로 둔다.

- organic-layer storage
- infiltration partition
- preferential-flow fraction
- shallow/lateral flow fraction

## 결정 21. inherited weathering-depth prior에 hillslope length/relief를 고려

Pedrazas et al. 2021 + Ferrier & Perron 2020에 따라:

```
divide-channel distance
local relief
ridge-valley spacing
```

은 inherited `Z_weathered(t0)` prior와 rock-moisture capacity 설계에 사용할 수 있다.

단 field-site-specific depth values를 고운사에 직접 전이하지 않는다.


## 결정 22. sandstone을 reaction lithology와 hydrologic architecture로 분리

Xiao et al. 2019의 forested sandstone catchment를 반영한다.

고운사에서 sandstone effect는:

```
A. mineral/cement chemistry
 -> reaction kinetics

B. soil/regolith/boulder architecture
 -> porosity/macropores
 -> storage/connectivity
 -> flow paths/residence time
```

두 갈래로 처리한다.

따라서 단일:
```
sandstone weathering factor
```
를 사용하지 않는다.

Hoagland et al. 2017에 따라 chemical-weathering water는 최소:
```
shallow
deep
lateral/mixed
```
reservoir로 구분할 수 있어야 한다.

## 결정 23. decadal vegetation-pedogenesis feedback은 허용하되 soil-thickness accumulation을 P_sand로 쓰지 않는다

Phillips et al. 2008은 newly exposed resistant sandstone에서 수십 년 내 vegetation-soil feedback이 나타날 수 있음을 보여준다.

따라서 100년 simulation에서:
```
vegetation recovery
<-> thin-soil / fracture state
```
feedback을 무시하지 않는다.

하지만 reported:
```
5-10 mm yr^-1
```
soil-cover thickening은:
- in-situ weathering
- organic accumulation
- mineral debris trapping
- fracture infill
을 포함하므로 `P_sand` calibration에 사용하지 않는다.

고운사 mass balance에서는 이 성분들을 분리한다.


## excluded

- mycorrhiza
- tree throw/uprooting
- shallow landslide
- arbitrary biomass multiplier
- arbitrary aspect multiplier
- current-vegetation equilibrium reset of inherited weathering depth

---

## 가장 중요한 새 결론

이전 구조보다 사면 feedback을 한 단계 강화한다.

기존:
```
LPJ-GUESS
 -> W_chem
```

수정:
```
LPJ-GUESS
 -> root/deep hydrology
 -> hillslope flow/residence
 -> W_chem
 -> H/CAZ/nutrients
 -> erosion/deposition/mineral residence
 -> W_chem
 -> LPJ-GUESS
```

즉 chemical weathering은 더 이상 vegetation에서 독립된 cell-local sink가 아니다.

It is a hillslope-connected state/process.

## 관련
- `models/Hillslope_Vegetation_Weathering.md`
- `models/Vegetation_Weathering_Coupling.md`
- `models/BioRT.md`
- `models/Sandstone_Soil_Production.md`
- `decisions/2026-09-21_MYCORRHIZA_EXCLUSION.md`
- `decisions/2026-09-21_SOIL_WEATHERING_FOURTH_PASS_NON_MYCORRHIZAL.md`
