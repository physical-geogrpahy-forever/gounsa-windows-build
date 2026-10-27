# 2026-10-28 심층검증 인계: 4대 단일 레퍼런스 통합모델

## 이번 턴 수행
- Original Kim2013 WRR full publisher Methods §§2,4.1,4.2,4.3, Table5 / Maggioli2022 Frontiers full Methods and calibration / Wei2017 author-hosted paper PDF text Methods §§3,4 / Long-He2010 original indexed abstract and 2017 next paper citation / Feng2026 WRR Methods and Zenodo source release.
- GitHub direct native trees and selected source lines for official tRIBS, vjetten/openlisem main_C, historic WatershedModels TREX, RDycore.
- 2017 Wei PDF screenshot requested but host returned 403; extractable original PDF text inspected, no claim of visual figure inspection. No native full code compilation or new simulation.
- Newly created decisions/2026-10-28_SINGLE_REFERENCE_4_CORE_MODELS_PRIMARY_PAPER_NATIVE_SOURCE_REAUDIT.md and models/RDycore.md; updated MASTER.md and regenerated INDEX.md.

## Core outcome
1) tRIBS-FEaST single 2013 paper does combine 3 engines; smallest 0.005m2 1D practical tests disable tRIBS hydrology; Lucky Hills true full 2D 5.56m2 min triangular element, canopy params Table5 Rutter, vegetation study uses Ksat and Manning rather than canopy-only intervention. Current tRIBS has no HairsineRose native exact code.
2) Maggioli 2022 5cm LISEM+LAI canopy is real. Published routine kinematic, 18 rainfall events and TLS initial/end, no isolated canopy ON/OFF. 7.5.2 native 5m timestep/soil-stock fail per older recorded 12-run QA, Work handles debug separately.
3) Long & He 2010 Gash+2D SWE+GreenAmpt+erosion/deposition+bed evolution confirmed abstract; exact computational mesh and original public solver not verified. 2017 GPU CA is different.
4) Wei 2017 author PDF exact diffusive wave XY and separate splash/flow net sediment, canopy interception named native hydrology; actual model 90m and canopy leafdrip KE not shown; old TREX archived C not exact modified forest code.
5) Feng2026 multi-engine single-ref qualifies but sediment source Se included in GAIA water-column only; Exner changes D-E, not upland Se hence hillslope DEM not eroded dynamically in that coupling. Actual30m, author source metadata8.2GB.
6) New RDycore code is a separate 2D SWE+sediment tracer with active shear-based Partheniades e/d, but its published HR theoretical documentation != native rainfall/flow/loose layer bed implementation; canopy not proven.

## Unresolved and next validation
- Matching author FEaST integrated code release and original field inputs nonexistent in found public GitHub (absence bounded to checked sources).
- Matching published 2010 Long/He code and mesh unknown.
- Modified Wei2017 source package unknown.
- Classic OpenLISEM numerical native full 5–10cm time/soil conservation remains separate Work.
- No complete production engine is yet approved for all same-native paper/source+5cm freely-XY canopy impact + sediment mass/bed tests.

## Updated files
- decisions/2026-10-28_SINGLE_REFERENCE_4_CORE_MODELS_PRIMARY_PAPER_NATIVE_SOURCE_REAUDIT.md
- models/RDycore.md
- MASTER.md
- INDEX.md
