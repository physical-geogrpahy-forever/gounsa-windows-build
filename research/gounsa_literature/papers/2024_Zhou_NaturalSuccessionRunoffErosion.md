# 서지정보
Zhou, S., Li, P., Zhang, X., Wang, Y., Yu, K., Shi, P., Xiao, L., Wang, T., & Chang, E. (2024). Runoff and erosion reduction benefits of vegetation during natural succession on fallow grassland slopes. Science of the Total Environment, 954, 176211. https://doi.org/10.1016/j.scitotenv.2024.176211

# 이 논문을 찾은 이유
천이단계별로 aboveground와 belowground 식생효과를 분리하여 runoff와 sediment 감소에 어떻게 기여하는지 확인하기 위해 검토했다.

# 연구 유형
- 현장 유수실험
- 구조방정식 분석

# 공간 구조
- hillslope plot
- 4개 natural succession stage

# 적용 환경
- 휴경지 자연천이 사면

# 핵심 과정
- runoff regulation
- sediment production
- soil-structure stabilization

# 식생 입력
- aboveground biomass
- stem count
- humus mass
- root volume density
- root surface area density
- root mass density

# 핵심 식
현재 채팅에서 복구된 PLS-PM 효과:
aboveground indirect effect on sediment production = -0.364
belowground indirect effect = -0.439
runoff -> erosion = +0.330
soil structure -> erosion = -0.616

# 파라미터와 단위
각 biomass/root trait 단위와 PLS-PM 세부계수는 원문 재검증 필요.

# 원 논문의 구현 범위
천이에 따라 지상부와 지하부의 erosion-control 경로가 달라지고, 효과가 단조적으로 증가하지 않음을 보인다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS의 aboveground biomass와 root traits를 서로 다른 물리경로로 연결해야 한다는 최신 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS cohort/PFT별 biomass를 runoff resistance와 erodibility로 직접 변환하는 것은 새로운 coupling이다.

# 한계
수치 지형모델이 아니라 현장실험 및 통계 인과모형이다.

# 최종 판정
- 보조근거
- 천이 의존적 기관별 coupling의 핵심 근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.scitotenv.2024.176211
