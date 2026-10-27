# Qu & Duffy (2007) PIHM vs public MM-PIHM vs PIHMSed distinction, original code screening 2026-10-27

## Why
OpenLISEM excluded to user's parallel Work. Determine whether a proven forest hillslope **native LAI interception model** also includes direct/flow storm sediment 2D with open source and cm native use.

## Original research and actual source
Qu & Duffy (2007), *WRR* DOI10.1029/2006WR005752: published **water balance ODE for interception storage h_v** based on intercepted precipitation, evaporation, and throughfall/stemflow on triangular prism watershed mesh.
Current open MM-PIHM https://github.com/PSUmodeling/MM-PIHM README MIT open source and build `pihm`, `flux-pihm`, `flux-pihm-bgc`. CVODE ODE solver and grid-based lateral surface processes. The source now is **not guaranteed the 2007 exact binary** but it is direct PIHM code lineage.

`src/is_sm_et.c` SHA `3a178dd207c69abe520fd7aa766c0c32ff7b11f7` L56–63 chooses projected LAI or monthly LAI; L85–86:
```c
intcp_max = elem[i].lc.cmcfactr * lai * elem[i].lc.shdfac;
```
L113–116 evapores from capped `ws.cmc`. `src/read_lai.c` SHA `4e2d2d496e0ae00e1e78645f06b01f89bf6d833a` parses optional `LAI_TS` input and timestamps. **Genuine native LAI-to-canopy storage and throughfall**, not just cover-factor concept.

## Prove sediment absence from current published builds, not infer from brand
- `src/transpt/` directory actual four C files: `init_solute.c`, `read_tracer.c`, `solute_conc.c`, `solute_transpt.c`: **solute** transport, not mass-balance cohesive soil detachment/rill sediment.
- Model README only hydrologic and eco-biogeochem sources, no `pihm-sed` build target.
- Historical Shale Hills CZO `PIHMSed` describes development of regolith transport, uplift, weathering and tree-throw with PIHM, not published **full 5cm raindrop/overland sediment + active canopy** runnable configuration. `PSUmodeling/MM-PIHM` vs PIHMSed identities not proven same executable.
- Current repo was code-inspected but **not compiled/run**; code exists and current build instructions documented.

## Scientific classification
Native LAI water storage **YES**. Genuine free X/Y full Saint-Venant momentum with cm published run **NOT DEMONSTRATED**. Rain-splash Hairsine-Rose/flow stress and depositional layer **NO in current MM-PIHM runtime branches inspected**. A future manually added soil-transport plugin = user-disallowed NEW coupling, not ready original.

## Verdict
**Strong fully released LAI hydrology reference, NOT high-resolution event erosion engine**. No-guess source provenance. `papers/2007_Qu_Duffy_PIHM_Canopy_ODE_FVM_Watershed.md`.
