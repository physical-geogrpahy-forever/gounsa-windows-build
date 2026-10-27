# HEC-HMS 4.14 — original USACE native canopy and 2D sediment model audit
## Bibliography
USACE HEC (2026), HEC-HMS v4.14 User Manual, Technical Reference Manual, v4.14 release notes. Original 4.14 finalized 2026-09-28. Official executable downloads Windows/Linux/macOS: https://www.hec.usace.army.mil/software/hec-hms/downloads.aspx .
## SAME existing program implemented functionality confirmed by official manual
- Gridded Simple Canopy: cell-specific canopy maximum storage map in mm and coefficient map, rainfall partitioned to canopy storage until capacity and then throughfall. Simple and Dynamic Canopy are other original options. Dynamic Canopy descriptive page says time-varying storage but detailed parameter instructions say maximum storage depth fixed for simulation; dynamic crop coefficient can be time-dependent. Do not attribute detailed Rutter/Gash drainage or kinetic leafdrip to native engine.
- Official HEC-HMS 2D Diffusion Wave Transform explicitly says it can be combined with ALL Canopy, Surface, and Loss methods. Model solves two-direction overland diffusion-wave with implicit finite volume in the HEC-RAS-origin engine. Mesh from HEC-RAS imported into HEC-HMS; single executed application with integrated choices; not an improvised coupling.
- Native 2D Sediment Transport in original Subbasin Erosion method: sheet and splash source from Wei et al. (2009) rangeland formula, hydraulic-flow erosion source, 2D non-equilibrium total sediment FVM on same unstructured mesh, local deposition, sorting, layers and bed elevation outputs.
- Input LAI itself is not the native canopy state equation. Canopy storage raster may be parameterized independently from measured LAI by a documented physical relationship. This is an externally derived model input, not original source modification; LAI impacts canopy water storage but not documented leafdrip KE.
- 2D water is diffusive-wave and two-direction, not full inertia SWE. Small pixel DEM used for subgrid elevation-volume lookup does NOT imply physics solved at that resolution. Actual 5/10cm computational mesh and stability NOT established.
## Release and code provenance
- Official free portable Windows v4.14 installer 205MB portable242MB, Linux313MB. Official 2026-09 release notes include bug fixes for 2D sediment connection time-series off-by-one (v4.13), and bulk-flow aggregation, as well as 2D mesh file support.
- Full official native HEC-HMS engine SOURCE not retrieved; official HEC software distribution policy discourages source release unless case by case: https://www.hec.usace.army.mil/SOFTWARE/distribution_policy.aspx . Free original binary is NOT fully public source.
- 4.14 Upper North Bosque public workshop uses MUSLE and reach routing, NOT verified genuine 2D gridded sediment+canopy example. Native 2D sediment reference manual specifically says tutorial TBD. No 2D native workflow constructed/tested here.
- No same paper demonstrating canopy ON with 2D sediment at 5/10cm, no numerical convergence, no evidence soil finite erodible limit, no explicit canopy drip energy and no verified four-edge open boundaries. Distinguish official documented feature existence from numerical success.
## Source links
https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.14/subbasin-elements/selecting-a-canopy-method
https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/transform/2d-diffusion-wave-model
https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.14/erosion-and-sediment-transport/subbasin-sediment
https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.14/release-notes/v-4-14-0-release-notes
## Verdict
One EXISTING DOWNLOADABLE application with canopy+2D runoff+sheet/splash+flow detachment+deposition documented YES. User HARD source+5/10cm+leafdrip FULL PASS NO. Binary-only alternative for native benchmark, not adoption.