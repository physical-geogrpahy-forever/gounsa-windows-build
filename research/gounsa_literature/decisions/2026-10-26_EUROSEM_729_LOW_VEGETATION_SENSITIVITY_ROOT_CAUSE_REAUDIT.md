# 2026-10-26 EUROSEM 낮은 수관/박리 민감도 재감사: 과거 실험 오류와 원본 수송항 지배

## 판정의 범위

사용자 지시: 기존 "LAI/피복률 차이가 너무 작으므로 EUROSEM 폐기"를 원자료와 **정확히 그 실험을 생성한 포크 코드**, 저자 공개 1998 Fortran을 읽고 재판정한다. 피복률을 식생 생물량 또는 RLD로 오인하지 않는다. **EUROSEM은 처음부터 연결 사면요소 기반의 1D 운동파 구조**여서 새로운 원인 발견만으로 고운사의 genuine 2D 침식 엔진 요구를 통과한 것으로 판정할 수 없다.

## 1. 기존 실제 자료 복구

2026-10-25 결과 CSV `three_erosion_parameters_total_729_runs.csv` 및 `요인별_민감도_분석보고서.md`는 Project 개인 Library에서 확인, 직접 dataframe으로 729행 23열 재분석했다.
- 정확한 실험 코드: `physical-geogrpahy-forever/gounsa-windows-build` branch `eurosem-single-model-lai-20261025`, `eurosem_lai_1998/patch_interception.py`. 이는 original `TheSoilman/EUROSEM`에 **새 `LAI.PAR` 포착계수/저류식**을 삽입한 실험 포크다. **원본 EUROSEM은 LAI 상태변수가 없다.**
- `Smax=S_leaf×LAI`, `k=min(COVER,k_per_LAI×LAI)`, `I(Pcum)=Smax[1-exp(-kPcum/Smax)]`. 사용한 S_leaf=0.2 mm/LAI 및 k_per_LAI=.046은 고운사 교정값이 아니다.
- 결과 (t/ha/event): 30 mm/h LAI 1.0,2.5,4.0 균형평균 15.29803,14.40108,13.53007; 50mm/h 84.93897,83.85250,82.76573. 10mm/h는 전 사례 출력 0.
- 30mm/h, LAI2.5, slope0.3, EROD .5, COVER .1 vs .9: directly TF 27.0 vs3.0mm, canopy drip1.067 vs11.303mm, stemflow1.434 vs15.197mm, **outlet sediment 12.982973 vs12.981208 t/ha**. Thus canopy rain partition is changing strongly, but sediment yield hardly changes.
- Fixed (COVER,LAI,RAIN,SLOPE) EROD0.1-0.9 across 81 3-point groups: max absolute sediment span **5.01567×10^-6t/ha**, zero/rounding precision for almost all cases, even though EROD perturbation ×9.
- Existing 729-run quality audit only water budget <.0376% and canopy volume closure, **no independent sediment mass closure or finite original soil depth audit**. Some synthetic erosion >150 t/ha in one storm, cannot accept as actual Gounsa yield.

## 2. Existing run setting errors and their consequences

**Height units:** `TheSoilman/EUROSEM/emainl.for` lines ~957–962 read `PLANTH` in **cm** and divide by 100. Original factorial kept `PLANTH=3.0` => 0.03 m. `eurseml.for::KINET` L325–345 computes `DRIPKE=max(15.8 sqrt(H_m)-5.87,0)×DRIPD/RAIN`. The height threshold `(5.87/15.8)^2≈0.138m` leads to **zero leafdrip impact energy in all 729 prior original height-3cm runs**. Any physical inference of realistic Miscanthus/coppice leafdrip from that ensemble is invalid. Later archived phenology fixes 80cm show KE >0, but aggregate output unchanged, prompting this deeper audit.

**Model routing:** 729 original branch models two interconnected synthetic hill elements, while new diagnostic controls below use one first original 100×145m plane (14,500m²) specifically to isolate rainfall and erosion. Do not compare absolute sediment values between these distinct study domains.

