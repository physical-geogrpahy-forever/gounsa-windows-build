# Garcia et al. (2023) — GSSHA forest interception by LAI

## 서지정보
Garcia, L. G., Salemi, L. F., Mingoti, R., Cassiano, C. C., Fransozi, A. A., de Faria, V. G., Vettorazzi, C. A., Lima, W. P., & de Barros Ferraz, S. F. (2023). Hydrological Effects of Spatial Harvest Patterns in a Small Catchment Covered by Fast-Growing Plantations in the Neotropics. *Advances in Environmental and Engineering Research, 4*(1), 022. https://doi.org/10.21926/aeer.2301022
Open full https://www.lidsen.com/journals/aeer/aeer-04-01-022

## 검색 이유·유형
검증된 완전 연구프로그램 GSSHA에 정량 LAI 수관 저류가 실제 적용되었는지 확인하는 peer-reviewed original forest application.

## 공간 구조/실제 환경
Brazil São Paulo Itatinga experimental Tinga catchment 85.8ha, Eucalyptus+Pinus 85%, native riparian10%, roads5%. **Actual simulation uniform 5×5 m grid** from 5m DEM; GSSHA 2D overland ADE diffusive wave and 1D channel, 10-second computational timestep. 30-minute measured rain, measured hydrograph and selected periods validation.

## 핵심과정·입력
GSSHA spatial canopy interception storage cap derived from LAI of Eucalyptus & Pinus and assumed interception index alpha0.2mm (journal §2.3); land use-specific storage mm eucalyptus0.64, Pinus1.20, native vegetation1.20, roads0.001, harvested0.001. Other roughness, vegetation transmission, canopy resistances, ET, infiltration and groundwater in model; authors vary harvest positions 30/70% removal. Peak flow/yield response. Original §2.3 full Table1 values.
- Interception coefficient table eucalyptus0.11, pinus0.07, native0.16 (printed as mm/h). **Units potentially inconsistent with some historic GSSHA manual which calls b a proportional coefficient; do not make arbitrary conversion without engine-version/unit test.**
- Infiltration Green–Ampt with redistribution; dynamic vegetation LAI values static per landuse case, not pixel-time-series canopy physiology.

## Sediment and geomorphology
**This article does NOT test soil erosion, 2D sediment source terms, local deposition or soil level feedback**. GSSHA native sediment capability is described in Downer et al. 2010 technical note and separate peer reviewed 2014 article. It is scientifically wrong to claim GSSHA 2023 paper demonstrates native simultaneous LAI+sediment and 5cm cell.

## 고운사 후보판정
PASS for GSSHA native forest LAI-informed interception and 2D diffusive runoff (on real 5m forest catchment). Does not establish leafdrip KE, rain+flow sediment runtime simultaneously active, native5/10cm or public matching source. **보조자료/조건부 후보.** No original source build or native tests in this session.
