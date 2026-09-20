# 서지정보
Nguyen Hao Quang, & Tran, V. N. (2025). *Robust uncertainty analysis of a process-based model for runoff and soil erosion simulations using surrogate modeling: a synthetic study*. Stochastic Environmental Research and Risk Assessment, 39, 2929-2944. DOI: 10.1007/s00477-025-03000-5.

# 이 논문을 찾은 이유
tRIBS-VEGGIE-FEaST가 최근에도 실제 사용되는지, 코드 접근성과 주요 erosion-parameter uncertainty가 어떻게 취급되는지 확인하기 위해 검토했다.

# 연구 유형
- process-model uncertainty analysis
- surrogate modeling / global sensitivity analysis
- tRIBS-VEGGIE-FEaST application

# 공간 구조
- process-based runoff and soil-erosion model inherited from tRIBS-VEGGIE-FEaST

# 적용 환경
- synthetic uncertainty-analysis experiments

# 핵심 과정
- runoff
- soil erosion
- model-parameter uncertainty
- surrogate modeling

# 식생 입력
No new quantitative root-erodibility linkage is introduced.

# 핵심 식
The study applies GLUE, global sensitivity analysis and Polynomial Chaos Kriging to tRIBS-VEGGIE-FEaST.

# 파라미터와 단위
Detailed uncertain erosion/hydrologic parameters are in the original article/supplement.

# 원 논문의 구현 범위
Demonstrates that tRIBS-VEGGIE-FEaST remains operational in recent research.

Importantly, the acknowledgements state that Professor Jongho Kim shared the model code and data with the authors, suggesting that the complete FEaST-coupled code is **not necessarily distributed as a fully public current repository**.

# 고운사에 직접 사용할 수 있는 부분
- recent model-use precedent
- sensitivity/uncertainty framework can guide calibration of new root/litter coupling parameters

# 새로운 coupling이 필요한 부분
No new vegetation-erodibility bridge.

# 한계
- synthetic study
- code was shared by author rather than clearly documented as a public open-source FEaST distribution

# 최종 판정
- **supporting implementation/uncertainty paper**
- tRIBS hydrology is open source, but FEaST integrated code availability still needs separate confirmation

# 참고 링크 / DOI
https://doi.org/10.1007/s00477-025-03000-5
