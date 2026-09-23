# Boulangeat et al. (2014) FATE-HD

## 서지정보
Boulangeat, I., Georges, D., Dentant, C., Bonet, R., Van Es, J., Abdulhak, S., Zimmermann, N. E., & Thuiller, W. (2014). FATE-HD: a spatially and temporally explicit integrated model for predicting vegetation structure and diversity at regional scale. *Global Change Biology*, 20, 2368–2378. DOI: 10.1111/gcb.12466.

## 이 논문을 검색한 이유
고운사 기준 가운데 특히 `공간명시 cohort`, `하층 초본·관목·교목 천이`를 가장 강하게 충족하는 landscape vegetation model이 일 이하 시간단계까지 가질 수 있는지 확인하기 위해 검토했다.

## 연구 유형
공간명시 동적 식생·생물다양성 모델 개발 및 프랑스 알프스 국립공원 적용/검증.

## 공간구조
- regular geographic grid
- case study: 258,582 pixels, 100 m resolution
- each grid cell has independent within-cell succession model
- cells linked by explicit seed dispersal
- individuals aggregated into age cohorts
- cohorts occupy height strata

## 적용환경
French Alps, Écrins National Park, 669–4102 m elevation, 178,400 ha; forest, heath, alpine and herbaceous communities.

## 핵심과정
- germination
- recruitment
- growth
- survival
- fecundity
- age-cohort transition
- vertical light competition by strata
- seed dispersal between cells
- abiotic habitat filtering
- disturbance effects on survival/fecundity/seeds

## 식생입력
24 plant functional groups in the key application:
- H1–H10: herbaceous groups
- C1–C6: chamaephyte/shrub/heath groups
- P1–P8: phanerophyte/tree groups

Each PFG can occupy multiple age cohorts and up to five height strata.

## 핵심식/알고리즘
FATE-HD uses a semi-quantitative succession framework rather than continuous mechanistic carbon/water equations. Light availability in a stratum is determined by abundance in upper strata and affects germination, recruitment and survival. Seed dispersal links cells and adds seeds to cell-level seed banks.

## 파라미터와 단위
Parameters are primarily demographic and semi-quantitative:
- cohort age class
- abundance
- shade tolerance/effect
- germination/recruitment/survival/fecundity probabilities
- dispersal-distance classes
- disturbance sensitivity/tolerance
- climate/habitat suitability

## 고운사에 사용할 수 있는 부분
Criterion 2 benchmark로 매우 중요하다. 초본, 낮은 관목/초본성 목본, 관목, pioneer/late-successional trees가 한 모델 안에서 명시적으로 경쟁·정착·소멸한다. 산불 후 하층식생 천이를 생물학적으로 어떻게 구조화할지 참고하기 좋다.

## 필요한 새로운 coupling
- mechanistic daily soil water module
- soil-depth/WHC feedback
- event-scale geomorphic state exchange
- hourly/daily storm response

이 모든 것은 **새로운 coupling**이 된다.

## 한계
가장 결정적 한계는 **succession model time step이 1 year**라는 점이다. 따라서 6시간 폭우가 지형과 토양을 바꾼 뒤 같은 날/다음 날 식생 수분상태와 생리 반응이 변하는 고운사 목적에는 맞지 않는다.

또한 climate response가 habitat-suitability map 형태로 들어가므로 soil-water mechanistic feedback이 약하다.

## 최종 판정
**생물학적 구조 benchmark로 유지, production vegetation engine 후보에서는 탈락.**

Five criteria:
- spatial cohort: YES
- explicit understory succession: EXCELLENT
- soil/geomorph coupling readiness: WEAK
- mountain/topography application: YES
- <=daily: NO, annual succession

FATE-HD는 criterion 2가 얼마나 명시적이어야 하는지 보여주는 좋은 기준점이지만 criterion 5 때문에 고운사의 직접 engine으로는 부적합하다.
