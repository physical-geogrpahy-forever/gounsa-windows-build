# 서지정보
Weng, E., Aleinov, I., Singh, R., Puma, M. J., McDermid, S. S., Kiang, N. Y., Kelley, M., Wilcox, K., Dybzinski, R., Farrior, C. E., Pacala, S. W., & Cook, B. I. (2022). Modeling demographic-driven vegetation dynamics and ecosystem biogeochemical cycling in NASA GISS's Earth system model (ModelE-BiomeE v1.0). Geoscientific Model Development, 15, 8153-8180. DOI: 10.5194/gmd-15-8153-2022

# 이 논문을 찾은 이유
개체목 모델보다 단순하지만 cohort 기반으로 나무, 관목, 초본과 하층식생 경쟁, 천이를 함께 모의하는 중간복잡도 식생모델 후보를 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- cohort-based vegetation demographic model

# 공간 구조
- 실제 개체 x,y를 추적하지 않음
- PFT와 크기/구조에 따른 cohort
- PPA 계열 canopy layer
- 한 site/tile 안에서 상층과 하층 구조를 표현

# 적용 환경
- 전지구 자연식생
- 나무, 관목, 초본 PFT
- 장기 천이 및 생지화학

# 핵심 과정
- 광합성 및 호흡
- 식물 생장
- 사망
- 번식 및 recruitment
- 광 경쟁
- 토양자원 경쟁
- 식생 구조 변화
- 토양 C/N
- 천이

# 식생 입력
- tree PFT
- shrub PFT
- grass PFT
- leaf C
- fine-root C
- sapwood/heartwood C
- NSC
- cohort density/size

# 시간 구조
- 생리 및 지표 과정: 시간 이하/시간 단위 계보
- 생장 및 phenology: 일 단위 계보
- demography: 연 단위

# 하층식생
- 낮은 canopy layer/understory를 PPA 구조로 표현
- shrubs and grasses가 독립 PFT로 존재
- 작은 woody cohorts도 하층에서 광 경쟁

# litter/root
- fine-root biomass 상태 존재
- leaf/fine-root turnover가 litter 및 soil C/N으로 전달
- metabolic/structural litter 및 soil organic matter pools 존재

# 원 논문의 구현 범위
식생구조, demographic competition, 토양 C/N을 결합한 cohort-based DVM.

# 고운사에 직접 사용할 수 있는 부분
- 개체목 없이 tree/shrub/grass 천이를 함께 계산
- fine-root와 litter 상태
- 상층/하층 경쟁
- 비교적 세밀한 시간 생리
- standalone BiomeE code 및 rsofun wrapper 계보

# 새로운 coupling이 필요한 부분
- LiDAR/geomorph raster의 각 공간 cell 또는 tile과 BiomeE site를 연결
- storm 직후 soil depth/moisture/disturbance state를 재시작 또는 강제 갱신
- cell 간 seed dispersal
- fire severity와 postfire 초기상태

# 한계
- native x-y landscape model이 아니라 site/tile model
- 2022 기본 설명에서는 명시적 wildfire/regrowth disturbance module이 핵심 기능으로 구현되지 않음
- lateral seed dispersal이 내장된 landscape engine은 아님

# 최종 판정
- 강한 후보
- 고운사에서 찾는 중간복잡도 cohort model에 매우 가까움
- event-coupling API와 postfire 초기화 가능성을 코드 수준에서 추가 확인 필요

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-15-8153-2022
