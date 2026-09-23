# 서지정보
Langan, L., Higgins, S. I., & Scheiter, S. (2017). Climate-biomes, pedo-biomes or pyro-biomes: which world view explains the tropical forest-savanna boundary in South America? Journal of Biogeography, 44(10). https://doi.org/10.1111/jbi.13018

# 이 논문을 찾은 이유
aDGVM2의 detailed model description과 South American forest-savanna application을 확인하고, climate-soil-fire controls가 vegetation assembly에 어떻게 반영되는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 응용
- trait-based individual vegetation dynamics

# 공간 구조
- representative stand simulations aggregated across geographic climate/soil space
- spatially explicit 2D seed-dispersal/fire landscape branch는 별도 2014 2D-aDGVM 계보

# 적용 환경
- South America
- tropical forest-savanna boundary

# 핵심 과정
- trait-based community assembly
- climate filtering
- soil/pedological constraints
- fire
- plant competition
- reproduction and mortality

# 식생 입력
- individual plant traits
- climate
- soil
- fire environment

# 핵심 식
상세 model formulation은 supporting information에 제공되며, vegetation structure와 trait distributions가 climate, soil and fire filtering을 통해 emergent하게 형성되는 구조이다.

# 파라미터와 단위
- individual plant state and traits
- soil/climate/fire drivers
- exact values are version specific and require source/supporting-information audit before implementation

# 원 논문의 구현 범위
- South American forest-savanna boundary
- trait-based individual community dynamics
- soil and fire effects on biome state

# 고운사에 직접 사용할 수 있는 부분
- soil state가 vegetation assembly와 경쟁을 제한하는 biological precedent
- shrub/tree/grass life-history differentiation을 확장할 수 있는 trait framework의 기반

# 새로운 coupling이 필요한 부분
- temperate Korean community parameterization
- event-wise external terrain/hydrology state overwrite
- 2D-aDGVM spatial branch와 최신 aDGVM2 ecology의 통합
- geomorphic soil geometry remap

# 한계
- tropical biome boundary 연구
- direct watershed/hillslope lateral hydrology 없음
- full individual approach의 계산량 부담

# 최종 판정
- 보조근거
- aDGVM2 model lineage의 detailed-description source

# 참고 링크 / DOI
- https://doi.org/10.1111/jbi.13018
