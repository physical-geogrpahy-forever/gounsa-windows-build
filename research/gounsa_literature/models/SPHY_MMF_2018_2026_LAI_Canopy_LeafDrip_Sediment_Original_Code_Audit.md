# SPHY-MMF published native canopy, leaf drainage, raindrop/flow erosion and sediment code audit (2018 vs 2026)

## 정확한 연구/코드 계보
1. **2018 논문** [Eekhout et al.](../papers/2018_Eekhout_Terink_deVente_SPHY_MMF_LAI_LeafDrain_Erosion.md) Earth Surface Dynamics DOI10.5194/esurf-6-687-2018. 원논문 §2.2–2.3 canopy/erosion complete equations, §3.2 실제 200m model grid, §4 daily and recommended 200m–1km.
2. **2018 실제 연구소스** Zenodo https://zenodo.org/records/1344534 **v2.1.1**, published 2018-08-13, 15.1MB `JorisEekhout/SPHY-v2.1.1.zip`, verified published DOI link, MD5 `3b3368227b9bac0b1ddd68e7b74b0bb7`. Zenodo points to GitHub https://github.com/JorisEekhout/SPHY/tree/v2.1.1 ; connected GitHub fetch v2.1.1 gave no ref 404, download from Zenodo in this runtime FAILED. **2018 ZIP code file-by-file contents and executability therefore unverified**, *2018 paper formulas* separate from *present public master code*.
3. **2026 current live C/Python code** https://github.com/FutureWater/SPHY , `sphy.py` main 2026 Apr v3.1.1 (blob SHA `cdc7d3073abb173eb2aa1714a557b8968beada22`), `modules/mmf.py` `3a7ef3e227126a4f7bcefbb0cf8da73183b53a39`, `modules/dynamic_veg.py` `7595963323020b09e1e80a2b995b76372860d54a`, `modules/sediment_transport.py` retrieved source. GitHub master newer version **not exact archived 2018 run**.

## 실제 작동 식과 호출 연결 (2026 source verified)
- `modules/dynamic_veg.py::Veg_function`: NDVI→FPAR→LAI, `Smax=0.935+0.498*LAI−0.00575*LAI²` [mm], native canopy reservoir. `Scanopy=Scanopy+Precip`; `Inter_function(Scanopy,Smax,Etr)` returns `PreT=max(0,S−Smax)`, `Int=min(1.5*Etr,S)`, resulting saved `Scanopy` and effective `Precip=PreT`.
- `sphy.py` dynamic() line 817: `Precip=self.dynamic_veg.dynamic(... Precip,ETref)` when `DynVegFLAG==1`; later line1233 `G=self.mmf.dynamic(self,pcr,Precip,Runoff)`. Thus **same run passes canopy-reduced P_eff to soil erosivity**, a real path not just variable keywords.
- `modules/mmf.py`:
  - L198–203 optional canopy fraction `CC=min(1,LAI)` when `CanopyCoverLAIFlag==1` and vegetation enabled; else table.
  - L20 `Rf=Precip*cos(Slope)`; `LD=Rf*CC`; `DT=Rf−LD`. **These partition the soil-reaching post-interception volume for KE estimation**; not a tracked concentration of individual branch drip points.
  - L43 `KE_LD=0 if PH<0.15 m else LD*(15.8 PH^0.5−5.87)` [J/m²] Brandt(1990). Plant height input mm? Source code parameter `PlantHeight` [m] yes paper Eq13.
  - `KE_DT=DT*0.29*(1−0.72 exp(−0.05 PrecInt))*100` **2026 active Brown–Foster formula** [J/m²], while **2018 published paper Eq14 = DT*(8.95+8.44 log10 I) Marshall–Palmer**. **Original published vs live code important version mismatch**. Both cannot be portrayed as identical validated results.
  - `KE=KE_DT+KE_LD`; `F_i=K_i*soil_fraction*(1−GroundCover−RockCover)*KE*0.001` [kg/m²], independent `H_i=DR_i*soil_fraction*Runoff^1.5*(1−Cover)*sin(slope)^0.3*0.001`.
  - MMF deposition `DEP=min(100,44.1 N_f^0.29)` percent, sediment in transport split; `sediment_transport.dynamic_mmf()` calls transport capacity and SedTrans routing.
- `sphy.py` input `FlowDir` for `pcr.accuflux`, `sediment_transport.py` uses `pcr.subcatchment,streamorder,accufractionflux` and runoff through directional network. **Not xy 2D shallow-water solver**, despite raster 2D geometry.
- `sphy.py` L1260 date advance `timedelta(days=1)`; per-day event balance, no internal 1-second hydrodynamic storm routing.
- `sphy_config.cfg` default `DynVegFLAG=0, SedFLAG=0, SedTransFLAG=0` are sample/template settings, not a demonstration published 2018 actually ran all toggles OFF. Published 2018 study reports coupled vegetation/soil modules ON. To reproduce use study runfile not repo default.

## Real published simulation, not image/DEM resolution
- Eekhout 2018 uses **200m computation** (SRTM30m source DEM); upper Segura catchment; original paper itself says SPHY recommended 200m–1km, daily rainfall (5km parent forcing interpolated), daily time resolution misses intense subhourly storm. Official site §4 explicitly admits both.
- 2021 [Eekhout et al.](../papers/2021_Eekhout_MillaresValenzuela_SPHY_Erosion_FiveModel_Ensemble.md) DOI10.1002/ldr.3920 integrates **5 selectable alternative erosion conceptions** DHSVM/HSPF/INCA/MMF/SHETRAN into common SPHY (not running all simultaneously). Separate 2021 historical matching SHA not identified, current source contains switch `SedModel=2..6`. `modules/shetran.py` inside SPHY is **NOT native SHETRAN hydrodynamic code**.

## Gounsa hard gate
| Gate | 2018 published & current code |
|---|---|
| Peer-reviewed integrated canopy + erosion same project | **YES** |
| Historical published original code explicitly archived | **YES** v2.1.1 Zenodo (download failed in this runtime) |
| LAI dynamic canopy capacity from live source | **YES** |
| Leaf drainage and direct KE + separate rain/flow detachment | **YES**, 2026 source and 2018 equations |
| Sediment deposition | **YES** within-cell + transport capacity routing |
| 5–10cm actual plot case | **NO**, 200m |
| One storm 6h/seconds time step | **NO**, daily |
| Unrestricted genuine XY SWE/2D sediment | **NO**, LDD routing |
| Reproducible 2018 source and 2026 code identical | **NO**, KE formula changed, archived ZIP not read |

**Final status: SOURCE+published canopy/erosion process example, Gounsa highres direct main NO-GO**. Even if someone took native SPHY canvas to 5cm, daily + directed routing cannot meet free-2D and event storm. Must not propose source as direct substitute for OpenLISEM Work branch.

## Exact links
https://doi.org/10.5194/esurf-6-687-2018
https://zenodo.org/records/1344534
https://doi.org/10.1002/ldr.3920
https://github.com/FutureWater/SPHY/blob/master/modules/mmf.py
https://github.com/FutureWater/SPHY/blob/master/modules/dynamic_veg.py
https://github.com/FutureWater/SPHY/blob/master/modules/sediment_transport.py
https://github.com/FutureWater/SPHY/blob/master/sphy.py
