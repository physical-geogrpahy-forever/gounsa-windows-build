# 2026-10-28 10cm truly 2D erosion precedent versus currently reproducible canopy+erosion complete source

## Important verified new result
Kim, Jeong, Kim, and Kim (2023), *Water Resources Research* 59 e2022WR033879 DOI10.1029/2022WR033879 publisher Methods §2.2.6 explicitly states 10m×21m hillslope represented by 41,380 **triangular 2D numerical cells, 21,000 nodes, spacing 0.1m (10cm)**, driven by genuinely two-direction dynamic shallow-water and multi-class Hairsine–Rose raindrop-flow detachment, sediment advection and deposition. Separate **1D** geometry at 0.01m must NOT be reclassified as 1cm real 2D. Spatial microtopography sediment distribution genuinely resolved 10cm. Yet §2.2.5 explicitly **BARE soils, no vegetation**, §2.2.2 no infiltration, 2D slope 0.03, 3 walls+1 outlet; complete published tRIBS-FEaST engine exact source still not independently available. Thus a credible **genuine centimeter decimeter erosion benchmark**, not complete Gounsa main model. `papers/2023_Kim_Jeong_Kim_Kim_Microtopography_2D_HR_10cm.md`.

## New source availability effort Ouyang 2023 DOI10.1029/2022JF006846
Publisher §4.5.1–4.5.5 genuinely LAI Aston interception + Green–Ampt + 2D full SWE MacCormack–TVD + five-size Hairsine–Rose rainfall/overland erosion and deposition and explicit published same-event integration. Original paper DOI10.5281/zenodo.7269322 identifies author source v1.1 but bibliography calls software 1.0.0; exact paper shows 10-m NUMERICAL spatial resolution (§6.1) and 10m DEM, not 5cm. Tried `zenodo.org/api/records/7269322` and landing page using web and Python requests; web returns inaccessible, container DNS failure. Source cannot be retrieved or read from this runtime. **DO NOT say downloaded or native built.** This is one-paper strong physics but only declared, not code audited. Code URL remains viable for human browsing https://doi.org/10.5281/zenodo.7269322 .

## Search dead-end audits
GitHub published McGuire SWEHR source is prior repeatedly verified and fails published canopy code; DO NOT rename new candidate. `Daishubinghydraulic/Shallow-water-equations-with-Hairsine-Rose-soil-erosion-equations` github tree contains `README.md` and `code.xls` only (no runnable C/Fortran engine), so filename cannot prove executable. No new full native 5cm canopy+rainfall+flow sediment code verified today.

## Decision
No scientific permission to represent a combination of Kim HR code and Ouyang canopy equations as a pre-published single exact model; that would be new coupling. Strict recommendation remains research-paper evidence for Ouyang full processes and Kim 10cm process mesh, but **original author code bytes+documented 5–10cm same-code fully vegetated benchmark remains unverified**. Focus on exact Zenodo archive access (not new paper volume). Never claim native success without archived program output including grid/time convergence, water and sediment mass, soil inventory and four open edges.

## URLs
https://doi.org/10.1029/2022WR033879
https://doi.org/10.1029/2022JF006846
https://doi.org/10.5281/zenodo.7269322
