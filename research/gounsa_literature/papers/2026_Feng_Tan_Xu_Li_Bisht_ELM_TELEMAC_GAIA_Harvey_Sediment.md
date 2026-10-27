# 서지정보
Feng, D., Tan, Z., Xu, D., Li, L., & Bisht, G. (2026). An integrated modeling framework for sediment dynamics during urban flooding: Application to Hurricane Harvey in Houston. *Water Resources Research*, 62, e2025WR042040. https://doi.org/10.1029/2025WR042040. Published 11 May 2026.

# 이 논문을 찾은 이유
기존 고운사 인덱스에 없었던 **원본 수정 소스와 실제 자료가 공개된 2026 최신 강우/사면침식 + 자유 2D hydrodynamics + 퇴적/지형변화** 연구를 찾음. 단일모델 요구와 독립적인 결합형 framework를 혼동하지 않고 실제 입력과 computational mesh를 따로 구분.

# 연구 유형
- Peer-reviewed, original model-integration and Hurricane Harvey 2017 event simulation and field/remote-sensed evaluation.
- **원논문 Wiley full HTML §2.2, §3, §4 및 Source Availability 직접 확인**. Separate published Zenodo v2 metadata/MD5/files listing directly verified.
- 수정 소스 **공개된 사실**과 그 소스를 연구자가 직접 **압축해제, 컴파일, 실행한 사실**은 다름. 이 세션에서는 **8.2GB full dataset archive 내부 C/Fortran source 미열람**, 모델 직접 재실행 없음.

# 공간 구조
- 3개 엔진 ELMv3 land hydrology+upland erosion, TELEMAC-2D finite-element 2D dynamic SWE, GAIA sediment class transport+erosion/deposition+Exner morphological bed update. This is a **published coupled framework of models**, NOT pre-existing single source-executable all-process.
- Paper §2.2: a shared JIGSAW Delaunay triangular variable-resolution mesh has 442,277 triangles/221,616 vertices, **finest ~30m**, tributary ~90m and peripheral ~1km. Raw NED DEM30m. The 1km rainfall forcing at hourly resolution is **not simulation mesh width**.
- ELM to TELEMAC / GAIA forcing updated hourly; TELEMAC-GAIA runs internal shorter numerical steps with piecewise constant ELM flux.

# 적용 환경
Houston Buffalo Bayou 1336km² urbanized watershed during August 2017 Hurricane Harvey, channel/reservoir/floodplain erosion and deposition. **No 5–10cm forest Miscanthus/oak coppice experimental plot.**

# 핵심 과정
1. ELM land model hydrology (vegetation/soil infiltration/runoff generation) and separate ELM-Erosion source for rainfall-induced and runoff-induced soil erosion at each cell.
2. TELEMAC-2D solves h,u,v hydrodynamics; GAIA incorporates two source classes from hillslopes and own water-shear-driven bed erosion/settling of three sediment classes and Exner elevation change.
3. **Actual published modification:** GAIA accepts ELM hourly areal sediment flux as an extra explicit right-hand-side source to 2D suspended sediment ADE. Sediment classes from land source: mud (60µm), sand (300µm), own coarse bed sand (500µm). This external source integration is a **new coupling** by Feng et al., not standard vanilla TELEMAC-GAIA feature.
4. Site roughness assumption uniform Manning n; model does NOT feedback evolving soil texture or deposited-sediment changes to terrestrial infiltration. Authors explicitly discuss numerical timestep/cost if spatial resolution <30m.
5. Water-sediment mass closure per 5cm hillslope event and leafdrop splash are NOT validated.

# 식생 입력
ELM land-surface vegetation process, land fractions and dynamical ecohydrologic response influence rainfall interception/hydrology and runoff/erosion. However direct **LAI→canopy C(t)→throughfall and leafdrip kinetic energy→GAIA native soil detachment** exact code path was **not checked** in published modified source: do NOT state canopy kinetic-impact original implemented. Dynamic land vegetation hydrology alone does not prove leafdrop kinetic splash.

