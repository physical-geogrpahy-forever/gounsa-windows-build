# 고운사 2026-10-28 새 공개 원본 및 실제 코드 감사 — SMART-SED
## Goal
Find a new exact single published reference and matching publicly available actual solver source: LAI canopy, genuine XY rainfall + runoff erosion, deposition, finite stocks and 5–10cm mesh with four-edge runoff.
## What was genuinely found now
- Published SMART-SED Gatti et al. 2023 DOI10.1016/j.cageo.2023.105362 PDF open and Methods §§2,4.3,4.4 read; Code Availability expressly links https://github.com/federicg/smartsed . Gatti original GNU license C++11/Eigen/MPI source main_final_H.cpp/utils_H.cpp, Makefile and event run/SMARTSED_input_ev, actual Inputs DEM/rain/land use accessible and inspected via connected GitHub. This genuinely fixes prior 'paper code never traced' error for THIS MODEL, not for other models.
- Published actual 2D SWE x/y, rain SCS-CN infiltration, 2D flow/advective sediment `h_sd`, Gavrilović rainfall-empirical source `W_Gav`, 2D velocity/residual and real sediment-on example. Published Dragone computation 10m and Caldone 20/50/90m. **Cannot claim published 5–10cm**.
- Original original paper §2 says terrain bed b does not vary in time, sediment source from Gavrilović EPM historical annual empiric assumed usable event time, no separate splash/flow detachment, no dynamic LAI canopy throughfall/drop energy. **Cannot declare single model meeting Gounsa core**. No full original C++ build/native test performed.
## Existing known public sources separately checked
- storm-fsv-cvut/smoderp2d master src active only rain/vegetation/interception and sheet/rill HYDRAULICS; no actual sediment mass detach/transport deposition execution. Prior canonical in models/SMODERP2D*; not new candidate.
- marcusnobrega-eng/HydroPol2D 2026 current MATLAB code real `interception_module.m → interceptionModel.m` LAI storage + thru rain connected in Hydrological_Model.m; source only water-quality pollutant buildup/washoff; no explicit soil erosion/bed sediment deposition. Prior canonical models/HydroPol2D.md; reject.
- psu-efd/HydroSed2D genuine unstructured SWE and Exner bedload; no rain infiltration/interception/splash. Prior canonical model.
- Durham DRAEM official software page https://draem.webspace.durham.ac.uk/software/ confirms MAHLERAN current event-based software must be requested by contacting author, not original full public downloadable source there.
## Archived
- papers/2023_Gatti_Bonaventura_Menafoglio_Papini_Longoni_SMART_SED_Coupled_Runoff_Erosion.md (new)
- models/SMART_SED.md (new)
- decisions/2026-10-28_SMARTSED_ORIGINAL_2023_PAPER_AND_CPP_FOUND_BUT_CANOPY_NO_GO.md (new)
- MASTER.md update
- INDEX.md regenerate (papers512, models115, decisions115 including .gitkeep)
## Integrity
- Original published Gatti PDF web screenshot attempted but 403 from primary host, so evidence was extracted PDF text and author GitHub source fetched through connector. Native compiler was never used; source exists != verified running cm-resolution model.
- Gounsa target remains outstanding; compare baseline all-open sources vs exact published research sources and do not rerun failed Classic OpenLISEM rescue assigned to other Work.