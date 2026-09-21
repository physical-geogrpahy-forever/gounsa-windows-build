# Gounsa Literature Master

업데이트: 2026-09-21

이 문서는 고운사 산불 후 식생-지형 상호작용 모델 문헌검토의 **단일 통합 요약본**이다.

세부 서지, 식, 적용환경, 한계는 `papers/`의 논문별 파일과 `models/`의 모델 계보 파일을 우선한다.
채택/탈락/새로운 coupling의 경계는 `decisions/`가 최우선 기록이다.

---

# 1. 프로젝트 목표

고운사 산불 이후 약 100년 동안 다음 과정을 함께 모의한다.

```
산불
 -> 식생 소실 및 회복
 -> 유수침식 변화
 -> 사면 creep / root-growth transport / dry ravel
 -> soil-regolith weathering / production
 -> fire-spall 및 coarse-fragment supply
 -> 지형 변화
 -> 다시 식생에 feedback

현재 production baseline에서 제외:
- tree throw / uprooting
- shallow landslide
```

식생 동태는 LPJ-GUESS를 중심으로 하고, 지형과정에는 가능한 한 기존 published equations를 그대로 사용한다.

---

# 2. 고정 원칙

1. COPLAS는 최종모델의 식, 철학, parameterization 근거에서 제외한다.
2. MUSLE는 최종 산지 유수침식식에서 제외한다.
3. vegetation cover 하나로 모든 식생효과를 표현하지 않는다.
4. root biomass, live/dead root mass, RLD, litter biomass, PFT biomass처럼 정량 상태량을 우선한다.
5. interrill/rill 또는 rainfall-driven/flow-driven 침식을 분리한다.
6. distributed 또는 raster라는 이유만으로 D8 routing을 genuine 2D라고 부르지 않는다.
7. field regression과 실제 numerical-model implementation을 구분한다.
8. 논문에 없는 모델 간 연결은 반드시 **새로운 coupling**이라고 기록한다.
9. 유수침식 root effect와 shallow-landslide root cohesion을 같은 parameter로 합치지 않는다.
10. 이미 결정된 Wu-vs-WEPP 갈림길을 다시 열지 않는다. 둘은 역할이 다르다.
11. chemical weathering에서 vegetation effect를 runoff 하나로 축소하지 않는다. hydrology, soil CO2/respiration, nutrient uptake/return, litter/decomposition의 published pathways를 분리한다.
12. physical sandstone production에는 검증되지 않은 root-biomass multiplier를 임의로 추가하지 않는다.

관련 결정:
- `decisions/2026-09-21_STRICT_2D_QUANTITATIVE_VEGETATION.md`
- `decisions/2026-09-21_EXCLUSIONS.md`
- `decisions/2026-09-21_COUPLING_BOUNDARY.md`
- `decisions/2026-09-21_PROCESS_ARCHITECTURE.md`
- `decisions/2026-09-21_WATER_EROSION_ENGINE_REASSESSMENT.md`
- `decisions/2026-09-21_WEATHERING_HILLSLOPE_TIMESCALE.md`
- `decisions/2026-09-21_WEATHERING_HILLSLOPE_SECOND_PASS_AUDIT.md`
- `decisions/2026-09-21_WEATHERING_MASS_BALANCE.md`
- `decisions/2026-09-21_BACKGROUND_CREEP.md`
- `decisions/2026-09-21_GEOMORPH_SCOPE_CORRECTION.md`
- `decisions/2026-09-21_SANDSTONE_WEATHERING_BASELINE.md`
- `decisions/2026-09-21_SHALLOW_SANDSTONE_PRODUCTION.md`
- `decisions/2026-09-21_WEATHERING_CREEP_IMPLEMENTATION_FRAMEWORK.md`
- `decisions/2026-09-21_VEGETATION_WEATHERING_COUPLING.md`

---

# 3. 가장 중요한 현재 결론

현재까지 검토된 범위에서 다음 네 조건을 **동시에** 만족하는 단일 published model은 확인되지 않았다.

```
genuine 2D
+ mountain / steep forest or postfire applicability
+ quantitative vegetation state
+ interrill/rill or rainfall/flow process separation
```

문헌은 두 계열로 분리된다.

## 3.1 genuine 2D erosion-engine 계열

| 모델 | genuine 2D | process separation | quantitative root state | 산지/산불 선례 | 공개 수정성 | 현재 역할 |
|---|---:|---:|---:|---:|---:|---|
| **SWEHR / McGuire 2016** | O | rainfall/flow | X | **O, steep postfire + TLS** | **GPL C source** | **잠정 1차 구현 엔진** |
| tRIBS-OFM/FEaST | O | rainfall/flow | X | catchment | coupled code 접근 제한 | 구조적 상위 선례 |
| tRIBS-VEGGIE-FEaST | O | rainfall/flow | vegetation state O, direct root-resistance X | event sequence | 제한 | dynamic vegetation + 2D erosion structural precedent |
| SERGHEI-SE | O | rainfall/flow/solid transport | X | catchment | **BSD, public C++/Kokkos** | HPC fallback / port candidate |
| Iber+ 2024 | O | rainfall/flow | X | catchment | public executable, general public source modification not verified | numerics comparison |
| Wu et al. 2020 | O | interrill/rill | X | 제한적 | model-level comparison | Ki/Kr interface benchmark |
| PSEM_2D | O | rainfall/flow | X | 제한적 | comparison | critical-shear lineage benchmark |
| OpenLISEM | O/공간분포형 | splash/flow | external root cohesion, cover weighted | O, burned forest | open source | postfire comparison |

## 3.2 quantitative vegetation -> erosion resistance 계열

| 모델 | quantitative vegetation | interrill/rill | genuine 2D | 현재 역할 |
|---|---:|---:|---:|---|
| WEPP | live/dead roots, residue | O | X | 핵심 Ki/Kr 근거 |
| Mao 2010 VIC-WEPP | roots/residue dynamic adjustment | O | X | published coupling precedent |
| Gould 2016 | WEPP-based wildfire mountain application | O | X | 산불 산지 선례 |
| DANSAT | plant/root/residue dynamics | O | X | dynamic Ki/Kr precedent |
| PROMET/Waldmann | dynamic RLD | 부분/과정별 | X | RLD -> resistance precedent |
| ELM-Erosion | PFT root biomass | rainfall/runoff | X | PFT biomass bridge |

따라서 최종 고운사 모델이 두 계열을 결합하면 그것은 **새로운 coupling**이다.

---

# 4. WEPP에서 확정된 식생-침식 연결

WEPP는 cover-only 모델이 아니다.

## 4.1 interrill erodibility

채팅과 공식 Chapter 7에서 확인한 root multipliers:

```
CKidr = exp(-0.56 * dr)
CKilr = exp(-0.56 * lr)
```

