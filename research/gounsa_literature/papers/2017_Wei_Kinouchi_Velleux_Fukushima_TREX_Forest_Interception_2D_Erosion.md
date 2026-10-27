# 서지정보
Wei, L., Kinouchi, T., Velleux, M. L., Omata, T., Takahashi, K., & Araya, M. (2017). Soil erosion and transport simulation and critical erosion area identification in a headwater catchment contaminated by the Fukushima nuclear accident. *Journal of Hydro-environment Research*, 17, 18–29. https://doi.org/10.1016/j.jher.2017.09.003

# 이 논문을 검색한 이유
이미 등록된 Wei & Kinouchi(2014)의 산림 LAI 연동 interception 개량 모델이 **같은 실행 연구계열 내에서 rain splash+flow detachment+2D sediment/deposition도 실제 사용되었는지** 확인하여 개념적 선행연구와 소스 재현 가능성을 정확히 구분하기 위해.

# 연구 유형
동료심사된 환경수문/유수침식 분포형 프로세스 모델 연구. 일본 후쿠시마 오염 지역 Kuchibuto River 유역 2011–2014년 약 4년간 지표유출·토사유출 관측과 모의 비교. 관측 기반 수위-유량 관계곡선, 탁도-SS 환산식, 현장 입경 분포와 각 사상 부유사량 비교. 원문의 방법론/그림/표가 PDF 텍스트 인덱스로 열람됨. web screenshot의 원격 호스트 403으로 시각 이미지는 열람실패, PDF 텍스트 결과 및 출판사 HTML 미리보기로 검증 범위 제한.

# 공간구조
- 실제 **90m DEM** 및 토지이용/토양 90m 재격자화; 1km 레이더 강우를 격자 입력으로 적용. 대상 유역 **137km²**, 평균 경사 약9°, 고도200~1000m.
- Overland **true XY distributed 2D diffusive-wave**, momentum terms omitted, not 2D full dynamic SWE. Channels 1D diffusion wave, connected through head difference.
- Governing sediment continuity in both x and y: ∂(AC_s)/∂t +∂(C_s q_x)/∂x + ∂(C_s q_y)/∂y = e_s + e_h. q_x,q_y [m²/s] unit discharges, e_s and e_h [kg/(s m)].
- 5cm/10cm actual modelling precedent: **NO**.

# 적용환경
일본 Fukushima 산림+논/경작지 혼합 산지, 식생있는 headwater. 고운사 불탄 참나무 맹아/억새 사면과 다른 식생, 토양, 유역 규모.

# 핵심과정
1. 원저자 Wei & Kinouchi(2014)가 TREX/CASC2D 계열을 연속 산림 수문용으로 개량했다고 명시. 수문: interception, evapotranspiration, infiltration (Green-Ampt in sibling 2017 paper), subsurface/groundwater + 2D overland +1D channel routing.
2. Upland splash `e_s`는 Woolhiser et al.(1990)의 rain intensity squared, `k_v` 식생피복 비율, 지표 수심의 감쇠를 고려. 이것은 **leaf-drip 높이별 운동에너지나 LAI와 직접 연결된 식이 아님**.
3. Flow net erosion `e_h` based on excess sediment transport capacity, `α` soil cohesion/erosion vs deposition, settling velocity v_s; Engelund-Hansen TC adjusted by calibration β.
4. sediment particle classes sand,silt,clay; spatial grid net erosion/deposition map, river boundary bed transport and settling.

# 식생입력
- 본문 산림 수문 interception and evapotranspiration yes (引用 2014 Wei & Kinouchi).
- 해당 기존 [2014 산림 연구](2014_Wei_Kinouchi_CASC2D_Forested_Interception.md)에는 LAI→Smax(mm)=0.935+0.498LAI-0.00575LAI² 문헌식 기록. **2017 논문이 정확히 같은 Smax map/LAI field parameterization을 모든 과거 run에서 활성화했다는 정확한 실행파일 또는 raster provenance는 확인 못했음**. 동일 연구자 개선 hydro line이라는 학술 연속성 인정하되 코드 동일성 단정 금지.
- `k_v`은 splash attenuation vegetation cover, LAI/throughfall canopy water storage와 같은 물리량 아님. Leafdrop KE 별도 부재.

