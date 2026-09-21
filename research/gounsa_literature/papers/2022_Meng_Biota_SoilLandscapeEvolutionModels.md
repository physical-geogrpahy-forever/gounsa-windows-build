# 서지정보
Meng, X., Kooijman, A. M., Temme, A. J. A. M., & Cammeraat, E. L. H. (2022). The current and future role of biota in soil-landscape evolution models. *Earth-Science Reviews, 226*, 103945. DOI: 10.1016/j.earscirev.2022.103945.

# 이 논문을 찾은 이유
현재 존재하는 soil-landscape evolution model들이 식생, 토양생성, 풍화, 수문, 지형진화를 어느 정도 함께 표현하는지 체계적으로 확인하고, 고운사 modular coupling이 기존 모델 공백을 실제로 메우는 구조인지 검증하기 위해 검토했다.

# 연구 유형
- systematic/scoping review
- soil-landscape evolution model comparison

# 공간 구조
- 19 unique SLEMs 비교
- plot to hillslope to landscape-scale model structures

# 적용 환경
- broad soil-landscape modeling literature

# 핵심 과정
reviewed process categories include:
- weathering and soil production
- clay translocation
- underground water flow
- soil organic matter dynamics
- hillslope sediment transport
- overland-flow erosion/deposition
- particle-size selectivity
- vegetation interception/infiltration effects
- vegetation effects on sediment transport
- biotic soil mixing

# 식생 입력
논문은 개별 production model이 아니라 existing models에서 vegetation state가 얼마나 단순화되어 있는지를 비교한다.

핵심 지적:
- vegetation traits/processes are often simplified
- litter quantity/quality impacts are poorly represented
- biota-soil-landscape interactions are underrepresented

# 핵심 결과
19개 soil-landscape evolution models를 검토한 결과:
```
geomorphic process detail
>
biotic process detail
```
인 경우가 일반적이었다.

즉 현재 SLEM 문헌에는:
```
dynamic vegetation
+ soil production/weathering
+ hydrology
+ hillslope transport
+ topography evolution
```
을 충분히 mechanistic하게 통합한 single model이 사실상 부족하다.

논문은 biota를 더 정교하게 표현하려면:
- additional state variables
- vertical discretization
- explicit process coupling
이 필요하다고 제안한다.

# 고운사에 직접 사용할 수 있는 부분
현재 modular architecture의 타당성을 강하게 지지한다.

```
LPJ-GUESS
 -> dynamic vegetation/root/litter/hydrology states

weathering engine
 -> mineral reaction / soil production

Landlab/SWEHR
 -> topography / erosion / sediment redistribution
```

을 하나의 monolithic published model로 찾으려 하기보다, published process models를 명시적 NEW COUPLING으로 결합하는 방식이 문헌상 합리적이다.

# 현재 scope 제한
논문 내 tree uprooting, animal bioturbation, mycorrhiza 등 모든 biotic process를 고운사에 넣는다는 뜻은 아니다.

Current exclusions 유지:
- mycorrhiza
- tree throw/uprooting
- shallow landslide

# 새로운 coupling이 필요한 부분
고운사의 LPJ-GUESS-centered vegetation state를 weathering/transport/soil profile state와 연결하는 대부분의 interface는 여전히 new coupling이다.

# 한계
- review
- specific equations/coefficients source 아님
- postfire sandstone 산림에 특화되지 않음

# 최종 판정
- **핵심 채택: integrated biota-soil-landscape model gap의 authoritative review**
- 고운사 modular architecture의 구조적 정당화
- coefficient source 아님

# 참고 링크 / DOI
https://doi.org/10.1016/j.earscirev.2022.103945
