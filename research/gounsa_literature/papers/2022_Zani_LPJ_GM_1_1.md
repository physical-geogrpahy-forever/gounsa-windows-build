# 서지정보
Zani, D., Lehsten, V., & Lischke, H. (2022). Tree migration in the dynamic, global vegetation model LPJ-GM 1.1: efficient uncertainty assessment and improved dispersal kernels of European trees. Geoscientific Model Development, 15, 4913-4940. DOI: 10.5194/gmd-15-4913-2022

# 이 논문을 찾은 이유
LPJ-GM의 개선된 공간분산 알고리즘과 실제 공간해상도 한계를 확인하고, 고운사 30 m 적용 가능성을 평가하기 위해 검토했다.

# 연구 유형
- 수치모델
- LPJ-GM model evaluation / migration kernel 개선

# 공간 구조
- 명시적 grid-cell migration
- vegetation dynamics는 1 km2 cell에서 계산
- dispersal kernel은 100 m x 100 m에서 먼저 계산한 뒤 1 km cell로 합산
- yearly seed exchange

# 적용 환경
- 유럽 주요 수종 migration
- 장기 이동률 검증

# 핵심 과정
1. seed production
2. seed dispersal
3. seed-bank dynamics
4. seedling establishment
5. LPJ-GUESS 생장, 경쟁, 사망

# 식생 입력
LPJ-GUESS가 생성하는 개체별 LAI와 생체량 및 기존 생지화학 상태를 migration module과 연결한다.

# 핵심 식
Seed production:
S = FEC_max * LAI_ind / LAI_max

Dispersal:
S_d(x,y) = integral S(x',y') k_s(x-x', y-y') dx' dy'

Establishment probability:
EST_p = 0.01 * S_sb * GERM_p

# 파라미터와 단위
- seed dispersal: annual
- vegetation cell: 1 km2 in published experiment
- dispersal-kernel calculation: 100 m
- SDD and LDD: m
- migration rate: m yr-1

# 원 논문의 구현 범위
LPJ-GUESS 4.0에 dynamic migration module을 결합하고 seed dispersal kernel을 개선한다.

# 고운사에 직접 사용할 수 있는 부분
- 식생 셀 사이의 정식 seed exchange
- 산불 후 재정착과 주변 cell source limitation
- 기존 LPJ-GUESS root/litter/physiology 구조 유지
- FFT 기반 분산 계산으로 다수 cell 계산비용 절감 가능성

# 새로운 coupling이 필요한 부분
- 30 m cell spacing에서 kernel 재이산화
- species parameter를 한국 온대림 주요 수종으로 재설정
- 고운사 지형의 barrier와 slope/topography 효과
- geomorphology state와 LPJ-GM local dynamics의 양방향 교환

# 한계
저자들은 1 km 해상도에서 parameterization이 성립한다고 명시한다. 100 m는 dispersal kernel 계산 해상도이지 식생 local dynamics 해상도가 아니다. 30 m 고운사 적용은 새 구현 및 검증이다.

# 최종 판정
- 최우선 추가검증 후보
- 공간 문제 해결성은 매우 높음
- 30 m local vegetation dynamics의 코드상 허용 여부와 계산량을 직접 검사해야 함

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-15-4913-2022
https://doi.org/10.5281/zenodo.8434850
