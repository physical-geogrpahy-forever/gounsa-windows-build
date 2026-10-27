# Downer et al. (2010) — Improved Soil Erosion and Sediment Transport in GSSHA

## 서지정보
Downer, C. W., Ogden, F. L., Pradhan, N. R., Liu, S., & Byrd, A. R. (2010, August). *Improved Soil Erosion and Sediment Transport in GSSHA*. U.S. Army Corps of Engineers ERDC Technical Note ERDC TN-SWWRP-10-3. **정부 기술보고서**로 동료심사 학술논문으로 둔갑시키지 않는다.
Primary source: https://gsshawiki.com/images/9/92/Sediment_TN.pdf (publisher search-indexed complete technical note, file direct web open 403)
Second source: https://erdc-library.erdc.dren.mil/bitstreams/81b728f8-750b-4ef8-e053-411ac80adeb3/download

## 검색 이유와 연구유형
기존 OpenLISEM의 보존성과 source code 결함 때문에 canopy interception + free XY routing + rainfall/flow detachment + deposition in already released non-LISEM single engine 탐색. Original model technical reformulation and catchment sediment demonstration.

## 공간 구조·환경
GSSHA 2D finite-volume overland diffusive-wave water, 2D sequential explicit sediment advection, 1D channel. Watershed event and extended simulations. **No native 5/10cm plot benchmark** in this document verified.

## 핵심 과정
- ERDC note explicit separate parent soil, suspended sediment, deposited erodible layer particle stock for user-specified sediment size classes.
- Raindrop and overland-flow detachment, transport capacity option; suspended advective exchange between gridcells, deposition if capacity insufficient, reentrainment of deposited sediment; after event can carry sediment/material states forward.
- Source note: "changes in overland flow cell elevation due to erosion or deposition can also be carried forward to the next event" when chosen; **do not reinterpret as same-event each flow step full bed elevation feedback**.
- Watershed calibration event sediment yield. Better sediment limitation than old CASC2D-SED; 2014 Downer et al. Journal of Hydrologic Engineering explicitly evaluates detachment limits in updated native GSSHA https://doi.org/10.1061/(ASCE)HE.1943-5584.0001104.

## 식생 입력 및 관정
Canopy interception implemented by GSSHA hydrology in same engine, though this specific 2010 note does not establish sediment experiment with activated LAI canopy and leafdrip KE. See Garcia et al. 2023 canonical paper for LAI-based canopy storage in GSSHA. Need verify same model version, runtime runfiles, and whether interception is used in sediment rain-momentum source term (distinct from erosion vegetation-cover factor).

## 식, 단위, 정량값
Erosion source rate per unit area and particle sediment mass in cell; report describes processes and flow, not all rates or particle parameters reproduced from inaccessible PDF. Input parameters: sediment class d (m or user standard, confirm), bulk density (kg/m³), rainfall mm/h, finite-volume cell area m². Native 5cm and timestep stability unverified.

## 원본 소스 및 limitations
Original GSSHA v8 free distribution announced 2024-10-07: https://www.erdc.usace.army.mil/Media/News-Stories/Article/3924653/gridded-surface-subsurface-hydrologic-analysis-model-version-80-released/ ; official executable link wiki https://gsshawiki.com/GSSHA_Download but wiki HTTP403 to automated inspector. Original full source v8 GitHub/Zenodo release **NOT verified**. CI-WATER/gsshapy is an input output adapter, not native erosion C++ sources. EarthSim developers explicitly note GSSHA executable freely available but core source closed in their integration vintage: https://earthsim.holoviz.org/user_guide/index.html. Later full source availability uncertain; do not claim never exists.

## 고운사 직접 사용 가능한 부분 / 새로운 coupling / 최종판정
Single existing engine's runoff and sediment mechanics, finite explicit parent/mobilized/deposition pools and optional inter-event DEM changes. Yet **same published study canopy and sediment activation unverified**, leafdrip KE unsupported, 5–10cm actual computational validation absent, original source not publicly confirmed. **보류: GSSHA executable track, not accepted as fully verified original-source canopy-morphodynamics model.**
