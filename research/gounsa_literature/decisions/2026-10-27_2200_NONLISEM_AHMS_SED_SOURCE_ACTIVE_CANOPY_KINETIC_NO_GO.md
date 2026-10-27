# 2026-10-27 22:00 Independent original-code study — AHMS-SED 2025, select native canopy option, 20km resolution limits

## Decision
OpenLISEM left for Work and not inspected here. New genuinely public source **Jiang et al. (2025) AHMS-SED** found: https://doi.org/10.1029/2024MS004593, original repo https://github.com/JiangCong1990/AHMS-SED, model archive DOI 10.5281/zenodo.14494932, **paper's own complete input/output Zenodo 10.5281/zenodo.14983610**.
True native Noah-MP `CANWATER` directly gives direct-throughfall QTHROR and leaf QDRIPR, called by native `EROSION` (option4) with separate KE and rainy detachment. Its 2D routing has native class sediment exchange, deposition, 8-neighbor flux.

## Why not Gounsa 5/10cm
Actual published **20km, 3600s** simulation and use of 30m DEM is only terrain preprocessing. Routing `Routing/module_rt_rt2d.F` is implicit water surface-gradient neighborhood solver, not full 2D SWE X/Y momentum. Current `Run/namelist.hrldas` example `erosion_option=1` (USLE), not original active leaf-drip `OPT_ERO=4`; direct author-config of published 2025 experiment still unverified. `module_rt_sed2d.F` has appealing EUROSEM source but is **not compiled** in `Routing/Makefile` and is not runtime-called. The actual native NoahMP `EROSION` case4 is separately in compile path. No 5cm or oak/grass event test, no 5cm numerical stability proof, no local field erosion/deposit DoD evidence.
Current code blob source trace:
- NoahMP `module_sf_noahmplsm.f` SHA `ad5ea8eba279f98463589f322cc7fd95faaebb1f`, L7061–72, L1198–1203, L9624–9781.
- Routing `module_rt_rt2d.F` SHA `a51aa6748f6b65ba8a7bea976f8185a22fe610c9` L1820–49 and L5453–5500.
- Nonwired draft `Routing/module_rt_sed2d.F` SHA `73126ffbc63c2f5d087ed5073bf2c5bba3ac815b`, `Routing/Makefile` excludes it.

## Distinguish processes carefully
- Native LAI canopy storage and direct/leaf drip water partition **confirmed as source**.
- Native EUROSEM-like raindrop splash (under OPT_ERO=4) **confirmed as callable source**.
- `DETFLOW=0` in NoahMP EROSION; **flow-driven erosion** is handled separately via `RoutSedOvrl` + `KRcap`, using LAI-derived C-factor; need prove same model run source flux additivity.
- `QDRIPR/QTHROR` names do not prove dynamic canopy output actually selected by full paper config.
- Public native source and paper inputs is not equivalent to 5–10cm demonstrated/stable.

## Verdict and actionable scholarly value
**Retain as an independently documented, fully open non-LISEM research model containing an optional physically based canopy-drip rain detachment plus 2D grid sediment architecture; reject for high-resolution strict main model**. Not just an arbitrary high-level model list: physical equations and active compilation flags actually audited.
- [Paper canonical](../papers/2025_Jiang_Parteli_Shao_AHMS_SED_Yellow_River_Open_Source.md)
- [Code audit](../models/AHMS_SED_2025_NOAHMP_CASC2D_NATIVE_CANOPY_SEDIMENT_AUDIT.md)

## Other-branch prior rejects maintained
- Iber+2024 public executable but solver source collaborator-only and canopy not built/tested. 5cm lab test is one-cell-wide quasi-1D 6m flume; not native 5cm fully lateral 2D validation. Paper https://doi.org/10.1016/j.envsoft.2024.106098.
- PSEM_2D2005 free lateral flow + erosion but canopy missing and exact public source absent.
- SHETRAN 4m model attempts not published cm precedent; 7.5.2 LISEM numerical issues delegated Work.

## Next
Search actual published ≤10cm plot vegetation+free2D+sediment with publicly archived same version; no all-pass as of this decision.

## 2026-10-27 22:05 후속 논문: Juez et al. (2018) full 2D SWE + HEM
- [원문 검토](../papers/2018_Juez_Tena_FernandezPato_2D_SWE_HEM_Algars_Erosion.md): DOI 10.18172/cig.3320, 저자 실제 2D **dynamic Saint-Venant** (triangular finite volume) + cellwise SCS + 2D extended HEM for rainstorm erosion. 419km2 Algars catchment 158000 triangular elements **min AREA 150m2, max AREA 600m2** (published §4.1), *not* 5cm/10cm grid.
- **Crucial exact limitation from full paper §4.3**: author explicitly says **sediment depositional processes that change local topography are NOT included in the erosion source term**, so one cannot call native model spatial deposition/morphodynamic feedback complete. No LAI interception or leafdrip active, exact public simulation source package not verified. Note 2017 abstract proposed future RiverFlow2D, but exact 2018 executable provenance unconfirmed.
- Model calibration on event1 runoff/sedigraph with trade-offs 2% sediment cumulative but 30% peak error vs event2 12% volume 40% peak for fitted alternative. Not independent field prediction. Valid hydraulic benchmark only, **strict stand-alone FAIL**.
