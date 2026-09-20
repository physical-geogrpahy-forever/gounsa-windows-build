# 서지정보
Greenwood, P., Bauer, J., & Kuhn, N. J. (2021). *Assessing hillslope sediment generation potential by tree throw: A preliminary field study along a small river valley in the Jura Mountains, northwest Switzerland*. Geographica Helvetica, 76, 319-333. DOI: 10.5194/gh-76-319-2021.

# 이 논문을 찾은 이유
tree throw event에서 root-plate geometry를 실제 downslope sediment travel distance와 fine-sediment volume으로 바꾸는 계산식을 확보하기 위해 재검토했다.

# 연구 유형
- field mapping
- event-volume estimation
- geometry-based sediment-transport calculation

# 적용 환경
- forested hillslopes
- Jura Mountains, Switzerland

# 핵심 과정
- tree uprooting
- root-plate volume
- fine sediment fraction
- sediment transport distance

# root-plate volume
Root-plate volume is estimated with a half-ellipsoid geometry following earlier tree-throw studies.

The field root plate includes:
- soil
- roots
- coarse fragments
- pore space

The paper conservatively assumes a fine-sediment fraction:

```
V_s
=
0.25 V_RP
```

where:
- `V_s`: detached fine-sediment volume
- `V_RP`: total root-plate volume

The value 0.25 is study-specific and not universal.

# downslope travel distance
The study uses the geometric tree-throw transport relation from the Gabet et al. lineage:

```
X_d
=
(W/2)(cos theta + sin theta)
+
(D/2)(sin theta - cos theta)
```

where:
- `X_d`: downslope sediment transport distance [m]
- `W`: root-plate width [m]
- `D`: root-plate depth [m]
- `theta`: hillslope angle

This supplies an explicit:
```
root-plate geometry + slope
 -> downslope displacement
```
bridge.

# 고운사에 직접 사용할 수 있는 부분
A practical event calculation can use:

```
V_RP(DBH)
 -> W,D geometry
 -> X_d(theta)
 -> displaced sediment volume x travel distance
```

This complements:
- Gallaway 2009 for DBH -> root-plate volume
- Doane 2021 for annual stochastic event population
- Constantine 2012 for storm/stand dynamics

# limitations
- preliminary study
- fine-sediment fraction 25% is local assumption
- total root plate contains coarse fragments and roots
- geometry can vary strongly with tree species, soil depth and substrate

# new coupling
Using Gallaway DBH-volume and Greenwood travel-distance geometry together with LPJ-GUESS is a new coupling.

# final judgment
**채택 보조근거: event travel-distance and fine-sediment geometry.**

# 참고 링크 / DOI
https://doi.org/10.5194/gh-76-319-2021
