# 결정: COPLAS 최종근거 제외와 식생 coupling 대체

날짜: 2026-09-21

## 결정 내용
COPLAS는 고운사 최종모델의 식생-지형 coupling 근거에서 제외한다.

## 왜 결정했는가
COPLAS는 leaf, root, litter, soil carbon을 해당 연구지의 평균과 표준편차로 0–1 정규화한 뒤 침식 관련 계수에 연결한다. 따라서 정규화값 1이 절대적인 생태학적 포화상태를 뜻하지 않으며 다른 지역으로 계수를 직접 이전하기 어렵다.

또한 leaf biomass가 전체 diffusive coefficient를 낮추기 때문에 rain splash와 creep이 함께 변하는 단순화가 있다.

## 근거 논문
Quijano-Baron et al. (2022), Catena 213, 106123.

## 보존할 개념
- 식물 기관별 biomass pool이 서로 다른 지형과정에 작용할 수 있음
- root, leaf, litter 효과를 하나의 vegetation-cover factor로 합치지 않을 수 있음

## 대체 방향
### 수관
Istanbulluoglu & Bras (2005)의 vegetation cover fraction 기반 관계를 참고한다.
```text
K_d = K_b exp(-alpha V)
```
LPJ-GUESS LAI에서 V를 계산하는 과정은 새로운 coupling이다.

### 뿌리
FineRootC를 COPLAS식 site normalization으로 넣지 않는다. absolute root biomass, root density, RLD, root cohesion 등 실제 erosion-resistance와 연결되는 변수를 우선 검토한다.

### litter
SurfaceLitC를 site z-score 형태로 정규화하지 않는다. litter mass 또는 litter cover와 flow resistance 사이의 published quantitative relation을 우선한다.

## 무엇을 제외했는가
- COPLAS의 normalized Leaf -> D
- COPLAS의 normalized Root -> beta를 고운사 최종식으로 그대로 사용
- COPLAS의 normalized Litter -> Manning n을 그대로 사용
- COPLAS 자체를 최종 고운사 모델 근거라고 표현하는 것

## 아직 해결되지 않은 문제
- root biomass와 erodibility의 최종 published relation
- litter mass/cover와 flow resistance의 최종 relation
- canopy effect를 splash와 creep 중 어느 항에 어떻게 배분할지

## 최종 판정
COPLAS는 탈락. 원 논문파일과 모델파일은 연구과정 기록을 위해 보존한다.
