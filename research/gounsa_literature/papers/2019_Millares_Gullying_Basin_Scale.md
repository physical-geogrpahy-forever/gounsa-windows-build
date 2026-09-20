# 서지정보
Millares, A., Díez-Minguito, M., & Moñino, A. (2019). *Evaluating gullying effects on modeling erosive responses at basin scale*. Environmental Modelling & Software, 111, 61-71. DOI: 10.1016/j.envsoft.2018.09.018.

# 이 논문을 찾은 이유
basin scale에서 raindrop, rill, gully, headcut을 함께 계산하고 산지 적용 가능한 distributed model을 찾기 위해 검토했다.

# 연구 유형
- distributed hydrological/erosion model

# 공간 구조
- 30 m DEM
- local 1D routing + D8
- genuine 2D surface flow 아님

# 적용 환경
- basin scale
- mountain/semi-arid application lineage

# 핵심 과정
- raindrop erosion
- rill erosion
- gully erosion
- headcut migration

# 식생 입력
- plant residue fraction
- vegetation/ground cover 중심
- root biomass 직접입력 없음

# 핵심 식
rill density는 flow, soil moisture, slope, plant residue fraction, random roughness의 함수로 계산된다.

# 파라미터와 단위
정확한 식과 단위는 원문 표/식 기준.

# 원 논문의 구현 범위
basin-scale distributed rill/gully/headcut simulation.

# 고운사에 직접 사용할 수 있는 부분
산악 유역에서 rill/gully dynamics를 분포형으로 다루는 구조적 선례.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root biomass를 erodibility에 연결하려면 **새로운 coupling**.

# 한계
- D8/local 1D
- vegetation residue/cover 중심
- strict 2D + quantitative vegetation 조건 미충족

# 최종 판정
**보조근거.** strict 최종 유수침식 엔진에서는 탈락에 가까움.

# 참고 링크 / DOI
10.1016/j.envsoft.2018.09.018
