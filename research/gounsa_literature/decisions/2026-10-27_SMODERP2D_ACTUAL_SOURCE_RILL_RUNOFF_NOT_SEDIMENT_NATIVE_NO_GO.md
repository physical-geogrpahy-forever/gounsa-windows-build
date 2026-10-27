# 2026-10-27 새 독립 오픈소스 SMODERP2D 원본검증: 'erosion model' 명칭과 실제 토사질량 연산 구분

## 조사 지시 및 중복관리
- 사용자 요구는 OpenLISEM fork 수정/실행을 별도 Work에 맡긴 상태에서 **새 기존 단일 모델 실증 및 전체 original source**를 조사하는 것.
- 연구 시작 전 SYSTEM.md, INDEX.md (496 papers/103 models/100 decisions at moment), MASTER, 2026 source-gates 확인. SMODERP2D는 canonical 등록 이전에 존재하지 않음.
- 실제 공개 GitHub https://github.com/storm-fsv-cvut/smoderp2d , Czech Technical University. 2019 paper doi10.5194/isprs-archives-XLII-4-W14-143-2019, 2022 validation doi10.3390/w14030327, related unpublished native sediment question solved by 2022 doctoral thesis hdl10467/104997.

## New papers indexed
1. [Landa, Jeřábek, Pešek & Kavka 2019](../papers/2019_Landa_Jerabek_Pesek_Kavka_SMODERP2D_OpenSource_Parallel.md): official peer-reviewed original 7page PDF page1 screenshot + methods p2 read. D8 flow-direction, rainfall interception reducing effective rain, infiltration, kinematic sheet empirical q=X I^Y h^b, rill Manning, CFL and GPU TensorFlow prototype. Not explicit sediment mass balance.
2. [Kavka, Jeřábek & Landa 2022](../papers/2022_Kavka_Jerabek_Landa_SMODERP2D_SheetRill_ThreeScaleValidation.md): 2×8m plot 60mm/h 30min runoff experiments (bare vs wheat/clover), 50m² Wischmeier monitored, 36.6ha Býkovice field spatial **5m×5m actual rill computation**, visually validated rill occurrence area. **Rill width/rill occurrence ≠ sediment erosion/deposition mass**. Inconsistencies from displaced routing cells, bare surface overpredicts rill occurrence.
3. [Neumann 2022 PhD dissertation](../papers/2022_Neumann_SMODERP_Sediment_Transport_PhD_Experimental_Evaluation.md), 450+ rain simulator 2015–21, slope4°–34°, rain40–160mm/h, 10 candidate methods, calibrated Kilinc & Richardson transport-capacity with USLE K and crop factor CS. **Original abstract explicitly describes current model as runoff-only while extension of sediment was research objective**. Thesis published does not prove distributed release in exact current active code.

## Actual 2026 public code static audit
- **[Full detailed source audit](../models/SMODERP2D_2019_2026_Native_Interception_Rill_Without_Sediment_Source_Audit.md)**.
- `core/vegetation.py`: `VegArrs(veg,ppl,pi)`, pi potential interception in mm, ppl leaf area fraction (Czech note "pomerna plocha listova").
- `processes/rainfall.py::current_rain()`: `interc=ppl*rainfall`; cumulative `sum_interception`, bounded by pi; returns net rainfall NS, with state `veg` flipping on storage saturation. This is **no storage drainage/leaf-drop height KE / Gash-Rutter dynamic canopy hydrology**.
- `core/kinematic_diffuse.py` Kinematic/Diffuse classes inherit `Mfda if Globals.mfda else D8`, Diffuse recalculates flow directions from `DEM+h` and reuses directional algorithm. 2D raster shapes ≠ free 2D Saint-Venant u,v flux.
- `core/surface.py` and `time_step.py` active sheet runoff, rill runoff, critical level, rill width, rain/infiltration and water mass flow; `time_step.py` has **no current sediment source/advect/deposit functions**; full repo code search `sediment` returns only documentation/plugin descriptions, `detach` and `deposition` no numeric kernels.
- Peer reviewed 2019 p2 screenshot already used to verify Eq1–6 explicitly water-only; 2022 MDPI paper expressly validates hydrographs/rill initiation. No matched 5cm published native sediment simulation.
- No newly downloaded executable or current code native test. Source inspection is rigorous **static code functional-gate**, not dynamic stability conclusion.

## Hard-gate comparison
| Gate | status |
|---|---|
| Public official original software | YES GPL/GitHub, new source |
| Event short rainfall / infiltration / sheet and rill | YES |
| Leaf area variable, finite simple interception cap | YES (`ppl,pi`) |
| LAI-controlled dynamic canopy storage and drainage / leaf KE | NOT PRESENT in audited active path |
| Genuine freely spreading full XY water dynamics + 4 side free exit | NO: D8/MFDA directional |
| Actual explicit sediment concentration, rain & flow detachment, deposition | **NO active executable path found** |
| Verified 5–10cm water+sediment scenario | NO: field grid 5m in 2022 |
| Field comparison with soil loss/deposition measured | 2022 tests runoff and mapped rills; soil mass output not shown |

**Decision: Reject as Gounsa standalone original 5–10cm sediment engine; retained as event rill/runoff model source/reference.** Model name/title not allowed to override source functional proof. If PhD prototype code later surfaces as independently released feature, repeat gate using exact commit+active time loop+numerical sediment mass validation.

## Sources
https://github.com/storm-fsv-cvut/smoderp2d
https://doi.org/10.5194/isprs-archives-XLII-4-W14-143-2019
https://doi.org/10.3390/w14030327
https://dspace.cvut.cz/entities/publication/3155d66e-c8c2-463b-9e5a-72539e77c103
https://storm-fsv-cvut.github.io/smoderp2d-manual/requirements.html
