# 서지정보
Taylor, L. L., Banwart, S. A., Valdes, P. J., Leake, J. R., & Beerling, D. J. (2012). Evaluating the effects of terrestrial ecosystems, climate and carbon dioxide on weathering over geological time: A global-scale process-based approach. *Philosophical Transactions of the Royal Society B, 367*(1588), 565-582.

# 이 논문을 찾은 이유
DGVM NPP와 PFT를 process-based chemical weathering에 연결한 선례를 찾기 위해 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- 전지구 process-based weathering

# 적용 환경
- 전지구 / 지질시대

# 핵심 과정
- silicate chemical weathering

# 식생 입력
- DGVM NPP
- PFT
- nutrient demand
- mycorrhizal functional type

# 핵심 식
`DGVM -> NPP -> nutrient uptake -> soil chemistry -> mineral weathering` 구조.

# 파라미터와 단위
PFT/NPP와 weathering parameter. 세부식은 원문 재검증 필요.

# 원 논문의 구현 범위
식물기능형과 생산성이 광물풍화에 미치는 효과를 process-based하게 연결.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS PFT/NPP를 chemical-weathering submodule에 연결할 비교 선례.

# 새로운 coupling이 필요한 부분
weathering flux를 고운사 C/Cr 두께변화로 바꾸는 것은 새로운 coupling.

# 한계
전지구 지질시대 모델이며 soil-production thickness를 직접 출력하지 않는다.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1098/rstb.2011.0251
