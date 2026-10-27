# 2026-10-27 23:02 independent non-LISEM original-source audit handoff

## Major newly recovered code
Existing canonical Doten et al 2006 DOI 10.1029/2004WR003829 previously wrote that official PNNL repo lacks forest sediment source. **New historical alternative repo https://github.com/jhamman/DHSVM** entire root source **has it**, and makefile actively lists relevant interception + rainfall momentum + route + sediment + channel objects. Read via connected GitHub file-level C source and blobs.
- `InterceptionStorage.c` L46–65 S(t) rain bucket and `MomentSq` leafdrip/throughfall,
- `InitNewMonth.c` L114–116 dynamic monthly `Smax=LAI*Fract*LAI_WATER_MULTIPLIER`;
- `MassEnergyBalance.c` L270–274 actual call, L277–279 no-canopy direct rainfall momentum;
- `RouteSurface.c` L259–331 sheet runoff flow/raindrop, sediment transport capacity and depositional flux; L392–405 routed by `TopoMap.Dir[n]/TotalDir` not x/y momentum;
- `MainDHSVM.c` L245–74 initializes sed; L319 `SedimentFlag`; L400–412 channel; L431–435 surface;
- `RouteChannelSediment.c` L128–280 sediment exchange and channel deposition.
Direct source study 2006 Rainy Creek **30m 49,085 native cells** and **3h** hydrology step (Wiley article §3).

## Critical actual source defects for user's bare/grass/oak canopy-on/off
1. `RouteSurface.c` L293–295 `DR=0` if no trees/understory → bare impact killed.
2. L261–73 drop impact only for sedoutflow>0, depth>1mm and stream power>0.004 → no independent low-flow raindrop soil detach.
3. L284–92 uses global `VType->` rather than mapped `VType[VegMap[y][x].Veg-1]` for erosivity; all pixels use type0 branch even if hydrology uses mapped types.
4. `MassEnergyBalance.c` L215–220 `if I>10 first`, followed by `else if I>=10 && I<100` middle range only I exactly10.
5. `SedimentFlag` enables kinematic routing; no true XY SWE.
6. unlimited erodible mass published paper; no 5cm native convergence evidence.

## Source status caveats
`jhamman/DHSVM` public historical C source full original makefile but **not 2006 article exact tagged source/inputs** (makefile comment 2006-10 post-dates original Apr publication), no native compile/test of this large old X11/Flex build this turn; only direct static file audit. Public readable does not equal explicit OS license (no root LICENSE file inspected). No UI bitmap/DEM scale mistaken for 5cm simulation.
**This is a genuine correction of prior false 'no sediment code' statement** but not an all-pass model.

## Archived files
- `models/DHSVM_Doten_2006_Original_Open_C_Sediment_Canopy_Execution_Path_2026.md`
- amended `papers/2006_Doten_DHSVM_Mountain_Forest_Sediment.md`
- `decisions/2026-10-27_DHSVM_DOTEN_LEAFDRIP_SEDIMENT_ORIGINAL_C_RECOVERED_BUT_BARE_PATCH_FAIL.md`
- this handoff, update `MASTER.md` and `INDEX.md`.
OpenLISEM is assigned Work, not touched. Existing source prior [`models/SEIMS_2026_Storm_Source_Callgraph_Canopy_And_Sediment_Unit_Audit.md`] found unit issue; avoid duplicate.
