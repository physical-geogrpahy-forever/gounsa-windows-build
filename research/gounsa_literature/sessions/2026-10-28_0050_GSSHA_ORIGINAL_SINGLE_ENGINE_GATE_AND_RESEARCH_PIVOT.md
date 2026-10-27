# 고운사 모델 선정 탐색 방식 전환 인계서 — 2026-10-28

## 문제
사용자: 수백 개 문헌기록을 남기고도 실행 가능한 공개 원본 수관차단+2D 사면침식 모델을 제시하지 못했다. 같은 OpenLISEM·tRIBS 과제 반복을 중단하라.

## 이 세션에 실제 수행
- Project SYSTEM, INDEX, 기존 2026-10-27 multi-engine single-reference definition audit and previously stored candidate papers reread.
- New web retrieval screened pre-existing ~10 near candidates and code-distribution materials. Highlights GSSHA USACE original core instead of another source-less research solver.
- Original indexed ERDC Downer et al. 2010 TN-SWWRP-10-3 sediment conservation process detail, 2023 peer-reviewed Garcia LAI-based native GSSHA forest flow application original HTML Methods, official 2024-10-07 GSSHA 8.0 release, 2014 online / 2015 ASCE Downer testing old sediment overestimation, independent EarthSim explicit closed source caveat.
- No original GSSHA 8 binary downloaded, no source executable built, no same-run forest canopy+sediment executed, no 5/10cm numerical proof. GSSHA wiki PDF and downloads returned 403 to automated web inspection; indexed snippets used where indicated and not misrepresented as full visual PDF inspection.

## Main discoveries
1. GSSHA native single-engine documented canopy two-parameter interception, XY diffusive-wave runoff, rain and overland detachment, 2D sediment transport, soil and deposit layer, explicit inter-event sediment/elevation forwarding. Different from failure-prone OpenLISEM code lineage.
2. Garcia et al. 2023 DOI10.21926/aeer.2301022 actually uses LAI-informed canopy storage in GSSHA forest setting 5m grid 10s dt, but hydrology only. Sediment native separately documented ERDC2010 and ASCE2015, not jointly proven 5cm same original release.
3. 8.0 2024 free executable, complete native public source NOT located, gsshapy only wrapper, older EarthSim docs explicitly say GSSHA simulator closed source. 5/10cm, original code SHA, canopy drip KE, same-event active DEM feedback not demonstrated. Thus despite improved source lineage, **not currently user strict all-pass candidate**.
4. GRASS r.sim.water / sediment source available true bidirectional WEPP-like erosion but lacks native canopy, and is effectively near kinematic + diffusion; Wflow.jl canopy but LDD sediment; Iber+ 2D sediment but canopy missing. New coupling would be needed if combining them: cannot call same original paper's single model.

## Saved
- papers/2010_Downer_Ogden_Pradhan_Liu_Byrd_Improved_GSSHA_Erosion.md
- papers/2023_Garcia_GSSHA_Forest_LAI_Interception_Harvest.md
- models/GSSHA.md
- decisions/2026-10-28_STOP_RESCUE_OPENLISEM_SWITCH_SOURCE_FIRST_GSSHA_GATE.md
- MASTER.md updated; INDEX.md regenerated from actual GitHub main tree (Papers511 incl gitkeep, Models113 incl gitkeep, Decisions113 incl gitkeep).

## Operational hard gates
- No repeating OpenLISEM rescue or tRIBS FEaST source speculation as solution.
- Any newly named candidate must show official original code or honestly binary only before paper physics claims; reproducible 5–10cm same release water+sediment with LAI canopy & four-edge flux and positive soil stock is an experimental gate.
- If source strictly mandatory, GSSHA 8 remains NOT APPROVED. Do not blame user for model-feature tradeoff and do not imply a viable published all-condition model exists without evidence.
