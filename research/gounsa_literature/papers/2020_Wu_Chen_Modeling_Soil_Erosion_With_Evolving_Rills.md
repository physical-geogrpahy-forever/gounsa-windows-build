# 서지정보
Wu, B., & Chen, L. (2020). *Modeling Soil Erosion With Evolving Rills on Hillslopes*. Water Resources Research, 56, e2020WR027768. DOI: 10.1029/2020WR027768.

# 이 논문을 찾은 이유
Wu 2020의 고정 rill mask 문제를 보완하여 rill이 시간에 따라 진화하는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- representative-rill approach
- 실제 raster branching/merging network와는 다름

# 적용 환경
- hillslope

# 핵심 과정
- rill width, depth, orientation, density, number의 시간 변화
- soil erosion

# 식생 입력
- root biomass/RLD 직접입력 없음

# 핵심 식
세부 진화식은 원문 재확인 필요. 이번 감사에서 확정한 것은 rill geometry/density를 동적으로 갱신한다는 점이다.

# 파라미터와 단위
- rill width
- rill depth
- rill orientation
- rill density
- rill number

# 원 논문의 구현 범위
대표 rill의 동적 진화.

# 고운사에 직접 사용할 수 있는 부분
고정 rill mask만 쓰는 모델보다 rill evolution을 표현하는 개념적/수치적 선례.

# 새로운 coupling이 필요한 부분
LPJ-GUESS biomass와 rill evolution 또는 erodibility를 연결하면 **새로운 coupling**이다.

# 한계
- 실제 2D raster rill network의 branching/merging을 생성하는 모델은 아님
- vegetation/root effect 없음

# 최종 판정
**보조근거.** rill evolution 선례로 유지하되 고운사 최종 엔진 단독후보는 아님.
