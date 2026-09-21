# 서지정보
Yu, F., & Hunt, A. G. (2018). Predicting soil formation on the basis of transport-limited chemical weathering. *Geomorphology, 301*, 21-27. DOI: 10.1016/j.geomorph.2017.10.027.

# 이 논문을 찾은 이유
현재 고운사에서 분리한:
```
W_chem
!=
P_sand(H)
```
사이에 mechanistic bridge가 가능한지 확인하기 위해 검토했다.

# 연구 유형
- analytical / process-based soil-formation model
- percolation-theory weathering model

# 공간 구조
- point-based soil depth evolution
- landscape evolution model에 point-to-point로 삽입 가능하도록 설계

# 적용 환경
- Alpine soils
- alluvial fan / terrace soils
- general soil formation

# 핵심 과정
- transport-limited chemical weathering
- solute transport
- soil production
- erosion
- net soil formation

# 식생 입력
식생을 직접 동적으로 모의하지 않는다.

organism effect에서 직접 고려한 것은 주로:
- respiration-derived CO2

기타 biological effects는 범위 밖이다.

# 핵심 식
핵심 개념:

```
chemical weathering / solute transport
 -> gross soil production

gross soil production
 - erosion
 -> net soil formation
```

percolation theory를 이용해 non-Gaussian solute transport와 weathering-front advance를 연결한다.

논문 계보에서는 soil production rate가 time/depth에 따라 power-law로 감소하며 deep infiltration rate에 비례한다.

# 파라미터와 단위
- deep infiltration rate
- porosity
- characteristic particle/pore length scale
- soil depth
- erosion rate
- transport scaling parameters

# 원 논문의 구현 범위
chemical weathering을 soil depth production으로 연결하고 erosion을 빼서 net soil formation을 계산한다.

# 고운사에 직접 사용할 수 있는 부분
현재:
```
W_chem
```
을 단순 dissolved-loss term으로만 두고:
```
P_sand(H)
```
을 독립 empirical production law로 두는 구조의 대안이 될 수 있다.

즉 장기적으로:
```
reactive transport weathering
 -> reaction/front advance
 -> soil production
```
을 mechanistic하게 연결하는 bridge 후보.

# 새로운 coupling이 필요한 부분
LPJ-GUESS/B-WITCH chemistry와 이 percolation soil-production law를 직접 연결하는 것은 새 coupling이다.

# 한계
- transport-limited assumption이 강함
- sandstone-specific calibration 없음
- biological effects는 대부분 직접 포함하지 않음
- 현재 Evans/Heimsath sandstone field constraints보다 local lithology realism이 낮음

# 최종 판정
- **보조 채택: W_chem -> soil-production bridge 후보**
- 현재 P_sand Mode A/B를 즉시 대체하지 않음
- 향후 mechanistic front model sensitivity에 사용

# 참고 링크 / DOI
https://doi.org/10.1016/j.geomorph.2017.10.027
