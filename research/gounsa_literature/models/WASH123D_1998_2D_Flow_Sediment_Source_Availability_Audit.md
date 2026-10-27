# WASH12D / WASH123D (Yeh et al. 1998), original 2D overland + sediment source screening, 2026-10-27

## Precise published lineage
1998 preliminary WASH12D technical report by Yeh/Cheng/Cheng documents 2D overland flow and sediment transport with **kinematic/diffusive/dynamic-wave options**. 1998 WASH123D USACE CHL-98-19 extends to 1D river/2D overland/3D subsurface and transport/quality. Those names refer to related but non-identical releases; do not assume exactly same solver version.

## 2D scope and experimental evidence
Official CSDMS https://csdms.colorado.edu/wiki/Model:WASH123D describes 2D Overland Regime and 1D river and 3D saturated/unsaturated soil, finite element mesh, integrated sediment transport. A general reactive/sediment transport solver does not prove raindrop splash / rain-and-flow source splitting, soil-stock-limited rill incision and depositional layer geomorphic updating. Same native source in a 5cm model with LAI canopy has **not been documented**.

## Critical original source distribution contradiction
- Exact CSDMS wiki lines 85–89: Model availability `As code`; `Source code availability` and `Source web address` **blank**.
- Exact CSDMS wiki bottom line235: model assigned **Category: Source code not available**.
- Our connected GitHub search `WASH123D` and `WASH12D sediment` returned NO original Fortran repositories; no complete public zip/executable/dataset path found in scholarly 1998 archive.
- Independent review notes source remains privately distributed in other research applications. This is NOT a declaration code does not exist anywhere; it is **NO reproducible all-source as available today**.
- CSDMS indicates old F77/F90 versions run on Windows and Unix; no tested current dependency matrix, build, mass ledger, fine-mesh benchmark.

## Active vegetation/sediment scientific unknown
- No native full LAI × storage/throughfall/leafdrip KE source lines found. Lumping ET/cover in parameter tables is not direct canopy interception.
- WASH12D manual did say **full dynamic option** but no published 5–10cm high-res canopy-on with free X/Y dynamic flow + sediment simultaneously verified.
- No full-paper performance conclusion provided until exact field experiment/methods recovered.

## Strict verdict
**NO-GO currently for user single published complete source model**, despite physics lineage containing true 2D transport. Blockers public source, active canopy hydrology/drip, cm mesh, independent sediment stability. 
References `papers/1998_Yeh_Cheng_WASH123D_2D_Overland_Sediment_TechReport.md`, https://csdms.colorado.edu/wiki/Model:WASH123D .
