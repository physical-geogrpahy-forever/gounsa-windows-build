# Bart et al. (2020) — RHESSys fire-effects model

## 서지정보
Bart, R. R., Kennedy, M. C., Tague, C. L., & McKenzie, D. (2020). Integrating fire effects on vegetation carbon cycling within an ecohydrologic model. *Ecological Modelling*, 416, 108880.

## 이 논문을 검색한 이유
고운사의 postfire vegetation-water feedback과 매우 유사한 distributed ecohydrologic-fire model이 cohort succession까지 포함하는지 확인하기 위해 검토했다.

## 연구 유형
RHESSys + WMFire + fire-effects process coupling.

## 공간구조
- watershed
- spatial patch as finest horizontal unit
- multiple vertical canopy strata within patch

## 시간
RHESSys water/carbon/nutrient fluxes: daily.

## 핵심과정
- vegetation growth
- litter/CWD
- fire-associated mortality
- biomass consumption
- surface-fire effects
- canopy effects through ladder fuels
- postfire hydrologic and carbon feedback

## 하층식생
Understory vegetation and ladder fuels are explicit enough to affect fire severity.

## 고운사에 사용할 수 있는 부분
- fire severity -> litter/CWD/vegetation mortality -> ecohydrologic recovery architecture
- upper/lower vegetation layer representation
- mountain watershed spatial coupling reference

## 한계
The study does not provide an endogenous recruitment-based herb-shrub-tree demographic succession engine.
Canopy strata are state layers rather than self-created age/size cohorts.

## 최종 판정
**fire/ecohydrology coupling reference로 유지, primary vegetation engine에서는 제외.**
