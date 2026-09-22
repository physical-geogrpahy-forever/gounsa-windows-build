# 서지정보
Lehsten, V., Mischurow, M., Lindström, E., Lehsten, D., & Lischke, H. (2019). LPJ-GM 1.0: simulating migration efficiently in a dynamic vegetation model. Geoscientific Model Development, 12, 893-908. DOI: 10.5194/gmd-12-893-2019

# 이 논문을 찾은 이유
LPJ-GUESS의 가장 큰 고운사 적용 문제인 grid cell 사이의 비상호작용과 종자분산 부재를 해결하는 공식 확장모델인지 검토했다.

# 연구 유형
- 수치모델
- LPJ-GUESS migration coupling

# 공간 구조
- LPJ-GUESS의 비공간 replicate patch 대신 명시적으로 배치된 작은 grid cells를 사용
- 논문 실험에서는 1 km x 1 km cell
- MPI로 cell 간 종자 이동
- 전체 domain의 seed distribution을 계산

# 적용 환경
- 장거리 식생 이동
- 유럽 수목 migration
- 수백-수천 년 규모 실험

# 핵심 과정
- LPJ-GUESS의 생리 및 식생동태
- seed production
- seed dispersal
- seed bank
- establishment
- competition
- mortality

# 식생 입력
LPJ-GUESS의 기존 상태량을 유지하므로 leaf, fine root, litter, soil C/N, LAI 등 LPJ-GUESS 출력 구조와 호환 가능하다.

# 핵심 식
연말 종자 생산량을 각 cell에서 master process로 전달하고, dispersal kernel에 따라 전체 공간에 재분배한 뒤 다음 해 seed bank와 establishment에 반영한다.

# 파라미터와 단위
- migration update: annual
- published local-dynamics cell: 1 km x 1 km
- LPJ-GUESS conceptual patch area: 약 1000 m2
- seed dispersal distance: species-specific

# 원 논문의 구현 범위
LPJ-GUESS에 명시적 종자분산과 공간적 migration을 추가한다.

# 고운사에 직접 사용할 수 있는 부분
- 기존 LPJ-GUESS 생리 및 root/litter 상태를 유지
- grid cell 사이를 seed flow로 연결
- 산불 후 주변 산림에서 재정착되는 과정을 명시적으로 표현할 수 있는 구조
- 기존 고운사 LPJ-GUESS 파이프라인을 가장 많이 재사용 가능

# 새로운 coupling이 필요한 부분
- published 1 km cell을 30 m 고운사 격자로 축소
- 고운사 경계와 지형장애를 dispersal kernel에 반영
- 지형모델의 soil depth/moisture를 LPJ-GM 각 cell에 전달
- fire severity map과 LPJ-GM 초기 postfire state 연결

# 한계
논문은 30 m vegetation grid를 검증하지 않았다. 1 km를 계산비용 타협으로 채택했다. 따라서 '30 m에서도 그대로 검증됨'이라고 주장할 수 없다.

# 최종 판정
- 최우선 추가검증 후보
- LPJ-GUESS 공간 비명시성 문제를 가장 직접적으로 해결
- 30 m 적용 가능성과 계산비용은 코드 검증 필요

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-12-893-2019
