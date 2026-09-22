# 서지정보
Sharmeen, S., & Willgoose, G. R. (2007). A one-dimensional model for simulating armouring and erosion on hillslopes: 2. Long term erosion and armouring predictions for two contrasting mine spoils. *Earth Surface Processes and Landforms, 32*(10), 1437-1453. https://doi.org/10.1002/esp.1482

# 이 논문을 찾은 이유
고운사의 목표기간 100년에서 armour가 단기 사건효과가 아니라 장기 상태변수로 사용할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- long-term numerical simulation
- ARMOUR application

# 공간 구조
- 1D hillslope
- flat cap 1-2%
- steep batter 10-30%

# 적용 환경
- Ranger Mine non-cohesive sandy gravel spoil
- Northparkes cohesive silt loam spoil

# 핵심 과정
- 100-200 yr erosion
- long-term surface coarsening
- slope-dependent armouring
- sediment transport limitation

# 식생 입력
- 없음

# 핵심 식
ARMOUR Part 1의 size-selective erosion/transport 구조를 장기간 반복사건에 적용한다.

# 파라미터와 단위
- slope
- grading
- runoff-event forcing
- entrainment/transport parameters

# 원 논문의 구현 범위
100-200 yr 시간규모에서 slope position과 material type에 따른 armour 및 erosion trajectory를 모의한다.

# 고운사에 직접 사용할 수 있는 부분
- 고운사의 100년 시간창과 직접적으로 맞는 armour model precedent
- armour equilibration을 event-by-event state update로 처리할 근거

# 새로운 coupling이 필요한 부분
고운사 사암 및 산림의 event hydrology와 식생회복은 별도이다.

# 한계
mine spoil, 1D.

# 최종 판정
- 핵심 장기 armour 근거

# 참고 링크 / DOI
https://doi.org/10.1002/esp.1482
