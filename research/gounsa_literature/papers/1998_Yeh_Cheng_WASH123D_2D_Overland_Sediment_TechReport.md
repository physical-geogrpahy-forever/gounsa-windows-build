# 서지정보
Yeh, G.-T., Cheng, H.-P., Cheng, J.-R., Lin, H.-C., & Martin, W. D. (1998). *A numerical model simulating water flow and contaminant and sediment transport in watershed systems of 1-D stream-river network, 2-D overland regime, and 3-D subsurface media (WASH123D: Version 1.0).* Technical Report CHL-98-19, U.S. Army Corps of Engineers, Waterways Experiment Station. Some catalogues use variant title and abbreviated author lists; original report citation corroborated by official CSDMS reference section https://csdms.colorado.edu/w/images/WASH123D_Reference.pdf and ASCE references.
1998 preliminary WASH12D report authors Yeh, Cheng, and Cheng https://www.researchgate.net/publication/235098796_A_Numerical_Model_Simulating_Flow_Contaminant_and_Sediment_Transport_in_Watershed_Systems_WASH12D . Treat WASH12D earlier two-medium and WASH123D three-medium as related lineage, not automatically same binary.

# 연구 선택 이유
원본 `full dynamic-wave 2D land overland + sediment transport + rainfall/interception?` 기성 모델이 고운사 단일 원본 요구에 해당할 가능성 조사.

# 연구 유형
U.S. Army Corps Fortran 77/90 **기술보고서 및 기존 배포 프로그램** 문헌, not journal article. Based on official CSDMS metadata and report references; technical manual text source broadly indexed. Avoid fabricating source line values and mesh resolutions without original reproducible package.

# 공간 구조
WASH123D explicitly 1D stream/river networks + 2D overland flow + 3D subsurface, single hydrological/transport watershed tool (CSDMS metadata lists 8 coupled modes). Earlier WASH12D technical abstract states three flow choices **kinematic, diffusive, full dynamic wave** in overland and channel. This demonstrates *available model options*, not actual high-res 2D dynamic-wave canopy-erosion run.

# 적용 환경
Watershed scale complex surface/subsurface transport. User's 5–10cm grass/oak forest patches and 10–50mm/h storms **not a published field case documented** in reviewed manual and database.

# 핵심 과정
Water transport, 2D overland, sediment transport, contaminant transport, water quality, fluid interactions. A general sediment transport module does **not** by itself establish raindrop impact and overland shear detachment, dynamically stored canopy water, depositional layer and Exner storm morphodynamics at 5cm.

# 식생 입력
CSDMS text and 1998 report abstract do not prove an active LAI-dependent Rutter/Gash canopy storage/throughfall/leafdrip KE solver. Potential hydrological vegetation parameters and evapotranspiration should not be interpreted as evidence of the required canopy rain kinetic terms.

# 핵심식
2D (possibly dynamic-wave) overland mass/momentum conservation and sediment advection module as documented in WASH12D original abstract. Exact detachment source terms and 5cm native code unknown; no transposition of generic formula.

# 파라미터와 단위
Rainfall mm/h, overland discharge m3/s and sediment mass transport units model-specific. **No original cm mesh/dt numeric demonstration found**, so leave unknown instead of conjecture.

# 원본 공개 여부 실제 확인
CSDMS current https://csdms.colorado.edu/wiki/Model:WASH123D lists **'Model availability: As code'** but actual `Source web address`, `Source code availability` fields blank and page is under **'Source code not available' category (bottom L231–235)**. Therefore metadata conflict; not a real tested download link.
Connected GitHub `search_repositories({query:"WASH123D"})` and `"WASH12D sediment"` returned **no matching original Fortran repo**. Cannot claim complete open source even though CSDMS claims code exists at some institution.
Independent 2021 paper review quotes model as 'private-domain source code not accessible'. Source ownership/licence and reproduce case unresolved.

# 고운사에 직접 활용 가능
A methodological precedent for same-framework 2D flow and watershed sediment transport with fully dynamic 2D solver option; potential alternative if original exact code is actually obtainable. **Current reproducible open source FAIL**.

# 새로운 coupling
If grafting a Gash/Rutter canopy and raindrop erosion on WASH123D without original validated source, it becomes a new model and user disallows labeling as existing engine.

# 한계 / 최종 판정
**보류 / 공개원본 없음으로 즉시 채택 불가**. Source URL missing, LAI canopy/rainfall splash not proven, 5–10cm published computed run absent. Original equations and code must be verified in primary report/executable before any promotion.

# 참고
https://csdms.colorado.edu/wiki/Model:WASH123D
https://csdms.colorado.edu/w/images/WASH123D_Reference.pdf
https://www.researchgate.net/publication/235098796_A_Numerical_Model_Simulating_Flow_Contaminant_and_Sediment_Transport_in_Watershed_Systems_WASH12D
https://doi.org/10.4122/1.1000000743
