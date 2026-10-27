# CCHE2D 2023 Jia et al. actual original software/provenance audit

## Paper and version
[Jia et al.(2023)](../papers/2023_Jia_Wells_Momm_Zhang_Bennett_CCHE2D_Raindrop_Rill_Gully_Morphology.md) DOI10.1016/j.jhydrol.2023.129419. A **modified CCHE2D hydrodynamic and morphodynamic model** physically integrates rain impact soil detachment, overland shallow sheet flow, concentrated rills/gullies, sediment transport, bed elevation and developing drainage network. Uses repeated UAS photogrammetry (SfM) landscape models and measured sediment flux/landform response. More closely matches user's local deposition/morphodynamic published precedent than static RUSLE.

## Direct hydrology/sediment model evidence
- Publisher article section snippets: depth-integrated Reynolds xy flow velocity u,v; continuity ∂h/∂t +∇·(u h)=R with h=η−ζ. Flow friction locally depends on water depth, roughness changes with rills/gullies.
- Rain increases from 30 to 105mm/h at t=360min with downstream base-level fall, single silt size0.05mm, observed erosion rate steady after t=600min at experimental basin. Example demonstrates rain-driven erosion dynamics and coupled morphodynamics, but **not canopy activity**.
- Heterogeneous tilled cornfield and experimental plot, study calls 'high resolution mesh' without specifying actual cell dimensions in accessible text, so numerical resolution **unverified**, no 5cm claim.

## Official release: not source-public
- NCCHE downloads https://www.ncche.olemiss.edu/downloads/ : legacy **32-bit CCHE2D+GUI** free and **unsupported**, alongside limited 64-bit model tests; newer modular **CCHE2D-SED** available as research-collaboration or commercial fully supported. Official site states CCHE2D moved to commercial copyright at University of Mississippi. Some free binaries do not mean **2023 paper modified original editable full source**.
- https://www.ncche.olemiss.edu/df676675gfhhlnw814/ records distributed CCHE2D+GUI Beta3.29.8 (32-bit) and newer 64-bit sediment trial version. No 2023 exact code hash/runfile ready made download found, GitHub repo search `CCHE2D` returns single unrelated `GHfrankyding/CCHE2D_Coast_V-V`; not the Jia soil erosion module.
- NCCHE sediment module official https://www.ncche.olemiss.edu/cche2d-sed-model/ describes unsteady flow, multiple-size particles, non-equilibrium bedload and suspended transport, bed topography and bank erosion; **generic module listing is not proof that Jia2023 rain splash patch is included in free binary**.
- No source checked as executable and no native numeric run.

## Canopy and experimental limits
- LAI→maximum rainfall interception, dynamic storage/drainage, throughfall, stemflow and leafdrop kinetic energy **not verified in Jia2023 nor NCCHE public module**.
- Original test fields agricultural tilled, canopy-ON/OFF young oak/Miscanthus not studied. Native 5cm temporal+spatial conservation tests absent.
- Boundary in lab base-level lowered downstream, not all four open boundaries proven.

## Hard verdict
YES: peer-reviewed independent same-model full xy 2D water+rain source+flow sediment+DEM landscape evolution.
NO/UNKNOWN: public exact Jia2023 editable source+runfiles, canopy dynamic state, 5cm actual model mesh, 4 open boundaries numeric QA.
**Therefore not eligible as an original publicly available directly usable Gounsa single engine, despite excellent high-resolution geomorphic scientific precedent.**

## References
https://doi.org/10.1016/j.jhydrol.2023.129419
https://www.ncche.olemiss.edu/downloads/
https://www.ncche.olemiss.edu/df676675gfhhlnw814/
https://www.ncche.olemiss.edu/cche2d-sed-model/
