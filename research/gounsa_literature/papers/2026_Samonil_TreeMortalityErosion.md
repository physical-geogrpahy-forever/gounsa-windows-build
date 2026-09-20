# 서지정보
Šamonil, P., Jaroš, J., Egli, M., et al. (2026). Accelerated erosion and tree mortality in a primeval temperate forest dominated by large trees, Washington, USA. Geomorphology, 508, 110373. https://doi.org/10.1016/j.geomorph.2026.110373

# 이 논문을 찾은 이유
큰 나무의 mortality와 uprooting이 실제 hillslope soil redistribution을 얼마나 지배하는지 최신 장기자료로 확인하기 위해 검토했다.

# 연구 유형
- 장기 tree census + radionuclide/geomorphic analysis

# 공간 구조
- old-growth forest hillslope

# 적용 환경
- primeval temperate forest

# 핵심 과정
- tree mortality
- uprooting
- soil redistribution
- erosion acceleration

# 식생 입력
- tree size
- mortality
- forest productivity

# 핵심 식
현재 채팅에서 직접 복구된 정량값:
tree mortality 관련 soil mass 약 3.95 t ha-1 yr-1
uprooting contribution 약 2.06 t ha-1 yr-1
최근 erosion 약 1.92-2.93 t ha-1 yr-1
장기 erosion 약 0.79-2.36 t ha-1 yr-1

# 파라미터와 단위
t ha-1 yr-1, tree size, mortality rate.

# 원 논문의 구현 범위
large-tree mortality와 slope soil redistribution의 장기관계를 관측한다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS mortality flux를 litter input만이 아니라 uprooting disturbance potential로 사용할 근거.

# 새로운 coupling이 필요한 부분
WoodC/cohort mortality를 uprooting probability와 sediment flux로 변환하는 것은 새로운 coupling이다.

# 한계
특정 old-growth forest 수치의 직접이식 금지.

# 최종 판정
- 보조근거
- woody mortality geomorphic coupling에 매우 중요
