# SoilGen

## 모델 목적
Parent material과 time-dependent soil-forming factors를 바탕으로 soil profile의 장기 pedogenesis와 chemical weathering을 계산한다.

## 구조
- 1D pedon
- 대표 면적 약 1 m2
- vertical 5 cm compartments
- process별 dynamic time stepping

## 주요 과정
- Richards water flow
- heat flow
- gas diffusion
- solute advection/dispersion
- organic carbon cycling
- physical weathering
- chemical weathering
- clay migration
- bioturbation
- bulk-density/profile-property change

## García-Gamero et al. 2022 catena application
7개의 catena positions를 독립 pedon으로 20,000 yr 모의했다.

핵심 결과:
catena position / slope gradient 자체보다 soil moisture와 infiltration 같은 hydrological variables가 chemical depletion variability를 더 잘 설명했다.

## 고운사에서 유용한 점
- vertical soil development + hydrology + gas + solute + weathering의 통합 구조
- 단순 hillslope-position multiplier 대신 process hydrology를 써야 한다는 model evidence
- H_AB / altered-zone profile state 설계 참고

## 결정적 한계
- 1D independent pedons
- lateral water flux 없음
- 2D connected hillslope hydrology 없음
- dynamic forest succession 없음
- evolving terrain 없음

따라서 SoilGen을 고운사의 full hillslope weathering model이라고 부르지 않는다.

## 최종 판정
- 보조 채택
- 역할: vertical pedogenesis-weathering engine reference