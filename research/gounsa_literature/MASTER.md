# Gounsa Literature Master

> **2026-10-26 실제 원본 Windows 2D 재시험 최종 판정: OpenLISEM 7.5.2 고운사 침식 주모델에서 제외(NO-GO).** 공식 원본 lisem.exe로 2D 계산 12회 성공, 강우 20mm, 양의 경계 유출, 전역 물/유사수지 폐합까지 확인했으나 유사유출량은 참나무 기본식 5/10/20초 각각 0.005993/123.037727/832.588686kg/ha, 참나무 개발진 제공 대체 침강식도 0.030954/28.707586/268.530307kg/ha로 극심하게 비수렴. 억새 대체식도 0.018893/0.044177/88.121322kg/ha. 20초 참나무 원본 기본식 최대 격자 순침식 5982.9t/ha로 가상 25cm 토층 3375t/ha 초과. 과거 실패가 **재현**됐으므로 LAI 기반 차단 및 2D 흐름 구현과 별개로 원본 버전은 고운사 침식 계산용으로 불합격. [새 Windows 원본 시험 보고](decisions/2026-10-26_OPENLISEM_752_NATIVE_2D_STABILITY_FAILED.md), [Actions](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304135775). 

> **2026-10-26 OpenLISEM 최종 GO/NO-GO 판단 규칙:** 과거 원본 Windows 7.5.2 전체 실행은 가능했으나 계산 시간간격 의존성 및 100μm 침전속도 오류, 유한 토층 제한 부재로 침식 결과 **이미 FAIL baseline**. 이번 `v7.5.2` 및 `main_C` 공개 소스 재확인 결과 두 계보의 `GetSV` 원식이 동일하고 `main_C`의 `DetachMaterial()` 호출은 여전히 주석 처리, `SwitchUseMaterialDepth=false`. LAI/interception/2D 기능만으로 채택 금지. **원본 지원 옵션으로 경계/설정 정상화 후 2D 시간간격 수렴, 토사저장량, 침강, 물/유사수지가 통과하지 못하면 고운사 유수침식 엔진으로 폐기.** 수정 포크 성공은 원본 통과로 간주하지 않음. [사전 등록 검증 게이트](decisions/2026-10-26_OPENLISEM_NUMERICAL_GO_NOGO_GATES.md).

> **2026-10-26 중대 정정(운영 판정 우선):** OpenLISEM `v7.5.2` 원본 Windows 실행은 **2026-10-23 실제로 성공**했다(공식 `lisem.exe` headless 전체 모델, Actions runs `39928519655`, `39929498985`). 그러나 합성 고운사 사면의 침식 출력은 **시간간격 수렴성 실패**(운동파 참나무 유사유출 0.25→10초에서 19.714→853.798 kg/ha), **2D 격자별 과도한 순침식**(참나무 10초에서 200,566.703 t/ha ≈ 14.86m 토층), **원본 GetSV 100μm 분기 침전속도 오류**(1.27226m/s, 99.9μm 대비 141.8배), `DetachMaterial()` 비활성 등 문제가 확인됐다. 10월25일 factory 시험에는 `Advanced Options` 입력 생성 오류, GUI/엔진 설정 키 불일치, 유출구 배치 미검증도 중첩. **따라서 OpenLISEM이 LAI 차단+2D 직접유출 침식+산지 적용 세 조건을 기능 차원에서 갖춘 사실은 유효하지만, 원본 7.5.2를 바로 고운사 유수침식 주 엔진으로 재선정해서는 안 된다.** 정확한 이유와 QA 상태: [실패 원인 복구](decisions/2026-10-26_OPENLISEM_752_PREVIOUS_NUMERICAL_FAILURE_RECOVERY.md). 


> **2026-10-26 신규 확인(OpenLISEM, 기존 미확정 판정 유지):** 원본 `vjetten/openlisem` `main_C` SHA `d894c72428947247ce49eb88353dadf49b3123e8`의 `lisInterception.cpp` LAI 저장/수관통과, `lisErosionSplash.cpp` 직접강우와 잎 적하 에너지 분리, `lisSWOF2DSediment.cpp` 원본 2D 유출박리/수송 확인. **Opedes et al. (2025, DOI 10.1002/esp.70074)** 는 Mount Elgon Ukha 44.5km² 산지, 12.5m, 15s, 실제 2D dynamic wave와 LAI/height/litter/rock/root extra cohesion 입력을 사용했고 유출 NSE .72/KGE .61이나 침식 관측 검증은 없음. 코드는 stemflow input 주석 처리, 자동 개체별 SF 및 RLD 변환 없음. Windows 7.5.2 실행과 코드 hash 일치/물유사수지도 아직 미검증. **세 사용자 우선 조건에 매우 유망하나 stricter native dynamic root criterion 및 최종 실행 QA를 통과한 엔진으로 간주하지 않는다.** 기록: [원본 소스 + 급경사지 판정](decisions/2026-10-26_OPENLISEM_THREE_CRITERIA_SOURCE_AND_STEEP_SLOPE_AUDIT.md), [Opedes 2025](papers/2025_Opedes_OpenLISEM_MountElgon_Trenches.md), [OpenLISEM model lineage](models/OpenLISEM.md).

> **2026-10-26 긴급 정정: 고운사 유수침식 모형 채택 상태 = 미확정.** 이전 채팅에서 제안된 "SHETRAN 제외 → SWEHR이면 된다"는 결론을 명시적으로 철회한다. 원본 SWEHR 2017 공개 C에는 2016 연구논문의 Rutter 수관차단과 수관충격 차폐가 구현되었다고 입증되지 않으며, 기존 38개 사례는 임의 계수를 넣은 수정 포크일 뿐 원본 식생 모델이나 현장 결과가 아니다. SHETRAN 4.7.2의 native 강우사상 실행 성공은 고운사 세류 침식과 공간별 DEM 변화의 검증이 아니다. EUROSEM은 본질적 2D 유동 요구조건을 충족하지 않는다. Iber+는 학술 검증 연구가 있지만 연구자의 요구인 온전한 공개 소스 및 필요한 식생 결합 인터페이스가 확인되지 않아 오늘의 채택 판정을 내릴 수 없다. **유효한 단일 주 엔진이 확보되었다고 주장 금지.** 근거: [SWEHR 원본 코드 부재 확인](decisions/2026-10-26_OFFICIAL_SWEHR_V1_0_ORIGINAL_CODE_PROVENANCE.md), [SHETRAN 적합성 재검토](decisions/2026-10-26_SHETRAN_FIT_FOR_PURPOSE_REASSESSMENT.md), [Iber+ 등 기존 비교](decisions/2026-10-26_EUROSEM_SWEHR_IBERPLUS_COMPARISON.md).


업데이트: 2026-10-26

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
`q_hill = q_creep + q_rootgrowth + q_treethrow`

근거:
- Gabet et al. 2003: root mass, turnover, rooting-depth distribution
- Gabet & Mudd 2010: root fracture와 tree throw
- Doane et al. 2021/2023/2024: tree throw와 hillslope roughness 계보
- Adams et al. 2023: post-fire CWD sediment storage/connectivity

산불 후 dead wood는 SurfaceLitC로만 보내지 않고 CWD 상태를 별도 검토한다.

### 풍화 및 soil/regolith production
현재 작업구조:
`W_total = W_hydroclimatic + W_deep_root_chemical + W_woody_mechanical`

