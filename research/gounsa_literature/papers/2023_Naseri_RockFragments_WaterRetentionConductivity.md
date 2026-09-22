# 서지정보
Naseri, M., Joshi, D. C., Iden, S. C., & Durner, W. (2023). Rock fragments influence the water retention and hydraulic conductivity of soils. *Vadose Zone Journal, 22*, e20243. https://doi.org/10.1002/vzj2.20243

# 이 논문을 찾은 이유
GEM을 고운사 매립 석력 수문에 사용할 경우 conductivity뿐 아니라 soil-water retention까지 자의적 단순축소 없이 다룰 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- laboratory hydraulic-property measurement
- scaling-model evaluation

# 공간 구조
- soil core
- effective hydraulic properties

# 적용 환경
- stony sandy loam and silt loam
- rock fragments up to 50% v/v

# 핵심 과정
- water retention curve
- hydraulic conductivity curve
- rock-fragment water storage
- high stoniness

# 식생 입력
- 없음

# 핵심 식
water-retention mixing:
```
theta_mix(h) = (1-f) theta_soil(h) + f theta_rock(h)
```
(rock fragments의 water storage를 포함하는 경우)

impermeable/nonporous 단순화:
```
theta_mix(h) = (1-f) theta_soil(h)
```

hydraulic conductivity에서는 여러 scaling model을 비교했고 GEM 계열이 좋은 성능을 보였다.

# 파라미터와 단위
- f: volumetric RF content [-]
- theta_soil(h)
- theta_rock(h)
- K(h)
- fragment size 8-16 mm in experiment

# 원 논문의 구현 범위
최대 50% v/v rock fragments가 있는 토양에서 effective WRC와 HCC를 측정하고 기존 모델들을 평가한다.
RF 자체의 water storage를 무시하면 특히 high-stoniness에서 WRC 오차가 커짐을 보여준다.

# 고운사에 직접 사용할 수 있는 부분
- soil depth와 rock-fragment volume을 LPJ-GUESS soil water capacity로 연결할 때 단순 `(1-f)`만 쓰지 않을 근거
- sandstone spall/embedded fragment의 자체 water retention을 측정하거나 문헌값으로 입력할 수 있음
- soil moisture feedback을 자의적 water-storage factor 없이 구성할 수 있음

# 새로운 coupling이 필요한 부분
effective WRC/HCC를 LPJ-GUESS soil-water state 및 erosion hydrology에 전달하는 model interface는 새로운 coupling이다.

# 한계
- 실험 fragment size 범위가 고운사 전체 gravel-cobble range를 대표하지 않음
- erosion process 없음

# 최종 판정
- 핵심 채택 후보
- embedded rock-fragment soil-water property interface의 현대 근거

# 참고 링크 / DOI
https://doi.org/10.1002/vzj2.20243
