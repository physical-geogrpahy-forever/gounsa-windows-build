# 서지정보
Anderson, R. S., Rajaram, H., & Anderson, S. P. (2018/2019). Climate driven coevolution of weathering profiles and hillslope topography generates dramatic differences in critical zone architecture. *Hydrological Processes, 33*(1), 4-19. DOI: 10.1002/hyp.13307.

# 이 논문을 찾은 이유
사면 topography, subsurface hydrologic flowpath, chemical weathering front, soil production과 transport를 한 수치모델에서 결합한 hillslope-weathering backbone을 확인하기 위해 검토했다.

# 연구 유형
- coupled numerical model
- reactive/hydrologic hillslope weathering
- landscape evolution

# 공간 구조
- 2D hillslope/interfluve geometry
- subsurface hydrologic flow paths
- water table
- weathering profile
- surface soil production and transport

# 적용 환경
- idealized hillslopes
- dry vs wet recharge end members
- climate-controlled Critical Zone architecture

# 핵심 과정
- water recharge
- subsurface lateral flow
- plagioclase-to-clay chemical weathering
- weathering-front advance
- soil production
- surface transport
- hillslope erosion/topographic evolution

# 식생 입력
explicit vegetation model은 없다.

따라서 식생은 직접 state가 아니고, 고운사에서는 LPJ-GUESS가 바꾸는:
- recharge
- ET
- soil moisture
- root-zone hydrology
를 통해 이 hydrologic-weathering skeleton에 들어가야 한다.

# 핵심 결과
dry and wet recharge cases에 동일한 geomorphic rules를 주어도 weathering profile이 크게 달라졌다.

Dry:
- incomplete weathering shallow
- surface-parallel weathering

Wet:
- intense weathering reaches depths near channel base
- substantial weathering below water table

핵심 nondimensional control:
```
weathering-front advance rate
/
landscape erosion rate
```
가 약 1 근처에서 system architecture가 급격히 전환될 수 있다.

# 핵심 구조

```
recharge
 -> subsurface flow paths
 -> mineral reaction
 -> weathering-front velocity
 -> regolith architecture
 -> soil production/transport
 -> topography
 -> flow paths
```

완전한 topography-weathering feedback이다.

# 파라미터와 단위
- recharge / water input rate
- weathering-front velocity [L T^-1]
- erosion rate [L T^-1]
- mineral conversion state
- hydraulic flow field

# 원 논문의 구현 범위
hydrology, weathering, geomorphic surface evolution을 결합하지만 dynamic vegetation은 없다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요한 numerical backbone.

고운사에서:
```
LPJ-GUESS vegetation
 -> recharge / ET / water distribution
 -> subsurface flow
 -> weathering front
 -> soil/regolith state
 -> topography
 -> LPJ-GUESS
```
를 만들 때 hydrology-weathering-geomorph core의 강한 선례가 된다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation/hydrology output을 이 모델의 recharge/flow forcing으로 연결하는 것은 새로운 coupling.

WITCH/BioRT chemistry와 Landlab topography를 이 구조로 결합하는 것도 새로운 coupling이다.

# 한계
- vegetation explicit 없음
- idealized hillslope
- specific sandstone chemistry 없음
- long-term climate/geomorph focus

# 최종 판정
- **채택: hillslope hydrology-weathering-topography coevolution 핵심 numerical precedent**
- vegetation effect는 LPJ-GUESS hydrologic pathway로 새로 연결
- direct vegetation multiplier 없음

# 참고 링크 / DOI
https://doi.org/10.1002/hyp.13307
