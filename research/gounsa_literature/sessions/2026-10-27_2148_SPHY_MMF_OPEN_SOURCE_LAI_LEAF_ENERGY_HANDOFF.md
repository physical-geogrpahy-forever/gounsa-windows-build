# 2026-10-27 21:48 KST OpenLISEM 제외 SPHY-MMF 신규 출처 원문 및 소스 수준 인계

## 작업범위
- OpenLISEM 수정과 native 재실행은 별도 Work에게 맡기고 비-LISEM 발표 단일모델 조사.
- SYSTEM.md/INDEX.md/기존 엄격 결정문 확인 후 신규 논문만 등록. Existing 2024 Ion ASTERIX, 2018 Cuomo, 2017 Wei TREX, 2025 AHMS-SED, 2013 Kim tRIBS-FEaST, 2021 Abrantes, WASA-SED etc are **already inspected** and not re-created.

## 이번에 새로 찾은 논문 (2)
1. [Eekhout, Terink & de Vente(2018)](../papers/2018_Eekhout_Terink_deVente_SPHY_MMF_LAI_LeafDrain_Erosion.md), DOI10.5194/esurf-6-687-2018, openly published original 2018 SPHY-MMF source Zenodo10.5281/zenodo.1344534, v2.1.1 ZIP md5 `3b3368227b9bac0b1ddd68e7b74b0bb7`. **2018 source archive listing confirmed; ZIP direct download HTTP/runtimes failed, exact extracted files/compile not verified**.
2. [Eekhout et al.(2021)](../papers/2021_Eekhout_MillaresValenzuela_SPHY_Erosion_FiveModel_Ensemble.md), DOI10.1002/ldr.3920, five alternative physical rain/runoff erosion conceptualizations DHSVM HSPF INCA MMF SHETRAN **run within one SPHY hydrology framework daily**. Do not say independent standalone SHETRAN 5cm.

## Current original code actually read (2026 live, different from 2018)
- [Source code audit](../models/SPHY_MMF_2018_2026_LAI_Canopy_LeafDrip_Sediment_Original_Code_Audit.md)
- [FutureWater/SPHY modules/dynamic_veg.py](https://github.com/FutureWater/SPHY/blob/master/modules/dynamic_veg.py) `Veg_function` NDVI→FPAR→LAI and `Smax=0.935+0.498LAI-0.00575LAI²`. `Inter_function` water bucket with stored state/evap and generated P_eff.
- [sphy.py](https://github.com/FutureWater/SPHY/blob/master/sphy.py) actual order 817 `Precip=dynamic_veg.dynamic(...)`, 1233 `mmf.dynamic(Precip, Runoff)`. Actual source passes net rainfall into erosion.
- [mmf.py](https://github.com/FutureWater/SPHY/blob/master/modules/mmf.py) `Rf=P_eff cos slope`, `CC=min(1,LAI)` optionally, `LD=Rf*CC`, `DT=Rf−LD`, `KE_LD=LD*(15.8 PH^.5−5.87)` for PH≥.15m, rain KE plus leaf KE used for independent `F_i` splash, `H_i` runoff detachment, landuse+rock groundcover, near-cell deposition.
- Major version difference: **2018 paper Eq14 `KE_DT=DT*(8.95+8.44 log10 I)` Marshall–Palmer vs 2026 current active `DT*0.29*(1−0.72 exp(−0.05 I))*100` Brown–Foster**. Do not mislabel code reproducibility.
- [sediment_transport.py](https://github.com/FutureWater/SPHY/blob/master/modules/sediment_transport.py) routes via PCRaster **FlowDir**/subcatchment/accufraction flux, not full xy hydraulic SWE 2D. `sphy.py` date +1 day, published model 200m cells (raw SRTM30m resampled), daily; authors recommend 200m–1km and admit subhourly storms cannot be represented.
- Sample config SedFLAG=0, DynVegFLAG=0 not published 2018 simulation selected flags; no accidental claim article processes disabled.

## Scientific decision
**Very strong published canopy+leafdrop KE+rain/flow detachment+deposition open-source same model precedent**, but **5–10cm free 2D short storm engine = NO-GO** due to 200m/daily directed downstream accumulation. This source is scientifically relevant to canopy physically, not direct replacement original single native model.

## GitHub files updated/created
- [paper 2018](../papers/2018_Eekhout_Terink_deVente_SPHY_MMF_LAI_LeafDrain_Erosion.md)
- [paper 2021](../papers/2021_Eekhout_MillaresValenzuela_SPHY_Erosion_FiveModel_Ensemble.md)
- [model source audit](../models/SPHY_MMF_2018_2026_LAI_Canopy_LeafDrip_Sediment_Original_Code_Audit.md)
- [strict decision](../decisions/2026-10-27_SPHY_MMF_LAI_DRIP_KE_EROSION_SOURCE_VERSIONS_AND_200M_DAILY_NO_GO.md)
- [MASTER.md](../MASTER.md) latest source decision
- [INDEX.md](../INDEX.md) exact per-section count **papers491 models102 decisions98** at update moment (other Work sessions concurrently writing).
- this handoff.

## Next independent academic search
Seek actual **≤10cm mesh+genuine freely XY 2D+LAI dynamic canopy+separate direct/drop splash and hydraulic rill detachment/deposition+matching publicly archived executable**, after screening 2018 SPHY, 2021 ensemble and 2025 AHMS source. Avoid case where 30m survey DEM is counted as native grid, or daily model split into hourly. Work remains separate from OpenLISEM modification.