- `dr`: dead root mass
- `lr`: live root mass

이 항들은 adjusted interrill erodibility `Ki`에 들어간다.

## 4.2 rill erodibility

```
CKrbr = exp(-0.4 * br)
CKrdr = exp(-2.2 * dr)
CKrlr = exp(-3.5 * lr)
```

- `br`: buried residue mass
- `dr`: dead root mass
- `lr`: live root mass

## 4.3 주의

현재 복구에서 확정된 root effect는 `Ki`와 `Kr`이다.

```
root biomass -> tau_c
```

를 같은 방식으로 자동 확장하지 않는다. 별도 문헌근거 없이 biomass-dependent `tau_c`를 만들지 않는다.

## 4.4 vegetation pools

WEPP 공식 문서는 다음을 분리한다.

- above-ground biomass
- live root biomass
- dead root biomass
- root depth
- LAI
- canopy
- standing residue
- flat residue
- buried residue
- coarse fragments

이 구조는 LPJ-GUESS output도 가능한 한 하나의 cover로 합치지 않아야 한다는 근거가 된다.

관련:
- `models/WEPP.md`
- `papers/1995_Alberts_WEPP_Soil_Component.md`
- `papers/1995_Arnold_WEPP_Plant_Growth_Component.md`
- `papers/1995_Stott_WEPP_Residue_Component.md`
- `papers/1995_Foster_WEPP_Hillslope_Erosion_Component.md`
- `papers/2022_Lee_WEPP_Erodibility_Critical_Shear.md`

---

# 5. 2D 유수침식 엔진

## 5.1 Wu et al. 2020

Sediment continuity:

```
∂(hc)/∂t + ∂(qx c)/∂x + ∂(qy c)/∂y
= μ D_i + (1-μ) D_r
```

Interrill:
```
D_i = K_i p R I_f F_nozzle
```

Rill:
```
D_r = K_r (τ-τ_c)(1-G/T_c)
```

장점:
- genuine 2D
- explicit interrill/rill
- WEPP/Foster-style parameter interface

한계:
- root biomass/RLD module 없음
- rill location fixed in the 2020 irregular-rill paper

WEPP-derived dynamic `Ki/Kr`를 Wu에 넣으면 **새로운 coupling**이다.

## 5.2 PSEM_2D

Nord & Esteves 2005.

- genuine 2D Saint-Venant
- rainfall detachment
- runoff detachment
- deposition/redetachment
- natural nonplanar surface

식생모듈은 없다.

## 5.3 Iber+ 2024

Suspended sediment:

```
∂(h C_k)/∂t + ∂(q_x C_k)/∂x + ∂(q_y C_k)/∂y
= D_rdd,k + D_rdrd,k + D_fdd,k + D_fdrd,k + D_dep,k
```

Rainfall-driven:
```
D_rdd,k = α_d,k r (1-ε) f_d g_k
```

Flow-driven:
```
D_fdd,k = K_d,k max(τ-τ_s,0)(1-ε)g_k
```

`K_d`는 kg s^-1 N^-1이며 WEPP/Foster-style `Kr`와 차원과 구조가 매우 잘 맞는다.

그러나 WEPP root dependence를 Iber `K_d`에 넣는 것은 **새로운 coupling**이다.

Iber+의 장점:
- GPU finite volume
- genuine 2D
- multiclass sediment
- rainfall/flow separation
- loose-layer shielding
- 2D Exner topography update

현재 현대 2D engine의 핵심 비교후보이다.

---

# 6. vegetation -> erosion resistance의 published precedents

## 6.1 Mao et al. 2010

VIC + WEPP-HE coupling.

Full WEPP를 통해:
- ground cover
- live root biomass
- dead root biomass
- residue

를 erosion-parameter adjustment에 사용하는 구조가 있다.

중요한 의미:
```
dynamic vegetation/soil state
 -> erosion erodibility
```
는 이미 published coupling precedent가 존재한다.

## 6.2 Gould et al. 2016

VIC-WEPP lineage를 Salmon River Basin, northern Rockies에 적용.

따라서:
```
wildfire mountain watershed
+ WEPP-based erosion parameterization
```
의 실제 적용 선례가 있다.

## 6.3 DANSAT

Cho & Mostaghimi 2009.

- dynamic plant growth
- live/dead root states
- residues
- interrill
- rill
- channel detachment
- continuous watershed simulation

강한 vegetation-erodibility precedent이나 agricultural watershed이며 genuine 2D는 아니다.

## 6.4 PROMET/Waldmann

```
root biomass growth
 -> root length increment
 -> soil-layer allocation
 -> RLD
 -> erosion resistance
```

동적 RLD를 사용하는 실제 model implementation precedent.

Upper Danube와 alpine/mountain context는 장점이나 1 km proxel routing이며 genuine 2D는 아니다.

## 6.5 ELM-Erosion

PFT-specific topsoil root biomass를 erosion resistance에 사용한다.

LPJ-GUESS PFT/FineRootC와 개념적으로 가장 가까운 선례 중 하나이나 global/land-model scale이다.

---

# 7. 실험/리뷰에서 확인한 root effect

이 자료는 최종 numerical model 그 자체가 아니라 parameterization 검증용이다.

## Ghidey & Alberts 1997

root density/RLD와 interrill erodibility의 exponential relation을 실험으로 제시.

## Gyssels et al. 2005

공통 synthesis:

```
SEP = exp(-b RP)
```

평균 `b`:
- splash: 약 0
- interrill: RD 0.1195, RLD 0.0022
- rill: RD 0.5930, RLD 0.0460

따라서 roots의 상대적 영향은 concentrated/rill erosion에서 더 강한 경향을 보인다.

이 평균값을 그대로 고운사 모델 계수로 넣는 것은 자동 정당화되지 않는다. sensitivity/validation reference로 우선 사용한다.

---

# 8. OpenLISEM 판정

OpenLISEM source code에서 확인:

```
CohesionSoil
= COHCalibration * (Cohesion + Cover * RootCohesion)
```

`cohadd.map`은 plant-root extra cohesion input이다.

그러나:
- root cohesion is externally supplied
- cover weighting remains
- root biomass/RLD from vegetation model is not dynamically converted internally

따라서 strict quantitative-vegetation 조건을 만족하지 않는다.

장점:
- burned Mediterranean forest catchment application exists
- spatial/2D hydro-erosion framework
- postfire calibration precedent

현재 역할은 비교/검증계보이다.

---

# 9. rill network

## McGuire 2013
- genuine 2D
- rill incision/branching/merging emergent
- vegetation module 없음
- fine microtopographic scale

대표 지형식:
```
∂z/∂t = β∇²z + (D-E)/(1-φ)
```

