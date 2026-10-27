# 2026-10-27 21:00 새로운 완전 2D modified Gash + rill erosion 문헌 발견 및 코드 탐색 인계

## 이번에 확인한 신규 선행연구
Long & He (2009 JICS; 2010 *Journal of System Simulation*): 원문 초록에 **2D SWE + modified Gash canopy interception + Green-Ampt infiltration + empirical erosion/deposition + dynamic rill topography**를 통합한 사례 명시. 기존 Maggioli2022는 실제 5cm인데 kinematic wave인 것과 반대의 장단점. Long–He는 genuine 2D/Gash는 보이나 **5–10cm 계산 및 공개 source 불명**.

1. `papers/2009_Long_He_Rill_Evolution_FVM_Modified_Gash.md`, JICS 6(6) 2349–2356.
2. `papers/2010_Long_He_2D_Gash_Rill_Erosion_Morphodynamics.md`, JSS22(2) 348–352, 후속 2017 원저 저널 참고문헌 재확인.
3. `papers/2009_Long_He_GPU_2D_SWE_Hydraulic_Erosion.md`, IEEE DOI 10.1109/ICIECS.2009.5363863; **GPU implementation paper's abstract doesn't mention Gash**; same code source inferred forbidden.
4. `models/Long_He_2D_Gash_Morphodynamics_Code_Audit.md`: connected GitHub search with exact model/author/Gash tokens returned no complete solver source. Not a proof nonexistence.

## 결정
[2026-10-27_2100_NEW_LONG_HE_2009_2010_2D_GASH_EROSION_SOURCE_VERDICT.md](../decisions/2026-10-27_2100_NEW_LONG_HE_2009_2010_2D_GASH_EROSION_SOURCE_VERDICT.md). Not executable for user requirements due to no publicly matched original software, no published actual 5cm run, LAI input not established, full paper inaccessible from checked paths.

## Other queries
Web queries with 2D/LAI/canopy/sediment and code repeatedly surfaced already rejected TREX, Iber+, ASTERIX, SHETRAN, current LISEM, GSSHA, SMODERP2D, PSEM_2D and tRIBS/FEaST. 2024 Perrini Runoff-On-Grid DREAM+Iber uses LAI bucket and 2D SWE but **two-model coupling**, no integrated sediment. Heng2009 native 0.05m is 1D numerical test not whole 2D canopy/erosion.

## Repository current state
Before new records: papers 470, models96, decisions89. Added 3 paper files + 1 model audit + 1 decision + this session. Need confirm latest INDEX/MASTER reflect new files.

## Next
Prior `SYSTEM.md` first. New Long & He exact **public original executable or full code linked to 2009/2010 journal records**, paper mesh width, LAI-Gash and rain/runoff detachment separately; absent verified source = not a candidate for native tests. Avoid reverting to SHETRAN speculative 5cm or OpenLISEM7.5.2 failed executable.

## No claims
No numerical solver compiled, no test run in this follow-up; code-access block remains. Do not ask user to relax 2D/published/LAI without necessity.
