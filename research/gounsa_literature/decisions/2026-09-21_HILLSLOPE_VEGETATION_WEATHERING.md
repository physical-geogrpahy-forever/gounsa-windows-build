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
