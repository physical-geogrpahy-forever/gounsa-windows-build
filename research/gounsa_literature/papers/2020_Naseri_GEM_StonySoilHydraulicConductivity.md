# 서지정보
Naseri, M., Peters, A., Durner, W., & Iden, S. C. (2020). Effective hydraulic conductivity of stony soils: General effective medium theory. *Advances in Water Resources, 146*, 103765. https://doi.org/10.1016/j.advwatres.2020.103765

# 이 논문을 찾은 이유
고운사처럼 매립 석력의 체적비가 높을 수 있는 산지토양에서 effective hydraulic conductivity를 자의적 보정계수 없이 계산할 modern physically based model을 찾기 위해 검토했다.

# 연구 유형
- physically based hydraulic model
- effective-medium theory

# 공간 구조
- effective soil hydraulic property model
- saturated/unsaturated conductivity

# 적용 환경
- stony soils
- high rock-fragment contents
- mountainous/forested applicability

# 핵심 과정
- effective hydraulic conductivity
- rock-fragment interaction
- shape/orientation effects
- permeable/impermeable fragments

# 식생 입력
- 없음

# 핵심 식
General Effective Medium(GEM) theory로 background soil과 rock fragments의 hydraulic conductivity를 혼합하여 effective conductivity를 계산한다.
모델은 volumetric RF content, RF hydraulic conductivity, shape/orientation parameter 및 matrix conductivity를 사용한다.
원문에는 Maxwell, Bruggeman-Symmetric 등 기존 scaling과 GEM을 비교한다.

# 파라미터와 단위
- f: volumetric rock-fragment fraction [-]
- matrix hydraulic conductivity
- rock-fragment hydraulic conductivity
- shape/orientation 관련 parameter
- matric potential

# 원 논문의 구현 범위
saturated 및 unsaturated hydraulic conductivity curve 전체를 계산할 수 있고, fragment 간 interaction을 허용하므로 high rock-fragment content에도 적용하도록 설계되었다.

# 고운사에 직접 사용할 수 있는 부분
- 매립 석력 비율이 높은 토양의 K(h)를 기존 published physics model로 산정
- `K_eff = K_fine * arbitrary factor` 같은 임의보정을 피할 수 있음
- sandstone fragment 자체가 완전 불투수인지 일부 투수인지도 모델에 넣을 수 있음

# 새로운 coupling이 필요한 부분
GEM K(h)를 Iber+/다른 erosion-hydrology engine의 hydraulic property로 입력하는 것은 model coupling이지만, 변수 자체는 동일한 물리량(hydraulic conductivity)이다.

# 한계
- runoff/erosion을 계산하지 않음
- water-retention curve는 별도 model이 필요

# 최종 판정
- 핵심 채택 후보
- high-stoniness embedded-fragment hydraulic conductivity의 우선 모델

# 참고 링크 / DOI
https://doi.org/10.1016/j.advwatres.2020.103765