# 핵심식
- 논문 §4.1 Eq1 (2D sediment conservation) 위에 표시.
- Eq2 precipitation splash source (rain intensity squared + vegetation cover + water depth attenuation), precise printed exponential typography PDF 텍스트 불완전이므로 변수/과정만 원문 확인, 의도적인 수식추정 금지.
- Eq3 `e_h = α w v_s (C_m - C_s)` with e_h [kg s^-1 m^-1], C_m,C_s [kg m^-3], v_s [m s^-1], w [m], α dimensionless.
- Eq4 modified Engelund-Hansen suspended transport capacity plus threshold stream power Ω0 [m/s] and calibration β.

# 파라미터와 단위
- Computational DEM grid 90m; rainfall input parent 1km; monitoring stage / turbidity at 10min.
- Soil fractions: sand dp100μm settling .8cm/s; silt dp20μm settling .0385cm/s; clay dp2μm settling .0004cm/s (paper Table1).
- Four years sediment export to Abukuma River: clay 5,500ton, silt 52,000ton, sand22,000ton.
- Hydrological flow NSE by year St.D 2011: .93, 2012: .69, 2013:.91, 2014:.80; individual events SSC measurement and concentration comparison (many measured with turbidity rating relation). This confirms watershed-scale SS flux, **not per 5cm cell erosion or sediment time-step convergence**.

# 원 논문의 구현 범위
**동일한 published hydrologic-sediment simulation has canopy/interception concept + forest hydrology + 2D diffusion flow + rainfall splash + flow detachment + local erosion/deposition**. This is materially closer to process gate than archived CASC2D-SED2003 without independent splash.
However, main paper does not separately test **canopy ON vs canopy OFF** or use resolved 5cm spatial input, nor provides exact matching ready-built 2017 executable publicly.

# 고운사에 직접 사용할 수 있는 부분
유효강우량, 식생피복에 의한 빗방울 보호, 유수 박리 및 유사퇴적을 하나의 **published forest hydrologic/sediment model architecture**에서 설명한 직접 학술근거. 2D landscape observation / flow conservation formula compare source.

# 새로운 coupling이 필요한 부분
Published 90m simulation 5cm extension, genuine open-all-boundary, explicit leafdrop KE, young oak/Miscanthus canopy individual-grid LAI and dynamic drip, sub-10cm numerical soil-stock/sediment convergence, exact published forest 2017 TREX source/inputs. Any manual transplant of new LAI code into historic TREX source is **new code fork**, not published 2017 unchanged.

# 한계
- **원본 2017 forest version publicly downloadable executable/source GitHub SHA NOT FOUND**. Historic TREX/CASC2D archived C sources are not same executable. Developer official TREX-Research page lists research but does not give this particular 2017 commit/binary.
- 90m, forest basin x137 km², outputs x/y grid erosion; full 2D SWE not proven, diffusive wave.
- Rain splash includes kv canopy cover but no canopy-induced impact KE. Exact 2014 LAI water storage on actual execution cannot be code-audited.
- Individual cell DoD and mass stability not validated; no native cm test done.

# 최종 판정
**유력한 통합된 발표모델 과정 선례 (학술 PASS), 실행 가능한 5–10cm 동일 공개 원본 NO-GO/보류.** 2014 forest hydrology and 2017 TREX sediment same research lineage, unlike two unconnected papers, but code/runfile exactness unresolved.

# 참고 링크 / DOI
https://doi.org/10.1016/j.jher.2017.09.003
https://www.sciencedirect.com/science/article/abs/pii/S157064431630065X
https://www.engr.colostate.edu/~pierre/ce_old/Projects/Paperspdf/Wei-Velleux%20et-al.-2017B.pdf
https://www.engr.colostate.edu/~pierre/ce_old/Projects/TREX%20Web%20Pages/TREX-Research.html
