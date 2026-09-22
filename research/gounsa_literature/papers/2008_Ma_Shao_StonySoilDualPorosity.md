# 서지정보
Ma, D., & Shao, M. (2008). Simulating infiltration into stony soils with a dual-porosity model. *European Journal of Soil Science, 59*(5), 950-959. https://doi.org/10.1111/j.1365-2389.2008.01055.x

# 이 논문을 찾은 이유
고운사의 매립 석력이 많은 토양에서 석력 함량과 크기/형상이 infiltration을 바꾸는 효과를 단순 경험계수가 아닌 기존 수문물리 모델로 처리할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- infiltration experiment
- dual-porosity numerical model

# 공간 구조
- soil profile
- 1D infiltration framework

# 적용 환경
- stony soil

# 핵심 과정
- infiltration
- dual porosity
- fine-earth / stone interaction
- pore structure modification

# 식생 입력
- 없음

# 핵심 식
non-equilibrium dual-porosity model(NDPM), equilibrium dual-porosity model(EDPM), equilibrium single-pore model(ESPM)을 비교했다.
세부 governing equations는 원문 구현 시 확인한다.

# 파라미터와 단위
- volumetric rock-fragment content
- stone size
- stone shape
- matrix hydraulic parameters
- mass-transfer coefficient

# 원 논문의 구현 범위
석력 함량 증가가 infiltration을 낮추고, 큰 stone이 작은 stone보다 infiltration을 더 방해하며, stone shape에 따라 효과가 달라지는 것을 NDPM으로 재현한다.
석력은 단순히 flow cross-section을 줄이는 것뿐 아니라 fine-earth pore structure도 바꿀 수 있음을 지적한다.

# 고운사에 직접 사용할 수 있는 부분
- 매립 석력이 많은 soil profile에서 infiltration 감소를 process-based하게 계산할 기존 모델 후보
- simple ROC scaling보다 세밀한 대안

# 새로운 coupling이 필요한 부분
NDPM에서 산정한 infiltration/hydraulic state를 2D erosion engine으로 넘기면 새로운 model coupling이다.

# 한계
- erosion model이 아님
- disturbed experimental soils
- 2D surface-flow model이 아님

# 최종 판정
- 보조 후보
- 매립석력 infiltration 상세검증용

# 참고 링크 / DOI
https://doi.org/10.1111/j.1365-2389.2008.01055.x
