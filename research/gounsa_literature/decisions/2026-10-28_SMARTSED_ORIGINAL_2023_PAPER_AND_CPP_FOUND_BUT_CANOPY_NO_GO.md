# 2026-10-28 Source-first actual discovery SMART-SED paper-matching original code
## Found
Exact 2023 peer-reviewed original full PDF Gatti, Bonaventura, Menafoglio, Papini, Longoni https://doi.org/10.1016/j.cageo.2023.105362 with EXPLICIT Code Availability original author's complete public C++ source https://github.com/federicg/smartsed .
Original code `main_final_H.cpp`, `utils_H.cpp`, `Makefile` and data `run/SMARTSED_input_ev`,`Inputs` all actually read via GitHub connector. This is more than a model name or unreleased in-paper tRIBS-FEaST source.
## Observed implementation
True two-direction SWE runoff, rainfall, SCS-CN infiltration, finite sediment transport with source map `W_Gav` and mobile layer `h_sd`, configurable erosion ON, author mountain event (Dragone 2010 126mm/3h). Published numeric scales actual 10m Dragone and 20/50/90m Caldone, not 5cm.
## Why NOT Gounsa GO
Missing LAI/canopy storage and leafdrip shock, annual Gavrilović-based rain empirical erosion source rather than independently resolved soil detachment by rain and flow, paper deliberately fixes bed topography during storm, no published centimeter actual mesh numerical validation. Exact author source accessible does NOT imply full code successfully compiled/tested today.
## Additional inspected new source
Current `storm-fsv-cvut/smoderp2d` master source rain/sheet/rill and vegetation interception functions, but NO per-grain sediment erosion/deposition active calculation. Already audited in canonical model. `marcusnobrega-eng/HydroPol2D` has actual source LAI interceptionModel + 2D hydrodynamics but only pollutant build-up/wash-off, NOT physical sediment (canonical models/HydroPol2D.md already existed). Avoid duplicate canonical files and new fake candidates.
## Decision
Archive Gatti paper and model evidence as supporting 2D erosion benchmark, clearly fail single published fully integrated LAI canopy+5cm+interrill/overland+bed source. Source-first searches continue only into unreviewed paper-matched model branches. Failed classic OpenLISEM not reconsidered as rescue.
## Sources
https://iris.cnr.it/retrieve/785de7b1-f0ff-492e-ba95-d3b4b301852f/1-s2.0-S0098300423000663-main.pdf
https://github.com/federicg/smartsed
https://doi.org/10.1016/j.cageo.2023.105362
https://doi.org/10.4408/IJEGE.2023-01.S-04