# 서지정보
van der Meij, W. M., Temme, A. J. A. M., Wallinga, J., & Sommer, M. (2020). Modeling soil and landscape evolution: The effect of rainfall and land-use change on soil and landscape patterns. *SOIL, 6*, 337-358.

# 이 논문을 찾은 이유
soil-landscape evolution model에서 forest와 grassland를 서로 다른 생물지형과정으로 처리하는 구조를 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- soil-landscape evolution

# 적용 환경
- 산림 / 초지

# 핵심 과정
- creep
- bioturbation
- tree throw
- water erosion
- SOM
- hydrology

# 식생 입력
- forest / grassland vegetation type

# 핵심 식
과정별 식은 모델 내부에 분리되어 있으나 biomass 직접 상태변수는 아니다.

# 파라미터와 단위
tree-throw probability 예시가 약 `0.2 trees ha^-1 yr^-1`로 이 채팅 정리에 기록됨.

# 원 논문의 구현 범위
vegetation type에 따라 creep, tree throw, hydrology, erosion protection을 분리.

# 고운사에 직접 사용할 수 있는 부분
과정 architecture 비교.

# 새로운 coupling이 필요한 부분
LPJ-GUESS cohort/biomass를 vegetation type process rates로 바꾸는 것은 새로운 coupling.

# 한계
식생모듈이 LPJ-GUESS 수준의 dynamic cohort succession은 아니다.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.5194/soil-6-337-2020
