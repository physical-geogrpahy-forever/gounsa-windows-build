# 서지정보
Léonard, J., & Richard, G. (2004). *Estimation of runoff critical shear stress for soil erosion from soil shear strength*. CATENA, 57(3), 233-249. DOI: 10.1016/j.catena.2003.11.007.

# 이 논문을 찾은 이유
De Baets 계열의 root-enhanced erosion-specific cohesion/soil strength를 Hairsine-Rose/SWEHR의 flow-erosion threshold 쪽으로 연결할 수 있는 published intermediate relationship이 있는지 확인하기 위해 검토했다.

# 연구 유형
- synthesis / reanalysis of experimental datasets
- soil mechanical strength -> hydraulic erosion threshold study

# 공간 구조
- multiple experimental datasets
- full distributed erosion model 아님

# 적용 환경
- cohesive/agricultural soils across prior experiments
- natural rough soil surfaces are explicitly discussed as a limitation

# 핵심 과정
- saturated soil shear strength
- critical runoff shear stress
- grain shear stress versus total hydraulic shear stress
- initiation of soil detachment

# 식생 입력
Direct vegetation input 없음.

However, roots are explicitly recognised as one of the factors contributing to aggregate/soil mechanical resistance, so this paper can function as the **strength-to-hydraulic-threshold** half of a root coupling.

# 핵심 식 / 관계
The central result is:

```
saturated soil shear strength ↑
 -> critical grain shear stress for runoff detachment ↑
```

The paper's major qualification is essential:
- total hydraulic shear stress is a poor predictor on rough soils
- the significant relationship appears when **grain shear stress** is distinguished from total shear stress

Subsequent process-model implementation by Waldmann (2010) cites Léonard & Richard for a conversion of the form:
```
tau_c = beta * sigma_s
```
with `beta = 2.6e-4`.

That numerical coefficient is therefore documented here as a **published-lineage implementation value**, but it must be checked against the original regression/domain before any Gounsa coding.

# 파라미터와 단위
- `sigma_s`: saturated soil shear strength
- `tau_c`: critical grain shear stress for runoff detachment
- roughness partition between grain shear and total shear is critical

# 원 논문의 구현 범위
The paper supports:
```
measurable soil mechanical strength
 -> critical hydraulic detachment threshold
```

It does not provide:
- root biomass/RLD dynamics
- stream-power threshold `Omega_c`
- Hairsine-Rose `J`
- a 2D solver

# 고운사에 직접 사용할 수 있는 부분
This provides a much stronger alternative bridge than inventing a universal cohesion-to-`J` equation:

```
RLD
 -> erosion-specific cohesion / soil strength
 -> tau_c
```

where the first step can be informed by De Baets and the second by Léonard & Richard.

# 새로운 coupling이 필요한 부분
Converting `tau_c` to SWEHR critical stream power `UC` is **not solved by this paper**.

Because stream power is:
```
Omega = tau * velocity
```
a critical stream-power threshold also requires a defensible critical velocity/hydraulic state.

Therefore:
```
RLD -> tau_c
```
has a published pathway,
but:
```
RLD -> SWEHR UC
```
remains unresolved without another validated bridge or calibration.

# 한계
- grain shear versus total shear distinction is difficult on rough natural surfaces
- root-reinforced forest soil was not the direct experimental target
- a universal coefficient should not be assumed across rough postfire forest soils

# 최종 판정
- **채택: soil-strength -> critical-shear bridge**
- does not solve cohesion -> J
- does not by itself solve tau_c -> SWEHR UC
- highly relevant if a tau_c-native erosion closure is selected

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2003.11.007
