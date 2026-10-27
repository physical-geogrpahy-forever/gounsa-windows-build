# HydroAS GS–Govers (Hinsberger & Yörük 2025) original software access and 0.25m model audit

## Sources
- Paper https://doi.org/10.1007/s40710-025-00797-9 (original full article HTML)
- Official vendor https://www.hydrotec.de/software/hydroas-en/
- Official download access https://www.hydrotec.de/software/hydroas/hydroas-downloadbereich/

## Actually published active processes
HydroAS FVM 2D SWE rain-on-grid model with Govers transport capacity in add-on GS. Changes in sediment bed elevation via Exner fed back to hydrodynamics, rill erosion at field-scale. Observed cm-res DEM was aggregated to **0.25m and 1m computation meshes**. Ground infiltration explicitly **disabled** by effective rainfall assumption in article §2; rainfall splash erosion **neglected**, no canopy LAI/throughfall/leafdrip hydrological treatment active. User requires canopy-on/off with spatial fine resolution; paper not matched.

## Public source vs binary
Official Hydrotec HydroAS product has commercial licensing, downloads restricted to authorized users, paid subscription and additional sediment modules. Model equation source **not publicly editable** from these pages. Source searches `HydroAS erosion` and `HydroAS source` on GitHub found no matching full solver. Even if binary executable could be licensed, it would not establish open-source requirement.

## Plot results and limitations
Govers transport capacity factor 10, 1.2, 3 needed for different field rills, not transferable automatically. DEM0.25 often more accurate small rill erosion than DEM1, illustrates aggregate DEM false fine-resolution claims. Max 25cm actual mesh, not 5cm.

## Final
**Reject native 5/10cm canopy erosion from this original code**, despite useful genuine 2D rill morphodynamics reference.
