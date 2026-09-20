# 서지정보
Zhang, L., Li, Y., Wu, B., & Qi, S. (2026). How does the roots architecture affect the runoff-infiltration-erosion processes under varying rainfall events? *Journal of Hydrology, 677*, 135802.

# 이 논문을 찾은 이유
root architecture가 runoff와 infiltration을 통해 간접적으로 erosion을 바꾸는 경로를 확인하기 위해 검토했다.

# 연구 유형
- 실험 + pore-network modeling

# 공간 구조
- root-pore network / plot

# 적용 환경
- bamboo stands / 강우실험

# 핵심 과정
- infiltration
- runoff
- erosion
- pore connectivity

# 식생 입력
- root architecture
- pore-network changes

# 핵심 식
`RootArchitecture -> PoreNetwork -> Infiltration/Runoff -> Erosion` 경로로 정리됨.

# 파라미터와 단위
pore throat radius, connected porosity, throat length 등.

# 원 논문의 구현 범위
CT와 pore-network modelling을 통해 root architecture가 수문-침식을 바꾸는 과정을 분석.

# 고운사에 직접 사용할 수 있는 부분
root effect를 erodibility 한 경로만이 아니라 hydrology 경로와 분리할 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root architecture와 고운사 infiltration/runoff 모듈 연결은 새로운 coupling.

# 한계
대나무 기반 사례이며 산림 PFT 전체로 일반화 필요.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.jhydrol.2026.135802
