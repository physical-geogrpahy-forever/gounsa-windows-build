# 서지정보
van der Meij, W. M., Temme, A. J. A. M., Wallinga, J., & Sommer, M. (2020). Modeling soil and landscape evolution – the effect of rainfall and land-use change on soil and landscape patterns. *SOIL, 6*, 337–358. https://doi.org/10.5194/soil-6-337-2020

# 이 논문을 찾은 이유
고운사에서 토양층별 gravel, sand, silt, clay와 유기물을 수직적으로 추적하면서 수문과 지형변화를 함께 계산하는 기존 모델이 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- soil-landscape evolution model

# 공간 구조
- raster 기반 HydroLorica
- 각 셀 아래에 여러 토양층
- 층 두께는 공간과 시간에 따라 변화

# 적용 환경
- 자연 토양경관
- 장기 토양형성
- 토지이용 변화 시나리오

# 핵심 과정
- 공간적 물수지
- runoff와 run-on
- reinfiltration
- water erosion
- tree throw
- bioturbation
- soil profile development
- erosion과 deposition

# 식생 입력
- forest와 grass 등 단순화된 식생상태
- LPJ-GUESS 수준의 PFT/cohort 동태는 아님

# 핵심 식
이 세션에서는 HydroLorica 전체 방정식을 구현수준으로 복구하지 않았다. 중요한 구조는 각 토양층이 gravel, sand, silt, clay와 유기물의 혼합비를 가지며 수문과 지형과정에 따라 그 조성이 변한다는 점이다.

# 파라미터와 단위
- layer thickness
- gravel, sand, silt, clay fraction
- organic matter pools
- water storage and flow
세부 매개변수는 원문 재검증 필요.

# 원 논문의 구현 범위
수문을 토양형성과 지형변화의 구동과정으로 명시하고, 다층 토양프로파일과 erosion/deposition을 장기적으로 함께 진화시킨다.

# 고운사에 직접 사용할 수 있는 부분
- 고정 단일토심 대신 다층 profile state를 두는 구조
- coarse fraction을 토양프로파일 구성요소로 명시하는 선례
- runoff, run-on, reinfiltration과 토양발달의 결합 구조
- erosion/deposition이 토양층 조성을 바꾸는 구조

# 새로운 coupling이 필요한 부분
고운사에서는 HydroLorica 전체를 이식하지 않고 LPJ-GUESS 수문과 별도 지형모델에 profile composition 구조만 연결하려 하므로 새로운 coupling이다.

# 한계
- 연구 사례는 장기 토양경관 발달이 중심
- 고운사처럼 fire spall provenance를 별도 추적하지 않음
- 식생 천이 표현이 LPJ-GUESS보다 단순함
- 전체 수문모듈을 가져오면 기존 고운사 수문과 중복됨

# 최종 판정
- 다층 토양과 coarse fraction 구조의 핵심 보조근거로 채택
- 전체 모델 이식은 미채택

# 참고 링크 / DOI
https://doi.org/10.5194/soil-6-337-2020
