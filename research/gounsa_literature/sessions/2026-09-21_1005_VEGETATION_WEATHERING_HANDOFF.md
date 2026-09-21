# Gounsa vegetation-weathering coupling handoff

날짜: 2026-09-21 10:05 KST
브랜치: `gounsa-water-erosion-deep-review-2026-09-21`

## 이번 세션의 질문

기존 production 구조에서 식생이 사면수송에는 명시적으로 들어가지만 토양/암석 풍화에는 충분히 들어가지 않는 문제가 확인되었다.

핵심 질문:

```
vegetation
 -> weathering
```

을 실제 published process model로 어떻게 구현할 것인가?

특히:
1. chemical weathering
2. sandstone soil production
3. living-root biomechanical weathering

을 분리해서 재검토했다.

---

## 핵심 수정

기존:

```
LPJ-GUESS
 -> runoff + soil temperature
 -> Hartmann chemical weathering
```

은 vegetation effect가 전혀 없는 것은 아니지만, 사실상 주로:

```
vegetation
 -> hydrology/runoff
 -> weathering
```

경로에 한정되어 complete vegetation-weathering representation으로는 부족하다.

새 production target:

```
LPJ-GUESS
├─ PFT / NPP
├─ root state / root depth / turnover
├─ litter / SOM
├─ soil temperature
├─ soil water / runoff / drainage
├─ belowground respiration / soil CO2
└─ nutrient uptake / return
       |
       v
B-WITCH-style vegetation interface
       |
       v
WITCH / PROFILE-style mineral kinetics
       |
       ├─ W_chem dissolved mass loss
       └─ nutrient release
                |
                v
       LPJ-GUESS-CNP nutrient pools
                |
                v
       vegetation growth / recovery
```

WITCH -> LPJ-GUESS-CNP feedback은 새로운 coupling이다.

---

## 새로 확인한 핵심 published lineages

### Goddéris et al. 2006
WITCH를 forest water/carbon model에 coupling.

식생 관련:
- soil CO2
- vegetation element uptake / release
- seasonal water/carbon forcing

### Roelandt et al. 2010 B-WITCH
LPJ-DGVM + WITCH.

LPJ에서 전달:
- PFT / fractional cover
- NPP
- hydrology / runoff / drainage
- belowground respiration
- biomass element uptake
- aboveground litter return
- root litter return

고운사에서 LPJ-DGVM을 LPJ-GUESS로 교체하고 postfire transient forcing으로 사용하는 것은 새로운 coupling.

### PROFILE / ForSAFE
Sverdrup & Warfvinge 1993 PROFILE:
- H+
- H2O
- CO2
- organic ligands
- temperature
- soil moisture
- mineral reactive surface

등을 이용한 mechanistic mineral dissolution.

Wallman et al. 2005 ForSAFE와 Kronnäs et al. 2019:
- forest growth
- nutrient uptake
- litter decomposition
- hydrology
- soil chemistry
- weathering

사이의 dynamic feedback을 구현.

### Banwart et al. 2009
```
biological productivity
 -> soil CO2 / DOC / proton balance
 -> pH
 -> mineral dissolution
```

### Taylor et al. 2011 / 2012
후속 범위 수정에 따라 균근-specific 항은 production/sensitivity에서 제외한다.

Taylor 2012는 DGVM -> process-based weathering이라는 상위 구조만 참고한다.

### REWTCrunch 2022
기존 archive 재확인:

```
root biomass(z,t)
 -> root exudation
 -> microbial / chemical reactions
 -> mineral dissolution
```

daily reactive-transport precedent.

---

## 중요한 nonlinearity / 반대부호 경로

### Oeser & von Blanckenburg 2020
NPP가 증가한다고 weathering rate가 체계적으로 증가하지 않았다.

증가한 nutrient demand가 nutrient recycling으로 충족될 수 있다.

따라서 금지:

```
W_chem = W_abiotic * f(NPP)
```

형태의 단순 양의 multiplier.

### Zuo et al. 2024
식생은 erosion을 억제하여 fresh-mineral supply를 줄일 수 있다.

```
vegetation
 -> erosion suppression
 -> fresh-mineral supply reduction
 -> supply-limited weathering reduction
```

