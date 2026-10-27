# 서지정보
Aksoy, H., Gedikli, A., Yilmaz, M., Eris, E., Unal, N. E., Yoon, J., Kavvas, M. L., & Tayfur, G. (2020). Soil erosion model tested on experimental data of a laboratory flume with a pre-existing rill. *Journal of Hydrology, 581*, 124391. https://doi.org/10.1016/j.jhydrol.2019.124391.

# 이 논문을 검색한 이유
기존 고운사 목록에 없는 **실제 양방향 종·횡 경사의 2D 강우유출 + 세류/세류간 침식 + 유사이송 실험 검증모델** 탐색. OpenLISEM은 사용자 지정 다른 Work에서 담당.

# 연구 유형
동료심사 독립 2D 수문-토양침식 모형 및 강우모사 실험. 2020 Elsevier publisher full abstract/official author university affiliation page 직접 확인. **본문 Methods 전문은 Elsevier 구매제한으로 확보하지 못했으므로 원본 수치식/격자, 결과 성능 수치를 추정해 쓰지 않음.**

# 공간 구조
원논문 abstract가 `process-based two-dimensional rainfall-runoff mathematical model` with erosion/sediment module이라고 명시. 실험수로에는 종방향 및 횡방향 모두 경사를 줘 세류 하나를 미리 형성. 그러나 그 '2D'가 원본 full-SWE x/y momentum인지 diffusive approximation인지 **본문 방정식 확인 전 미확정**. Preformed longitudinal rill ≠ event-generated dynamic incision.

# 적용 환경
실내 나지 모래 기반 실험수로, 세류 형성 후 강우모사, 45–105mm/h 강우강도, 5–20% 종/횡경사, 균일한 고운 모래 및 중간 모래. 한국 산림/사암/억새/참나무가 아님.

# 핵심 과정
2D 강우유출, 세류와 세류간 유사이송, 강우사상 sedigraph simulation and calibration. Sediment dynamics/model calibrated against experimental sediment discharge. **Native canopy storage, leaf-drip rainfall KE and deposited-layer mass/process, bed-elevation feedback not documented in accessible abstract**.

# 식생 입력
Bare flume. Quantitative LAI, canopy water-storage, throughfall/stemflow, leafdrip KE or litter layer absent in accessible original test description.

# 핵심 식 / 파라미터 / 단위
Rainfall 45–105 mm h^-1, x/y slope gradients 5–20%; characteristic particle size fine/medium sand. Governing 2D flow and erosion PDE **exact form UNKNOWN** without full paper; Δx [m] and Δt [s] **UNKNOWN**. Don't mistake lab flume dimensions for actual model cell or 5cm test.

# 원 논문의 구현 범위
Published event-scale 2D rill and interrill water/sediment response compared with actual dual-slope artificial rainfall under varying intensities. **User's freely spreading 2D SWE and same-run canopy activation not established**. Author university https://research.itu.edu.tr/en/publications/soil-erosion-model-tested-on-experimental-data-of-a-laboratory-fl-2/ confirms attribution and paper.

# 원본 코드 공개 / 실행 검증
GitHub repository exact author title keywords `Aksoy Gedikli Kavvas`, `Aksoy Gedikli` and paper title returned no **matching complete publicly licensed original hydrodynamic + sediment solver**; publisher DOI has no specific software/code archive in publicly available metadata. Neither compile nor cm-grid benchmark performed. Code *might* exist privately; absence from bounded search not proof of nonexistence.

# 고운사 직접 사용 가능한 부분
Demonstrates combined longitudinal/transverse slopes, already-incised micro-rill and rainfall range overlapping 10–50mm/h upper end (45–50mm/h overlap); comparison of native sediment yield over rill/interrill with plot experimental observation. Benchmark principle only.

# 새로운 coupling
Adding LAI interception, leafdrip energy or bespoke 5cm numerical solver is **new model coupling/porting**, not an existing proven Aksoy version.

# 한계 및 최종 판정
**보조 학술근거, 주모델 채택 보류**: actual 5cm computational mesh and corresponding source NOT verified; native canopy absent in field test; full SWE/dynamic deposition details not verified.

# 참고 자료
https://doi.org/10.1016/j.jhydrol.2019.124391
https://www.sciencedirect.com/science/article/pii/S0022169419311266
https://research.itu.edu.tr/en/publications/soil-erosion-model-tested-on-experimental-data-of-a-laboratory-fl-2/


## 2026-10-27 추가 원본 'Introduction/Section snippets' 중요 정정 (같은 DOI, 별도 논문 중복 없음)
ScienceDirect 원문 공개 Introduction https://www.sciencedirect.com/science/article/pii/S0022169419311266 직접 열람:
- 논문 자체는 'two-dimensional continuity equation of sediment'이라고 기술하나 **2016년에 기반한 수문부는 2D control volume에서 유도되었음에도 실제 'only the longitudinal direction of flow is taken into account'**라고 저자 본문에 적음. 이어 이번 모형을 reduced number of dimensions로 기술. 따라서 **free X/Y full SWE dynamic 2D overland solver가 이 2020 출판 모형에서 검증되었다고 주장하면 안 됨**.
- 실험수로의 **실제 물리 크기 6.50m×1.36m×깊이0.17m**, 조절 가능한 종·횡방향 경사5–20%, 사전 형성 세류. 모래 D50 **0.45mm / 0.15mm**. 수로 물리 폭을 numerical `dy`에 대응시키거나 5cm 격자 실증이라고 주장 금지.
- 해당 연구는 2D 미세지형(세류 및 세류간 구역)과 2D sediment continuity라고 소개되지만, **수문 유동 차원이 감소된 formulation**이란 점에서 고운사의 진정한 각 방향 2D 관성모멘텀 수송 요구 미달. Exact underlying PDE and discrete sediment direction needs full paper equation; 현재 증거만으로 '100% 순수 1D entire sediment model'이라고도 단정하지 않는다.
- 저자는 rainfall-driven / runoff-driven erosion 둘 다 고려한다고 Introduction에서 명시. Canopy model activation 여전히 확인 안 됨.
- Elsevier indexed **section snippets** indicate two parameter beta/epsilon constants unity and other calibration/validation from flume, but quantitative NSE not confirmed. Avoid conflating validation language with independent field/vegetation holdout.
**Updated stricter verdict:** not a demonstrated free X/Y two-component SWE hydrodynamic published model. Only published rill/interrill process benchmark.
