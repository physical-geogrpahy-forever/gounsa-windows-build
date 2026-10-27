# 2026-10-27 22:52 KST 독립 CCHE2D와 SIMWE 최신 문헌 검증 인계

## 범위와 중복
사용자 지정: OpenLISEM 수정은 Work 담당. 이 세션은 새로운 단일모델 논문과 original source만 조사.
시작 시 SYSTEM.md, MASTER.md, INDEX.md와 기존 모델 탈락결정 확인. Jia 2023 DOI10.1016/j.jhydrol.2023.129419 및 Adiprana 2026 DOI10.1002/esp.70329는 기존 INDEX 논문 파일 부재 확인.

## 새 논문 A: Jia et al.(2023) CCHE2D
- [canonical](../papers/2023_Jia_Wells_Momm_Zhang_Bennett_CCHE2D_Raindrop_Rill_Gully_Morphology.md) Journal of Hydrology 620:129419.
- 2D true xy surface hydrodynamics (h,u,v), raindrop detachment, soil entrainment/transport, measured sediment loss and topographic rill/gully network response against UAS repeated survey.
- Paper experimental rainfall example 30 to 105mm/h after360min with downstream baselevel lowering, grain0.05mm. Exact computational mesh cell size NOT verified; high-resolution LiDAR/photogrammetry is not proof of 5cm numerical cell.
- [CCHE2D code release audit](../models/CCHE2D_2023_Jia_Raindrop_Morphodynamics_Source_Release_Audit.md): official NCCHE https://www.ncche.olemiss.edu/downloads/ provides unsupported old free 32bit GUI and limited 64bit trials. Full software commercial. Exact Jia 2023 soil splash patch and runfiles/full editable source NOT publicly verified, no dynamic LAI canopy/leafdrop KE.

## 새 논문 B: Adiprana & Samodra (2026) forested/vegetated landslide SIMWE
- [canonical](../papers/2026_Adiprana_Samodra_SIMWE_Lidar_Vegetated_Landslide_Erosion.md), ESPL 51(7) e70329; DOI10.1002/esp.70329, first published June25 2026.
- Kalisari active landslide Java Indonesia UAV LiDAR site; rainfall 84mm/h30min and 38.2mm/h65min; infiltration vegetation72 vs bare30mm/h, swapped scenario reveals infiltration influence; water depth vegetation about1cm and bare about4cm under intense event.
- GRASS GIS source public, green-function stochastic 2D SIMWE for spatial erosion/deposition, NOT full transient 2D SWE. Vegetation controls infiltration/roughness rather than explicit LAI dynamic canopy interception/drip.
- Actual numerical grid resolution not known from accessible abstract; author-request only inputs and GRASS setting/scripts, paper itself cautions steady-state and sediment magnitude uncertainty.
- Existing [GRASS SIMWE](../models/GRASS_SIMWE_RSimTerrain.md) appended with this 2026 follow-up.

## Overall decision and archive
- [new strict two-model decision](../decisions/2026-10-27_JIA_CCHE2D_2023_AND_ADIPRANA_SIMWE_2026_SOURCE_VEGETATION_HIGHRES_SCREEN.md)
- New papers x2, CCHE2D model audit x1, GRASS SIMWE canonical updated, MASTER and INDEX updated.
- Indexed snapshot: Papers506 / Models108 / Decisions105 (other Work may update). No model runs or claims of 5cm native success.
- Still missing same published 5-10cm code with LAI canopy, throughfall/leafdrip KE, full unconstrained xy hydraulic sediment, both raindrop and overland flow detachment, local deposition and mass/time convergence.
