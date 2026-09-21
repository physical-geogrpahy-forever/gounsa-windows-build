# 서지정보
Gatz-Miller, H. S., Gérard, F., Su, D., & Mayer, K. U. (2023). Two-dimensional modeling of CO2 mineral trapping through the oxalate-carbonate pathway: Influence of the root system model. *Science of the Total Environment, 904*, 166280. DOI: 10.1016/j.scitotenv.2023.166280.

# 이 논문을 찾은 이유
100년 고운사 모델에서 root biomass만으로 weathering을 표현하지 않고, 실제 root architecture와 root-zone water/solute uptake가 공간적 weathering 결과를 바꾸는지 확인하기 위해 검토했다.

# 연구 유형
- 2D reactive transport numerical model
- dynamic root architecture comparison

# 공간 구조
- 2D soil domain
- simplified root system vs discrete dynamically evolving root architecture

# 적용 환경
- Iroko root zone
- soil mineral weathering / carbonate precipitation

# 시간척도
- **170-year simulation**

고운사 100년 연구시간척도와 매우 가까운 published precedent다.

# 핵심 과정
- dynamic root architecture
- root water uptake
- solute transport
- mineral weathering
- oxalate oxidation
- soil pH zoning
- Ca mobilization
- calcite precipitation
- gas transport

# 식생 입력
- dynamically evolving root architecture
- spatial root extent
- root water uptake
- root solute uptake
- litter/oxalate return

# 핵심 식
두 root representations를 비교한다.

```
simplified root model
vs
dynamic discrete root architecture
```

root geometry는:
- local water uptake
- solute transport
- geochemical-zone geometry
- mineral-weathering-derived Ca availability
에 영향을 준다.

# 파라미터와 단위
- root growth/architecture parameters
- root uptake parameters
- hydraulic properties
- mineral reaction kinetics
- gas transport
- oxalate pathway chemistry

# 원 논문의 구현 범위
root architecture와 soil geochemistry의 공간적 coupling을 2D에서 170년 동안 계산한다.

# 고운사에 직접 사용할 수 있는 부분
매우 강한 구조적 선례다.

```
LPJ-GUESS root depth / distribution
 -> spatial water and solute uptake
 -> reactive transport
 -> weathering pattern
```

따라서 chemical weathering interface에 FineRootC 총량만 넣지 말고 root-depth/distribution을 보존할 근거가 된다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root distribution을 discrete/dynamic root geometry로 변환하지 않고도 layer-wise root uptake field로 mapping하는 단순화가 필요하다. 이는 새로운 coupling이다.

# 한계
- Iroko OCP-specific chemistry
- sandstone-specific 아님
- individual-tree/root-zone scale
- LPJ-GUESS와 직접 coupling되지 않음

# 최종 판정
- **채택: 100년 규모 root-architecture-weathering coupling의 핵심 benchmark**
- root vertical/spatial distribution을 chemical weathering interface의 필수 state로 승격할 근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.scitotenv.2023.166280
