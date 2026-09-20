# 서지정보
De Baets, S., Torri, D., Poesen, J., Salvador, M. P., & Meersmans, J. (2008). *Modelling increased soil cohesion due to roots with EUROSEM*. Earth Surface Processes and Landforms, 33(13), 1948-1963. DOI: 10.1002/esp.1647.

# 이 논문을 찾은 이유
root density/root architecture를 실제 process-based erosion model 내부의 soil-resistance variable로 직접 넣은 numerical implementation이 있는지 확인하기 위해 검토했다.

# 연구 유형
- EUROSEM numerical model modification and scenario analysis
- root-density/concentrated-flow experiment-based parameterization

# 공간 구조
- EUROSEM event-based rill/interrill framework
- slope-plane / linked-element routing
- genuine 2D SWE는 아님

# 적용 환경
- root-permeated silt-loam topsoil
- fibrous-grass roots and tap-rooted species
- concentrated-flow erosion

# 핵심 과정
- runoff detachment
- concentrated-flow erosion
- root-enhanced soil cohesion
- sediment transport capacity
- runoff and soil loss scenario analysis

# 식생 입력
- measured root density
- root architecture/root-system type
- fibrous versus tap-root systems

# 핵심 식
The implementation does not simply multiply erosion by vegetation cover.

Measured soil detachment is used with the EUROSEM runoff-detachment equation to back-calculate flow detachment efficiency beta.

Soil cohesion is then related to beta through:
```
C = (-1/0.85) ln(beta/0.79)
```

Power and exponential relationships are subsequently fitted between measured root density and the calculated soil-cohesion input.

Therefore the actual numerical pathway is:
```
root density / architecture
 -> soil cohesion C
 -> EUROSEM concentrated-flow detachment
```

Exact root-density-to-cohesion regression coefficients must be taken from the original article tables/equations before coding.

# 파라미터와 단위
- root density: study-specific mass/volume or root-density metric
- soil cohesion C: kPa-scale EUROSEM input
- detachment efficiency beta: EUROSEM flow-detachment efficiency

# 원 논문의 구현 범위
The paper explicitly modifies the EUROSEM soil-cohesion input to represent quantitative root effects and performs erosion scenarios with the modified model.

Important result:
- fibrous roots increase erosion-resisting cohesion more strongly than tap roots at comparable root-density states
- root-binding cohesion relevant to erosion is much smaller than the tensile-root reinforcement mobilized in slope failure, confirming that surface erosion and landslide root mechanics should remain separate

# 고운사에 직접 사용할 수 있는 부분
This is one of the strongest published numerical precedents for:
```
quantitative root state
 -> erosion-specific soil cohesion
 -> concentrated-flow detachment
```

It may be more defensible than applying a generic root multiplier to Kr alone.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC/RMD/RLD -> De Baets root-density metric -> cohesion in a genuine 2D engine is **새로운 coupling**.

If the receiving 2D model does not use EUROSEM cohesion directly, translating cohesion to its erosion-threshold/detachability parameter is another new coupling.

# 한계
- not genuine 2D
- experimental soil/species parameterization
- exact root-density-to-cohesion coefficients are not universal
- EUROSEM original vegetation representation still contains cover-based effects for rainfall/interrill processes

# 최종 판정
- **채택: quantitative root -> concentrated-flow soil-cohesion model precedent**
- final 2D engine: no
- high priority for the root-resistance submodel

# 참고 링크 / DOI
https://doi.org/10.1002/esp.1647
