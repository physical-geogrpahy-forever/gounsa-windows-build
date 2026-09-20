# 결정: 고운사 유수침식 엔진 재평가와 잠정 구현구조

날짜: 2026-09-21

## 결정 내용

기존의 “Iber+ 2024를 우선 본체로 확정” 방향을 철회한다.

현재 고운사 유수침식의 **잠정 1차 구현 엔진**은:

```
SWEHR / McGuire 2016
+ 2D Hairsine-Rose erosion
+ hourly-rainfall event manager
```

로 둔다.

SERGHEI-SE는 **2차 구현 후보 및 HPC fallback**으로 둔다.

Iber+는 process/numerics 비교대상으로 유지하지만, 일반 사용자에게 공개된 배포물이 실행파일 중심이고 독립적인 소스 수정 접근성이 확인되지 않았으므로 현재 1차 구현 본체에서 내린다.

tRIBS-FEaST / tRIBS-Erosion은 장기 event-to-event surface memory와 100-year hydro-geomorphic simulation의 구조적 선례로 유지한다.

---

## 왜 SWEHR인가

고운사와 직접 맞는 과정이 가장 많다.

```
steep postfire mountain
+ genuine 2D
+ rainfall detachment
+ flow entrainment
+ emergent rill
+ original cohesive soil
+ deposited/loose sediment layer
+ shielding
+ multi-size sediment
+ deposition
+ topographic change
+ field/TLS calibration
+ public GPL C source
```

공개 코드에 이미 셀별:
- `ASMASK`
- `ADSMASK`
- `JSMASK`
- `UC`
- `UC2`
- `H`
- `M[k]`

가 있으므로 LPJ-GUESS 상태를 받기 위한 수정 지점이 명확하다.

SERGHEI-SE보다 오래되고 느리지만, 고운사의 핵심 연구질문에 필요한 **새로운 과정식을 덜 만들어도 된다.**

---

## 공개소스 비교 결과

### SWEHR
- GPL v2
- public C source
- erosion resistance arrays 직접 감사 완료
- single processor
- single-rainstorm event model 성격
- Courant stability constraint

### SERGHEI-SE
- public 3-clause BSD source
- C++ / Kokkos / MPI
- modern HPC and portability
- spatial parameter-array architecture
- public tests
- 그러나 quantitative root/litter resistance와 postfire Hairsine-Rose-style intact/deposited structure를 새로 설계해야 함

### Iber+
- C++ / CUDA / OpenMP
- 매우 강한 GPU/finite-volume architecture
- public executable/test data는 확인
- 일반 사용자에게 완전한 수정가능 source가 공개되었다고 확인하지 못함
- collaborator source access가 있으면 즉시 재평가

---

## root coupling 결정

### 직접 확인된 문헌
Gyssels et al. 2005:
```
SEP_root = exp(-b RP)
```

rill erosion review-average:
- root density: `b = 0.5930`
- RLD: `b = 0.0460` when RLD is km m^-3

Hairsine-Rose/SWEHR:
```
E_flow ∝ 1/J
```

### 고운사 새로운 coupling

같은 hydraulic forcing, shielding, `F`, threshold stream power에서:

```
E_root / E_bare = SEP_root
```

이므로:

```
J_eff
= J_bare / SEP_root
= J_bare * exp(b RP)
```

를 사용할 수 있다.

이 식은 기존 published model이 아니다.

**Gyssels empirical response를 SWEHR의 기존 `1/J` 구조에 대수적으로 삽입한 새로운 coupling이다.**

### 제한
- Gyssels average `b`는 sensitivity/initial prior로만 사용
- 최종 `b`는 PFT/species/root architecture를 고려하여 보정
- FineRootC -> RLD 변환은 별도 해결
- 같은 root effect를 `J`와 `UC`에 동시에 적용하지 않는다
- `cohesion -> J` 보편식이 있다고 주장하지 않는다

### alternative validation pathway
De Baets + Léonard & Richard + PROMET:

```
RLD
 -> erosion-specific cohesion / soil strength
 -> tau_c
```

이 경로는 root-resistance validation 및 sensitivity에 사용한다.

하지만:
```
tau_c -> SWEHR UC
```
는 아직 직접 문헌식이 없으므로 만들지 않는다.

---

## surface litter coupling 결정

SurfaceLitter와 IncorporatedLitter는 분리한다.

### mass -> cover

Gregory / WEPP / Pannkuk-Robichaud 계열:

```
C_lit = 1 - exp(-b_m M_lit)
```

- `M_lit`: exposed dry litter mass/area
- `b_m`: litter-type-specific coefficient

