# 서지정보
Wei, L., Kinouchi, T., Yoshimura, K., & Velleux, M. L. (2017). Modeling watershed-scale 137Cs transport in a forested catchment affected by the Fukushima Dai-ichi Nuclear Power Plant accident. *Journal of Environmental Radioactivity*, 171, 21–33. https://doi.org/10.1016/j.jenvrad.2017.01.017

# 이 논문을 검색한 이유
Wei, Kinouchi 등의 2014 산림 hydrology + 2017 erosion 연구와 같은 실행 TREX 계보에서 **수관저류 및 식생과 입경별 토사유출 과정이 실제 동시에 작동하는지**, 별도 방사성 세슘 수관세척 과정을 interception water로 잘못 해석하지 않기 위해.

# 연구 유형
관측 유량, 탁도, SS 및 Cs-137 분포를 사용한 Fukushima 산림유역 공간분포형 hydrology–soil erosion–contaminant transport 모델 개발/검증.

# 공간구조
Trex 2D diffusive-wave XY overland and 1D channel, basin137km², SRTM DEM90m and rain 1km; the corresponding study (Wei et al. 2017 JHER) uses 90m for same catchment. **5–10cm native paper model 없음**.

# 적용환경
Fukushima Kuchibuto River forest-dominated mountain catchment, June2011–December2014 137Cs and sediment source.

# 핵심과정
- Hydrologic TREX with rainfall, interception, evapotranspiration, Green-Ampt infiltration, subsurface and groundwater, 2D diffusive overland runoff, 1D channel.
- Soil erosion module: direct rainfall splash (rain intensity squared), water-flow transport capacity, suspended sediment sand/silt/clay and deposition.
- Separate contamination processes: `J_v` radio-cesium **wash-off from forest canopy**; `J_ws` Cs wash-off/soil particle attachment, advective/dissolved transport.
- Vegetation interception of **137Cs inventory** does **not** equal hydrologic canopy water storage or LAI-based rainfall interception. Their effects must be distinguished.

# 식생입력
Vegetation fraction `k_v` (or cover), forest canopy contaminated inventory, canopy Cs wash-off flux. Other 2014 modified forest TREX reference for hydro canopy parameters. Dynamic LAI from native 2017 code not disclosed.

# 핵심식
- Physical hydrological water and sediment conservation from TREX framework; 137Cs mass exchange from vegetation to soil and soil to sediment/stream. Exact equations are in the published PDF sections2.1–2.2, not transcribed due to different scientific focus.
- Results: 2011–2014 0.57TBq 137Cs exported, 17:70:13 clay/silt/sand particulate ratio; net 137Cs rain-runoff wash-off reduction 1.6%.
- Watershed flow NSE .88, SS flux NSE .81 at downstream (article results), **not canopy interception error nor per-cell 5cm sediment mass convergence**.

# 파라미터와 단위
137km² basin, 90m underlying DEM from SRTM/2017 sibling, model years 2011–2014, Cs TBq, discharge m³/s, SS flux mass/time.

# 원 논문의 구현 범위
Published **one modified TREX forest hydrology/sediment/Cs compound** model. No exact publicly downloadable fully matching source executable SHA or 5cm forest splash with LAI water budget tests in this paper.

# 고운사에 직접 사용할 수 있는 부분
Supporting published forest canopy-contaminant-sediment interaction, confirming 2017 modified TREX architecture. For gounsa most relevant physical erosion results from companion [Wei et al 2017 JHER](2017_Wei_Kinouchi_Velleux_Fukushima_TREX_Forest_Interception_2D_Erosion.md) rather than Cs transport.

# 새로운 coupling이 필요한 부분
Fine-grid 2D sediment and actual dynamic LAI hydrologic interception verified code not available. Forest 137Cs wash-off cannot substitute for rainfall throughfall or drop impact.

# 한계
2017 TREX native binary/source exact release and input files missing; 90m rather than 5cm; 2D diffusive hydrology only. No direct raindrop KE leaf height module verified.

# 최종 판정
**보조근거**, 2017 modified TREX model lineage; source/cell resolution fail strict native high-res. Radiocesium interception must not be mistaken for hydrologic interception.

# 참고 링크 / DOI
https://doi.org/10.1016/j.jenvrad.2017.01.017
https://www.sciencedirect.com/science/article/abs/pii/S0265931X17300619
https://www.engr.colostate.edu/~pierre/ce_old/Projects/Paperspdf/Wei-Velleux%20et-al.-2017A.pdf
https://pubmed.ncbi.nlm.nih.gov/28161316/
