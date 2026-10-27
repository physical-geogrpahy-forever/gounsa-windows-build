# 2026-10-28 HEC-HMS 4.14 one-existing-program integrated canopy and 2D sediment discovery
## Why this candidate is different
USACE official v4.14 manual directly confirms native Gridded Simple Canopy, bidirectional 2D Diffusion Wave runoff and 2D Sediment Transport (sheet/splash raindrop detach, flow erosion, non-equilibrium sediment transport, deposition and bed elevation/layers) are configurable in the **same original executable project**, with canopy explicitly compatible with 2D transform. This is NOT based on combining equations from separate published models.
## Hard limits
Official binary free and available but complete original engine source not obtained, HEC policy generally discourages open source distribution. LAI native mechanistic interception, canopy drainage/leafdrip KE not demonstrated. External LAI to canopy capacity spatial raster is model input parameterization. No genuine 5 or 10cm computational numerical proof, HEC subgrid-resolution DEM should not be confused with actual numerical cell resolution. No native full 2D canopy + sediment run or supplied exact sample project built/verified. Release 4.14 fixed older 2D sediment output bugs; this does not constitute external validation.
## Decision
HEC-HMS 4.14 first NEW single-executable *binary-available alternative*, not GO if full source and 5cm numerical stability are mandatory. Original OpenLISEM v7.5.2 NO-GO persists, authors-only tRIBS-FEaST integration unavailable. If research insists on full public source, reject HEC-HMS rather than falsely advertise it. If native binary allowed, one bounded smoke test of 2D canopy ON + 2D Sediment Transport, followed by 5/10cm timestep/mass validation, is necessary before adoption.
## Sources
https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.14/subbasin-elements/selecting-a-canopy-method
https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/transform/2d-diffusion-wave-model
https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.14/erosion-and-sediment-transport/subbasin-sediment
https://www.hec.usace.army.mil/software/hec-hms/downloads.aspx
https://www.hec.usace.army.mil/SOFTWARE/distribution_policy.aspx
https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.14/release-notes/v-4-14-0-release-notes
## linked model lineage
../models/HEC_HMS_2D_Sediment.md