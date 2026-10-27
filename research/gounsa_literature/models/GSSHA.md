# GSSHA (USACE ERDC) — available integrated canopy+2D diffusive runoff+sediment native software
## Model version and 2026-10-28 new audit
Official USACE free original executable latest independently evidenced GSSHA v8.0 announced 2024-10-07: https://www.erdc.usace.army.mil/Media/News-Stories/Article/3924653/gridded-surface-subsurface-hydrologic-analysis-model-version-80-released/ . Download wiki https://gsshawiki.com/GSSHA_Download returns HTTP403 to automated inspection, binary NOT downloaded, source NOT obtained, no original code compiled.
2010 Downer et al. USACE ERDC TN-SWWRP-10-3 https://gsshawiki.com/images/9/92/Sediment_TN.pdf indexed text establishes:
- overland 2D diffusive hydrology and 2D explicit advection sediment.
- rainfall and runoff detachment, particle-size-dependent transport, original/parent soil, suspended sediment and deposited loose layer as three native inventory bins, local deposition and preferential remobilization.
- optional DEM cell elevation updates **carried forward to next event**, not proven dynamic during event.
- improved detachment limits to reduce old CASC2D-SED overestimation; 2015 Journal of Hydrologic Engineering Downer et al. DOI10.1061/(ASCE)HE.1943-5584.0001104 tested storm extrapolation, prior excessive sediment yield warning.
Real 2023 peer reviewed forest GSSHA case https://doi.org/10.21926/aeer.2301022, original publisher §2.3 proves LAI→canopy storage via α0.2mm LAI−1, 5×5m actual model mesh, 10s model time step, Pinus/Eucalyptus; study tests hydrology/harvest positions NOT sediment. The same model product has both capabilities but **same-run activated canopy+sediment and independent LAI-only effect NOT established by this paper**.
GSSHA Primer original indexed text "interception coefficient b and storage capacity a": i(t)=r(t) while cumulative I<=a, afterward i(t)=b*r(t). Historic GSSHA manual units for b differ or appear inconsistent vs formula; original 2023 paper labels coefficient mm/h; **do not assert physically separate dynamic Rutter throughfall/dripping**. This is empirical two-parameter native canopy interception; LAI used for a as 2023 external mapped vegetation parameter, not leafdrip KE.
Forest 2023 model default overland scheme is ADE 2D diffusive wave, not full momentum SWE; 5m genuine computational grid vs user5–10cm UAV DEM.
Original source: binary distributed free but exact complete C++ 8.0 public GitHub source not located. Published independent EarthSim docs explicitly call GSSHA simulator currently closed source https://earthsim.holoviz.org/user_guide/index.html ; GitHub CI-WATER/gsshapy is Python wrapper only. GSSHA academic/HPC catalog may say public-domain/OpenSource but this does NOT prove source bytes are actually publicly downloadable.
## Applicability and checks
Advantages over abandoned OpenLISEM: no known original 7.5.2 dt catastrophic failure documented for GSSHA, separate finite soil/susp/deposited masses (theory), officially distributed 8.0 executable, both canopy and flow/sediment in one native product. **Absence of observed numerical failures is not evidence of cm stable outputs**.
Critical missing: actual downloadable 8.0 binary checked, full native erosion source accessible, 5/10cm native numerical benchmark, four-edge open boundary and sediment export, rain KE with leafdrip, canopy-on/off sediment trial, finite soil/bed budget, intra-event bed feedback (only event-to-event supported). DO NOT declare ready.
## Evaluation status
For original **executable rather than source** user intent, GSSHA is a worth-audit candidate after new discovery. Under full original-source requirement it is **NO-GO currently**. Even if binary free, still source and cm validation not done. Do not casually "solve" by adding custom interception or using cover fraction alone.
## Sources
- ../papers/2010_Downer_Ogden_Pradhan_Liu_Byrd_Improved_GSSHA_Erosion.md
- ../papers/2023_Garcia_GSSHA_Forest_LAI_Interception_Harvest.md
- ../papers/2014_Downer_Pradhan_Ogden_Byrd_GSSHA_Sediment_Transport_Limits.md
- https://www.erdc.usace.army.mil/Media/News-Stories/Article/3924653/gridded-surface-subsurface-hydrologic-analysis-model-version-80-released/
- https://www.lidsen.com/journals/aeer/aeer-04-01-022
- https://earthsim.holoviz.org/user_guide/index.html
