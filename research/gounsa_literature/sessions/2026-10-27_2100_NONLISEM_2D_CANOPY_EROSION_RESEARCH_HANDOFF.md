# 2026-10-27 OpenLISEM 제외한 다른 연구와 원본 모델 감사 인계

## 사용자 요청
OpenLISEM 문제는 다른 Work가 담당. 본 조사 역할은 **OpenLISEM과 독립적으로** 선행연구 탐색, 수관차단/자유 XY 2D/침식/퇴적/실제 5cm 공개 코드 원본 대조. 신규 소스 디버깅을 Work 몫과 중복하지 않음.

## 출발 확인
`SYSTEM.md` → `MASTER.md` → `INDEX.md` (직전 473 papers/97 models/90 decisions) → 최근 Long–He strict decision과 기존 Iber+, HydroPol2D, r.sim.terrain, Wu2020 record, GSSHA archive 확인. 이미 공개된 논문 중복 새 파일 금지.

## 이번에 확인한 신규 학술연구
1. Abrantes et al. (2021) DOI 10.2478/johh-2021-0003: 실제 **2×2m X1% / Y10% 두 방향 실험사면 유출 및 유사량 검증**, active 2D runoff+Horton-SCS infiltration+interrill/rill+sediment deposition. 세부 수치격자는 PDF octet-stream fetch 실패로 미확인, LAI/interception 없음, exact public solver 못 찾음. `papers/2021_Abrantes_Simoes_2D_Experimental_Two_Direction_Erosion.md`.
2. Hinsberger & Yörük (2025) DOI 10.1007/s40710-025-00797-9: true HydroAS SWE+Exner bed change, field rill, **actual 0.25m min mesh** (cm DEM only originally), no infiltration (effective rain), no rain splash, no canopy. HydroAS proprietary vendor app with authorized download/paid license, not full open source. `papers/2025_Hinsberger_Yoruk_HydroAS_2D_Rill_Erosion_025m.md`, `models/HydroAS_Govers_2D_Sediment_NonOpen_Canopy_Audit.md`.
3. Mueller et al. (2010) DOI 10.5194/gmd-3-275-2010: **WASA-SED real complete Fortran repo**, with LAI/interception in `src/Hillslope/soilwat.f90` blob `536d2392...` and `sedi_yield.f90` blob `43af5642...`. But subbasin/LU/TC/SVC semi-distributed model; hillslope USLE/Onstad-Foster/MUSLE/MUST, not full free 2D SWE or 5cm physics. `papers/2010_Mueller_Guntner_WASA_SED_Dryland_Sediment.md`, `models/WASA_SED_2026_Public_Fortran_Canopy_Erosion_Source_Audit.md`.
4. Downer et al. (2014 online / 2015 print), GSSHA DOI 10.1061/(ASCE)HE.1943-5584.0001104: historical CASC2D-SED severe storm extrapolation overprediction. `papers/2014_Downer_Pradhan_Ogden_Byrd_GSSHA_Sediment_Transport_Limits.md`.
5. Raza et al. (2021) DOI 10.3390/land10040422: 51-model review and cropland spatial heterogeneity + canopy model-gap conclusion, not executable. `papers/2021_Raza_Ahrends_Field_Erosion_51_Model_Review.md`.

## Original code actually inspected
- `TillF/WASA-SED/README.md`, `docs/index.md`, `src/Hillslope/soilwat.f90`, `src/Hillslope/sedi_yield.f90`, `license.txt`. Verified original Fortran source (CC-style license), LAI canopy, TC runoff, USLE-family source not finite-volume 2D. **Strict FAIL**.
- Original HydroAS vendor/download pages confirm licenses and registered download, no full publicly editable source. Strict FAIL.
- GitHub author/DOI terms for Abrantes no matching full source. Not proof no code exists.

## Summary outcome
New true native 5–10cm + quantified LAI interception + independent X/Y shallow-flow + native rainfall/runoff sediment and deposition + public same-run original **not verified**. Scientific references provide distinct physical subcriteria, none full PASS.
[Complete decision](../decisions/2026-10-27_NON_LISEM_2D_CANOPY_EROSION_LITERATURE_FOLLOWUP.md).

## Archive update
New papers 5, new models 2, new decisions 1, this session1. Update INDEX and MASTER, expected Papers 478, Models 99, Decisions 91. Ensure actual count after changes.

## What not to do next
- Do not take back OpenLISEM code branch testing from the user's delegated Work.
- Do not re-explore older rejected SWEHR/SHETRAN5cm/TREX/GSSHA/SPHY as if newfound.
- Do not conflate 2m flume physical size or 0.25m calculation with 5cm native cell.
- Do not recommend user manually couple new modules under "single existing published model".
- Need a **published native <=10cm free hydrodynamic 2D + canopy + rainfall and flow detachment + deposition** matching executable source before positive model selection.


## 2026-10-27 추가: LAI 수관저류의 실제 Fortran 식 확인
공식 소스 `TillF/WASA-SED/src/Hillslope/soilwat.f90` (blob SHA `536d2392c441988f43899fbbf25fcb9c9191a767`) 줄 878–882 주석은 식생 수관의 one-bucket interception과 단위 LAI당 수관저류 계수 `intcf`를 설명하며, 문서상 값 0.25 mm per LAI를 언급한다. 소스 줄 925–931은 SVC별 `lai_act`를 면적가중하고, **줄 945, 976, 996의 실제 실행식**은 `maxintc=lai_act(id_veg_intern(j,tcid_instance2))*intcfc(i_ce)`이다. 곧 **Smax [mm] = LAI [-] × intcfc [mm/LAI]**이며 실제 저장량 `intercept`의 증감과 `intc_evap` 증발이 뒤따른다. 주석상의 0.25mm는 프로그램의 전역 불변 상수가 아니라 매개변수 기본·설명값으로 보고 현장값이라고 단정하면 안 된다.
이는 변수명만 LAI가 존재하는 것과 달리 **원본이 LAI를 수관최대저류용량에 실제로 연산 연결했다는 검증**이다. 다만 침식식 `sedi_yield.f90`은 USLE/Onstad–Foster/MUSLE/MUST이고 공간흐름도 사면 terrain component 간 집계 재분배 방식이므로 사용자 요구의 자유 X/Y 유동 및 국지 박리·퇴적을 만족시키지 않는다. 원본 `soilwat.f90` 자체를 컴파일·시뮬레이션하진 않았으며 수학적 활성 소스 경로만 확인함.
- 원본: https://github.com/TillF/WASA-SED/blob/master/src/Hillslope/soilwat.f90
