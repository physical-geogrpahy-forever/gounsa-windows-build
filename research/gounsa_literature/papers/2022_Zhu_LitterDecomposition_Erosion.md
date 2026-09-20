# 서지정보
Zhu, F., & Cheng, J. (2022). *Comparison of the effects of litter decomposition process on soil erosion under simulated rainfall*. Scientific Reports, 12, 20929. DOI: 10.1038/s41598-022-25035-2.

# 이 논문을 찾은 이유
surface litter protection을 단순 mass 하나로만 처리해도 되는지, decomposition state가 overland-flow hydraulics와 erosion protection을 바꾸는지 확인하기 위해 검토했다.

# 연구 유형
- forest rainfall-simulation experiment
- numerical model 아님

# 공간 구조
- rainfall-simulation plots / litter layers

# 적용 환경
- Pinus massoniana forest
- subtropical forest, Hubei, China
- non-decomposed versus semi-decomposed litter

# 핵심 과정
- overland-flow hydraulics
- rainfall interception
- erosion reduction
- litter decomposition

# 식생 입력
Seven litter mass/coverage gradients were tested across:
- non-decomposed litter
- semi-decomposed litter
with slope and rainfall-intensity treatments.

# 핵심 식
No universal erosion-equation parameterization was proposed.
Measured hydraulic response demonstrates that Reynolds number and other overland-flow characteristics vary with litter mass and decomposition stage.

# 파라미터와 단위
- litter coverage mass: g m^-2
- rainfall intensity: 60 and 120 mm h^-1
- slope: 5 and 10 degrees
- Reynolds number and hydraulic indices

# 원 논문의 구현 범위
Quantifies how litter decomposition state changes its hydraulic protection function.

# 고운사에 직접 사용할 수 있는 부분
Supports at least two exposed-litter traits:
```
SurfaceLitterMass
+ decomposition state / bulk structure
```
rather than a universal litter-mass coefficient.

# 새로운 coupling이 필요한 부분
LPJ-GUESS litter turnover/decomposition state -> hydraulic/detachment modifier remains a **new coupling**.

# 한계
- experimental
- no dynamic root state
- no full erosion engine

# 최종 판정
- **보조근거**
- decomposition state should be preserved if a surface-litter submodel is constructed

# 참고 링크 / DOI
https://doi.org/10.1038/s41598-022-25035-2
