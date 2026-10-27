# FullSWOF_2D 기반 Le et al. 2015 Hairsine–Rose 2D 침식 해석기: 논문 코드 대조

## 조사 대상
- [Le, Cordier, Lucas, Cerdan (2015)](../papers/2015_Le_Cordier_Lucas_Cerdan_FullSWOF_HairsineRose_2D_Sediment_Splitting.md), DOI10.1002/2014WR015690, Water Resources Research 51(2),987–1005. **논문 전문 HTML 직접 검토**.
- 공개 2016 pure hydraulic code original clone [BUCEA/FullSWOF_Rif](https://github.com/BUCEA/FullSWOF_Rif), version1.07.00 2016-03-14 `README.txt` blob SHA `33270a9e7d83700b8dd3ec60430fe935d849bdaa`, root `Makefile` SHA `4b30c3c1cf5c3b0d0e1a3b86e83e215efc81bd44` 확인.
- FullSWOF scientific official website https://www.idpoisson.fr/en/fullswof/ confirms 1D/2D hydrology open source; new 1D transfer added 2021 but **does not assert publicly released full 2015 2D HR sediment edition**.

## Actual code path / exact source identity
- `BUCEA/FullSWOF_Rif/Makefile`: compiled libraries `-lschemes -lboundaryconditions -lflux -lfrictions -lrain_infiltration -linitializations -lreconstructions -llimitations -lsave -lparameters -lparser`; **no sediment/erosion/Hairsine-Rose` C++ lib in active build**.
- Original 2016 FullSWOF open-source 2D water h,u,v + rainfall/infiltration, not released source for model modified in 2015 Le paper. 2015 paper §4 states "we thus use an SW code, to which we add an erosion component", meaning their code has extra particle classes, HR detached layer and concentration. No exact modified archive/commit/file/runfile detected in direct search.
- Therefore **source available only for base hydrodynamics, not verified for article-exact sediment executable**. A reader cannot run published 2015 sediment case using only this unchanged 2016 `FullSWOF_Rif` repo; adding HR yourself constitutes new custom model.

## Paper's actual implementation and numerical physics
- 2D full shallow-water system h,velocity(u,v), zbed, concentration c_i, surface deposit storage m_i for multiple particle classes. Hairsine–Rose rate equations represent rainfall and flow origin detachment, re-detachment/re-entrainment of deposit material, settling and surface shielding, plus 2D sediment advection.
- Numerical method: nonnegative h and sediment c_i, wet/dry reconstruction, semi-implicit friction, Green-Ampt infiltration; **Strang-splitting settlement (half) + detachment/reentrainment (full) + settlement (half)**. Analytic deposit update avoids extra negative concentration dt bound beyond SWEs CFL limit.
- Original 2015 authors compare Roe-type Kim2013/Heng2009 where sediment positivity forced a more stringent additional dt. Reported 2D speed advantage ≥100× applies to exact Le scheme/reference case, **not to original Classic OpenLISEM or 2026 source**.

## What the 2D application really measured
- Thiès Senegal raked V-slope 10m×4m, longitudinal1%, transverse1%, rainfall70mm/h for120min. Multi-size 10 classes 10–1000μm with shallow water, soil mostly sandy.
- Article §4.3 explicit: stream power too small to exceed sediment entrainment critical value (except at outlet), **flow does not contribute flow-induced detachment in the presented realistic 2D application**, instead carries rainfall-detached particles; deposition layer m_i evolves.
- Thus supporting separate code terms for rain and flow detachment ≠ demonstrated real 2D detachment result for flow term. Even with full code this test is **rainfall-dominated**, not Gounsa requested simultaneous intense overland flow detachment.
- Numerically resolved plot DEM raster dx/dy not found in Wiley accessible formatted body. **Don't equate plot length or 5cm soil thickness with native 5cm model computational resolution**. No canopy LAI, canopy storage, throughfall, leafdrop energy.

## Next strict code test if a source archive emerges
1. Match 2015 HR extension, exact release source SHA, test input and author version.
2. Run 2015 10x4m 70mm/h reference on supported mesh; examine h>=0, c_i>=0, deposition m_i>=0, Σ_sed changes equal mapped erosion/deposition and exports; both water and sediment CFL positivity with lossless internal face flux.
3. Independent **flow-only vs rain-only vs rain+flow** entrainment under e.g. higher slope/rain, not only author §4.3 low-stream-power case.
4. Only after published exact source is runnable, ask high-res LAI canopy expression, four-side boundary and 5–10cm convergence. Missing source/vegetation remains hard NO-GO without new coupled software being correctly labelled new development.

## Verdict
**Scientific original 2D sediment numerical stability literature = PASS; published study's exact free code + canopy + 5cm explicit flow scour = FAIL/UNVERIFIED; main Gounsa candidate NO-GO.** Code available for base hydraulic engine, not matching full 2015 sediment source. Do not conflate original 2D water code and updated 2015 full water/sediment solver.
