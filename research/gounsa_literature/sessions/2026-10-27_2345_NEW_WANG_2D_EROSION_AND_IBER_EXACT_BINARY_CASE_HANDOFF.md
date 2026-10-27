# 2026-10-27 23:45 계속 찾기: 독립 2D Wang 논문 + published Iber 원본 재현패키지 구별

## 작업 출발
`research/gounsa_literature/SYSTEM.md` `MASTER.md` `INDEX.md` latest decisions 읽고 중복 검사. 현재 user 고운사 요구: published actual grid 5–10cm, genuine 2D freely XY, LAI-based canopy interception + direct/leafdrip rain KE, rain/overland flow detachment + local deposition and original code matching exact same study. OpenLISEM 별도 Work 소관.

## 새 논문
- **Wang et al 2023, CATENA232:107387 DOI10.1016/j.catena.2023.107387** new `papers/2023_Wang_Hou_Catena_TwoDimensional_Loess_Slope_Erosion.md`. Authentic 2D numerical loess hillslope rainfall + sediment carrying formula calibrated from experiments + mapping of internal sediment source. 2022 EGU precursor DOI10.5194/egusphere-egu22-1885 includes runoff NSE0.83 / sediment NSE0.66 / runoff and sediment R2 0.89/0.73 / relative bias -5.02/-1.02. **EGU precusor not final 2023 independent holdout accuracy**. Exact run mesh spacing and LAI canopy equations unavailable in paper abstract; full article restricted, no same original source found. Related GPL HiPIMS open water code is not proof of author's erosion solver released.

## Existing canonical paper sharpened after reading whole Wiley journal text
- `papers/2012_Cooper_Wainwright_MAHLERAN_MiC_30cm_Interception_Drip.md`: original explicitly says **interception losses, leafdrip and throughfall rain kinetic energy scaling when vegetation present**, but actual bare sand 13.75×6.5m 0.3m computational grid 60mm/h×20min. **Kinematic cardinal-steepest-descent water**, not free XY SWE, even though sediment markers move within grid stochastically. Upper sand depth0.05m is soil layer not grid Δx. Spatial 137Cs tracer model NSE0.98, outlet hydrograph NSE0.93 and 580L vs534L (9% mismatch) strong process benchmark but doesn't prove canopy test/native5cm. Paper DOI10.1029/2012JF002499. Existing canonical only edited, not new duplicate.

## Previously archived model updated with exact published runnable original (binary, not editable source)
- `models/Iber.md` new five author-deposited DOIs with 2024 Cea erosion test matching Windows and Linux Iber+ V3.2b executable:
 `10.57745/UFEK4L` executable; `10.57745/2WH9AL` T1 5cm longitudinal × **2m transverse** quasi1D; `10.57745/J2A44Q` T2 Pradel ~120m²/3300 cells characteristic sqrt(mean area)0.19m, not claimed min Δx; `10.57745/NOHRHJ` Galabre mountainous 20km²; `10.57745/VFBGFR` Ullion sediment deposition. Open exact binaries/datasets are scientific advance in reproducibility, **but underlying CUDA/C++ source is collaborator-only**, native LAI canopy and leafdrip unavailable. Doesn't meet user's all conditions.

## Decision
`decisions/2026-10-27_2345_WANG_2023_SLOPE_EROSION_AND_IBER_EXACT_BENCHMARK_CODE_GATE.md`: no all-PASS; exact original Iber test assets can be used as numerical benchmark reference, not as Gounsa main.
## Archive operations
One new paper and one new decision, 2 canonical edits, add to MASTER/INDEX, save this handoff. Before session count papers496, models103, decisions100, likely after paper497, decision101.
## Next tight priority
Only find **actual published canopy ON/ OFF in physically 2D erosion at ~10cm with full code**, otherwise don't overpromise or repeat known failed SHETRAN 5cm extrapolation. Scientific user wants existing model, not hypothetical new coupling.
