# 서지정보
Hale, S. E., Gardiner, B. A., Peace, A., Nicoll, B., Taylor, P., & Pizzirani, S. (2015). *Comparison and validation of three versions of a forest wind risk model*. Environmental Modelling & Software, 68, 27-41. DOI: 10.1016/j.envsoft.2015.01.016.

# 이 논문을 찾은 이유
LPJ-GUESS woody cohorts의 DBH/height/stand structure와 실제 windthrow probability를 연결할 때 arbitrary uprooting probability 대신 validated mechanistic wind-risk model을 사용할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- hybrid mechanistic wind-risk model
- model validation against observed storm damage
- ForestGALES lineage

# 모델 출력
ForestGALES는:
- critical wind speed for overturning
- critical wind speed for stem breakage
- local wind climate에 따른 damage risk/probability

를 계산한다.

# 핵심 입력
model lineage에서 중요한 입력:
- tree height
- DBH
- stand spacing/competition
- species mechanical properties
- crown/aerodynamic structure
- soil/rooting class or rooting depth
- wind climate/exposure

# 검증 결과
2012 Scottish storm damage를 이용해 세 ForestGALES version과 logistic model을 비교했다.

Increasing:
- tree height
- local wind speed

가 observed damage와 가장 강하게 연결됐다.

기계적 model들은 damaged/undamaged stand 구분에서 실용적 성능을 보였고, 일부 version은 forest-scale bias가 낮았다.

# ForestGALES 2.5 핵심 구조

Overturning critical wind speed is calculated by balancing wind-induced turning moment against tree anchorage resistance.

ForestGALES manual gives a critical-overturning form proportional to:

```
u_crit,over
~ sqrt(
  C_reg * SW
  /
  aerodynamic/turning-moment terms
)
```

where anchorage depends on soil/rooting resistance and tree/stand structure.

Critical wind speed is then combined with a wind-speed distribution to obtain annual exceedance probability and return period.

# 고운사에 직접 사용할 수 있는 부분
Live/surviving tree pathway:

```
LPJ-GUESS
 DBH
 height
 density/spacing
 PFT/species
      |
      v
ForestGALES/fgr
 critical wind speed
      |
local wind forcing/climate
      |
      v
windthrow probability
```

This is substantially more defensible than assigning a constant annual uprooting probability to all live trees.

# 새로운 coupling
- LPJ-GUESS PFT -> ForestGALES species mechanical parameters
- LPJ-GUESS root/soil state -> anchorage/rooting input
- local Korean wind climate -> ForestGALES wind forcing
are new couplings unless directly parameterized.

# 산불 고사목 한계
ForestGALES is not a postfire dead-standing-tree decay model.

Do not directly use live-tree anchorage after fire without modifying for:
- dead-root mechanical decay
- stem deterioration
- canopy loss
- altered wind loading

For dead-standing fire-killed trees Gallaway 2009 delayed-toppling lineage is preferable.

# 최종 판정
**채택: live-tree wind-driven uprooting probability engine candidate.**

Postfire dead-standing tree collapse remains a separate pathway.

# 참고 링크 / DOI
https://doi.org/10.1016/j.envsoft.2015.01.016
