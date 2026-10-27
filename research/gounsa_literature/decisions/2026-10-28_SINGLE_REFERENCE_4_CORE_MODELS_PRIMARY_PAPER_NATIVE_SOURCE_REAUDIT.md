# 2026-10-28 고운사 단일 레퍼런스 결합모델 4대 후보: 원논문 / native 소스 재검증

## 0. 정의 및 조사방법
2026-10-27 기준 오해 수정: '단일'이란 엔진 수 1개가 아니라 원논문 하나에서 연결하여 실제 실행한 hydrology+canopy+XY-flow+erosion/deposition 통합모델의 문헌 계보를 의미. 원논문 속 개별 실험과 공식 소스의 재현가능성은 별도 검증. 이번 감사는 원문 공개 full-HTML(Publisher), 학술지 원문 PDF에서 텍스트 확인(시각 스크린샷 도구는 원서버403으로 실패), GitHub 연결 앱의 공개 계산코드 blob과 트리를 읽었다. **이번 세션은 Windows 네이티브 빌드/전사면 실행/수치수렴을 수행하지 않았다.**

## A. Kim, Ivanov & Katopodes(2013): tRIBS–OFM–Hairsine–Rose
- Original https://doi.org/10.1002/wrcr.20373 (publisher full page).
- §§2: hydrology tRIBS with Rutter canopy, ET, soil water, OFM full 2D SWE Roe FVM, Hairsine–Rose particle-class rainfall detachment and flow entrainment + deposited layer and elevation.
- Table 5 Lucky Hills canopy storage Ss=1mm, free throughfall p=0.35, canopy field capacity Sc=1mm, drainage K=0.18mm/h, exponent gd=3.9/mm, canopy vegetation fraction=0.5. Thus actual canopy parameters documented. However the §4.3.5 vegetation ablation modifies Ksat 5–30mm/h and Manning roughness 0.0265–0.0395 based on biomass, **not canopy-only ON/OFF or throughfall/leafdrip KE isolated**.
- §4.1: 5.8x1m, triangle cell area 0.005m2, 1170 triangles, dt 0.05s, hydrology OFF. §4.2: 10x1m, triangle area 0.005m2, 2010 triangles, dt 0.005s, hydrology OFF. §4.3 paragraph36 author emphasizes preceding two tests 'in fact one-dimensional'.
- §4.3 Lucky Hills full-coupled 36,800m2, coarsest triangle area 50m2, 908 elements, finest 9x smaller area=5.56m2 and 8192 elements. Native hydrology dt3.75min, XY/erosion dt0.01s. 3hr event 908-cell serial wall time264min on Xeon3.33GHz 2013-era workstation. Computational cost cannot be linearly extrapolated to modern PC/5cm; still no published 5–10cm full canopy sediment validation.
- Native current code https://github.com/tRIBS-Model/tRIBS tree main 333 entries, only interception source matching sediment/erosion/interception search: src/tHydro/tIntercept.cpp; actual Rutter tIntercept::InterceptRutter at L256 with L235 dC/dt equation, coefficient configuration near L453, actual LAI_LU stored in src/tHydro/tHydroModel.cpp L442/483. No Hairsine-Rose sediment source in official current branch, no complete published FEaST solver, no exact paper commit.
- **Judgement: highest single-reference coupled 2D full physics candidate; cannot approve 'download and run original published code' or '5cm canopy applied'.**