근거:
- Pelak et al. 2016: biomass-driven soil production의 최소모델
- Gabet & Mudd 2010: woody mechanical weathering
- REWTCrunch 2022: root biomass/exudation -> reactive weathering
- Pawlik et al. 2023/2024: living tree roots와 soil formation의 최근 현장근거
- Osorio-Leon et al. 2025: deep roots가 bedrock-vadose-zone silicate weathering을 정량적으로 강화
- Billings et al. 2025: deep root-regolith interaction의 biome-scale 근거
- Bemis et al. 2026: bare rock -> moss -> grass -> shrub -> tree succession과 Critical Zone 생성

### 최신 결정 파일
- [COPLAS/MUSLE 제외](decisions/2026-09-21_COPLAS_MUSLE_EXCLUSION.md)
- [LPJ-GUESS quantitative biomass coupling](decisions/2026-09-21_LPJGUESS_BIOMASS_COUPLING.md)
- [세 지형과정 구조](decisions/2026-09-21_THREE_PROCESS_GEOMORPH_STRUCTURE.md)

### 남은 핵심 gap
1. FineRootC -> RMD/RLD/RSAD/SRL의 PFT별 변환
2. genuine 2D 산지 flow solver와 biomass-dependent detachment 식의 최종 결합
3. WoodC/cohort mortality -> tree throw/CWD의 정량 변환
4. deep-root chemical weathering flux -> R/C/Cr mass or thickness production 변환
5. 2025 LPJ-GUESS P-weathering 논문의 정확한 서지정보 재복구


---

## 2026-09-22 fire-spall / rock-fragment armour / postfire vegetation 추가 결론

### 1. dynamic armour
coarse fragments를 고정 cover로 두지 않는다.

```
fine-soil removal
 -> buried fragments exhumed
 -> surface armour increases
 -> rill incision / sediment yield decrease
```

Rieke-Zapp et al. 2007은 concentrated flow 아래에서 이 transient armouring을 직접 관찰했다.

### 2. armour hydrology
`armour -> infiltration 감소`를 고정 규칙으로 사용하지 않는다.

Poesen et al. 1990과 Cerdà 2001에 따르면:
- surface-resting fragments는 sealing을 억제하고 infiltration을 증가시키며 runoff를 줄일 수 있다.
- embedded fragments는 infiltration을 감소시키고 runoff를 증가시킬 수 있다.

따라서 hydrological effect는 cover뿐 아니라 fragment size, embeddedness/position, fine-earth properties, sealing, antecedent moisture 및 slope의 함수로 둔다.

### 3. fragment size classes
Li et al. 2022에서 fragment size에 따라 runoff와 soil-loss response가 크게 달랐다.
따라서 armour state에는 grain-size distribution이 필요하다.

중요:
```
fragmentation != armour loss
```

작은 fragments가 제자리에 남으면 shielding과 flow resistance가 오히려 강화될 수 있다.

### 4. fire-spall -> long-term fragmentation -> removal
- Buckman et al. 2021: wildfire-induced spalling의 sandstone 현장근거
- Pala et al. 2025: thermal spalling이 existing boulders를 작게 만들어 이후 mobilization에 필요한 shear stress를 낮춤
- Shtober-Zisu & Wittenberg 2021: 산불 10년 뒤 large spalls/flakes의 breakdown 및 pulverization 관찰
- Poesen 1987: rill flow에 의한 size-dependent rock-fragment transport

따라서 권장 구조:
```
fire
 -> spall production(size)
 -> large/coarse surface fragments
 -> postfire weathering/fragmentation
 -> smaller size classes
 -> size-specific entrainment/removal
 -> armour change
```

### 5. armour와 erosion의 상충효과
hydrology와 detachment shielding을 분리한다.

```
fragment architecture
 -> hydrological modifier
 -> infiltration / runoff / rill hydraulics

fragment architecture
 -> exposed fine-soil fraction / roughness
 -> detachment and transport resistance
```

따라서 runoff가 커져도 armour가 강하면 sediment yield가 낮을 수 있다.

### 6. soil water -> vegetation
Huang et al. 2024는 rock-fragment content가 soil-water profile을 바꾸며 plant species/root traits에 따라 response가 다름을 보였다.

고운사에서는:
```
soil depth
+ fine-earth volume
+ fragment cover/size/position
+ roots/macropores
 -> soil hydraulic state
 -> soil moisture
 -> PFT establishment/growth
```
를 새로운 coupling으로 검토한다.

### 7. oak vs kudzu
현재 문헌은 `stony/poor soil -> kudzu exclusion`을 지지하지 않는다.

- Takahashi et al. 1995: fire-disturbed Mt. Rokko에서 compacted, eroded, steep soils에도 natural kudzu stands가 발달
- Hwang et al. 2011: 한국 poorly developed mountain soil의 postfire oak sprouting
- Kim et al. 2020: oak resprouts가 pre-existing stump/root resources를 이용해 초기 경쟁우위를 가짐
- Susko et al. 1999: kudzu seed establishment는 dormancy, water stress, burial depth에 민감
- Tsugawa et al. 1990: kudzu는 prostrate stem/root network에 의한 clonal expansion이 중요

따라서 초기천이 필터:
```
environmental suitability
+ prefire rootstock legacy
+ seed propagule availability
+ clonal access
+ resprouting ability
+ light competition
```

참나무와 칡을 동일한 seed-based PFT establishment로 처리하지 않는다.

### 8. 최신 결정/모델
- `models/Rock_Fragment_Armour.md`
- `decisions/2026-09-22_FIRE_SPALL_ARMOUR_HYDROLOGY.md`

### 9. 남은 핵심 gap
1. 고운사 사암에서 burn severity -> spall mass 및 initial size distribution
2. postfire sandstone의 1-100 year fragmentation rate
3. size-class별 rill/dry-ravel entrainment 및 removal parameter
4. fragment architecture -> LPJ-GUESS soil hydraulic parameter 변환
5. oak rootstock 및 kudzu propagule/clonal state의 현장 초기화


---

## 2026-09-22 매립 석력 다량 조건에서의 모델 선택

현장 전제: 고운사 토양에는 **매립된 rock fragments가 많다**.

### 자의성 최소화 원칙
고운사에서는 다음과 같은 임의 보정식을 만들지 않는다.

```
K_eff = K_fine * arbitrary_stone_factor
soil_water = soil_water * arbitrary_armour_factor
erosion = erosion * custom_armour_factor
```

대신 각 과정에 대해 기존 published model의 원식과 상태변수를 사용하고, 모델 사이에서는 동일한 물리량과 단위를 전달한다. 모델 간 연결 자체는 새로운 coupling으로 명시하되 새로운 경험계수를 만들지 않는다.

### 1. 매립 석력의 수문: GEM / Naseri 계열
**Naseri et al. 2020 General Effective Medium (GEM)**을 high embedded-stoniness의 우선 hydraulic-property model로 둔다.

입력:
- volumetric rock-fragment fraction
- fine-earth hydraulic conductivity
- rock-fragment hydraulic conductivity
- fragment shape/orientation
- matric potential

출력:
- effective hydraulic conductivity `K(h)`

장점:
- saturated/unsaturated conductivity
- permeable/impermeable fragments
- fragment interaction
- 높은 석력함량을 직접 다루는 physically based model

soil-water retention은 Naseri et al. 2023의 volume-mixing framework를 우선 검토한다.

```
theta_mix(h)
= (1-f) theta_soil(h)
+ f theta_rock(h)
```

따라서 매립 석력의 효과를 임의의 infiltration multiplier로 만들지 않는다.

### 2. 표면/부분매립 석력과 seal: EUROSEM
EUROSEM은 다음을 이미 분리한다.
- `ROC`: 토양체적 내 rock-fragment fraction
- `PAVE`: surface non-erodible/stone cover
- `ISTONE`: surface/seal 조건에 따른 infiltration effect 방향

대표 published relations:
```
B_roc = B (1 - ROC)
DET_pav = DET (1 - PAVE)
```

