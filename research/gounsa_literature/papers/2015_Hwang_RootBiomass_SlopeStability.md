# 서지정보
Hwang, T., Band, L. E., Hales, T. C., Miniat, C. F., Vose, J. M., Bolstad, P. V., Miles, B., & Price, K. (2015). *Simulating vegetation controls on hurricane-induced shallow landslides with a distributed ecohydrological model*. Journal of Geophysical Research: Biogeosciences, 120(2), 361-378. DOI: 10.1002/2014JG002824.

# 이 논문을 찾은 이유
산림의 belowground biomass를 공간분포 root cohesion으로 변환해 distributed ecohydrological slope-stability model에 넣은 published bridge를 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 + 공간자료
- distributed ecohydrological model + planar/infinite-slope landslide model

# 공간 구조
- distributed hillslope/watershed
- spatially variable root cohesion
- transient hydrology / pore-pressure simulation

# 적용 환경
- 산림 산지
- southern Appalachian catchments
- hurricane-induced shallow landslides

# 핵심 과정
- belowground biomass estimation
- root cohesion
- transient soil moisture/pore pressure
- shallow landslide stability

# 식생 입력
- canopy height from lidar
- total belowground biomass
- root tissue density
- vertical root distribution
- root tensile strength / root area distribution

# 핵심 식
논문은 canopy height와 belowground biomass의 allometric relation, 토심별 root-area exponential distribution을 이용해 root cohesion을 공간분포화하고 slope-stability calculation에 넣는다.

대표 vertical root-area structure:
```
A(z) = A_0 exp(-b z)
```
형태의 two-parameter exponential model을 사용한다.

# 파라미터와 단위
- belowground biomass: g m^-2 또는 kg m^-2 계열
- root tissue density: kg m^-3
- root area: m2
- b: m^-1
- root cohesion: Pa 또는 kPa 계열

세부식과 모든 계수는 원문을 따른다.

# 원 논문의 구현 범위
lidar canopy information과 soil-pit root observations를 이용해 spatially distributed root cohesion을 만들고, distributed ecohydrological model의 hydrology와 결합하여 shallow-landslide occurrence를 예측한다.

# 고운사에 직접 사용할 수 있는 부분
- FineRootC/BGB -> root distribution -> root cohesion -> factor of safety의 published bridge
- spatially uniform root cohesion보다 spatially variable root cohesion이 산림 산지의 landslide prediction을 개선한다는 근거

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC/cohort outputs를 이 논문의 BGB, root-depth distribution, canopy-height allometry와 직접 연결하는 단계는 새로운 coupling이다.

# 한계
- DGVM과 직접 결합된 모델은 아님
- southern Appalachians의 allometry와 root traits를 고운사에 그대로 이식할 수 없음
- 유수침식 Ki/Kr용 root effect와 별개인 shallow-landslide mechanics 모듈이다

# 최종 판정
- 채택: slope-stability bridge
- Hales 2018과 함께 root-reinforcement 계보의 핵심 보조근거

# 참고 링크 / DOI
https://doi.org/10.1002/2014JG002824
