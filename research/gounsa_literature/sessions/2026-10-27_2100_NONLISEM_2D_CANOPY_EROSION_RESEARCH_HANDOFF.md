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
