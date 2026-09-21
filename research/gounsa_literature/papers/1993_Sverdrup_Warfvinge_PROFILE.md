# 서지정보
Sverdrup, H., & Warfvinge, P. (1993). Calculating field weathering rates using a mechanistic geochemical model PROFILE. *Applied Geochemistry, 8*(3), 273-283. DOI: 10.1016/0883-2927(93)90042-F.

# 이 논문을 찾은 이유
ForSAFE가 사용하는 mineral-weathering 핵심식이 어떤 변수에 반응하는지 확인하여 식생이 풍화에 들어갈 수 있는 통로를 분해하기 위해 검토했다.

# 연구 유형
- mechanistic geochemical numerical model

# 공간 구조
- layered soil profile
- 1D vertical chemistry

# 적용 환경
- field soil weathering
- 다양한 soil/mineral assemblage

# 핵심 과정
- mineral dissolution
- acid-base chemistry
- weathering release of base cations
- chemical inhibition

# 식생 입력
PROFILE 자체의 식생은 외부 forcing으로 주어진다.
직접 weathering reaction은 다음 환경변수에 반응한다.
- H+
- H2O
- CO2
- organic acids / DOC
- dissolved Al
- base cations

# 핵심 식
transition-state-theory 기반 mineral dissolution rate를 사용한다.
12개 주요 primary/secondary mineral group이 H+, H2O, CO2, organic acids와 별도 반응한다.

# 파라미터와 단위
- mineral-specific kinetic parameters
- exposed mineral surface area
- soil temperature
- soil moisture
- soil density
- H+, CO2, organic ligand concentrations
- product/inhibitor concentrations

# 원 논문의 구현 범위
field weathering rate를 soil samples에서 운영적으로 구할 수 있는 입력으로 계산하는 mechanistic model.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS로부터 식생이 바꾸는:
- soil moisture
- soil temperature
- CO2-related respiration state
- organic-matter / ligand proxy
를 weathering kinetics에 연결할 반응식 계보.

# 새로운 coupling이 필요한 부분
LPJ-GUESS litter/root carbon에서 DOC 또는 organic-ligand state를 산출하는 것은 별도 coupling이 필요하다.

# 한계
- 식생 동태 자체는 내장하지 않음
- bedrock-to-mobile-soil geomorphic production rate와 동일하지 않음

# 최종 판정
- 보조 채택
- ForSAFE chemical-weathering equation의 기반

# 참고 링크 / DOI
https://doi.org/10.1016/0883-2927(93)90042-F
