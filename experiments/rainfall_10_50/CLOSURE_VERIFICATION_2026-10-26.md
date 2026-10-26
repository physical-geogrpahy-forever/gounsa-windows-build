# 2026-10-26 native source reinitialization and hydrology/sediment closure

## Scope and provenance
- SWEHR original `csdms-contrib/swehr` commit `4e6f783f335ac6dc1c116ef0d516c2f3d1b911e2`.
- EUROSEM original `TheSoilman/EUROSEM` commit `8652944da6e1e8436495aa0c08765e2399830dd7`.
- Separate production code from controlled test harness. The published process equations were not replaced with new ad hoc erosion laws.
- Native experiment branch: `swehr-water-sediment-closure-20261026`.

## SWEHR root causes fixed
1. Original code unconditionally imposes an external `j=ny` water+sediment inflow **AFTER** the boundary selection. The original boundary inflow peak water discharge is 0.035 m²/s and suspended concentration up to 500 kg/m³, which invalidates any 'rainfall-only sediment' interpretation.
2. `U[1]` conserved water depth was not explicitly assigned from initial depth `DEPTHINIT`; `SOLID` mask and `M[k]` deposited layer lacked explicit empty initialization. All these are initialized for the rain-only benchmark. `TOTM`, `DEP`, `TOTSED` also initialize explicitly.
3. Published slope topography is unchanged; only original external imposed inflow disabled. j=1 open transmissive boundary for rainfall experiments; closed-box variant for no-input checks.
4. Spatially homogeneous example `KS=0` was changed to a **declared hypothetical** `KS=2e-6 m/s` (7.2mm/h) to exercise the original Green-Ampt infiltration, not to calibrate Gounsa.
5. Native original `F=0.004`, exploratory `a=ad=0.25` for all 5 rainfall-event runs. All comparison runs keep same geomorphic inputs.
6. No source code modifications to governing 2D shallow-water equations, Green-Ampt flux equation, Hairsine–Rose erosion source equations, sediment transport, friction or geomorphic transport.

## Indepedent conservation equations
Water volumes (m³):
```
initial surface volume + rainfall - infiltration - signed outward water boundary flux
+ mixture solids displacement = final surface water volume.
```
Sediment ledger A (kg): `bed_surface_elevation_change*rho_s*(1-phi)*cellarea + suspended_mass + net_outward_sediment_mass = 0`.
Sediment ledger B (kg): `original_soil_detachment - deposited_layer_mass - suspended_mass - net_outward_sediment_mass = 0`.
Sediment ledger C (kg): `bed_surface_elevation_change*rho_s*(1-phi) - deposited_layer_mass + original_soil_detachment = 0`.
All fluxes integrated over actual adaptive numerical `dt` and all edges; no manufactured closure by setting outlet sediment equal to bed difference. Finite-precision residuals printed as `QA_JSON` and `QA_LAYER`.

## SWEHR 3×51 published test topography, dx=0.25m, area=9.5625m²
Same storm intensity for 3600s. Unit conversion: t/ha = (kg/A[m²])×10.

| Intensity (mm/h) | Rain (m³) | Infiltration (m³) | Net water boundary out (m³) | Gross ORIGINAL soil detached (kg) | Final loose layer (kg) | Final suspended (kg) | Sediment boundary out (kg) | Gross detachment (t/ha) | Sediment exported (t/ha) |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
|10|0.095625|0.080486|0.007118|0.0188734|0.0188681|0.00000304|0.00000229|0.01973|0.00000240|
|20|0.191250|0.086021|0.092387|0.0463353|0.0459304|0.00004092|0.00036398|0.04846|0.00038063|
|30|0.286875|0.087916|0.183859|0.0934287|0.0886164|0.00027316|0.00453919|0.09770|0.00474686|
|40|0.382500|0.089108|0.276705|0.1614564|0.1380384|0.00094915|0.02246881|0.16884|0.023497|
|50|0.478125|0.089991|0.370199|0.2494528|0.1809234|0.00218087|0.06634849|0.26086|0.069384|

