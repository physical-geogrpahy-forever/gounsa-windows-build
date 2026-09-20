# 서지정보
Verbruggen, W., Wårlind, D., Horion, S., Meunier, F., Verbeeck, H., Wieckowski, A., Tagesson, T., & Schurgers, G. (2025). *Implementing a process-based representation of soil water movement in a second-generation dynamic vegetation model: application to dryland ecosystems (LPJ-GUESS-RE v1.0)*. Geoscientific Model Development, 18, 6623-6645. DOI: 10.5194/gmd-18-6623-2025.

# 이 논문을 찾은 이유
LPJ-GUESS의 vertical root distribution을 정확한 식으로 복구하고, FineRootC를 토층별 RLD로 분배할 때 임의적인 뿌리깊이식을 새로 만들지 않기 위해 검토했다.

# 연구 유형
- LPJ-GUESS model development
- process-based soil hydrology implementation

# 공간 구조
- LPJ-GUESS patch/PFT structure
- standard 15-layer soil profile
- updated version permits variable layer thickness

# 적용 환경
- dryland ecosystems
- model-development context

# 핵심 과정
- soil water movement
- root water uptake
- vertical root distribution
- groundwater/bottom-boundary effects

# 식생 입력 / 상태
Standard LPJ-GUESS v4.1 root uptake uses the PFT-specific root fraction in each soil layer.

# 핵심 식
Vertical cumulative root distribution is:

```
RD_cumul(z) = 1 - beta_root^z
```

where:
- `RD_cumul`: cumulative root fraction from the soil surface to depth z
- `beta_root`: PFT-specific root-distribution shape parameter
- `z`: depth using the convention of the Jackson et al. parameterization

For layer i bounded by `z_top` and `z_bottom`, the corresponding fraction follows from the cumulative difference:

```
f_i
= RD_cumul(z_bottom) - RD_cumul(z_top)
```

In the standard implementation, if the cumulative distribution does not sum to one at the bottom of the soil profile, the remaining fraction is assigned to the bottom layer.

# 파라미터와 단위
Default current LPJ-GUESS v4.1:
- 15 soil layers
- 0.1 m each
- total represented depth 1.5 m

LPJ-GUESS-RE permits variable layer thickness and soil depth.

# 원 논문의 구현 범위
This paper provides the current model architecture for distributing root biomass/access among soil layers.

# 고운사에 직접 사용할 수 있는 부분
Prefer the actual LPJ-GUESS layer fractions `f_i` from the simulation/configuration rather than recalculating them externally.

Then:
```
C_root,i = C_root * f_i
```
provides the layer allocation for the root-C pool.

# 새로운 coupling이 필요한 부분
- conversion of root C to root length via SRL
- choosing which shallow layer depth is mechanically relevant to surface erosion
- connection of resulting RLD to SWEHR `J`

These are separate steps and must remain documented.

# 한계
- static prescribed root architecture in the standard model
- default root profile limited to 1.5 m
- bottom-layer remainder assignment can create unrealistically high bottom-layer fractions in shallow-soil configurations

# 최종 판정
- **채택: exact LPJ-GUESS vertical root-distribution source**

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-18-6623-2025
