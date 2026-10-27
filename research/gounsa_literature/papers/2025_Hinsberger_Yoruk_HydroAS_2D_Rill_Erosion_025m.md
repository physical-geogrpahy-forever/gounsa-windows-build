# 서지정보
Hinsberger, R., & Yörük, A. (2025). Application of a 2D Hydrodynamic Numerical Model for Heavy Precipitation-Induced Soil Erosion. *Environmental Processes, 12*, article 54. https://doi.org/10.1007/s40710-025-00797-9

# 이 논문을 검색한 이유
다른 연구자가 실제 사용한 **2D SWE + sediment erosion/deposition + within-event DEM feedback** 단일 모델과 명시적 해상도/수치오차 근거, 그리고 original executable/source 확보 가능성 검증.

# 연구 유형
독일 Hydrotec의 HydroAS GS에 Govers (1990) overland sediment transport capacity 구현 및 시범 검증을 수행한 동료심사 모형 연구. 출판일 2025-10-14, 동료심사 원문 HTML을 직접 읽고 수식 및 메타데이터 확인.

# 공간구조 및 계산해상도
**full 2D shallow-water equations** finite volume, 2D velocities u/v, erodible-bed sediment transport with Exner topographic elevation feedback each time step. Input DEM은 cm급 관측자료도 있었으나 논문 모델은 그것을 재격자화한 **0.25×0.25m 와 1×1m 계산격자만 사용** (원문 §2.4). 연구원본 초고해상도 DEM을 computational 5~10cm로 기록하면 안 됨.

# 적용 환경과 연구 방법
Cropland heavy-precipitation rill field observations from prior Hinsberger (2024) field dataset plus published laboratory erosion conditions. Fields #4, #7, #8 surface roughness Manning n and median grain d50 sensitivity, plus extra factor k*TC_Govers to calibrate erosion. DEM0.25 tends to reduce overestimated small-rill erosion relative to DEM1; small rills particularly resolution sensitive and d50/roughness sensitive. Some larger rills require calibration factor 10, 1.2, 3 for selected fields.

# 핵심 과정
- HydroAS depth-averaged 2D momentum and continuity solved by FVM, overland runoff rain on grid;
- Govers (1990) transport capacity adapted into HydroAS GS erosion and bed sediment delivery;
- sediment exchange and Exner equation for grid topographic change;
- study focuses on **flow erosion and rill development**, not separate canopy leafdrip splash mechanism.

# 식생 입력
**No native LAI canopy interception/throughfall reservoir demonstrated.** Study openly says `effective precipitation` input, no infiltration in actual simulations, and **splash erosion neglected** (Springer §2.4 L162-174). No canopy-on/off or Miscanthus/oak tests.

# 핵심 식 및 단위
2D SWE water state vector w=[H,uh,vh], fluxes in X/Y, source terms friction and bed slope. Exner `(1-np)*rho_s*dZ/dt + S=0`, Govers TC function of d50 and hydraulic conditions. 0.25m/1m mesh, no finer numeric precedent. Govers calibrated erosion multiplier is not universal gounsa sandstone physical parameter.

# 원본 프로그램과 코드 공개 감사
HydroAS GS HydroTec commercial proprietary executable/add-on. Developer https://www.hydrotec.de/software/hydroas-en/ explicitly mentions licensing, paid subscriptions, user authorization, extra sediment modules. https://www.hydrotec.de/software/hydroas/hydroas-downloadbereich/ official executable releases require registered user rights; **not the public editable solver original source**. `https://ecohydraulics.org/software-guide/` categorizes HYDRO_AS-2D/FS proprietary. GitHub repository keyword `HydroAS erosion`, `HydroAS source` no matching original solver. Thus strict open-source user condition fails independently of canopy and grid.

# 고운사에 직접 사용할 수 있는 부분
2D hydrodynamic morphodynamic erosion in overland flash storms is operationally demonstrated (in **25cm minimum computational mesh**) and spatial resolution substantially affects local rill erosion. Important methodological comparator, not ready-made 5cm forest interception engine.

# 새로운 coupling
Native canopy storage, leaf drip, splash dynamics not verified; manual addition or third-party model coupling would be new model. Cannot advertise it as existing forest erosion process.

# 한계 및 최종 판정
**보조근거, 주모델 탈락**: 25cm finest mesh; no canopy or splash; proprietary licensed source; calibrated site-dependent Govers sediment parameters; infiltration excluded in experiments. Even though hydrodynamics and Exner are present this cannot satisfy all required processes.

# 참고 링크
https://doi.org/10.1007/s40710-025-00797-9
https://link.springer.com/article/10.1007/s40710-025-00797-9
https://www.hydrotec.de/software/hydroas-en/
https://www.hydrotec.de/software/hydroas/hydroas-downloadbereich/
