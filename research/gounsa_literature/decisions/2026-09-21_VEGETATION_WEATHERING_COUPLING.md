# 결정: 고운사 식생-풍화 coupling 수정

날짜: 2026-09-21

## 문제
기존 production description은:

```
LPJ-GUESS
 -> runoff + soil temperature
 -> Hartmann chemical weathering
```

을 사용했다.

이 구조에는 vegetation effect가 일부 존재하지만, 실제로는 주로:

```
vegetation
 -> hydrology / runoff
 -> weathering
```

경로에 한정된다.

따라서 root/litter/respiration/nutrient cycling까지 포함하는 "완전한 식생-풍화 feedback"이라고 부르기에는 부족했다.

## 문헌 재검토 결과

### B-WITCH
Roelandt et al. 2010은 LPJ-DGVM을 WITCH에 직접 coupling했다.

식생에서 풍화로 전달되는 published variables:
- PFT / cover
- NPP
- soil water / drainage / runoff
- belowground respiration / soil CO2
- element uptake
- aboveground litter return
- root litter return

따라서:
```
dynamic vegetation model -> mechanistic weathering
```
published coupling이 실제 존재한다.

### WITCH-ASPECTS
Goddéris et al. 2006은 forest water/carbon model output으로:
- soil CO2
- vegetation uptake/release
- seasonal weathering
을 강제했다.

### ForSAFE
Wallman et al. 2005 및 Kronnäs et al. 2019은:
- forest growth
- nutrient uptake
- litter decomposition
- soil moisture
- soil chemistry
- mineral weathering
사이의 dynamic feedback을 구현한다.

### REWTCrunch
Roque-Malo et al. 2022는:
```
root biomass
 -> root exudation
 -> microbial / acid-base reactions
 -> mineral dissolution
```
을 daily reactive transport로 구현한다.

### biological proton cycle
Banwart 2009의 비균근 process 계보를 참고한다.

고운사에서 유지:
```
biological productivity
 -> root respiration / soil CO2
 -> DOC / proton balance
 -> pH
 -> mineral dissolution
```

Taylor 2011/2012의 mycorrhizal functional-type 및 fungal weathering 항은 최신 결정 `2026-09-21_MYCORRHIZA_EXCLUSION.md`에 따라 production/sensitivity에서 제외한다. Taylor 2012는 DGVM -> process-based weathering이라는 상위 구조만 참고한다.

## 결정 1: Hartmann-only 구조를 complete weathering representation으로 사용하지 않는다

Hartmann/LPJ-GUESS-CNP는 유지한다.

역할:
- low-cost benchmark
- P-cycle consistency check
- lithology/runoff/temperature sensitivity

그러나 complete production vegetation-weathering process의 유일한 식으로 사용하지 않는다.

## 결정 2: chemical weathering production target

우선 구조:

```
LPJ-GUESS
├─ PFT / NPP
├─ soil temperature
├─ soil water / runoff / drainage
├─ root / litter / SOM respiration
├─ nutrient uptake
└─ litter / root turnover
       |
       v
B-WITCH-style vegetation interface
       |
       v
WITCH / PROFILE-style mineral kinetics
       |
       ├─ W_chem dissolved mass loss
       └─ nutrient release
```

### 새 coupling 표시
원 B-WITCH는 LPJ를 사용하고 장기 평균 forcing으로 WITCH를 steady state에 가깝게 돌린다.

고운사에서는:
```
LPJ-GUESS transient postfire states
 -> WITCH-style chemistry
```
를 사용하므로 이 부분은 **새로운 coupling**이다.

## 결정 3: vegetation feedback back to LPJ-GUESS

목표:

```
weathering nutrient release
 -> LPJ-GUESS-CNP available nutrient pools
 -> vegetation growth
```

ForSAFE에는 soil chemistry <-> forest growth의 two-way feedback 선례가 있다.

하지만 WITCH -> LPJ-GUESS-CNP 직접 연결은 published B-WITCH 기능이 아니므로 **새로운 coupling**으로 기록한다.

첫 구현에서는 P release를 우선 feedback 대상으로 한다.

## 결정 4: root exudation

REWTCrunch는 explicit root-exudation chemistry의 가장 직접적인 선례다.

초기 core에서 full REWTCrunch를 domain-wide로 돌리지는 않는다.

우선:
- advanced sensitivity
- mechanistic validation
으로 둔다.

향후 LPJ-GUESS FineRootC / root respiration을 exudation source로 mapping할 수 있다. 이 mapping은 새로운 coupling이다.

## 결정 5: physical sandstone soil production

현재 background front-production은 유지:

```
P_sand(H)
```

- Mode A: exponential
- Mode B: shallow finite-depth hump

그러나 이것이 "식생 무관"이라는 뜻은 아니다.
원 analogue rates는 자연 토양생산의 장기 통합량이다.

다만 고운사 production에서 임의의:

```
P_sand(H) * f(root biomass)
```

를 만들지는 않는다.

이유:
- Gabet & Mudd 2010 root fracture는 tree-throw/rootwad geometry와 결합
- Pawlik 2023 sandstone evidence는 process evidence이지 annual rate law가 아님
- Malik 2019는 root-pressure crack widening 증거가 inconclusive라고 평가
- transferable FineRootC -> sandstone production law가 없음

