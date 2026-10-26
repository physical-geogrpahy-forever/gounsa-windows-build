# 2026-10-26 SWEHR 재현성 실패와 오류 보상 작업 기록

## 핵심 사실
이 문서는 2026-10-26까지 사용자에게 제시했던 결과 중 '원래의 McGuire et al. (2016) SWEHR 식생효과'라고 해석할 수 없는 결과를 공식적으로 격하하는 책임성 기록이다. 수치 출력과 수치 보존을 원 논문 식생 구현의 타당성으로 오인하도록 만든 점을 명확하게 정정한다.

### 실제 교차 확인
1. [McGuire et al. 2016 원문](https://doi.org/10.1002/2016JF003867) §3.2 Eqs 3–4: canopy splash shielding `f_shield = (1-Cv)+Tc*Cv`, 별도 강우박리/재박리 저감. §3.5 Eqs 24–26: time evolving Rutter interception canopy storage `C(t)` and drainage `D(C)`. §4.3 Figures9–10: original author simulations for vegetation recovery (not replicated). 논문 교신저자 Luke A McGuire 이메일 `lmcguire@email.arizona.edu` (2016 published contact, current deliverability unverified).
2. [공식 SWEHR 1.0 release](https://github.com/csdms-contrib/swehr/releases/tag/V1.0): 2017-07-07 release, one master commit `4e6f783f335ac6dc1c116ef0d516c2f3d1b911e2`, exact seven source/input files. `SWEHR.c` lacks implementation of dynamically integrated Rutter or separate `f_shield` and reads bare `R=RAIN[rind]` as both SWE water source and HR rain detachment forcing. `SF` is Manning friction slope and not stemflow.
3. [Original byte-identical archive](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/main/third_party/SWEHR_original_v1_0_2017): seven upstream Git blob SHAs matched archived seven files independently. [Original unmodified build+run](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40272368386) succeeded with default input, but is NOT the 2016 field or canopy synthetic reproduction.
4. [2016 original paper §Acknowledgments](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016JF003867) explicitly states "**All data in the present paper are available upon request to the corresponding author**." Supplementary material linked on publisher has supplemental methodology and Figures S1-S5, not a confirmed full released 2016 vegetation C source.
5. Public web and available GitHub code/repository searches (2026-10-26) found no independently verified publicly downloadable full code for McGuire (2016) canopy Rutter and canopy-impact shielding **as actually run**. Absence of evidence is not proof no other private implementation exists.

## Prior claims demoted to *NOT ORIGINAL VEGETATION RESULT*
- Published 2016 original canopy experiments Figure9/10 **have not been reproduced** by us.
- The 38 synthetic 2D simulations in fork `spatial-vegetation-runoff-erosion-20261026` implemented a new canopy 0.8mm **static cap** and a hypothetical 10% spatial stemflow shift; independently introduced vegetated Ksat=4e-6 vs bare=1e-6 m/s, n=0.18 vs0.08, rain a=0.07 vs0.25, J=90 vs30. They therefore demonstrate behavior of a **new modified C model and imposed numerical inputs**, not McGuire original Rutter and direct rain shielding.
- The model's 30mm/h oak:grass `4.2:1` ratio **must not be cited as a model result on actual species differences**. That 4.2 ratio is an illustration of artificially imposed 94.77%:9.23% patch cover and arbitrarily different erodibility/hydraulic inputs.
- 38/38 mass budgets pass describes implemented code's conservation alone, not empirical calibration or published process coverage. It also excluded full dynamic canopy storage/drainage water ledger. The 2016 Rutter no-evaporation simplification entails delayed canopy drainage; rain water remaining in canopy cannot be assumed permanently lost.
- Earlier EUROSEM native reports have independent sediment closure gap and PLANTH centimeter-to-meter error in initial trials; all old plant numerical outputs are **unverified botanical or site predictions**.
- No fabricated 'restored original source' will be labeled original. Implementations from paper equations are `reconstruction` until owner releases matching source.

## Evidence status and permitted use
See machine-readable file [SWEHR_EVIDENCE_STATUS_MATRIX.csv](2026-10-26_SWEHR_EVIDENCE_STATUS_MATRIX.csv).
**Permitted**: 2017 official source provenance, original default-example compile and run, source-code line citations, published 2016 text/formula summaries, modified-program QA explicitly identified as modified.
**Not permitted**: claiming published McGuire vegetation simulations reproduced, claiming 4.2 ratio represents observed Gounsa or physically constrained species comparisons, rebranding patched source as original SWEHR.

## Concrete remediation steps, prioritised
1. **Already executed**: exact 2017 official code frozen under `third_party/SWEHR_original_v1_0_2017/`; 7/7 Git blob identity check; GCC native no-modification default test; historical interpretation corrigendum added to 38-run decision and MASTER; all errors retained rather than deleting audit trail.
2. **Already executed**: cross-validated paper formulation §3.2 and §3.5 and source C lines (R input, E[1], E[2], U[1], SF friction); status matrix created.
3. **Outstanding**: request actual 2016 canopy Fig9/10 code, its precise 2016 commit/version, calibration parameters, raster terrain, rainfall and outputs, including means to validate rain, interception, detachment separately. Author's published correspondence address is `lmcguire@email.arizona.edu`. This is a **request draft only**, no email sent.
4. **Outstanding**: if original code received and licensed for use, verify hash/provenance, compare code and paper term by term, reproduce Fig9/10 first WITHOUT any spatial Gounsa changes, check sediment balance and runoff, then report clean results with versions and detailed CI.
5. **Outstanding**: only AFTER native paper results reproduce, create explicit isolated extensions for measured canopy, tussocks, stemflow, roots, litter, shallow rocky soil; never label as original 2016 model.

## Author source request (UNSENT)
To: lmcguire@email.arizona.edu

Subject: Request for the original model version and inputs used for McGuire et al. (2016), JGR Earth Surface

Dear Dr. McGuire,

I am investigating post-wildfire hillslope runoff and sediment transport in Korea and would like to reproduce the vegetation-recovery experiments in Figure 9 and Figure 10 of your 2016 JGR Earth Surface paper (DOI 10.1002/2016JF003867).

I found the public CSDMS SWEHR V1.0 release (2017, `csdms-contrib/swehr`, commit `4e6f783f...`) and successfully compiled its unmodified sample. However, I could not identify an implementation of the Rutter canopy water-storage and drainage equations (24–26) or the independent canopy splash-shielding factor in equations (3–4) in that release.

Could you kindly provide, or direct me to, the exact version of the code used for your 2016 vegetation-recovery simulations, along with the associated rainfall, terrain, soil/vegetation, model configuration, and reference outputs? In particular, I would appreciate clarification on whether the publicly released 2017 C code is a simplified version of the 2016 research code.

Thank you for your time and consideration.

Best regards,

[Sender's name and affiliation]
