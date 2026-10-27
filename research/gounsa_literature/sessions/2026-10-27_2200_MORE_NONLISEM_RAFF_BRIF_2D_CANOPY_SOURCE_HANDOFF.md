# 2026-10-27 22:00 다른 논문 추가 탐색 인계 — Raff2005 full2D + Wang2025 BRIF forest interception CUDA

## 독립 업무
사용자 요청: OpenLISEM은 Work에 맡기고 본 대화는 계속 다른 published model 찾기. 기존 Gounsa `SYSTEM.md`, `MASTER.md`, `INDEX.md`, PSEM_2D, Wflow_Sediment, GRASS SimWe, CAESAR-Lisflood, 2026 Braga SERGHEI-SE, 2010 Waldmann PROMET, TREX Wei2017, GSSHA/CASC2D provenance 체크.

## 신규 발견
1. Raff & Ramírez 2005 DOI10.1002/fld.1016 official Wiley peer-reviewed: true 2D SWE + vertical 1D Richards + sediment transport/erosion in same original method, small slope; cannot establish 5/10cm Δx, canopy LAI or open compiled source. Related Ramírez & Raff 2003 project synopsis notes bare/vegetated *soil* patch boundary but not rainfall interception. Github code searches exact title/author no originals.
2. Wang et al. (2025) DOI10.1029/2024EA004076 **BRIF** CPU/GPU 2D local inertia + forest LAI canopy + infiltration, steep Cutou forest 22km2. Published **2.5m native flood simulation 6.32 million cells** 18–24h, Vcatchment1m, other basin8m. 0.3m UAV DEM is survey input only, LAI remote-sensing resolution500m. **NO erosion/sediment/deposition solver**. Partial official CUDA code https://github.com/chinafl/HFDM-GPU and Zenodo DOI10.5281/zenodo.15613301: `test/wind_cuda.cu` actual canopy Smax(LAI) functions and K=1-exp(-Cover×LAI), `test/windmath_cuda.cuh` declares Diff_interception but implementation `windmath_cuda.cu` absent from repo tree. Root `hfdm` binary, not source. So not full source package; do not claim source fully public or code built.
3. Already archived 2010 Waldmann PROMET erosion and 2026 Braga SERGHEI-SE new papers found during search; avoid second papers (existing `papers/2010_Waldmann_PROMET_Large_Scale_Erosion.md` and `papers/2026_Braga_SERGHEI_SE_Finite_Volume_Evaluation.md`).

## Repository writes
- `papers/2005_Raff_Ramirez_Fully_Coupled_2D_Hillslope_Hydrology_Erosion.md`
- `papers/2025_Wang_Ouyang_An_BRIF_2D_Mountain_Interception_Flash_Flood.md`
- `papers/2003_Ramirez_Raff_Evolution_Landscapes_Hillslopes_Project_Synopsis.md`
- `models/BRIF_HFDM_GPU_2025_LAI_2D_Interception_No_Sediment_Code_Audit.md`
- `decisions/2026-10-27_2200_NONLISEM_FURTHER_RAFF_BRIF_SOURCE_REAL_CELL_SCREEN.md`
- `INDEX.md` updated counts now 494 papers,103 models,99 decisions; concurrent Work touched inventory earlier, do not hardcode counts blindly.

## Scientific verdict
**No new all-pass** 5–10cm true free2D rainfall-splash+flow erosion with LAI canopy and local deposition in published reproducible original; new Raff true 2D flow and erosion but canopy/source unknown, new BRIF verified LAI and mountainous open reference but only water and 2.5m. Original physics, published applied mesh, full distributable source are separate evidence tiers.

## Next strict search
Focus case reported actual ≤0.1m *native computation*, and DOI of complete matching software test branch. Avoid another unconstrained list of models. OpenLISEM excluded; separate Work owns numerical repair.
