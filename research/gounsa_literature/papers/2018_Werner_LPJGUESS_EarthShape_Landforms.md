# 서지정보
Werner, C., Schmid, M., Ehlers, T. A., Fuentes-Espoz, J. P., Steinkamp, J., Forrest, M., Liakka, J., Maldonado, A., & Hickler, T. (2018). Effect of changing vegetation and precipitation on denudation – Part 1: Predicted vegetation composition and cover over the last 21 thousand years along the Coastal Cordillera of Chile. Earth Surface Dynamics, 6, 829–858. https://doi.org/10.5194/esurf-6-829-2018

# 이 논문을 찾은 이유
고운사에서 LPJ-GUESS를 실제 지형모델과 연결할 수 있는지, 특히 topography/soil depth를 식생모델에 되먹임하는 published precedent가 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 개발 및 지역 적용
- LPJ-GUESS subpixel landform extension
- 후속 Landlab landscape-evolution coupling을 위한 인터페이스 설계

# 공간 구조
- coarse LPJ-GUESS grid cell 내부를 DEM 기반 landform units로 세분
- landform은 elevation, slope position, aspect 등의 공통 특성을 갖는 patch group
- 고해상도 DEM은 약 30 m 자료를 사용하고, coupling 대상 Landlab은 약 100 m scale
- LPJ patch 자체는 여전히 통계적 replicate patch이며 literal x-y 위치를 갖지 않음

# 적용 환경
- Chile Coastal Cordillera
- arid shrubland, steppe, woodland, temperate forest 등 강한 기후 및 지형 구배
- LGM부터 present까지 21 kyr transient vegetation simulation

# 핵심 과정
- LPJ-GUESS cohort/gap vegetation dynamics
- light, water, nutrient, space competition
- establishment, mortality, fire
- PFT-specific interception/transpiration
- landform별 local climate modification
- landform별 soil-water storage modification

# 식생 입력/상태
- tree/shrub/grass PFT
- LAI
- FPC
- cohort biomass
- root distribution
- surface runoff

# 핵심 구현
EarthShape source audit에서 `Landform` 구조체에 다음이 확인됨.
- elevation
- aspect
- slope
- `soildepth`
- `soildepth_lower_mod`
- `has_deepwater`

2018 구현은 continuous dynamic soil-depth input을 직접 읽는 것이 아니라 slope-position class에 따라 lower-soil-layer depth modifier를 설정한다.

기본 two-layer soil:
- upper = 0.5 m
- lower = 1.0 m

예시 modifier:
- ridge 0.25 -> total effective depth 약 0.75 m
- upslope 0.33 -> 약 0.83 m
- midslope 0.5 -> 1.0 m
- flat 1.0 -> 1.5 m
- downslope 1.25 -> 1.75 m
- valley 1.5 -> 2.0 m

`sp_modifysoildepth`가 활성화되면 lower-layer AWC가 `soildepth_lower_mod`로 곱해지며, N leaching 계산에도 동일한 depth modifier가 사용된다.

# 원 논문의 구현 범위
논문 자체에서는 LPJ-GUESS vegetation simulation과 landform disaggregation을 구현했다.
완전한 LPJ-GUESS ↔ Landlab two-way coupling은 future work로 명시됐다.

논문이 명시한 향후 구조:
LPJ-GUESS -> vegetation cover + surface hydrology -> Landlab
Landlab -> updated topography + landform area + soil depth -> LPJ-GUESS

후속 공개 GitHub `toddehlers/lpj_landlab_coupling`에는 실제 two-way wrapper가 존재한다.

# 고운사에 직접 사용할 수 있는 부분
1. LPJ-GUESS를 terrain/landform 상태와 연결하는 동일 계열 published precedent
2. `Landform`을 LPJ-GUESS Stand와 연결하는 코드 구조
3. soil depth 변화가 AWC 및 plant water stress에 영향을 주는 최소 구현
4. LAI/FPC를 landscape evolution model로 넘기는 software architecture
5. elevation/slope/aspect/soil depth를 geomorph model에서 vegetation model로 전달하는 인터페이스 설계

# 새로운 coupling이 필요한 부분
고운사에서는 다음을 새로 구현해야 한다.
- Landlab/geomorph의 continuous dynamic soil depth를 실제 LPJ soil profile로 직접 반영
- erosion으로 제거된 soil layer와 함께 fine-root biomass를 실제로 제거
- surviving root profile 재분배
- deposition에 따른 burial 및 신규 rooting volume 처리
- water/C/N/root pool conservative remapping
- hourly/event geomorph -> daily vegetation synchronization
- vegetation effect를 FPC 하나가 아니라 root biomass, litter, live/dead roots 등 정량 상태로 전달

# 한계
- 2018 source에서 direct NetCDF `soildepth` loading은 주석 처리되어 있음
- 실제 active soil-depth effect는 slope-position class 기반 modifier
- root distribution은 soil-depth 변화에 따라 동적으로 절단되지 않고 PFT-prescribed root distribution을 사용
- full coupled Landlab experiment는 100-year timestep 장기 LEM용이어서 storm-scale 목적과 다름
- erosion engine 자체는 고운사의 최종 genuine-2D runoff erosion engine이 아님

# 최종 판정
**채택: LPJ-GUESS ↔ geomorph coupling architecture의 핵심 published precedent.**

단, 최종 고운사 vegetation engine이나 erosion equation으로 그대로 채택하는 것이 아니라, modern LPJ-GUESS SEC/PPA + external hydrology/geomorph coupling을 설계하는 근거로 사용한다.

# 참고 링크 / DOI
- https://doi.org/10.5194/esurf-6-829-2018
- https://github.com/toddehlers/lpj_guess_earthshape
- https://github.com/toddehlers/lpj_landlab_coupling