Ksat의 PAVE 효과는 surface seal/structural porosity 조건에 따라 증가 또는 감소식을 선택한다.

중요:
**'embedded'라는 이유만으로 infiltration 감소를 부여하지 않는다.**
surface seal, macroporosity 및 fragment position을 함께 판정한다.

EUROSEM은 stony steep hillslope 적용 선례가 있지만 plane/channel cascade이므로 genuine 2D production engine으로는 사용하지 않는다.

### 3. 2D runoff / erosion / sediment transport: Iber+ 2024
현재 production erosion engine의 우선 구조는 **Iber+ 2024**이다.

기존 구현:
- genuine 2D shallow-water finite volume
- rainfall-driven detachment
- flow-driven detachment
- multiclass sediment
- suspended load / bed load
- loose low-cohesion sediment layer
- mass-conserving class fractions
- shielding of original soil by loose layer
- size-specific transport / hiding
- 2D Exner topographic update

따라서 새 2D erosion equation이나 custom armour erosion coefficient를 만들 필요가 없다.

### 4. 현재 권장 published-model chain
```
LPJ-GUESS
       |
       | vegetation/root/litter state
       |
       +------------------------------+
                                      |
embedded rock-fragment soil           |
hydraulic properties                  |
GEM 2020 + Naseri 2023                |
       |                              |
       | K(h), theta(h), Ksat         |
       v                              v
                Iber+ 2024
       genuine 2D runoff + erosion
       multiclass sediment + shielding
                 |
                 v
      soil depth / sediment redistribution
```

surface/seal 특수효과가 필요할 때만 EUROSEM의 ROC/PAVE/ISTONE published relation을 사용한다.

### 5. 단일모델과 모듈결합의 trade-off
현재까지 확인한 범위에서:
- **EUROSEM 하나**를 쓰면 stoniness + infiltration + erosion을 한 published model 안에서 가장 많이 해결하지만 genuine 2D와 dynamic multiclass armour 조건을 잃는다.
- **Iber+ 하나**는 genuine 2D와 multiclass erosion/loose-layer shielding을 해결하지만 high embedded-stoniness의 soil hydraulic-property physics가 부족하다.
- 따라서 기존의 모든 요구를 유지하면서 자의적 경험식을 피하려면 **GEM/Naseri -> Iber+**가 가장 방어적인 published-model chain이다.

이 연결은 하나의 기존 published model이 아니므로 새로운 coupling으로 명시한다. 그러나 연결부에서 새 fitted equation을 만들지 않고 `K(h)`, `theta(h)`, `Ksat`, sediment fractions 같은 동일 물리량을 전달하는 것을 원칙으로 한다.

### 6. 후순위
- KINEROS2: ROC/PAVE 계열과 event hydrology 강점은 있으나 genuine 2D 아님
- OpenLISEM: postfire 2D 비교에는 강하지만 stoniness는 주로 surface/splash 항이며 high embedded-stone hydraulic-property model이 아님
- Ma & Shao NDPM: embedded-stone infiltration 상세검증/민감도용
- HYDRUS 2D/3D stony-soil studies: hydraulic benchmark용

### 7. 최신 관련 파일
- `models/Stony_Soil_Hydraulics_GEM.md`
- `models/EUROSEM.md`
- `models/Rock_Fragment_Armour.md`
- `models/Iber.md`
- `decisions/2026-09-22_STONY_SOIL_MODEL_SELECTION.md`

### 8. 남은 검증
1. Iber+ loose-layer/original-soil class에 fire-spall coarse classes를 넣을 수 있는 원 구현 범위 재검증
2. GEM effective hydraulic properties를 Iber+ infiltration parameter에 전달할 때 사용할 published transformation 확인
3. 고운사 sandstone fragment 자체의 `K(h)`, `theta(h)` 또는 실측
4. fire severity -> spall mass/initial size distribution의 published quantitative model


---

## 2026-09-22 dynamic armour 최종 모델 선택 보완

### 핵심 계보 발견
고운사에서 필요한 dynamic armour와 embedded rock-fragment profile을 이미 구현한 published model lineage가 확인되었다.

```
ARMOUR
 -> mARM
 -> mARM3D / mARM5D
 -> SSSPAM
```

이 계보가 기존 모델로 처리하는 과정:
- selective fine removal
- surface coarsening
- armour formation
- particle-size-specific entrainment
- parent-to-daughter weathering
- multilayer embedded PSD
- subsurface resupply
- soil-depth update
- DEM evolution

따라서 고운사에서 custom armour coefficient를 새로 만들 필요가 없다.

### event hydro-erosion과 long-term armour의 역할분담
현재 우선 구조:

```
OpenLISEM + SWATRE
 -> actual event erosion/deposition mass
 -> SSSPAM/mARM state updater
 -> surface PSD / embedded PSD / armour / soil depth / DEM
```

OpenLISEM+SWATRE:
- measured/effective theta-h-K direct input
- Richards-equation soil water
- 2D SWOF surface flow
- splash / flow detachment
- erosion/deposition

SSSPAM/mARM:
- dynamic armour
- embedded PSD
- weathering/fragmentation
- profile resupply
- long-term soil-depth/DEM evolution

### OpenLISEM 소스 검증에서 확인된 한계
- StoneFraction은 static input
- material-depth evolution switch는 현재 비활성
- dynamic armour가 production code에서 완결되지 않음
- 일부 multiclass sediment UI/initialization은 비활성/주석 상태
- root effect는 extra cohesion input
- litter effect는 interception/splash protection 중심

따라서 OpenLISEM 단독으로 100년 armour/profile feedback을 완결한다고 주장하지 않는다.

### SSSPAM 자체 침식식은 쓰지 않는 이유
SSSPAM의 fluvial erosion parameterisation은 site/laboratory calibration을 필요로 하므로 고운사에 그대로 이식하면 자의성이 남는다.

따라서 SSSPAM에서는:
- grading transition
- armour
- weathering
- profile resupply
- mass balance
- soil-depth/DEM update
를 사용하고,
actual event erosion/deposition mass는 OpenLISEM에서 받는다.

### 핵심 결정
현재 최우선 구조:
**OpenLISEM+SWATRE for event hydro-erosion + SSSPAM/mARM for long-term armour/profile evolution**

관련:
- `models/ARMOUR_mARM_SSSPAM.md`
- `decisions/2026-09-22_DYNAMIC_ARMOUR_MODEL_SELECTION.md`


---

## 2026-09-22 Iber+ ↔ SSSPAM exact mass interface 및 event-engine 변경

### 1. event erosion engine
Primary event erosion engine을 **Iber+ 2024**로 변경한다.

이유:
- genuine 2D SWE
- particle-class-specific suspended/bed load
- original-soil detachment와 loose-layer redetachment 분리
- class별 deposition
- loose-layer mass `M_s,k`의 active mass conservation
- dynamic loose-layer grading
- shielding
- Exner topographic update

OpenLISEM은 SWATRE hydrology benchmark/postfire comparison으로 유지한다.

### 2. Iber+ persistent states
Original soil:
```
g_k
D_rdd,k
D_fdd,k
```

Loose surface layer:
```
M_s,k [kg m^-2]
f_k = M_s,k/M_s
D_rdrd,k
D_fdrd,k
D_dep,k
```

### 3. long-term profile handoff
embedded soil profile에서 실제로 제거해야 하는 class-k mass:

```
E_orig,i,k
=
A_i ∫(D_rdd,i,k + D_fdd,i,k) dt
```

반면:
```
E_redet,i,k
=
A_i ∫(D_rdrd,i,k + D_fdrd,i,k) dt
```
는 이미 loose layer에 있던 material의 재이동이므로 deep profile에서 다시 제거하지 않는다.

