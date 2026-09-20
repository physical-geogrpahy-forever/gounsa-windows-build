# 서지정보
Pelletier et al. (2018). Earth Surface Processes and Landforms. DOI: 10.1002/esp.4306. 정확한 제목과 전체 저자목록은 원문 재검증 필요.

# 이 논문을 찾은 이유
biomass를 hillslope diffusivity Kd에 직접 연결한 2010년대 LEM 사례를 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- 장기 landscape evolution sensitivity experiment

# 공간 구조
- landscape evolution model
- 2D 지형 진화

# 적용 환경
- 장기 지형발달

# 핵심 과정
- hillslope diffusion
- runoff/fluvial erosion
- vegetation-biomass feedback

# 식생 입력
- biomass B

# 핵심 식
현재 채팅에서 확인한 구조는 biomass 증가가 Kd를 증가시키는 bioturbation 가설과 감소시키는 physical shielding 가설을 각각 시험했다는 것이다.
Runoff erodibility에도 biomass 감쇠항을 사용했다.

# 파라미터와 단위
- B, Bmax
- Kd
- biomass-effect coefficient
- exact 식과 단위는 원문 재검증 필요

# 원 논문의 구현 범위
biomass-Kd 관계의 부호를 경쟁가설로 비교하는 장기 LEM 실험.

# 고운사에 직접 사용할 수 있는 부분
biomass가 Kd에 직접 들어갈 수 있다는 published precedent.

# 새로운 coupling이 필요한 부분
100년 LPJ-GUESS biomass time series를 연도별 Kd로 변환하는 것은 새로운 coupling.

# 한계
장기 민감도 실험이며 고운사 100년 시간척도에 계수를 직접 이식할 수 없음.

# 최종 판정
- 보조근거 / 민감도 참고
- 주 사면확산식으로는 채택하지 않음

# 참고 링크 / DOI
https://doi.org/10.1002/esp.4306
