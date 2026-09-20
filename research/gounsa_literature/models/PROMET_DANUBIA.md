# PROMET / DANUBIA erosion lineage

## 핵심 자료
- Waldmann (2010), *Large-Scale Process-Oriented Modelling of Soil Erosion by Water in Complex Watersheds*, DOI 10.5282/edoc.11575
- related Waldmann & Mauser Upper Danube paper, exact publication metadata needs re-verification

## 고운사에서 검토한 이유
dynamic vegetation model이 root length density를 직접 계산하여 erosion resistance에 전달하는 actual numerical implementation을 찾기 위해 검토했다.

## 공간구조
- PROMET distributed proxels
- Upper Danube basin
- about 1 km2 spatial scale
- hourly erosion time step
- proxel runoff/sediment delivered to channel network
- not genuine 2D shallow-water surface routing

## vegetation state
PROMET biological module dynamically calculates root development:
```
root biomass growth
 -> root length increment
 -> allocation among soil layers
 -> RLD by layer
 -> senescence/update
```

RLD is then used in erosion-resistance/root-reinforcement parameterization.

## erosion vegetation coupling
This chat verified an exponential root-density effect lineage, but exact final equation and parameter choices should be taken from Waldmann dissertation equation numbers rather than reconstructed from memory.

## 강점
- dynamic quantitative root state
- root length density, not just cover
- coupled vegetation-hydrology-erosion
- alpine/mountain basin included

## 한계
- not genuine 2D surface hydraulics
- coarse proxel scale
- hillslope sediment routing differs from high-resolution DEM routing

## 고운사에 쓸 수 있는 부분
Strong published precedent for:
```
dynamic vegetation
 -> RLD
 -> erosion resistance
```

## 새로운 coupling
PROMET RLD equations transferred to LPJ-GUESS or a 2D engine are **새로운 coupling**.

## 최종 판정
**핵심 vegetation bridge lineage.**
