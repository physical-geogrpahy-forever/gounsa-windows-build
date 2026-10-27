# 2026-10-27 독립 신규 논문: 실제 2D 강우침식+지형변화 CCHE2D (2023)와 UAV LiDAR 산지 식생 SIMWE (2026)

## 모델 요구사항과 중복 검증
Work가 OpenLISEM 원본 수정 담당. 본 세션은 고운사 문헌 501개 현재 INDEX 및 MASTER, 기존 2019 SIMWE 연구/2025 Iber+, 2005 PSEM/2025 HydroAS의 탈락 근거를 읽고 다른 연구를 검색. **Jia2023, Adiprana2026은 INDEX에 동일 DOI/저자 논문 없음**, 기존 GRASS SIMWE model file은 있지만 2026 논문 신규 발견이므로 model canonical 추가가 아닌 기존 갱신.

## 새 검증 논문 1: Jia et al. 2023, Journal of Hydrology
- [논문별 상세검증](../papers/2023_Jia_Wells_Momm_Zhang_Bennett_CCHE2D_Raindrop_Rill_Gully_Morphology.md) DOI10.1016/j.jhydrol.2023.129419.
- [NCCHE CCHE2D 버전별 공개상태 감사](../models/CCHE2D_2023_Jia_Raindrop_Morphodynamics_Source_Release_Audit.md).
- Peer-reviewed **same 2D model** actual raindrop erosion, runoff driven overland sediment transport, topography/DEM and gully/channel development tested against UAV repeated surveys and field physical experiment. Continuity ∂h/∂t+∇·(u h)=R, xy velocities.
- Publisher snippet experiment rain 30→105mm/h t=360min with baselevel lowering, one grain 0.05mm, rain-induced model actual morphodynamics. Paper term 'high resolution mesh' but **actual computational Δx not yet verified**; UAS surface observations are not native mesh proof.
- NCCHE official downloads offer free legacy 32bit model binaries+GUI and 64-bit limited trials, but full CCHE2D commercial and **exact 2023 Jia patch source/run data not openly deposited**. Generic CCHE2D-Sed module does not demonstrate rain-splash patch in downloadable binaries. Published LAI canopy storage/drain/drop KE not shown.
- **Scientific geomorphic precedent high; original public single-model for gounsa NO-GO**.

## 새 검증 논문 2: Adiprana & Samodra 2026, Earth Surface Processes and Landforms
- [논문별 상세검증](../papers/2026_Adiprana_Samodra_SIMWE_Lidar_Vegetated_Landslide_Erosion.md) DOI10.1002/esp.70329. Published 2026-06-25 by Wiley 51(7) e70329. Kalisari landslide Indonesia, **UAV LiDAR spatial erosion-deposition, actual vegetated and non-vegetated steep terrain**, unlike agricultural examples.
- Events: 84mm/h 30min, 38.2mm/h 65min; infiltration field vegetated72mm/h vs bare30mm/h, reversed infiltration tests isolate soil hydraulic effect. Simulated water depth ~1cm vegetation vs ~4cm bare under 84mm/h corroborated by observed video order of magnitude. Infiltration changed sediment maps, but this **does not isolate canopy interception effects**.
- Original GRASS `r.sim.water/r.sim.sediment` available as open source and [existing canonical SIMWE audit](../models/GRASS_SIMWE_RSimTerrain.md). SIMWE Green-function/Monte Carlo stochastic **2D spatial runoff and sediment but not full transient finite-volume Saint-Venant SWE**. The article admits *steady-state assumptions* and erosion magnitude uncertainty.
- Input **LiDAR-derived DEM cell resolution vs actual model numerical grid unspecified**, must not claim 5cm. Field infiltration/rain/morphology input files and GRASS command scripts available on request, not instantly public. LAI→C(t)/leaf-drip KE **not native**.
- **Useful high-rel vegetated steep-slope process and infiltration-vs-canopy confound precedent**, strict user all-original 5cm canopy 2D NO-GO.

## Conclusion
New differentiated valid literature: two papers showing (a) dynamic true 2D rain+runoff morphology and (b) forest/vegetation slope spatial erosion 2026 with open runnable solver. But neither together nor individually supplies **same released executable 5–10cm vegetation LAI dynamic canopy water/throughfall, free xy 2D water/sediment, rain/flow detachment and local deposition with published numerical stability**. Do not launder CCHE free trial binary to actual author code or count drone DEM point spacing as solver Δx. No native run performed.

## Source URLs
https://doi.org/10.1016/j.jhydrol.2023.129419
https://www.ncche.olemiss.edu/downloads/
https://doi.org/10.1002/esp.70329
https://grass.osgeo.org/grass-stable/manuals/r.sim.sediment.html