이 `β∇²z`는 storm-time rain-splash/colluvial process이다.
Pelletier-style long-term hillslope diffusion과 동일시하지 않는다.

McGuire output을 단순 Wu rill-mask generator로 사용하는 것은 **새로운 coupling**이다.

## RillGrow
- cellular automaton
- emergent rill network
- splash, flow erosion/deposition, sidewall slumping
- multi-grain
- bare-soil/plot scale
- D8 local routing

비교계보로 유지한다.

---

# 10. 산지 distributed erosion: WiMMed / HEMINGS

강점:
- mountain/semi-arid basin applications
- raindrop erosion
- rill erosion
- gully erosion
- headcut migration
- long-term sediment transport

그러나 후반 재검증 결과:
- genuine 2D SWE가 아님
- vegetation quantity direct coupling은 충분히 확인되지 않음
- plant residue/cover representation이 남음

따라서 산지 적용성의 근거로 유지하되 strict 최종 solution은 아니다.

---

# 11. shallow landslide

**현재 production baseline에서 제외한다. Archive-only이다.**

Hales 2018, Istanbulluoglu 계열 등 기존 검토 문헌은 향후 범위 재개 시 참고하기 위해 보존한다.

현재 구현에는 다음을 넣지 않는다.

```
root cohesion for landslide
factor of safety
failure probability
landslide event routing
```

유수침식의 root effect와 shallow-landslide root cohesion은 서로 다른 과정이라는 기존 문헌 판정은 유지한다.

```
erosion Ki/Kr root effect != shallow-landslide root cohesion
```

관련 최우선 결정:
`decisions/2026-09-21_GEOMORPH_SCOPE_CORRECTION.md`

---

# 12. biogenic hillslope transport와 soil profile

다음 과정은 서로 합치지 않는다.

## lateral transport
현재 production:
- root growth/decay disturbance

Archive-only:
- tree throw / uprooting
- 관련 organismal displacement 계보 중 tree-throw 기반 항

관련 계보:
- Gabet: 현재 root-growth/decay transport 근거
- Gabet & Mudd, Constantine, Doane, Kirwan/Shugart: archive/reference only where tree throw or uprooting is involved

## vertical/profile mixing
- LORICA
- HydroLorica
- related soil-profile evolution models

vertical mixing을 lateral downslope sediment flux와 동일 diffusion coefficient로 처리하지 않는다.

## 100-year hillslope transport

Pelletier 2013의 biomass-dependent long-term diffusivity를 주식으로 사용하지 않는다.

현재 구조:
```
q_hill
=
q_bg
+
q_rootgrowth
+
q_dryravel
```

- `q_bg`: residual background creep, Furbish 2009 depth-slope structure
- `q_rootgrowth`: Gabet et al. 2003, annual root turnover
- `q_dryravel`: Lamb 2011 postfire disturbance pathway
- shallow landslide는 현재 production에서 제외하며 archive-only로 유지

Roering 2001 nonlinear transport는 steep-slope sensitivity/alternative로 유지한다. 자연산림에서 보정된 total diffusivity를 현재 production의 root-growth transport와 별도로 사용할 경우 double counting 위험이 있으므로 `K` 또는 `D`는 residual background coefficient로 보정해야 한다. Tree throw/uprooting과 shallow landslide는 현재 production에서 제외한다.

Pelletier 2013은 long-term consistency benchmark로만 유지한다.

---

# 13. postfire dry ravel

Lamb et al. 2011.

Mass balance:
```
dh/dt = -(1/w) dQ/dx + (ρ_r/ρ_s) E
```

Vegetation storage:
```
V_c = V_ci c A_b
```

핵심:
```
fire
 -> vegetation sediment-storage capacity collapse
 -> stored loose sediment release
 -> dry-ravel pulse
 -> vegetation recovery and storage recovery
```

이 과정은 fire-spall production 자체가 아니다.

---

# 14. fire spall

현재 가장 중요한 unresolved gap 중 하나.

필요한 것은:
```
fire severity / heating
 -> rock spall production
 -> coarse-fragment supply
```

Lamb dry ravel은 공급된 loose material의 이동/저장을 설명할 수 있지만 thermal spall 생산량을 계산하지 않는다.

따라서:
```
spall production module
+ dry-ravel/storage module
```
을 합치면 **새로운 coupling**이다.

---

# 15. coarse fragments / armour

고운사에서는 coarse fragments를 단순 고정 cover로만 두지 않는 방향을 유지한다.

가능 source:
- prefire gravel
- fines removal로 노출된 residual fragments
- fire-spall fragments

가능 효과:
1. mobile loose sediment supply
2. surface armour로 splash/interrill suppression

WEPP와 EUROSEM lineage에 coarse-fragment treatment 선례가 있으나 최종 상태변수식은 추가 문헌 검증 후 확정한다.

---

# 15.1 vegetation-weathering correction

2026-09-21 재검토 결과, 기존:

```
LPJ-GUESS -> Hartmann
```

만으로는 complete vegetation-weathering feedback을 표현하기에 부족하다.

Published process precedents:

- Goddéris et al. 2006: WITCH + forest water/carbon model
- Roelandt et al. 2010: B-WITCH = LPJ-DGVM + WITCH
- Wallman et al. 2005: ForSAFE
- Kronnäs et al. 2019: dynamic ForSAFE weathering
- Banwart et al. 2009: biological productivity, DOC, pH, mineral dissolution
- Roque-Malo et al. 2022: root exudation -> reactive transport -> mineral weathering

따라서 chemical weathering의 production target은:

```
LPJ-GUESS
 -> hydrology
 -> belowground respiration / soil CO2
 -> nutrient uptake / return
 -> litter / decomposition
 -> WITCH / PROFILE-style mineral kinetics
 -> W_chem + nutrient release
```

이다.

Nutrient release를 LPJ-GUESS-CNP에 다시 넣는 것은 **새로운 coupling**이며, ForSAFE의 양방향 forest-soil feedback을 구조적 선례로 사용한다.

반면 sandstone physical production:

```
P_sand(H)
```

에는 현재 transferable한:

```
FineRootC -> annual sandstone-production rate
```

식이 없으므로 임의 root multiplier를 추가하지 않는다.

Pawlik et al. 2023은 sandstone root weathering의 현장근거이지만 universal rate law가 아니다. Malik et al. 2019도 root pressure 단독 fracture의 증거가 불확실함을 보여준다.

관련:
- `models/B_WITCH.md`
- `models/Vegetation_Weathering_Coupling.md`
- `decisions/2026-09-21_VEGETATION_WEATHERING_COUPLING.md`

---

# 16. 현재 production 전체 architecture

