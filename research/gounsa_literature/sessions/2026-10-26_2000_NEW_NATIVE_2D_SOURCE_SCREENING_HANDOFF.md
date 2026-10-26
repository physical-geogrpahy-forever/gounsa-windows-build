# 2026-10-26 20시 고운사 유수침식 완전 원본 모형 추가 스크리닝 인계

## 요청
사용자 "병신새끼 그럼 더 찾아라". 수관 LAI → native canopy storage, throughfall, leaf-drip rainfall KE, direct rainfall+runoff detachment, fully 2D water+sediment, rills, steep postfire forests, original code public. "의심이 되면 버려" 원칙. 기존 모두 탈락 반복 추천 금지.

## 이번 채팅의 실제 작업 (source screen, no native run)
1. SERGHEI-SE 2025, Braga et al.(2026) Water 18:1870 DOI 10.3390/w18151870 2D SWE+2D suspended sediment+Exner true finite-volume, original GitLab BSD3 and benchmark; **already** in existing archive models/SERGHEI_SE.md, papers/2026_Braga... and 2025 preprint. Native LAI-water canopy/dynamic leaf drip **not positively verified** and GitLab file-by-file audit inaccessible. Strict main engine NO-GO, independent benchmark only.
2. `bastianvandenbout/LISEM` original independent C++/OpenCL **not** `vjetten/openlisem` Classic 7.5.2. Actual SHA 6a5ef17d87bab4227d48673c95c12c61462114dd. Native `model_hydrology.cl` input Smaxc read unused, canopy contents redirected to surface and next canopy state reset 0; native `model_sediment.cl` throughfall = vegcover*rain and directrain = (1-vegcover)*rain. Has 2D flux detachment and corrected sqrt bracket settling unlike broken Classic, but **NOT authentic LAI-driven canopy interception/drip**. Strict NO-GO no build. `models/LISEM_Integrated_VanDenBout_Source_Audit.md`. License metadata ambiguous MIT third-party root LICENSE vs GNU GPL3 licence.txt; do not claim MIT license for whole.
3. `lreis2415/SEIMS` GPL3 native C++; `SPLASHERO_PARK` vegetation fraction splash and `KinWavSed_OL` true flow detachment + upstream network sediment. CASC2D_OF water does not make Kinematic sediment 2D; canopy LAI/leaf drip native coupling absent. NO-GO. `papers/2019_Zhu_Parallelized_SEIMS_Framework.md`, `models/SEIMS.md`.
4. `baharmon/landscape_evolution` `r.sim.terrain` GRASS GPL2 2D stochastic SIMWE water+sediment/DEM morphodynamic, 2019 GMD 12:2837–2854 Fort Bragg LiDAR 450m2 rill/gully case, good independent TLS DEM benchmark; native LAI canopy interception and leafdrip not present in verified manual/options. NO-GO complete engine. `papers/2019_Harmon_RSimTerrain_DynamicHydrology.md`, `models/GRASS_SIMWE_RSimTerrain.md`.
5. Finaud-Guyot et al. (2026) EMS online Oct 8 DOI 10.1016/j.envsoft.2026.107190, SW2D open source 2D polygon finite-volume SWE porosity/rain/infiltration/wind, no native sediment/canopy verified. NO-GO. `papers/2026_FinaudGuyot_SW2D_Porosity_ShallowWater.md`.

## Records and verdicts
- canonical `decisions/2026-10-26_POST_TIMEOUT_NEW_2D_ENGINES_SERGHEI_LISEM_SEIMS.md` strict five-lineage verdict (including appended SIMWE/SW2D)
- `models/SERGHEI_SE.md` updated (not new/duplicate)
- `MASTER.md` updated
- `INDEX.md` regenerated from actual folder contents 442 papers, 93 models, 65 decisions
- NO chosen validated native all-in-one model from these five, NO new compiled/executable test. Do not invent success.
- Sources from GitHub exact funcs and GMD/GRASS manuals linked in files.

## Moving forward
Investigate genuinely new independent published+released code lineage only if demonstrable LAI dynamic canopy water/leafdrip and genuine 2D multi-face sediment (not simply a 2D water module next to kinematic 1D erosion), steep slope precedent; if one passes code gate, stage finite soil stock, dt 1/2 refinements, verified outlet water/sediment and net sediment ledger before recommendation.
Paper-only models, source unavailable, non2D sediment or generic canopy fraction fail instantly. Do not silently relax user criteria. Do not claim historical OpenLISEM problem fixed by unrelated new LISEM kernels. If no such native model verified, transparent bounded negative search result and distinguish separate new coupling research option, never label it original.
