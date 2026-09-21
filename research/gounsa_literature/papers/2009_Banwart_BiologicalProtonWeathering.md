# 서지정보
Banwart, S. A., Berg, A., & Beerling, D. J. (2009). Process-based modeling of silicate mineral weathering responses to increasing atmospheric CO2 and climate change. *Global Biogeochemical Cycles, 23*(4), GB4013. DOI: 10.1029/2008GB003243.

# 이 논문을 찾은 이유
식생 생산성과 유기탄소, 토양 CO2가 silicate weathering에 들어가는 과정을 단순 biomass multiplier가 아니라 mechanistic reaction model로 표현한 선례를 찾기 위해 검토했다.

# 연구 유형
- process-based 수치모델
- soil chemistry / weathering model

# 공간 구조
- 1D conceptual soil profile
- O/E, B, C에 대응하는 3개 well-mixed compartments

# 적용 환경
- northern European boreal coniferous forest soils
- Swedish catchments

# 핵심 과정
- biological productivity
- root/mycorrhizal respiration
- DOC production and decomposition
- soil CO2 and pH
- mineral dissolution kinetics
- hydrology and runoff
- alkalinity feedback

# 식생 입력
- biological productivity
- biomass decomposition
- root/mycorrhizal contribution to soil CO2
- DOC / organic acid related proton balance
- vegetation effects on reactive mineral surface conceptualized

# 핵심 식
이 모델은 다음을 하나의 soil reaction system으로 연결한다.

```
biological productivity
 -> soil CO2 + DOC
 -> proton balance / pH
 -> kinetic mineral dissolution
 -> alkalinity release
 -> pH feedback
 -> weathering flux
```

weathering flux는 base-cation export를 이용해 계산한다.

# 파라미터와 단위
- W: weathering flux [equivalents ha-1 yr-1]
- mineral dissolution activation energy
- runoff
- soil temperature
- DOC decomposition parameter
- soil depth, porosity, water content
- mineral reactive surface area

# 원 논문의 구현 범위
steady-state modern forest soil의 weathering process를 대상으로 하며, atmospheric CO2 증가에 따른 temperature, runoff, biological productivity 변화의 weathering feedback을 sensitivity analysis한다.

# 고운사에 직접 사용할 수 있는 부분
식생 영향이 단순한 biomass multiplier가 아니라:
- CO2
- DOC
- pH
- hydrology
- reactive surface
를 거쳐 weathering kinetics에 들어가야 한다는 process 근거.

이는 Hartmann-only forcing보다 생태 피드백이 풍부한 chemical-weathering formulation을 정당화한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS의 실제 root/litter pools를 이 모델의 productivity, respiration, DOC terms로 mapping하는 것은 새 coupling이다.

# 한계
- steady-state assumption
- fire, landslide 등 episodic disturbance 미포함
- sandstone-specific parameterization 아님
- explicit root architecture는 없음

# 최종 판정
- **채택: 식생-화학풍화 process mechanism의 핵심 근거**
- production 구현은 B-WITCH/REWTCrunch와 함께 비교하여 단순화 수준을 정한다.

# 참고 링크 / DOI
https://doi.org/10.1029/2008GB003243


## 2026-09-21 mycorrhiza scope override

고운사에서 이 논문을 사용할 때 균근-specific interpretation은 제외한다.

사용 가능한 비균근 process reference:
- biological productivity
- root respiration / soil CO2
- DOC production/decomposition
- proton balance / pH
- hydrology
- mineral dissolution kinetics

사용하지 않는 항:
- mycorrhizal state
- fungal functional type
- fungal weathering multiplier
