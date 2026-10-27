# 서지정보
Jiang, C., Parteli, E. J. R., & Shao, Y. (2025). A Model for Regional-Scale Water Erosion and Sediment Transport and Its Application to the Yellow River Basin. *Journal of Advances in Modeling Earth Systems, 17*(5), e2024MS004593. https://doi.org/10.1029/2024MS004593

# 이 논문을 찾은 이유
OpenLISEM은 다른 Work에 배정돼 조사에서 제외한다. 공개 원본 **LAI 수관저류→직접수관통과우/수관적하→강우박리, 2D 표면 유사수송과 침식·퇴적**을 동시 구현한 타 연구 실물코드 찾기. INDEX DOI 조회 결과 기존 canonical 등록 없음.

# 연구 유형
수문-토사 통합 Fortran 모델과 중국 황허 대유역 장기 검증(1979–1987). 논문 원문 Wiley HTML 전수 주요 Method, Data Availability, 공간 및 시간 분해능을 읽고, linked GitHub 현재 원본 Fortran 소스 내용 대조.

# 공간 구조 / 실제 계산해상도
**20km 계산격자, 60분 시간간격** (paper §3.3.1). 원본 30m DEM 경사를 20km 계산격자에 집계한 것. 30m DEM이 30m native simulation을 뜻하지 않으며 5–10cm와는 전혀 다름. `module_rt_rt2d.F`는 implicit water-level routing과 주변 **8방향 경사 수송** (Shepherd, Gaussian dense, sparse solver)로 계산; user 요구 full two-direction SWE momentum solver (Roe etc.)로 분류 금지. CASC2D-SED-derived sediment source.

# 적용환경
황허 유역 광역 수문과 유사수송, 황토고원, 관개, 영구 세류 / 대규모 협곡 경험지수. 고운사 산불 후 20~50mm/h 억새와 참나무 사면 5cm 실제 실험 없음.

# 핵심 과정
공식 논문: AHMS (Noah-MP land) + modified CASC2D-SED active water/sediment routing, multi-fraction suspended sediment, sediment flux in cardinal and diagonal neighboring pathways, stored deposited/eroded material. Source also includes canopy interception and several erosion equation options within Noah-MP. 그러나 **실제 2025 published 20km run의 canopy-on/off 및 LEAF-DRIP kinetic energy branch 선택/field validation 미확인**.

# 식생 입력과 코드에서 확인된 실제 식
공식 repo `https://github.com/JiangCong1990/AHMS-SED`, 파일 `Offline_AHMS-SED/Land_models/NoahMP/Noah/module_sf_noahmplsm.f`, blob SHA `ad5ea8eba279f98463589f322cc7fd95faaebb1f`:
- `CANWATER` lines ~7061–7072:
  `MAXLIQ=CH2OP(VEGTYP)*(ELAI+ESAI)` [mm];
  `QINTR = MIN(FVEG*RAIN*FP, (MAXLIQ-CANLIQ)/DT*(1-EXP(-RAIN*DT/MAXLIQ)))` [mm/s], clipped nonnegative;
  `QDRIPR=FVEG*RAIN-QINTR`, `QTHROR=(1-FVEG)*RAIN` [mm/s].
- `WATER` returns `QDRIPR,QTHROR`, `CALL EROSION` lines ~1200–1203 passes these to rainfall/flow erosion.
- `EROSION` lines ~9624–9781 `OPT_ERO=4`: `KEDT=max(8.95+8.44*log10(QRAIN*3600),0)` and `KELD=max(15.8*sqrt(HTOP)-5.87,0)` [J m^-2 mm^-1]; `KE=KEDT*QTHROR*DT+KELD*QDRIPR*DT` [J/m²], `DETRAIN=ERODRD*KE*exp(-b*RUNSRF*DT)*1.E-2/DT` [t ha^-1 s^-1 according to in-code comments; conversion =1e-6*1e4]. ***The code's ERODRD g/J and output unit conversion require separate unit scrutiny before numerical adoption.***
- Other `OPT_ERO=1,2` branches compute (modified) USLE; `OPT_ERO=3` HSPF raindrop source; `OPT_ERO=5` another rainfall source. All branches currently set `DETFLOW=0` at initialization in this routine, so local EUROSEM-type line **is only rainfall detachment**, while flow-driven sediment transport capacity is separate `Routing/module_rt_rt2d.F::KRcap`.
- Published source `Offline_AHMS-SED/Run/namelist.hrldas` **line32 `erosion_option=1`**. This repository example chooses USLE, *not* `OPT_ERO=4` leafdrip physics. Actual original 2025 calibrated selected config for Yellow River must be verified from Zenodo published input, cannot simply assume sample is exact 2025 config.

