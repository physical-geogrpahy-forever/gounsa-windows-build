# 2026-10-26 21:40 KST: EUROSEM 기존 '차이 너무 적음' 재감사 인계

## 중요 사용자 지시
앞서 LAI 1→4, COVER10→90%에 따른 침식량 차이가 너무 작아 내린 EUROSEM 폐기 판정을 다시 살펴, **과거 시도가 잘못된 것인지 원본 소스와 실제 자료로 재현하라**. 전송 시간 초과/연결 단절이 반복되어 **작업을 이어가기 위한 기록**. 임의로 모델을 다시 적합하다고 선정하지 말고 native hydrology/sediment QA 구분.

## 원래 729회 결과를 되찾음
- `three_erosion_parameters_total_729_runs.csv` Project Library 실제 원자료 729×23 직접 pandas 재분석, `요인별_민감도_분석보고서.md` 함께 확인.
- **정확한 원래 실험 코드** `eurosem-single-model-lai-20261025/eurosem_lai_1998/patch_interception.py` GitHub 직접 조회. `LAI.PAR`은 **연구진 2026 새 함수**로서 본래 EUROSEM에 LAI 독립 매개변수 없음. Synthetic Sleaf=.20 mm/LAI, k_leaf=.046. Cumulative storm capacity saturates 0.2–0.8mm from 1→4 LAI; 30/50mm/h 1h storm runoff effect inherently small.
- 729분석 30mm/h mean sediment LAI1=15.29803, 2.5=14.40108, 4=13.53007t/ha. COVER .1→.9 at 30mm/h LAI2.5 S0.3: free TF 27→3mm, leafdrip 1.067→11.303mm, stemflow 1.434→15.197mm, outlet sediment 12.982973→12.981208 t/ha. EROD .1→.9 per matched 81 groups max 5.016e-6t/ha.
- Native original input height **cm**: prior PLANTH=3.0 = 3cm, suppresses `max(15.8sqrt(H_m)-5.87,0)` until ~13.8cm. Real grass/oak scenario erroneously set 1.2/2.5 as metres rather than native cm in earlier trials. Later 80cm correction had positive KE but still no output response.

## 1998 original Fortran source smoking gun
- `TheSoilman/EUROSEM/eurseml.for` `KINET`: `DRIPKE=(15.8sqrt(PLHGT)-5.87)*DRIPD/RAIN`
- `DRIPS`: `DMMSEC=RMMSEC*DRIPD/RAIN`, `DRDTIN=DRIPKE*DMMSEC*...*ERODGJ`. Thus leafdrip energy source scales with **(drip/rain)^2**. Theory Morgan (1998) KE leaflet × drip depth once. Native bug check confirmed.
- `emainl.for` reads PLANTH cm→m.
- `eplanel.for` `MCODE>=1` selects Everaert for interrill, `MCODE=0` Govers, old report wrongly called MCODE1 Govers.
- `eusedl.for` `DTRF=PAVF*CGU*TW` and `DTRC=DTRF*CEX + PAVF*RDET(I)`, `SUP=DTRC - CT*DTRF` may mix bed-area detachment m/s with width-bearing transport m²/s. Require dimensional source derivation; experimental width patch alone not author validation.
- The original shallow soil limit and independent sediment mass conservation NOT proven. Default test.par original soil erosion depth cap DERO5m synthetic; not actual Gounsa.

## 28 native full original/experimental Fortran re-runs, 20+8
- Model code from TheSoilman original cloned by GitHub Actions into GNU Fortran CI; 1998 equations unchanged except clearly labelled trials.
- 20 factorial native tests (H3 vs H120cm, COVER.1/.9, EROD .1/.9, original vs removing duplicate drip-ratio; and Govers counterpart) 20/20 hydrology QA PASS, all **reported net erosion unchanged for EROD or drip-source fix**; mcode1/C90/H120 case 25.630276t/ha, mcode0 21.592552t/ha.
- [main 20 runs](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40322591668).
- [20 reruns with `SPLASH_DIAG` + `SED_SOURCE_DIAG`](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40323173111): native EROD×9→RDET×9; removing duplicated drip weighting→ RDET×1.5. At L40, C90,H120, mcode1, EROD .1: original RDET first grid1.6625e-9m/s vs corrected2.4959e-9m/s, at downstream point RDET2.054e-10, flow term DTRF*CEX0.007768, net SUP9.346e-5 (printed precision unchanged). This is **transport term dominated**, not a missing EROD input.
- [8 source width counterfactual tests](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40323570418) multiply RDET by TW only in two candidate width-conversion expressions. 8/8 original native hydrology QA. Govers export 24.435034→24.435103 at EROD.1, at EROD.9 24.435034→24.435241t/ha; Everaert 28.619862→28.620069 at .9. This is a hypothetical **modified fork** and does not repair non-2D limitations. This 8-run subset has DINT .9 vs 20-run DINT1.5 so do NOT cross-compare absolute sediment.
- All output t/ha values are original **reported net soil erosion**. None has passed **independently calculated sediment and deposit ledger**.

## Current verdict
**Withdrawal:** "LAI/COVER differences intrinsically small so canopy has no erosional influence" is scientifically unjustified. The previous experimental inputs were flawed (height units) and the original source drip factor is doubly weighted, while native flow entrainment / capacity numerically dominates under synthetic settings.
**Maintain strict caveat:** EUROSEM a 1D linked slope model, cannot spontaneously simulate spatial 2D rills or stemflow around separate stumps, not full primary Gounsa erosion engine. But **can be used for physically audited canopy-interrill comparison**, if sediment store and field parameters can be independently validated. No full original correction or acceptance claim.
**Next priority:** independent EUROSEM sediment mass ledger and physical dimensional checking; event dt convergence. If 1D acceptable for subsidiary benchmark, use corrected plant height/LAI/source attribution, avoid misusing trunk SF as spatially resolved.

## Saved this turn
- `decisions/2026-10-26_EUROSEM_729_LOW_VEGETATION_SENSITIVITY_ROOT_CAUSE_REAUDIT.md`
- `models/EUROSEM.md` updated
- `MASTER.md` updated
- Testing code `experiments/rainfall_10_50/verify_eurosem_reaudit_20261026.py`, `run_eurosem_bug_reaudit_20261026.py`, `run_eurosem_width_trial_20261026.py`
- Workflows `.github/workflows/eurosem_drip_ratio_reaudit_20261026.yml`, `eurosem_splash_width_unit_recheck_20261026.yml`