- All 9 cases PASSED: closed zero-rain no erosion; closed 30mm/h no infiltration or erosion; open 30mm/h infiltration; open 30mm/h short erosion; five 1h rainfall erosion scenarios.
- Strict water relative residuals across full five 1-hour cases: max `2.32e-13`. Strict parent-soil/loose-layer independent sediment relative residual: max `2.22e-13`. Geometric sediment budget less than 0.02% error at 10mm/h, substantially lower at larger events.
- Source run and native evidence: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40254743506 .
- **Numerical closure PASS is NOT calibration or validation against observed Gounsa erosion**, and canopy interception/TF/SF not coupled yet.

## EUROSEM legacy original Fortran native debug audit
- Source fixed-form files compiled with `gfortran -g -O0 -std=legacy -fcheck=bounds -finit-local-zero`; fixed trailing DOS EOF markers and column 72 only. Original 2-plane test input contained **two unconnected elements** and cumulative hyetograph declared **2 pairs despite 3 data rows**.
- For this strictly isolated hydrological benchmark only, set NELE=1 (original first plane 100×145m, slope=0.85, COVER=0.15), removed unused computational order and second gauge row, and corrected `NGAGES MAXND` and `ND` to 3. Event 0min=0, 60min=10..50mm, 100min=constant; 28min recession to `TFIN=88min`.
- Enlarged the two static sediment-summary output fields from `F9.3` to `E14.6` **without altering numerical erosion calculation**; at 40 and 50mm/h the fixed-width original printed '*********'.
- 30mm/h run repeated twice from fresh folders, outputs equal.

| Rain(mm/h) | Native runoff (mm) | Global water balance error (%) | Gross interrill detachment (kg) | Net erosion/deposition (kg) | Water balance pass | Independent sediment balance |
|--:|--:|--:|--:|--:|:--:|:--:|
|10|0|0|0|0|YES|NOT ESTABLISHED|
|20|0.00022|-0.0333|351.043|1.51067|YES|NOT ESTABLISHED|
|30|4.22102|-0.0002|47347.5|47044.4|YES|NOT ESTABLISHED|
|40|12.66189|0.0060|139376|139088|YES|NOT ESTABLISHED|
|50|21.96220|0.0088|238136|237937|YES|NOT ESTABLISHED|

- Water budgets all within 0.034% for the single-plane test, with GNU bounds checks active and all runs exit code 0. This is **hydrological numeric PASS** for original EUROSEM.
- These erosion numbers are very large (50mm/h net result >160 t/ha event) and the published source output does **not** independently integrate rainfall detachment, net loose soil storage, settled sediment and true outlet sediment for a verified closed sediment ledger here. Thus **do not call sediment closure PASS**, and never substitute net erosion for exported yield without an independent model check. The original single-plane program reports `sednet=sedtot+sedin*cmtkg` in eplanel.for, but this identity alone is not a fully independent sediment budget.
- Native proof: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40255588717 .

## Explicit remaining scope
1. Confirm model numerical resolution dependence and positive definite flux for other DEMs; closed water and sediment balances do not imply discretization convergence.
2. Replace hypothetical `KS=2e-6`, `a=ad=0.25` and original test raster with independently determined high-resolution Gounsa soil/rock conditions.
3. Integrate actual interception, throughfall, canopy drip kinetic energy, local stemflow and preferential infiltration WITHOUT model-process duplication; not included in native boundary-only test.
4. EUROSEM needs distinct production-consumption/deposition/export integrals and dry soil layer initial state before sediment balance can be confirmed; do not report its high net erosion as site evidence.
5. Iber+ is the primary event-erosion engine in 2026-09-22 Gounsa model decision; SWEHR/EUROSEM here are engineering benchmarks only. Do not silently override Iber+ selection.