# 핵심 식
- TELEMAC SWE water continuity and x/y momentum.
- Published paper §2.2.3 for GAIA: deposition D=w_s C_b, bed erosion depends on stress excess (Krone-Partheniades M, τ_b=0.5ρ C_d (u²+v²)).
- Sediment extra ELM cell source `S_e` enters balance as `S_t = D-E+S_e` with paper authors' sign convention Eq7; bed changes Exner `(1-λ)∂(ρ_s z_b)/∂t=D-E` Eq8. Source from ELM not identical to bed erosion E term.
- Sign conventions, units kg m^-2 s^-1, h[m], w_s[m/s], z_b[m], number size classes3. Full exact equations in Wiley §2.2.3.

# 파라미터와 단위
- Finest computational mesh 30m, total 442277 triangles. Forcing 1-hour land update; rainfall original MRMS1km/hour.
- 2017 extreme event, deposition totals ~8.0 million m³ (reservoirs5.7 and floodplain/channel2.3 million).
- Observed water levels at 16 USGS gauges, median R²0.83 and KGE0.78. These are site calibration skill/outlet/inundation, NOT 5cm sediment mass and canopy intercept validation.
- Authors report 30m setup HPC runtime ELM ~2h/1600 cores; TELEMAC-GAIA ~10h/40cores, discussing sub30m unrealistic scaled cost.

# 원 논문의 구현 범위
Entire urban basin 30m refined sediment redistribution, LiDAR-constrained flood deposition patterns and subgrid hydrologic/erosion sources fed to TELEMAC-GAIA. Explicitly three engines with one-to-one mesh, **not the user's requested single previously-existing native model**. Full sources in archive use modified GAIA, not identical to publicly installed vanilla TELEMAC.

# 공개 소스 직접 확인
- [Zenodo 2026 v2](https://zenodo.org/records/18331808), DOI10.5281/zenodo.18331808, published Jan21, single **`Data_Scripts_Harvey_Sediment_v2.zip` 8.2GB** md5 `efdf94753cd7f29cd8476bf71abb9ff6` verified Zenodo page. Dataset page lists `src/` **modified TELEMAC/GAIA source**, `Scripts/` processing/figure scripts, `Data/` observations and simulations, `shpfiles/` geospatial data.
- **This is actual deposited modified code unlike papers merely pointing to generic platform**; however full 8.2GB ZIP source internal files were **not downloaded, code paths not static audited, not compiled/executed**. Thus source metadata PASS / runnable 5cm same version source proof NOT TESTED. Zenodo v2 dated 2026; 2025 date in original source bibliography is citation/deposit and not actual DOI article date.
- ELM exact version can be developed from E3SM code elsewhere, but Zenodo src/ states modified TELEMAC/GAIA, **not full source for every ELM dependency**. Do not claim ZIP contains complete 3-engine compiled executable stack unless archive inspected.

# 고운사에 직접 사용할 수 있는 부분
Published, openly documented integration for **external rain/flow hillslope erosion source into 2D sediment/advection/Exner** with an actual public revised code archive; computational mesh vs input DEM forced distinction. Numerical control of water/sediment source double-counting is important to avoid when using model couplings.

# 필요한 새로운 coupling
Would be substantial new development to put a **single** model inside 5cm forest plot with hour→seconds, dynamic LAI canopy storage/leafdrop KE, finite active soil layer and all-four-side free boundary. Not an existing one-engine already validated variant; specifically user disallows casually combining models.

# 한계
- Multiple external engines, 30m min, hourly sources, extremely large HPC, full internal source zip uninspected.
- Morphodynamics/infiltration not fully feedback and spatial roughness constant.
- No per-tussock/drop canopy mechanical rainfall energy and 5cm numerical converged fluxes.

# 최종 판정
**Important NEW 2026 integrated model and openly deposited modified source; strict native single 5–10cm Gounsa NO-GO.** Source archive metadata exists; native code read or run not achieved and must not be claimed.

# 참고 링크
https://doi.org/10.1029/2025WR042040
https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025WR042040
https://zenodo.org/records/18331808
https://www.pnnl.gov/publications/integrated-modeling-framework-sediment-dynamics-during-urban-flooding-application