따라서 식생은 weathering을 증가시키는 경로와 감소시키는 경로를 동시에 가질 수 있다.

### Osorio-Leon et al. 2025
16 m bedrock vadose zone의 reactive-transport model에서 deep-root-associated CO2 production을 명시해야 관측 chemistry가 재현됨.

해당 현장:
- deep-root-associated processes: BVZ solute weathering flux의 약 43 ± 3%
- deep-rhizosphere carbonic-acid effect 포함 시 background 대비 약 1.8 ± 0.1배

이 값은 고운사 coefficient로 직접 전이하지 않는다.

역할:
- deep-root respiration pathway의 강한 정량 근거
- root-access depth가 H_AB보다 깊을 수 있다는 근거

---

## living-root biomechanical weathering 재검토

### Pawlik et al. 2023
sandstone fracture에서 root weathering field evidence.
그러나 annual production law 없음.

### Malik et al. 2019
root anatomy가 crack widening을 기록하지만 root pressure 자체가 원인이라는 증거는 inconclusive.

### Calusi et al. 2020
mechanical inclusion numerical model:

```
root growth
 -> contact stress
 -> fracturable matrix
 -> fracture-regrowth cycle
```

그러나 soil/artificial medium 대상이며 sandstone bedrock production model이 아님.

### Wright et al. 2026
EGU conference abstract.
FE + SRXCT로 high-strength environment에서 crack propagation을 검토.

결론:

```
living-root biomechanical weathering
= physically plausible
= emerging quantitative mechanics
!= production-ready sandstone annual soil-production law
```

따라서 현재 production에는:

```
P_sand(H) * f(root biomass)
```

형태의 임의 multiplier를 넣지 않는다.

---

## sandstone soil production과 chemical weathering의 분리

유지:

```
P_sand(H)
!=
W_chem
```

### P_sand(H)
- parent material -> mobile soil / boundary lowering
- Mode A exponential
- Mode B shallow finite-depth hump / zero-depth suppression

### W_chem
- dissolved chemical mass loss
- nutrient release
- vegetation-aware WITCH/PROFILE-style chemistry

WITCH를 parent-material reaction front까지 확장하여 mineral dissolution을 직접 boundary lowering으로 환산하면 P_sand를 residual physical production으로 재분해하거나 제거해야 한다.

같은 mass를 두 번 계산하지 않는다.

---

## 사면수송 구조는 유지

```
q_hill
=
q_bg
+
q_root
+
q_dryravel
```

- q_bg: Landlab DepthDependentDiffuser, no biomass multiplier
- q_root: LPJ-GUESS root state / turnover -> Gabet
- q_dryravel: vegetation storage / fire disturbance
- SWEHR: roots / litter / surface resistance

따라서 vegetation effects are process-specific, not a single geomorphic coefficient.

---

## 새로 생성한 paper files

- `papers/1993_Sverdrup_Warfvinge_PROFILE.md`
- `papers/2005_Wallman_ForSAFE.md`
- `papers/2006_Godderis_WITCH_ForestWeathering.md`
- `papers/2009_Banwart_BiologicalProtonWeathering.md`
- `papers/2010_Roelandt_BWITCH_LPJ_Weathering.md`
- `papers/2011_Taylor_Ectomycorrhiza_WeatheringModel.md`
- `papers/2016_Pawlik_RootsRockRegolithReview.md`
- `papers/2019_Kronnas_ForSAFE_Weathering.md`
- `papers/2019_Malik_RootCrackBiomechanicalWeathering.md`
- `papers/2020_Calusi_RootMechanicalInclusion.md`
- `papers/2026_Wright_RootFracture_FE_Conference.md`

Taylor 2012 중복:
- 기존 canonical `papers/2012_Taylor_DGVMWeathering.md`에 상세 내용을 병합
- 중복 `papers/2012_Taylor_GlobalBiologicalWeathering.md` 삭제
- 동일 DOI `10.1098/rstb.2011.0251`

---

## 새 model / decision

- `models/B_WITCH.md`
- `models/Vegetation_Weathering_Coupling.md`
- `decisions/2026-09-21_VEGETATION_WEATHERING_COUPLING.md`

