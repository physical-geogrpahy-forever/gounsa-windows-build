# 서지정보
Jia, Y., Wells, R. R., Momm, H. G., Zhang, Y., & Bennett, S. J. (2023). Physically based numerical model for the landscape evolution of soil-mantled watersheds driven by rainfall and overland flow. *Journal of Hydrology, 620*, 129419. https://doi.org/10.1016/j.jhydrol.2023.129419

# 이 논문을 찾은 이유
기존 OpenLISEM 이외의 모델 계열 가운데 **2차원 유동과 빗방울 박리, 유사 이송, 지형갱신을 하나의 수치모델로 실제 구현하고 드론 관측지형으로 검증한** 선례 확보. 입력 DEM 원해상도와 실제 계산격자, 저자 연구판과 공개 소스의 일치를 구분.

# 연구 유형
Journal of Hydrology 2023 peer-reviewed numerical hydrodynamics/morphodynamics model development and experimental + agricultural field validation. Elsevier official HTML full abstract, article section snippets, author affiliation listing; USDA ARS official bibliographic validation reviewed. **Full paper body PDF not accessed**; grid sizes and all parameter numerical values not confirmed.

# 공간 구조
- **CCHE2D real 2D** flow: depth-integrated Reynolds equations, flow depth h, xy velocities u,v, water surface η and bed ζ; ∂h/∂t+∇·(uh)=R. Dynamic water and sediment spatial fields, not D8 downstream-only.
- Experimental eroding landscape and tilled corn agricultural watershed including furrows, gullies. UAS Structure-from-Motion photogrammetry acquired repeated detailed DEMs.
- Paper uses term 'high resolution mesh', but **numerical mesh Δx/Δy [cm] in printed accessible abstract/snippets was not specified**. Never translate UAS point spacing into actual simulation grid, and do not assert 5/10cm published precedent.

# 적용 환경
Agricultural tilled field / lab experimental soil-mantled landscape, channel network and drainage furrows; not oak coppice/Miscanthus forest canopy, bare/row vegetation possible but canopy interception field comparison not shown.

# 핵심 과정
- 2D thin sheet runoff and concentrated flow over nonplanar terrain, wetting from rain.
- Physically based rainfall splash soil detachment, soil entrainment/sediment transport due to thin sheet and concentrated rill/gully, and bed-elevation updates (landscape morphodynamics).
- Modified depth-dependent Manning roughness n reflecting gullies and rills developing with water depth.
- Experimental landscape: rain 30 mm/h increased to 105mm/h after 360 min with downstream base-level lowering; representative silt 0.05mm; reported quasi-stabilized observed erosion after 600min; this is **special experimental case**, not 6h forest canopy validation.

# 식생 입력
No verified dynamically updated LAI or leaf drip canopy reservoir, interception, stemflow or branch-drop kinetic energy in 2023 modified CCHE2D research. Agricultural roughness/vegetation effects and model capabilities cannot be equated to Rutter canopy water balance.

# 핵심 식
Published indexed article hydrodynamic eq ∂h/∂t+∇·(u h)=R, h=η−ζ, u=(u,v). Additional 2D horizontal momentum and sediment conservation equations discussed in paper; their complete printed exact equations unavailable, **do not invent numerical coefficients**. Rain splash source distinct from flow entrainment according to verified highlights/abstract.

# 파라미터와 단위
Laboratory rain step 30→105mm/h at 360min; one silt fraction diameter0.05mm, sediment rate stabilizes after600min, directly text-indexed paper snippets. All mesh dimensions/time step and canopy LAI: unverified.

# 원 논문의 구현 범위
Same published **2D hydrodynamics + raindrop and flow erosion + sediment transport + actual topographic/landform evolution** and photogrammetric comparison. This is stronger spatial morphodynamics precedent than paper claims only outlet sediment. Does not prove same executable 5cm forest canopy.

# 고운사에 직접 사용할 수 있는 부분
- Scientific precedent of all-direction xy 2D rain-driven morphodynamic erosion and DEM comparison from UAV, useful validation architecture.
- Reference for evaluating local erosion/deposition maps and evolving roughness, without claiming original code access.

# 새로운 coupling이 필요한 부분
- LAI storage C(t), throughfall/branch drip spatial KE, stemflow if desired, forest roughness, site canopy experimental validation.
- High-resolution 5–10cm native numerical convergence and 4-edge open boundaries explicit benchmarks (not established).
- Replicating 2023 specific modified CCHE2D academic source needs licensed research executable + runfiles, otherwise would be custom new model.

# 한계
- **NCCHE university official website** https://www.ncche.olemiss.edu/downloads/ offers **legacy unsupported 32-bit CCHE2D GUI**, trial/limited 64-bit modules. It explicitly states full-featured CCHE2D is commercially licensed, and use under collaborative research may be possible. **It does NOT provide complete editable 2023 modified soil splash source code and parameter runfiles for download**. This conclusion about verifiable public matching source, not that code must be nonexistent.
- Separate free GUI/mesh binaries not identical to article added splash routines without version provenance.
- No verified 5cm computation, canopy storage or forest comparison.
- No native code execution or numerical QA performed.

# 최종 판정
**Published genuine 2D rain/flow morphodynamic validation YES; Gounsa same-source fully open 5–10cm LAI interception/leafdrop NO-GO**. Retain as strong new independent geomorphic research and validation paper, not current main engine.

# 참고 링크 / DOI
https://doi.org/10.1016/j.jhydrol.2023.129419
https://www.sciencedirect.com/science/article/pii/S002216942300361X
https://www.ars.usda.gov/research/publications/publication/?seqNo115=396221
https://www.ncche.olemiss.edu/downloads/
https://www.ncche.olemiss.edu/cche2d-sed-model/
