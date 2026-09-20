# Pelletier et al. (2013)

# 서지정보
Pelletier, J. D., et al. (2013). Coevolution of nonlinear trends in vegetation, soils, and topography with elevation and slope aspect. *JGR Earth Surface, 118*, 741-758. https://doi.org/10.1002/jgrf.20046

# 이 논문을 찾은 이유
AGB를 유수침식, 사면수송, 풍화와 연결한 선례인지 확인.

# 연구 유형
- 수치모델 + 현장자료 보정

# 공간 구조
- landscape evolution framework
- 세부 routing은 원문 재검증 필요

# 적용 환경
- 미국 남서부 산지

# 핵심 과정
- slope-wash/fluvial erosion
- colluvial transport
- soil production/weathering

# 식생 입력
- AGB
- EEMT
- NPP, LAI, belowground biomass도 대안 가능하다고 논의

# 핵심 식
채팅에서 확인한 핵심은 AGB가 bioturbation형 사면수송을 증가시키고, 식생 증가는 slope-wash/fluvial erodibility를 낮춘다는 구조이다. 실제 fluvial 구현에서는 AGB 자체보다 EEMT를 대리변수로 쓴 부분이 있어 구분이 필요하다.

# 파라미터와 단위
- AGB, EEMT, soil depth, diffusivity, erodibility
- exact coefficients: 원문 재검증 필요

# 원 논문의 구현 범위
식생이 사면수송과 유수침식에 서로 다른 방향으로 작용.

# 고운사에 직접 사용할 수 있는 부분
식생량이 여러 지형과정에 동일 방향으로 작용하지 않는다는 구조적 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS PFT/cohort별 AGB를 목본/초본과 기관별로 분해하는 것은 새로운 coupling.

# 한계
목본/초본, 상층/하층을 명시적으로 구분하지 않음.

# 최종 판정
- 보조근거
- 최종 유수침식식 또는 사면확산식 단독 근거로는 사용하지 않음.

# 참고 링크 / DOI
- https://doi.org/10.1002/jgrf.20046

## 2026-09-21 현재 채팅 최종 보정
- **100년 고운사 사면확산 주식으로는 사용하지 않는다.** 이 논문의 AGB-biogenic transport 관계는 장기 지형-식생 공진화와 공간구배에 기반한 것으로, LPJ-GUESS의 연간 biomass 변화에 곧바로 적용하는 것은 시간척도 전이가 된다.
- 따라서 `AGB(t) -> Kd(t)`의 단기 동적식 근거로 사용하지 않는다.
- 역할은 장기적으로 biomass와 colluvial transport가 연결될 수 있고, 식생효과의 부호가 과정별로 달라질 수 있다는 **보조근거**로 제한한다.