```
LPJ-GUESS
 ├─ PFT / cohorts / AGB
 ├─ FineRootC / root depth / turnover
 ├─ litter / SOM state
 ├─ NPP / nutrient demand
 ├─ soil temperature
 ├─ soil water / runoff / drainage
 └─ vegetation recovery
       |
       +--> water-erosion resistance
       |      ├─ roots / litter
       |      └─ surface state
       |               |
       |               v
       |             SWEHR
       |
       +--> root state + turnover
       |      -> Gabet root-growth/decay transport
       |
       +--> vegetation-weathering interface
              ├─ hydrology / drainage
              ├─ soil CO2 / belowground respiration
              ├─ nutrient uptake / return
              └─ litter / decomposition
                       |
                       v
              WITCH / PROFILE-style
              mineral weathering
                       |
                       ├─ W_chem dissolved mass loss
                       └─ nutrient release
                              |
                              v
                    LPJ-GUESS-CNP nutrient pools
                              |
                              └--> vegetation growth feedback

Hartmann + LPJ-GUESS-CNP
 └─ low-cost hydroclimatic benchmark only

REWTCrunch
 └─ advanced root-exudation sensitivity / validation

Landlab grid
 ├─ shallow-sandstone production P_sand(H)
 |      ├─ Mode A exponential
 |      └─ Mode B shallow finite-depth hump sensitivity
 ├─ residual background creep
 |      -> DepthDependentDiffuser
 ├─ Gabet root-growth/decay flux
 └─ dry-ravel coupling

P_sand(H)
 └─ no arbitrary root-biomass multiplier
    direct biomechanical root weathering remains unresolved/optional

fire
 ├─ vegetation storage loss
 |      -> dry ravel
 └─ spall production [UNRESOLVED]
        |
        v
 coarse-fragment state
        ├─ mobile supply
        └─ armour

ARCHIVE ONLY
 ├─ tree throw / uprooting
 └─ shallow landslide
```

---

# 17. 현재 유수침식 implementation 선택

최신 결정:
`decisions/2026-09-21_WATER_EROSION_ENGINE_REASSESSMENT.md`

## 17.1 잠정 1차 구현 엔진: SWEHR / McGuire 2016

선택 이유:

```
steep postfire mountain
+ genuine 2D
+ rainfall detachment
+ flow entrainment
+ emergent rill
+ original cohesive soil
+ deposited/loose layer
+ shielding
+ multi-size sediment
+ topographic change
+ TLS calibration
+ public GPL C source
```

공개 SWEHR 코드에서 셀별:
- `ASMASK`
- `ADSMASK`
- `JSMASK`
- `UC`
- `UC2`
- `H`
- `M[k]`

를 직접 확인했다.

따라서 새 침식엔진을 만드는 대신 LPJ-GUESS 식생/토양 상태가 기존 SWEHR resistance fields를 갱신하는 구조를 우선한다.

## 17.2 root interface

Gyssels et al. 2005:

```
SEP_root = exp(-b RP)
```

Hairsine-Rose/SWEHR에서 hydraulic forcing 등이 같을 때:

```
E_flow ∝ 1/J
```

따라서 baseline 새 coupling:

```
J_eff
= J_bare / SEP_root
= J_bare * exp(b RP)
```

으로 둔다.

중요:
- 이 식은 기존 published single model이 아니라 **새로운 coupling**
- Gyssels 평균 `b`는 sensitivity/initial prior
- 같은 root effect를 `J`와 `UC`에 동시에 적용하지 않음
- `cohesion -> J` 보편식이 있다고 주장하지 않음

대안 검증계보:

```
RLD
 -> erosion-specific cohesion / soil strength
 -> tau_c
```

근거:
De Baets + Léonard & Richard + PROMET/Waldmann.

그러나 `tau_c -> SWEHR UC` 직접식은 아직 없다.

## 17.3 surface litter interface

SurfaceLitter와 IncorporatedLitter를 분리한다.

Exposed litter:

```
C_lit = 1 - exp(-b_m M_lit)
```

Gregory / WEPP / Pannkuk-Robichaud 계열을 사용한다.

SWEHR rainfall protection의 baseline 새 coupling:

```
f_lit,rain = exp(-k_lit C_lit)

ASMASK_eff = ASMASK_bare * f_lit,rain
```

Pannkuk & Robichaud 2003은 postfire conifer forest, 40% slope에서 직접 mass-cover 및 interrill/rill protection을 검증한 핵심 근거이다.

반면 IncorporatedLitter는 soil structure, `Kr`, `tau_c` 유형 효과로 별도 취급한다.

## 17.4 100-year hourly forcing architecture

강수 forcing은 1시간 자료를 그대로 사용한다.

```
hourly rainfall series
 -> storm-event segmentation
 -> piecewise-constant 1 h rainfall forcing
 -> SWEHR sub-hourly CFL-constrained integration
 -> topography/H/M[k]/PSD persistence
 -> next event
```

SWEHR 내부 numerical time step을 1시간으로 두는 것이 아니다.

LPJ-GUESS는 장기 생태상태를 갱신하고 SWEHR는 실제 침식성 호우사상에서 호출한다.

storm separation dry-gap은 임의값으로 고정하지 않고 hydrologic response와 sensitivity test로 결정한다.

## 17.5 다른 엔진의 역할

### SERGHEI-SE
- public BSD C++/Kokkos/MPI
- 가장 강한 modern open-source HPC fallback
- SWEHR runtime/확장성이 실패하면 본체 승격 또는 Hairsine-Rose-like closure port 검토

### Iber+ 2024
- 현대 GPU finite-volume numerics는 매우 강함
- 일반 공개 배포에서 독립적인 source modification access가 확인되지 않아 현재 1차 구현 본체에서 내림
- source access 확보 시 즉시 재평가

### tRIBS-FEaST
- 2D Hairsine-Rose와 event-to-event surface-state memory의 구조적 상위 선례
- tRIBS-Erosion 100-year simulation은 장기 결합의 계산적 선례

---

# 18. 절대 되돌아가지 않을 결론

- COPLAS를 다시 최종후보로 올리지 않는다.
- MUSLE를 최종 유수침식식으로 쓰지 않는다.
- Wu vs WEPP를 양자택일 문제로 다시 검토하지 않는다.
- OpenLISEM의 external root cohesion을 dynamic root biomass model이라고 부르지 않는다.
- WiMMed D8 routing을 genuine 2D라고 부르지 않는다.
- McGuire를 단순 rill-mask generator라고 부르지 않는다.
- field root regressions를 “완성된 erosion model”이라고 부르지 않는다.
- root effect on Ki/Kr를 tau_c에도 자동 적용하지 않는다.

---

# 19. 미해결 문제

우선순위 순:

