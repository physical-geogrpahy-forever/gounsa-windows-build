# 2026-10-27 23:45 다른 5–10cm 출판 연구 재탐색: Wang2023 + Cooper2012 + Iber published executable bundles

## 논문 인덱스 조사 및 제외원칙
출발 기록 `SYSTEM.md`, `MASTER.md`, `INDEX.md` 논문496/모델103/결정100과 가장 최근 비LISEM 작업 인계 확인. OpenLISEM 7.5.2 원본 디버깅은 사용자가 다른 Work로 넘겼으므로 다루지 않음. 사용자가 **기존 published original same model**을 원하므로 미확인 source를 논문명만으로 runnable model로 제시하거나 최근 탈락 (SHETRAN subcm 등) 재권유하지 않음.

## 1. 완전히 신규 확인한 2023 2D 사면 유수침식 논문
**Wang, T., Hou, J., Li, J., Li, P., Tong, Y., Zhang, N., Cheng, S., Li, J., Li, Z. (2023)** *CATENA*232 107387 DOI https://doi.org/10.1016/j.catena.2023.107387 : indoor loess-slope rainfall experiment to derive corrected sediment transport capacity, 2D planar rainfall-runoff sediment source dynamics and spatial erosion contribution. Source paper abstract/readable introduction discuss **evolving rills and 2D planar redistribution**. **Do not infer exact full Saint-Venant equations** from generic paper label without missing full Methods and actual discretization. 2022 EGU **precursor** https://doi.org/10.5194/egusphere-egu22-1885 reports runoff NSE0.83, sediment NSE0.66, R²0.89/0.73, relative bias−5.02/−1.02%, ~69.59% of predicted erosion from 1–4m laboratory slope segment. **Not equal a 2023 independent holdout field validation**.
- Original lab loess, no quantified canopy LAI / undercanopy drip in accessible paper material. Published actual ∆x and ∆t unknown, none at verified 5cm.
- Exact executable source / test archive not linked in publisher metadata. Connected GitHub exact study title and author queries no matching sediment source. Related *HEMLab/HiPIMS-CUDA* is original **flood hydraulics** solver but not proven used by Wang paper and not known to include its special soil-erosion solver; false attribution prohibited.
- [canonical](../papers/2023_Wang_Hou_Catena_TwoDimensional_Loess_Slope_Erosion.md). **Scientific support, no full-pass main engine**.

## 2. Existing Cooper et al 2012 verified directly from journal original
[canonical updated](../papers/2012_Cooper_Wainwright_MAHLERAN_MiC_30cm_Interception_Drip.md), DOI https://doi.org/10.1029/2012JF002499. **Important because canopy 'exists' but fails actually active test.**
- Full 2012 journal Methods §3.1 explicit rain KE **adjusted for interception losses, direct throughfall, leafdrip**; but no verified dynamic LAI canopy store in this code. Original §2 unequivocal **MAHLERAN kinematic cardinal-direction steepest descent**, not bidirectional full SWE. 2D stochastic sediment markers do not imply freely 2D water physics.
- 13.75×6.5m plot, **actual native ∆x 0.30m**, 60mm/h×20min, **bare sand** with upper **0.05m deep sand layer** (depth != native 5cm computation). Observed flow534L vs simulated580L (9% difference), runoff hydrograph NSE0.93, `137Cs` marker redistribution NSE0.98 across 20 stochastic repeats. Substantive **local deposition tracer** benchmark and code architectural precedent but no canopy ON/OFF tested and no 5cm computational run. Exact 2012 complete downloadable code not identified. **Reject as Gounsa native cm dynamic forest**.

## 3. Original deposited Iber+2024 2D soil erosion benchmarking is reproducible in binary form
[Existing model audit augmented](../models/Iber.md); original paper Cea et al (2024) DOI https://doi.org/10.1016/j.envsoft.2024.106098 **full SWE + multiclass rain/flow detachment + deposition**.
New exact **author-deposited public DOIs** identified:
- Executable Iber+ V3.2b Windows/Linux [10.57745/UFEK4L](https://doi.org/10.57745/UFEK4L) (adapted 2023 binary, **not calculation source**).
- T1 laboratory [10.57745/2WH9AL](https://doi.org/10.57745/2WH9AL), 6×2m=12m², 120 mesh elements **5cm long ×2m wide: explicit quasi-1D**. Misreporting `5cm 2D` would be false.
- T2 Pradel field hillside [10.57745/J2A44Q](https://doi.org/10.57745/J2A44Q), 120m² 3300 mesh elements, sqrt mean area ~0.19m equivalent cell side. Nonuniform min and max mesh widths not established; no canopy physical dynamic LAI state shown.
- T3 Galabre mountain event [10.57745/NOHRHJ](https://doi.org/10.57745/NOHRHJ), 20km² 94119 mesh elements, and T4 Ullion creek [10.57745/VFBGFR](https://doi.org/10.57745/VFBGFR), 45314 mesh. Real source/demo cases all published and real downloadable as datasets.
- 2024 independent paper [NHESS 24:609](https://nhess.copernicus.org/articles/24/609/2024/) states calculation **source code available to collaborators only**, binaries freely shared. Therefore user full-source and dynamically stored canopy/drip **NO-GO** persists. Exact executable can be a **limited reference benchmark** if binary allowed, but **not a newly identified full-source forest engine**.

## Strict comparative conclusion
| Study | 5cm actual computational | vegetation LAI canopy storage/drip active study | Full XY 2D hydro | Rain+flow erosion sediment deposition | Matching fully public original source |
|---|---|---|---|---|---|
| Wang2023 | unknown | unknown/not documented | 2D numerical, SWE variant unknown | runoff and sediment yield mapped, morphology goals | Not found |
| Cooper2012 | NO 0.30m | KE scaling in code concept, **bare scenario tested** | NO cardinal kinematic | detachment/transport/deposition marker YES | Not found |
| Iber+2024 T1 | **5cm length only** ×2m breadth | not documented | **effectively 1D test** despite full SWE core | rainfall erosion and multiclass transport tested | **Binary only, no C/CUDA sources** |
| Iber+2024 T2 | actual mean area suggests ~19cm characteristic; no smallest confirmed | no verified canopy storage | full 2D SWE | rain/flow sediment local transport yes | Binary only |
| Existing Kim2013 tRIBS-OFM+Hairsine Rose | 0.005m² mesh equivalent (~7cm), not direct 5cm square | Rutter hydrology documented but active canopy in fine erosion test not proven | full XY 2D SWE | 2D raindrop+flow source and depositional H-R physics | matching FEaST full source missing |
| Existing Maggioli2022 classic LISEM | 5cm actual | canopy LAI and retention verified | study uses kinematic | rainfall+flow sediment model yes | paper exact build unavailable, later 7.5.2 numerically fails native |

**No new all-PASS.** Biggest new actionable proof: exact original Iber erosion reproducer with DOI and source restrictions, and a new experimentally assessed planar Wang2023 erosion method to index. Do not promise running it as if source open. Unknown status must remain unknown, not categorical no model exists.

## Reason for scientific caution
Even published exact full 2D source 5cm test can be **quasi-1D in mesh connectivity**, or report input 5cm sand layer/0.3m UAV LiDAR while computational mesh is much coarser. A free 2D canopy erosion example must evidence all properties **in the same active experiment**.