# 유동 및 유사수송 실제 소스 감사
- `Routing/module_rt_rt2d.F` SHA `a51aa6748f6b65ba8a7bea976f8185a22fe610c9`: lines ~965-975 iterative water surface solver, L1099–1104 8 directions, L1821–1948 intercell sediment routing `RoutSedOvrl`, channel `RoutSedChn`, settling/deposition; L5453 `FBARE=exp(-0.52*LAI)` and L5497 LAI-based **USLE crop management C factor**, not physical interception/drip. Pathways physically distinct. True finite-volume SWE X,Y momentum equation implementation not shown.
- `Routing/module_rt_sed2d.F` blob `73126ffbc63c2f5d087ed5073bf2c5bba3ac815b`: file mentions EUROSEM leafdrip KE and LAI but appears **incomplete/noncompilable draft** (undeclared lines, mismatched IF, stranded `t`). More importantly the official `Routing/Makefile` OBJS contains `module_rt_rt2d.o` but **does not contain `module_rt_sed2d.o`** and main runtime `module_rt_rt2d.F` has no call `rt_sed`. Thus **do not assert module_rt_sed2d.F is active**. Active Noah-MP `EROSION` branch 4 is a **different implementation** present in compile tree.
- Input `Offline_AHMS-SED/Run/namelist.hrldas` contains `erosion_option=1`, and the 2025 paper simulates 20km land-to-river basin scales. **Single repo with canopy and sediment mathematical modules ≠ published 5cm canopy-on/off dynamic XY erosion case**.

# 매개변수와 단위
`DX` [m] = 20000, `dt` [s] =3600 as paper experiment. LAI [-], `FVEG` [-], `ELAI` [-], `ESAI` [-], `CH2OP` [mm per unit plant area], QDRIPR/QTHROR [mm/s], KEDT/KELD [J m^-2 mm^-1], sediment volume per class [m³], erosion `DETRAIN` t ha^-1 s^-1 (comments). **NO cm-scale validation**.

# 공개 원본과 입력자료
- GitHub `https://github.com/JiangCong1990/AHMS-SED` original full project source (but 2026 head may differ from exact v1.0).
- Published model v1.0 https://doi.org/10.5281/zenodo.14494932 (CC BY 4.0). Exact paper inputs/results https://doi.org/10.5281/zenodo.14983610. This is stronger provenance than many previous closed models; matching 2024 Zenodo code against current GitHub SHA remains outstanding.
- No source was compiled/run in this audit.

# 원 논문의 구현범위와 사용 가능성
Published fully archived large-area source, 2D raster neighbor sediment, hydrological land model canopy and an `OPT_ERO=4` drop-energy choice in current source. **It is not a validated 5–10cm genuine XY SWE source** and current example disables the most relevant leaf-drip source option. One-run exact canopy→sediment→flow feedback not confirmed from article selected configs.

# 새로운 coupling
Never describe separate archive Noah-MP and routing paths as a new bespoke external pairing: they are **inside original AHMS-SED repo**. However grafting this land module into a 5cm distinct free-SWE solver would be a **new coupling**, not an original published 5cm model.

# 한계 / 최종 판정
**Source code publication PASS**, **canopy and leafdrip native optional code PASS**, **same published event with selected options and tested canopy ON/OFF UNKNOWN**, **5–10cm computation FAIL**, **genuine full 2D SWE momentum FAIL / at least unproven**, **hillslope local sediment validation FAIL**. **Strong source-verifiable alternative science, not suitable standalone Gounsa 5cm native model.**

# DOI and source
https://doi.org/10.1029/2024MS004593
https://github.com/JiangCong1990/AHMS-SED
https://doi.org/10.5281/zenodo.14494932
https://doi.org/10.5281/zenodo.14983610
