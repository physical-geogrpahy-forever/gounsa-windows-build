# TREX: Two-Dimensional Runoff, Erosion and Export

## 2026-10-26 current audit
Identity: original Colorado State University Velleux / England / Julien 2008, event-scale 2D overland / 1D stream, rain-on-grid, interception as equivalent depth, infiltration, distributed erosion deposition and bed-elevation adjustment. Original development from CASC2D.

## Native candidate status
- Source: [official TREX site](https://www.engr.colostate.edu/~pierre/ce_old/Projects/TREX%20Web%20Pages/TREX-Home.html) advertises complete source and hydrology/sediment example ZIP but actual original C source archive download/contents **not yet independently verified** (403 on web view, no source fetched into runtime).
- Numerics: actual source numerical stability and mass balance **NOT TESTED**. Do not repeat OpenLISEM error of recommending on model-paper features only.
- Genuine 2D: yes in published overland flow, but source numerical routing kind must be read prior to claiming full 2D dynamic SWE.
- Native LAI dynamic canopy and leaf drip impact: **UNCONFIRMED / NOT ESTABLISHED**, current published TREX model says canopy interception and surface storage equivalent depths. This is a major gap to user criterion.
- Ground cover/root or litter biomass as explicit quantitative state: no verified native process.
- Forest/mountain: Fukushima forested catchment 2017 via model adaptation; Naesung River Korea 2014 cited on developer site; distinct from original release's own validated scenarios.
- Exner/topography: developer site says bed elevation adjustment; verify that actual hillslope grid DEM is dynamically updated, not just channels, before claiming on-event feedback.

## Decision
Not selected; new original-source candidate in source retrieval tier. If canopy is purely depth parameter, rank behind fully vegetation-aware possible alternatives for single-native criteria. No new calibration until source/LAI+drip+sediment checks.

## Papers
[2008 Velleux et al](../papers/2008_Velleux_England_Julien_TREX_2D.md)


## 2026-10-26 **strict original-source recheck overrides earlier 'archive unavailable'**
**Actual full source found, reviewed**: [WatershedModels/trex_src_csu](https://github.com/WatershedModels/trex_src_csu), preservation copy of CSU original TREX; README claims source version `101017` updated 2018-05-18, pinned commit `5cfe714557333ecf8062ac04b5fba3165906a775`. `src/` directory contains 233 entries including original 2D overland C, solids and chemical transport, makefile. There is no excuse to say code unavailable. It is a third-party **archival mirror** of CSU source, not verified official-author release from CSU website; no original exe and no numerical test carried out.

Code-level ground truth:
- `src/Interception-r4.c` is **fixed remaining interception depth** deduction: `netrainrate = grossrainrate - interceptiondepth/dt` when rainfall fills it; otherwise 0, no active canopy LAI-driven storage/drain/release cycle, no throughfall vs leaf-drip kinetic energy.
- `src/OverlandSolidsErosion.c` flow sediment detachment, multiple transport-capacity/shear options, native `available` mass cap limiting potential erosion to physically available soil mass. This is better than OpenLISEM finite-material unbounded 7.5.2, but does not fix missing canopy physics.
- `src/OverlandWaterRoute-r3.c` grid-face 2D overland routing; no proof complete dynamic SWE.
- GitHub default-branch scoped code search: `throughfall`, `drip`, `raindrop`, `splash` returned no indexed original source matches; `canopy` matched only solar-radiation comment. Search-based absence is corroborating, not standalone proof.
- Full original code checked for these fundamental missing native capabilities, without creating a new canopy patch or claiming implicit LAI from landuse.

**STRICT GO/NO-GO: Reject TREX as Gounsa standalone original engine.** Failed primary quantitative LAI canopy interception/leafdrip criterion regardless of its excellent two-dimensional runoff + sediment source availability. Do not spend additional days building/test-run before features. Earlier statement that original source had not been located is superseded by this recheck, not a license to elevate TREX.
