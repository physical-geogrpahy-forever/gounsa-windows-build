# 서지정보
Eekhout, J. P. C., Terink, W., & de Vente, J. (2018). Assessing the large-scale impacts of environmental change using a coupled hydrology and soil erosion model. *Earth Surface Dynamics, 6*, 687–703. https://doi.org/10.5194/esurf-6-687-2018

# 이 논문을 검색한 이유
독립 비-LISEM 공개 원본에서 **LAI 동적 수관저류, 직접 수관통과우/수관낙수 KE, 독립 raindrop/flow detachment, 퇴적과 유사송출**을 동시 구현한 학술 동일 실행 연구가 있는지 검증.

# 연구 유형
독립 SPHY hydrological model + modified Morgan–Morgan–Finney MMF erosion module의 실제 발표된 통합 모델 개발, 오픈 소스 버전 제공, 스페인 upper Segura catchment 사후 관측 자료 비교 및 기후/식생/토지관리 변화 시나리오 실험.

# 공간 구조
- **격자기반 분포형 유출 생성**, LDD/flow direction PC-Raster network downstream accumulation, river/reservoir transport capacity and within-cell deposition. **Four-edge unrestricted XY 2D SWE/2D diffusive-wave sediment conservation 아니다**.
- 실제 모델계산 격자 **200m**, 기초 SRTM DEM 원자료 **30m**→200m 집계; 기상 5km 원자료 재격자, 모델 시간간격 **1일**.
- 원논문 §4 명시 200m–1km 권장 해상도, 일별 시간간격은 subhourly intense storm 상세과정 해결 못하는 한계.

# 적용 환경
Spain southeast Upper Segura 25 land use types, arid/semiarid Mediterranean watershed, long-term climate/management scenario. 5–10cm 한국 산지 소사면 단기 강우 실증 아님.

# 핵심 과정
1. SPHY hydrology: NDVI→LAI→maximum canopy storage Smax, canopy actual bucket, effective P_eff, saturation/infiltration excess, evapotranspiration, soil moisture and runoff.
2. MMF erosion: `P_eff cos(slope)` split by canopy cover CC into `LD=P_eff*CC` and `DT=P_eff-LD`. These are leaf-drainage/direct-throughfall **for rainfall impact energy calculation**, not necessarily physically released drip flux resolved per crown location.
3. KE = KE_LD + KE_DT, leafdrop KE uses plant height, direct throughfall KE uses rainfall intensity, raindrop detachment Fi by land use/soil size and cover, runoff detachment Hi separately, within-cell deposition roughness/trapping, routed sediment to network/outlets.
4. Dynamic leaf-area and landuse class-specific plant height/density/diameter, vegetation flow roughness, ground/rock/snow cover.

# 식생 입력
- LAI [-] via NDVI; Smax [mm] from published quadratic `Smax=0.935+0.498LAI−0.00575LAI²`, dynamic `Scanopy`, ETr, canopy cover CC=min(1,LAI) optional. Values site-calibration/landuse specific.
- Leaf drainage and direct throughfall [mm], plant height PH[m], coarse/no ground cover GC[-], root texture etc are physically different inputs.

# 핵심 식
- Eq12 `KE=KE_DT+KE_LD` [J/m²].
- Eq13 `KE_LD=LD(15.8 sqrt(PH)−5.87)` for PH>=0.15m; else 0 [J/m²]. LD [mm], PH[m].
- Eq14 original 2018 paper direct throughfall `KE_DT=DT(8.95+8.44 log10 I)`; I [mm h^-1].
- Eq16 `LD=P_eff CC`, Eq17 `DT=P_eff−LD`, Eq18 `F_i=K_i*(%i/100)*(1-GC)*KE*10^-3` [kg/m²], K_i[g/J]. Runoff detachment Eq19 computed separately.
- **Version caveat:** 2026 current `FutureWater/SPHY/modules/mmf.py` has active KE_DT formula **Brown & Foster** `DT*0.29*(1-0.72 exp(-0.05 I))*100` instead of published Eq14 Marshall-Palmer (2018). These versions are not byte-identical! Published 2018 exact v2.1.1 archived source not directly opened in this session, so attribute above Eq to 2018 paper, code comparison to current 2026 GitHub only.

# 파라미터와 단위
- 200m spatial mesh, daily temporal timestep. original runoff/erosion tested at catchment scale.
- KE_LD/KE_DT J m^-2; soil K_i g/J, runoff R mm/day, plant height m, LAI dimensionless.
- Original 2018 code archive **Version v2.1.1 2018-08-13**, 15.1MB zip md5 `3b3368227b9bac0b1ddd68e7b74b0bb7` official https://zenodo.org/records/1344534 and linked at https://github.com/JorisEekhout/SPHY/tree/v2.1.1 **but GitHub tag request 404 in connected GitHub**. Zenodo archive exists, actual extracted files not inspected. Do not assert 2018 repo/tag accessible through GitHub.
- 2026 current repo https://github.com/FutureWater/SPHY `modules/mmf.py` blob SHA `3a7ef3e227126a4f7bcefbb0cf8da73183b53a39`; `modules/dynamic_veg.py` SHA `7595963323020b09e1e80a2b995b76372860d54a`; `sphy.py` SHA `cdc7d3073abb173eb2aa1714a557b8968beada22`. **Source available (current different version)**.

# 원 논문의 구현 범위
- Original peer-reviewed LAI canopy and direct/leaf KE linked with rain-/runoff-driven soil detachment and deposition, applied operationally to catchment.
- This is a **genuine same integrated scientific code lineage with an original 2018 archived release**, not an idea of adding unpublished SPHY coupling.
- But time/mesh scale purposely regional/daily, not 6h storm 5cm; erosion routing by LDD network instead of freely dispersing XY sediment.

# 고운사에 직접 사용할 수 있는 부분
- Literature-based check of active quantitative canopy geometry, direct vs leafdrop KE, raindrop/flow detachment/deposition variable segregation. Original 2018 Eq13/16/17/18 distinguish canopy rainfall budget from kinetic impact.
- Without modifying user's single-model requirement, could benchmark physically relevant canopy submodule but **not accepted as Gounsa native single XY erosion engine**.

# 새로운 coupling이 필요한 부분
- Replace LDD with 2D SWEs, free 4-boundary sediment transport, subhourly canopy partition and soil water, 5cm numerical CFL/soil mass; these are **new coupling/development**, cannot call original SPHY-MMF result.

# 한계
- No execution / published 5–10cm. 2018 release ZIP download in environment failed, cannot claim archived same SHA compiled and run.
- Current mmf.py uses brown-foster KE instead of original paper Marshall–Palmer, critical source-version mismatch; avoid mixing exact equations.
- Limitation called out explicitly by authors: 200m-1km recommended scales, daily timestep cannot resolve subhourly intense storms. Do not present current SPHY as a full 2D flow or dynamically redistributed canopy-drip point hotspot algorithm.

# 최종 판정
**Strong published and openly archived same-lineage process precedent, strict Gounsa 5–10cm XY 2D event single-engine NO-GO**. Original 2018 source available via Zenodo v2.1.1; current repo direct source inspected (different version) with function-active canopy/drip erosion; no native run here.

# 참고 링크 / DOI
https://doi.org/10.5194/esurf-6-687-2018
https://zenodo.org/records/1344534
https://github.com/FutureWater/SPHY
https://github.com/FutureWater/SPHY/blob/master/modules/mmf.py
https://github.com/FutureWater/SPHY/blob/master/modules/dynamic_veg.py
https://github.com/FutureWater/SPHY/blob/master/modules/sediment_transport.py