**Transport formula:** Source `eplanel.for` and `eurseml.for::CAPAC` use `MCODE>=1` for **Everaert** interrill stream-power capacity and `MCODE=0` for **Govers** rill-related formulation. Default `test.par` has MCODE1. Old 'Govers mode by default' claim is false for first-plane non-rill baseline.

**Source-experiment identity:** The 729 experiment is **LAI-modified fork**, NOT pristine 1998 native Fortran. Source-compatible run may still use bug workarounds e.g. NKIR/MB initialization. Do not conclude original model native LAI response from the extended source outputs.

## 3. Original 1998 canopy drip factor duplication (confirmed via original code)

`TheSoilman/EUROSEM/eurseml.for`:
```fortran
C Original KINET already weights energy coefficient by drip fraction
DRIPKE(K)=(15.8*SQRT(PLHGT(J))-5.87)*DRIPD(K)/RAIN(K)
C Original DRIPS AGAIN weights drip rainfall rate
IF(RAIN(IZ).GT.0.) DMMSEC=RMMSEC*DRIPD(IZ)/RAIN(IZ)
DRDTIN(K)=DRIPKE(IZ)*DMMSEC*DAMPF*(1.-RWR(K))*ERODGJ(J)
```
Original effective canopy drip detachment rate depends on **(DRIPD/RAIN)^2**, versus Brandt/Morgan theoretical single weighted drip rainfall rate. This is a **genuine source-equation discrepancy**, not merely unmeasured vegetation uncertainty. Relative to first power, squared fraction underweights drip when drip fraction <1. At rain30mm and drip11.175mm, ratio=0.3725; H=1.2m, effective energy weighted once127.82 J/m², twice47.61J/m²; factor ≈2.685. This is an analytical component comparison, not full-event EUROSEM output.

## 4. Actual new 2026-10-26 native Fortran experimental audit

