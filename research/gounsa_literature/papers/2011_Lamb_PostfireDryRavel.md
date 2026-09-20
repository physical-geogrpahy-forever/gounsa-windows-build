# 서지정보
Lamb, M. P., Scheingross, J. S., Amidon, W. H., Swanson, E., & Limaye, A. (2011). A model for fire-induced sediment yield by dry ravel in steep landscapes. *Journal of Geophysical Research, 116*, F03006. https://doi.org/10.1029/2010JF001878

# 이 논문을 찾은 이유
산불 후 급경사면에서 vegetation destruction과 loose sediment release를 연결하는 실제 수치모델을 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- 현장관측 검증
- postfire sediment-storage model

# 공간 구조
- contributing hillslope area 기반 mass balance
- steep hillslope storage model

# 적용 환경
- 급경사 산지
- chaparral
- 산불 후
- San Gabriel Mountains

# 핵심 과정
- dry ravel
- vegetation sediment storage
- postfire sediment pulse
- soil production

# 식생 입력
- plant density
- sediment impoundment capacity per plant
- vegetation recovery timescale

# 핵심 식
저장용량:
`Vc = Vci * c * Ab`

여기서 Vci는 개별 식물의 sediment storage capacity, c는 plant density, Ab는 contributing hillslope area이다. 산불로 storage capacity가 급감하면 저장되던 sediment가 방출된다.

# 파라미터와 단위
- Vc: sediment volume
- Vci: sediment volume per plant
- c: plants m-2
- Ab: m2
- vegetation recovery timescale: time

# 원 논문의 구현 범위
angle of repose보다 가파른 사면에서 기존 dry-ravel transport law가 적용되기 어려운 문제를 storage-limited model로 처리한다.

# 고운사에 직접 사용할 수 있는 부분
- fire spall, loose gravel, detached mineral soil을 별도 loose-sediment pool로 두는 구조
- 산불 직후 저장능력 상실에 따른 sediment pulse 개념

# 새로운 coupling이 필요한 부분
LPJ-GUESS의 biomass/PFT에서 vegetation sediment-storage capacity를 계산하는 식은 원 논문에 없다. 고운사 적용 시 반드시 `새로운 coupling`으로 표시한다.

# 한계
- chaparral parameter를 고운사 산림에 그대로 사용할 수 없음
- 유수침식식이 아니라 dry-ravel storage model

# 최종 판정
- 채택
- 역할: postfire loose sediment/spall redistribution 구조

# 참고 링크 / DOI
https://doi.org/10.1029/2010JF001878