1. LPJ-GUESS native root output의 SWEHR coupling mapping과 surface effective-depth weighting
2. 고운사 토양의 `J_bare` calibration과 root-dependent `J_eff` 검증
3. 한국 산림 litter별 dry mass -> cover `b_m`와 cover -> protection `k_lit`
4. 1시간 강수자료의 storm-event separation dry-gap 및 event wrapper
5. actual Gounsa DEM에서 SWEHR runtime / CFL / event count benchmark
6. dead-root mechanical-integrity decay와 fire severity/depth별 root mortality transfer
7. coarse-fragment supply vs armour dynamics
9. fire-spall production의 정량식/수치모델
10. sandstone `P0_sand`/`gamma_sand` calibration과 dissolved chemical mass-loss 규모

유수침식 엔진 자체의 우선순위는 현재:

```
SWEHR = 잠정 1차 구현
SERGHEI-SE = HPC fallback
Iber+ = source access 확보 시 재평가
```

---

# 20. 핵심 모델 계보 파일

- `models/WEPP.md`
- `models/VIC_WEPP.md`
- `models/DANSAT_ANSWERS2000.md`
- `models/Wu_2D.md`
- `models/PSEM_2D.md`
- `models/Iber.md`
- `models/OpenLISEM.md`
- `models/PROMET_DANUBIA.md`
- `models/WiMMed_HEMINGS.md`
- `models/McGuire_RillNetwork.md`
- `models/RillGrow.md`
- `models/SERGHEI_SE.md`
- `models/ELM_Erosion.md`
- `models/Hairsine_Rose_2D_Postfire.md`
- `models/EUROSEM_RootCohesion.md`
- `models/LPJ_GUESS_Root_Erosion_Interface.md`
- `models/Postfire_Root_Persistence_Erosion.md`
- `models/Short_Timestep_Weathering_HillslopeTransport.md`
- `models/TreeThrow_Annual.md`
- `models/SSSPAM.md`
- `models/DynSoil_MErSiM.md`
- `models/Weathering_MassBalance_Regolith.md`
- `models/Residual_Background_Creep.md`

---

# 21. 문헌 사용 원칙

개별 manuscript/model implementation에서 수식이나 계수를 사용할 때:
1. 해당 `papers/` 파일을 확인한다.
2. original paper/technical documentation을 다시 연다.
3. units와 domain of calibration을 확인한다.
4. LPJ-GUESS variable과 의미가 동일한지 확인한다.
5. 동일하지 않으면 conversion을 별도 coupling으로 문서화한다.

이 MASTER는 방향과 판정을 보존하기 위한 통합본이지, 원 논문의 식/표를 대체하지 않는다.


---

## 2026-09-21 LPJ-GUESS biomass-geomorph 복구

이번 채팅에서 유수침식, 사면확산/biogenic transport, 풍화/soil production을 LPJ-GUESS의 동적 PFT/cohort biomass와 연결하는 문헌을 복구했다.

### 현재 확정 원칙
- COPLAS는 최종 고운사 모델 근거에서 제외한다. 비교대상으로만 보존한다.
- MUSLE는 최종 산지 유수침식식에서 제외한다.
- 단일 vegetation cover 대신 PFT/cohort별 quantitative vegetation state를 우선한다.
- root-access depth는 AB soil thickness와 동일시하지 않는다. C/Cr까지 root access를 허용한다.
- 현장실험 회귀식과 실제 수치모델을 구분한다.
- 서로 다른 published model의 결합은 모두 `새로운 coupling`으로 표시한다.

### 유수침식
핵심 모델근거:
- Saco & Moreno-de las Heras 2013: biomass -> SIBERIA erodibility의 직접 선례
- Tan et al. 2022 ELM-Erosion: PFT별 topsoil root biomass effect
- Wang et al. 2024 VED: detachment capacity와 transport capacity에 vegetation effect를 별도 적용

최신 실험근거의 방향:
- FineRootC 자체보다 RMD, RLD, RSAD, SRL, root architecture가 Dc/Kr/tau_c 설명에 더 직접적
- grass, shrub, forest 또는 fibrous/tap root를 동일 계수로 처리하지 않는다
- forest biomass 증가가 erosion resistance의 단조증가를 의미하지 않는다

### 사면확산 및 biogenic transport
현재 작업구조:
`q_hill = q_bg + q_rootgrowth + q_dryravel`

근거:
- Gabet et al. 2003: root mass, turnover, rooting-depth distribution
- Gabet et al. 2003: root growth/decay transport
- Furbish et al. 2009: active-soil-depth dependent residual creep
- Lamb / Roering-Gerber / Jackson-Roering: postfire dry-ravel pathway
- tree throw/uprooting literature is retained as optional archive only

산불 후 dead wood는 SurfaceLitC로만 보내지 않고 CWD 상태를 별도 검토한다.

### 풍화 및 soil/regolith production
100년 시간척도에서 Pelletier 2013을 주식으로 사용하지 않는다.

현재 작업구조:
```
Delta H_prod
=
Delta H_chem_front
+
Delta H_other_phys_if_supported
```

tree throw/rootwad 기반 woody mechanical production은 현재 production baseline에서 제외한다.

핵심 모델:
- **LPJ-GUESS-CNP 2025**: patch별 daily runoff + soil temperature -> daily empirical chemical-weathering/P-release forcing, geomorphic soil-production engine 자체는 아님
- REWTCrunch 2022: deep-root chemical-weathering validation/advanced option
- SoilGen 2022: daily-hydrology 1D chemical-weathering benchmark
- SSSPAM 2019/2021: physical weathering/profile/armour + 100-year feasibility benchmark
- Pelletier 2013: geologic-timescale structural benchmark only

중요:
LPJ-GUESS-CNP weathering output을 geomorphic soil/regolith thickness로 바꾸는 mass/volume conversion은 **새로운 coupling**이다.

### 최신 결정 파일
- [COPLAS/MUSLE 제외](decisions/2026-09-21_COPLAS_MUSLE_EXCLUSION.md)
- [LPJ-GUESS quantitative biomass coupling](decisions/2026-09-21_LPJGUESS_BIOMASS_COUPLING.md)
- [세 지형과정 구조](decisions/2026-09-21_THREE_PROCESS_GEOMORPH_STRUCTURE.md)

### 남은 핵심 gap
1. LPJ-GUESS native root-state output을 geomorphic modules에 전달하는 interface mapping
2. genuine 2D 산지 flow solver와 biomass-dependent detachment 식의 최종 결합
4. deep-root chemical weathering flux -> R/C/Cr mass or thickness production 변환
5. LPJ-GUESS-CNP chemical-weathering flux를 geomorphic solid-mass/thickness 변화로 바꾸는 mass-balance coupling


---

## 2026-09-21 water-erosion deep review 통합

이번 deep review에서 기존 Iber+ 중심 판단을 재검토했다.

