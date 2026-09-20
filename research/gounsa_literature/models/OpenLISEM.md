# OpenLISEM lineage

## 핵심 문헌
- Wu et al. (2021), Catena 207, 105658, DOI 10.1016/j.catena.2021.105658
- Wu, Baartman & Nunes (2021), Catena 207, 105620, DOI 10.1016/j.catena.2021.105620
- current OpenLISEM source code inspected in this chat

## 고운사에서 검토한 이유
2D/spatial hydrology + erosion + sediment transport를 산불 산림 유역에서 실제 적용한 모델 중 root cohesion까지 받을 수 있는 후보인지 확인했다.

## 공간구조
- spatially distributed
- current code includes 2D SWE/flood-flow paths
- runoff, sediment transport and erosion modules
- burned Mediterranean catchment application exists

## vegetation/root implementation confirmed from source code
Input maps include:
- `coh.map`: soil cohesion
- `cohadd.map`: extra cohesion by e.g. plant roots
- vegetation cover
- litter cover
- LAI
- plant height

Current initialization includes approximately:
```
CohesionSoil = COHCalibration * (Cohesion + Cover * RootCohesion)
```

Then detachment efficiency `Y` is calculated from cohesion.

## interpretation
Root cohesion can be supplied spatially, but:
- it is an external map
- it is weighted by vegetation cover
- the model itself does not dynamically derive root cohesion from root biomass/RLD

Therefore it does not satisfy the strict “quantitative vegetation state directly calculated by model” requirement.

## 산불 적용
2021 Part 1/2:
- burned Mediterranean forest catchment
- 18.5 km2
- pre/postfire runoff and sediment response
- event and return-period analysis

## 고운사에 쓸 수 있는 부분
- 2D/spatial burned-catchment modeling precedent
- root-cohesion input architecture
- splash/flow erosion and sediment transport

## 새로운 coupling
LPJ-GUESS FineRootC/RLD -> root cohesion map is **새로운 coupling** unless an independent published conversion equation is used and cited.

## 최종 판정
**보조 2D/postfire lineage.**
Strict quantitative vegetation coupling fails in current implementation.
