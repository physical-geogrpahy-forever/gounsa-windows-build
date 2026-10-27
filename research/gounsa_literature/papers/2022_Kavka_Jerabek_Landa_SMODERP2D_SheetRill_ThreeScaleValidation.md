# 서지정보
Kavka, P., Jeřábek, J., & Landa, M. (2022). SMODERP2D—Sheet and rill runoff routine validation at three scale levels. *Water*, 14(3), 327. https://doi.org/10.3390/w14030327

# 이 논문을 찾은 이유
강우사상별 공개 모델이 작은 실험구와 실제 농경지 세류에서 검증됐으므로 actual computational mesh, hydraulic routing direction and actual sediment amount scope를 구분하려는 목적.

# 연구 유형
관측 기반 3축척 수문/세류발생 임계수심 검증과 매개변수보정. 학술 원문 HTML abstract + Methods 2.2–2.3 + Results + Conclusion 검색 직접 확인. MDPI 본문 직접 web.open 429 제한이 있지만 publisher indexed full text/DOI 사용.

# 공간 구조
2m×8m (16m²) 인공 강우사면 수문, 50m² 자연강우 Wischmeier runoff plot, 36.6ha field grid rill identification. Last Býkovice field grid **5m×5m numerical cells**; raw UAV/Digital Terrain Model can be finer, 5cm computing not published.
Sheet flow empirical kinematic wave, rill flow Manning with critical sheet water depth; spatial routing algorithm can displace rills vs measured positions. 2D raster and routing != full 2D SWE.

# 적용 환경
Býkovice Czech agricultural field Cambisol, slope9% (Wischmeier 22.1m plot), crops wheat/clover vs bare. Runoff calibrations via 2013/2014 8 rainfall simulator trials under 60mm/h for 30min after runoff onset, and 2010/2011 6 natural rain events. Forest steep oak/Miscanthus excluded.

# 핵심 과정
- Rain volume balance, infiltration, surface retention, effective precipitation and runoff.
- Sheet flow/rill cross-section width, onset critical water depth related shear; simulate rill occurrence/flow.
- Model rill width and rill flags compared 36.6ha plot remote sensing.
- **Observational rill location agreement is not observed/modelled sediment concentration, total detachment mass, deposition thickness or geomorphic feedback.**

# 식생 입력
Agricultural land vegetation vs bare calibrated roughness/infiltration. Current 2026 source allows `ppl` leaf area fraction and `pi` static potential rain interception, but no verified LAI→Smax dynamic drainage or drop height KE in 2022 published benchmark.

# 핵심 식
Water balance and flow q_sh=X I^Y h^b; q_rl=Manning(A,R,I). Rill width `b_rill=h_rill/0.7` in growth phase; hydraulic flow source, no published native soil detachment conservation Eq in this 2022 model tested outputs.

# 파라미터와 단위
Rain 60mm/h, time 30min after runoff begins, experimental 2×8m; 22.13×2.27m plot slope9%. Field 36.6ha, 5×5m computational raster; visual rill cover measured about 5% of field area, best vegetated scenario similar cover. Some mismatches and bare plot overprediction.

# 원 논문의 구현 범위
Paper tests runoff curve, rill width/occurrence, no direct erosion mass validation even though risk framing. Rill spatial displacement from flow routing led to false predicted presence/absence. 5cm untested, forest interception untested, soil loss flux/source code none.

# 고운사에 직접 사용할 수 있는 부분
Qualitatively useful 'rill initiation / width and runoff timing' control measure reference, not high-resolution deposited sediment model, cannot substitute visual rill width for sediment quantity.

# 필요한 새로운 coupling
Multiclass sediment detachment/transport/soil stock, full LAI canopy state, free 4-boundary hydrodynamics; must be called new code modifications.

# 한계
The paper reports grid5m for big field; small runoff plots do not imply field trials 5cm spatial gridding; detailed hydraulic rheology not full 2D SWE. Not source verified identical SHA for published code.

# 최종 판정
**Published run-off/rill-formation verification PASS, native highres 2D erosion/deposition NO-GO.**

# 원문 및 코드
https://doi.org/10.3390/w14030327
https://www.mdpi.com/2073-4441/14/3/327
https://github.com/storm-fsv-cvut/smoderp2d
