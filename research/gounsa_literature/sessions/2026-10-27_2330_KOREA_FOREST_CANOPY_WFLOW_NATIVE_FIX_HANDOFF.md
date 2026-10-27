# 2026-10-27 23:30 비LISEM 후속 인계

## User request
계속 찾기. OpenLISEM original assigned another Work, so this investigation strictly excludes that engine's debugging. Need published original same-source original model with 0.05–0.10m actual computational pixels, quantitative LAI interception, real drop/direct rain + runoff erosion, independent free X/Y 2D hydrodynamics and local sediment deposition, matching publicly executable code.

## New verified items
1. 2009 J.K. Kim, D.Y.Yang, M.S.Kim & Y.Onda, J-STAGE doi10.3178/hrl.3.36, natural-rain Korean Anseong forest canopy-under/open 0.18m² soil-loss plots at 10/20/30°. Interrill soil erosion lower under canopy, rainfall threshold/throughfall saturation. 2009 paper is observation, not numerical solver.
2. 2016 Thompson/Davis/Oliphant, ESPL DOI10.1002/esp.3881, author 9-page PDF screenshot p2/p6, 8 oak/eucalyptus paired plots in California including sandstone/shale forest, mean oak litter5cm vs eucalyptus10cm, Jan2008 oak sediment greater (p0.019 ANOVA); paired observations cannot isolate canopy from litter. R data repo `iGISc/iGIScData/data/tidy_eucoak.rda` is accessible, 180 × 12 including rain_subcanopy, runoff_L, no sediment mass. Native 5cm numerical grid has **nothing** to do with reported litter depth.
3. Major upstream native regression in existing open Wflow.jl (not new model) PR #939 merged 2026-06-15, tag v1.0.3 June23: pre-fix `KE × 0.001` incorrectly multiplied and original depth in m without converting to mm for EUROSEM shielding; after patch corrected. Original included tests at one grid rainfall erosion 0.012323→12.323 tonnes/cell??? **Do not invent units for test amount**, code defines amount with ton/cell but source test only. Upstream test reported 1000× in one case, not generic whole model. Wflow transport still directed network, no free-X/Y sediment.
4. Existing full-2D polygon SRH-2D Lai2020, 2026 MDPI Braga SERGHEI-SE, Iber+2024, tRIBS-FEaST2013 rediscovered but present in archive and no all-pass with same source canopy/5cm.

## New file records
- `papers/2009_Kim_Yang_Kim_Onda_Korean_Forest_Canopy_Interrill_Erosion.md`
- `papers/2016_Thompson_Davis_Oliphant_Oak_Eucalyptus_Litter_Soil_Erosion_Field.md`
- `models/Wflow_Sediment.md` canonical updated (not duplicated)
- `decisions/2026-10-27_2330_KOREA_CANOPY_FIELD_AND_WFLOW_EUROSEM_SOURCE_REGRESSION_SCREEN.md`
- this session
- update INDEX and MASTER after.

## Verdict
No newly verified truly existing published cm free2D native canopy+sediment open solver. Publish genuinely new Korean forest undercanopy validation material and upstream code fix for Wflow; do not call either new operational native engine.
