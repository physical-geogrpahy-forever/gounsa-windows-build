# 서지정보
Turkington, A., & Shouse, M. (2019). The impact of large Trees on bedrock denudation on forested hillslopes in the southern United States. Chikei/Transactions, Japanese Geomorphological Union, 40(3), 259-278.
DOI: 확인된 공개 서지페이지에서 DOI를 확인하지 못함.

# 이 논문을 찾은 이유
사암 산림사면에서 큰 나무가 soil protection만 하는 것이 아니라 exposed bedrock와 subsoil bedrock을 실제로 biomechanically weathering하는지 확인하기 위해 검토했다.

# 연구 유형
- 현장 관찰 + 기존 연구 종합
- forested hillslope bedrock denudation study

# 공간 구조
- 미국 남부 산림사면
- exposed siliceous sandstone surface와 tree microsite
- hillslope topography와 soil-depth observation을 함께 사용

# 적용 환경
- forested hillslope
- siliceous sandstone

# 핵심 과정
- root-groove development
- joints and bedding planes opening
- root-hair / microorganism infill pathway
- subsoil bedrock biomechanical weathering
- local soil deepening
- surface bioprotection과 bedrock bioerosion의 동시 가능성

# 식생 입력
- large trees와 root systems
- 정량 biomass / RLD 입력은 없음

# 핵심 식
직접적인 process-rate equation은 없다.
이 논문은 geomorphic field evidence를 제공한다.

# 파라미터와 단위
- soil depth: 길이
- root groove와 joint opening은 형태적 증거
- transferable weathering coefficient는 제시하지 않음

# 원 논문의 구현 범위
- exposed siliceous sandstone에서 roots가 groove를 발달시키고 joints/bedding planes를 열어 bedrock denudation을 촉진할 수 있음을 보고
- dead-tree 주변 soil-depth 자료는 trees가 이 환경에서 soil을 국소적으로 더 깊게 만들 수 있음을 지지
- hillslope topographic variables만으로 soil thickness를 잘 설명하지 못했다고 보고

# 고운사에 직접 사용할 수 있는 부분
1. forest vegetation의 효과는 한 방향이 아니다.
2. surface에서는 binding/cover를 통해 erosion을 억제할 수 있지만, shallow exposed sandstone에서는 root-rock contact가 substrate production을 촉진할 수 있다.
3. 따라서 `vegetation factor` 하나로 erosion reduction과 weathering/soil production enhancement를 동시에 처리하면 안 된다.

# 새로운 coupling이 필요한 부분
`root-rock contact + fracture accessibility -> biomechanical production` 경로는 고운사에서 별도 NEW COUPLING으로만 둘 수 있다.
LPJ-GUESS biomass를 직접 bedrock-denudation coefficient로 곱하는 방식은 근거가 없다.

# 한계
- 정량적인 연간 weathering/soil-production rate가 없다.
- 일부 근거는 dead/uplifted tree legacy와 관련되며 현재 production에서 tree throw는 제외되어 있다.
- southern US siliceous sandstone과 고운사 사암의 cement/mineralogy 차이를 고려해야 한다.

# 최종 판정
- 보조근거
- 역할: sandstone에서 tree bioprotection과 bedrock bioerosion을 분리해야 한다는 field evidence

# 참고 링크 / DOI
- University of Kentucky research record: The impact of large Trees on bedrock denudation on forested hillslopes in the southern United States
- ISSN 0389-1755