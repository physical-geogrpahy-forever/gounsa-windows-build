# 서지정보
Quijano-Baron, J., Saco, P. M., & Rodriguez, J. F. (2022). Modelling the effects of above and belowground biomass pools on erosion dynamics. *Catena, 213*, 106123.

# 이 논문을 찾은 이유
기관별 biomass pool을 SIBERIA 지형모듈에 결합한 직접 선례로 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- distributed landscape model, SIBERIA 결합

# 적용 환경
- 반건조 지형

# 핵심 과정
- 유수침식
- splash/creep 묶음 확산

# 식생 입력
- root, leaf, litter biomass의 정규화값
- wood는 생태모듈에는 있으나 직접 지형항 없음

# 핵심 식
기본식은 `q_s = beta q^m S^n`, `q_d = D S`. root biomass는 erodibility `beta`, leaf biomass는 `D`, litter는 Manning `n`을 수정한다.

# 파라미터와 단위
정규화 biomass와 경험계수. 정확한 계수는 원문 재확인 필요.

# 원 논문의 구현 범위
기관별 biomass pool을 지형과정에 연결하나 big-leaf 구조이며 understory/overstory를 분리하지 않는다.

# 고운사에 직접 사용할 수 있는 부분
기관별 biomass pool을 서로 다른 지형과정에 연결해야 한다는 구조적 비교대상.

# 새로운 coupling이 필요한 부분
LPJ-GUESS PFT/cohort 구조를 쓰려면 새로운 coupling 필요.

# 한계
현장 평균/표준편차 정규화, leaf가 splash와 creep을 함께 수정, overstory/understory 미분리.

# 최종 판정
- 탈락. COPLAS는 고운사 최종모델 근거에서 제외한다.

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2022.106123