### 새 핵심
- McGuire 2016 SWEHR를 top-tier가 아니라 **잠정 1차 구현 엔진**으로 승격
- SWEHR 공개 GPL C source에서 cell-wise `J/UC/rainfall detachability/H/M[k]` 확인
- SERGHEI-SE를 public BSD modern HPC fallback으로 승격
- Iber+는 일반 공개 source-access 제약 때문에 구현 본체 우선순위 하향
- tRIBS-FEaST를 event-memory와 dynamic vegetation + 2D Hairsine-Rose 구조적 선례로 채택

### root
```
LPJ-GUESS native root state
 -> RLD_eff
 -> SEP_root
 -> J_eff
```

의 새 coupling을 baseline으로 검토한다.

### litter
```
SurfaceLitter mass
 -> litter-type cover
 -> rainfall protection
```

을 사용하고 IncorporatedLitter는 별도 soil-resistance pool로 둔다.

### 시간구조
1시간 강수자료를 외부 forcing으로 쓰되 SWEHR 내부는 CFL 조건의 sub-hourly time step으로 적분한다.

장기 100년 simulation은 continuous SWEHR가 아니라 event-driven wrapper로 구성한다.


---

## 2026-09-21 FineRootC -> RLD 정량 인터페이스 확정

수식/단위 구조는 해결됐다.

```text
RLD_p,i = C_root,p * SRL_C,p * f_p,i / Dz_i
```

- `C_root,p`: LPJ-GUESS fine-root carbon [kg C m^-2 ground]
- `SRL_C,p`: carbon-based specific root length [m root kg C^-1]
- `f_p,i`: PFT별 soil-layer root fraction
- `Dz_i`: layer thickness [m]

따라서 `FineRootC -> RLD` 자체는 더 이상 식이 없는 gap이 아니다. Dantas de Paula et al. 2025의 LPJ-GUESS-NTD SRL 구현, Zhou et al. 2024의 15-layer root fractions, Verbruggen et al. 2025의 vertical root-distribution equation을 결합하면 차원적으로 닫힌다.

한국 산림 제약도 추가했다. Huh et al. 2025에서는 Korean pine과 oak의 0-30 cm total fine-root biomass가 비슷하지만 oak SRL이 전체 토층에서 약 3배, 0-10 cm에서 거의 5배 높아 `same FineRootC != same surface RLD`임을 보여준다. Kim et al. 2017 Pinus densiflora 자료는 국내 소나무 SRL의 토양조건 민감성을 보조한다.

프로젝트 수정: PFT별 SRL/RLD는 LPJ-GUESS가 계산한다. 따라서 외부에서 `SRL_C`를 별도 설정해 production RLD를 재계산하지 않는다. 아래 관계는 output audit/fallback 용도로만 보존한다.

현재 남은 것은:

1. 어떤 LPJ-GUESS native root output을 coupling에 사용할지 확인
2. output의 단위/patch-gridcell normalization 확인
3. surface erosion에 사용할 effective depth
4. postfire live/dead root persistence
5. `RLD -> J_eff`의 local calibration

세부 계보: `models/LPJ_GUESS_Root_Erosion_Interface.md`


---

## 2026-09-21 postfire live/dead-root persistence 확정사항

산불 후 root erosion protection을 live FineRootC 하나로 표현하지 않는다.

필수 상태:

```text
RLD_live
RLD_dead
I_dead = dead-root mechanical integrity
```

Ghidey & Alberts 1997은 dead-root mass/length가 interrill erodibility를 지수적으로 낮추고 soil shear strength를 높인다는 직접 실험식을 제시한다. Wang et al. 2014와 Wang & Zhang 2017은 concentrated-flow erosion에서 dead/live root와 physical binding/live-root bonding을 분리한다.

postfire 시간근거는 Montagnoli 2023, Uljin의 Ramirez et al. 2024, Lei et al. 2022, Vergani et al. 2017, Sousa et al. 2026으로 보강했다. 이들은 산불 직후 dead-root/necromass pulse가 존재하고, 이후 root quantity와 mechanical quality가 수개월부터 수년 동안 함께 저하되며, 새 뿌리 재생이 회복을 담당함을 보여준다.

따라서 다음 처리는 금지한다.

```text
fire mortality -> root resistance = 0 immediately
```

현재 SWEHR용 일반형 후보는:

```text
J_eff = J_bare * exp(b_live*RLD_live + b_dead*RLD_dead_eff)
RLD_dead_eff = RLD_dead * I_dead
```

이나, `b_dead`와 `I_dead(t)`는 아직 production-approved 값이 아니다. slope-stability root-decay 계수를 SWEHR에 직접 이식하지 않는다.

세부: `models/Postfire_Root_Persistence_Erosion.md`


---

## 2026-09-21 LPJ-GUESS native root-state 원칙

PFT별 SRL, root length, RLD, 층별 root distribution 등 LPJ-GUESS가 계산하는 root quantity는 외부에서 별도 parameterization하지 않고 model-native 결과를 사용한다.

Production coupling:

```text
LPJ-GUESS root calculation
 -> native RLD/root-length/layer output
 -> unit/spatial-basis check
 -> erosion-active RLD_eff
 -> SWEHR JSMASK
```

`RLD = C_root * SRL_C * f / Dz`는 output이 직접 제공되지 않을 때의 audit/fallback relation으로만 보존한다. 따라서 PFT별 `SRL_C` 탐색은 현재 유수침식 구현의 다음 우선과제가 아니다.


---

## 2026-09-21 풍화와 사면수송 시간척도 재결정

최신 결정:
`decisions/2026-09-21_WEATHERING_HILLSLOPE_TIMESCALE.md`

### Pelletier 2013 판정
Pelletier는 작은 내부 numerical timestep을 사용하지만 model objective와 constitutive calibration은 geologic timescale이고 결과도 10 Myr landscape states를 비교한다.

따라서:
```
small solver dt != annual ecological process model
```

으로 판정하며 100년 고운사의 주 weathering/diffusion model에서 제외한다.

### chemical weathering
```
LPJ-GUESS-CNP
 -> daily runoff + daily soil temperature
 -> daily chemical weathering
 -> annual accumulation
 -> [NEW] regolith mass/thickness conversion
```

### hillslope transport
```
q_hill
=
q_bg
+
q_rootgrowth
+
q_dryravel
```

- background: residual annual creep
- root growth/decay: Gabet 2003
- dry ravel: Lamb 2011

Roering 2001 nonlinear law is retained as steep-slope sensitivity/alternative, with explicit double-counting control.

### comparison models
- HydroLorica: dynamic daily/monthly/yearly hydrology but authors warn its vegetation representation is not for annual-decadal systems
- SSSPAM: actual 100-year coupled soilscape-landform simulation; useful for physical weathering/armour/profile benchmark but lacks dynamic forest roots
- SoilGen: daily hydrology + chemical soil-profile weathering, 1D
- REWTCrunch: root-induced reactive transport, advanced validation

