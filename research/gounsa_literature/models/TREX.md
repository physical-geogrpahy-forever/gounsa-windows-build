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
