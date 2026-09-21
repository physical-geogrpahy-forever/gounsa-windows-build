# 서지정보
Baars, C., Jones, T. H., & Edwards, D. (2008). Microcosm studies of the role of land plants in elevating soil carbon dioxide and chemical weathering. *Global Biogeochemical Cycles, 22*, GB3019. DOI: 10.1029/2008GB003228.

# 이 논문을 찾은 이유
root respiration -> soil CO2 -> chemical weathering 경로가 단순 이론이 아니라 실험적으로 관찰되는지 확인하기 위해 검토했다.

# 연구 유형
- controlled microcosm experiment

# 공간 구조
- tray-scale plant-substrate system

# 적용 환경
- analog plants with contrasting rooting systems
- ambient and elevated atmospheric CO2

# 핵심 과정
- root development
- root respiration
- substrate CO2
- carbonic acid production
- silicate chemical weathering

# 식생 입력
- rooting-system complexity
- living rooted plants
- dead organic matter treatment

# 핵심 결과
deep/complex rooting system을 가진 plant treatment에서 substrate CO2가 증가했다.

단순/no-root plants 또는 dead organic matter만 추가한 treatment는 같은 방식으로 substrate CO2를 증가시키지 않았다.

이는:
```
living roots
 -> belowground respiration
 -> elevated soil CO2
 -> carbonic-acid weathering potential
```
경로의 실험적 근거다.

# 파라미터와 단위
- atmospheric CO2 treatments
- substrate CO2 concentration
- plant/rooting type
- weathering-related solute response

# 원 논문의 구현 범위
rooting complexity와 belowground CO2 generation을 controlled environment에서 비교.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS에서 total NPP보다:
- living-root state
- root respiration
- root depth
를 weathering interface에 넣어야 한다는 실험적 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC / root maintenance respiration을 soil pCO2 profile로 바꾸는 것은 새 coupling.

# 한계
- experimental analogue
- exact forest species / sandstone system 아님
- direct numerical production law 없음

# 최종 판정
- **보조근거: root respiration -> soil CO2 pathway**
- B-WITCH/Osorio-Leon process chain을 독립적으로 지지

# 참고 링크 / DOI
https://doi.org/10.1029/2008GB003228