### 4. event-end state
다음 상태를 그대로 보존한다.

```
M_s,k(end)
f_k(end)
z_b(end)
```

Iber+ relation:
```
l_d,k = M_s,k / (rho_s phi)
```

따라서 loose-layer mass-to-thickness에 custom equation을 만들지 않는다.

### 5. SSSPAM/mARM 역할
사용:
- depth-resolved embedded PSD
- vertical profile resupply
- weathering transition
- inter-event profile restructuring

사용하지 않음:
- SSSPAM 자체 calibrated fluvial erosion equation
- Iber+ event result 위에 SSSPAM erosion/deposition을 다시 계산하는 것

### 6. double counting 금지
- redetachment를 deep profile erosion으로 재계산 금지
- Iber+ Exner elevation change와 SSSPAM event elevation change 중복 금지
- Iber+ class-selective deposition 뒤 SSSPAM deposition sorting 재적용 금지
- Iber shielding 외 별도 custom armour factor 동시 적용 금지

### 7. surface-layer mismatch
Iber+ variable-thickness loose layer와 SSSPAM armour/profile layer는 동일한 정의가 아니다.

따라서:
- surface authoritative state = Iber+ `M_s,k`
- deeper authoritative profile = SSSPAM/mARM
- surface/deep exchange는 mass conservation과 기존 SSSPAM vertical-resupply rule만 사용
- fitted exchange coefficient 금지

### 8. Hairsine-Rose 계보
Iber+의 original-soil / deposited-layer 구조는:
- Hairsine & Rose 1991 rainfall detachment/deposition
- Hairsine & Rose 1992 sheet flow
- Hairsine & Rose 1992 rill flow
계보에 기반한다.

이 계보는 original cohesive soil과 deposited noncohesive layer를 분리하고, deposited layer가 original soil을 shield하는 구조를 이미 갖는다.

### 9. 자의성 없는 parameter policy
다음 값은 output fitting으로 정하지 않는다.

Iber hydrology:
- Ksat
- porosity
- initial saturation
- soil depth
- wetting-front suction

Iber erosion:
- original-soil PSD `g_k`
- initial loose-layer mass `M_s,k`
- critical shield mass `M_s,cr`
- rainfall detachability
- flow detachability `K_d,k`
- critical shear stress `tau_s`

우선순위:
1. 현장 직접 측정
2. 독립 rainfall/flume detachment experiment
3. published physically based transformation
4. 직접 측정 불가능 시 literature-constrained uncertainty range

**soil-loss 결과에 맞춘 자유 calibration은 production parameter source로 사용하지 않는다.**

### 10. 현재 production architecture
```
LPJ-GUESS
    |
    v
measured / independently constrained soil state
    |
    v
Iber+ 2024
2D runoff
multiclass detachment / redetachment
deposition / transport
dynamic loose-layer mass
event topography
    |
    | E_orig,k ; M_s,k(end) ; z_b(end)
    v
SSSPAM / mARM
embedded multilayer PSD
vertical resupply
weathering
inter-event profile evolution
    |
    v
next-event g_k / soil depth / profile state
```

관련 결정:
- `decisions/2026-09-22_IBER_SSSPAM_EVENT_PROFILE_INTERFACE.md`


---

## 2026-09-22 LiDAR vegetation-engine reassessment

사용자가 vegetation-geomorph coupling에 30 m보다 세밀한 LiDAR 지형을 사용할 수 있음을 명확히 하여 식생모델 기준을 수정했다.

### revised criterion
- LiDAR individual-tree/crown initialization
- 1-10 m 이하 공간상태와의 결합성
- 100-year succession
- seed production/dispersal/regeneration
- quantitative fine-root and litter state
- hourly/daily ecohydrology where possible
- postfire recovery
- modifiable implementation

### current provisional primary engine
**HETEROFOR + spatial helper models**

HETEROFOR current documentation confirms:
- adult tree x,y,z and crown geometry initialization
- configurable cell size for radiation/regeneration/ground vegetation
- hourly meteorology and water balance
- optional tree-level water balance
- fine-root allocation, vertical root proportion and turnover
- structural roots
- annual litter cohorts / soil-carbon dynamics
- seed-bank regeneration
- 2022 Capsis seed approach with global/local seed dispersion and seed rain
- temperate mixed-forest calibration and century-scale application

### root spatialization
**ChaMRoots (Mao et al. 2015)** is now the preferred helper from LiDAR/HETEROFOR trees to 3-D root-density fields.

```
tree x,y, DBH, species
 -> ChaMRoots
 -> RID by horizontal position, diameter class and depth
```

For shallow landslides:
```
spatial root distribution
 -> Schwarz spatial Root Bundle Model
 -> root reinforcement field
```

Do not use this landslide reinforcement as water-erosion resistance.

### litter spatialization
Use HETEROFOR tree litterfall plus LiDAR crown footprints and the Sánchez-López et al. 2023 spatial litter approach to create 1-5 m surface-litter maps.

### main HETEROFOR gaps
1. no documented native wildfire/fire-spread module in HETEROFOR 1.2
2. early postfire herb/shrub **root biomass and turnover** are not yet established as strong HETEROFOR states
3. intended stand scale is roughly 0.5-5 ha; larger-domain performance and inter-stand coupling need testing
4. Korean species/PFT parameterization required

### secondary candidates
1. **SEIB-DGVM**: retains major advantage if endogenous repeated wildfire is required; native wildfire/SPITFIRE lineage, grasses, roots and litter.
2. **SORTIE-ND 7.06**: excellent spatial tree/recruitment/substrate framework and postfire applications, but no standard dynamic root-biomass/root-water-uptake state.
3. LANDIS-II + NECN: landscape fallback, but coarse coupling relative to LiDAR/event geomorph.
4. iLand: 1-ha resource-unit ecohydrology is a scale mismatch.
5. LPJ-GM: solves migration but published local vegetation resolution is too coarse for this LiDAR objective.
6. standard LPJ-GUESS: retains good physiology but not preferred as spatial engine.

### current Gounsa-specific order
For an observed initial wildfire with fine-scale LiDAR and quantitative root/litter geomorphic coupling:

1. HETEROFOR + ChaMRoots + spatial litter helper
2. SEIB-DGVM
3. SORTIE-ND + root helper
4. LANDIS-II + NECN
5. iLand
6. LPJ-GM
7. standard LPJ-GUESS

This is not a generic ranking of forest models.

Latest decision:
- `decisions/2026-09-22_LIDAR_VEGETATION_ENGINE_SELECTION.md`


---

# 2026-10-25 신규 확인: 수관 강우 분배 → 침투/유출 → 침식의 연쇄

**신규 판정 문서:** [수관-수간유하-유출-침식 문헌 점검](decisions/2026-10-25_CANOPY_STEMFLOW_RUNOFF_EROSION_RESEARCH.md)