### 현재 결론
100년 고운사에서는 **Pelletier 단일 장기계수보다 process-specific daily/annual models를 사용한다.**


---

## 2026-09-21 풍화 및 사면수송 2차 문헌감사

최신 감사:
`decisions/2026-09-21_WEATHERING_HILLSLOPE_SECOND_PASS_AUDIT.md`

1차 결론인:
```
Pelletier 2013을 100년 주식으로 사용하지 않고
daily/annual process-specific modules를 사용
```
은 유지한다.

### 중요한 정정

#### Gabet et al. 2021
DOI `10.1029/2020JF005858`은:
```
Hilltop Curvature Increases With the Square Root of Erosion Rate
```
이며 biomass-transport efficiency 논문이 아니다.

기존 잘못된 파일을 삭제하고:
`papers/2021_Gabet_HilltopCurvature_ErosionRate.md`
로 교체했다.

#### Pelletier et al. 2018
DOI `10.1002/esp.4306`은:
```
Which way do you lean? Using slope aspect variations to understand Critical Zone processes and feedbacks
```
이며 직접 biomass -> diffusivity 수치모델이 아니다.

기존 잘못된 파일을 삭제하고:
`papers/2018_Pelletier_SlopeAspect_CriticalZone.md`
로 교체했다.

#### Kirwan & Shugart 2008
peer-reviewed full paper가 아니라 AGU Fall Meeting abstract로 재분류했다.
정량 tree-throw 근거는 Constantine 2012, Doane 2021, Gabet & Mudd 2010을 우선한다.

### chemical weathering의 최종 역할 구분

```
LPJ-GUESS-CNP
= daily chemical-weathering/P-release forcing
!= geomorphic regolith-production engine
```

따라서:

```
weathering flux
 -> solid mass balance
 -> volume conversion
 -> regolith thickness change
```

는 여전히 새로운 coupling이다.

Oeser & von Blanckenburg 2020에 따라 NPP를 보편적 weathering multiplier로 추가하지 않는다.

### postfire hillslope process separation

Roering & Gerber 2005와 Jackson & Roering 2009를 다시 확인하여:

```
background creep
!= postfire dry ravel
!= root-decay / landslide response
```

를 유지한다.

따라서 산불 후 모든 사면수송을 하나의 증가된 diffusivity로 표현하지 않는다.

### 최종 문헌 hierarchy

Production process sources:
- Dantas de Paula et al. 2025
- Gabet & Mudd 2010
- Gabet et al. 2003
- Doane et al. 2021
- Constantine et al. 2012
- Lamb et al. 2011

Advanced validation/sensitivity:
- REWTCrunch 2022
- SoilGen 2022
- Roering 2001
- Roering & Gerber 2005
- Jackson & Roering 2009

Comparison/long-term consistency:
- SSSPAM 2019/2021
- HydroLorica 2020
- Pelletier 2013
- Pelletier et al. 2018
- Gabet et al. 2021


---

## 2026-09-21 weathering mass-balance 확정

최신 결정:
`decisions/2026-09-21_WEATHERING_MASS_BALANCE.md`

풍화는 다음 두 과정으로 분리한다.

```
chemical dissolved mass loss
!=
bedrock-to-regolith front advance
```

### mobile A/B soil

```
M_AB = rho_AB H_AB
```

```
dM_AB/dt
=
Phi_AB
+
D_phys
-
E_phys
-
W_AB
```

Yoo 2007와 Brosens 2020의 mass-balance 계보를 사용한다.

### sandstone soil production

고운사 parent material은 sandstone으로 취급한다.

```
P_sand(h)
=
P0_sand exp(-h/gamma_sand)
```

Sandstone literature:
- Heimsath et al. 2001
- Evans et al. 2019
- Evans et al. 2021

Evans et al. 2021 analogue envelope:

```
P0_sand = 0.071-0.274 mm yr^-1
gamma_sand = 0.80-4.50 m
```

DynSoil/MErSiM은 optional advanced transient mineral/regolith state로 유지한다.

### LPJ-GUESS/Hartmann weathering
Hartmann 2011/2014 parent lineage는 bulk chemical weathering을 먼저 계산하고 lithology-specific P content를 사용해 P release를 얻는다.

따라서 고운사에서는:

```
F_bulk_chem
F_P_release
```

를 별도로 보존한다.

LPJ-GUESS P-weathering output만을 역산해 geomorphic mass loss를 만드는 것이 기본안은 아니다.

### sandstone production hierarchy
- sandstone-specific `P_sand(h)`: production baseline
- DynSoil/MErSiM: optional advanced transient mineral/regolith state
- Braun 2016: optional groundwater/pore-fluid-driven alternative

### 현재 남은 풍화 문제
1. exact Gounsa sandstone petrography
2. local `P0_sand`
3. local `gamma_sand`
4. parent/soil bulk density and porosity
5. chemical dissolved-loss partition
6. fire-spall production
이다.


---

## 2026-09-21 residual background creep 확정

최신 결정:
`decisions/2026-09-21_BACKGROUND_CREEP.md`

기존 임시식:
```
q_bg = -D_bg S
```
을 다음 depth-dependent local-creep 구조로 교체한다.

```
q_bg
=
-K_bg H_* [1-exp(-H_active/H_*)] grad(z)
```

근거:
- Furbish et al. 2009: vertically integrated creep flux의 depth-slope dependence
- Furbish & Haff 2010: local bulk creep와 intermittent/nonlocal transport 분리
- Doane et al. 2021: temperate forest에서 tree throw는 total flux의 약 11-18%만 설명
- Sonoda & Kurashige 2017: 일본 풍화화강암 산림에서 wet-dry residual deformation이 net creep로 누적
- Richards et al. 2011: fauna bioturbation도 nonzero flux
- Deshpande et al. 2021: 외부 disturbance가 없어도 granular creep가 지속될 수 있음

따라서:
```
D*_bg != 0
```
을 기본으로 하지만, Richardson 2019 같은 natural-landscape total diffusivity를 직접 residual coefficient로 사용하지 않는다.

`D*_bg`는:
1. local calibration
2. total flux에서 explicit process flux를 뺀 residual
3. sensitivity prior
순으로 정한다.

Fire multiplier를 임의로 곱하지 않는다. 산불효과는 `H_active`, dry ravel, roots, tree throw, landslide의 explicit states로 우선 전달한다.

Freeze-thaw가 고운사에서 중요하다고 판명되면 Anderson 2002 frost-creep model을 별도 explicit process로 승격한다.


---

## 2026-09-21 production scope correction

