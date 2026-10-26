# 고운사 작업 인계: 빽빽한 억새 대 군데군데 참나무 맹아

사용자 핵심 지적: dense Miscanthus stand와 sparse Quercus coppice islands를 같은 mean cover/infiltration model로 비교하는 것은 부적절함. 기존 native simulation 숫자는 실제 식생의 침식량이 비슷하다는 증거가 아님.

신규 문헌:
- papers/2008_Mayor_FlowlengthRunoffSourceConnectivity.md, DOI 10.1029/2007WR006367, vegetation pattern + microtopography connectivity Flowlength tested with 6 plots, 3 catchments.
- papers/2023_Crompton_PatchHillslope_2DConnectivity.md, DOI 10.1029/2022GL101801, 2D Saint-Venant numerical patch experiment shows run-on infiltration versus run-around from rough patches.

실제 기록: decisions/2026-10-26_DENSE_MISCANTHUS_SPARSE_OAK_SPATIAL_COMPARISON.md; MASTER.md and INDEX.md updated (391 papers).
핵심 구조: UAV/TLS observed M. sinensis tussock polygons and gaps versus oak stump/sprout islands with interconnected bare soil. SF per-tussock or per-stump volume+location, separate direct TF and leaf-drip KE, root/litter + rock-fragment effects, per-cell infiltration and 2D flow. Do not equate species phenotype with arbitrary Ksat/n/erodibility or COVER alone. The actual Gounsa difference likely flows from exposed-ground continuity and roots/litter/microtopography; high roughness can divert flow around vegetation, so compare flow paths, not assert universal less erosion.
Numerics: run both actual map A/B and controls with fixed traits but rearranged patches to isolate arrangement, then traits-only counterfactual; 10-50 mm/h 1h mass balance and class sediment budget. Original SWEHR 3×51/0.25m field too narrow for dispersed stump spacing, EUROSEM one-plane no spatial routing. Iber+ selected production engine maintained.
No new site-specific 2D erosion simulation was performed in this turn. Need user datasets accessible via attachment/connected repo or actual surveyed raster to run non-invented geometry. Do not label conceptual design as run.