- **세 강우성분을 모두 계산하는 모형은 이미 존재**: EUROSEM(Morgan et al. 1998)은 직접 통과우/잎 배수/수간유하와 차단저류를 계산하여 infiltration, runoff, rainfall detachment, flow detachment와 연결함. Apip et al. (2008)도 같은 연쇄를 계승. 단, 두 연구는 SF를 유효강우로 합산하여 나무별 국지 집중의 효과가 지표 격자에서 유지되지 않으며 genuine 2D 지표유동을 구성하지 않음.
- **국지 SF → runoff 검증 선례**: Charlier et al. (2009)은 수간유하 집중 구획을 따로 두어 18개 사건 수문곡선을 검증. 단, 침식 및 자유로운 2D 없음.
- **식생 생태수문**: de Wergifosse et al. (2020)의 HETEROFOR는 canopy storage/throughfall/stemflow와 층별 토양수분 1시간 계산을 제공하지만 **지표유출을 구현하지 않음**.
- **산불 후 2D 침식**: McGuire et al. (2016)은 Rutter 기반 차단, Green-Ampt 침투, 2D shallow-water, rainfall/flow detachment 및 size-selective sediment transport를 결합했지만 **줄기별 SF 집중과 수관적하 운동에너지는 별도 구현이 확인되지 않음**. 원 연구의 산불 직후 실제 사상에서는 수관이 전소하여 interception 자체를 끄고 검증함.
- **반대 경로 중요**: Liang et al. (2009), Beven & Van Stan (2026), Di Prima et al. (2026)은 줄기 기부의 preferential infiltration을 강조. Chen et al. (2026)은 줄기열 내부 SF 공급은 크지만 inter-row 침식이 더 큰 관측을 보고. SF 증가를 항상 유출과 침식 증가로 환산하는 것은 부당함.
- **강우박리 에너지**: Li & Tian (2026)은 자유통과/튀김/적하 빗방울의 KE를 구분. 자유 TF와 적하 TF를 합산한 체적 하나만으로 rainfall detachment를 정하지 말 것.
- **미해결 결합**: 나무/초본 패치별 시간별 물수지와 위치별 TF·SF·drip KE를 2D 침투-유출-침식 엔진에 질량보존으로 전달. 이는 **새로운 coupling**이며 출판된 단일 모형 기능이라고 표기하지 않음. LPJ-GUESS 뿌리량과 침식저항의 별도 결합 문제는 종전대로 유지.


---

# 2026-10-26 실제 원본 실행 침식량 물리적 타당성 점검

최신 판정: [강우 10~50 mm/h 침식량 유효성 감사](decisions/2026-10-26_RAINFALL_EROSION_PHYSICAL_VALIDITY_AUDIT.md)

- **SWEHR 공개코드 3×51 원본 예제**: 0.25m 격자, 초기 Ks=0, a=ad=0, F=0.004. 강우 10~50 mm/h 1시간 재실행에서 격자 높이 감소 총 약 0.0191 m³ vs 높이 증가 약 0.549~0.553 m³; 10~50 강우에 사실상 같은 최대 약 100.61mm 국지 고도 감소. 지형 전처리, 초기조건, 경계유사수지 검증 불가로 **모두 결과 기각**, McGuire et al. 2016 원 논문 자체의 모델 검증 결과와 구별.
- **EUROSEM 원본 2-element test**: 10mm/h gross erosion 0, 20mm/h gross 383.9kg / net 각 1.511kg, global water balance -0.0299%; 30mm/h gross 53,224.3kg / net 합 52,987.3kg, water balance 12.8593%; 40mm/h first element만 15,305kg, water error 28.8924%; 50mm/h segfault. Gross detachment vs delivered sediment **구분 필수**. 30, 40 모두 기각, 20도 반복성 문제. 시험 경사 S=0.85, 피복 COVER=0.15는 고운사 입력값이 아님.
- **실측 비교**: Johansen et al. 2001(60mm/h burned 76kg ha^-1 per mm rainfall), Samoil et al. 2026(185mm/h 30min unburned 0.0178 / moderate burn 1.05 / high burn 5.29t/ha), Kinner & Moody 2008(20/35/50mm/h infiltration response), 한국 Shin et al. 2024(RUSLE 0.07–94.9 / SEMMA 0.24–83.6t/ha/storm **모형 예측**). 극심한 침식은 실제 가능하지만 어느 숫자도 고운사 허용범위 상한이 아님.
- **기존 HETEROFOR, Charlier, Rutter/Gash**는 interception / SF / runoff 중 일부를 산출하지만 독립적으로 erosion mass를 직접 생성하지 않음. **WEPP/OpenLISEM/Apip**은 erosion 가능한 기성 구조지만 10~50 실험은 이번에 수행하지 않음.
- **현재 결론**: 검증된 고운사 t/ha/event 숫자는 아직 없음. 본문에 임의 곡선을 넣지 않는다. source archive는 다음 수행에서 물수지, 유사수지 및 단위를 확인하는 토대로만 사용.


---

## 2026-10-26 원본 수문-침식 모형 보존시험: 검증된 결과와 한계

- [실제 원본 SWEHR 및 EUROSEM 재검증](decisions/2026-10-26_SWEHR_EUROSEM_SOURCE_CLOSURE_VERIFICATION.md). **SWEHR는 원본 예제의 강제 외부 물/토사 유입 제거, 초기 U[1]/M/SOLID/TOTM 정의 후 9/9 물수지 및 원토양-퇴적층-부유사-경계유사량 독립 수지 검증 통과**. 10~50mm/h×1h에서 단위면적당 경계유실량은 시험조건 0.0000024~0.0694 t/ha/event. **고운사 현장 예측값 아님**.
- **EUROSEM**은 불연결 2사면 및 누적우량 자료의 세 지점 수 불일치 해소 후 10~50mm/h 수문 물수지 5/5 통과(잔차 -0.0333~+0.0088%), 하지만 유사수지 독립 검증은 아직 없음. 모델이 출력한 수만~수십만kg 규모의 총박리량 및 순침식량을 고운사 연구값으로 사용 금지.
- 기존 2026-09-22 잠정 Iber+ / SSSPAM/mARM 생산 구조는 유지하며 SWEHR/EUROSEM은 실행환경 및 방정식 검증 기준으로만 사용. 고운사의 수간유하 집중 위치와 수관적하 에너지, 뿌리 우선침투에 의한 2D 침식 효과는 새 결합 및 현장 매개변수 검증이 아직 필요.
- 코드 및 raw output: [swehr-water-sediment-closure-20261026 실험 브랜치](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/swehr-water-sediment-closure-20261026/experiments/rainfall_10_50).


---

## 2026-10-26 참나무 맹아형과 억새형 원본 SWEHR/EUROSEM 전과정 민감도 결과

최신 결정: [식생구조, 침투, 유출 및 침식 원본모형 조건부 민감도 110개 실행](decisions/2026-10-26_OAK_MISCANTHUS_NATIVE_MODEL_SENSITIVITY.md).

- SWEHR 원본 방정식 유지, 가상 수관 유효강우와 다양한 원본 침투/유수박리 매개변수로 50개 실행. **50/50 물수지 및 독립 유사수지 통과**. 그러나 줄기별 SF 집중, leaf-drip KE 미구현이므로 실제 억새 대 참나무 맹아 침식 우열 주장 불가.
- EUROSEM 원본 INTERC의 수관저류, 직접 TF, leaf drip, SF를 실제 기록하며 60개 실행. **59/60 물수지 통과, 1개 SPLTEX 1 실패, 독립 유사수지 미검증**. 같은 토양조건 30 mm/h 참나무형 runoff 3.708mm, 억새형 3.491mm; 식생 구조에 따른 차이가 존재하지만 SF 위치별 공급이 합산되므로 stemflow 공간 집중이 침식에 미치는 효과는 이 모형에서 직접 검증 불가.
- 30 mm/h에서 SWEHR canopy-only export 참나무형 0.004025, 억새형 0.003784 t/ha; 가상 Ks/roughness/erodibility를 바꾸면 경향이 반전되거나 값 차가 커짐. 현장자료 없이 species ranking은 식별 불가능.
- EUROSEM 30 mm/h 원본 출력 net erosion 26~29t/ha(수관형) 수준은 독립적인 sediment closure 없는 **미검증 숫자**이며 논문의 토양유실량으로 직접 사용 금지. 범위는 고운사 사이트가 아닌 원본 사면 테스트 조건에 한정.
- 생산모형 선택 **Iber+ 중심 event erosion + SSSPAM/mARM**을 SWEHR로 바꾸는 결정이 아님. 필요한 새 결합은 공간보존적 stemflow/leaf drip forcing, 토양수분과 root macropore, 수관 및 뿌리 상태 각각이다.

