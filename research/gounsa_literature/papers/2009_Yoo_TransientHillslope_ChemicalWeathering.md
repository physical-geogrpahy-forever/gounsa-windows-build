# 서지정보
Yoo, K., Mudd, S. M., Sanderman, J., Amundson, R., & Blum, A. (2009). Spatial patterns and controls of soil chemical weathering rates along a transient hillslope. *Earth and Planetary Science Letters, 288*(1-2), 184-193. DOI: 10.1016/j.epsl.2009.09.021.

# 이 논문을 찾은 이유
사면의 erosional/depositional 위치와 transient morphology가 soil chemical weathering의 공간분포를 어떻게 바꾸는지 확인하기 위해 검토했다.

# 연구 유형
- field geochemistry
- process-based hillslope mass-balance model

# 공간 구조
- grass-covered hillslope
- upper erosional section
- lower depositional section
- soil + saprolite

# 적용 환경
- coastal California
- transient hillslope following channel-incision history

# 핵심 과정
- soil production
- physical erosion/deposition
- soil chemical weathering
- sediment transport
- channel-incision transient
- mineral residence time

# 식생 입력
- grass-covered surface
- dynamic vegetation state 없음

따라서 식생 model source는 아니고 hillslope-position weathering mass-balance 근거다.

# 핵심 결과
upper eroding section:
```
soil production
=
physical erosion
+
chemical weathering
```
에 가까운 balance.

lower slope:
- channel incision history 변화로 depositional state
- soil accumulation
- different weathering/residence history

Weathering rates were among low values for actively eroding watersheds because:
- parent material had relatively little weatherable mineral
- primary minerals had coatings of secondary clay and Fe oxides

따라서:
```
same climate
!= same hillslope weathering rate
```
이며 mineral supply + transport history가 중요하다.

# 고운사에 직접 사용할 수 있는 부분
현재 Landlab/SWEHR sediment state를 chemical-weathering engine과 연결할 때:

```
erosional cell
depositional cell
upslope-derived soil
in-situ produced soil
```

을 구분할 필요가 있다는 강한 근거.

식생이 erosion/deposition을 바꾸면 다시 mineral residence and weathering을 바꾸는 feedback으로 이어진다.

# 새로운 coupling이 필요한 부분
SWEHR/Landlab의 annual net erosion/deposition와 particle provenance/age를 W_chem에 전달하는 것은 새로운 coupling.

# 한계
- grassland
- no dynamic vegetation
- coastal California parent material
- direct root/weathering relation 없음

# 최종 판정
- **채택: transient hillslope transport-weathering coupling 핵심 precedent**
- local H만으로 weathering을 결정하지 말아야 한다는 근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.epsl.2009.09.021
