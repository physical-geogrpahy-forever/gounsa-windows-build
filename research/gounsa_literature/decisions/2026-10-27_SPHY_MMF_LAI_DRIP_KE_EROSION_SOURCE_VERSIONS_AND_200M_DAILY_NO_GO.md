# 2026-10-27 Non-LISEM independent original SPHY-MMF canopy/drip/rill investigation — 2018 archived release vs 2026 live source

## Decision
**Scientific process verification PASS:** SPHY-MMF published 2018 integrated **LAI-driven canopy water storage, separately modeled direct throughfall kinetic energy and leaf-drip kinetic energy, distinct rain/runoff detachment, within-cell deposition and sediment transport**. The published code is officially archived (Zenodo v2.1.1) and later source is available on GitHub.
**User high-resolution model selection NO-GO:** published 200m, daily, directional channel/LDD routing not free all-boundary XY hydraulic sediment, unfit for 6h storm 5–10cm.

This is a new scholarly/code lineage beyond Classic LISEM/SHETRAN/SWEHR/TREX/AHMS-SED and wasn't in INDEX at start.

## Verified source and papers
- [2018 Eekhout, Terink & de Vente](../papers/2018_Eekhout_Terink_deVente_SPHY_MMF_LAI_LeafDrain_Erosion.md), Earth Surface Dynamics 6:687–703 DOI https://doi.org/10.5194/esurf-6-687-2018. **Published open full text** details 200m model, 1day, direct+leaf KE, rill/interrill, transport, vegetation and snow. Authors explicitly say recommended 200m–1km and daily cannot resolve sub-hourly storms in discussion.
- **Exact old archive** [Zenodo SPHY-MMF v2.1.1](https://zenodo.org/records/1344534), published 2018-08-13, `JorisEekhout/SPHY-v2.1.1.zip` 15.1MB md5 `3b3368227b9bac0b1ddd68e7b74b0bb7`. 2018 GitHub linked release `JorisEekhout/SPHY/tree/v2.1.1` NOT resolvable from connected GitHub (404), zip direct external download in runtime FAILED. **Archive metadata confirmed; original release extracted native code unexamined.**
- **Different current source** [FutureWater/SPHY](https://github.com/FutureWater/SPHY) at master 2026 v3.1.1, exact code SHA and lines in [models audit](../models/SPHY_MMF_2018_2026_LAI_Canopy_LeafDrip_Sediment_Original_Code_Audit.md). `dynamic_veg.py` computes canopy maximum `Smax=0.935+0.498LAI−0.00575LAI²` and canopy water state `Scanopy`, passes net precipitation via `sphy.py` to `mmf.dynamic`. `mmf.py` divides `LD=Rf CC`, `DT=Rf-LD`; canopy KE `KE_LD=LD(15.8 sqrt(PH)-5.87)` if PH≥0.15m, adds KE_DT, raindrop detach F and flow detach H, within-cell deposition. `sediment_transport.py` routes using flow-direction network `pcr.accu*/subcatchment`; **not freely XY 2D**.
- **Important 2018/2026 version mismatch:** 2018 paper Eq14 uses Marshall–Palmer direct-throughfall KE `DT (8.95+8.44 log10(I))`, current 2026 active `mmf.py` uses Brown–Foster `DT*0.29*(1-0.72 exp(-0.05 I))*100`. Can't silently represent 2026 current source as 2018 executed paper software.
- [2021 Eekhout et al.](../papers/2021_Eekhout_MillaresValenzuela_SPHY_Erosion_FiveModel_Ensemble.md) DOIhttps://doi.org/10.1002/ldr.3920 five alternative original SPHY rainfall-/runoff-erosion schemes DHSVM HSPF INCA MMF SHETRAN, daily Mula catchment, climate ±95% etc. **SPHY 'SHETRAN' erosion formula module is NOT standalone SHETRAN hydraulic source or 5cm published SHETRAN test.**

## Why it helps scientifically, not as a main model
- The paper and current source really do distinguish **intercepted rainfall storage [mm]**, **water reaching soil [mm]**, **direct throughfall and leaf drainage for KE [J/m2]**, **two erosion source terms [kg/m2]**, **within-cell deposition**. This directly confronts the misconception that all canopy effects are a single cover coefficient.
- However 2026 code leaf-drainage flux is `post-interception net precipitation × CC` as simplified partition, not explicitly spatial branches and local drip hotspots. Forest oak coppice and Miscanthus parameter calibration is not supplied.
- 200m field calibration cannot be reinterpreted as 5cm plot, and daily runoff cannot represent 6h 10–50mm/h event. Directed routing and bundled deposition aren't full local x/y erosion/deposition.
- Original version v2.1.1 archived but download failed; 2026 code inspected but compiled run not attempted. These are separate facts.

## Final strict criteria
| Native property | Verification |
|---|---|
| LAI dynamic water interception / canopy bucket | YES in 2026 source and 2018 published model |
| Direct/leafdrip KE different pathways | YES formula published and current call path |
| Distinct rain & runoff detachment, deposition | YES published and current code |
| Actual 5–10cm peer-reviewed cell experiment | NO, paper 200m |
| 6h storm sub-minute dynamics | NO, daily |
| Free four-sides 2D x/y advection SWE | NO, PCRaster drainage routing |
| Identical verified historical 2018 source and current master | UNVERIFIED + real KE equation difference |

**No new all-PASS native single model found**. Keep this as strong published plant-rain erosivity benchmark / native process reference only, NOT direct candidate replacement for OpenLISEM fork being handled by Work.

## Index and maintenance
- New papers 2018 SPHY and 2021 ensemble appended and indexed.
- New model code audit file created.
- This decision and session handoff saved.
- No duplicate existing paper by DOI at 2026-10-27 INDEX beginning; full sources anchored DOI, source paths.
