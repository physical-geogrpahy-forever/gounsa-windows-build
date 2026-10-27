# 2026-10-27 21:48 요청 독립 연구: CASC2D-SED 원본 소스와 2017 개량 산림 TREX 실증 인계

## 연구 분담과 목표
- 사용자 명시: Classic OpenLISEM 수정은 다른 ChatGPT Work에게 맡김. 본 세션은 **독립적 기성 논문/원본 코드 조사만** 수행. 이 세션은 OpenLISEM 수정, native compile/run, patched code 테스트 수행하지 않음.
- hard requirements: 5–10cm published actual grid, quantitative LAI canopy water intercept/storage/drain + preferably drop KE, real 2D unrestricted four-side outflow, rainfall and flow detachment, sediment transport/deposition and cell soil mass numerical stability, original matching executable/source.

## 기존 인덱스 확인 후 새 원본문헌 5편 (이번 조사로 생성)
1. [Johnson et al.(2000), CASC2D-SED](../papers/2000_Johnson_Julien_Molnar_Watson_CASC2D_SED.md) DOI10.1111/j.1752-1688.2000.tb04246.x: xy two-direction diffusive-wave erosion, size fractions and deposition, catchment hydrology/SSC comparison.
2. [Rojas et al.(2008), grid-scale effects](../papers/2008_Rojas_Velleux_Julien_Johnson_CASC2D_SED_GridScale.md) DOI10.1061/(ASCE)1084-0699(2008)13:9(793): **30–330m computational cells**.
3. [Jiang et al.(2025), AHMS-SED](../papers/2025_Jiang_Parteli_Shao_AHMS_SED_20km_Original_Code.md) DOI10.1029/2024MS004593: 20km Yellow River regional modified CASC2D-SED source, Zenodo10.5281/zenodo.14494932, GitHub JiangCong1990/AHMS-SED.
4. [**Wei et al.(2017), JHER actual forest integrated 2D erosion**](../papers/2017_Wei_Kinouchi_Velleux_Fukushima_TREX_Forest_Interception_2D_Erosion.md) DOI10.1016/j.jher.2017.09.003: 90m grid, same published modified TREX water interception, canopy/hydrology, 2D XY diffusive wave, distinct rainfall splash and flow sediment/deposition Eq1–3, Fukushima forest basin SSC observation, four-year simulation.
5. [Wei et al.(2017), Cs forest TREX](../papers/2017_Wei_Kinouchi_Yoshimura_Velleux_Forested_Cesium_TREX.md) DOI10.1016/j.jenvrad.2017.01.017: sibling 2017 model with forest Cs wash-off and sand/silt/clay sediment. **Cesium canopy interception != hydrological rainfall canopy storage**. No exact native release.
- 기존 [Wei & Kinouchi 2014 forest CASC2D](../papers/2014_Wei_Kinouchi_CASC2D_Forested_Interception.md) 과거 canonical paper 보강: LAI Smax equation is their hydrologic new routine, **not present in archived older C**; 2017 forest TREX paper connects processes in same actual study, 90m not 5cm.

## Real recovered independent C source (new verified file provenance)
- Archive https://github.com/wy7980/CASC2D-SED , [CSU origin site](https://www.engr.colostate.edu/~pierre/ce_old/Projects/CASC2D-SED%20Web%20site%20082506/CASC2D-SED-Home.htm); repo `readme.md` says rint→wrint compiler symbol fix, not byte-identical original.
- [Full source audit](../models/CASC2D_SED_C_Original_Independent_Code_Audit_2026.md):
  - `ReadControlFile.c` landuse retention[i]mm, Manning roughness, USLE C/P.
  - `InitializeVars.c` ret=retention/1000; `intercept.c` 22 lines static initial retention depletion, **no LAI/dynamic canopy drain or drip**.
  - `OvrlRout.c` neighboring signed head gradient + Manning: true interior XY pairwise diffusive, not D8/full SWE.
  - `RoutOutlet.c` one outlet `jout,kout`; four free sides FAIL.
  - `RoutSedOvrl.c` sand/silt/clay flow TC and deposition, source `Fcts_sed.c::KRcap` slope^1.66 and discharge^2.035 USLE C/K/P; independent rainsplash absent in archived source.
