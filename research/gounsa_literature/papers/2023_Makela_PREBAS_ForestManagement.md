# 서지정보
Mäkelä, A., Minunno, F., Kujala, H., Kosenius, A.-K., Heikkinen, R. K., Junttila, V., Peltoniemi, M., & Forsius, M. (2023). Effect of forest management choices on carbon sequestration and biodiversity at national scale. Ambio, 52(11), 1737–1756. https://doi.org/10.1007/s13280-023-01899-0

# 이 논문을 찾은 이유
PREBAS가 고운사에서 원하는 가벼운 tree cohort/stratum 구조, daily soil-water response, ground vegetation을 동시에 제공하는 새 후보인지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 응용
- national wall-to-wall forest simulation
- PREBAS forest growth and carbon-balance model

# 공간 구조
- wall-to-wall grid
- 각 spatial unit에서 stand/stratum forest state
- actual lateral hillslope hydrology는 없음

# 적용 환경
- Finland national forest landscape

# 핵심 과정
- PRELES: daily GPP, evapotranspiration, soil water
- CROBAS: tree growth and structural allocation
- YASSO: soil carbon
- mortality
- forest management and regeneration
- empirical ground-vegetation carbon module

# 식생 입력
- forest stand/stratum initial state
- basal area
- height
- DBH
- species
- site fertility
- soil and climate state

# 핵심 식
본 검토에서는 모델 architecture가 핵심이다.
PREBAS는 daily canopy gas exchange and soil water를 계산하고, 획득한 carbon을 tree growth에 배분한다.

# 파라미터와 단위
- daily meteorological forcing
- stand structure
- ground vegetation carbon output
- tree growth/allocation은 주로 annual update

# 원 논문의 구현 범위
- Finland wall-to-wall grid
- management scenarios to 2050
- tree C, soil C, ground vegetation C
- daily GPP/ET/soil water
- annual tree structural growth and litter exchange

# 고운사에 직접 사용할 수 있는 부분
- 가벼운 stand/stratum representation과 daily soil-water coupling의 비교
- spatial raster application precedent
- litter/soil-C interface 참고

# 새로운 coupling이 필요한 부분
- explicit herb/shrub demographic recruitment and succession
- lateral hillslope hydrology
- event-time geomorphic soil-state overwrite
- soil-layer geometry remapping

# 한계
- ground vegetation은 explicit demographic cohort succession이 아니라 empirical biomass module이다.
- tree structural development는 annual scale이다.
- fine hillslope/catchment lateral water redistribution precedent가 없다.

# 최종 판정
- 탈락
- criterion 1은 부분 충족 가능하나 criterion 2와 4에서 strict target에 미달
- daily ecohydrology comparator로만 유지

# 참고 링크 / DOI
- https://doi.org/10.1007/s13280-023-01899-0
