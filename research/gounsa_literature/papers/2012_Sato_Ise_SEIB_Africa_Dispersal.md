# 서지정보
Sato, H., & Ise, T. (2012). Effect of plant dynamic processes on African vegetation responses to climate change: Analysis using the spatially explicit individual-based dynamic global vegetation model (SEIB-DGVM). Journal of Geophysical Research: Biogeosciences, 117, G03017. https://doi.org/10.1029/2012JG002056

# 이 논문을 찾은 이유
SEIB-DGVM이 virtual forest 내부만 공간명시적인지, 아니면 여러 geographic grid 사이의 식생 이동까지 published implementation으로 다룬 선례가 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- 대륙규모 DGVM 적용
- SEIB-DGVM modification

# 공간 구조
- Africa domain: 0.5° x 0.5° geographic grid
- 각 geographic grid를 30 m x 30 m spatially explicit virtual forest 하나가 대표
- virtual forest 내부는 개별목이 위치를 가지고 정착, 경쟁, 사망
- fine root는 biomass로만 표현

# 적용 환경
- African vegetation
- climate-change transient response
- wildfire 포함

# 핵심 과정
- 개별목 생장과 경쟁
- PFT 정착
- wildfire
- 대륙규모 migration sensitivity
- biomass, LAI, soil carbon

# 식생 입력
- woody PFT biomass
- fine-root biomass
- LAI
- grass biomass
- litter/fuel pools

# 핵심 식 / 공간 이동 규칙
Control dispersal 조건:
- 정착 가능한 mesh의 90%는 해당 virtual forest 내부 woody PFT biomass에 비례해 배분
- 나머지 10%는 현재 환경에서 정착 가능하면서 두 인접 geographic grid 중 하나에 존재하는 woody PFT에 균등 배분
- geographic PFT distribution map은 1901, 2001년에 갱신

따라서 이 논문은 SEIB-DGVM에 cell-to-cell recruitment limitation을 추가한 published precedent이다.

# 파라미터와 단위
- geographic grid: 0.5° x 0.5°
- virtual forest: 30 m x 30 m
- maximum migration proxy: 1° per century, 약 100 km / 100 yr
- establishment candidate allocation: local biomass 90%, adjacent-grid eligible PFT 10%

# 원 논문의 구현 범위
대륙규모 기후변화에 대한 vegetation lag와 migration effect를 비교한다.

# 고운사에 직접 사용할 수 있는 부분
- 인접 plot의 식생 존재 여부가 다음 plot 정착에 영향을 줄 수 있다는 SEIB 계보 내 published precedent
- fire, fine-root biomass, litter/fuel, 개별목 dynamics를 한 모델 안에서 함께 사용한 선례

# 새로운 coupling이 필요한 부분
- LiDAR 유역에서 실제 거리 기반 seed kernel
- 수 m에서 수십 m plot 사이의 연례 seed exchange
- slope/ridge/topography에 의한 이동 제약
- geomorphic soil-depth and moisture feedback

# 한계
이 논문의 dispersal은 mechanistic seed production/seed transport 모델이 아니다. 0.5° geographic cells와 매우 드문 distribution-map update를 사용하며 고운사 미세격자에 그대로 적용할 수 없다.

# 최종 판정
- 보조근거
- SEIB inter-plot dispersal이 완전히 전례 없는 coupling은 아니라는 중요한 근거
- 고운사용 fine-scale dispersal은 새 구현 필요

# 참고 링크 / DOI
https://doi.org/10.1029/2012JG002056
