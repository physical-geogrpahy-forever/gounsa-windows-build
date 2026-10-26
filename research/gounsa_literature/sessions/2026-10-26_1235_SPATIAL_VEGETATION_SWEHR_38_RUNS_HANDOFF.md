# 2026-10-26 고운사 밀생 억새 대 산발 참나무 2D 공간모형 38회 인계

## 완료
- main 자료검색 결과 GitHub repository에는 field georeferenced DTM, 억새 포기 polygons, 참나무 맹아 rootstock 위치, coarse fragments 래스터 원자료가 없음. 현장이라고 주장하지 않고 13×25 (0.5m) 가상 사면 생성.
- SWEHR published C source `csdms-contrib/swehr` SHA `4e6f783f335ac6dc1c116ef0d516c2f3d1b911e2` 활용. 지난 세션의 초기조건 명시/원본 외부 강제물/유사 유입 제거 + novel spatial vegetation coupling (per-cell rain water/drop source, Ks, roughness, rainsplash detachment a/ad, stream-power detachment J). Native source equations Hairsine-Rose and SWE retained.
- 4 배치(밀생 억새, 산발 참나무, 40%/40% 연결형 vs 고립형)×5 rain(10,20,30,40,50mm/h×1h) 20개, stemflow relocation 10개(기본 30의 2개 + 나머지 8개), 물리과정 제거 대조 8개: 총 38개.
- **38/38 물수지 및 독립 유사수지 통과**. maximum water residual 4.15e-11, original soil detachment ledger 1.16e-13, bed geometry ledger 4.67e-05.
- 예시 P30 mm/h 밀생 억새 가상 유출10.0866mm/수출0.000542655t/ha vs 산발 참나무 유출21.6609mm/수출0.002290642t/ha; 임의 site-like arrangement만 반영, observed Gounsa ratio 아님.
- 40% 동일면적 패치모의에서 고립형이 횡방향 연결형보다 P50에 약1.410배 많은 유사량; runoff totals 거의 비슷.
- Process OAT(30mm/h) 에서 spatial hydraulics controls runoff, detachment controls sediment. SF source relocation from canopy surface to stem/tussock locations is mass conserving but outlet yield effect small in this chosen microtopography and Ks field. Leaf-drip KE absent and must be implemented as independent forcing.
- 종별 고정 parameter가 아니라 식생/노출 격자 공통 *hypothetical* Ks(1e-6 vs4e-6m/s), Manning .08 vs.18, a .25 vs .07, J 30 vs90, vegetation storage0.8mm. Not calibrated to oak vs Miscanthus; no root biomass or RLD law implementation.
- Native original C first crashed from uninitialized spatial matrix allocation before NX/NY read and original hardwired output probes y=50 beyond new ny25. Debugged with AddressSanitizer and fixed the initialization order and output-only locations, not physical equations.

## Permanent code and evidence
- branch: `spatial-vegetation-runoff-erosion-20261026`.
- experiments/rainfall_10_50/spatial_patch_swehr.py (synthetic masks, new spatial water/drop forcing and 2D original solver code).
- experiments/rainfall_10_50/aggregate_spatial_sensitivity.py and workflows spatial_swehr_2d.yml, spatial_swehr_controls.yml, aggregate_swehr_2d.yml.
- verified machine readable CSV, full_qa.json, textual raster masks and summary: `experiments/rainfall_10_50/spatial_patch_experiments/verified_20261026/` (committed by successful GH Action).
- 20+2 run: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40264048008
- 16 controls: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40264354578
- 38-result aggregation: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40264757325
- main decision: `decisions/2026-10-26_SPATIAL_NATIVE_SWEHR_DENSE_MISCANTHUS_SPARSE_OAK_38RUNS.md`; MASTER and INDEX updated.

## Remaining
1. Regrid actual Gounsa drone/TLS terrain and vegetation maps at enough spatial resolution to express real tussocks/rootstocks and connected exposed surface.
2. Calibrate Ksat and initial soil moisture, actual oak stump vs Miscanthus tussock herb root distribution and litter independently, published soil erodibility equations. Never infer RLD from cover.
3. Quantify stemflow and throughfall species-specific hourly volumes and impact energy/leaf-drip, with mass conservative per-plant footprint (not arbitrary 0.02m²).
4. Validate native hydrological/sediment boundary mass budgets, domain and mesh/time-step convergence and event soil loss against measured Gounsa runoff/TLS.
5. Production decision Iber+ / SSSPAM-mARM retained; proof-of-concept SWEHR does not implicitly replace it.
