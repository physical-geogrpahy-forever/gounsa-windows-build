# 서지정보
Zuo, H., Liu, Y., Li, G., Xu, Z., Zhao, L., Guo, Z., & Hu, Y. (2024). A revised model of global silicate weathering considering the influence of vegetation cover on erosion rate. Geoscientific Model Development, 17, 3949-3974. https://doi.org/10.5194/gmd-17-3949-2024

# 이 논문을 찾은 이유
식생이 weathering을 항상 증가시키는지, 아니면 erosion suppression을 통해 fresh mineral supply를 줄일 수도 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- global weathering model

# 공간 구조
- global grid

# 적용 환경
- 전지구

# 핵심 과정
- silicate weathering
- erosion supply limitation
- vegetation shielding

# 식생 입력
- LAI / vegetation cover

# 핵심 식
현재 채팅에서 확인한 핵심 구조는 vegetation -> erosion suppression -> fresh-mineral supply reduction -> weathering change 이다. 세부 수식은 원문 재검증 필요.

# 파라미터와 단위
LAI, erosion rate, weathering flux. 세부값 원문 재검증 필요.

# 원 논문의 구현 범위
식생이 weathering enhancement와 반대방향인 supply-limitation 효과도 만들 수 있음을 전지구 모델에서 다룬다.

# 고운사에 직접 사용할 수 있는 부분
식생효과를 단일 양의 weathering multiplier로 두지 않아야 한다는 경고 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS biomass/NPP와 fresh-mineral supply를 연결하는 것은 새로운 coupling이다.

# 한계
주 입력이 biomass가 아니라 LAI/cover 중심이며 고운사 주모듈 후보는 아니다.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-17-3949-2024