Pannkuk & Robichaud 2003은 실제 postfire conifer forest, 40% slope 조건에서 needle mass -> cover와 cover -> interrill/rill protection을 정량화했다.

### baseline rainfall-protection coupling

```
f_lit,rain = exp(-k_lit C_lit)

ASMASK_eff
= ASMASK_bare * f_lit,rain
```

이 결합식은 **새로운 coupling**이다.

Pannkuk & Robichaud의 `k_lit` 값은 local transfer coefficient가 아니라 functional-form evidence 및 sensitivity prior로만 사용한다.

### 상태분리

```
SurfaceLitter
 -> mass -> cover -> rainfall shielding / interception / roughness

IncorporatedLitter
 -> soil structure -> Kr / tau_c type effects

DepositedLooseSediment
 -> M[k] -> H shielding / armoring
```

세 상태를 하나로 합치지 않는다.

---

## 100년 시간구조 결정

고운사 강수 forcing은 1시간 자료다.

따라서 외부 forcing은:

```
P_1h(t)
```

를 그대로 사용한다.

각 1시간 구간에서 강수량/강도는 piecewise constant forcing으로 준다.

하지만 SWEHR 내부 numerical time step은 1시간으로 두지 않는다.

```
hourly rainfall forcing
 -> sub-hourly hydraulic/sediment integration
 -> CFL stability
```

을 사용한다.

장기모의는:

```
hourly rainfall series
 -> storm-event segmentation
 -> SWEHR event simulation
 -> topography/H/M[k]/PSD persistence
 -> next event
```

으로 수행한다.

LPJ-GUESS는 ecological time step에서 root/litter/biomass를 갱신한다.

사건 사이:
- surface water depth는 drain/reset 가능
- suspended sediment는 event-boundary rule에 따라 정리
- topography는 유지
- deposited sediment `M[k]` 유지
- shielding `H` 유지
- surface PSD 유지
- soil/vegetation state 유지 및 갱신

storm separation dry-gap은 임의 고정하지 않고 hydrologic response와 sensitivity test로 결정한다.

---

## 이 결정이 뒤집은 것

이전:
```
Iber+ 2024 = 가장 유력한 2D 본체
```

현재:
```
SWEHR = 1차 process engine
SERGHEI-SE = modern HPC fallback
Iber+ = source access 확보 시 재평가
```

변화 이유:
1. McGuire 2016의 process match 재평가
2. SWEHR 공개 C source 직접 감사
3. 셀별 `J/UC/detachability` field 확인
4. emergent rill 확인
5. postfire steep-mountain TLS calibration 확인
6. Iber+ 일반 공개 source-access 제약 확인
7. SERGHEI-SE 공개 BSD/Kokkos source 확인
8. root와 litter의 방어 가능한 coupling path 추가 확보

---

## 아직 확정되지 않은 것

1. LPJ-GUESS FineRootC -> PFT별 RLD 변환
2. `J_bare`의 고운사 토양 calibration
3. 한국 산림 litter별 `b_m`, `k_lit`
4. storm-event separation dry-gap
5. actual Gounsa DEM에서 SWEHR runtime
6. 100-year event count와 계산비용
7. SWEHR를 그대로 유지할지, 이후 SERGHEI-SE에 Hairsine-Rose-like closure를 port할지
8. root effect를 `J` 대신 `tau_c`-native closure로 쓰는 대안의 validation

---

## 최종 판정

**SWEHR를 잠정 1차 구현 엔진으로 채택한다.**

단, 이것은 production hard-lock이 아니다.

다음 hard-lock 조건:
- actual DEM runtime benchmark
- hourly rainfall event wrapper prototype
- FineRootC -> RLD interface
- litter mass -> cover/protection interface
- 최소 수 개 관측/대표 storm calibration

이 조건을 통과하지 못하면 SERGHEI-SE를 본체로 승격하고 Hairsine-Rose/postfire process closure를 이식하는 방안을 검토한다.


---

## FineRootC -> RLD 업데이트

이전 결정문에서 미해결로 두었던 `FineRootC -> RLD`의 수식/단위 구조는 해결됐다.

```text
RLD_p,i = C_root,p * SRL_C,p * f_p,i / Dz_i
```

이 식은 LPJ-GUESS fine-root C와 carbon-based SRL, PFT별 soil-layer root fraction을 사용한다.

따라서 root coupling의 현재 baseline은:

```text
FineRootC
 -> PFT-specific RLD
 -> SEP_root = exp(-b RLD)
 -> J_eff = J_bare / SEP_root
```

남은 것은 `SRL_C`, active-depth weighting, postfire live/dead-root persistence와 local calibration이다.

세부: `models/LPJ_GUESS_Root_Erosion_Interface.md`
