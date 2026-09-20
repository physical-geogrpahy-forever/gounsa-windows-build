# 결정: 고운사 과정별 모듈을 분리한다

날짜: 2026-09-21

## 원칙
식생효과를 단일 vegetation coefficient로 합치지 않는다.

## 유수침식
```
LPJ-GUESS
 -> FineRootC / dead-root state / litter
 -> erosion-resistance interface
 -> 2D rainfall/runoff erosion engine
```

Interrill/rainfall-driven과 rill/flow-driven을 서로 다른 process term으로 유지한다.

## shallow landslide
```
FineRootC
 -> root distribution / architecture
 -> root reinforcement or cohesion c_r
 -> factor of safety
 -> shallow landslide
```

유수침식 Ki/Kr와 landslide root cohesion을 같은 parameter로 합치지 않는다.

## biogenic hillslope transport
- root growth/decay
- tree throw
- organismal soil transport
를 별도 lateral sediment flux로 둔다.

## vertical soil mixing
MILESD/LORICA/HydroLorica/ChronoLorica 계열의 vertical profile mixing은 lateral hillslope transport와 분리한다.

## postfire dry ravel
Lamb et al. 2011의 vegetation sediment-storage loss/recovery를 사용 가능한 독립과정으로 본다.

## thermal spall
spall fragment production은 Lamb dry ravel과 다른 source process이다.
현재 별도의 quantitative production equation이 필요한 unresolved gap이다.

## coarse fragments
- prefire gravel
- fines removal로 노출된 fragments
- fire-spall fragments
를 상태변수 후보로 둔다.
loose supply와 armour effect를 구분한다.
