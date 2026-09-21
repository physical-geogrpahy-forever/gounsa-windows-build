# 결정: 고운사 토양풍화 4차 문헌감사 - non-mycorrhizal core

날짜: 2026-09-21
브랜치: `gounsa-water-erosion-deep-review-2026-09-21`

## 목적

사용자 범위 수정에 따라 균근(mycorrhiza)을 production과 sensitivity에서 제외한 뒤, 토양/암석 풍화 구조가 여전히 충분한 published evidence를 가지는지 재검토했다.

핵심 질문:

1. living roots 자체가 mineral weathering을 정량적으로 증가시킬 수 있는가
2. root respiration / soil CO2가 core process인가
3. root exudate를 production에 넣어야 하는가
4. hydrologic residence time이 얼마나 중요한가
5. chemical weathering과 sandstone soil production의 경계는 어떻게 유지할 것인가

---

## 1. authoritative exclusion

최신 결정:

`decisions/2026-09-21_MYCORRHIZA_EXCLUSION.md`

제외:

```
mycorrhizal_type
AM / EcM state
fungal hyphal weathering
fungal oxalate allocation
PFT -> mycorrhiza mapping
mycorrhizal weathering multiplier
```

관련 논문은 archive/reference only이다.

---

## 2. root respiration / deep CO2는 production core로 유지

### Baars et al. 2008
living/deeper rooting system이 substrate CO2를 증가시킬 수 있음을 microcosm에서 확인했다.

### Tune et al. 2020
thin soil 아래 4-8 m weathered bedrock에서 substantial CO2 production을 직접 관측했다.

```
deep rooting
 -> below-soil C turnover
 -> bedrock-zone CO2
 -> dissolved inorganic carbon / water-rock interaction
```

deep bedrock CO2 production은 soil-only carbon model로 설명되지 않았다.

### Tune et al. 2023
16 m weathering profile에서 vadose-zone CO2는 petrogenic carbon oxidation보다 recently fixed carbon associated with deep rooting이 지배했다.

### Osorio-Leon et al. 2025
reactive transport model에서 deep CO2 source를 명시적으로 넣어야 관측 chemistry를 재현했다.

원 site lithology:
```
primarily argillite
+ sandstone interbeds
```

이므로 고운사 sandstone coefficient로 직접 사용하지 않는다.

하지만 process conclusion은 강하다.

```
deep-root-associated respiration
 -> bedrock-zone CO2
 -> carbonic-acid reactivity
 -> W_chem
```

### 결정

**root / belowground respiration-derived CO2 source는 production core input이다.**

필수 interface state:

```
root_access_depth
FineRootC(z)
root/soil respiration source by layer
soil/fracture pCO2 or CO2 production
```

LPJ-GUESS에서 정확한 respiration output을 어떻게 취득할지는 별도 implementation audit가 필요하다.

---

## 3. root distribution은 total root biomass로 축약하지 않는다

Gatz-Miller et al. 2023:
- 2D reactive transport
- 170-year simulation
- dynamic root architecture comparison

root representation이:
- water uptake
- solute transport
- geochemical-zone geometry
를 바꾸었다.

따라서 chemical weathering interface 최소 state:

```
FineRootC_total
+ FineRootC(z)
+ root fraction by layer
+ root access depth
+ root water uptake by layer
```

이다.

Explicit discrete roots까지 갈 필요는 없지만 vertical structure를 버리지 않는다.

---

## 4. hydrologic residence time은 production core 제어변수다

### Maher 2010

weathering-rate variation은 material age보다:

```
fluid residence time
flow rate
approach to equilibrium
```

에 강하게 제어될 수 있다.

기본 reaction:

```
R_d
=
-k A (1-Q/K_eq)
```

transport:

```
0
=
-q dc/dz
+
R_d(1-c/c_eq)
```

의 competition이 weathering flux를 결정한다.

### Wen et al. 2022
2D forest hillslope에서:
- flow-path depth
- residence time
- hydrologic regime
가 chemical weathering과 solute export를 바꾸었다.

### BioRT-Flux-PIHM
watershed-scale spatial hydrology와 reaction network를 결합할 수 있다.

### 결정

다음은 production core / mandatory sensitivity로 본다.

```
infiltration
drainage
flow-path depth
water residence time
soil water
temperature
```

단순 annual runoff 총량만으로 chemical weathering을 완전히 표현하지 않는다.

---

## 5. root exudate / organic ligand는 optional sensitivity

### Calvaruso et al. 2013
Scots pine root-only treatment에서도 apatite dissolution과 Ca/P/trace element release가 abiotic control보다 크게 증가했다.

따라서 균근 없이도:

```
living root
 -> proton / organic-acid source
 -> mineral dissolution
```

경로가 존재한다.

### Chibesa et al. 2025
realistic rhizosphere-level organic root exudate compounds:

- citrate
- oxalate
- catechol

이 soil/mineral Si solubilisation을 크게 변화시켰다.

하지만 effect ordering은:
- primary minerals
- clays
- whole soils

사이에서 달랐다.

따라서:

```
organic-ligand effect
= compound-specific
x mineral-specific
x soil-state-specific
```

이다.

### Lawrence et al. 2014
organic acid가 near-surface dissolution을 빠르게 하더라도 secondary-mineral precipitation, decomposition, transport 때문에 profile-scale net weathering은 감소할 수도 있다.

