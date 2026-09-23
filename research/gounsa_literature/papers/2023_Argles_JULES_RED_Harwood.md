# Argles et al. (2023) — JULES-RED Harwood Forest

## 서지정보
Argles, A. P. K., Robertson, E., Harper, A. B., et al. (2023). Modelling the impact of forest management and CO2-fertilisation on growth and demography in a Sitka spruce plantation. *Scientific Reports*, 13, 13487. https://doi.org/10.1038/s41598-023-39810-2

## 이 논문을 검색한 이유
RED가 이론적 demographic model에 그치지 않고 실제 JULES land-surface physics와 결합되어 온대 산림에서 mass-class demography, soil, subdaily carbon/water flux를 함께 계산하는지 확인하기 위해 검토했다.

## 연구 유형
- process-based land-surface + forest demography field application
- managed temperate conifer stand validation

## 공간구조
- Harwood Forest의 stand/site-scale JULES-RED
- RED mass classes로 tree size structure 표현
- 개별목 x-y 좌표는 추적하지 않음

## 적용환경
Harwood Forest, Northumberland, UK:
- Sitka spruce plantation
- 약 40 ha
- elevation 약 290 m
- slope 약 2 degrees
- peaty-gley soil
- half-hourly flux observations available

## 핵심과정
- JULES photosynthesis, respiration, energy and water balance
- RED mass-class tree demography
- canopy closure
- thinning/management
- CO2 fertilisation

## 식생입력
- Needle-leaved Evergreen Tree PFT
- initial plant number density / observed mass distribution
- RED demographic/allometric parameters
- CHESS-met or in-situ meteorological forcing
- HWSD-derived van Genuchten soil parameters

## 결과의 핵심
- tree number-density distribution across mass classes was simulated explicitly
- thinning reduced tree density and biomass while changing mean tree size/LAI
- modelled carbon fluxes were compared against half-hourly observations
- fitted-demography simulations stayed close to observed stand structure over the short evaluation period

## 고운사에 사용할 수 있는 부분
- RED가 실제 JULES 안에서 작동하는 implementation precedent
- temperate conifer forest에서 demographic mass classes + process-based water/carbon flux 결합
- 고운사 수목 cohort 부분을 개별목보다 가볍게 처리하는 참고
- restart/stand-state initialization concept

## 필요한 새로운 coupling
- natural mixed PFT postfire succession
- Korean tree/shrub/herb PFT calibration
- distributed fine hillslope grid
- geomorphic soil-depth state remapping

## 한계
- even-aged managed plantation
- single tree PFT 중심
- shrub/grass coexistence 및 herb-shrub-tree succession을 이 논문이 직접 검증하지 않음
- distributed catchment coupling 없음
- mortality/allometry calibration에 민감

## 최종 판정
**JULES-RED implementation viability의 강한 근거.**
다만 criterion 2의 하층식생과 천이는 Argles et al. (2020) RED mixed-PFT framework 및 별도 mixed-vegetation evidence와 함께 평가해야 한다.