## B. Maggioli et al.(2022): classic LISEM 5cm
- Primary https://doi.org/10.3389/fevo.2022.765148 section 'Model Selection': exact 5cm computational DTM/LISEM and 1-second output maps; 'one water layer that is routed with a kinematic wave routine'. Do not recast as true XY dynamic SWE precedent.
- Vegetation Related Variables: TLS classified plant pixels→cover fraction→estimated LAI using Ramírez2007→canopy water storage. Native 5cm interception and runoff/erosion legitimate, LAI estimated not measured.
- Table 1 bare Ksat3mm/h, biocrust10, plant25; cohesion, random roughness, soil stability and treatment vary concurrently with canopy. Thus vegetation scenario is **not independent interception ablation**, throughfall/drip isolated effect unknown.
- 18-month cumulative erosion measured TLS and 18 rain events: modeled3.55t versus observed2.81t, reported RMSE17.79% not independent 5cm gridwise time-series deposit validation.
- Source https://github.com/vjetten/openlisem default branch main_C actual tree paths hydro/lisInterception.cpp SHA fd3cac..., erosion/lisErosionSplash.cpp SHA 7f75a1..., erosion/lisSWOF2DSediment.cpp SHA 683eb8..., flow/lisOverlandflow.cpp SHA 0e4531.... Explicit canopy source L43–70 RainNet and LeafDrain, splash L~59-101 directrain vs throughfall and KE, FullSWOF dynamical branch in flow file. Function exists in source != exact 2022 paper used full SWE.
- Existing project native 2026 7.5.2 12-test Windows 5m 5s/10s/20s report decisions/2026-10-26_OPENLISEM_752_NATIVE_2D_STABILITY_FAILED.md: 123.037727 vs0.005993 etc for same rain/plant and dt changes; water/global sediment ledger sums not enough to ensure local soil finite mass and dt convergence. Full 5/10cm same source numerical GO has not been confirmed. Other Work handles numerical repair.
- **Judgement: strongest published 5cm canopy-runoff-erosion precedent but NOT native verified free-XY/stable Gounsa 7.5.2.**

## C. Long & He (2009/2010) FVM with modified Gash
- 2009 Simulation of rill evolution based on finite volume method Journal of Information and Computational Science 6(6):2349–2356.
- 2010 Simulation of soil erosion and rill evolution for overland flow Journal of System Simulation 22(2):348–352, https://eurekamag.com/research/099/685/099685317.php .
- Indexed author abstract: integrated 2D SWE, Green–Ampt, **modified Gash water interception**, empirical erosion and deposition, active evolving microtopography and point-implicit bed friction. Not merely canopy+runoff in separate papers; original abstract explicitly in one model.
- Publisher 2017 successor https://www.china-simulation.com/CN/abstract/abstract1200.shtml cites 2010 paper but **new 2017 GPU cellular automaton** has different original solver, no proof of 2010 full source.
- No matching exact publicly deposited full original 2009/2010 source identified from targeted GitHub repository/source searches. Actual mesh spacing, forest LAI time-varying canopy storage, individual leafdrip KE and zero-runoff splash routing, source SHA, numerical conservation/5cm validation unknown.
- **Judgement: physical paper candidate, not a currently executable recommendation.**

## D. Wei et al.(2017) forest modified TREX
- Original DOI https://doi.org/10.1016/j.jher.2017.09.003, original author-hosted PDF https://www.engr.colostate.edu/~pierre/ce_old/Projects/Paperspdf/Wei-Velleux%20et-al.-2017B.pdf.
- Study §3: actual SRTM DEM90m and soil/land-use 100m/1km resampled90m, precipitation radar1km. §4: forest 2014 TREX hydrology enhancement includes rainfall interception and ET, 2D overland **diffusive-wave** plus 1D channel.
- Eq1 explicitly sediment ∂(A Cs)/∂t+∂(Cs qx)/∂x+∂(Cs qy)/∂y=es+eh; Eq2 es square of net-rainfall i_n times cover factor and water depth; Eq3 eh net detachment/deposition as function transport capacity. Native canopy leafdrip KE separate not evidenced, direct morphological gridwise DEM feedback absent/unproven.
- Actual historical https://github.com/WatershedModels/trex_src_csu tree has src/Interception-r4.c, OverlandSolidsErosion.c but is **old generic code**, no paper2017 matching author's modified forest code SHA. No native5/10cm experimental validation.
- **Judgement: actual forest + 2D diffusive XY plus splash and flow sediment paper, no exact source, no cm.**

