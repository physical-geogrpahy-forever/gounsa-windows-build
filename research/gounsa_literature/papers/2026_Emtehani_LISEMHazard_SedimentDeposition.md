# 서지정보
Emtehani, S., Jetten, V., van Westen, C., & van den Bout, B. (2026). Evaluating catchment-scale physically based modeling of sediment deposition during an extreme rainfall event. *Geosciences, 16*(2), 88. https://doi.org/10.3390/geosciences16020088

# 이 논문을 찾은 이유
LISEM 계열이 현재도 sediment generation, transport, deposition과 2D flood/runout을 실제 catchment scale에서 사용하고 검증되는지 최신 사례를 확인하기 위해 검토했다.

# 연구 유형
- physically based catchment modeling
- calibration/validation
- LISEMHazard/OpenLISEM lineage

# 공간 구조
- 10 m catchment grids
- coupled sediment/flood/debris-flow system

# 적용 환경
- Dominica
- Hurricane Maria extreme rainfall
- steep tropical catchments

# 핵심 과정
- runoff
- erosion
- landslide
- debris flow
- sediment transport
- sediment deposition

# 식생 입력
- land-use based parameters
- quantitative dynamic root biomass model은 아님

# 핵심 식
이 논문의 핵심은 새로운 단일 erosion equation보다 OpenLISEM/LISEMHazard의 integrated process architecture와 실제 검증이다.

# 파라미터와 단위
- soil depth
- cohesion
- Ksat
- surface roughness
- sediment/debris-flow parameters

# 원 논문의 구현 범위
extreme rainfall event에서 sediment generation부터 downstream deposition까지 동일 LISEM 계열로 모의한다.
연구에서는 soil depth와 cohesion이 주요 uncertainty source였고 Ksat/roughness sensitivity는 해당 case에서 상대적으로 작았다.

# 고운사에 직접 사용할 수 있는 부분
- 현대 LISEM 계열이 sediment transport/deposition까지 실제 사용되고 있다는 최신 검증
- steep catchment 2D sediment model 후보로 유지할 근거

# 새로운 coupling이 필요한 부분
고운사 fire-spall, dynamic armour, LPJ-GUESS biomass coupling은 별도이다.

# 한계
- tropical hurricane setting
- landslide/debris-flow 비중이 큼
- 고운사 postfire 100-year eco-geomorphic feedback validation은 아님

# 최종 판정
- 최신 보조 검증근거
- OpenLISEM/LISEMHazard production viability 확인

# 참고 링크 / DOI
https://doi.org/10.3390/geosciences16020088
