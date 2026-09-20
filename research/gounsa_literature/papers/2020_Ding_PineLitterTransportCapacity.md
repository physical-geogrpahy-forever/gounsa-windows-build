# 서지정보
Ding, L., Fu, S., Liu, B., Yu, B., Zhang, G., & Zhao, H. (2020). Effects of *Pinus tabulaeformis* litter cover on the sediment transport capacity of overland flow. *Soil and Tillage Research, 204*, 104685.

# 이 논문을 찾은 이유
litter가 detachment뿐 아니라 sediment transport capacity를 직접 줄이는지 확인하기 위해 검토했다.

# 연구 유형
- 실험 + 예측식

# 공간 구조
- flume/plot

# 적용 환경
- pine litter-covered slope

# 핵심 과정
- overland-flow sediment transport capacity

# 식생 입력
- litter cover

# 핵심 식
`T_c`가 litter cover 증가에 따라 지수적으로 감소하며 unit discharge, slope, litter cover로 예측.

# 파라미터와 단위
unit discharge, slope gradient, litter cover.

# 원 논문의 구현 범위
litter의 flow resistance와 sediment transport capacity 효과를 실험.

# 고운사에 직접 사용할 수 있는 부분
litter를 Manning n 하나에만 넣지 않고 `T_c`에도 별도 영향 가능하다는 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS SurfaceLitC를 litter cover/geometry와 `T_c`로 변환하면 새로운 coupling.

# 한계
수치 landscape model 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.still.2020.104685
