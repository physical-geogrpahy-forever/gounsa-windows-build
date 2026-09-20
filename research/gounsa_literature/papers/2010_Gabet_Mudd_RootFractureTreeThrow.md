# 서지정보
Gabet, E. J., & Mudd, S. M. (2010). *Bedrock erosion by root fracture and tree throw: A coupled biogeomorphic model to explore the humped soil production function and the persistence of hillslope soils*. Journal of Geophysical Research: Earth Surface, 115, F04005. DOI: 10.1029/2009JF001526.

# 이 논문을 찾은 이유
100년 고운사에서 LPJ-GUESS woody cohort를 연 단위 physical bedrock disturbance와 tree throw에 연결할 수 있는 실제 numerical precedent인지, 그리고 root fracture가 어느 정도 mechanistic하게 구현되어 있는지 원문을 재검토했다.

# 연구 유형
- annual coupled numerical biogeomorphic model
- tree population + tree mortality + tree throw + physical bedrock disturbance + soil creep

# 공간 구조
- 1D 100 m hillslope
- 0.1 m nodes
- explicit soil-thickness and bedrock surface
- finite-difference creep

# 적용 환경
- Pacific Northwest temperate conifer analogue
- Douglas fir
- weak sandstone analogue

# 시간간격
**1 year.**

Every year the model updates:
- recruitment
- mortality
- toppling
- pit/mound excavation
- clast disintegration
- bedrock elevation
- soil creep

# vegetation structure
The original model uses a very simple annual tree-population model.

Mortality probability is set to approximately:
```
1/330 yr^-1
```
for old-growth Douglas fir life expectancy.

Tree throw is then separated from other death modes.

From regional observations, topples were assumed to cause about:
```
15% of tree deaths
```
for trees old enough to topple.

Only trees older than about 80 years are eligible for this tree-throw treatment in the original parameterization.

These values are regional and not transferable to Gounsa.

# pit/rootwad geometry

The key numerical treatment is geometric rather than mechanical.

Rootwad/pit volume is sampled from a normal distribution:
```
V_pit
~ Normal(
  mean = 3 m3,
  sd = 1.3 m3
)
```
for the Douglas-fir analogue.

The pit is approximated as half an ellipsoid with circular planform.

With:
```
h_p = r / 2
```
the radius is:

```
r
=
(3 V / pi)^(1/3)
```

A semi-elliptical pit of this geometry is excavated from:
- soil
- and bedrock if the pit reaches below the soil-bedrock interface.

# thin-soil rootwad rule
The model assumes rootwad depth/radius declines in thin soil.

For soil thicker than 0.5 m:
```
h_p / r = 1/2
```

As soil thickness falls from 0.5 m to zero, the ratio is assumed to decrease linearly toward:
```
1/4
```

The authors explicitly state that this thin-soil geometry rule is **not quantitatively derived from data** and is a reasoned assumption.

# critical correction: what "root fracture" means in the numerical model

The model does **not** calculate:

```
root force
vs
bedrock tensile/fracture strength
```

and does not contain a mechanistic root-force fracture criterion.

Instead, physical bedrock disruption is represented geometrically.

For a tree throw:
- the rootwad/pit volume intersects the bedrock
- intersected bedrock is excavated/disrupted.

For a tree that dies but does not topple:
- the extent of bedrock broken by root growth is assumed to be similar to the dimensions of an uprooted rootwad
- the disrupted material remains in place because there is no lateral displacement.

Thus:

```
root fracture in Gabet-Mudd
=
rootwad-geometry-based bedrock disturbance
```

rather than a mechanistic rock-fracture-force model.

# bedrock clasts and physical weathering
Disrupted bedrock is represented as approximate 25 cm cubic clasts.

The paper explicitly says this is an approximation.

Clast surfaces are then weathered annually.

A sandstone disintegration rate of:
```
0.5 mm yr^-1
```
is adopted from another cool/wet setting.

Do not transfer this value to Gounsa.

# tree-fall direction
Original 1D model assumes fall either uphill or downhill.

Probability of downhill fall increases linearly from:
- 50% on horizontal surface
- 90% at 45 degrees

The authors acknowledge this is poorly constrained and actual wind direction can dominate.

# mound transport
Pit-mound centroid separation uses the Gabet et al. 2003 tree-throw geometry.

The mound is created at the event in the numerical model, although in reality root-plate release can take 5-10 years or longer.

Gallaway 2009 provides a much better explicit delayed-disintegration formulation.

# background creep
Original:
```
q_sc = -D S
```

with:
```
D = 2.5e-3 m2 yr^-1
```
for the Oregon analogue, plus annual random variation.

Gounsa no longer adopts this as its background law.

Current Gounsa baseline:
```
q_bg = -D*_bg H_active grad(z)
```
from the residual-creep decision.

# 고운사에 직접 사용할 수 있는 부분

Strong transferable architecture:

```
annual woody cohort
 -> mortality
 -> toppling or standing death
 -> rootwad/pit geometry
 -> soil/bedrock intersection
 -> physical bedrock disturbance
 -> pit/mound microtopography
```

This is much closer to the Gounsa timescale than long-term Pelletier soil-production functions.

# relation to LPJ-GUESS
LPJ-GUESS can replace the simple internal forest demography for:
- DBH/cohort size
- density
- mortality
- disturbance status

But rootwad geometry should preferably use a DBH-dependent published relation such as Gallaway 2009 rather than the fixed random Douglas-fir rootwad distribution.

# 새로운 coupling
The production Gounsa coupling would be:

```
LPJ-GUESS DBH/cohort mortality
 -> uprooting probability
 -> rootwad geometry
 -> bedrock intersection/disturbance
```

This exact combined system is new.

# unresolved
1. local/PFT-specific rootwad-volume relationship
2. uprooting probability after each mortality cause
3. whether roots penetrating C/Cr disturb rock even without tree death
4. actual rock-fracture efficiency within rootwad volume
5. clast-size distribution created by root disturbance

# final judgment
**채택: annual geometric physical-weathering architecture.**

Important limitation:
do not describe it as a mechanistic root-force fracture model.

Use Gallaway/other root-plate allometry to improve geometry, and retain rock-fracture efficiency as a calibration/uncertainty term.

# 참고 링크 / DOI
https://doi.org/10.1029/2009JF001526
