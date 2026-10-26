# 2026-10-26 엄격한 원본 모형 탈락 판정 — TREX, Iber+, ASTERIX

## 판정 원칙
사용자 지시: **"의심이 되면 버려"**. 이에 따라 모델의 원본 공개, LAI-driven interception (canopy storage + throughfall; leaf drip KE important), explicit rain-and-overland runoff erosion, genuine 2D mountain suitability, finite soil stock/mass and numerical stability를 통과할 때만 고운사 유수침식 주 모형에 올린다. 원본 없음/필요 프로세스 부재/버전 불일치/과거 numeric FAIL를 모델명이나 논문 권위로 우회하지 않는다.

## 1. TREX: definitively exclude
- Colorado State University official page says C source and watershed examples available, but some official web fetches 403. **New independent CSU source mirror identified and read**: `WatershedModels/trex_src_csu`, repo README specifically says CSU TREX source version `101017`, updated 2018-05-18, pinned repository head `5cfe714557333ecf8062ac04b5fba3165906a775`. `src` directory has 233 files (not all are C files).
- `src/Interception-r4.c` native code: remaining `interceptiondepth` [m] is subtracted from `grossrainrate*dt`; `netrainrate = grossrainrate - interceptiondepth/dt` for rainfall > remaining interception. No dynamic LAI-driven storage capacity, evap, drip or throughfall partition. It's a prescribed depth capacity, not active plant biophysics.
- `src/OverlandWaterRoute-r3.c` 2D grid-face flow; `src/OverlandSolidsErosion.c` physically explicit overland shear/transport capacity, and **`available` cap limits removal to finite sediment stock**, which is a concrete strength versus OpenLISEM 7.5.2. Does not rescue absent canopy physics.
- GitHub indexed full repository code search: `throughfall`, `drip`, `raindrop`, `splash` absent, `canopy` only solar radiation comment. No observed proof dynamic plant LAI drip impact.
- Mirror has no recognized LICENSE metadata: publicly viewable C ≠ independently confirmed rights for redistributed/open-source integration. User's GPL source requirement unverified.
- **REJECT** full standalone Gounsa engine. Stop source build; physical key criterion fails before numerical gate. No assertion original published model invalid for its other applications.

## 2. Iber+: definitively exclude as fully open native all-in-one
- Published Cea et al. 2024 `Environmental Modelling & Software` DOI 10.1016/j.envsoft.2024.106098: authentic 2D SWE finite-volume multiclass raindrop/runoff erosion, shielding, deposition and published mountainous Galabre, Pradel. Good numerical theory but native LAI/canopy+leafdrip is not established.
- 2024 Fernández-Nóvoa et al., `Natural Hazards and Earth System Sciences` 24, 609–630, **Code and data availability** explicitly states executable is public, **model source only available to collaborators**. https://nhess.copernicus.org/articles/24/609/2024/nhess-24-609-2024.html.
- [Iber+ V3.2b dataset](https://doi.org/10.57745/UFEK4L) explicitly includes **Windows/Linux executable archive** only, not source. 2024 journal's "software openly available" includes this binary and data, must not be mistaken for complete open C/CUDA source.
- **REJECT** strict fully open-source dynamic canopy+2D erosion Gounsa native engine. Do not spend time calibrating closed engine and claim reproducible editable original.

## 3. ASTERIX: reject integrated erosion-canopy edition
- Ion, Marinescu, Cruceanu 2025 *Environmental Modelling & Software* 186, 106336, DOI 10.1016/j.envsoft.2025.106336: open-source 2D extended Saint-Venant **water flow** module with vegetation porosity and plant drag.
- Their original 2024 *ASTERIX water flow module* technical paper *Future Extensions* explicitly says **water infiltration and canopy interception NOT implemented**, and Hairsine-Rose erosion/sediment module still in preparation (not integrated into published flow software). Authored text: https://www.researchgate.net/publication/381652990_ASTERIX_Module_for_modelling_the_water_flow_on_vegetated_hillslopes (Future Extensions).
- 2024 authors' separate preprint https://arxiv.org/abs/2408.12465 discusses extended Saint-Venant plus Hairsine-Rose and numerical erosion experiments, but **is not proof that public 2025 ASTERIX_flow_2D.tar.xz has that erosion module**. 2025 paper speaks only flow; no matching full erosion source verified.
- No LAI-driven canopy storage, throughfall and leafdrip KE in proven edition. Vegetation porosity != LAI.
- **REJECT** from fully integrated main engine selection.

## Prior fixed rejects (do not reopen without materially new evidence)
- **OpenLISEM 7.5.2** original Windows 2D numerical failure on 2026-10-26: dt 5/10/20s orders-of-magnitude sediment export, finite column issue; canonical file `2026-10-26_OPENLISEM_752_NATIVE_2D_STABILITY_FAILED.md`. No source upgrade proof.
- **SHETRAN 4.7.2** original Fortran canopy+rain/leafdrip+sheet erosion, but no true self-forming rills, no integrated hillslope morphodynamic feedback, limited field erosion accuracy and `BALSED` stub: file `2026-10-26_SHETRAN_FIT_FOR_PURPOSE_REASSESSMENT.md`; retain as science auxiliary only, not Gounsa main.
- **SWEHR 2017 original C** 2016 reported Rutter dynamic canopy native absent; custom 38 tests = modified fork, cannot represent native original.
- **DHSVM/Doten 2006** canopy and mountain published rain/runoff detachment but official PNNL source does not include sediment model and hydrological routing not 2D dynamic SWE.
- **SMODERP2D** LAI interception code but no verified sediment advection or physically separate rain and flow detachment source.
- **EUROSEM** physics-based hillslope erosion but not genuine 2D shallow-water erosion source.
- **WEPP** established LAI vegetation+forest erosion but hillslope 1D profile and watershed network, not genuine 2D spatial surface flow.
- **WaTEM/SEDEM** openly licensed code but RUSLE-style average erosion + DEM-routing, not event-resolved native rain/flow separation or LAI canopy.
- **FeST/ERODE** paper alpine forest water + erosion model, but rain splash in overland cells/shear channel, raster RUSLE-style and source availability/2D dynamic wave not proven; no recommendation as strict native model.

## Present conclusion
**NONE OF THE INVESTIGATED UNMODIFIED PUBLICLY REPRODUCIBLE INTEGRATED MODELS PASS ALL MANDATORY CONDITIONS.** This is a bounded negative finding based on listed models, **not a universal theorem** about every simulation code. No model automatically promoted. To proceed scientifically, either relax *one explicitly identified* criterion (not implicitly) or implement and independently validate an **honestly named new coupling** between source-verifiable canopy and source-verifiable 2D erosion engines. Prefer not to relax quantitative canopy and no hiding instability. Need original trusted engine numerical stability before coupling.

## Evidence URLs
- https://github.com/WatershedModels/trex_src_csu/tree/5cfe714557333ecf8062ac04b5fba3165906a775/src
- https://nhess.copernicus.org/articles/24/609/2024/nhess-24-609-2024.html
- https://doi.org/10.57745/UFEK4L
- https://www.sciencedirect.com/science/article/pii/S1364815225000209
- https://www.researchgate.net/publication/381652990_ASTERIX_Module_for_modelling_the_water_flow_on_vegetated_hillslopes
- https://arxiv.org/abs/2408.12465
