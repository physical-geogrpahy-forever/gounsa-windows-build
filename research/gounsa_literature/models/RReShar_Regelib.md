# RReShar / Capsis Regeneration library (Regelib)

## 현재 판정
완전한 all-cohort forest model은 아니지만, **하층 재생과 초본/관목을 공간 cell 기반 cohort/layer로 처리하는 현재형 모듈**로 고운사 하층식생 설계에 매우 중요한 선례다.

## 구조
RReShar는 1 ha plot을 사용자 지정 크기의 square cells로 나눈다.
- adult trees: explicit spatial individuals
- regeneration: species/size cohorts
- suppressed trees, saplings, seedlings
- herbaceous/shrubby vegetation: cell-level vegetation layers

따라서 전체 모델은 개체목+cohort hybrid이며 사용자가 요구한 순수 cohort model보다 복잡하다.

## 시간
- overstory/understory growth: annual
- light interception: monthly
- water cycle: daily

## 경쟁
- forest strata 사이 light and water competition
- tree regeneration과 herb/shrub vegetation이 같은 cell-level resource environment를 공유

## 공간
- 1 ha scene
- square cells, size user-defined and described as a few metres
- regeneration and vegetation vary by cell

## 최근 개발 상황 2024-2026
Capsis 공식 개발 기록에서 다음이 확인된다.
- 2024: tree/understorey root distribution across soil layers 개선
- 2024: Samsara2가 regeneration cohorts를 사용하고 이후 sapling/tree로 recruitment
- 2025: Sureau와 연결하여 tree와 understorey cohort/layer의 hydric stress 평가 작업
- 2025: Regeneration library에 nitrogen balance 개발 시작
- 2025: FORCEEPS-Regelib connection 및 regeneration management 개발
- 2026-09: Regelib cohort height classes 최적화

HETEROFOR도 이 Regeneration library를 사용한다.

## 하층식생 예시
공식 RReShar 문서는 다음과 같은 temperate understory 적용을 제시한다.
- Calluna vulgaris
- Pteridium aquilinum
- Molinia caerulea
- Rubus sp.
- tree seedlings including Quercus petraea, Carpinus betulus, Fagus sylvatica

## 뿌리
토층별 tree/understorey root distribution 작업이 공식 Capsis 개발기록에 존재하며, water sharing과 연결된다. 그러나 현재 공개 문서만으로 fine-root biomass turnover/litter pool이 MEDFATE 또는 LandscapeDNDC 수준으로 완성되었다고 단정하지 않는다.

## 고운사 의미
강점:
- 실제 수 m 공간 cell
- 하층 tree regeneration cohort
- herb/shrub vegetation layer
- daily water
- light competition
- 최근에도 actively developed

한계:
- adult layer는 개체목
- annual demographic growth
- full root/litter C pools 검증 부족
- wildfire/postfire succession native completeness 미확인

## 판정
**독립 최종 식생모델보다는 하층식생/재생 구조의 핵심 참고모듈.**
BiomeE 또는 다른 overstory cohort engine을 사용하면서 Regeneration library와 유사한 하층 구조를 새로 결합하면 그것은 새로운 coupling이다.

## 근거
https://capsis.cirad.fr/capsis/help_en/rreshar
https://capsis.cirad.fr/