산출물: [네이티브 민감도 종합 Actions](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40258842917), [소스 스크립트](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/swehr-water-sediment-closure-20261026/experiments/rainfall_10_50).


## 2026-10-26 종별 생태 특성과 PLANTH 단위 오류 정정

[식생 특성 재검증](decisions/2026-10-26_OAK_MISCANTHUS_REAUDIT.md): 참나무 맹아의 줄기와 기존 뿌리, 억새의 포기별 지하경 및 가는뿌리 차이, 생육기와 비생육기의 차이를 원문으로 재검토함. 이전 EUROSEM에 2.5m라고 입력한 PLANTH=2.5는 원래 **2.5cm**였으며 원본 input routine은 /100으로 내부 m 변환. 구 수치 중 적하 운동에너지 관련 해석 오류를 폐기함. 6개 계절별 가상 구조×강우 5강도×두 엔진을 다시 실행함. EUROSEM은 TF/drip/SF 분리하지만 SF 국지침투 공간 집중 미구현, SWEHR는 canopy interception으로 차감한 유효강우를 균일하게 공급함. 두 식생 침식 억제 우열을 현장 수치 없이 주장 금지. 수정 실행: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40261338013


## 2026-10-26 밀생 억새와 산발적인 참나무 맹아 비교의 공간구조 오류 정정

[핵심 결정: 실제 배치가 다른 두 식생을 평균피복과 균일 유효강우로 동일 취급하지 않는다](decisions/2026-10-26_DENSE_MISCANTHUS_SPARSE_OAK_SPATIAL_COMPARISON.md). 진짜 고운사 식생 대조는 밀생 Miscanthus tussock/roots/litter와 떨어진 Quercus oak stump/sprouts 사이의 **노출토양 연결성 및 runon/runaround/유사수송 경로**이다. 기존 110회+60회 native SWEHR/EUROSEM 균일사면 실험은 이 핵심 공간변수가 없었으므로 실제 두 식생의 침식량 유사성 또는 우열을 입증하지 않는다. Mayor et al. 2008 WRR DOI 10.1029/2007WR006367의 6 plot/3 catchment Flowlength 검증, Crompton et al. 2023 GRL DOI 10.1029/2022GL101801의 2D Saint-Venant runon/runaround 역학이 신규 직접근거. 비교는 UAV/TLS 기반 2D 지형과 포기/그루터기별 뿌리/낙엽/토양수리/암편 및 SF 위치를 모형입력으로 구성해야 하며 관련 통계는 10–50 mm/h 1시간마다 물수지와 유사수지를 통과해야 한다. Iber+ 주연산 모형 선택은 그대로 유지.


## 2026-10-26 고운사 밀생 억새와 산발 참나무 맹아 2D 공간형 SWEHR 38회 실험

[원본 source 기반 가상사면 물수지 및 독립 유사수지 검증](decisions/2026-10-26_SPATIAL_NATIVE_SWEHR_DENSE_MISCANTHUS_SPARSE_OAK_38RUNS.md). GitHub에서 실제 고운사 DTM/식생 분포 원자료가 확인되지 않아, 13×25 cell, dx=0.5m, 81.25m² **가상** 경사에 밀생 억새(94.77%), 산발 참나무(9.23%), 정확히 동일 면적 40%의 횡방향 식생대 및 고립 식생패치를 분리해 10~50mm/h×1h 20회 모의. 공간적 SF 재분배 10회 및 원래 수관/수리/박리 과정별 추가 8회로 총 38회 실행. **38/38 물수지와 원토양-퇴적층-부유토사-경계 유사수지 통과**. 최대 물수지 상대오차 4.15e-11, 원토양 독립 유사수지 최대 1.16e-13. 30mm/h 산발 참나무 예시 유출 21.661mm, 유사 배출 0.002291t/ha; 밀생 억새 예시 유출 10.087mm, 유사 배출 0.000543t/ha. 동일 40% 피복 50mm/h 고립 패치가 횡방향 연결형보다 유사 배출 1.410배. **이는 식생 공간배치에 따른 가능성 검증이지 고운사 실제 종별 침식량 계량 예측이 아님**. 노출/식생 격자의 Ks, 거칠기, 박리 저항과 차단저류 및 SF 분율은 가상 설정; 루트 RLD 및 litter, 암편, 수관적하 KE는 미연동. 이전의 단일 평균 COVER 비교를 현장 근거로 재사용 금지. Iber+ 본 생산 선택 유지.

실험 원본 및 영구 결과 [공간형 SWEHR branch](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/spatial-vegetation-runoff-erosion-20261026/experiments/rainfall_10_50/spatial_patch_experiments/verified_20261026), [38-run Actions](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40264757325).


## 2026-10-26 EUROSEM vs SWEHR vs Iber+

[세 모형 원본/소스/API 검증](decisions/2026-10-26_EUROSEM_SWEHR_IBERPLUS_COMPARISON.md): EUROSEM(1998)은 canopy interception/direct throughfall/leaf-drip KE/stemflow 및 ROC/PAVE/ISTONE에 강하지만 kinematic wave connected slope planes이며 DT+LD+SF가 NR로 다시 합쳐짐. SWEHR(2016)은 postfire steep hillslope TLS, 2D SWE Green-Ampt Hairsine-Rose 입경별 original/deposited detachment/redeposit에 강하고 소스 C 코드 개조 가능; 원문 Rutter canopy와 실제 공개 C 구현은 동일시 금지. Iber+(2024)는 2D SWE GPU, class-specific suspended+bedload, rainfall/flow detachment, loose-layer Ms,k, Exner, Alps headwater 20km² 사례(해당 시뮬레이션은 rainfall-driven only)에 강하여 prior Iber+ event erosion first choice 유지. 다만 개별 줄기 SF 위치, 분리된 leaf-drip KE와 root/litter RLD 및 rock spall/weathering에는 어느 원본모형도 완결되어 있지 않으며 독립 공간적 coupling이 필요. SWEHR spatial native 38/38 budget pass; EUROSEM 59/60 water budget and no independently checked sediment closure; Iber+ **현장대조 코드 실측 재현 실행 전무**, 공개 Iber+ V3.2b Windows+Linux original reproducibility binaries 존재. 서로 다른 시험환경의 침식량을 3-way model numerical verification이라고 부르지 말 것. 2D rainfall impact source와 stemflow water-only source 분리 필수.


## 2026-10-26 SWEHR 수관차단과 강우충격 저감 원문/소스 정밀 확인

