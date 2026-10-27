# 2026-10-28 Ouyang 2023 and SWEHR model-source audit handoff

New Ouyang et al. 2023 DOI10.1029/2022JF006846 combines LAI-informed Aston canopy interception, Green-Ampt infiltration, two-dimensional MacCormack-TVD shallow water, five grain class Hairsine-Rose rainfall/flow sediment detachment and deposition within one published study, at a steep post-fire mountain basin. Original author source and inputs in Data Availability DOI10.5281/zenodo.7269322 and DOI10.5281/zenodo.7269648. First is called version 1.1 there but v1.0.0 in bibliography. The recorded code bytes and file manifest cannot be retrieved from Zenodo via current tooling, so exact source package is not yet verified or compiled. DEM used 10m; no original 5cm native proof. Canopy leafdrop energy not confirmed.

Original published McGuire SWEHR source recheck is NOT new, and previously 2026-10-26 38 modified runs do NOT provide original Rutter canopy, which is absent from CSDMS 1785-line C source; sampled example 0.25m grid with zero rainfall, field actual computational 0.375m from 0.025m observations. Original remains ineligible.

Zi et al 2016 GEOtopSed canopy interception code found in `GEOtop/vegetation.c` and `energy.balance.c` repo https://github.com/TanZiTT/GEOtopSed, but sediment module not found in inspected 95 tree files; kinematic one direction flow in original paper; no native 5cm.

Files: new Ouyang and Zi paper/model canonical records, new Ouyang decision, MASTER and INDEX actual tree regeneration. Next key verification is to fetch publisher-linked exact Zenodo archive and audit LAI-to-sediment call path in native original, then 5/10cm validation; nothing has been native built this turn.
