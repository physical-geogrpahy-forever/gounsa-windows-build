# Gounsa literature session handoff

시작 기준 시각: 2026-09-21 01:47 KST  
브랜치: `gounsa-water-erosion-deep-review-2026-09-21`

## 이번 세션의 핵심 변화

기존의:
```
Iber+ 2024 우선
```
판정을 재검토하고 다음으로 변경했다.

```
SWEHR / McGuire 2016
= 잠정 1차 water-erosion implementation engine

SERGHEI-SE
= modern open-source HPC fallback

Iber+
= strong numerical comparison engine,
  but source access 확보 시 재평가
```

## source-code audit

### SWEHR
- public GPL C source
- cell-wise `ASMASK`, `ADSMASK`, `JSMASK`, `UC`, `UC2`, `H`, `M[k]`
- postfire steep-mountain/TLS process match strongest
- single-processor/event-scale model
- 100-year continuous second-by-second run이 아니라 event wrapper 필요

### SERGHEI-SE
- public 3-clause BSD
- C++ / Kokkos / MPI
- modern HPC
- distributed spatial parameter/state arrays
- root/litter quantitative erosion-resistance coupling은 아직 없음

### Iber+
- C++ / CUDA / OpenMP
- strong GPU finite-volume erosion
- public executable/test data confirmed
- general public modifiable source access not verified
- collaborator source access 확보 시 재평가

## root bridge

Direct universal:
```
cohesion -> Hairsine-Rose J
```
equation은 찾지 못했다.

Gyssels et al. 2005:
```
SEP_root = exp(-b RP)
```

SWEHR:
```
E_flow ∝ 1/J
```

따라서 baseline **new coupling**:

```
J_eff
= J_bare / SEP_root
= J_bare * exp(b RP)
```

rill RLD review-average:
```
b = 0.0460
```
for RLD in km m^-3.

주의:
- review-average `b`는 sensitivity/initial prior
- FineRootC -> RLD는 별도 해결
- `J`와 `UC`에 root effect를 동시에 적용하지 않음

Alternative validation pathway:
```
RLD
 -> erosion-specific cohesion / soil strength
 -> tau_c
```

근거:
- De Baets 2008/2020
- Léonard & Richard 2004
- Waldmann PROMET 2010

하지만:
```
tau_c -> SWEHR UC
```
직접식은 없음.

## surface litter bridge

새 핵심문헌:
- Gregory 1982
- Pannkuk & Robichaud 2003
- WEPP residue documentation
- Ding et al. 2020

Mass to cover:
```
C_lit = 1 - exp(-b_m M_lit)
```

Pannkuk & Robichaud 2003은 postfire conifer forest 40% slope에서 needle mass-cover와 interrill/rill protection을 직접 검증.

Baseline **new coupling**:
```
f_lit,rain = exp(-k_lit C_lit)
ASMASK_eff = ASMASK_bare * f_lit,rain
```

State separation:
```
SurfaceLitter != IncorporatedLitter != DepositedLooseSediment
```

## hourly rainfall and 100-year architecture

사용자 확인:
- precipitation forcing은 1-hour data

따라서:
```
hourly rainfall
 -> storm segmentation
 -> piecewise-constant hourly forcing
 -> SWEHR sub-hourly CFL integration
 -> persist topography/H/M[k]/PSD
 -> next event
```

SWEHR internal numerical timestep은 1시간이 아님.

LPJ-GUESS:
- long-term ecological clock
- FineRootC/litter/biomass update

SWEHR:
- erosive storm-event solver

storm dry-gap은 임의 고정하지 않고 hydrologic response와 sensitivity로 정한다.

## 이번 세션에서 새로 만든 논문 md

- `papers/1982_Gregory_ResidueMass_SurfaceCover.md`
- `papers/2003_Pannkuk_Robichaud_Postfire_NeedleCast.md`
- `papers/2004_Leonard_Richard_CriticalShear_SoilStrength.md`

## 이번 세션에서 주요 수정한 파일

- `models/Iber.md`
- `models/SERGHEI_SE.md`
- `models/Hairsine_Rose_2D_Postfire.md`
- `models/PROMET_DANUBIA.md`
- `papers/1995_Stott_WEPP_Residue_Component.md`
- `papers/2005_Gyssels_Root_Resistance_Erosion_Review.md`
- `papers/2010_Waldmann_PROMET_Large_Scale_Erosion.md`
- `papers/2020_Ding_PineLitterTransportCapacity.md`
- `MASTER.md`
- `INDEX.md`

## 새 decision

`decisions/2026-09-21_WATER_EROSION_ENGINE_REASSESSMENT.md`

핵심:
- SWEHR 잠정 1차 구현 엔진
- SERGHEI-SE HPC fallback
- Iber+ source access 확보 시 재평가
- hourly event-driven architecture
- root baseline receiver = `J`
- surface litter = mass -> cover -> rainfall protection

## 현재 INDEX 상태

세션 인계서 추가 직전:
- Papers: 261
- Models: 26
- Decisions: 9
- Sessions: 2

이 파일 추가 후 Sessions는 3으로 INDEX를 다시 갱신해야 한다.

## 다음 시작점

### 1순위
```
LPJ-GUESS FineRootC
 -> PFT-specific RLD
```
정량 변환을 확정한다.

필요:
- LPJ-GUESS FineRootC 단위
- carbon -> dry root biomass
- PFT별 SRL 또는 diameter/architecture
- soil-layer vertical root distribution
- postfire live/dead root dynamics

### 2순위
실제 고운사 DEM + 1시간 강수자료를 가정한 SWEHR runtime/event-count prototype 설계.

### 3순위
한국 산림 litter 유형별 `b_m`, `k_lit` 자료 탐색.

### production hard-lock 전 조건
- FineRootC -> RLD
- `J_bare` calibration strategy
- litter mass-cover/protection parameterization
- storm segmentation
- actual DEM runtime benchmark
- representative storm validation