[원본 논문 vs 실제 C 코드 검증](decisions/2026-10-26_SWEHR_RUTTER_CANOPY_SHIELDING_SOURCE_AUDIT.md), [model 기록](models/SWEHR.md), [McGuire 원논문 추가 해설](papers/2016_McGuire_SWEHR_Postwildfire_2D.md): **McGuire et al. (2016)은 Rutter 수관차단 §3.5 식24–26과 강우박리/재박리에 곱하는 별도 canopy splash shielding `(1−Cv)+TcCv` §3.2 식3–4를 각각 구현했지만, CSDMS 공개 단일 `SWEHR.c`에는 어느 과정도 그대로 구현되어 있지 않다.** 코드에서는 직접 원시 강우 `R=RAIN[rind]`를 지표수 `U[1]+=dtR`와 강우박리 `E1,E2∝R`에 사용한다. 소스에 기존 보호항으로는 표면 퇴적층 H, 수심의 빗방울충격 감쇠 및 Manning 수심마찰만 확인된다; `SF`는 수간유하우 아닌 friction slope. 원 논문 단기 실측 사건에서는 수관 연소로 interception을 의도적으로 제외, 식생회복 가상사면에서는 Cv0.05–0.95와 Tc0.35 등으로 민감도 분석. 원래 Rutter 1975에는 별도 stemflow 저류모형이 있지만 2016 논문의 간략형과 공개 C에는 독립 줄기기부 SF 공급이 없음. 기존 고운사 spatial 38-run branch `QA_WFACTOR`/`QA_DFACTOR`는 신규 정적 저류/강우충격 분리 입력이며 **Rutter의 동적 C(t), 배수 D(t), 계절별 수관저류 및 실제 leaf-drip KE는 미구현**. 특히 논문은 E=0 가정하므로 1시간 차단저류를 영구 수문 손실로 취급하지 않고 종료 후 배수와 수관 저장을 물수지에 계상해야 한다. 우선 원본 논문 두 분리항 복구한 후 10–50mm/h 수지 재검증. 공간 식생 피복을 뿌리와 동일시하지 말 것.


## 2026-10-26 최종 정정: 공식 SWEHR 1.0 원본 코드 별도 보존

[원본 코드 및 원논문 차이 검증](decisions/2026-10-26_OFFICIAL_SWEHR_V1_0_ORIGINAL_CODE_PROVENANCE.md): 저자 등록 CSDMS SWEHR V1.0 (2017-07 최초 커밋 4e6f783f3...) 7개 원본 파일을 `main/third_party/SWEHR_original_v1_0_2017/`에 바이트 **7/7 동일**하게 보존. 수정하지 않은 원본 C/입력 예제 GCC 컴파일 및 실행 success (GitHub Actions 40272368386). 그러나 2016 논문 원식 `Rutter C(t),D(t)` + `(1-Cv)+TcCv` canopy direct-rain shield는 공식 C 버전에 없음. 연구에 꼭 필요한 것은 **저자가 실제 논문 실험에 사용한 수관 모듈 포함 원 구현 버전**으로, 현재 공개자료에서 확보되지 않았음. 기존 38회 공간민감도 및 110/60회 가상 식생 모의는 원본 vegetation physics 재현이 아닌 modified fork 민감도임을 명시하고, 고운사 억새/참나무의 차이가 4.2배라는 결론 등 이전 정량연구 주장을 철회. 기존 모든 가상 실행을 원본 프로그램 실행 결과처럼 취급하지 않는다. [원본 7파일](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/main/third_party/SWEHR_original_v1_0_2017), [원본 무수정 컴파일 실행](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40272368386).


## 2026-10-26 SWEHR 연구결과 신뢰성 전수감사 및 공식 정정

[종합 정정 보고서](decisions/2026-10-26_SWEHR_REPRODUCIBILITY_REMEDIATION.md) 및 [결과 상태 CSV](decisions/2026-10-26_SWEHR_EVIDENCE_STATUS_MATRIX.csv): 2016년 논문에 기술한 Rutter 수관저류 §3.5와 독립 수관 강우충격 차폐 §3.2는 공식 SWEHR V1.0의 C 소스에 없음. 2017 V1.0은 바이트 동일 7/7로 보존하고 기본 예제 무수정 컴파일/실행 확인함. 본 연구가 실행한 38회 SWEHR synthetic mask 공간 실험과 기타 억새/참나무 식생 사례는 **2016 SWEHR original published vegetation model reproduction이 아니며, 4.2배 수치는 실제 종별 효과로 사용하면 안 된다**. 논문 데이터는 교신저자 요청을 통해 입수한다는 2016년 원문 안내를 확인했고, Luke A. McGuire 논문 게재 연락처 `lmcguire@email.arizona.edu`를 정정 보고서에 명시함. 원논문의 해당 코드 버전과 Figure 9/10 입력자료를 확보해 최초 상태 그대로 재현하는 것이 이전 실험 복원보다 우선임. 저자 문의는 발송하지 않은 초안이며 응답이나 코드 확보를 주장하지 않음.


## 2026-10-26 공개 원본 전체 소스 기반 후속 침식모형 재선정

[완전 공개 소스 감사](decisions/2026-10-26_FULL_OPEN_SOURCE_NATIVE_2D_VEGETATION_EROSION_MODELS.md) 및 [SHETRAN 계보](models/SHETRAN.md), [수정된 openLISEM 계보](models/OpenLISEM.md): SWEHR 공식 V1.0에서 누락된 수관차단/수관적하 충격을 실제 소스에 구현한 두 후보기술 확인. **SHETRAN** `nclwater/Shetran` GNU GPLv3 current version CMake 4.7.2.0 실제 `ETmod.f90` dynamic `CSTORE,CSTCAP,CK,CB,DRAIN,DRAINA`, `SYmod.f90` `SYWAT` 직접강우/적하 분리, `SYOVER` 빗방울+잎적하 momentum, 지표 초본 및 표면 암편 저감, flow detachment, 퇴적층의 원토양 보호, 유사 입경 7종, 2D 4방향 유동 및 완전한 `Cobres` SYD 유사 입력 예제 확보. 현재 공식 코드의 **`BALSED`가 빈 함수**이고 미세 rill 자동 발달은 Wicks & Bathurst 1996 원문에 `without rilling` 명시. Windows ifx/VS2026, Linux gfortran 및 CMake, 세 dependency tarball이 코드에 제공되지만 **현재 직접 컴파일/모델 실행/수지검증하지 않음**. **openLISEM** original GPLv3 `vjetten/openlisem` `hydro/lisInterception.cpp` actual canopy/litter, `erosion/lisErosionSplash.cpp` direct rain/leafdrip kinetic energy, stone/grass suppression, `lisSWOF2DSediment.cpp` actual dynamic 2D SWOF sediment transport source confirmed. 이전 Linux Qt6/QWT build blocked, fixed라고 주장하지 말 것. DHSVM 공식 source는 canopy 있으나 별도 Doten 2006 sediment extension 미확인, GEOtopSed github archive에는 sediment routines not found. **기능만 설명된 논문 또는 공개되지 않은 2016 SWEHR 식생 코드를 원래 있다고 하지 않음**. 1차 새 원본 실행 우선순위 SHETRAN의 Cobres 유사 시뮬레이션, 다음 openLISEM Windows native 기능 및 version/build identity 감사. 두 모델 모두 실제 현장 root biomass→erosion link, 개별목 SF, fire-spall rock weathering and explicit evolving rills에는 한계.


## 2026-10-26 SHETRAN 4.7.2 원본 Fortran 구현의 실제 호출경로 감사

[원본 source, 호출순서, 수식, 누락 기능 정밀 기록](decisions/2026-10-26_SHETRAN_472_NATIVE_IMPLEMENTATION_CALLGRAPH_AUDIT.md): 코드 2026 최신 버전 commit cf9cd540. 실제 원본에서 `run_sim: ETSIM→VSSIM→OCSIM→SYMAIN`; `SYMAIN: SYWAT→SYOVER→SYCOLM/SYLINK→SYBED`. `ETmod` 는 time-varying CSTORE,CSTCAP,CK,CB,DRAIN,PNETTO,DRAINA, `SYWAT` 는 FCC,LRAIN,DRDROP, QOC and tau, `SYOVER` 는 직접 빗방울 운동량 GMR 및 수관 적하운동량 GMD separately. 강우박리 DR은 `(1-FCG-FCROCK)`, 유수박리 DF는 `(1-FCROCK)`에 비례하므로 지표 초본 FCG는 유수박리를 직접 감소시키지 않음. DLS>=DLSMAX에서 모든 원토양 새 박리가 stepwise 0. SHETRAN 수문은 2D 4면 연결이지만 `OCmod2/OCQGRD`는 Manning-Strickler head-gradient `Q=C√(|Δz|/L)` 형태 **확산파 근사**로, 2D 완전 천수방정식 동압력/관성 해법 아님. `SYMAIN` `ZGRUND INTENT(IN)`이므로 사면 고도 업데이트, rill incision 없음. `RDF`는 수분흡수만, sediment inputs GKF/GKR keyed soil class not vegetation root RLD; 개별 수간유하우 미구현; 암편 FCROCK은 피복값이지 시간변화 풍화/파쇄 아님. 유사수지 `BALSED`는 empty stub; 원본 실제 실행/수치 검증 아직 없음. 고운사 시나리오 결과라고 주장하지 말 것.