최신 범위 결정:
`decisions/2026-09-21_GEOMORPH_SCOPE_CORRECTION.md`

현재 100년 production baseline에서는 다음을 제외한다.

```
tree throw / uprooting
shallow landslide
```

관련 문헌은 archive/reference로 유지하되 구현 우선순위에서 제거한다.

현재 핵심 지형과정:

```
water erosion
+ residual background creep
+ root-growth/decay transport
+ postfire dry ravel
+ soil/regolith weathering and production
+ fire spall / coarse fragments
```

사면수송:

```
q_hill
=
q_bg
+
q_rootgrowth
+
q_dryravel
```

풍화/생산에서는 rootwad/tree-throw 기반 production을 기본항에서 제거한다.

따라서 현재 다음 구현을 진행하지 않는다.
- windthrow probability
- DBH -> root plate volume
- pit/mound transport
- landslide factor of safety
- shallow-landslide root cohesion

필요성이 후속 자료에서 확인될 때만 optional module로 재검토한다.


---

## 2026-09-21 sandstone lithology correction

고운사 parent material은 **sandstone**으로 취급한다.

최신 결정: `decisions/2026-09-21_SANDSTONE_WEATHERING_BASELINE.md`

Production baseline:

```text
P_sand(h) = P0_sand exp(-h/gamma_sand)
```

Sandstone field constraints:
- Evans et al. 2019: 0.026-0.096 mm yr^-1
- temperate conifer woodland mean: 0.070 +/- 0.010 mm yr^-1
- Evans et al. 2021: P0_sand = 0.071-0.274 mm yr^-1
- Evans et al. 2021: gamma_sand = 0.80-4.50 m

따라서 granite analog를 이용해 century-scale soil production이 negligible하다고 가정하지 않는다.

Final P0_sand/gamma_sand는 matrix abundance, cement type, permeability, tensile strength, fracture density를 확인한 뒤 정한다.

Chemical dissolved mass loss W_chem은 P_sand와 별도 질량수지항으로 유지한다.

DynSoil/MErSiM과 Braun 2016은 optional advanced sensitivity model로 둔다.


---

## 2026-09-21 shallow-soil sandstone correction

Project condition:
```
sandstone + shallow mobile soil
```

Latest decision:
`decisions/2026-09-21_SHALLOW_SANDSTONE_PRODUCTION.md`

### sandstone production
Do not hard-lock:
```
P(h)=P0 exp(-h/gamma)
```
as a universal relation down to bare bedrock.

Required modes:

```
mode A
= Evans-style exponential sandstone production

mode B
= shallow-soil humped / zero-depth-suppressed sensitivity
```

Oregon sandstone evidence permits a finite-depth production peak around the shallow-soil range and reduced production near bare/exposed bedrock.

Therefore:
```
less soil
!= always faster production all the way to h=0
```

### creep
Shallow mobile soil strengthens the current baseline:

```
q_bg
=
-D*_bg H_active grad(z)
```

because small `H_active` directly limits residual creep.

Current hillslope transport remains:

```
q_hill
=
q_bg
+
q_rootgrowth
+
q_dryravel
```

with strict mobile-soil availability caps.

### current priority
1. actual Gounsa `H_AB` distribution
2. shallow sandstone production regime
3. local sandstone matrix/cementation
4. fire-spall/coarse-fragment production
5. compare 100-year production against erosion/export

Deep-regolith DynSoil/MErSiM remains optional rather than the next priority.


---

## 2026-09-21 shallow-sandstone Landlab production baseline

이 절은 풍화/사면 creep에 대한 현재 production 기준을 요약하며 이전 임시식보다 우선한다.

### scope

포함:
```
water erosion
residual background creep
root-growth/decay transport
postfire dry ravel
sandstone soil production
chemical dissolved weathering
fire spall / coarse-fragment supply
```

제외:
```
tree throw / uprooting
shallow landslide
```

Tree-throw 관련 decision/model files는 archive-only다.

### hillslope transport

```
q_hill
=
q_bg
+
q_root
+
q_dryravel
```

Residual creep:

```
q_bg
=
-K_bg H_* [1-exp(-H/H_*)] grad(z)
```

For shallow soil:

```
H << H_*
```

```
q_bg
approx
-K_bg H grad(z)
```

Implementation:
Landlab `DepthDependentDiffuser`.

Root-growth/decay transport:

```
q_root
=
x r tau / rho_r
```

with the Gabet et al. 2003 geometry/turnover formulation and LPJ-GUESS native root state.

Do not encode root effects again inside `K_bg`.

Dry ravel remains a separate postfire transport process.

### sandstone production

Current mandatory sensitivity modes:

```
Mode A:
P_A(H)
=
P0 exp(-H/gamma)
```

```
Mode B:
shallow-soil finite-depth hump / zero-depth suppression sensitivity
```

Mode B functional form/coefficients are **not invented** before suitable local/regional evidence.

The reason for Mode B is that shallow Oregon sandstone evidence permits lower production toward very thin/exposed bedrock and a finite-depth high-production zone around roughly 0.15-0.30 m.

### 100-year analogue envelope

For Evans et al. 2021 sandstone `P0,gamma` pairs and shallow soils around 0.05-0.30 m, the simple exponential sensitivity gives approximately:

- Comer: 7.2-7.6 mm / 100 yr
- Hilton: 15.7-17.2 mm / 100 yr
- Rufford: 6.2-6.9 mm / 100 yr
- Woburn: 18.8-25.7 mm / 100 yr

Oregon thin-soil sandstone evidence provides a broader order-of-magnitude sensitivity of roughly 15-35 mm / 100 yr in some shallow regimes.

These are **analogue sensitivity values, not Gounsa predictions**.

Therefore sandstone production is not omitted merely because the simulation horizon is 100 years.

### chemical weathering

```
P_sand
!=
W_chem
```

Use:
- slow sandstone parent-material production: `P_sand(H)`
- daily LPJ-GUESS/Hartmann chemical dissolved-weathering forcing: `W_chem`

Do not apply arbitrary climate, biomass or fire multipliers to `P_sand` without separate evidence.

### Landlab numerical scaffold

```
LPJ-GUESS
├─ root state + turnover
│  └─ Gabet q_root
├─ runoff + soil T
│  └─ Hartmann chemical dissolved weathering
└─ vegetation recovery

Landlab grid
├─ soil__depth
├─ bedrock__elevation
├─ topographic__elevation
├─ custom sandstone weatherer
│  ├─ Mode A
│  └─ Mode B
├─ DepthDependentDiffuser
├─ Gabet root flux
└─ dry-ravel coupling

SWEHR
└─ event-scale water erosion
```

Optional only:
`DepthDependentTaylorDiffuser` for steep-slope sensitivity.

Pelletier 2013 remains long-term comparison only and is not a production engine.
