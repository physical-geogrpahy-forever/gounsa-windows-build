# SMART-SED — Politecnico di Milano original published C++11 2D hydrodynamic + sediment engine
## Canonical peer-reviewed reference and original identical author's code
Gatti et al. (2023) *Computers & Geosciences* 177 105362, DOI https://doi.org/10.1016/j.cageo.2023.105362 . Exact paper original p.11/12 code availability cites source https://github.com/federicg/smartsed .
Original source public C++11, MPI, Eigen and R geostat preprocessing, real `run/SMARTSED_input_ev`, `Inputs/` mountain catchments. The code README is terse, but paper matches author source and repository. Previous gounsa papers INDEX did not list this original as of this research turn.
## Scientific operations in source
1. `main_final_H.cpp` initializes 2D u,v staggering, DEM, rain, groundwater and soil variables; paper §2 Eq1 bidirectional SWE semi-implicit hydrodynamics.
2. `physics/is_sediment_transport` toggles sediment, `compute_dt_sediment` time substepping; `h_sd` transported through vertical/horizontal staggered boundary fluxes (two directions), grid sediment production `W_Gav` using rainfall, temperature and Gavrilović coeffs; `W_Gav_cum` output.
3. **No original LAI/Smax interception, canopy throughfall/stemflow/drip-KE**, no independently modeled rain-splash vs shear detach.
4. Eq(9) empirical sediment velocity factor `α|∇b|^β`, Eq(10) rainfall-driven Gavrilović original annual sediment production downscaled to events. Note original paper uses temporal extrapolation of annual empirical production rate.
5. Paper explicitly says *orography profile is not changing in time* even when suspended sediment concentration and source maps calculated; no native same-storm erosion/deposition feedback in DEM.
6. Actual studied grids Caldone 20/50/90m numerical based 5m input DTM and Dragone10m numerical, not user 5/10cm actual grid. Output layer positivity claimed by authors not independently tested by this investigator.
## Source code
https://github.com/federicg/smartsed/blob/main/DeterministicProgram/main_final_H.cpp
https://github.com/federicg/smartsed/blob/main/DeterministicProgram/utils_H.cpp
https://github.com/federicg/smartsed/blob/main/DeterministicProgram/Makefile
https://github.com/federicg/smartsed/blob/main/run/SMARTSED_input_ev
## Verdict
Source-authentic strong 2D hydrodynamics/sediment existing model; mandatory original Gounsa canopy interception + separate rainfall/flow detachment + DEM feedback missing. NO-GO for direct deployment. Not compiled/tested in this session.
## Full paper audit
../papers/2023_Gatti_Bonaventura_Menafoglio_Papini_Longoni_SMART_SED_Coupled_Runoff_Erosion.md