# 서지정보
Landa, M., Jeřábek, J., Pešek, O., & Kavka, P. (2019). SMODERP2D soil erosion model entering an open source era with GPU-based parallelization. *The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences*, XLII-4/W14, 143–149. https://doi.org/10.5194/isprs-archives-XLII-4-W14-143-2019

# 이 논문을 찾은 이유
기존에 조사되지 않았던 공개 소스 사면 강우사상 모형이 식생 수관차단, 다방향 2D 자유유동, 세류 박리/토사이송/퇴적을 **동일 바이너리로 모의**하는지 추적.

# 연구 유형
2019 FOSS4G 학술회의 동료심사 논문. SMODERP2D GIS 기반 오픈소스 전환, GRASS/QGIS, GPU/CPU TensorFlow 병렬화 시범. 공식 학술 PDF 텍스트 전체 및 PDF 페이지 2 screenshot을 확인.

# 공간 구조
Raster cell water storage and flux balance (Eqs.1–3). 실제 논문 p2 **inflow direction controlled by D8** 명시. kinematic sheet flow plus rill Manning flow on same 2D array; **2D full momentum shallow-water solver가 아님**. Later GitHub offers multiflow/kinematic or diffusive modes but old 2019 study's D8 and modern current multiple option must distinguish.
Experimental GPU application is about accelerating runoff/rill hydraulic CFL computations, not implementing multigrain sediment flux.

# 적용 환경
Agricultural plots and small catchments, heavy rainfall events, soil conservation structural planning. Not verified steep forest with Miscanthus/oak patch or per-cell 5cm transport.

# 핵심 과정
- Soil moisture infiltration and surface retention, rainfall interception represented via effective precipitation es [L/T].
- Raster water surface balance Storage/Δt=Inflow−Outflow, spatial inflow sum from flow-direction routing.
- Sheet discharge q_sh=X I^Y h^b (empirical calibrated), concentrated rill Manning q_rl=A/n R^(2/3) I^(1/2).
- CFL qΔt/dx < 1 adjusted timestep, TensorFlow GPU proof of concept.
- **2019 peer-reviewed manuscript uses "erosion" in title and description but Methods formal equations show water runoff and rill flows; no confirmed sediment concentration, erosion source or deposition continuity equation in the native code audited 2026.**

# 식생 입력
2019 Methods effective precipitation reduced by vegetation interception; current code `smoderp2d/processes/rainfall.py::current_rain` `ppl` leaf-area proportion and `pi` potential interception; not Rutter/C(t)/LAI dynamic canopy drainage/leafdrip impulse state.
Soil cover status/land use and parameters are set per raster, not mechanistic root biomass or leaf-drop height.

# 핵심 식
Paper Eq1 Storage/Δt = Inflow−Outflow.
Paper Eq2 Inflow_i = es_i+sum_j q_j ; Eq3 Outflow_i=inf_i−q_i−ret_i.
Paper Eq4 CFL=q Δt/Δx <1.
Paper Eq5 sheet q_sh=X I^Y h^b; Eq6 rill q_rl=(A/n) R^(2/3) I^(1/2).
Units: q, es, inf, ret [L/T] for cell-normalized water budget, A[m²], R[m], I[-], Manning n with appropriate units.

# 파라미터와 단위
Exact paper experimental grid size / 5cm actual demonstration not established. Velocity and grid width jointly determine CFL timestep; no sediment sediment stock data.

# 원 논문의 구현 범위
Open-source GIS providers (GRASS/QGIS) and preliminary TensorFlow parallelization for surface water/rill processes. Real 2D DEM grid, flow direction routed. No published canopy+full xy2D sediment mass result verified.

# 실제 공개 코드
Repository https://github.com/storm-fsv-cvut/smoderp2d.
2019 main research implementation and 2026 current main are not byte-identical, source audit uses latter.
- `smoderp2d/core/vegetation.py`: vegetation input attributes `ppl` (leaf area proportion), `pi` potential interception [mm].
- `smoderp2d/processes/rainfall.py` 154+: retained rain `interc=ppl*rainfall` under remaining `pi` capacity and returns net rain.
- `smoderp2d/core/kinematic_diffuse.py`: `Kinematic/Diffuse(Mfda if Globals.mfda else D8)`.
- `smoderp2d/time_step.py` 629 lines imports runoff/rill/infiltration, **not native sediment flux/detach/deposition**. All full code search for sediment, detachment, deposition yielded no active numerical functions (repository readme/messaging only).
No native compile/run by this investigator.

# 고운사에 직접 사용할 수 있는 부분
Documented small-event runoff/critical depth/rill width and D8-vs-multiple flow discrepancy. Could independently benchmark hydraulic runoff and source code clarity, not sediment main model.

# 필요한 새로운 coupling
Grid sediment concentration, rain/drop detachment, flow detachment, sediment deposition, free XY SWE, LAI time-varying canopy capacity/drainage would be *new extension*, not original presented 2019/2022 same source.

# 한계
2019 DOI title 'soil erosion' cannot be used as evidence that native source calculates net erosion/deposition mass. Same for '2D' meaning gridded D8 flow. 5cm mesh field precedent missing.

# 최종 판정
**고운사 native canopy+genuine2D erosion/deposition all-in-one: NO-GO.** Strong official and public source for event runoff and rill onset only, not complete sediment.

# 원본자료
https://doi.org/10.5194/isprs-archives-XLII-4-W14-143-2019
https://isprs-archives.copernicus.org/articles/XLII-4-W14/143/2019/
https://github.com/storm-fsv-cvut/smoderp2d
