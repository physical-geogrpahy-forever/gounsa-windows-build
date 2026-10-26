# 2026-10-26 OpenLISEM 7.5.2 NO-GO 후 대체 유수침식 원본 소스 조사 인계

## 확정된 이전 결론
- OpenLISEM 7.5.2 원본 Windows native 12건 2D water/sediment QA: 2026-10-26 time-step erosion nonconvergence; main Gounsa engine discarded. Full actual QA in `decisions/2026-10-26_OPENLISEM_752_NATIVE_2D_STABILITY_FAILED.md`.
- SHETRAN 4.7.2 original Fortran has Rutter-like canopy and leafdrip and 4-face flow detachment, but no autonomous incised rill/DEM feedback, weak field sediment performance, native BALSED stub; its previous `decisions/2026-10-26_SHETRAN_FIT_FOR_PURPOSE_REASSESSMENT.md` excludes main Gounsa rill engine. DO NOT recommend it as solved after this session.
- SWEHR published 2016 vs publicly available 2017 source mismatch: native Rutter canopy+shielding unverified and former 38 cases were modified fork. Do not restore to selected original.

## Today newly checked
- **DHSVM Doten(2006):** Published forest mountain rainfall+leafdrip+surface-flow erosion. But official PNNL GitHub downloadable source tree `DHSVM/sourcecode` does NOT include this sediment module, and hydrology D4/D8/kinematic not full 2D SWE. Paper-only reference.
- **TREX:** Colorado State 2008 Velleux/England/Julien 2D overland watershed erosion model; website advertises C source & sediment example ZIP, and references actual forest Fukushima/Naesung Korea studies. **No retrieved original source ZIP and no native LAI-driven interception/drip equation confirmed**, cannot mark as complete native match.
- **Iber+ 2024 Cea et al:** actual verified published lab Pradel hillslope + Galabre French Alps 20km2 + full 2D SWE/exner/multiclass erosion; **research dataset DOI 10.57745/UFEK4L hosts Windows/Linux V3.2b executable**, but full original source and native LAI-throughfall/drip unconfirmed. Quantitative vegetation coupling remains a new process, not existing model.
- **SMODERP2D:** Open Python does have `core/vegetation.py` ppl 'LAI' and rainfall interception `ppl*rain` capped by pi, but reviewed source `processes/` lacks complete sediment continuity, actual rain-impact/runoff detachment, sediment advection. Erosion control hydro model, NOT a passed sediment mass engine.
- **SPHY:** native six sediment algorithms but 1-day timestep and routing `FlowDir`, not genuine 2D.
- **GSSHA:** 2D hydro & sediment + simple canopy interception, but native LAI/leafdrip and complete original source not verified.

## Files saved this session
- `papers/2006_Doten_DHSVM_Mountain_Forest_Sediment.md`
- `papers/2008_Velleux_England_Julien_TREX_2D.md`
- `models/TREX.md`
- `decisions/2026-10-26_POST_OPENLISEM_CANDIDATE_SOURCE_SCREENING.md`
- MASTER/INDEX regenerated.

## Near-term go/no-go order
1. TREX exact downloadable original model archive + matching original Sediment example. Read C source for native LAI, dynamic canopy storage/leafdrip and canopy protection. If absent, immediately exclude from 'single complete engine' without 2-day compile.
2. Iber+ original V3.2b executable official scientific input and field measured output test; confirm executable runs and erosion dt/grid convergence. If a model itself lacks native LAI canopy, no claim 'complete model' (if necessary test external canopy -> rainfall source carefully and label NEW coupling).
3. Broader source search for original complete LAI interception + genuine 2D erosion/raindrop/flow model in mountain forest remains unresolved.

## Important source URLs
- https://github.com/pnnl/DHSVM-PNNL
- https://www.engr.colostate.edu/~pierre/ce_old/Projects/TREX%20Web%20Pages/TREX-Overview.html
- https://www.engr.colostate.edu/~pierre/ce_old/Projects/TREX%20Web%20Pages/TREX-Research.html
- https://doi.org/10.57745/UFEK4L
- https://doi.org/10.1016/j.envsoft.2024.106098
- https://github.com/storm-fsv-cvut/smoderp2d
- https://github.com/nclwater/Shetran
