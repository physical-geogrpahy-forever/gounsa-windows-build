# 서지정보
Welivitiya, W. D. D. P., Willgoose, G. R., Hancock, G. R., & Senanayake, I. P. (2025). Modelling hillslope soil profiles using a coupled pedogenesis and landform evolution model. *Soil Advances, 4*, 100074. DOI: 10.1016/j.soilad.2025.100074.

# 이 논문을 찾은 이유
기존 SSSPAM 계보가 2025년에 hillslope soil-profile evolution과 multiple weathering functions까지 확장되었는지 확인하고, 고운사 Mode A/B 및 soil-profile bookkeeping 비교대상으로 검토했다.

# 연구 유형
- coupled pedogenesis-landform numerical model
- SSSPAM application

# 공간 구조
- hillslope
- multilayer soil profile
- evolving landform
- spatially distributed soil properties

# 적용 환경
- generic / reconstructed hillslope soilscape
- landscape restoration-oriented modeling

# 핵심 과정
- soil production/weathering
- pedogenesis
- fluvial erosion
- diffusive erosion
- deposition
- soil armouring
- particle-size profile evolution
- landform evolution

# 식생 입력
explicit dynamic vegetation model은 없다.

따라서 식생-풍화 model source가 아니라:
- soil-profile/weathering law comparison
- landform feedback
용 benchmark다.

# 핵심 weathering functions
논문은 네 가지 depth-dependent weathering/pedogenesis function을 비교한다.

- exponential
- humped exponential
- static reversed exponential
- dynamic reversed exponential

# 핵심 결과
weathering/pedogenesis function 선택 자체가:
- hillslope evolution stage
- soil-profile structure
- internal feedback
를 크게 변화시켰다.

즉:
```
choice of P(H)
 -> soil profile
 -> erosion/deposition
 -> landform
```
feedback이 강하다.

# 고운사에 직접 사용할 수 있는 부분
현재:
```
Mode A exponential
Mode B humped
```
를 mandatory sensitivity로 유지하는 근거를 최신 SSSPAM 계보가 강화한다.

또:
- multilayer PSD
- armouring
- weathering
- erosion/deposition
의 coevolution은 coarse-fragment module 비교에 유용하다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation/root states를 SSSPAM weathering parameter에 넣으면 new coupling이다.

# 한계
- vegetation dynamics 없음
- forest root/weathering feedback 없음
- chemical reaction network가 WITCH/BioRT/PFLOTRAN보다 단순
- engineered/post-mining application lineage가 강함

# 최종 판정
- **보조 채택: hillslope soil-profile / P(H) / armouring benchmark**
- vegetation-weathering production engine으로는 사용하지 않음
- Mode A/B와 coarse-fragment sensitivity 검증에 사용

# 참고 링크 / DOI
https://doi.org/10.1016/j.soilad.2025.100074
