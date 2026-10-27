# 2026-10-27 OpenLISEM 수정과 독립적으로 수행한 선행연구 검증 인계

## 사용자가 지정한 역할분담
- **Classic OpenLISEM 7.5.2 코드 수정 및 수치 시험은 Work에게 위임**.
- 본 세션은 수정/새 실행/시간격자 보정 없이 외부 SCI 논문 및 소스 자료만 조사.
- 연구 기준: 5–10cm, LAI canopy storage/throughfall and droplet KE, freely spreading 2D runoff, splash/flow detachment, local deposition, published method + exact public executable.

## 새롭게 발견한 논문 및 코드
1. [Abrantes et al.(2021) 2D bidirectional laboratory runoff/rill/interrill/deposition](../papers/2021_Abrantes_Simoes_2D_TwoDirectional_Slope_Erosion.md), DOI10.2478/johh-2021-0003. 2m×2m, x1% y10%; 2D flood, Horton-SCS, sediment transport. LAI canopy and code not found, actual mesh cell dimension unknown. Official abstract/first page confirmed; entire PDF web.open refused octet-stream, detailed equations not verified.
2. [Li & Tian(2025) multi-layer microphysical canopy interception](../papers/2025_Li_Tian_Microphysical_Canopy_Interception_Python.md), DOI10.1029/2024WR038296; experiment 20/80mm/h, structurally determined beta,p, LAI,G,gamma canopy multilayers. **Python original file names from [Zenodo](https://doi.org/10.5281/zenodo.15045577) verified**, no native 2D sediment/erosion and python files not executed.
3. [Senn et al.(2025) LiDAR VSF throughfall KE](../papers/2025_Senn_Schaefer_Hosseini_Seitz_VSF_ULS_Energy.md), DOI10.1002/esp.70150. ULS 0.5m XY and 0.25m vertical voxel, splash cups field support but model systematically underpredicts KE. No soil runoff/sediment solver.
4. [Katayama et al.(2023) spatial concentrating woody canopy drip energy](../papers/2023_Katayama_Nanko_Jeong_Canopy_Drip_Kinetic_Hotspots.md), DOI10.5194/esurf-11-1275-2023. Single branch drip hotspot TKE 15.2× other canopy /49.7× freefall; field pilot not mathematical erosion model and not transferable as an erosional multiplier.

## Source/implementation distinction
- Existing Long & He 2009/2010 2D SWE+Green-Ampt+modified Gash+rill erosion paper model already logged before this task (MASTER second block), exact source/code or sub-10cm verified match not available. Not counted again as new discovery.
- New four papers expand specific physical/method evidence, **do not resolve simultaneous native full model requirement**.
- Classic OpenLISEM original numerical NO-GO preserved, no change to Work's run.

## GitHub changes
- [decisions model-screen report](../decisions/2026-10-27_INDEPENDENT_NEW_2D_EROSION_AND_CANOPY_PHYSICS_PAPERS.md)
- [papers/ Abrantes](../papers/2021_Abrantes_Simoes_2D_TwoDirectional_Slope_Erosion.md)
- [papers/ Li-Tian](../papers/2025_Li_Tian_Microphysical_Canopy_Interception_Python.md)
- [papers/ Senn](../papers/2025_Senn_Schaefer_Hosseini_Seitz_VSF_ULS_Energy.md)
- [papers/ Katayama](../papers/2023_Katayama_Nanko_Jeong_Canopy_Drip_Kinetic_Hotspots.md)
- [MASTER.md](../MASTER.md), [INDEX.md](../INDEX.md) section paper count473→477 and indexed recent decision links 90→93.
- this session handoff.

## Next independent investigation
- After reading current `MASTER/INDEX`, seek genuinely new publicly released integrated **LAI canopy-on + full 2D sediment runoff + 5–10cm published native same-source**; prefer authors' executable archive provenance over code fragments and never re-select failed native candidates based on process existence.
- The 2025 canopy-only Python code and ULS VSF may be used as independent physical benchmarks **if later validated**, not recast as existing integrated erosion programs.
