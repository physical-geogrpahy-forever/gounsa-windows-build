# 서지정보
Millares, A., Díez-Minguito, M., & Moñino, A. (2019). *Evaluating gullying effects on modeling erosive responses at basin scale*. Environmental Modelling & Software, 111, 61-71. DOI: 10.1016/j.envsoft.2018.09.018.

# 이 논문을 찾은 이유
산지에서 rill과 gully를 함께 계산하는 모델 후보로 검토.

# 연구 유형
- 수치모델

# 공간 구조
- 30 m DEM
- D8
- local 1D routing
- genuine 2D 아님

# 적용 환경
- steep semiarid mountain basin

# 핵심 과정
- raindrop erosion
- rill erosion
- gully erosion
- headcut migration

# 식생 입력
- vegetation cover
- plant residue fraction
- root biomass 직접입력 없음

# 핵심 식
rill density가 flow, soil moisture, slope, plant residue, roughness의 함수로 변한다.

# 파라미터와 단위
Ki, Kr, critical shear stress, residue fraction, roughness.

# 원 논문의 구현 범위
산지 basin event에서 rill/gully processes를 계산.

# 고운사에 직접 사용할 수 있는 부분
산지 rill/gully modeling 선례.

# 새로운 coupling이 필요한 부분
LPJ-GUESS biomass 연결은 새로운 coupling.

# 한계
genuine 2D가 아니고 식생량 직접입력 조건도 충족하지 않는다.

# 최종 판정
- 탈락: 최종 erosion engine
- 보조근거: mountain application

# 참고 링크 / DOI
10.1016/j.envsoft.2018.09.018