수정:
- `MASTER.md`
- `models/Short_Timestep_Weathering_HillslopeTransport.md`
- `models/Landlab_ShallowSoil_Weathering_Creep.md`
- `models/Sandstone_Soil_Production.md`
- `papers/2025_DantasDePaula_LPJGUESS_CNP_Weathering.md`
- `papers/2010_Gabet_Mudd_RootFractureTreeThrow.md`

---

## 현재 authoritative weathering structure

```
CHEMICAL WEATHERING

LPJ-GUESS
 -> B-WITCH-style vegetation interface
 -> WITCH/PROFILE mineral kinetics
 -> W_chem + nutrient release
 -> LPJ-GUESS-CNP [new return coupling]

Hartmann/LPJ-GUESS-CNP
 -> low-cost benchmark

REWTCrunch
 -> advanced root-exudation sensitivity


PHYSICAL / SOIL PRODUCTION

P_sand(H)
 -> Mode A / Mode B
 -> no arbitrary root biomass multiplier

fire spall
 -> separate physical supply [still unresolved]

living-root fracture
 -> optional / unresolved
 -> no production coefficient yet
```

---

## 다음 작업 우선순위

1. LPJ-GUESS에서 B-WITCH/WITCH에 실제 전달 가능한 변수와 단위 mapping
2. WITCH/PROFILE 중 고운사 production에 더 실용적인 chemistry core 선택
3. 고운사 sandstone mineralogy에 맞춘 mineral assemblage / kinetic parameter set
4. LPJ-GUESS-CNP P pool로 nutrient release를 되돌리는 mass-conserved coupling 설계
5. root respiration / soil CO2를 LPJ-GUESS에서 어떻게 얻거나 계산할지 확인
6. REWTCrunch root-exudation을 sensitivity로 어느 수준까지 단순화할지 결정
7. fire-spall production
8. coarse-fragment supply / armour

Do not return to:
- Pelletier as production engine
- tree throw/uprooting production
- shallow landslide production
- arbitrary NPP/biomass weathering multiplier


---

## post-audit completion

최종 consistency audit에서 `MASTER.md` 후반에 남아 있던 옛 Hartmann-only scaffold와 tree-throw production hierarchy를 발견하여 정리했다.

최종 상태:
- complete chemical-weathering production target = LPJ-GUESS -> B-WITCH-style interface -> WITCH/PROFILE
- Hartmann/LPJ-GUESS-CNP = low-cost benchmark
- Gabet-Mudd/Doane/Constantine tree-throw lineage = archive/reference only
- no stale `daily LPJ-GUESS/Hartmann chemical dissolved-weathering forcing` production statement remains in MASTER
- direct living-root sandstone fracture = optional/unresolved, not production-ready
- `INDEX.md` regenerated from actual branch tree

Final actual index counts:
```
Papers    325
Models     40
Decisions  19
Sessions    8
```

Key final commits in this audit:
- vegetation-weathering decision refinement: `6d8ff09534d04c47e1c5903bff064924bbb8f50a`
- vegetation-weathering model refinement: `d66ad63f64488cec9235b9e4a935ad1ad31f53b0`
- MASTER nonlinear constraints: `a439cba20d543dd6a851edbf72d9e2fb41290466`
- INDEX regeneration: `3f6341f14ad8b6a25ec02f62418585572319dd82`
- final MASTER stale-text cleanup: `4bc39048266845a14d7e144f90cf4f3f6f1ffad4`


---

## later scope correction: mycorrhiza excluded

사용자 범위 수정에 따라 균근(mycorrhiza)은 현재 고운사 production 및 sensitivity에서 제외한다.

Authoritative decision:
`decisions/2026-09-21_MYCORRHIZA_EXCLUSION.md`

관련 문헌은 archive/reference only이며, 이후 구현에는 다음 변수를 만들지 않는다.

```
mycorrhizal_type
AM / EcM state
fungal weathering source
fungal oxalate allocation
```

Non-mycorrhizal vegetation-weathering pathways만 유지:
- root respiration / soil CO2
- root depth/distribution
- root water uptake
- litter/SOM
- DOC/organic-ligand sensitivity without fungal parameterization
- nutrient uptake/return
- hydrology