## 2026-10-26 SHETRAN 강우사상별 DEM 갱신 입출력 완전 추적

[원본 SHETRAN HDF5, FR39, SY51–SY53 및 hotstart 제약 검증](decisions/2026-10-26_SHETRAN_INTEREVENT_DEM_UPDATE_NATIVE_OUTPUT_AUDIT.md): 본 연구는 **원본 내부에 사상별 지형갱신이 없음**을 모델 탈락사유로 삼지 않는다. original `s_v_er=GNU×86400000`[mm/day] (원토양 강우/유수 박리), `s_t_dp=DLS×1000`[mm] (표면 퇴적층 두께), `s_dis`[kg/s]가 공식 V4 HDF5에서 확인됨. `SYCOLM`은 입경별 수송, 재퇴적, DLS와 FDEL 업데이트 원형 포함. `FRmod.f90`의 과거 출력 id44는 `GNUCUM − (DLS−DLSSRT)×1000`[mm] 원형 순유실량을 계산하지만 **PREVTM과 GNUCUM 초기화 보장 없음**으로 원 출력 수치 신뢰 금지. 다음 강우의 DEM은 외부 `z[n+1]=z[n]−∫GNUdt+(DLS_end−DLS_start)`로 갱신 가능하며, 원본 terrain FR37–FR39 `ZGRUND` 입력, 유사 초기상태 SY51 DLS, SY52 FBETA, SY53 FDEL이 존재. **원본 hotstart에 FBETA/FDEL/DLS 부재**, 따라서 단순 DEM 편집으로 보존적인 완전 다사상 재시작이 된다고 주장 금지. FR39 native `10G7.0` 고정 7글자 입력은 mm 이하 갱신값 손실 위험. 원본은 바꾸지 않고 **독립 event-to-event postprocessor** `experiments/shetran_original_event_bridge.py` 및 4개 unit test를 실제 구현, GitHub Actions 통과: [CI](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40280065364). Sampled GNU 적분이므로 정확한 sediment substep-integrated native ledger를 재현한 것은 아님. 출력은 new FRD, next DEM/depth/DLS와 `restart_ready=false` 오류진단. 아직 unmodified native SHETRAN Cobres 실행 또는 실제 출력 기반 사상 연결 검증은 없음.


## 2026-10-26 SHETRAN 강우사상별 DEM 갱신 검토
- 원본 Fortran 및 공식 출력 검증: 침식 `GNU`와 표층 퇴적 `DLS`를 구분, 다음 사상 DEM에 `delta z = -sum(GNU * dt) + DLS_end-DLS_start`를 외부 신규 결합으로 전달하는 구조는 조건부 가능.
- 원본 `FRRESP` 출력 44번에 초기화/기준시각 문제가 있으므로 단독 지형갱신량으로 사용 금지. `SY51/52/53` 초기 `DLS/FBETA/FDEL`과 수문 hotstart 정합성 및 미구현 `BALSED` 외부 감사 필요.
- 상세 근거: `decisions/2026-10-26_SHETRAN_EVENT_BOUNDARY_DEM_STATE_AUDIT.md` 및 `models/SHETRAN.md`. 원본 예제 실행과 수지 검증 아직 미실시.


### 2026-10-26 SHETRAN 전체 실행경로 감사 추가
[SHETRAN 4.7.2 원본 전체 호출경로 감사](decisions/2026-10-26_SHETRAN_472_FULL_PATH_SOURCE_AUDIT.md)를 최신 상세 근거로 우선한다. 검토한 공식 Fortran: FRINIT/INFR/VSIN/ETIN/TMSTEP/OCQDQ/SYMAIN/SYCOLM/SYBED/FRRESP/HDF5/Hotstart. 확인된 필수 검증: 최초 유사계산 시간간격 누락, `GNU`의 `DLSMAX` threshold lag, 기존 output44 초기화 및 시간 재설정 오류, 외부 sediment boundary 미구현, BALSED 빈 함수, 수문 hotstart의 sediment 미포함, VS08 재생성으로 잔존 토심 소실 미표현. **SHETRAN 후보 유지, 최종채택 및 수치검증 주장 보류.**


## 2026-10-26 실제 SHETRAN 4.7.2 native 실행 (정적 검토 이후 갱신)
- [원본 SHETRAN Cobres 0,10,30,50 mm/h 강우사상 실행](decisions/2026-10-26_SHETRAN_472_NATIVE_COBRES_RAIN_QA.md)은 upstream SHA cf9cd540add78ad3accbaf62b4199d2032887f6b Fortran 4.7.2.0 실제 빌드/실행 로그에 근거. 원본 방정식과 코드 수정 없이 2 km 원본 Cobres 입력 복사에 강우 3시간, 48시간 사건으로 설정했다.
- s_v_er 최대 0,2.708,105.330,430.591 mm/day; HDF5 시계열 오른쪽 끝 적산 최대 총침식 0,0.143,15.724,29.702 mm (내부 정확 적산이 아니라 근사). 초기 DLS=30mm, HDF5 t=0=0mm 출력 오류 주의. 종료시간 48h 초과 18.9~37.9분.
- 20/40mm/h 추가 자동 native 실험은 진행 중이며, 완결 전까지 통과로 쓰지 않는다.
- **고운사 final model 채택 X**: native erosion/sediment budget, 일관된 sediment restart, VS08 잔존토심, grid-link-bank DEM event coupling은 미검증.


### 2026-10-26 원본 SHETRAN 강우 5강도 native 시험 종결
- [native QA 결정 기록](decisions/2026-10-26_SHETRAN_472_NATIVE_COBRES_RAIN_QA.md): 실제 pinned SHETRAN Fortran 4.7.2.0 빌드 및 건조, 10,20,30,40,50 mm/h 3시간 강우 + 건조 후속 실행, HDF5 sediment 기록 분석이 [CI run 40287116566](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40287116566)에서 전부 성공. 이전 문서의 '20,40 진행 중' 기록은 이 최신 판정으로 대체.
- 강우강도 10/20/30/40/50 mm/h 최대 침식률 각각 2.708/67.260/105.330/133.284/430.591 mm/day. 시간별 HDF5 근사 최대 누적 원토양 박리 각각 0.143/6.770/15.724/23.506/29.702 mm. 이는 native 내부 exact GNU 적산이 아님.
- 원본 초기 SY51 DLS 30mm인데 native HDF5 t=0 DLS=0mm로 출력되는 초기화 이전 snapshot 확인. 원본 종료시각 48h를 최종 시간이 18.90~51.73분 초과. 정확한 외부 사상 경계 연동에서 해결 필수.
- SHETRAN native 침식 계산 구동 성공과 **원본 유사질량수지 폐합, 정확한 강우사상 종료, 퇴적층 상태 전체 재시작, DEM/토심 재입력에 따른 유동 피드백 검증은 별개**. 고운사 최종 모델 확정 불가.
