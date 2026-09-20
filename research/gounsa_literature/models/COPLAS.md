# COPLAS

## 핵심 논문
Quijano-Baron, J., Saco, P. M., & Rodriguez, J. F. (2022). Modelling the effects of above and belowground biomass pools on erosion dynamics. *Catena, 213*, 106123. https://doi.org/10.1016/j.catena.2022.106123

## 구조
COPLAS는 hydrology, vegetation, biomass pools, landform evolution을 일 단위로 순차결합하고 SIBERIA 계열 지형식을 사용한다.

주요 biomass coupling:
```text
root   -> soil erodibility beta
leaf   -> diffusion coefficient D
litter -> Manning n
soil C -> water-retention capacity
```

## 핵심식
```text
q_s = beta q^m S^n
q_d = D S
D = Dmax - alpha Lhat
n = nbare + nref Lithat^w
```

Root 등 biomass pool은 해당 연구지의 평균과 표준편차를 이용해 정규화한다.
```text
Rhat = ((R - Rmean) / Rstd) / 5 + 0.5
```

## 이 세션에서 확인한 문제
- normalized biomass = 1이 생태학적 포화상태를 의미하지 않음
- 지역 평균과 표준편차에 의존하므로 다른 지역으로 직접 parameter transfer가 어려움
- leaf가 D 전체를 낮추므로 rain splash뿐 아니라 creep도 동시에 억제하는 형태가 됨
- big-leaf 접근이라 상층과 하층 식생을 분리하지 않음
- LPJ-GUESS LeafC, FineRootC, SurfaceLitC와 정의가 완전히 동일하지 않음

## 고운사 판정
COPLAS는 고운사 최종모델의 직접 근거에서 제외한다.

보존할 것은 다음의 개념적 아이디어뿐이다.
- 식물 기관별 biomass pool이 서로 다른 지형과정에 영향을 줄 수 있음
- root, leaf, litter 효과를 하나의 vegetation-cover 계수로 합치지 않는 것이 가능함

## 대체 방향
- leaf: LPJ-GUESS LAI -> actual vegetation cover/FPC -> published vegetation-dependent hillslope relation
- root: absolute root biomass 또는 root traits -> soil erodibility
- litter: litter mass 또는 cover -> flow resistance
- soil carbon hydrology: LPJ-GUESS 수문과 중복되지 않도록 별도 검토

## 새로운 coupling
위 대체 연결은 COPLAS 원식이 아니며 모두 고운사의 새로운 coupling이다.

## 최종 판정
- 최종모델 근거: 탈락
- 역사적 참고: 유지
