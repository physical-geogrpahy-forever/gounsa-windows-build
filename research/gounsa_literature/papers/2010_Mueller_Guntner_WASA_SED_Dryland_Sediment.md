# 서지정보
Mueller, E. N., Güntner, A., Francke, T., & Mamede, G. (2010). Modelling sediment export, retention and reservoir sedimentation in drylands with the WASA-SED model. *Geoscientific Model Development, 3*, 275–291. https://doi.org/10.5194/gmd-3-275-2010.

# 이 논문을 검색한 이유
LISEM을 제외하고 **완전한 공개 원본, 식생 LAI 수관차단, 사면 유수와 침식, 퇴적**을 동시에 갖는 모델의 5~10cm 계산 적합성 평가. 기존 473편 INDEX에서 동 DOI 미등재 확인.

# 연구 유형과 적용환경
독일 포츠담 연구진의 semi-distributed hydro-sedimentological WASA-SED v1.0 논문. 스페인 프레피레네 Isábena 445km2 건조지역 유역, 하류 Barasona 저수지 93 hm3의 유역 유사생산 및 저수지 퇴적량 재현과 관리 시나리오.

# 공간구조 및 시간
명시적 **semi-distributed** 계층: sub-basin → landscape unit → terrain component (TC) → soil-vegetation component (SVC), hillslope runoff redistributed to downstream TC; river/reservoir separate modules. 2025 공개 설명서 `hymo_all.f90` hourly or daily timestep, **5~10cm DEM XY 자유유동 계산격자 아님**.

# 핵심 과정
Hydrological interception, ET, infiltration, saturation/Horton overland runoff, groundwater, lateral/downslope redistribution. Hillslope sediment yield is computed with **USLE / Onstad-Foster / MUSLE / MUST selectable** equations, with sediment transported and retained in landscape, river/reservoir including storage/remobilisation. The presence of erosion models here should not be mistaken for cellwise 2D raindrop+runoff detachment with finite-volume sediment advection and spatial morphodynamics.

# 식생 입력
Soil-vegetation components with LAI `lai_act`, `tclai`, and interception state `tcintc` in native Fortran `soilwat.f90` with canopy storage/evaporation. Field LAI source and species parameter calibration cannot be transferred unaltered to Korean Miscanthus/oak.

# 핵심식 및 매개변수
`sedi_yield.f90` `SELECT CASE (erosion_equation)`: 1 USLE, 2 Onstad-Foster, 3 MUSLE, 4 MUST, weighted `K_fac,C_fac,P_fac,CFRG_fac` over SVC, runoff q_out m3, peak m3/s, timestep hours. Hillslope sediment yield depends on TC units. `soilwat.f90` `q_surf_in` and `q_surf_out` m3 per TC, LAI and canopy interception mm. Model's published 445km2 use is not evidence of 0.05m resolution.

# 원 논문의 구현 범위
Published spatially semi-distributed vegetation-influenced water and sediment modeling at large dryland basin scale, retention/remobilisation in river/reservoir. This is a mature research lineage, but different hydraulic structure and sediment equations from user's target.

# 실제 공개 소스와 재현성
Source `https://github.com/TillF/WASA-SED` publicly distributed including `Makefile`, `src/Hillslope/soilwat.f90`, `src/Hillslope/sedi_yield.f90`, `docs/index.md`, sample inputs and Windows releases. `soilwat.f90` blob `536d2392c441988f43899fbbf25fcb9c9191a767`, `sedi_yield.f90` blob `43af5642e1879ad7794f47299dbf5b7234256ad8`. No native simulation compiled this session because critical free XY 2D condition fails before computational tests.

# 고운사에 직접 사용 가능한 부분
WASA-SED native interception/canopy and large-basin suspended/sediment redistribution provides conceptual context only. No native cm-resolution erosion map or free 2D run.

# 새로운 coupling
Free XY 2D hydrodynamics added externally would be a new model/coupling, not original WASA-SED. Do not do that under one-model restriction.

# 최종 판정
**탈락 for Gounsa native single-event ≤0.10m free-2D water erosion despite open and complete Fortran.** Source availability **PASS**, LAI+interception presence **PASS**, freely spreading 2D SWE and native 5cm hillslope erosion **FAIL**.

# 참고
https://gmd.copernicus.org/articles/3/275/2010/
https://github.com/TillF/WASA-SED
https://tillf.github.io/WASA-SED/


## 2026-10-27 추가: LAI 수관저류의 실제 Fortran 식 확인
공식 소스 `TillF/WASA-SED/src/Hillslope/soilwat.f90` (blob SHA `536d2392c441988f43899fbbf25fcb9c9191a767`) 줄 878–882 주석은 식생 수관의 one-bucket interception과 단위 LAI당 수관저류 계수 `intcf`를 설명하며, 문서상 값 0.25 mm per LAI를 언급한다. 소스 줄 925–931은 SVC별 `lai_act`를 면적가중하고, **줄 945, 976, 996의 실제 실행식**은 `maxintc=lai_act(id_veg_intern(j,tcid_instance2))*intcfc(i_ce)`이다. 곧 **Smax [mm] = LAI [-] × intcfc [mm/LAI]**이며 실제 저장량 `intercept`의 증감과 `intc_evap` 증발이 뒤따른다. 주석상의 0.25mm는 프로그램의 전역 불변 상수가 아니라 매개변수 기본·설명값으로 보고 현장값이라고 단정하면 안 된다.
이는 변수명만 LAI가 존재하는 것과 달리 **원본이 LAI를 수관최대저류용량에 실제로 연산 연결했다는 검증**이다. 다만 침식식 `sedi_yield.f90`은 USLE/Onstad–Foster/MUSLE/MUST이고 공간흐름도 사면 terrain component 간 집계 재분배 방식이므로 사용자 요구의 자유 X/Y 유동 및 국지 박리·퇴적을 만족시키지 않는다. 원본 `soilwat.f90` 자체를 컴파일·시뮬레이션하진 않았으며 수학적 활성 소스 경로만 확인함.
- 원본: https://github.com/TillF/WASA-SED/blob/master/src/Hillslope/soilwat.f90
