# 서지정보
Gallaway, J. M., Martin, Y. E., & Johnson, E. A. (2009). *Sediment transport due to tree root throw: integrating tree population dynamics, wildfire and geomorphic response*. Earth Surface Processes and Landforms, 34, 1255-1269. DOI: 10.1002/esp.1813.

# 이 논문을 찾은 이유
LPJ-GUESS woody cohort의 DBH, mortality, fire-killed standing trees를 실제 root-throw event volume과 시간지연, sediment transport로 바꾸는 published quantitative bridge를 찾기 위해 검토했다.

# 연구 유형
- postfire field study
- forest-population dynamics model
- root-throw sediment-transport model
- wildfire disturbance coupling

# 공간 구조
- forest plots / hillslope
- Canadian Rockies, Hawk Creek
- field-calibrated root-plate geometry
- model cycles through successive forest generations and fires

# 적용 환경
- subalpine forest
- Pinus contorta, Picea engelmannii, Abies lasiocarpa
- 2003 crown fire
- hillslope gradients from gentle to about 28 degrees in detailed plots, steeper terrain elsewhere

# 핵심 과정
- tree recruitment
- growth / DBH development
- competition mortality
- fire mortality
- delayed toppling
- uprooting versus stem breakage
- root-plate volume
- root-plate disintegration
- sediment transport

# 식생 입력
Original model uses:
- tree cohort
- tree age
- DBH distribution
- mortality
- fire-killed standing dead trees
- time since death/fire

For Gounsa these states are conceptually close to LPJ-GUESS woody cohort outputs.

# 핵심 식

## 1. root plate volume from DBH

Field-derived Hawk Creek regression:

```
V_RP
=
-5.74e-4 * DBH
+
5.82e-3 * DBH^2
```

where:
- `V_RP`: root plate volume [m3]
- `DBH`: diameter at breast height [cm]

Fit:
```
R2 = 0.45
```

This is a direct published:
```
DBH -> uprooted soil/root-plate volume
```
bridge.

Mean root-plate volume also increased with slope class:
- gentle plot around 0.22 m3
- intermediate around 0.35 m3
- steep plot around 0.71 m3

Thus DBH is not the only control.

## 2. root-plate geometry

Field root-plate volume is calculated using a half-ellipsoid approximation.

The measured dimensions are:
- width parallel to surface
- height normal/plan dimension
- depth

The half-ellipsoid geometry provides the event volume.

## 3. dead-tree toppling delay

Standing dead trees topple with exponential waiting:

```
F_T
=
1 - exp(-F * dt)
```

where:
- `F_T`: fraction toppling during timestep
- `F`: annual falling-rate parameter
- `dt`: timestep [yr]

Example model parameters:
- between-fire falling rate: 0.058 yr^-1
- postfire falling rate for fire-killed trees: 0.084 yr^-1

These are site-specific.

## 4. uprooting versus breakage

For the Hawk Creek model:
```
fraction uprooted = 0.8
```

based on local empirical surveys.

This means:
```
tree mortality/toppling
!=
root throw
```

Only the uprooted fraction becomes root-throw sediment disturbance.

## 5. critical DBH

The model only counts notable sediment upheaval when:

```
DBH > 13 cm
```

This threshold comes from local/unpublished regional observations and must not be treated as universal.

## 6. root-plate disintegration

The fraction of original root-plate volume remaining after time `t` years is fitted as:

```
PV
=
-0.1029
+
46.19 exp(-0.719 t)
+
56.35 exp(-0.02102 t)
```

where:
- `PV`: percent volume remaining [%]
- `t`: years since root throw

Thus sediment is not necessarily delivered to the ground instantaneously.

The model spreads root-plate sediment release through time.

## 7. fraction falling outside the pit

```
P_S
=
FA / 180
```

where:
- `P_S`: proportion of sediment falling outside the original pit
- `FA`: tree fall angle in degrees under the paper's directional convention

This is geometry-specific.

## 8. root-plate width/height for transport geometry

```
w_RP
=
0.65
+
4.65 DBH
```

```
h_RP
=
29.24
+
0.54 w_RP
```

where:
- DBH [cm]
- `w_RP`, `h_RP` [cm]

Reported:
```
R2 = 0.62
```
for the listed geometry regressions.

## 9. sediment transport rate

The model sums event displaced sediment volume times event travel distance over plot area:

```
q_s
~
sum(V_RP,event * dist_RP,event) / A_t
```

where:
- `q_s`: sediment transport rate [m3 m^-1 yr^-1]
- event volume and travel distance are evaluated separately
- only sediment ending outside the original pit contributes net transport

# 핵심 postfire result

Two sediment-transport pulses emerge:

1. If prefire trees are already large enough, fire-killed trees topple over subsequent years and generate an immediate postfire pulse that decays with time since fire.
2. After roughly 50-60 years, new cohort trees begin reaching sediment-effective size and competition mortality produces a second tree-throw pulse.

This is highly relevant to a 100-year Gounsa simulation.

# 고운사에 직접 사용할 수 있는 부분

The strongest transferable architecture is:

```
LPJ-GUESS cohort DBH
+ mortality state
+ fire-killed standing-dead state
        |
        v
toppling probability over time
        |
        v
uprooting vs stem break
        |
        v
V_RP(DBH)
        |
        v
pit/mound geometry
        |
        v
sediment travel and delayed release
```

Unlike Gabet & Mudd 2010, this paper directly provides a DBH-to-root-plate-volume regression.

# 새로운 coupling이 필요한 부분

Applying the Canadian Rockies regression to Korean PFTs is not automatically valid.

The following remain Gounsa-specific/new:
- PFT/species correction to `V_RP(DBH)`
- wind/storm-driven uprooting probability if wind data are introduced
- fire severity/root-decay effects on toppling rate
- raster placement of pit and mound
- coupling LPJ-GUESS cohort mortality to the Gallaway toppling-delay state

# limitations
- Canadian Rockies conifers
- local root architecture and coarse substrate
- moderate R2 for DBH-volume relation
- several falling/DBH parameters based on unpublished regional data
- original model uses its own forest population dynamics rather than LPJ-GUESS

# final judgment
**핵심 채택: strongest direct published DBH -> root-plate volume + postfire delayed tree-throw bridge currently identified.**

Use the functional architecture in production.

Use numerical coefficients initially only as comparison/sensitivity priors until Korean/local calibration is available.

# 참고 링크 / DOI
https://doi.org/10.1002/esp.1813
