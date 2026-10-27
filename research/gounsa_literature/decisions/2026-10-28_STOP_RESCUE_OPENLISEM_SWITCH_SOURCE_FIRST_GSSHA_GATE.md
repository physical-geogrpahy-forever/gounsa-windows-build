# 2026-10-28 고운사 모델 탐색 전환 결정 — 실패 모델 재권고 중단, source-first, GSSHA 재평가
## Decisions
1. Stop original OpenLISEM v7.5.2 rescue as mainline. Its published functionality does not supersede actual 2026-10-26 twelve native 5m 2D failures in temporal convergence and finite soil stock. Experimental fork is a separate newly modified model requiring full QA; no success claim.
2. tRIBS–FEaST(2013/2014) authors' full 2D Hairsine-Rose integration remains unavailable via verified official current tRIBS GitHub source; do not make acquisition an open-ended plan or promote as executable.
3. Evaluate *newly surfaced* native GSSHA source lineage as a **bounded alternative**, not a GO. Has original canopy interception+2D diffusive XY runoff+raindrop/overland erosion+native finite layer sediment stock+local deposition and between-storm bed-state forwarding. v8 release binary announced, GSSHA original C++ public source NOT confirmed (GSSHA differs from open-source gsshapy). Published forest LAI 2023 GSSHA at 5m, original 2010 improved sediment native report; no published same-run 5cm canopy erosion verification identified.
4. Stop criterion: if complete GSSHA 8.0 original source cannot be found, classify as **binary-only** and do not pretend fulfills user source requirement. Even if versioned executable found, canopy-on-off sediment + bed elevation conservation in 10cm computational mesh must be run before adoption, and leafdrip KE must be marked unverified.
5. Strict one-reference (multi-engine allowed) plus confirmed 5/10cm original source, canopy quantitative state, true two-direction runoff, rainfall/flow erosion, spatial deposition, and mass/stability remains **0 verified today**, not an impossibility theorem.
6. Standalone proven base physics routes not to misrepresent as single paper: Iber+ open author binary/2D erosion without canopy, Wflow.jl open source dynamic LAI+drip but directed sediment routing, GRASS SIMWE public source genuine bivariate erosion without native canopy. They are **comparators/fallbacks requiring explicit new coupling** if combined; user did not authorize recommending new coupling as ready same-paper model.
## Evidence
- GSSHA v8.0 official news https://www.erdc.usace.army.mil/Media/News-Stories/Article/3924653/gridded-surface-subsurface-hydrologic-analysis-model-version-80-released/
- USACE original 2010 Technical Note https://gsshawiki.com/images/9/92/Sediment_TN.pdf (web PDF open403; search-indexed text inspected only)
- Garcia et al. 2023 forest case https://doi.org/10.21926/aeer.2301022 full HTML §2.3 LAI and 5m grid
- 2014 online / 2015 print Downer et al https://doi.org/10.1061/(ASCE)HE.1943-5584.0001104 (severe older sediment bias)
- EarthSim original integration documentation https://earthsim.holoviz.org/user_guide/index.html (freely available but closed source)
- https://github.com/CI-WATER/gsshapy (I/O wrapper, not C++ solver)
- GRASS true bivariate 2D routing https://grass.osgeo.org/grass-stable/manuals/r.sim.sediment.html; https://grass.osgeo.org/grass-stable/manuals/r.sim.water.html (manual specifies 2D *approximate* kinematic plus diffusion rather than full SWE)
## Next tangible test direction
Require one versioned official GSSHA 8 original executable and published example dataset, confirm rain interception and sediment and outputs from native run, and runtime 10cm if original code visibility can be established; no actual simulation performed here because access to wiki binary and native inputs not verified. Avoid another 500-paper sweep.
