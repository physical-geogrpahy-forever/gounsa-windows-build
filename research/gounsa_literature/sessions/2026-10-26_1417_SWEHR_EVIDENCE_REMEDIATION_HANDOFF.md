# SWEHR 원본 복구 우선 및 신뢰성 오류 대응 인계 (2026-10-26)

## 사용자 핵심 요구
임의 식생계수/수문변수를 추가한 SWEHR 파생코드가 아닌 **McGuire et al. (2016)에 실제 사용된 SWEHR 원래 구현 버전**과 원본 입력값을 확보해 검증할 것. 숫자를 임의 조합하여 원본모형 결과라고 부르지 말 것. 이전 부정확한 연구결과의 책임성 및 정정 명시.

## 이미 실제 실행한 복구/정정
- 공식 CSDMS SWEHR V1.0 7개 파일: `third_party/SWEHR_original_v1_0_2017/`, 2017 initial commit 4e6f783..., original vs archived Git blob 7/7 exact. Original C/source+included input native Linux GCC compiled and exited 0: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40272368386
- McGuire et al. 2016 original §3.2 splash shielding `(1-Cv)+TcCv` and §3.5 Rutter canopy C(t),D(t) listed; both missing in official released C. Original study 2016 vegetation recovery Fig9/Fig10 not reproduced.
- Prior 38 spatial 2D synthetic runs are non-original **modified** C with externally imposed Ks, roughness, detachment coefficients, heuristic static canopy cap and stemflow displacement. Published original canopy/process validation not claimed. 4.2x 'species erosion' interpretation withdrawn.
- NEW incident evidence matrix `decisions/2026-10-26_SWEHR_EVIDENCE_STATUS_MATRIX.csv` categorizes 6 core documents.
- NEW main correction `decisions/2026-10-26_SWEHR_REPRODUCIBILITY_REMEDIATION.md` explains exact source/paper differences, retractions, actual previous proof, and unanswered data request.
- `MASTER.md` / `INDEX.md` updated; 38-run decision previously annotated with withdrawal.

## Important new original source retrieval lead
McGuire et al. 2016 original paper end says 'All data in the present paper are available upon request to the corresponding author'; corresponding author Luke A. McGuire historical address `lmcguire@email.arizona.edu`, **not verified current**. Source: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016JF003867 .
The journal page provides six supporting PDFs (methods+Figures S1–S5), not confirmed 2016 vegetation source code. GitHub search/Zenodo/CSDMS official original does not reveal 2016 Rutter implementation. **No author email has been sent**; request draft in remediation.md. Do not claim source obtained or 2016 Fig9/Fig10 reproduced.

## Immediate next verified work sequence
1. Send manuscript-specific code/data request with explicit user action/permission to published author contact; original publication email may now be stale.
2. If exact author code obtained, record hash/license/version/date and untouched check-in; compare every Rutter/splash expression to 2016 paper, compile and reproduce Fig9/Fig10 before any code edits.
3. If cannot obtain, explain research limitation clearly; officially released SWEHR V1.0 can still be used *unchanged*, but cannot attribute absent canopy functionality.
4. Only thereafter separate original, original-manuscript recreation, and modified experiment; do not invent couplings or choose substitute models without labeling.

## Compensation mechanism
Assistant cannot authorize monetary refunds, credits or legal damages. OpenAI Help Center has official Korean policy and support chat route: https://help.openai.com/ko-kr/articles/7232895-how-do-i-request-a-refund-for-my-chatgpt-subscription ; https://help.openai.com/en/articles/6614161-how-can-i-contact-support . A support request is user's action; no refund has been promised or initiated.
