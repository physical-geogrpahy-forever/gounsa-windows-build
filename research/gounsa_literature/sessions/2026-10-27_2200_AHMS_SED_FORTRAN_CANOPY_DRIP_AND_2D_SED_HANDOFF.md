# 2026-10-27 22:00 Independent non-LISEM model original-source audit handoff

## User constraint and existing exclusions
OpenLISEM code/numerical debugging delegated to separate Work. Primary user scientific criteria: published actual 5–10cm numerical model, measured LAI native interception/throughfall/drip, direct+runoff erosion and local deposition, truly free XY 2D SWE, a *single published original* with matching public source. Do not conflate open original code vs code proven under actual paper's configuration.

## New high-confidence research
2025 Jiang et al JAMES AHMS-SED DOI10.1029/2024MS004593 public current Fortran https://github.com/JiangCong1990/AHMS-SED, archived v1 DOI10.5281/zenodo.14494932, published observed+input+output DOI10.5281/zenodo.14983610. 20km and 1h actual simulation.
`NoahMP/Noah/module_sf_noahmplsm.f`: `CANWATER` L7063–72 uses LAI+SAI with plant coefficient to compute `MAXLIQ`, canopy QINTR, QDRIPR and QTHROR. `CALL EROSION` L1200–03. `EROSION` L9719–31 branch option4 physically distinguishes leafdrip and directfall kinetic energy (EUROSEM-like) for rainfall detachment. `Run/namelist.hrldas` published repo example `erosion_option=1` **not option4**; no claim paper selected 4.
`Routing/module_rt_rt2d.F` L1821–48 routes 8 neighbor multi-fraction erosion/deposition; L5453 `FBARE=exp(-0.52*LAI)` in USLE C-factor. Implicit surface-head flow, NOT true momentum 2D SWE.
`Routing/module_rt_sed2d.F` is **a nonwired incomplete EUROSEM leafdrip draft**; Routing/Makefile doesn't include it, active routing doesn't call rt_sed. No cm validation.
Original code fully read on GitHub connector, no build/run on this session.

## Files created
- papers/2025_Jiang_Parteli_Shao_AHMS_SED_Yellow_River_Open_Source.md
- models/AHMS_SED_2025_NOAHMP_CASC2D_NATIVE_CANOPY_SEDIMENT_AUDIT.md
- decisions/2026-10-27_2200_NONLISEM_AHMS_SED_SOURCE_ACTIVE_CANOPY_KINETIC_NO_GO.md
- sessions/2026-10-27_2200_AHMS_SED_FORTRAN_CANOPY_DRIP_AND_2D_SED_HANDOFF.md
- Updated MASTER/INDEX as commits. Avoid duplicates in following chats.

## Conclusion
**Research advance**: publicly archived integrated canopy-water and original leafdrip rain-splash pathway + multidirectional sediment code exists, countering overly broad 'no canopy erosion source' claim. **Fails actual published ≤10cm and strict SWE, sample option4 not selected**; cannot be operational gounsa main.

## 2026-10-27 22:05 후속 논문: Juez et al. (2018) full 2D SWE + HEM
- [원문 검토](../papers/2018_Juez_Tena_FernandezPato_2D_SWE_HEM_Algars_Erosion.md): DOI 10.18172/cig.3320, 저자 실제 2D **dynamic Saint-Venant** (triangular finite volume) + cellwise SCS + 2D extended HEM for rainstorm erosion. 419km2 Algars catchment 158000 triangular elements **min AREA 150m2, max AREA 600m2** (published §4.1), *not* 5cm/10cm grid.
- **Crucial exact limitation from full paper §4.3**: author explicitly says **sediment depositional processes that change local topography are NOT included in the erosion source term**, so one cannot call native model spatial deposition/morphodynamic feedback complete. No LAI interception or leafdrip active, exact public simulation source package not verified. Note 2017 abstract proposed future RiverFlow2D, but exact 2018 executable provenance unconfirmed.
- Model calibration on event1 runoff/sedigraph with trade-offs 2% sediment cumulative but 30% peak error vs event2 12% volume 40% peak for fitted alternative. Not independent field prediction. Valid hydraulic benchmark only, **strict stand-alone FAIL**.
