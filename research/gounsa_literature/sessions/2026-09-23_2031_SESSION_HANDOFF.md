# 2026-09-23 20:31 고운사 식생엔진 심층감사 인계

## 이번 세션 목표
광범위 후보탐색을 끝내고 상위 계열을 source/state-variable 수준으로 파서 실제 고운사 coupling 가능성을 판정.

상위 후보:
1. FATES
2. LPJ-GUESS SEC/PPA + external hydrology
3. MEDFATE + medfateland
4. JULES-RED fallback

EDYS는 ecogeomorphic architecture benchmark.

---

## 이번 세션의 핵심 새 결론

### FATES
- current default source has tree, shrub, C3/C4 grass PFTs.
- generic seed production/bank/germination/recruitment exists.
- PFT-specific inter-grid seed-dispersal fraction and maximum distance exist.
- actual seed dispersal is coordinated by host-land-model cadence.
- `FatesInterfaceMod.F90` explicitly defines the **FATES public API**.
- host supplies `bc_in`; FATES returns `bc_out`.
- HLM interface controls soil layers, timestep, restart, seed-dispersal cadence, hydraulics, recruitment, etc.
- therefore FATES requires a host/driver but is not conceptually fixed to ELM/CLM.
- source interface includes `max_rooting_depth_index_col`, explicitly defined for bedrock/permafrost rooting limits.
- root fraction is recalculated against actual host soil interfaces.
- FATES-HYDRO gives strongest cohort plant-hydraulic structure among shortlist.
- however erosion does not automatically kill/export roots in removed soil. New root-severing/remap needed.

### LPJ-GUESS SEC/PPA
- SEC nominal patch 0.1 ha ≈ 31.6×31.6 m, very close to desired 25–50 m vegetation cell.
- persistent within-patch cohort gap positions and forest-floor light mosaic are unique strengths.
- same patch count runtime: SEC ~2.26× standard LPD, PPA ~1.54×; SEC can converge with fewer replicate patches.
- PF-LPJG and SEC modifications are relatively orthogonal enough to justify prototype merge.
- preferred route: SEC biology + PF-LPJG external hydrology ownership + selected RE soil/bedrock concepts.
- do not run full RE Richards and ParFlow simultaneously.
- crucial limitation: allocation, establishment, background mortality remain mainly annual. 6-hour erosion/root-loss event needs explicit immediate damage hook.
- LPJ-GUESS-RE shallow soil can pack missing root fraction into bottom layer. Do not use this after erosion; physically remove root mass first.

### MEDFATE
- actual GIS cells and daily state manipulation remain easiest engineering route.
- `soilDomains="none"` allows external bulk hydrology.
- `soil_redefineLayers()` allows rebuilding layer widths but explicitly loses initialized state, so conservative remapper is mandatory.
- herbs have real Z50/Z95/Z100 root profiles and participate in daily physiology.
- decisive downgrade: `regeneration.R` removes herbData in recruitment forest and does not create herb recruits like tree/shrub.
- stronger downgrade: `growth_day_c.cpp` explicitly sets `dynamicCohort=false` for herb, so herbs do not use woody daily dynamic mortality path.
- therefore selecting MEDFATE requires a full herb lifecycle module, not just a small recruit helper.
- woody daily fine-root, hydraulic, growth and mortality response is strong.

### JULES-RED
- source `veg3_red_dynamic_mod.F90` explicitly computes reproductive allocation, seedling influx, mass-class flux, mortality and plant-number-density change.
- current caller passes `rsec_per_day`; source-level daily demography confirmed.
- important downgrade for geomorph coupling: mass-class carbon is re-aggregated to PFT-level `rootC`; root depth is prescribed PFT exponential weighting.
- soil-layer thickness structure is much less friendly to event-driven cell-specific soil-depth change.
- remains lightweight fallback.

---

## 현재 판정
절대 1위 하나보다 다음 삼각구도가 정확하다.

```text
FATES
= strongest ready biology + daily demography + hydraulics

LPJ-GUESS SEC
= strongest spatial canopy/cohort middle ground

MEDFATE
= strongest engineering / GIS / daily event-loop usability

JULES-RED
= lightweight fallback
```

---

## 공통 새 coupling
어느 후보를 쓰든 고운사에는 다음 module이 필요하다.

```text
geomorph event
 -> old/new soil interfaces
 -> conservative remap of water/C/N
 -> calculate roots in physically removed soil volume
 -> subtract live/dead roots
 -> route removed roots to sediment/export/dead organic pools
 -> root burial/exposure stress
 -> resume vegetation model
```

단순 root-fraction renormalization을 physical root loss와 동일시하지 않는다.

---

## common-event prototype
모든 후보에 동일한 시험을 적용한다.

```text
T0 postfire state
T1 6-hour extreme storm
 -> erosion/deposition
 -> soil-depth change
 -> root loss/burial
 -> hydrologic state change
T1+1 day physiological response
T1+season/year recruitment/mortality/succession
```

최종 엔진은 feature count가 아니라 **이 시험을 가장 적은 비문헌 custom biology로 통과하는 모델**로 선택한다.

---

## 이번 세션 저장/갱신 파일
- `models/LPJ_GUESS_SPATIAL_COHORT_SYNTHESIS.md`
- `models/FATES.md`
- `models/MEDFATE_MEDFATELAND.md`
- `models/JULES_RED.md`
- `decisions/2026-09-23_VEGETATION_ENGINE_DEEP_AUDIT.md`
- `decisions/2026-09-23_VEGETATION_ENGINE_DEEP_AUDIT_ADDENDUM.md`
- 이 인계서

---

## 바로 다음 작업
1. FATES `bc_in/bc_out` exact state contract audit: soil moisture/potential, soil layers, root uptake, litter/C/N fluxes.
2. LPJ SEC event damage insertion point를 가능한 source/paper level에서 특정.
3. MEDFATE herb lifecycle을 추가할 경우 필요한 최소 state/equations 산정.
4. 네 후보 common-event prototype의 state vector와 event sequence를 표준화.
5. 이후에만 실제 prototype code implementation 여부 결정.
