# 서지정보
Chibesa, M. C., Monoshyn, D., Puschenreiter, M., Golestanifard, A., Wieshammer, G., Wenzel, W. W., & Santner, J. (2025). Silicon solubilisation from soil minerals and soil by root exudate compounds. *Geoderma, 459*, 117375. DOI: 10.1016/j.geoderma.2025.117375.

# 이 논문을 찾은 이유
균근을 제외하고 root-exudate compounds 자체가 realistic rhizosphere concentration에서 soil/mineral weathering을 얼마나 변화시키는지, 그리고 그 효과가 mineral-specific인지 확인하기 위해 검토했다.

# 연구 유형
- controlled extraction / dissolution experiment
- soil + primary mineral + clay mineral comparison

# 공간 구조
- batch mineral/soil reaction
- rhizosphere concentration analogue

# 적용 환경
- six soils
- seven primary minerals
- four clay minerals

# 핵심 과정
- citrate complexation
- oxalate complexation / dissolution
- catechol redox/complexation
- Si solubilisation
- co-solubilisation of Al, Ca, Fe, K, Mg, Mn

# 식생 입력
실제 plant model은 없다.

root-derived chemistry analogue:
- citrate
- oxalate
- catechol

# 핵심 식
수치 model equation보다 controlled comparison이 핵심.

공통 treatment concentration:
```
5 mmol L^-1
```
수준의 OREC concentration을 사용했다.

이 값은 고운사 source term으로 직접 전이하지 않는다.

# 핵심 결과
OREC는 control보다 Si solubilisation을 크게 증가시킬 수 있었고, 일부 mineral/soil에서는 최대 약 11배 수준 차이가 나타났다.

하지만 효율 순위가 substrate에 따라 달랐다.

Primary minerals:
```
citrate > catechol > oxalate
```
경향

Clay minerals:
```
catechol > citrate > oxalate
```
경향

Soils:
```
oxalate > citrate > catechol
```
경향

즉:

```
root exudate effect
= compound-specific
x mineral-specific
x soil-state-specific
```

이다.

# 파라미터와 단위
- organic compound concentration [mmol L^-1]
- extracted Si
- Al, Ca, Fe, K, Mg, Mn co-solubilisation
- soil clay/mineral composition

# 원 논문의 구현 범위
realistic rhizosphere-level root-exudate compounds가 primary/clay minerals와 soils의 Si release에 미치는 차이를 실험.

# 고운사에 직접 사용할 수 있는 부분
중요한 parameterization constraint:

```
DOC pool
!= one generic ligand
```

최소한 root-exudate sensitivity를 만들 경우 ligand composition 또는 effective ligand class를 구분해야 한다.

또한 고운사 sandstone mineralogy/cement composition이 root-exudate weathering response를 강하게 제약할 가능성을 지지한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root C / nutrient stress를:
- citrate-like
- oxalate-like
- phenolic/reducing compound
effective source로 분리하는 것은 새로운 coupling이다.

첫 production에서는 full speciation을 넣지 않고 sensitivity level에서 다룬다.

# 한계
- short-term batch extraction
- actual forest root system 아님
- sandstone whole-rock weathering directly tested하지 않음

# 최종 판정
- **채택: non-mycorrhizal root-exudate mineral-specific constraint**
- root-exudation은 optional sensitivity로 유지
- single organic-ligand multiplier는 사용하지 않음

# 참고 링크 / DOI
https://doi.org/10.1016/j.geoderma.2025.117375
