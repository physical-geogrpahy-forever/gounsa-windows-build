# 서지정보
Scheiter, S., Langan, L., & Higgins, S. I. (2013). Next-generation dynamic global vegetation models: learning from community ecology. New Phytologist, 198(3), 957–969. https://doi.org/10.1111/nph.12210

# 이 논문을 찾은 이유
aDGVM2가 실제로 plant community assembly, recruitment, competition, mortality를 individual level에서 계산하는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 개발
- conceptual/methodological vegetation-model paper

# 공간 구조
- representative stand
- individual-based plants
- 본 버전은 geographic 2D landscape model이 아님

# 적용 환경
- trait-based community assembly
- grass-tree vegetation

# 핵심 과정
- individual plant growth
- reproduction
- mortality
- trait inheritance
- mutation/crossover
- competition
- fire response
- emergent community assembly

# 식생 입력
- individual trait sets
- plant type
- leaf traits
- phenology
- carbon allocation
- root/crown architecture
- resprouting
- reproduction and mortality traits

# 핵심 식
개별 plant의 trait combination이 성장과 경쟁, 번식 성공을 결정하고, 세대 간 trait inheritance 및 mutation을 통해 community trait spectrum이 형성되는 구조이다.

# 파라미터와 단위
- trait ranges
- plant biomass, height, LAI
- reproductive and mortality parameters
- fire-response traits
- exact parameter ranges는 원문과 supporting information 재확인 필요

# 원 논문의 구현 범위
- each plant has unique trait combination
- growth, reproduction and mortality at individual level
- community assembly and coexistence emerge from competition and trait filtering

# 고운사에 직접 사용할 수 있는 부분
- criterion 2에 매우 강한 benchmark
- postfire 초기 군집을 predefined cover trajectory가 아니라 recruitment/competition/mortality로 만들 수 있는 접근
- grass와 woody life-history competition을 명시적으로 표현하는 구조

# 새로운 coupling이 필요한 부분
- shrub-specific Korean calibration
- actual geomorphic grid
- external soil-state overwrite
- hillslope lateral water redistribution
- erosion/deposition layer remapping

# 한계
- full individual-based model
- source lineage is tropical/savanna oriented
- fine terrain hydrologic coupling을 제공하지 않음

# 최종 판정
- 강한 biological benchmark
- aDGVM2 conditional candidate 계보의 핵심 논문

# 참고 링크 / DOI
- https://doi.org/10.1111/nph.12210
