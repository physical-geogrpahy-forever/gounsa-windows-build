# 서지정보
Downer, C. W., Pradhan, N. R., Ogden, F. L., & Byrd, A. R. (2015 [published online October 28, 2014]). Testing the Effects of Detachment Limits and Transport Capacity Formulation on Sediment Runoff Predictions Using the U.S. Army Corps of Engineers GSSHA Model. *Journal of Hydrologic Engineering, 20*(7). https://doi.org/10.1061/(ASCE)HE.1943-5584.0001104
Year recorded 2014 for first online publication; volume issue 2015 should be retained in bibliographic citation.

# 이 논문을 검색한 이유
기존 고운사 GSSHA 유역단위 2D diffusive-wave + canopy cover detachment 문헌은 있었지만 **원본 sediment solver가 extreme rainfall에 어떻게 무너지는지** 직접 다룬 연구가 있는지 확인. 새로운 모델이 아니라 선행 numerical/physical failure evidence.

# 연구 유형
US Army Corps original GSSHA/CASC2D-SED erosion transport formulation methodological research. ASCE paper abstract and source metadata checked, full content not freely read in this session.

# 공간구조
GSSHA 2D gridded diffusive-wave overland flow, separate 1D stream channel, raindrop and runoff erosion and deposition.

# 핵심 과정 및 방법
Abstract: GSSHA original CASC2D-SED sediment formulation used rainfall, overland depth and velocity for erosion/transport. Independent tests of CASC2D-SED showed **severe sediment yield overprediction for storm events larger than calibration event**. Study evaluates impact of soil detachment limits and transport capacity formulation. Need actual full paper for numerical quantitative before-after results.

# 식생 입력
GSSHA erosion raindrop factor includes `canopy cover factor` and vegetation cover-management (see separate 2021 Water study DOI10.3390/w13213054). This fact alone is NOT a physical LAI-driven canopy water reservoir or throughfall/leaf-drip model and not a 5cm vegetation calibration.

# 단위 및 해상도
Output sediment yield typically [kg or Mg], rainfall mm/h, flow depth m, sediment concentration and mass conservation; original exact mesh, dt, detachment source equation and threshold **abstract only; not verified**.

# 공개 원본
GSSHA official executable download documented, `CI-WATER/gsshapy` is a Python input/ORM toolkit, **not GSSHA C/C++ executable source**; original all-in-one public Git SHA matching 2014/2015 formulation not found in this investigation. See official GSSHA USACE and research assessment links.

# 고운사에 사용할 수 있는 부분
Shows a real published concern that successful numerical integration and reasonable calibration under some rainfall does **not guarantee extrapolative sediment predictions**. Test severe rainfall 10–50mm/h must include sediment stability/stock not just drainage.

# 한계 및 최종 판정
**Methodological caution (not new valid main engine)**. No published 5/10cm + native LAI canopy/drip + complete open original demonstration; same basin case precipitation larger than calibration significant errors. Do not collapse water balance and sediment numerical stability.

# 참고
https://doi.org/10.1061/(ASCE)HE.1943-5584.0001104
https://www.mdpi.com/2073-4441/13/21/3054
https://github.com/CI-WATER/gsshapy
