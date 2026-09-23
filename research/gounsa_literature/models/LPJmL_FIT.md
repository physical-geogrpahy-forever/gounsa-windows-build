# LPJmL-FIT

## 왜 검토했는가
고운사 식생엔진 후보의 다섯 조건을 만족하는 모델을 추가 탐색하는 과정에서, LPJmL-FIT이 10 m x 10 m forest gap patch, 개별 수목과 grass PFT 경쟁, 일별 기후/토양수문, 자연 정착/경쟁/고사를 동시에 갖는 것으로 확인되어 정식 후보로 검토했다.

## 모델 성격
- LPJmL 계열 flexible-individual-trait DGVM
- 10 m x 10 m independent forest patches
- individual trees + herbaceous grass PFTs
- 자연 정착, 생장, 경쟁, 사망
- daily climate forcing and soil hydrology

## 1. 공간명시 구조
**STRONG-PARTIAL.**

각 large grid cell 내부에 다수의 독립 10 m x 10 m forest patches를 모의한다. patch 내부에서는 실제 수목 개체를 개별적으로 계산한다.

장점:
- 매우 세밀한 forest-gap scale
- 고운사의 10-25 m 식생격자와 공간규모가 잘 맞음

한계:
- 이 10 m patch들은 geographic x-y로 서로 연결된 실제 사면 셀이 아니라 큰 grid cell을 대표하는 replicate patch로 쓰이는 경우가 많음
- patch 사이 lateral water flow나 seed dispersal이 기본 구조의 핵심은 아님

## 2. 하층식생과 천이
**STRONG-PARTIAL.**

공개 연구에서 LPJmL-FIT은 tree individuals와 C3/C4 grass PFTs를 명시적으로 함께 계산한다.
- tree와 grass는 같은 10 m x 10 m patch에서 light와 water를 경쟁
- 새 tree strategy가 지속적으로 establishment 가능
- 환경 및 경쟁 filtering에 따라 tree community가 내생적으로 변화
- grass도 herbaceous PFT로 존재

그러나:
- shrub layer가 별도 명시적 demographic group으로 잘 발달한 모델은 아님
- herbaceous diversity는 주로 C3/C4 grass PFT 수준
- 고운사에서 원하는 산불 후 `초본 -> 관목 -> 교목`의 세 단계 천이를 직접 풍부하게 표현하려면 shrub PFT extension이 필요

따라서 MEDFATE의 shrub cohorts나 FATES의 shrub/grass/tree demography보다 criterion 2는 약간 낮다.

## 3. 토양-지형 coupling readiness
**MODERATE-STRONG for local soil water, WEAK for lateral terrain coupling.**

- daily climate forcing
- soil texture controls soil hydrology
- tree and grass water competition
- variable rooting scheme lineage available
- soil water stress affects transpiration, photosynthesis, phenology, growth efficiency and mortality

외부 토양-지형모델에서 soil moisture/soil properties를 주입하는 것은 구조적으로 가능해 보이지만, PF-LPJG처럼 external hydrology state overwrite가 published coupling으로 확인된 것은 아니다.

침식/퇴적으로 토심이나 layer geometry가 바뀌는 경우에는 새로운 coupling이 필요하다.

## 4. 유역/지형 선례
**WEAK-PARTIAL.**

- Alpine Mountains, Carpathians, Central European low mountains 등 산악 환경 적용은 있음
- 그러나 해당 적용들은 geographic grid climate/soil forcing에 기반하며, 실제 연결된 hillslope/catchment lateral hydrology를 푼 사례는 현재 확인하지 못함
- 10 m patch도 실제 DEM-connected terrain cells가 아니라 representative forest patches인 경우가 많음

따라서 criterion 4가 주된 약점이다.

## 5. 시간해상도
**YES for daily environmental response.**

- climate input daily
- soil hydrology daily
- photosynthesis/water limitation daily process framework
- tree demography/trait filtering은 장기적 forest dynamics로 누적

고운사의 일 단위 식생-지형 synchronization에는 원칙적으로 적합하다.

## 고운사 장점
1. 10 m patch라는 매우 적절한 공간규모
2. 개별 수목 + grass coexistence
3. 자연 establishment와 경쟁 filtering
4. flexible traits로 postfire recovery 전략 차이를 표현 가능
5. daily soil-water and vegetation response
6. European temperate forest validation이 풍부

## 고운사 한계
1. explicit shrub succession이 약함
2. representative patch와 actual geographic terrain cell을 혼동하면 안 됨
3. published catchment lateral hydrology coupling이 확인되지 않음
4. 개별목 계산은 cohort model보다 무거움
5. geomorphic soil-depth change state-remapping은 native 기능이 아님

## five-criteria verdict
| criterion | verdict |
|---|---|
| 1 spatial cohort/hybrid | PARTIAL-STRONG: 10 m individual-tree gap patches, but often replicate patches rather than connected terrain cells |
| 2 explicit understory succession | STRONG-PARTIAL: trees + grasses explicit, shrubs weak |
| 3 soil/geomorph coupling readiness | MODERATE-STRONG local soil water; external/lateral coupling not demonstrated |
| 4 watershed/topography precedent | PARTIAL/WEAK |
| 5 <= daily | YES |

## 현재 역할
**Serious secondary candidate, but not above LPJ-GUESS spatial-hydrology lineage.**

LPJmL-FIT은 식생 생태와 10 m 규모에서는 매우 매력적이다. 그러나 고운사에서 결정적인 `actual hillslope/catchment + external soil state coupling` 근거가 약하기 때문에, 현 시점에서는 PF-LPJG/LPJ-DH 계열을 제치지 못한다.

## key references
- Sakschewski et al. (2015), Global Change Biology, flexible individual traits lineage.
- Thonicke et al. (2020), Journal of Biogeography, European forest adaptation.
- Schnabel et al. (2022), Scientific Reports, Future tree survival in European forests depends on understorey tree diversity. https://doi.org/10.1038/s41598-022-25319-7
- Billing et al. (2024), Global Change Biology, functional diversity across European regions.
- NHESS (2025), What if extreme droughts occur more frequently? Mechanisms and limits of forest adaptation in pine monocultures and mixed forests in Berlin-Brandenburg, Germany.
