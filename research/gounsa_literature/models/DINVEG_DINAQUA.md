# DINVEG + DINAQUA

업데이트: 2026-09-23

## 현재 판정
고운사 생산 식생엔진 후보가 아니라 **하층 초본-관목 demographic benchmark**이다.

장점은 초본과 관목의 전 생애주기, 종자은행, 공간좌표, 6층 토양수분, 수직 뿌리중첩을 매우 명시적으로 다룬다는 점이다. 결정적 약점은 교목이 없고 식생 demographic timestep이 월 단위라는 점이다.

## 구조
DINVEG는 Patagonian semi-arid grass-shrub steppe용 spatially explicit individual-based ecohydrological model이다.

공간:
- 50 x 50 m plot
- 0.2 x 0.2 m cells
- grass tuft가 대략 한 cell을 차지
- shrub는 최대 여러 cells를 점유
- 각 식물은 x,y 좌표를 가짐

식생:
- grass species
- shrub species
- seed bank
- seedling / young / adult stages

주요 demographic processes:
1. seed dispersal / seed bank
2. emergence
3. recruitment
4. facilitation
5. growth
6. water competition
7. space competition
8. mortality
9. seed production

## 수문과 뿌리
DINAQUA가 soil water를 계산한다.
- 6 soil layers
- each 0.1 m thick
- volumetric soil water content
- grass/shrub transpiration
- explicit alternative hypotheses for vertical root overlap
- neighborhood root competition includes focal cell and surrounding 3 x 3 cells

따라서 초본과 관목의 vertical root niche separation 및 overlap을 직접 시험할 수 있다.

## 시간구조
DINVEG demographic model:
- monthly timestep
- 200-year simulations in Cipriotti et al. 2014

DINAQUA validation/output에는 daily soil water series가 사용되기도 하지만, coupled vegetation demographic update itself is monthly.

따라서 고운사 strict criterion 5에는 FAIL/PARTIAL이다.

## 고운사 가치
MEDFATE처럼 woody recruitment는 좋지만 herbaceous recruitment가 약한 모델을 확장할 경우, DINVEG의 다음 구조가 좋은 참고가 된다.

```text
species seed bank
 -> emergence
 -> seedling recruitment
 -> adult herb/shrub
 -> growth/reproduction/mortality
```

또한
```text
layer soil water
 + species root distribution
 -> emergence/recruitment/growth/mortality
```
의 demographic filtering을 그대로 참고할 수 있다.

## 5조건
| 기준 | 판정 |
|---|---|
| 1 spatial cohort/hybrid | spatially VERY STRONG but full individuals, not cohorts |
| 2 understory + succession | VERY STRONG for grass/shrub; no trees |
| 3 soil/root | STRONG: 6 layers and root-overlap competition |
| 4 watershed/topography | WEAK: homogeneous 50 m plot, no distributed hillslope routing |
| 5 <=daily | FAIL/PARTIAL: demographic timestep monthly |

## 최종 역할
**하층식생 demographic module benchmark.**

고운사 최종 vegetation engine을 대체하지 않지만, postfire herb/shrub recruitment extension을 설계할 때 가장 유용한 비교모델 중 하나다.

## 핵심 문헌
- Cipriotti et al. (2012), original DINVEG formulation.
- Cipriotti et al. (2014). A complex network of interactions controls coexistence and relative abundances in Patagonian grass-shrub steppes. Journal of Ecology. DOI 10.1111/1365-2745.12246.
- Cipriotti et al. (2019). Combined effects of grazing management and climate on semi-arid steppes. Journal of Applied Ecology.