- **CASC2D-SED exact code new found but strict all-process model NO-GO**. [Decision](../decisions/2026-10-27_NEW_CASC2D_SED_SOURCE_ARCHIVE_DEEP_2D_CANOPY_GATE.md).

## Vital new positive published integrated method but native gap
- [Wei et al.(2017) rigorous source/claim decision](../decisions/2026-10-27_WEI_2017_FOREST_TREX_CANOPY_SPLASH_2D_INTEGRATED_90M_NO_CODE.md):
  - 2017 revised TREX is explicitly descended from 2014 Wei-Kinouchi forest-interception hydrology and includes rain splash source Eq2 with vegetation cover plus 2D xy diffusive wave and flow erosion/deposition Eq3.
  - 2017 paper model cell **90m** in 137km² catchment, observational outlet SSC/annual NSE. No per cell 5cm test; exact 2017 modified TREX source, setup and GH checksum missing.
  - [WatershedModels/trex_src_csu](https://github.com/WatershedModels/trex_src_csu) archive previously checked fixed retention `Interception-r4.c`, not proven 2017 branch. Do not claim 2017 model code already available simply because classic TREX is mirrored.
  - 2D diffusive wave, not full dynamic Saint Venant; throughfall drop energy module not confirmed.

## Web/PDF verification
- Original 2017 JHER PDF text [CSU](https://www.engr.colostate.edu/~pierre/ce_old/Projects/Paperspdf/Wei-Velleux%20et-al.-2017B.pdf) read p.4 source equations, field methods p.1–3, outputs p.8–9; `web.run screen` twice attempted but CSU legacy host HTTP403 screenshot unavailable; no pixel table claims made beyond indexed original PDF text and ScienceDirect abstract.
- Same author [2017 A J Env Radioactive](https://www.sciencedirect.com/science/article/abs/pii/S0265931X17300619) body HTML and CSU text confirmed.
- `2017 Wei source exact Github` not found by targeted search. Nothing compiled or run this session.

## GitHub artifacts written and status
- papers x5 as above
- model audit + [models/TREX.md](../models/TREX.md) append 2017 continuation
- [decisions CASC 2003](../decisions/2026-10-27_NEW_CASC2D_SED_SOURCE_ARCHIVE_DEEP_2D_CANOPY_GATE.md)
- [decisions Wei 2017](../decisions/2026-10-27_WEI_2017_FOREST_TREX_CANOPY_SPLASH_2D_INTEGRATED_90M_NO_CODE.md)
- [MASTER.md](../MASTER.md) top current research summaries updated
- [INDEX.md](../INDEX.md) papers 482 at start? other concurrent work changed; **after this session papers487, models100, decisions96** entries. Reindex observed actual cumulative counts; index includes other session updates.
- this handoff.

## Final research decision
**2017 Wei: positive published same-research-model forest canopy/interception+2D XY run+splash and flow source+deposition**, however 90m actual mesh and matching original source unavailable, drop-energy incomplete. Historical CASC C source is materially different, no dynamic canopy and one outlet. **No newly validated full native <=10cm software**, do not falsely recommend. Work separately evaluates fixing Classic OpenLISEM. Next independent research: published exact model release with verified LAI state path, free XY multi-edge and <=10cm actual published test, e.g. uniquely released updated TREX 2017 source rather than historic C. Do not revisit this as if new.

## Rules
First read `SYSTEM.md`, `MASTER.md`, `INDEX.md`. One paper per DOI, references maintained. No coupling name laundering, no running-code claim without actual build.
