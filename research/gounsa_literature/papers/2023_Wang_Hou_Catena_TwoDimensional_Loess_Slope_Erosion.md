# 서지정보
Wang, T., Hou, J., Li, J., Li, P., Tong, Y., Zhang, N., Cheng, S., Li, J., & Li, Z. (2023). A novel two-dimensional numerical model developed for slope soil erosion. *CATENA, 232*, 107387. https://doi.org/10.1016/j.catena.2023.107387. Publisher abstract: https://www.sciencedirect.com/science/article/pii/S0341816223004782
Predecessor conference (different authors and version): Wang, T., Hou, J., Tong, Y., Zhao, J., & Wang, F. (2022), EGU22-1885, https://doi.org/10.5194/egusphere-egu22-1885 ; draft preprint SSRN https://doi.org/10.2139/ssrn.4001207.

# 이 논문을 검색한 이유
OpenLISEM Work와 분리된 **타 저자가 실제 시험한 독립 원본 2차원 침식 및 세류 형성 모델** 조사. 사용자 필수 조건인 검증된 native 0.05-0.1m, LAI/수관저류/수관적하, 실제 X/Y 양방향 유동, 직접/유수박리와 퇴적, 논문 일치 source를 확인하기 위해. 사전 확인한 `INDEX.md` 496편에서 동일 DOI 및 2023 Wang 이 논문이 없음.

# 연구 유형
동료심사 original numerical erosion-method article and original experimental rainfall laboratory validation. Full 2023 CATENA manuscript is paywalled in current retrieval: **Elsevier published abstract+visible introduction, 2022 EGU conference abstract, SSRN bibliographic abstract verified, but 2023 manuscript's exact equations, input configurations and numerical test tables not available in full**. Hence neither full 2D SWE nor exact mesh size to be asserted without direct equation-level proof.

# 공간 구조
Paper: explicitly 'two-dimensional slope erosion numerical model', rain-runoff, sediment transport and spatiotemporal erosion mapping. Introduction explicitly criticizes 1D models and wants evolving rill topography feedback. This is evidence of a truly planar numerical ambition, **but specific full 2D momentum SWE vs diffusive/local inertia simplification not accessible without full methods text**. Unlike shallow-sheet 1D profiles, paper plots spatial erosion contributions.

# 적용 환경
Chinese Loess Plateau slope rainfall-simulation experiments, **loess transport capacity correction**. Its corrected sediment capacity empirical coefficients have no independent validity for Gounsa's sandstone, rock fragments, sparse oak and Miscanthus. Do not extrapolate physically.

# 핵심 과정
An independently measured loess-slope sediment carrying-capacity formula is used within 2D rainfall-runoff and sediment transport predictions. Paper abstract says simulation reproduces runoff, sediment variation and spatial erosion contribution. The main erosion intensity is middle/lower slope, with source-area contribution. 2022 EGU precursor reports 1–4m part contributes **69.59% of total erosion** for that laboratory slope. This quantitative finding is from the *precursor* and should not be automatically assigned to the finally published 2023 model configuration.

# 식생 입력
Full abstract and accessible paper intro **do not report LAI, canopy storage, throughfall, leaf-drip kinetic energy, stemflow or Rutter/Gash model**. Indoor loess-slope experiment is not Gounsa oak/grass canopy plot. Lack of mention in abstract is not proof logically absent from full inaccessible manuscript; mark 'not verified', not false absolute negative.

# 핵심 식
Corrected formula for loess sediment transport capacity + two-dimensional runoff/sediment erosion/morphodynamic scheme. **Exact capacity formula, H-R/Govers transport, continuity and cellwise change formula could not be extracted from public abstracts** and must not be invented or cited from different models. Exact boundary water conditions and total sediment conservation not checked.

# 파라미터와 단위
Erosion contribution [%] and sediment concentration [mass/volume], runoff rate [volume/time]. Actual published `Δx` [m], Δt [s], DEM coarseness and erosion mask **unknown** from accessible metadata. Lab slope portion 1–4m is a *physical location*, not 1–4m grid spacing. Real 5–10cm numerical cells **not verified**.

# 실제 성능과 검증 범위
2022 original conference abstract (not necessarily 2023 final):
- Runoff NSE=0.83; sediment concentration NSE=0.66;
- Runoff R²=0.89; sediment concentration R²=0.73;
- Runoff relative bias −5.02%; sediment concentration relative bias −1.02%;
- Middle/lower source and 1–4m segment ~69.59% of total predicted erosion.
These are original *model versus rainfall laboratory comparison*, not strictly separated external forest-site validation and not cellwise DEM DoD measurement proof.

# 원본 코드 및 자료 접근
- 2023 CATENA DOI and 2022 EGU abstract and 2021 SSRN preprint provide **no verified exact publicly downloadable executable/source branch/commit, input archive, regression output**.
- Connected GitHub repository searches exact author+erosion and exact paper title produced no matching original sediment solver. **Absence of results does not prove no private lab code exists**.
- Some coauthors have published hydrodynamic methods related to HiPIMS, and upstream **HEMLab/HiPIMS-CUDA** is public GPL-3 source for 2D shallow-water **flood** only; **cannot ascribe that source to the 2023 erosion version** without provenance and sediment routines. Separate program tree and manual identify hydrology/source only.

# 고운사 직접 사용 가능
Important new independent actual experimentally evaluated erosion-process precedent that explicitly maps spatial rill/overland soil sources. Native Gounsa executable, canopy causal effect, 5–10cm and source-matched binary remain unverified.

# 필요한 새로운 coupling
Adding Rutter canopy or modifying soil erodibility to oak/Miscanthus, if unsupported in author original version, constitutes NEW implementation and violates user's requirement if falsely described as existing single original model.

# 최종 판정
**추가 논문으로 등록 / 모델 채택 보류.** Actual 2D slope erosion with rainfall laboratory is supported. Full SWE, active canopy hydrology, 0.05/0.10m calculation and downloadable exact source are **not validated**. Do not propose operational model yet.

# DOI / 실제 자료
https://doi.org/10.1016/j.catena.2023.107387
https://doi.org/10.5194/egusphere-egu22-1885
https://doi.org/10.2139/ssrn.4001207
https://github.com/HEMLab/HiPIMS-CUDA