Original source pin: `TheSoilman/EUROSEM` archived repo as cloned in GitHub Actions. New branch `swehr-water-sediment-closure-20261026` has:
- `experiments/rainfall_10_50/verify_eurosem_reaudit_20261026.py` adapted earlier native full-model harness, preserves original 1998 source equations except an *explicit optional* `--drip-fix` replaced duplicated rate fraction with single factor. Separate `--mcode`, `--trace-splash` and experimental `--test-splash-width` paths all labelled patched.
- `run_eurosem_bug_reaudit_20261026.py`, `run_eurosem_width_trial_20261026.py`.
- [20 full runs original vs isolated drip fix; heights3/120cm, covers10/90%, EROD .1/.9, Govers vs Everaert](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40322591668), **20/20 hydrology QA PASS, sediment ledger NOT TESTED**. For RAIN 30mm/h, synthetic 14500m² single-plane:
  - MCODE1 Everaert, height3cm/COVER10%: net native reported erosion32.36069 t/ha for EROD .1/.9, unchanged drip fix.
  - MCODE1 height3cm/COVER90%:25.63028 t/ha, EROD .1/.9, unchanged drip fix.
  - MCODE1 height120cm/COVER90%:25.63028 t/ha, EROD .1/.9, unchanged drip fix, although `DRIPKE` becomes4.171214 (units code's per-mm energy weighted fraction).
  - MCODE0 Govers height120cm/COVER90%:21.59255t/ha, EROD .1/.9 unchanged drip fix.
  - The numeric values are **reported net erosion**, not independently budgeted outlet sediment. Zero change is at reported output precision, not proof exact mathematical identity at infinite precision.

**Critical in-solver trace** [repeated 20 model runs with RDET and transport printouts](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40323173111):
- At L40, COVER.9, H1.2m, EROD.1, MCODE1:
  - `SPLASH_DIAG`: `RMMSEC=0.0083333mm/s`, original `DMMSEC=.0030390`, corrected `DMMSEC=.0083333`; `RAINKE=3.7656`, `DRIPKE=4.1712`.
  - `RDET(K=1)` original `1.6625e-9` (m/s), corrected `2.4959e-9`; EROD.9 originals `1.4963e-8`, corrected `2.2463e-8`. **EROD ×9 changes internal RDET exactly ninefold** and drip-fix increases RDET 1.5× (rain direct part unaffected).
  - `eusedl.for` `I=NM` same L40: original `RDET≈2.054e-10m/s`, `DTRF*CEX≈7.768e-3` (flow width-bearing quantity), `SUP≈9.346e-5`. Both latter unchanged in printed precision when EROD and drip term vary. Direct comparison of these values as same *physical unit* is not legitimate because code source appears to add `RDET` (m/s per bed area) to width-bearing `DTRF*CEX` (m²/s); code-level dimensional consistency requires independent derivation.
  - Original `eusedl.for` L629–633 `DTRC=DTRF*CEX+PAVF*RDET(I)`, `DTRF=PAVF*CGU*TW(I)`, `SUP=DTRC-CT(I)*DTRF`; source model **computes** raindrop detachment but huge width-bearing flow transport controls sediment exchange/output for this synthetic case. This provides plausible explanation for EROD insensitivity; we are not asserting general ecological irrelevance.

## 5. Second isolated dimensional source experiment, 8 full native calculations

In **explicit experimental fork only**, multiply original `RDET(I)` by `TW(I)` in `DTRC` and inlet `RDET(1)` by `TW(1)` in `SUP(1)`, leaving EROD and hydrology fixed, with original versus width-trial benchmark and corrected double-drip factor.

[8/8 runs](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40323570418) report:
| transport `MCODE` | EROD | original width calculation | experimental width conversion | Δ(t/ha/event) |
|:--|--:|--:|--:|--:|
| 0 Govers | .1 | 24.43503448 | 24.43510345 | +.00006897 |
| 0 Govers | .9 | 24.43503448 | 24.43524138 | +.00020690 |
| 1 Everaert | .1 | 28.61986207 | 28.61986207 | 0 |
| 1 Everaert | .9 | 28.61986207 | 28.62006897 | +.00020690 |

The width-trial defaults `DINT=.9` vs first 20-run series DINT=1.5; **do not compare absolute output between series**. Width multiply hypothesis is not author-sanctioned, and native overall sediment conservation, numerical dt convergence, field sediment observation were NOT done. It shows even added width factor does not restore meaningful canopy/EROD output response in these forcing conditions.

## 6. Final scientific outcome and limits

**Prior exclusion rationale "LAI/canopy effects intrinsically near zero" was NOT supported.** Reconstructed original study contained 3 cm error switching off leafdrip KE, bespoke LAI patch, original drip fraction squared, and enormous synthetic erosion without independent mass QA. Observed canopy partition can change by ~25mm while outlet sediment hardly moves. This is **not a field observation of vegetation inefficacy**.

**But** even after correcting height and duplicated ratio, the tested single-plane EUROSEM output remains EROD- and leafdrip-insensitive, while transport formulation changes sediment totals. In-solver trace isolates supply vs output: **flow transport/source dominance in this synthetic test**. Unit handling in `SED` needs systematic dimensional derivation, not ad hoc width correction.

**Go/no-go**
- EUROSEM only **reinstated as subject of validated quantitative canopy physics and 1D process research audit**, not accepted as Gounsa full spatial 2D runoff-erosion engine.
- To accept its reported yield as scientific Gounsa result, independently reconstruct event gross detachment, deposited material, suspended storage, boundary export; enforce finite soil thickness, dt convergence, tested native process input with field rainfall, and 2D geomorphic requirements separately. No independent sediment mass closure here.
- No root RLD effect native; no localized stemflow injection; 1D linked hillslopes and pre-specified rills cannot satisfy fully spatial 2D original user requirement.
- Most important next original process fix is native sediment book-keeping + state-separating splash vs hydraulic detachment under matched real site soil, *not* force rank Miscanthus > oak by tuning coefficients.

## Direct primary sources
- [Morgan et al. 1998 publication](https://www.researchgate.net/publication/233426022_The_EUROSEM_model)
- [Native source and original sample](https://github.com/TheSoilman/EUROSEM)
- [Former LAI extension branch](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/eurosem-single-model-lai-20261025)
- [Today's native 20 run matrix](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40322591668)
- [Today's internal RDET/sediment transport source trace](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40323173111)
- [Today's 8 width source dimensional experiment](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40323570418)