따라서 direct biomechanical root-weathering term은:
```
optional / unresolved
```
로 유지한다.

## 결정 6: double counting 방지

```
P_sand(H)
!=
W_chem
```

현재 역할:
- P_sand(H): bedrock / parent material -> mobile-soil production and boundary lowering
- W_chem: dissolved mass loss and elemental release from explicitly modelled chemical domain

WITCH를 parent-material reaction front까지 확장하여 그 dissolution을 boundary lowering으로 바꿀 경우:
- P_sand를 residual physical production으로 재분해하거나
- P_sand를 제거하고 mechanistic front model로 교체해야 한다.

둘을 동일 mass에 독립적으로 더하지 않는다.

## 사면수송과의 관계

전체 사면수송은 그대로:

```
q_hill
=
q_bg
+
q_root
+
q_dryravel
```

식생 직접효과:
- q_root: LPJ-GUESS roots + turnover -> Gabet
- q_dryravel: vegetation storage/recovery
- SWEHR resistance: roots/litter
- q_bg: biomass multiplier 없음

풍화 식생효과:
- hydrology
- soil temperature
- soil CO2 / respiration
- nutrient uptake/return
- litter/decomposition
- optional root exudation

으로 분리한다.

## 추가 제약: vegetation effect의 부호와 크기를 단일 multiplier로 두지 않는다

### Oeser & von Blanckenburg 2020

LPJ-GUESS NPP를 포함한 기후-식생 구배 비교에서:
- NPP와 강수량이 크게 증가해도 weathering rate가 체계적으로 증가하지 않았다.
- 증가한 식물 양분수요는 더 빠른 nutrient recycling으로 충족되었다.

따라서 금지:

```
W_chem = W_abiotic * f(NPP)
```

형태의 단순 양의 biomass/NPP multiplier를 calibration 없이 사용하지 않는다.

### Zuo et al. 2024

식생은 erosion을 줄여 fresh-mineral supply를 낮출 수 있다.

따라서 vegetation-weathering feedback에는 서로 반대 부호의 경로가 존재한다.

```
vegetation
 -> respiration / CO2 / ligands
 -> chemical weathering enhancement

vegetation
 -> erosion suppression
 -> fresh-mineral supply reduction
 -> weathering supply limitation
```

고운사에서는 두 효과를 하나의 empirical multiplier로 합치지 않는다.

### Osorio-Leon et al. 2025

깊은 뿌리와 연관된 CO2 production을 reactive transport에 명시적으로 넣어야 16 m bedrock vadose-zone chemistry가 재현되었다.

해당 현장에서는:
- deep-root-associated processes가 BVZ solute weathering flux의 약 43 ± 3%에 기여
- deep-rhizosphere carbonic-acid effect를 포함할 때 chemical weathering이 background 대비 약 1.8 ± 0.1배

였다.

이 값은 **고운사 coefficient로 전이하지 않는다.**

역할:
- deep-root respiration을 weathering interface에 포함할 강한 process 근거
- root-access depth가 H_AB보다 깊을 수 있음을 허용할 근거
- site-specific sensitivity envelope 설계의 참고

## 추가 제약: direct biomechanical root weathering

새 mechanics 검색 결과:

### Calusi et al. 2020
```
root growth
 -> contact stress
 -> fracturable matrix response
 -> fracture-regrowth cycle
```
의 continuum-mechanics numerical precedent가 존재한다.

하지만 검증 매질은 soil / artificial medium이며 sandstone bedrock production model이 아니다.

### Wright et al. 2026
FE + SRXCT preliminary work에서 root가 direct penetration limit를 crack propagation과 local exudate softening으로 극복할 수 있음을 보였다.

하지만:
- conference abstract
- constitutive details 제한
- sandstone annual-production flux 없음

따라서 현재 판정:

```
living-root biomechanical weathering
= physically plausible
= emerging quantitative mechanics
!= production-ready sandstone soil-production law
```

Production baseline에서는 여전히 임의:
```
P_root = k * FineRootC
```
또는:
```
P_sand = P_sand(H) * f(root biomass)
```
를 만들지 않는다.

후속 peer-reviewed rock-fracture model 또는 고운사 사암의 fracture-strength/root-pressure 자료가 확보될 때 optional module로 재검토한다.

## 최종 판정

기존:
```
LPJ-GUESS/Hartmann only
```
는 **불완전한 vegetation-weathering representation**으로 강등한다.

새 production target:
```
LPJ-GUESS
 -> B-WITCH-style vegetation interface
 -> WITCH/PROFILE mineral kinetics
 -> W_chem + nutrient release
 -> LPJ-GUESS-CNP feedback [new coupling]
```

Physical root fracture:
```
not zero conceptually
but no hard-coded production coefficient yet
```


## mycorrhiza scope override

최신 결정:
`decisions/2026-09-21_MYCORRHIZA_EXCLUSION.md`

균근 관련 state/coupling은 현재 production 및 sensitivity에서 제외한다.

```
mycorrhizal_type
AM / EcM
fungal hypha weathering
fungal oxalate allocation
PFT -> mycorrhiza mapping
```

관련 논문은 archive/reference only로 유지한다.
