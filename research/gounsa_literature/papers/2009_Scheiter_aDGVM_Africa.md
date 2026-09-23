# 서지정보
Scheiter, S., & Higgins, S. I. (2009). Impacts of climate change on the vegetation of Africa: an adaptive dynamic vegetation modelling approach. Global Change Biology, 15(9), 2224–2246. https://doi.org/10.1111/j.1365-2486.2008.01838.x

# 이 논문을 찾은 이유
aDGVM 계보의 원형 구조가 실제 individual-based dynamic vegetation model인지, grass-tree competition과 fire가 어떻게 표현되는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 개발
- dynamic global vegetation model

# 공간 구조
- representative vegetation stand
- individual-based woody vegetation
- 본 논문 자체는 spatially explicit hillslope/catchment model이 아님

# 적용 환경
- Africa
- tropical grassland, savanna, forest transition

# 핵심 과정
- individual-based vegetation
- phenology
- carbon allocation
- physiology
- reproduction
- fire
- grass-tree competition

# 식생 입력
- adaptive plant traits / plant state
- grass and woody biomass
- root and shoot allocation
- climate and atmospheric CO2

# 핵심 식
본 검토에서는 개별 식보다 model architecture가 핵심이다. aDGVM은 fixed-PFT-only DGVM보다 individual-based plant state와 adaptive phenology/allocation/fire processes를 사용한다.

# 파라미터와 단위
- climate forcing
- biomass and allocation parameters
- fire and recruitment-related parameters
- 정확한 값은 원문 표와 supporting information을 production 적용 전에 재확인해야 함

# 원 논문의 구현 범위
- tropical vegetation
- grassland-savanna-forest patterns
- individual-based vegetation dynamics
- climate and fire response

# 고운사에 직접 사용할 수 있는 부분
- explicit grass-woody competition의 계보적 근거
- post-disturbance vegetation assembly를 cover correction이 아니라 생장/번식/고사로 계산하는 비교 사례

# 새로운 coupling이 필요한 부분
- Korean temperate PFT/trait parameterization
- spatial terrain grid
- lateral hydrology
- external geomorphic soil-state exchange
- dynamic soil-layer geometry remapping

# 한계
- tropical Africa 중심
- full individual-based representation이라 fine-grid watershed scale에서 계산량 우려
- actual hillslope hydrology 없음

# 최종 판정
- 보조근거
- aDGVM2 계보의 원형
- 단독 고운사 production engine으로 채택하지 않음

# 참고 링크 / DOI
- https://doi.org/10.1111/j.1365-2486.2008.01838.x
