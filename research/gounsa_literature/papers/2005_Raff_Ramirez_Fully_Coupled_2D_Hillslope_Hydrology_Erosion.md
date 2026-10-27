# 서지정보
Raff, D. A., & Ramírez, J. A. (2005). A physical, mechanistic and fully coupled hillslope hydrology model. *International Journal for Numerical Methods in Fluids, 49*(11), 1193–1212. https://doi.org/10.1002/fld.1016. Publisher first online September 1, 2005, volume issue December 20, 2005.

# 논문 검색 이유
OpenLISEM은 별도 Work 담당. **기성 단일 원본에서 full 2D shallow flow + physically interactive infiltration + sediment detachment and transport**가 5~10cm 소규모 사면에서 확인 가능한지 다른 모델 탐색. 기존 2026-10-27 INDEX 489편 중 DOI/저자 제목 중복 없음.

# 연구 유형
2005년 동료심사 numerical-method paper. Wiley official abstract and bibliography actually read. Abstract says two simulated demonstrations and validations; **full paper paywall/complete numerical experiment parameters not obtained**. Unverified information must be noted.

# 공간 구조
Full **bidirectional 2D hydrodynamic shallow-water equations** overland, 1D vertical Richards infiltration and sediment detachment/transport coupled. True SWE momentum x,y, not LDD; exactly which explicit discretization and slope wet/dry method need full-text.

# 적용환경
Small artificial hillslope, very small spatial scale runoff and evolving organization. 2004 related experimental paper Raff, Ramírez & Smith describes bare slope without vegetation, but this is **separate article**, so vegetated inputs of 2005 should not be inferred nor prohibited from unrelated experimental paper.

# 핵심과정
Rainfall forcing, 2D overland hydraulics, Richards infiltration, sediment detachment, sediment transport and spatial erosion pattern. Authors describe capable of small-scale changes and drainage network self-organization.

# 식생 입력
**LAI, canopy maximum storage, stemflow, throughfall, leaf-drip splash KE, root cohesion not shown by original 2005 abstract**. Publisher abstract contains no quantitative vegetation-state or canopy interception component. Absence in abstract is NOT proof that full manuscript has none, but **cannot pass user requirement** without equation and native source evidence.

# 핵심식
SWE 2D mass + momentum; Richards 1D vertical infiltration; native sediment mass and detachment/transport closure unspecified at equation-level in accessible abstract. Do not invent author's numerical closure, exact splash/flow separation or runfile.

# 파라미터와 단위
Δx [m], Δt [s], test dimensions [m], rainfall intensity [mm/h], erosion [kg/m²/s] **exact published values not verified**. Words 'very small scales' cannot establish computed 5cm or 10cm. Article PDF inaccessible via free publisher path.

# original source verification
Connected GitHub global repos searched exact Raff+Ramírez, Raff+Richards+erosion, exact title and author. **No matching complete solver repository found**. Publisher paper provides no code-repository SHA or direct executable in accessible page. No source compiled or numerical benchmark executed.

# 고운사 직접 사용 가능
Useful rigorous published physics precedent for 2D full flow/vertical infiltration/sediment in one model, not original-available forest canopy single engine.

# 새로운 coupling
Manual LAI canopy module or new solver write-up would be new code and is not the user's requested previously used intact executable.

# 한계
Cannot establish published 5–10cm original runtime, LAI canopy active, independent soil erosion/doD validation or downloadable source. Search absence not absolute proof private source absent.

# 최종 판정
**보조근거, 운영모델 선정 보류/탈락** under user's hard public source, native 5–10cm canopy + free 2D + sediment conditions.

# links
https://doi.org/10.1002/fld.1016
https://onlinelibrary.wiley.com/doi/10.1002/fld.1016
https://www.researchgate.net/publication/252675059_The_Evolution_of_Landscapes_and_Hillslopes
