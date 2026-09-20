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
 -> 사면 토사이동
 -> shallow landslide
 -> tree throw / root bioturbation
 -> soil production / weathering
 -> fire-spall 및 coarse-fragment supply
 -> 지형 변화
 -> 다시 식생에 feedback
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

관련 결정:
- `decisions/2026-09-21_STRICT_2D_QUANTITATIVE_VEGETATION.md`
- `decisions/2026-09-21_EXCLUSIONS.md`
- `decisions/2026-09-21_COUPLING_BOUNDARY.md`
- `decisions/2026-09-21_PROCESS_ARCHITECTURE.md`

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

| 모델 | genuine 2D | process separation | quantitative root state | 산지/산불 선례 | 현재 역할 |
|---|---:|---:|---:|---:|---|
| Wu et al. 2020 | O | interrill/rill | X | 제한적 | 2D erosion skeleton |
| PSEM_2D | O | rainfall/flow | X | 제한적 | 2D 비교엔진 |
| Iber+ 2024 | O | rainfall/flow | X | catchment scale | 핵심 현대 2D 후보 |
| McGuire 2013 | O | emergent rill | X | 실험 hillslope | rill-network benchmark |
| OpenLISEM | O/공간분포형 | splash/flow | external root cohesion, cover weighted | O, burned forest | postfire comparison |
| SERGHEI-SE | O | hydro-erosive source terms | X | catchment framework | 최신 HPC 비교엔진 |

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

유수침식 erodibility와 별도 모듈로 둔다.

권장 architecture:

```
LPJ-GUESS FineRootC
 -> root vertical distribution / architecture
 -> RAR / diameter / tensile properties
 -> root reinforcement or c_r
 -> factor of safety
 -> shallow landslide
```

Hales 2018은 biome-scale root reinforcement의 주요 근거이다.

Istanbulluoglu 계열은 postfire vegetation loss/recovery와 slope stability/sediment response를 함께 생각하는 구조적 근거이다.

중요:
```
erosion Ki/Kr root effect != shallow-landslide root cohesion
```

---

# 12. biogenic hillslope transport와 soil profile

다음 과정은 서로 합치지 않는다.

## lateral transport
- root growth/decay disturbance
- tree throw
- organismal soil displacement

관련 계보:
- Gabet
- Gabet & Mudd
- Constantine
- Doane
- Kirwan/Shugart

## vertical/profile mixing
- LORICA
- HydroLorica
- related soil-profile evolution models

vertical mixing을 lateral downslope sediment flux와 동일 diffusion coefficient로 처리하지 않는다.

## long-term landscape/soil evolution
- Pelletier 2013
- Pelak 2016
- related soil-production/weathering studies

100-year 고운사에서는 장기항의 실제 크기를 sensitivity로 확인한다.

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

# 16. 현재 잠정 전체 architecture

```
LPJ-GUESS
 ├─ PFT
 ├─ AGB
 ├─ FineRootC
 ├─ dead-root state
 ├─ litter
 └─ root depth/distribution
       |
       +--> water erosion interface
       |      ├─ interrill / rainfall-driven
       |      └─ rill / flow-driven
       |               |
       |               v
       |        genuine 2D hydro-erosion engine
       |
       +--> root mechanics
       |      -> c_r / reinforcement
       |      -> shallow landslide
       |
       +--> biogenic transport
       |      -> root disturbance / tree throw
       |
       +--> soil production / weathering
       |
fire --+--> spall production [UNRESOLVED]
              |
              v
       coarse-fragment state
              |
              +--> mobile supply
              +--> armour

fire
 -> vegetation storage loss
 -> dry ravel (Lamb)
```

---

# 17. 현재 유수침식 implementation 선택 문제

이 문헌 아카이브는 아직 특정 2D engine을 최종 확정하지 않는다.

현재 주요 비교:

### Wu 2020
장점:
- explicit interrill/rill
- direct Ki/Kr interface
단점:
- fixed rill mask
- older 2D formulation

### Iber+ 2024
장점:
- modern finite volume/GPU
- rainfall/flow detachment
- multiclass + Exner
단점:
- no root state
- mapping WEPP Ki/Kr biology requires new coupling

### PSEM_2D
장점:
- clean 2D rainfall/runoff erosion
단점:
- plot/bare soil orientation

### SERGHEI-SE
장점:
- latest HPC/catchment architecture
단점:
- no quantitative root state

최종 선택은 구현 가능성, 산지 DEM resolution, computational cost, vegetation-interface defensibility를 함께 평가한 뒤 결정한다.

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

1. fire-spall production의 정량식/수치모델
2. LPJ-GUESS FineRootC -> erosion-model root mass/RLD의 단위와 depth mapping
3. dead-root pool의 fire mortality 후 시간변화
4. litter biomass -> rainfall/interrill protection을 cover로 축약하지 않는 가장 방어적인 published interface
5. 2D engine 최종선택: Wu vs Iber+ vs SERGHEI-SE 등 구현 비교
6. coarse-fragment supply vs armour dynamics
7. shallow-landslide root architecture conversion
8. 100-year scale에서 long-term creep/weathering 항의 실제 중요도

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

---

# 21. 문헌 사용 원칙

개별 manuscript/model implementation에서 수식이나 계수를 사용할 때:
1. 해당 `papers/` 파일을 확인한다.
2. original paper/technical documentation을 다시 연다.
3. units와 domain of calibration을 확인한다.
4. LPJ-GUESS variable과 의미가 동일한지 확인한다.
5. 동일하지 않으면 conversion을 별도 coupling으로 문서화한다.

이 MASTER는 방향과 판정을 보존하기 위한 통합본이지, 원 논문의 식/표를 대체하지 않는다.
