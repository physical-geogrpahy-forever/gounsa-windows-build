# 2026-10-27 신규 명확한 동일 논문 모델 결합 사례: Wei et al.(2017) 산림 TREX, 90m, 수관차단+비세류/세류 박리+XY 이송/퇴적

## 동기
[2026-10-27 독립 CSU CASC2D-SED 소스 감사](2026-10-27_NEW_CASC2D_SED_SOURCE_ARCHIVE_DEEP_2D_CANOPY_GATE.md)는 2003 archived source에 고정 초기저류만 있고 raindrop detachment 없음, 단일 출구라고 확인. 같은 2014 Wei & Kinouchi forest LAI hydrology 개량판과 동일 실행판인지 미확인. 이번에는 저자 Wei의 **2017년 직접 후속 논문을 원문 Methods/식별자/격자해상도까지 확인해 근거를 추가**했다.

## 새 논문 2편 (서로 다른 DOI)
- [2017 Wei et al. JHER](../papers/2017_Wei_Kinouchi_Velleux_Fukushima_TREX_Forest_Interception_2D_Erosion.md), DOI10.1016/j.jher.2017.09.003. 방법론 §4.1 및 원문 PDF 전반 https://www.engr.colostate.edu/~pierre/ce_old/Projects/Paperspdf/Wei-Velleux%20et-al.-2017B.pdf.
- [2017 Wei et al. J Environ Radioact](../papers/2017_Wei_Kinouchi_Yoshimura_Velleux_Forested_Cesium_TREX.md), DOI10.1016/j.jenvrad.2017.01.017. 모델 설명에는 같은 저자들의 modified TREX forest hydrology + rain splash/flow sediment and ^137Cs vegetation wash-off. **^137Cs interception/washoff ≠ water interception**.

## 실제 연구 내부에 들어간 과정 (원논문에서 확인)
1. 2017 JHER §4 hydrological model explicitly builds on Wei & Kinouchi (2014) improved continuous forest TREX. The 2014 paper Smax[mm]=.935+.498 LAI−.00575 LAI² is part of forest study lineage. **2017 run exact LAI input values/canopy drainage C(t) is NOT recoverable from paper/code**.
2. Rainfall, interception, ET, surface storage, infiltration, subsurface, groundwater, 2D diffusive wave XY runoff, 1D channel.
3. Eq1 ∂(A Cs)/∂t + ∂(Cs qx)/∂x + ∂(Cs qy)/∂y = es+eh, es rainfall splash, eh flow net detachment/deposition.
4. Eq2 rainfall-induced splash in paper uses net rain intensity squared and vegetation fraction kv, water-depth attenuation. Mechanical leafdrip-energy of actual oak/grass not modeled as independent process.
5. Eq3 **eh=α w v_s (Cm−Cs)** and modified Engelund Hansen Cm with beta calibration, three size fractions; river sediment deposition via settling. Measured SSC time series (field grabs+turbidity conversion), flux, 2011–2014 net erosion hotspot from maps.

## Resolution and context exactness
- Fukushima Kuchibuto River basin 137km², elevation200–1000m, mean slope9°; **model DEM and land-use data 90m**, rain radar 1km. **Real simulation not 5cm or 10cm**.
- Four-year basin total outputs sand22,000t, silt52,000t, clay5,500t; hydrologic annual St D NSE2011 .93, 2012 .69, 2013 .91, 2014 .80. Those are calibrated basin-scale metrics, **not 5–10cm cell sediment mass/DoD metrics**.
- Actual solver is **2D diffusive-wave**. Modelled physical XY sediment fluxes, but 2D **full Saint-Venant dynamics** unproven. 4-sides free outflow also unproven.

## Public source status
- Historic CSDMS/CSU/WatershedModels TREX archival C source exists [WatershedModels/trex_src_csu](https://github.com/WatershedModels/trex_src_csu) and code reviewed in [models/TREX](../models/TREX.md), Interception-r4.c basic fixed depth **not** LAI动态 canopy.
- Source for **2017 hydrology+sediment improved version** exact GitHub checksum, build, runfile, canopy settings, sediment stock **NOT FOUND** in this review. [CSU TREX-Research](https://www.engr.colostate.edu/~pierre/ce_old/Projects/TREX%20Web%20Pages/TREX-Research.html) cites these two 2017 papers as development, but no complete 2017 source release is proven.
- 2017 JHER original PDF available in web parsed text; screenshot tool twice returned 403 from legacy CSU server. Verified text and ScienceDirect HTML abstract; figures can be described only from original caption/numeric text.
- Exact LAI on 2017 run / canopy-on vs canopy-off ablation not published or coded here; avoid claim of fully quantified canopy effect.

## Meaning for Gounsa
**Important new positive conclusion:** published **single forest-integrated model** with *canopy/interception+2D XY overland+rainsplash+flow detachment+deposition* was indeed used (2017 Wei et al.), not merely possible after ad hoc literature coupling. This differs from historic CASC2D-SED old C.
**Still negative strict adoption:** published mesh90m, original exact published run source unavailable, no published <=0.1m, explicit leafdrip energy absent, all 4 boundaries/free flow and finite soil mass+dt convergence unvalidated.

## Final model selection decision
**Published physical-process architecture: valid precedent, retain and cite**.
**Directly usable unmodified publicly reproducible 5–10cm gounsa single-model: NO-GO**.
Do NOT disregard this 2017 model existence; do NOT present 2017 published hydrology variant as available in unmodified historic archived CASC/TREX C.
Work handles original OpenLISEM code fixes separately; independent research only.

## Links
https://doi.org/10.1016/j.jher.2017.09.003
https://doi.org/10.1016/j.jenvrad.2017.01.017
https://www.engr.colostate.edu/~pierre/ce_old/Projects/TREX%20Web%20Pages/TREX-Research.html
https://github.com/WatershedModels/trex_src_csu
