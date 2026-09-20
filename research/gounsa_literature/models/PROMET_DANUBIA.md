# PROMET / DANUBIA erosion lineage

## 핵심 자료
- Waldmann (2010), *Large-Scale Process-Oriented Modelling of Soil Erosion by Water in Complex Watersheds*, DOI 10.5282/edoc.11575
- Léonard & Richard (2004), CATENA 57, 233-249, DOI 10.1016/j.catena.2003.11.007
- related Waldmann & Mauser Upper Danube publication, exact metadata requires re-verification

## 고운사에서 검토한 이유
dynamic vegetation model이 root length density를 직접 계산하여 erosion resistance와 critical runoff threshold에 전달하는 actual numerical implementation을 찾기 위해 검토했다.

## 공간구조
- PROMET distributed proxels
- Upper Danube basin
- about 1 km2 spatial scale
- hourly erosion time step
- proxel runoff/sediment delivered to channel network
- not genuine 2D shallow-water surface routing

## vegetation state
PROMET dynamically calculates:
```
root biomass growth
 -> root length increment
 -> soil-layer allocation
 -> RLD
 -> senescence/update
```

## erosion vegetation coupling
The implemented conceptual chain is:

```
RLD
 -> root-reinforced effective cohesion
 -> soil shear strength sigma_s
 -> critical runoff shear stress tau_c
```

For the last step Waldmann uses the Léonard & Richard lineage:
```
tau_c = beta * sigma_s
beta = 2.6e-4
```

The thesis caps soil shear strength at 20 kPa before conversion.

However, it subsequently multiplies `tau_c` by 0.0005 to match the magnitude of the erosion-resistance dataset used in its calibration.

Therefore:
- the **process pathway is published and implemented**
- the final numerical scaling is **not universal**

## importance for Gounsa
This is the strongest recovered numerical precedent for:

```
dynamic quantitative root state
 -> soil mechanical resistance
 -> hydraulic erosion threshold
```

It provides an alternative to trying to force roots directly into Hairsine-Rose `J`.

## relation to candidate engines

### tau_c-native closure
A 2D engine with an explicit critical-shear term can receive this lineage more naturally, subject to Gounsa calibration and grain/total-shear issues.

### SWEHR
SWEHR uses:
- `J`: specific entrainment energy
- `UC`: critical stream power

Thus PROMET does **not** directly close:
```
RLD -> J
```
or:
```
RLD -> UC
```

A critical stream-power threshold requires a hydraulically defensible critical velocity in addition to critical shear.

## 강점
- dynamic quantitative root state
- RLD, not just cover
- coupled vegetation-hydrology-erosion
- alpine/mountain basin included
- explicit numerical path to critical shear

## 한계
- not genuine 2D surface hydraulics
- coarse proxel scale
- hillslope sediment routing differs from high-resolution DEM routing
- empirical final rescaling of critical shear
- roughness partition/grain shear remains an important issue

## 새로운 coupling
PROMET RLD equations or strength-threshold relations transferred to LPJ-GUESS + SWEHR/SERGHEI/Iber are **새로운 couplings**.

## 최종 판정
**핵심 vegetation-to-threshold bridge lineage.**
