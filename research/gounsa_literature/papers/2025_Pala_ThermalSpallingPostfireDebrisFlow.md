# 서지정보
Pala, C., Melis, M. T., Pioli, L., Sarro, R., Loddo, S., Cinus, S., et al. (2025). Sediment generation through thermal spalling during the 2021 Montiferru Planargia wildfire and its contribution to postfire debris flows. *Scientific Reports, 15*, 30918. https://doi.org/10.1038/s41598-025-15527-2

# 이 논문을 찾은 이유
고운사의 `fire -> spall -> coarse fragments -> postfire transport`를 직접 연결하고, 큰 암괴가 spalling으로 작아져 더 쉽게 이동한다는 가설을 검증하기 위해 찾았다.

# 연구 유형
- postfire field survey
- geomorphic mapping
- sediment connectivity/rockfall analysis

# 공간 구조
- burned hillslopes and channels
- sub-basin scale

# 적용 환경
- Mediterranean dense oak forest and shrubland
- rocky wildfire terrain

# 핵심 과정
- thermal spalling
- boulder fragmentation
- loose-sediment production
- sheet/rill/interrill remobilization
- channel blocking
- debris flow

# 식생 입력
- prefire land cover
- burn severity
- vegetation recovery는 postfire erosion decline의 배경요인

# 핵심 식
보편 spall-production equation은 제시하지 않는다.
핵심 관측:
- spall thickness approximately 3 mm to 13 cm
- 한 표본 deposit에서 pebble 74.8%, cobble 23.2%, gravel 2%
- 기존 boulder가 thermal spalling으로 작아지면 이후 이동에 필요한 shear stress가 감소한다고 명시
- sheet wash, rill-interrill flow가 spalls를 재이동시키며 pebble/gravel이 rill을 막기도 함

# 파라미터와 단위
- burn severity
- spalled surface percentage
- fragment size distribution
- rainfall events
- debris-flow occurrence

# 원 논문의 구현 범위
산불 자체가 exposed rock 및 pre-existing boulders를 파쇄하여 새로운 loose coarse sediment를 만들고, 후속 강우가 이를 재이동시키는 연쇄를 현장에서 보여준다.

# 고운사에 직접 사용할 수 있는 부분
- `fire spall -> fragment size reduction -> mobility threshold 감소`의 매우 직접적인 근거
- fire-spall을 단순 풍화가 아니라 synfire sediment-source pulse로 둘 근거
- coarse fragments가 rill을 막는 local storage/roughness effect도 함께 표현할 근거

# 새로운 coupling이 필요한 부분
고운사 사암의 burn severity/rock properties에서 spall mass와 size distribution을 계산하는 식은 여전히 **새로운 coupling 또는 추가 정량문헌이 필요**하다.
장기 postfire weathering에 의한 추가 fragmentation은 이 논문이 직접 다루지 않는다.

# 한계
화산암 중심 사례이며 debris-flow scale이 강하다. 고운사 사암 parameter를 직접 이식하지 않는다.

# 최종 판정
- 핵심 채택
- fire-spall supply 및 mobility 연결의 현재 가장 직접적인 현장근거

# 참고 링크 / DOI
https://doi.org/10.1038/s41598-025-15527-2
