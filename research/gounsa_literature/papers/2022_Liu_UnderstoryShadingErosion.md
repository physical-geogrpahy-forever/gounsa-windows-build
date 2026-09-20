# 서지정보
Liu, Y.-F., Huang, Z., Meng, L.-C., Li, S.-Y., Wang, Y.-B., Liu, Y., López-Vicente, M., & Wu, G.-L. (2022). Understory shading exacerbated grassland soil erosion by changing community composition. *CATENA, 208*, 105771.

# 이 논문을 찾은 이유
상층 교목이 하층식생 조성을 바꾸면서 침식보호를 오히려 약화시킬 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- 장기 식생조작/침식 실험

# 공간 구조
- understory plots

# 적용 환경
- forest canopy 아래 grassland communities

# 핵심 과정
- runoff
- sediment yield
- understory composition change

# 식생 입력
- canopy shading
- herb species identity
- litter mass
- root quality

# 핵심 식
단일 모델식보다 `TreeCanopy -> Shade -> HerbPFTComposition -> HerbRootTraits -> Erodibility`의 인과경로가 핵심.

# 파라미터와 단위
종조성, litter, runoff/sediment. 세부값 원문 재검증 필요.

# 원 논문의 구현 범위
수관 아래 5년 식생변화와 침식반응을 비교.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS overstory/understory 경쟁을 지형모듈 직전까지 보존해야 한다는 강한 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS shade/competition 결과를 understory root-quality erosion response로 연결하면 새로운 coupling.

# 한계
수치 지형모델 아님.

# 최종 판정
- 핵심 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2021.105771
