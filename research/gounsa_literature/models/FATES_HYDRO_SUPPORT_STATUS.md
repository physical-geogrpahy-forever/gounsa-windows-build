# FATES-HYDRO current support status

업데이트: 2026-09-23

## 왜 별도 기록하는가
FATES current source `FatesInterfaceTypesMod.F90`의 `hlm_use_planthydro` 주석에는 `THIS IS CURRENTLY NOT SUPPORTED`라는 문구가 남아 있다. 그러나 2024-2026의 실제 개발/실행/논문 근거는 FATES-HYDRO가 실제로 작동하고 연구에 사용되는 기능임을 보여준다.

따라서 단일 source comment만으로 production status를 판정하지 않고 현재 실제 상태를 분리해 기록한다.

## 현재 확인된 실행/개발 근거
2024 FATES maintainers discussion `hydro solver default`:
- Taylor 1D solver가 기존 default
- Picard solver가 all root layers와 plant compartments를 동시에 풂
- collaborators가 Picard가 dry-grid crashes를 줄였다고 보고
- 2024-09에는 API36.0에서 `fates_hydro_solver=2` Picard로 out-of-box Hydro 실행에 성공했다고 보고
- 2025-09에도 default solver setting을 E3SM HLM namelist에서 고치는 discussion/issue가 이어짐

즉 Hydro code는 dead/unreachable feature가 아니다.

## 연구 사용 근거
- Xu et al. 2023 FATES-HYDRO V1.0 model paper
- 2025 coastal vegetation dynamics study uses FATES-Hydro
- 2025 Fire Ecology ponderosa pine study parameterized and ran FATES-HYDRO
- 2026 New Phytologist review treats FATES-HYDRO as an operating hydrodynamic model
- 2026 GitHub issue documents users running CLM-FATES with Hydro on

## 하지만 maturity warning은 유지
FATES official `Current Unsupported or Broken Features` page classifies FATES Hydro as experimental and notes limited evaluation for combinations such as Hydro + fire/logging.
The page itself has an old update history, so it cannot alone establish current failure status, but it remains an official caution.

A January 2026 open GitHub issue reports anomalous global forest patterns when CLM-FATES Hydro is active in one configuration, while another collaborator can reproduce more realistic behavior with the same parameter/meteo setup. This indicates host/soil/configuration sensitivity and unresolved robustness issues rather than a simple universal failure.

## current source comment conflict
Current `FatesInterfaceTypesMod.F90` still comments:
```fortran
integer, public :: hlm_use_planthydro
! THIS IS CURRENTLY NOT SUPPORTED
```
Yet the same source defines multiple hydraulic solvers and current users/maintainers actively run the feature.

Therefore this comment is treated as either stale or reflecting a narrower support convention. It is **not** sufficient evidence to classify FATES-HYDRO as unusable.

## correct Gounsa interpretation
```text
FATES-HYDRO
= functional and actively used in research
+ sophisticated plant hydraulic machinery
+ available in current host configurations
- still experimental / configuration-sensitive
- not a low-risk turnkey production feature
```

For Gounsa, Hydro remains a scientific advantage but its maturity risk must be included in engineering comparisons.

## implication for ranking
Previous statement:
`FATES = strongest ready hydraulics`

should be nuanced to:
`FATES = strongest mechanistic plant-hydraulics option among shortlist, but Hydro maturity is lower than the basic FATES demography and requires dedicated validation.`

This does not remove FATES from the top tier, but reduces the advantage attributed to Hydro when comparing with LPJ-GUESS + external ParFlow or MEDFATE + SERGHEI.

## references
- Xu et al. (2023), GMD 16, FATES-HYDRO V1.0.
- NGEET/fates Discussion #1187, hydro solver default, 2024-2025.
- NGEET/fates Issue #1527, CLM-FATES Hydro global patterns, opened 2026-01-27.
- FATES Users Guide, Current Unsupported or Broken Features.
- Dukes et al. (2026), New Phytologist, plant hydrodynamic model review.
