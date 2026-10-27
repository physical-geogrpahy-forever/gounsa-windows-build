# 서지정보
Eekhout, J. P. C., Millares-Valenzuela, A., Martínez-Salvador, A., García-Lorenzo, R., Pérez-Cutillas, P., Conesa-García, C., & de Vente, J. (2021). A process-based soil erosion model ensemble to assess model uncertainty in climate-change impact assessments. *Land Degradation & Development, 32*(7), 2409–2422. https://doi.org/10.1002/ldr.3920

# 이 논문을 검색한 이유
서로 다른 침식식이 **실제 오픈소스에서 같은 LAI 수관수문 코드와 연동**돼 있는 연구인지 확인하고, 모델 개별 기능과 2차원 유동을 혼동하지 않기 위해.

# 연구 유형
동료심사된 분포형 물리기반 침식모델 앙상블 개발 및 스페인 남동부 반건조 유역 기후변화 시나리오 비교.

# 공간 구조
SPHY hydrological raster with LDD/PC-Raster direction-based water/sediment routing; **genuine unrestricted XY shallow-water hydraulic finite volume and 5cm sediment interface not model scope**. Daily temporal timestep, catchment/regional grids; exact paper mesh dimension not separately verified.

# 적용 환경
Spanish Mula semiarid catchment, extreme precipitation/soil erosion changes under global warming +1.5/+2/+3°C scenarios. 5cm forested hillslope six-hour event not experimentally simulated.

# 핵심 과정
Five rainfall- and runoff-based physically motivated erosion conceptualizations **DHSVM, HSPF, INCA, MMF, SHETRAN** encoded *within the SPHY hydrological model*. Raindrop detachment, runoff detachment and within-cell immediate deposition; model selection implemented as `SedModel=2..6`, not running all erosion formulas simultaneously.
- 2026 latest Github `FutureWater/SPHY/sphy.py` source `SedModel==2` MMF, 3 INCA, 4 SHETRAN, 5 DHSVM, 6 HSPF. Separate module files in `modules/*.py`.
- Source code physically within common SPHY, **not proof standalone SHETRAN version 4.7.2 spatial equations nor 5cm source app**.

# 식생 입력
SPHY native NDVI→LAI→canopy storage via `dynamic_veg.py`; separate cover, rock fraction and soil erodibility. Original exact published 2021 config/option dynamic canopy active is not verified in this research; source option presence is true.

# 핵심 식
Compare detachment rain/sheetflow and deposition equations for each method from original cited publications, no conflate separate SedModel choices. Refer [2018 actual MMF equations](2018_Eekhout_Terink_deVente_SPHY_MMF_LAI_LeafDrain_Erosion.md) for KE=KE_LD+KE_DT and rill/interrill. For 2021 source code `modules/shetran.py` is a rewritten **erosion equation module inside SPHY**, not source of the full SHETRAN hydrodynamic model.

# 파라미터와 단위
Daily time step explicitly published. Monthly/annual soil loss scenario response ±95% increase to −30% decrease climate cases, model uncertainty increasing with extreme rainfall/slope/runoff. Not numeric 5cm erosion convergence.

# 원 논문의 구현 범위
Five equations family integrated as switchable modules in one SPHY hydrological platform; published landscape scale scenario sensitivity study, separate model uncertainty.

# 고운사에 직접 사용할 수 있는 부분
Benchmark of physical detachment conceptualization differences due to rainfall vs flow and deposition as independent model uncertainty; canopy/erosion physical submodules available in public software.

# 새로운 coupling이 필요한 부분
Free 2D shallow-water with open all sides, 5cm source-adequate sediment transport and within-event rainfall and sediment time step would be novel development, not published 2021 engine.

# 한계
2026 present Github version not identical to 2021 article release; v2.1.1 Zenodo2018 is also prior to 2021 ensemble and cannot be claimed to contain all post-2018 ensemble modules. Needs precise historical 2021 source SHA for strict executable consistency. No compile/run here.

# 최종 판정
**보조근거: confirmed published process-based erosion family software, not native 5cm 2D event model**.

# 링크
https://doi.org/10.1002/ldr.3920
https://onlinelibrary.wiley.com/doi/10.1002/ldr.3920
https://github.com/FutureWater/SPHY
https://github.com/FutureWater/SPHY/blob/master/sphy.py
