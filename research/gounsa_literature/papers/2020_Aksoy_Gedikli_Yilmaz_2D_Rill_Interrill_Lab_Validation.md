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
