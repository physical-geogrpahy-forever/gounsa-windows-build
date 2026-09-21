# 서지정보
Hasenmueller, E. A., Gu, X., Weitzman, J. N., Adams, T. S., Stinchcomb, G. E., Eissenstat, D. M., Drohan, P. J., Brantley, S. L., & Kaye, J. P. (2017). Weathering of rock to regolith: The activity of deep roots in bedrock fractures. *Geoderma, 300*, 11-31. DOI: 10.1016/j.geoderma.2017.03.020.

# 이 논문을 찾은 이유
산림사면에서 tree roots가 실제 weathered bedrock fracture를 얼마나 사용하고, 그 분포가 hillslope position에 따라 달라지는지 확인하기 위해 검토했다.

# 연구 유형
- field root survey
- rock-fracture/root observations
- hillslope Critical Zone study

# 공간 구조
- ridge/upslope to toeslope
- soil
- weathered bedrock fractures
- hillslope groundwater gradient

# 적용 환경
- Susquehanna Shale Hills Critical Zone Observatory, Pennsylvania
- temperate forest
- shale-derived Critical Zone

# 핵심 과정
- deep rooting
- root growth in fractures
- water/nutrient access
- fracture exploitation
- hillslope-position control
- bedrock-to-regolith weathering environment

# 식생 입력
- fine/coarse root occurrence
- root density in fractures
- tree roots observed below soil

# 핵심 결과
Tree roots were observed in bedrock fractures below the soil profile.

중요하게 root density in fractures varied by hillslope position.

Toeslope locations had lower fracture-root density than upslope locations despite greater fracture abundance.

Interpretation:
```
shallower / more available water near toeslope
 -> less need for deep fracture-root investment

drier upslope
 -> stronger deep-root exploitation
```

즉:
```
hillslope position
 -> water availability
 -> root vertical deployment
 -> rock interaction
```
이 실제 존재한다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요하다.

LPJ-GUESS에서 root depth/distribution을:
```
fixed by PFT only
```
로 두기보다 hydrologic/topographic state와 연결할 필요성을 지지한다.

Chemical-weathering interface에서는:
```
root access depth
root fraction in weathered zone
```
를 hillslope-position-independent constant로 두지 않는 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root distribution을:
- soil moisture
- deep water availability
- local water table / rock moisture
에 따라 조정하는 것은 NEW COUPLING이다.

# 한계
- shale
- root presence/activity field study
- chemical-weathering rate를 직접 정량화하지 않음
- root fracture causality를 annual P_sand law로 변환할 수 없음

# 최종 판정
- **핵심 채택: hillslope-position-dependent deep-root activity**
- root distribution을 static PFT trait만으로 두지 않는 근거
- direct weathering coefficient source 아님

# 참고 링크 / DOI
https://doi.org/10.1016/j.geoderma.2017.03.020
