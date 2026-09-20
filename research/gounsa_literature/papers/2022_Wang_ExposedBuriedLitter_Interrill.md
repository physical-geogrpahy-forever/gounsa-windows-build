# 서지정보
Wang, L., Zhang, G., & Wang, X. (2022). *Undecomposed litter mixed in the soil can increase interrill erosion on hillslopes: A laboratory study*. Soil and Tillage Research, 219, 105350. DOI: 10.1016/j.still.2022.105350.

# 이 논문을 찾은 이유
고운사 산불 후 litter를 하나의 단일 protective pool로 두어도 되는지, surface-exposed litter와 buried litter가 interrill erosion에 같은 방향으로 작용하는지 확인하기 위해 검토했다.

# 연구 유형
- laboratory rainfall-simulation experiment
- interrill erosion process study
- numerical erosion model 아님

# 공간 구조
- soil boxes
- 10-degree slope
- rainfall intensity 80 mm h^-1

# 적용 환경
- litter-soil mixed hillslope surface
- early undecomposed-litter stage

# 핵심 과정
- interrill erosion
- runoff velocity
- infiltration
- sediment yield
- surface-litter shielding
- buried-litter weakening

# 식생 입력
Four litter mass rates:
- 0
- 0.10
- 0.20
- 0.35 kg m^-2

Treatments:
- surface litter only
- buried litter only
- mixed with residual surface-exposed litter

# 핵심 식
This paper's key contribution is process separation rather than a universal model equation.

Results:
- surface-exposed litter decreased runoff velocity and sediment yield
- under comparable surface-cover conditions, surface litter reduced sediment yield by up to about 39%
- buried litter increased sediment yield by up to about 43% relative to bare soil
- mixed treatment at 0.35 kg m^-2 gave about 19% lower sediment yield than bare soil

# 파라미터와 단위
- litter mass rate: kg m^-2
- rainfall: mm h^-1
- sediment yield and runoff hydraulic metrics

# 원 논문의 구현 범위
Demonstrates that exposed and buried undecomposed litter can have **opposite effects** on erosion.

Buried litter can reduce infiltration / weaken resistance due to water repellency, pore disconnection, oversaturation, and deformation effects, whereas surface litter shields the soil.

# 고운사에 직접 사용할 수 있는 부분
A crucial state-variable decision:
```
SurfaceLitter != IncorporatedLitter
```

The two pools must not be collapsed into one universal erosion-reduction factor.

This is highly relevant immediately after fire and during subsequent mixing/decomposition.

# 새로운 coupling이 필요한 부분
LPJ-GUESS litter pools must be partitioned by position and incorporation/decomposition process. That partitioning is **새로운 coupling**.

# 한계
- laboratory study
- one rainfall intensity/slope setup
- no root dynamics
- not a full erosion model

# 최종 판정
- **채택: litter-state separation evidence**
- rules out a simple monotonic “more litter = less erosion” assumption
- does not by itself provide the final exposed-litter parameterization

# 참고 링크 / DOI
https://doi.org/10.1016/j.still.2022.105350
