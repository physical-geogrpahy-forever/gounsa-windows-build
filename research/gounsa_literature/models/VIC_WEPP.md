# VIC-WEPP / WEPP-HE lineage

## 핵심 문헌
- Mao, Cherkauer & Flanagan (2010), WRR 46, W08543, DOI 10.1029/2009WR008268
- Gould et al. (2016), Journal of Hydrology 536, 74-91, DOI 10.1016/j.jhydrol.2016.02.025

## 고운사에서 검토한 이유
large-scale distributed hydrology와 WEPP-style process erosion을 published coupling으로 실제 결합한 선례, 그리고 이를 산불 산악 유역에 적용한 선례를 찾기 위해 검토했다.

## 구조
```
VIC hydrology
 -> runoff / soil-water states
 -> WEPP-HE erosion parameterization
 -> erosion/sediment yield
```

Full WEPP vegetation states를 사용하여:
- ground cover
- live root biomass
- dead root biomass
- residue
등이 erodibility adjustment에 들어간다.

## 산지/산불 적용
Gould et al. 2016:
- Salmon River Basin, Idaho
- northern Rocky Mountains
- wildfire mountain watershed
- elevation 약 304-3713 m

## 장점
- quantitative vegetation/root state를 process erosion resistance에 넣는 실제 coupling
- forest/wooded grassland/prairie/cropland vegetation classes
- wildfire mountain watershed application

## 한계
- genuine 2D shallow-water surface flow가 아님
- representative hillslope architecture

## 고운사에 쓸 수 있는 부분
- `vegetation state -> erodibility` coupling의 published precedent
- mountain wildfire application precedent

## 새로운 coupling
VIC 대신 LPJ-GUESS를 사용하거나 WEPP-HE 대신 genuine 2D engine을 사용하면 **새로운 coupling**.

## 최종 판정
**핵심 선례.** 2D engine 자체는 아님.
