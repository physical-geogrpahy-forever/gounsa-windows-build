# 서지정보
Adiprana, M. H., & Samodra, G. (2026). Comparing erosion processes in vegetated and non-vegetated landslide slopes using the physically based SIMWE model and UAV-LiDAR. *Earth Surface Processes and Landforms, 51*(7), e70329. https://doi.org/10.1002/esp.70329

# 이 논문을 찾은 이유
고운사와 유사한 **식생 및 나지 혼재 산지사면, 드론 LiDAR 지형, 단일 강우사상, 격자별 침식과 퇴적**을 실제 공개 소프트웨어로 모의한 2026 새 연구를 찾아 기존 2019 GRASS SIMWE 후속 산지 실증을 확인하기 위해.

# 연구 유형
2026-06-25 Wiley open access peer-reviewed 2026 original field/DEM-based scenario study. Publisher abstract, data availability, quantitative results, figures caption listed research portal verified. Wiley publisher full Methods PDF and model raster geometry not fully opened; source/full paper-specific inputs provided **on reasonable request to authors**, not instant public archive.

# 공간 구조
- GRASS GIS SIMWE 2D landscape grid Green's function Monte Carlo path sampling with 2D rain excess and 2D transport capacity/erosion deposition. 2D spatial process **but NOT full 2D Saint-Venant finite-volume momentum solver**. The solver can generate spatial maps of water depth and erosion/deposition.
- UAV LiDAR high-resolution DTM at Kalisari landslide, central Java, Indonesia; published article abstract does **not reveal actual model computational Δx/Δy or time substeps**, cannot claim native 5cm.
- Model uses quasi-steady-state erosion/flow assumptions; user event time series physically resolved as hydrograph cannot be inferred.

# 적용 환경
Tropical active landslide vegetated/soil-bare zones in central Java, field measured infiltration and lab soil erodibility. This is genuine **steep vegetated geomorphic slope** unlike many agricultural studies, but no study-specific leaf-drop/LAI canopy water path.

# 핵심 과정
- Simulated **84mm/h 30min** and **38.2mm/h 65min** rainfall scenarios; measured vegetation infiltration 72mm/h and bare30mm/h; 'reversed infiltration' swaps them to isolate infiltration control of source/erosion.
- Runoff water depth, erosion and deposition maps by GRASS SIMWE, field erosion pins and video-derived hydraulic water-depth validation.
- Dynamic leaf canopy rainfall interception, leaf-drip impact energy, throughfall, root biomass explicit stress resistance **not shown**. Their native vegetation effect is variation in infiltrability and Manning roughness.
- Field measured water depths under 84mm/h event vegetated ~1cm and bare ~4cm, sim matched order of magnitude. 38.2mm/h relative contrast consistent.

# 식생 입력
Infiltration vegetated72mm/h vs nonvegetated30mm/h, roughness (Manning map) and topographic/soil texture; **not LAI based canopy storage**. Do not equate high infiltrability with canopy interception.
- Reverse-infiltration scenario means vegetation class labels alone not mechanistic leafdrip/rain shield.

# 핵심 식
- GRASS SIMWE `r.sim.water` computes flow/water depth via stochastic duality of fields and particles; `r.sim.sediment` from depth + dx/dy + Manning + detachment/transport coefficient + critical shear stress produces net erosion/deposition maps.
- Full original article exact formulas/coefficients hidden in Methods not transcribed. Publisher abstract states erosion rate 'kg m^-2 s^-1' for zones, but reported magnitude (0.28) is unexpectedly enormous by typical real geomorphic contexts; **do not use to infer credible 6h soil loss without checking what those units describe and the time integration**.

# 파라미터와 단위
Two event intensities 84 and 38.2 [mm/h], durations 30 and 65min; infiltrability 72 vs30mm/h. Reported author zone-average erosion 0.18 vs0.28 [kg m^-2 s^-1] and reversed 0.52 vs0.09 (as printed in abstract), could reflect rates/solver normalization so **not used as observational validated mass loss**. Actual SIMWE grid cell length NOT reported in accessible abstract; LiDAR resolution distinct.

# 원 논문의 구현 범위
Published "vegetated vs nonvegetated" comparative field-slope SIMWE scenario; field event water-depth order comparison, grid mapped erosion-deposition, **infiltration process sensitivity**. Erosion absolute magnitude subject to steady-state assumptions, authors explicitly warn parameter/uncertainty.
- Hydraulics observations validate water depths not **gridwise cell sediment/DoD conservation**. A map showing net deposition ≠ full Exner feedback.

# 고운사에 직접 사용할 수 있는 부분
Strong 2026 precedent of UAV LiDAR and open-source spatial erosion mapping on forest/vegetated landslide, with an explicit surface-infiltration swap isolation method. Separate test when assessing canopy effect should also control soil infiltration/roughness differences.

# 새로운 coupling이 필요한 부분
To turn into fully native Gounsa canopy-on vs off single published model requires dynamic LAI canopy store, branch drip energy, subhourly water/sediment flux coupling and 5cm mesh stability. Those are **not published native features**.
- Actual Kalisari paper GRASS input maps/scripts/rainfall/erosion pins **author request**, not independently downloadable complete reproduction package.

# 한계
- True hydrodynamic SWE absent, steady state SIMWE design, LAI dynamic canopy absent, exact 5cm grid not established.
- Published vegetation contrasts partly soil hydraulic property contrasts, not canopy.
- No actual GRASS model run in this review.

# 최종 판정
**Valuable new recent steep vegetated 2D erosion map precedent; high-res forest dynamic LAI canopy + freely dynamic 2D storm sediment original engine NO-GO.**

# 참고 링크 / DOI
https://doi.org/10.1002/esp.70329
https://onlinelibrary.wiley.com/doi/10.1002/esp.70329
https://grass.osgeo.org/grass-stable/manuals/r.sim.sediment.html
https://grass.osgeo.org/grass-stable/manuals/r.sim.water.html
