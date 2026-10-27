# 서지정보
Raza, A., Ahrends, H., Habib-Ur-Rahman, M., & Gaiser, T. (2021). Modeling Approaches to Assess Soil Erosion by Water at the Field Scale with Special Emphasis on Heterogeneity of Soils and Crops. *Land, 10*(4), 422. https://doi.org/10.3390/land10040422

# 이 논문을 검색한 이유
기존 473건 모델 목록 외에 식생 패치와 수관차단을 분리하면서 자유 2D 유수침식 수송을 계산하는 **기성 published field-scale model** 누락 여부 확인.

# 연구 유형
Systematic review of 51 retained soil erosion models from >60 reviewed, screening 1D/2D dimensions, vegetation/crop and spatial field heterogeneity, processes, plot/field applications. **Review, not a new native numerical solver**.

# 공간 구조
Explicit discussion of most field-scale models' one-dimensional limitation. WaNuLCAS dynamic crop tree zoning and 2D-like spatial soil loss not same as coupled bidirectional SWE 2D. Also RillGrow, WEPP, EUROSEM, CREAMS, EROSION2D/3D compared under different scales but review tables' `2D` label cannot be equated automatically to free 2D hydrodynamics.

# 과정과 식생
Review explicitly identifies canopy interception in EPIC, WEPP, EUROSEM, CREAMS, SCUAF and WaNuLCAS. Some of these rely on event or daily empirical soil loss, but **no single ready-made 5cm with native canopy and genuine 2D source** is established by the review. Need rill/interrill/transport and canopy same native build test to promote.

# 핵심 식 및 파라미터
No independently new parameterization proposed. Discusses scale-dependent hydrology, detachment/transport/deposition and effect of canopy and crop patch design. No 5cm original solver in the paper.

# 원 논문의 구현 범위와 한계
A review of 51 models, not proof no future or unpublished model can satisfy criteria. Conclusions are especially on heterogeneity of cropland, not steep Korean wildfire sandstone forest. Published 2021 so does not consider later 2022–2026 models.

# 고운사 적용
Independent literature support for **why canopy interception and 2D distributed sediment modelling in heterogeneous vegetation patches are difficult to find in one established plot-scale model**. Use as synthesis, not adoption.

# coupling
Coupling crop/ecohydrology frameworks SIMPLACE/APSIM with 2D erosion is review suggestion, not preexisting single user-required code.

# 최종 판정
**Review supporting evidence only**.

# 참고
https://doi.org/10.3390/land10040422
https://www.mdpi.com/2073-445X/10/4/422