## E. Multi-engine reinstated reference Feng2026 and comparison Iber+ / AHMS-SED
- Feng et al.(2026) https://doi.org/10.1029/2025WR042040 original full Methods: ELM land hillslope eroded mass + TELEMAC2D hydrodynamics + GAIA erosion/deposition and Exner. Their scientific **single-reference 3-engine coupling qualifies**. Actually authored modified TELEM/GAIA code Zenodo https://zenodo.org/records/18331808, metadata 8.2GB archive folder src; exact archive bytes not extracted or executed.
- Actual mesh min 30m 442277 triangles, ELM hourly flux. **Original Eq7 suspended class source St=D-E+Se but Eq8 bed elevation source ONLY D-E, omits upland soil loss Se**; authors explicitly state upland geomorphic changes caused by hillslope erosion excluded. Thus not per-cell hillslope microtopography development model. Not excluded for 3 engines.
- Iber+2024 DOI10.1016/j.envsoft.2024.106098 author exact 2023 public Windows/Linux case binaries https://doi.org/10.57745/UFEK4L; 5cm T1 mesh is 5cm *along slope* by 2m cross, one cell across not full high-res 2D case. LAI dynamic interception source unverified and complete source collaborator-only.
- Jiang2025 AHMS-SED DOI10.1029/2024MS004593 original source https://github.com/JiangCong1990/AHMS-SED + NoahMP throughfall/drip; native 20km; more specific sediment routing module not in build target, no 5cm validation.

## F. Newly code-audited RDycore is NOT a native Kim FEaST recovered implementation
- Repo https://github.com/RDycore/RDycore, current docs/theory/sediment.md reproduces coupled 2D Hairsine–Rose equations, cites Kim2013; docs alone can falsely suggest available exact HR code.
- Actual src/tracer/tracer_sources_ceed.h lines 37–71 and src/tracer/tracer_petsc.c lines 633–636 and 701–706 implement per-class e=kp*(tau_b-tau_cr)/tau_cr and d=v_settle*c*(1-tau_b/tau_cd), constants kp0.001, v_settle0.01, taucr_e0.1, taucr_d1000. These are **simplified shear-based GAIA/Partheniades source terms, not complete Hairsine-Rose rain + flow + deposited layer equations in prose documentation**.
- Sediment tiny 5x10 dam-break driver/tests/sediment/sediment.yaml has 2 sediment classes, dt0.01s and no rainfall/canopy. No manuscript-native 5/10cm canopy-runoff erosion or original FEaST implementation. Not Gounsa candidate.
- Potential concern source formula lacks explicit max clipping when tau_b below threshold in extracted code; not proof of failed entire simulation. No full compilation/run undertaken.

## 7. Selection, pass gates, next
- **Single-reference physical process evidence**: Kim (genuine XY + interception + source/dep), Maggioli LISEM (published 5cm canopy, kinematic), Long–He (2D SWE + Gash + rills), Wei TREX (forest interception + XY diffusive erosion).
- **Native complete usable same-paper public application**: none so far passes all of 5/10cm actual canopy ON and OFF, unrestricted bidirectional flux and sediment, flow+rainsplash, percell deposition/DEM, stable time/mesh/finite soil stock and source reproducibility. Existing old model releases distinguish from paper-version original.
- User decided OpenLISEM native numerical troubleshooting is assigned to separate Work; do not claim fixed or reselect without its exact source and test outputs.
- Before ranking as production model, require actual matching source version, paper input/runfile, runtime canopy water flux trace and sediment ledger, actual 10cm and 5cm native 2D canopy ON/OFF strong storm and timestep/CFL convergence. A paper citation is not an executable pass.

## Sources
https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/wrcr.20373
https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.765148/full
https://www.engr.colostate.edu/~pierre/ce_old/Projects/Paperspdf/Wei-Velleux%20et-al.-2017B.pdf
https://eurekamag.com/research/099/685/099685317.php
https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025WR042040
https://github.com/tRIBS-Model/tRIBS
https://github.com/vjetten/openlisem
https://github.com/RDycore/RDycore
