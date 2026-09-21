# 서지정보
Tune, A. K., Druhan, J. L., Lawrence, C. R., & Rempe, D. M. (2023). Deep root activity overprints weathering of petrogenic organic carbon in shale. *Earth and Planetary Science Letters, 607*, 118048. DOI: 10.1016/j.epsl.2023.118048.

# 이 논문을 찾은 이유
deep-root carbon cycling과 bedrock weathering을 분리해 볼 때, 식생-derived CO2 signal이 bedrock 자체의 weathering signal을 얼마나 지배할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- field geochemistry
- radiocarbon/stable isotope analysis
- laboratory incubation comparison

# 공간 구조
- 16 m weathering profile
- steep forested hillslope
- bedrock vadose zone

# 적용 환경
- Northern California Coast Ranges
- shale/argillite-dominated sedimentary bedrock
- deep-rooted forest

# 핵심 과정
- modern root-derived carbon respiration
- petrogenic organic carbon oxidation
- bedrock weathering
- gas-phase CO2
- physical accessibility of reactive carbon

# 식생 입력
- deep-root-associated recently fixed carbon
- rhizosphere respiration

# 핵심 결과
OC_petro는 weathering profile에서 제거되지만 field rate는 crushed laboratory rate보다 매우 낮았다.

또한 upper weathering profile의 CO2는 petrogenic carbon oxidation보다 **recently fixed carbon associated with deep rooting**이 지배했다.

즉:
```
deep vegetation C cycling
 -> observed bedrock-zone CO2
```
signal이 매우 강해서 rock-derived carbon oxidation signal을 덮을 수 있다.

# 파라미터와 단위
- OC_petro removal [g C m^-3 yr^-1]
- radiocarbon
- stable isotopes
- gas CO2
- depth [m]

# 원 논문의 구현 범위
deep forest rhizosphere와 sedimentary-bedrock carbon weathering을 isotope evidence로 분리한다.

# 고운사에 직접 사용할 수 있는 부분
chemical-weathering model에서:
```
soil/root CO2
```
를 surface soil에만 생성시키면 안 된다는 추가 근거.

또한 weathering-zone chemistry를 해석할 때:
```
biological CO2 source
vs
rock-derived reaction source
```
를 분리해야 한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS deep-root carbon flux를 vertical CO2 source profile로 변환하는 것은 새 coupling이다.

# 한계
- shale/argillite system
- silicate soil-production flux 직접 산출이 주 목적 아님
- 고운사 sandstone coefficient source가 아님

# 최종 판정
- **보조 채택: deep-root respiration source separation constraint**
- Tune 2020 + Osorio-Leon 2025 계보를 보강

# 참고 링크 / DOI
https://doi.org/10.1016/j.epsl.2023.118048