### Drever 1994
organic ligands 및 plant-induced pH effect는 mineral/pH context에 따라 작거나 방향이 달라질 수 있다.

### Garcia-Arredondo et al. 2023
root-derived DOC는:
- microbial consumption
- mineral sorption
- redox reactions
으로 partition된다.

### 결정

root exudation / DOC ligand pathway는 **production 필수항이 아니라 optional sensitivity**로 둔다.

첫 production core:

```
NO explicit exudate speciation required
```

Advanced sensitivity:

```
root C / nutrient stress
 -> effective ligand source
 -> partition / decay
 -> mineral reaction
```

금지:

```
all root exudate C -> weathering ligand
```

금지:

```
W_chem *= constant_root_exudate_factor
```

---

## 6. sandstone-specific constraints

### Pawlik et al. 2023
temperate mountain forest sandstone에서 tree roots가 cracks/fissures를 이용하고 soil properties와 weathering을 변화시키는 field evidence.

Universal annual rate law는 없음.

### Potysz & Bartz 2024
sandstone under artificial-root-exudate conditions에서:
- Si
- Al
- Fe

release가 inorganic control보다 크게 증가할 수 있었다.

반응은 sandstone cement/mineralogy에 민감했다.

따라서 Gounsa weathering parameterization에는 반드시:

```
cement type
Fe-bearing cement
matrix abundance
weatherable feldspar/lithic grains
fracture density
```

를 확인한다.

이는 P_sand parameters뿐 아니라 W_chem chemistry에도 필요하다.

---

## 7. plant effect의 방향은 비단조적

### Drever 1994

식생은:
- CO2/pH
- ligand
- surface area
- water residence
- fine-particle binding

을 동시에 바꾼다.

따라서 식생이 항상 weathering을 증가시키는 것은 아니다.

### Oeser & von Blanckenburg 2020

```
higher NPP
!=
higher weathering rate
```

일 수 있다.

### Zuo et al. 2024

```
vegetation
 -> erosion suppression
 -> less fresh-mineral supply
 -> lower supply-limited weathering
```

가능.

### 결정

금지:

```
W_chem = W_base * f(biomass)
```

금지:

```
W_chem = W_base * f(NPP)
```

식생은 각 process route로만 들어간다.

---

## 8. chemical weathering production core

균근 제외 후 production target:

```
LPJ-GUESS
├─ PFT / NPP
├─ FineRootC(z)
├─ root access depth
├─ root water uptake by layer
├─ root / belowground respiration
├─ litter / SOM
├─ nutrient uptake / return
├─ soil temperature
└─ soil water / runoff / drainage
       |
       v
vegetation-hydrology interface
       |
       v
WITCH / PROFILE
or BioRT spatial alternative
       |
       ├─ mineral dissolution / precipitation
       ├─ aqueous chemistry
       ├─ W_chem
       └─ nutrient release
              |
              v
      LPJ-GUESS-CNP [new return coupling]
```

Optional only:

```
root-derived DOC / organic ligand sensitivity
```

No mycorrhiza state.

---

## 9. engine hierarchy after fourth pass

### WITCH / PROFILE
역할:
- primary chemistry candidate
- B-WITCH/ForSAFE에서 vegetation/forest coupling precedent 존재
- 균근 항을 쓰지 않고 hydrology/CO2/uptake/return/litter pathways만 사용

### BioRT-Flux-PIHM
역할:
- strong spatial alternative
- lateral/deep hydrology
- residence time
- plant uptake / soil respiration

### REWTCrunch
역할:
- root-exudate advanced sensitivity / validation only
- full domain production core 아님

### Hartmann/LPJ-GUESS-CNP
역할:
- low-cost hydroclimatic benchmark only

---

## 10. chemical weathering vs soil production

현재 유지:

```
W_chem
!=
P_sand(H)
```

### W_chem
- dissolved chemical mass loss
- mineral transformations
- nutrient release

### P_sand(H)
- parent material -> mobile soil / boundary lowering
- Mode A exponential
- Mode B shallow finite-depth hump sensitivity

Yu & Hunt 2018 및 Braun 2016은:

```
reactive/hydrologic weathering
 -> weathering-front advance
 -> regolith production
```

bridge의 future sensitivity다.

현재 sandstone field-constrained P_sand를 대체하지 않는다.

---

## 11. next implementation audit

다음은 문헌검색보다 source/output 확인이 중요하다.

1. LPJ-GUESS root respiration output 확인
2. layer-wise root water uptake output 확인
3. soil water / drainage / runoff의 timestep과 units 확인
4. PFT/cohort root state를 weathering grid에 mapping
5. WITCH vs PROFILE vs BioRT source/code practicality 비교
6. Gounsa sandstone petrography/mineral assemblage 확정
7. reactive surface area parameterization
8. optional root-exudate sensitivity source-term 설계
9. water residence-time calculation
10. W_chem -> nutrient pool return mass balance

## 관련 authoritative files

- `decisions/2026-09-21_MYCORRHIZA_EXCLUSION.md`
- `decisions/2026-09-21_VEGETATION_WEATHERING_COUPLING.md`
- `decisions/2026-09-21_SOIL_WEATHERING_THIRD_PASS.md`
- `models/Vegetation_Weathering_Coupling.md`
- `models/B_WITCH.md`
- `models/BioRT.md`
- `models/REWTCrunch.md`
- `models/Sandstone_Soil_Production.md`
