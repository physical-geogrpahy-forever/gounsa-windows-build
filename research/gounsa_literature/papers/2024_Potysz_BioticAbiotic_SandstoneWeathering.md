# 서지정보
Potysz, A., & Bartz, W. (2024). Long-term (bio)deterioration of Fe-containing and Fe-depleted sandstones: An experimental insight into biotic and abiotic interactions. *Construction and Building Materials, 421*, 135700. DOI: 10.1016/j.conbuildmat.2024.135700.

# 이 논문을 찾은 이유
고운사 parent material이 sandstone이므로, root exudate-like organic conditions가 sandstone cement와 matrix dissolution에 실제로 미치는 영향을 직접 실험한 최신 자료를 찾기 위해 검토했다.

# 연구 유형
- long-term laboratory weathering experiment
- biotic / abiotic comparison

# 공간 구조
- sandstone cubes / grains
- batch leaching weathering system

# 적용 환경
- Fe-containing sandstone
- Fe-depleted sandstone
- simulated rhizospheric conditions

# 핵심 과정
- artificial root exudate weathering
- bacterial / siderophore effect
- cement dissolution
- Fe oxide dissolution
- elemental release
- sandstone deterioration

# 식생 입력
실제 vegetation model은 없음.

rhizosphere proxy:
- artificial root exudate solution
- organic-rich conditions
- bacterial/siderophore treatment

# 핵심 식
수치 weathering equation이 아니라 experimental comparison이다.

Artificial root exudate solution에는:
- glucose
- fructose
- sucrose
- citric acid
- lactic acid
- succinic acid
등이 포함되어 rhizospheric organic conditions를 모사한다.

핵심 결과:
- organic-rich conditions가 inorganic acidic water보다 sandstone weathering을 더 크게 유도
- sandstone cement가 특히 dissolution에 취약
- Fe-rich sandstone에서 biodeterioration susceptibility가 더 큼
- goethite가 hematite보다 dissolution에 더 민감

# 파라미터와 단위
- pH treatments
- artificial-root-exudate composition
- sandstone Fe/cement state
- element release
- mineralogical changes

# 원 논문의 구현 범위
sandstone의 mineral/cement composition에 따라 biotic chemical weathering susceptibility가 어떻게 달라지는지 실험적으로 평가한다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요한 sandstone-specific constraint.

```
vegetation chemistry effect
x
sandstone cement/mineralogy
```
interaction이 커질 수 있음을 보여준다.

따라서 고운사 petrography에서:
- cement type
- Fe oxide cement
- matrix abundance
를 확인하는 것이 vegetation-weathering parameterization에도 필수다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root/litter chemistry를 artificial exudate concentration에 대응시키는 것은 새 coupling이며 직접 coefficient transfer는 금지한다.

# 한계
- dimension-stone laboratory system
- natural forest hydrology/root architecture 없음
- annual field weathering rate로 직접 변환 불가

# 최종 판정
- **채택: sandstone-specific biogeochemical-weathering constraint**
- final Gounsa sandstone petrography 조사 우선순위를 강화함

# 참고 링크 / DOI
https://doi.org/10.1016/j.conbuildmat.2024.135700
