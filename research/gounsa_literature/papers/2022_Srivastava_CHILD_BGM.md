# 서지정보
Srivastava et al. (2022). Earth Surface Processes and Landforms. DOI: 10.1002/esp.5427. 정확한 제목과 전체 저자목록은 원문 재검증 필요.

# 이 논문을 찾은 이유
최근 eco-LEM에서 dynamic biomass와 background hillslope diffusion의 동시 처리를 확인.

# 연구 유형
- 수치모델

# 공간 구조
- CHILD 계열 landscape evolution model

# 적용 환경
- eco-geomorphic landscape evolution

# 핵심 과정
- dynamic vegetation biomass
- runoff/fluvial erosion
- hillslope diffusion
- topographic evolution

# 식생 입력
- aboveground/belowground biomass 계열

# 핵심 식
현재 채팅에서 확인한 핵심은 dynamic biomass가 있어도 background hillslope diffusivity는 biomass와 독립적으로 유지할 수 있다는 구조이다.

# 파라미터와 단위
원문 재검증 필요.

# 원 논문의 구현 범위
동적 식생과 background hillslope diffusion을 병렬 계산.

# 고운사에 직접 사용할 수 있는 부분
100년 모델에서도 background diffusion을 삭제하지 않는 구조적 근거.

# 새로운 coupling이 필요한 부분
biomass를 Kd에 직접 연결하면 새로운 coupling.

# 한계
strict biomass-dependent diffusion 직접식은 아님.

# 최종 판정
- 보조근거
