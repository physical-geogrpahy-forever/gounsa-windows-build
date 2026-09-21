# 결정: 고운사 토양풍화 3차 문헌감사

날짜: 2026-09-21

## 목적
기존 vegetation-weathering decision 이후에도 다음 문제를 추가 검토했다.

1. root/litter organic compounds가 weathering을 항상 증가시키는가
2. root architecture 자체가 chemical weathering 공간패턴에 중요한가
3. WITCH/PROFILE 외 spatial reactive-transport 대안이 있는가
4. chemical weathering을 soil production으로 연결할 수 있는가
5. sandstone에서 biotic chemistry가 lithology와 어떻게 상호작용하는가

---

## 1. organic acids는 단일 양의 weathering multiplier가 아니다

Lawrence et al. 2014 reactive-transport model:

```
organic acids
 -> near-surface dissolution enhancement
```

은 가능하지만, 동시에:

- organic-metal complexation
- secondary-mineral precipitation
- organic-acid decomposition
- transport

이 작용하여 profile-scale long-term net weathering은 오히려 감소할 수 있었다.

따라서 production에서 금지:

```
root exudation
 -> constant positive multiplier
 -> W_chem
```

대신 explicit reaction / transport state로 다룬다.

Perez-Fodich & Derry 2019는 high soil CO2와 LMW organic acids가 서로 다른 경로로 mineral loss와 reaction-front propagation을 강화할 수 있음을 보여준다.

결론:

```
respiration CO2
!=
organic ligand effect
```

두 source를 합치지 않는다.

---

## 2. chemical weathering interface에 root depth/distribution을 필수 state로 유지

Gatz-Miller et al. 2023:
- 2D reactive transport
- dynamic root architecture
- 170-year simulation

simplified root representation과 dynamically evolving root architecture를 비교한 결과 root-water uptake의 공간차이가 water/solute transport와 geochemical-zone geometry를 변화시켰다.

따라서 고운사에서는:

```
FineRootC_total
```

만 chemical weathering에 전달하지 않는다.

최소한:

```
FineRootC(z)
root fraction by soil layer
root access depth
root water uptake by layer
```

를 보존한다.

LPJ-GUESS root distribution을 explicit discrete root architecture로 바꿀 필요는 없지만, vertical layer distribution을 잃으면 안 된다.

---

## 3. root-exudate carbon의 availability를 100%로 가정하지 않는다

Garcia-Arredondo et al. 2023:

```
root-derived DOC
 -> microbial consumption
 OR mineral sorption
 OR redox reactions
```

의 경쟁이 존재한다.

따라서:

```
all root exudate C
 -> mineral-weathering ligand
```

라고 두지 않는다.

REWTCrunch sensitivity에서는 exudate partition / loss에 대한 sensitivity가 필요하다.

---

## 4. sandstone biotic-weathering은 cement/mineralogy 의존성이 매우 중요

Potysz & Bartz 2024:
- artificial root exudates
- bacterial / siderophore conditions
- Fe-containing vs Fe-depleted sandstone

비교에서 organic-rich conditions가 inorganic conditions보다 sandstone alteration을 강화했고 sandstone cement가 특히 민감했다.

따라서 고운사 petrography에서 우선 확인:

```
cement type
Fe-oxide cement abundance
matrix abundance
feldspar abundance
grain contacts
fracture density
```

이는 단순한 P0/gamma calibration뿐 아니라 chemical vegetation-weathering reaction network를 결정한다.

---

## 5. spatial reactive transport 대안으로 BioRT를 추가

BioRT-Flux-PIHM:

```
land-surface + distributed hydrology
 -> mineral dissolution
 -> soil respiration
 -> plant uptake
 -> solute transport
```

을 watershed scale에서 결합한다.

따라서 chemical-weathering engine 후보를 다음처럼 정리한다.

### A. WITCH / PROFILE
장점:
- B-WITCH/ForSAFE vegetation coupling precedent 강함
- forest chemistry history가 길고 명확

### B. BioRT-Flux-PIHM
장점:
- watershed-scale spatial hydrology
- lateral/deep flow
- modern reactive transport
- plant uptake / respiration 포함

### C. REWTCrunch
장점:
- explicit root exudation
- high-resolution rhizosphere

단점:
- domain-wide 2D/100-year implementation burden 큼

### D. Hartmann/LPJ-GUESS-CNP
역할:
- low-cost benchmark only

현재 WITCH/PROFILE production target은 유지하되 BioRT-Flux-PIHM을 **공간수문 대안 후보**로 승격한다.

---

## 6. topography / flow path feedback을 chemical weathering에 고려

