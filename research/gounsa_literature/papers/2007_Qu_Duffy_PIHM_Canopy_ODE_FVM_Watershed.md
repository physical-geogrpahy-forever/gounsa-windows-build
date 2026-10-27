# 서지정보
Qu, Y., & Duffy, C. J. (2007). A semidiscrete finite volume formulation for multiprocess watershed simulation. *Water Resources Research, 43*, W08419. https://doi.org/10.1029/2006WR005752.

# 이 논문 검색 이유
무료 공식 공개 수관차단 + unstructured 2D physics-based watersheds PIHM의 *actually compiled original*에 유사박리·퇴적까지 포함됐는지, 다른 프레임워크의 sediment claims와 중첩 오류 여부 검증.

# 연구 유형
원본 수문 다과정 유한체적법/동역학적 수문모델 논문. Wiley 원논문 HTML 전문 §3.2.1 interception 직접 읽음. Penn State Shale Hills research watershed validation. Native contemporary compiled code via MM-PIHM Github source inspected.

# 공간 구조
Triangulated irregular surface/subsurface prism mesh, finite-volume hydrological flux ODE. 2D distributed lateral surface water along connected mesh edges, as opposed to one 1D hillslope profile, but **not shown as full Saint-Venant two-component inertia** in original published formulation. No genuine cm-grid sediment advection benchmark.

# 적용 환경
Shale Hills experimental upland watershed, Pennsylvania, hillslope soil hydrology and microtopographic runoff pathway; highly relevant steep forested critical zone with hydrological canopy. However original study focused on **runoff and subsurface**.

# 핵심 과정
Original §3.2.1 dynamic water-balance state for vegetation interception `h_v` with precipitation, evapotranspiration and throughfall/stemflow. Surface and subsurface hydrology, evapotranspiration, snow, groundwater. **Does not present native raindrop/rill sediment mass balances / flow vs splash detach / deposition module** in 2007 original paper.

# 식생 입력 및 실제 현대 original code evidence
Public **[PSUmodeling/MM-PIHM](https://github.com/PSUmodeling/MM-PIHM)** MIT-licensed currently rebuildable source, README lists `pihm`, `flux-pihm`, `flux-pihm-bgc` compiled versions (PIHM, land-surface, BGC) and SUNDIALS CVODE build.
`src/is_sm_et.c` blob `3a178dd207c69abe520fd7aa766c0c32ff7b11f7`: lines 56–63 reads time-varying projected LAI if supplied or monthly LAI by land cover, L85–86 `intcp_max=lc.cmcfactr*lai*lc.shdfac`, actual canopy evaporation `wf.ec` and water storage `ws.cmc` bounded by max. `src/read_lai.c` blob `4e2d2d496e0ae00e1e78645f06b01f89bf6d833a` reads forcing temporal `LAI_TS`.
**This modern repository is not automatically identical to the 2007 executable**, but the canopy process and LAI in the current actively published source lineage are proven.

# 핵심식/파라미터 단위
`intcp_max = cmcfactr × LAI × shdfac`; [water storage in model's internal water depth unit], canopy shape `cmcfactr` depth per unit LAI, LAI dimensionless, shading fraction dimensionless. Original §3.2.1 `dh_v/dt = p_v - e_v - throughfall/stemflow`. No verified numerical cm resolution.

# Original current code publication and erosion absence
`src/transpt/` directory consists of `init_solute.c`, `read_tracer.c`, `solute_conc.c`, `solute_transpt.c` = solute, **not suspended sediment erosion**. Github README lists only 3 builds and does **not include sediment solver**. Historical CZO website lists research-development `PIHMSed` for geomorphic tree throw, weathering and regolith transport (https://czo-archive.criticalzone.org/shale-hills/models/model_details/pihm-sediment-transport/), but no **matching open executable and event rain/rill H-R component** established; separate environmental model lineage cannot be merged by name alone.
Connected GitHub repo search `PIHM sediment` and `PIHM-sed` returned no matching public full erosion code; absence not absolute proof.

# 고운사에 직접 사용할 수 있는 부분
Confirmed LAI→maximum interception storage and mesh edge hydrological coupling for a forest critical-zone environment, unlike canopy placeholder. Not native storm erosion model.

# 새로운 coupling
Integrating Hairsine-Rose sediment with current PIHM, or importing PIHMSed tree-throw transport, would be NEW coupling unless original published matching integrated code can be identified. Not allowed as preexisting.

# 최종 판정
**수관차단 원본 참고용 PASS; 현재 same-source raindrop+runoff erosion, 5cm true SWE and local sediment transport FAIL**. Do not adopt as Gounsa event engine. Also no native compiled/field test performed this session.

# references
https://doi.org/10.1029/2006WR005752
https://github.com/PSUmodeling/MM-PIHM
https://github.com/PSUmodeling/MM-PIHM/blob/main/src/is_sm_et.c
https://czo-archive.criticalzone.org/shale-hills/models/model_details/pihm-sediment-transport/
