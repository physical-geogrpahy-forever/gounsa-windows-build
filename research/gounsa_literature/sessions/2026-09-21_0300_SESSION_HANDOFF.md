# Gounsa literature session handoff

날짜: 2026-09-21  
브랜치: `gounsa-water-erosion-deep-review-2026-09-21`

## 세션 주제
Pelletier 2013을 100년 고운사 토양 풍화 및 사면확산의 주 모델로 사용할지, 더 짧은 시간간격의 published process models로 대체할지 재검토.

## 핵심 결론

**Pelletier 2013을 주 모델로 사용하지 않는다.**

이유:
- model objective is geologic-time-scale eco-pedo-geomorphic coevolution
- prescribed EEMT states
- reported landscape states after 10 Myr
- small internal timestep is numerical-stability requirement, not annual ecological calibration

100년 고운사는 daily/event/annual multi-rate process architecture를 사용한다.

---

## weathering decision

### chemical hydroclimatic weathering
Primary:
`LPJ-GUESS-CNP 2025`

Exact citation recovered:
Dantas de Paula et al. 2025, GMD 18, 2249-2274.
DOI 10.5194/gmd-18-2249-2025.

Important:
- actual LPJ-GUESS implementation
- daily weathering rates for every patch
- uses LPJ-GUESS prognostic soil temperature and runoff
- vegetation affects runoff, creating a vegetation-weathering feedback

Core:
```
F_PW = F_CW,i * F_T * F_s,i
F_CW,i = (b_carbonate + b_silicate)_i * p_i * q
```

Unresolved:
```
chemical weathering/mineral flux
 -> geomorphic regolith mass/thickness
```
is a new coupling.

### woody mechanical weathering
Primary:
`Gabet & Mudd 2010`

Exact source re-read:
- annual timestep
- tree recruitment/mortality annually
- stochastic tree throw annually
- exposed clast physical weathering annually
- bedrock erosion computed annually
- soil creep annually

Original Oregon sandstone coefficients are NOT transferred.

### comparison
- REWTCrunch 2022: root/reactive-transport advanced validation
- SoilGen 2022: daily hydrology + 1D chemical-weathering profile benchmark
- SSSPAM 2019/2021: physical weathering/profile/armour and 100-year feasibility
- Pelletier 2013: long-term structural benchmark

---

## hillslope transport decision

Do not use one vegetation-dependent diffusion coefficient.

Current:
```
q_hill
=
q_bg
+
q_rootgrowth
+
q_treethrow
+
q_dryravel
```

### q_bg
First implementation:
```
q_bg = -D_bg S
```
as a residual background creep term.

Reason:
explicitly modeled separately:
- root growth/decay
- tree throw
- postfire dry ravel
- shallow landslides

Using a field-calibrated total forest diffusivity without removing these processes would double count them.

### Roering 2001
Nonlinear alternative/sensitivity:
```
q =
-K grad(z)
/
[1-(|grad(z)|/S_c)^2]
```

Useful for steep-slope sensitivity, but:
- K may aggregate biological disturbance
- near-critical nonlinearity may overlap explicit shallow landslides
- therefore not baseline without residual calibration

### q_rootgrowth
Gabet et al. 2003:
annual root-turnover bioturbation.
Use LPJ-GUESS native root state/turnover.

### q_treethrow
Doane et al. 2021:
- one-year timestep
- annual stochastic pit-mound production
- 2D topographic roughness / sediment flux

CSDMS TreeThrow:
- independent annual timestep precedent
- tree growth/death/regeneration -> tree fall -> sediment flux
- source currently categorized unavailable by CSDMS
- use as conceptual/model precedent, not code base

### q_dryravel
Lamb 2011, already separate.

### shallow landslide
separate discrete mass-wasting module; do not hide inside diffusion.

---

## SSSPAM result

Newly reviewed:
- Welivitiya et al. 2019, DOI 10.5194/esurf-7-591-2019
- Welivitiya et al. 2021, DOI 10.1002/esp.5175

SSSPAM:
- soil profile + evolving landform
- physical weathering
- diffusion
- erosion/deposition
- armouring
- particle-size/profile evolution
- 2021 paper explicitly performs 100-year short-term landform simulations
- can use short events, variable precipitation or annual average precipitation

But:
- no dynamic forest/root state
- physical weathering only in 2019 formulation
- overlaps SWEHR erosion/deposited-layer/PSD/armour states

Current role:
comparison and possible future coarse-fragment/armour source, not primary Gounsa core.

---

## HydroLorica result
Hydrology can use daily/monthly/yearly dynamic timestep.

But authors explicitly state simplified vegetation can change annually and should be interpreted over >100 yr; it should not be used for annual-to-decadal ecological systems.

Therefore architecture reference only.

---

## new paper files

- `papers/2001_Roering_NonlinearHillslopeTransport.md`
- `papers/2019_Welivitiya_SSSPAM_CoupledSoilscapeLandform.md`
- `papers/2021_Welivitiya_SSSPAM_100yr.md`
- `papers/2022_GarciaGamero_SoilGen_ChemicalWeathering.md`
- canonical recovered:
  `papers/2025_DantasDePaula_LPJGUESS_CNP_Weathering.md`

Removed obsolete placeholder:
- `papers/2025_LPJGUESS_PWeathering_CitationUnrecovered.md`

## updated papers
- `papers/2010_Gabet_Mudd_RootFractureTreeThrow.md`
- `papers/2013_Pelletier_Coevolution_Vegetation_Soils_Topography.md`
- `papers/2020_vanDerMeij_HydroLorica.md`
- `papers/2021_Doane_TreeThrowFlux.md`

## new/updated model lineages
- `models/LPJ_GUESS_Weathering.md` updated
- `models/TreeThrow_Annual.md` new
- `models/SSSPAM.md` new
- `models/Short_Timestep_Weathering_HillslopeTransport.md` new
- `models/Doane_TreeThrow_Roughness.md` updated

## new decision
- `decisions/2026-09-21_WEATHERING_HILLSLOPE_TIMESCALE.md`

## MASTER
Updated to:
- demote Pelletier to long-term benchmark
- adopt LPJ-GUESS-CNP daily chemical weathering
- adopt Gabet-Mudd annual woody mechanical weathering
- use modular annual hillslope transport
- note residual-diffusivity double-counting constraint

---

## unresolved next steps

1. chemical weathering flux -> regolith solid mass/thickness conversion
2. local lithology parameters
3. woody cohort -> root-fracture/rootwad geometry
4. residual background creep D_bg calibration
5. annual tree-throw event geometry/rate from LPJ-GUESS
6. quantify whether chemical/physical weathering is detectably important over only 100 years
7. reconcile future coarse-fragment/armour module with SWEHR
8. investigate fire-spall supply separately
