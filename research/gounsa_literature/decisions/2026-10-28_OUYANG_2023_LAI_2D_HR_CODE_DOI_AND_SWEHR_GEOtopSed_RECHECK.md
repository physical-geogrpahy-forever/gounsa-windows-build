# 2026-10-28 Ouyang LAI canopy + free XY 2D flow + Hairsine-Rose combined paper and author code DOI

## Decision
Ouyang et al. (2023) DOI10.1029/2022JF006846 is a major *same-published-paper* candidate which natively combines remotely sensed LAI based empirical canopy interception (Aston1979/Hoyningen-Huene1983), Green–Ampt infiltration, bidirectional 2D SWE MacCormack–TVD and five-grain Hairsine–Rose rain/flow detachment, sediment mass/deposition and debris flow morphodynamics in a 2021 postfire steep mountain event. Field comparison inundated modeled59.8ha measured50.1ha, local erosion depths compared. This is not the assistant constructing ad hoc new coupling.

## Exact SOURCE provenance not yet passed
Original Wiley JGR published Data Availability says original source v1.1 deposited Zenodo DOI10.5281/zenodo.7269322, input/rainfall/soils DOI10.5281/zenodo.7269648, but its References cite same software release v1.0.0. Both DOI verified in original journal article. DOI redirects to Zenodo but its landing page / actual archive content denied by available web, container DNS blocked; original exact source files NOT read, compiled or numerically validated. Cannot assert it is actually currently retrievable complete C/Fortran source; code source remains PENDING.

## Actual spatial resolution and hard limits
Paper uses 10m satellite DEM, Landsat 30m and 0.98m optical images; DEM is not proven numerical mesh spacing. No 0.05m/0.1m full native SWE and sediment precedent. Aston LAI canopy is empirical storage (not detailed Rutter stemflow or leafdrop KE). Paper models extreme postfire debris-flow transition 47% solid, not baseline 10–50mm/h subtle bare/oak/Miscanthus patch raindrop energy. Does not verify 4 all-open borders or finite topsoil erosion inventory at cm.

## Source/code recheck and no fake discoveries
SWEHR is ALREADY audited in gounsa 2026-10-26, with author/CSDMS source and 38 spatial modified-fork experiments. Paper vegetation Rutter and canopy shielding features NOT in released 1785 line SWEHR.c, initial GitHub test 0.25m cells and ZERO rainfall, model original field 0.375m DEM, 2.5cm lidar observation only. Reintroducing as NEW was an error, and no GO status update. GEOtopSed Zi2016 DOI10.1016/j.envsoft.2016.06.004 is published canopy+3D hydrology+soil sediment study but uses 1D kinematic routed surface flow, nominal public GitHub TanZiTT/GEOtopSed includes GEOtop canopy rain but inspected tree does not reveal sediment module, thus NO native full source proved. SMARTSED, HEC-HMS, other repeated candidates no status promotion.

## Outcome
**Scientific process: Ouyang original article PASS. Published code DOI: YES declared. Downloaded complete exact source, native verified same-run and sub10cm: NO.** Next meaningful check is retrieval/inspection of Zenodo DOI archive and entrypoint, not another literature title search. No native execution conducted here.

## Evidence
https://doi.org/10.1029/2022JF006846
https://doi.org/10.5281/zenodo.7269322
https://doi.org/10.5281/zenodo.7269648
https://github.com/csdms-contrib/swehr
https://doi.org/10.1016/j.envsoft.2016.06.004
