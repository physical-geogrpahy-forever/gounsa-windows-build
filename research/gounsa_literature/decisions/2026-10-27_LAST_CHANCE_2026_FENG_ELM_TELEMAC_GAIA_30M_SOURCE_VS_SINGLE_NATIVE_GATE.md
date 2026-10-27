# 2026-10-27 마지막 독립 원본 소스 연구: 2026 Feng revised 2D sediment package 실제 공개와 30m 단일모델 조건 탈락

## 확실하게 새로 확보한 출처
- [Feng, Tan, Xu, Li & Bisht (2026)](../papers/2026_Feng_Tan_Xu_Li_Bisht_ELM_TELEMAC_GAIA_Harvey_Sediment.md), Water Resources Research 62 e2025WR042040 DOI10.1029/2025WR042040, published May11 2026. Wiley original article §§2.2,3,4, Availability full HTML inspected.
- **Original modified source archive indeed published** [Zenodo v2](https://zenodo.org/records/18331808) DOI10.5281/zenodo.18331808 Jan21 2026, Data_Scripts_Harvey_Sediment_v2.zip **8.2GB**, md5 efdf94753cd7f29cd8476bf71abb9ff6. Archive lists src/ modified TELEMAC/GAIA source, Data/, Scripts/, shpfiles/. **Only archive metadata and listing were verified, zip NOT extracted, code NOT compiled/run**.
- Actually published ELM land runoff/erosion source + 2D TELEMAC fluid + GAIA sediment transport/deposition/Exner, and newly developed GAIA ELM source term mapped cell-to-cell. THREE coupled models, not existing single independent code.
- Real 442,277 triangular mesh finest **~30m**, tributaries ~90m and periphery ~1000m; 1h land output, smaller hydraulic steps. Baseline DEM30m, rainfall forcing1km. Cannot call this 5–10cm simulation.
- Hurricane Harvey Houston sediment deposition 8m million cubic meters and 16 gauge water level median R²0.83 KGE0.78 not 5cm cell sediment and LAI canopy direct/drop energy experimental validation. Dynamic canopy state code path, leafdrop kinetic impact, four sides open on small plot NOT checked.

## Distinct already-screened 2026 source not rediscovered
- [Braga, Martínez-Aranda & García-Navarro (2026)](../papers/2026_Braga_SERGHEI_SE_Finite_Volume_Evaluation.md), DOI10.3390/w18151870, and [SERGHEI-SE code lineage](../models/SERGHEI_SE.md) were already in INDEX. Published **5mm** erodible bed dam-break case; **1m** rainfall hillslope/V benchmark; author future work includes vegetation. 5mm native dam-break must not be represented as 5mm canopy rainfall erosion.
- Classic OpenLISEM 7.5.2 canopy+2D runoff+sediment code exists but prior native erosion dt convergence failures remain, user gave its code repair/test to another Work; no simulated pass here.

## Binding user requirement and result
- Single published executable, source matching paper and code hash, 5/10cm real computation, 6h 10–50mm/h rainfall, LAI dynamic interception and leafdrop KE, genuine x/y freely opening flow, rain+flow detachment+advection+local deposition, positive mass/finite soil stock and timestep/mesh convergence.
- New Feng source **deposited but different three-model coupling and 30m**. Already-screened Braga native 5mm not rain/canopy. Neither qualifies.
- This is an actual discovery of an open modified-source research archive, NOT proof same full three-engine stack reproducible, and NOT a qualifying single native model. Current strict all-PASS=0, not universal proof no suitable model exists.

## Sources
https://doi.org/10.1029/2025WR042040
https://zenodo.org/records/18331808
https://doi.org/10.3390/w18151870