Wen et al. 2022의 2D temperate-forest hillslope RTM:

```
topography / hydrology
 -> flow-path depth
 -> residence time
 -> acidity / carbon transformation
 -> weathering
 -> solute export
```

을 보여준다.

따라서 향후 고운사 chemistry는 완전한 cell-independent box로만 두지 않는다.

최소 sensitivity:

```
local water residence / drainage
deep vs shallow flow partition
```

을 포함해야 한다.

---

## 7. W_chem -> soil production bridge

Yu & Hunt 2018은 transport-limited chemical weathering에서:

```
chemical weathering / solute transport
 -> gross soil production
gross production - erosion
 -> net soil formation
```

을 연결하는 analytical framework를 제시한다.

이것은 현재:

```
W_chem
!=
P_sand(H)
```

분리를 없애라는 뜻이 아니다.

현재 production:
- P_sand Mode A/B 유지
- W_chem 별도 유지

향후 sensitivity:
```
RTM weathering
 -> weathering-front velocity
 -> soil production
```

mechanistic bridge로 Yu-Hunt/percolation lineage를 시험할 수 있다.

Sandstone field constraints보다 우선하지 않는다.

---

## 8. root respiration pathway의 독립 실험 근거

Baars et al. 2008 microcosm:

```
living/deeper rooting
 -> substrate CO2 increase
 -> carbonic-acid weathering potential
```

을 지지한다.

따라서 LPJ-GUESS interface에서는 NPP만 쓰지 않고:
- living-root biomass
- root respiration
- root depth
를 분리한다.

---

## 9. mycorrhiza production 제외

최신 범위 결정:
`decisions/2026-09-21_MYCORRHIZA_EXCLUSION.md`

다음은 현재 production 및 sensitivity에서 제외한다.

```
mycorrhizal_type
AM / EcM / mixed
fungal hyphal weathering
fungal oxalate allocation
PFT -> mycorrhiza mapping
```

Quirk 2012, Bonneville 2011, Schmalenberger 2015, Rombouts 2026은 archive/reference only로 유지한다.

Chemical weathering은 균근 없이:
- root respiration / soil CO2
- root depth/distribution
- root water uptake
- litter/SOM
- non-mycorrhizal DOC/organic-ligand sensitivity
- nutrient uptake/return
- hydrology
를 사용한다.

## 10. sandstone petrography의 역할 강화

Potysz & Bartz 2024 때문에 기존 petrography 우선순위를 더 강화한다.

확인 필요:
- cement mineralogy
- Fe-bearing cement
- goethite / hematite
- matrix abundance
- feldspar and other weatherable grains
- fracture network

이는:
```
P_sand(H)
```
보정뿐 아니라:
```
organic ligand / microbial weathering susceptibility
```
에도 필요하다.


## 최종 production correction

Chemical weathering input state:

```
LPJ-GUESS
├─ PFT
├─ NPP
├─ FineRootC by layer
├─ root-access depth
├─ root water uptake by layer
├─ root respiration / belowground CO2 source
├─ litter / SOM state
├─ nutrient uptake / return
├─ soil temperature
└─ soil water / drainage / runoff
```

Reaction state:

```
mineralogy
reactive surface area
pH / H+
soil/fracture CO2
DOC / organic ligand pool
secondary-mineral precipitation
water residence time
flow-path partition
```

Outputs:

```
W_chem
nutrient release
secondary mineral state
solute export
```

Important:

```
root exudation
!= always increased net weathering

total root biomass
!= sufficient weathering state

chemical weathering
!= automatically soil-production thickness
```

---

## physical sandstone production status

변경 없음.

```
P_sand(H)
= Mode A exponential
+ Mode B shallow finite-depth hump sensitivity
```

No arbitrary:
```
P_sand * f(root biomass)
```

Direct living-root fracture remains optional/unresolved.

---

## 다음 우선순위

1. WITCH/PROFILE vs BioRT-Flux-PIHM source/code practicality 비교
2. LPJ-GUESS root respiration / belowground C flux output 확인
3. LPJ-GUESS layer-wise root water uptake output 확인
4. root exudation source term을 어떻게 근사할지 결정
5. Gounsa sandstone cement/mineral assemblage 확정
6. reactive surface area parameterization
7. 2D subsurface flow/residence-time sensitivity
8. W_chem -> P_sand mechanistic bridge sensitivity

## 관련 파일
- `models/Vegetation_Weathering_Coupling.md`
- `models/B_WITCH.md`
- `models/BioRT.md`
- `models/REWTCrunch.md`
- `models/Sandstone_Soil_Production.md`
- `decisions/2026-09-21_VEGETATION_WEATHERING_COUPLING.md`
