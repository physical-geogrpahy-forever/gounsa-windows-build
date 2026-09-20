# 서지정보
Constantine, J. A., Schelhaas, M.-J., Gabet, E. J., & Mudd, S. M. (2012). *Limits of windthrow-driven hillslope sediment flux due to varying storm frequency and intensity*. Geomorphology, 175-176, 66-73. DOI: 10.1016/j.geomorph.2012.06.022.

# 이 논문을 찾은 이유
LPJ-GUESS woody cohort size distribution과 기후/폭풍 forcing을 tree-throw sediment flux로 연결하는 published dynamic-forest precedent를 확인하기 위해 재검토했다.

# 연구 유형
- numerical forest-gap model
- stochastic windthrow
- geomorphic sediment-flux model

# 공간 구조
- ForGEM forest-gap population dynamics
- hillslope sediment flux represented from tree-throw events

# 적용 환경
- Douglas-fir forest
- storm-driven windthrow

# 핵심 과정
- tree growth and size distribution
- wind loading
- uprooting/toppling
- root-plate volume
- sediment transport
- stand-structure feedback

# vegetation input
The model dynamically represents:
- tree population
- size distribution
- forest succession/growth state

Larger trees experience greater wind loading and are preferentially toppled as storm intensity increases.

# key coupling
The model connects:

```
forest size distribution
+ wind regime
 -> windthrow probability
 -> root plate volume
 -> sediment flux
```

Root-plate volume is treated as proportional to trunk diameter in the paper's transport formulation.

Therefore larger trees transport more sediment per event.

# nonlinear stand feedback
The response is not monotonic.

As wind severity rises:
- windthrow frequency increases
- large trees are preferentially removed
- the remaining forest becomes younger/smaller
- event volume eventually declines

The modeled sediment transport peaks at an average windthrow rate of about:

```
8 trees ha^-1 yr^-1
```

and decreases under still more severe disturbance because large-tree supply is depleted.

This is a key reason not to model tree throw as:

```
tree biomass x constant coefficient
```

# 고운사에 직접 사용할 수 있는 부분
Strong structural precedent for using LPJ-GUESS cohort outputs directly:

```
LPJ-GUESS DBH distribution
+ cohort density
+ mortality/disturbance
+ optional wind forcing
 -> event-scale windthrow
```

The vegetation dynamics should remain upstream of tree throw, rather than compressing everything into an effective diffusivity.

# relation to Gallaway 2009
Gallaway provides a direct field regression:

```
DBH -> V_RP
```

Constantine provides the stronger:
```
dynamic forest structure + storm regime -> windthrow
```
architecture.

Together they form a good published basis for the Gounsa tree-throw coupling.

# 새로운 coupling
LPJ-GUESS is not ForGEM.

Replacing ForGEM state with LPJ-GUESS cohort outputs is a new coupling.

If Gounsa does not explicitly model wind speed/gusts, a separate stochastic uprooting probability must be calibrated rather than claimed as a Constantine implementation.

# limitations
- Douglas-fir calibration
- storm/windthrow focus
- not wildfire-specific postfire dead-standing tree decay
- exact transport coefficients and root-plate scaling are site/model specific

# final judgment
**핵심 채택: dynamic woody cohort + storm -> windthrow architecture.**

Use Gallaway 2009 for the more direct postfire DBH/root-plate/delayed-toppling bridge.

# 참고 링크 / DOI
https://doi.org/10.1016/j.geomorph.2012.06.022
