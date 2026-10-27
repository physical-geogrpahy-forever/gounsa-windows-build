# 2026-10-27 19:40 고운사 강우사상 5–10cm 수관차단+2D 유수침식 인계

## GitHub 우선 확인한 선행기록
`SYSTEM.md` → `MASTER.md` → `INDEX.md` → `decisions/2026-10-27_GITHUB_FIRST_SUB10CM_NATIVE_MODEL_FOLLOWUP.md` 및 10cm/LISEM branch/SHETRAN documents. 직전 상태: 논문 468, 모델 94, 결정 85. 기존 반복탈락 TREX/SMODERP2D/EUROSEM/LISEM Classic/SWEHR/ASTERIX/tRIBS-FEaST/SERGHEI-SE 등은 별도 새 모델로 추천하지 않음.

## 이번 세션 새 문헌
1. Ámon, Bene, Ray, Gribovszki & Kalicz (2024) *Water* 16:750, DOI 10.3390/w16050750. HEC-RAS genuine 2D SWE + forest canopy interception/litter retention preprocessed effective rainfall, forest steep catchment 2010/2012 storms, native grid 4–20m, **erosion/sediment disabled**. 저장 `papers/2024_Amon_HECRAS_Forest_Canopy_Litter_2D_FlashFlood.md`.
2. Onsamrarn, Chittamart & Tawornpruek (2020) *PLOS ONE* e0241689, DOI 10.1371/journal.pone.0241689, Thailand field tests of WaNuLCAS vs WEPP with agroforestry canopy and root traits; WaNuLCAS spatial zoning/daily storm response not free 2D 5cm. 저장 `papers/2020_Onsamrarn_WaNuLCAS_WEPP_Thailand_Erosion.md`.

## 이번 세션 공개 원본 직접 확인
1. `psu-efd/HydroSed2D` GPL Fortran sources. `src/sediment.f90` SHA `7e6be5983c8f8eee32a5ba919a6347acf425d615`; original actually solves X/Y bedload flux with MPM/Grass and Exner, but **no canopy LAI, rainfall input, infiltration or splash in examined distributed integration**. Dynamic bed is not event soil rain-erosion. 저장 `models/HydroSed2D_Fortran_Original_Source_Audit.md`.
2. WaNuLCAS v3.01 technical manual Chapter3.2.5 canopy water film*LAI, §3.2.7 Rose erosion; distributed **zone** modeling. modern Shiny GitHub `degi/wanulcas` and old v3 release equivalence not known. 저장 `models/WaNuLCAS_Interception_Erosion_Strict_2D_Screen.md`.
3. Other search: `CH-Earth/sedhydro` explicitly model-agnostic external hydrologic coupling, EROSION-3D public R wrappers are not solver source, no native 5cm forest 2D erosion candidates.

## 이번 세션 변경
- [판정 결정](../decisions/2026-10-27_1940_GITHUB_FIRST_2D_CANOPY_SEDIMENT_SOURCE_SCREEN.md)
- HydroSed2D **strict reject**: missing canopy, rainfall splash.
- WaNuLCAS **strict reject**: zonal flow not XY full SWE.
- Ámon2024 **supporting**: forest canopy and hydrodynamic 2D, but no concurrent erosion.
- All requirements passed public executable **none newly found**.
- Native compile/run of new models **not performed**.

## GitHub 신규파일
- `papers/2024_Amon_HECRAS_Forest_Canopy_Litter_2D_FlashFlood.md`
- `papers/2020_Onsamrarn_WaNuLCAS_WEPP_Thailand_Erosion.md`
- `models/HydroSed2D_Fortran_Original_Source_Audit.md`
- `models/WaNuLCAS_Interception_Erosion_Strict_2D_Screen.md`
- `decisions/2026-10-27_1940_GITHUB_FIRST_2D_CANOPY_SEDIMENT_SOURCE_SCREEN.md`
- `sessions/2026-10-27_1940_GITHUB_FIRST_2D_CANOPY_SEDIMENT_HANDOFF.md`

## 다음 시작점
과거 마감된 모델 이름 재추천 금지. 고해상도 논문과 버전 식별의 최소 가능성은 classic LISEM **Cuomo2018 10cm**, **Maggioli2022 5cm**와 v7.5.2 실증 수렴 실패 간의 정확 소스버전 대조, 그리고 **Epple2025 1cm 신형 LISEM 소스 SHA/standalone 0.2.4 바이너리 차이**. 전체 PASS 못 찾았음을 명시하고 신규 코드를 새로 추가하는 일은 결합으로 명확히 표시.

## 미확인
- 수관저류·배수 및 강우박리/유수박리 전체를 포함한 진정한 2D 5cm 같은 소스빌드 QA
- HydroSed2D/WaNuLCAS 5cm native stability/sediment closure 미수행
- HEC-RAS 2024 canopy+erosion 동일실험 무근거

