# 고운사 유수침식 주 엔진 strict screening handoff (2026-10-26)

## 사용자 최우선 원칙
'의심이 되면 버려' — 공개 원본 소스, native quantitative LAI canopy interception/storage/throughfall and ideally leafdrip, actual surface runoff-driven erosion, genuine 2D, mountains/steep applicability. After source gates, independent sediment/time-step convergence, finite soil stock, outlet, water/sediment ledgers. Ambiguity/failure **not pass**. Do not call published source math implemented native if not coded.

## Confirmed this session
1. TREX full C original **actually found** GitHub mirror `WatershedModels/trex_src_csu`, SHA `5cfe714557333ecf8062ac04b5fba3165906a775`, root `src` 233 entries, README indicates CSU v101017 copy 2018-05-18. Read `Interception-r4.c` fixed available interception depth, `OverlandSolidsErosion.c` available sediment cap, `OverlandWaterRoute-r3.c` 2D grid face. No source verified LAI dynamic canopy or leafdrip KE; repository search throughfall/drip/splash/raindrop empty. **REJECT native Gounsa main model**.
2. Iber+ 2024 Cea paper DOI 10.1016/j.envsoft.2024.106098 published genuine multiclass 2D raindrop/runoff erosion. Crucial primary source Fernández-Nóvoa et al. NHESS 24:609–630 (2024) https://nhess.copernicus.org/articles/24/609/2024/nhess-24-609-2024.html, Code/Data availability **source only for collaborators**, freely distributed executables. DOI 10.57745/UFEK4L solely binary Windows/Linux. Native LAI canopy erosion integration also unverified. **REJECT main open-source engine**, scientific benchmark papers optional.
3. ASTERIX: 2025 Ion et al. *Environmental Modelling & Software* 186, 106336 DOI 10.1016/j.envsoft.2025.106336 publishes free 2D vegetation-porosity **water flow module**. Authors 2024 Future Extensions expressly state **canopy interception not implemented and Hairsine-Rose sediment module not yet added** (https://www.researchgate.net/publication/381652990_ASTERIX_Module_for_modelling_the_water_flow_on_vegetated_hillslopes). Distinct 2024 Ion et al. arxiv:2408.12465 *math erosion paper* cannot be represented as compiled water+canopy+sediment original. **REJECT**.
4. Additional quick-screen exclusions from existing records: WEPP forest LAI + physical erosion but hillslope 1D, WaTEM/SEDEM RUSLE and spatial routing not event 2D, SMODERP2D intercepted rain map but no source-verified sediment advection, SHETRAN published canopy+sheet but rill/DEM/observed sediment shortcomings; OpenLISEM 7.5.2 original Windows 2D and finite sediment stock + dt validation **FAIL**, no reinstatement.

## Files actually saved
- `papers/2025_Ion_ASTERIX_2D_VegetatedFlow.md` NEW
- `papers/2024_Ion_VegetatedHillslope_HairsineRose_Erosion.md` NEW
- `papers/2008_Velleux_England_Julien_TREX_2D.md` UPDATED
- `models/TREX.md`, `models/Iber.md` UPDATED
- `decisions/2026-10-26_STRICT_REJECTION_TREX_IBER_ASTERIX.md` NEW
- `decisions/2026-10-26_POST_OPENLISEM_CANDIDATE_SOURCE_SCREENING.md` UPDATED with withdrawal
- `MASTER.md` UPDATED, `INDEX.md` REGENERATED 434/84/62 file counts.

## Final verified verdict
**No single unmodified openly editable native engine discovered that meets every required process. No new build/time-step numerical run claimed this session.** This is bounded to searched sources, not universal impossibility. Avoid cycling previously rejected choices. Do not silently couple models as if original one. Future only source-screen candidates with actual native source/LAI and erosion, then build with identical native source and run water/soil/2D time-step convergence gate. Otherwise explicitly state no passing model.
