# Decision: LPJ-GUESS baseline lock for Gounsa

Date: 2026-09-23
Status: ACCEPTED CURRENT BASELINE

## Decision

고운사 연구의 식생모델 광범위 탐색은 여기서 종료한다. 새로운 전체 식생모델을 계속 비교하는 대신 LPJ-GUESS 계열을 식생 엔진의 기준선으로 고정하고, 고운사에 필요한 지형 및 사건 규모 과정은 외부 모듈과 명시적으로 결합한다.

이 결정은 `LPJ-GUESS가 모든 과정을 단독으로 해결한다`는 뜻이 아니다. 오히려 역할을 분리한다.

- 식생 경쟁, 천이, 탄소배분, 잎/세근/목질부 biomass, LAI, litter, PFT/cohort demography: LPJ-GUESS
- 얕은 토심과 수직 토양수분: LPJ-GUESS-RE 계열의 variable-depth soil / bedrock 구조를 우선 활용
- 수관공극과 하층식생 광환경: SEC를 우선 검토
- 폭우 중 시간 이하 수문, overland flow, rill/interrill erosion, deposition: 외부 event hydrology / geomorphology engine
- root-driven soil transport, dry ravel, shallow landslide, soil production/weathering, fire-spall: 별도 published process modules

## Baseline architecture

현재 1차 구현 기준선은 다음과 같다.

```text
GIS vegetation unit / hillslope element
        |
        v
LPJ-GUESS + SEC canopy
        |
        +-- LPJ-GUESS-RE-style variable soil depth / bedrock
        |
        v
pre-event vegetation + soil state
        |
        v
external event hydrology / erosion / geomorphology
        |
        v
conservative state remapping
        |
        v
LPJ-GUESS resumes
```

SEC와 LPJ-GUESS-RE는 서로 다른 published branches/developments이므로 둘을 합친 고운사 버전은 새로운 coupling/merge이다. published single model인 것처럼 기술하지 않는다.

## Single water-state authority rule

LPJ-GUESS-RE와 외부 폭우 수문모델이 동일한 시간구간의 토양수분을 독립적으로 동시에 계산하도록 두지 않는다.

### Background/non-event interval

- LPJ-GUESS-RE가 수직 토양수분과 식물 수분이용을 계산할 수 있다.

### Storm/event interval

- 외부 event hydrology/geomorphology engine이 강우, 침투, 지표유출, 필요시 측방/지하 흐름의 물 상태를 소유한다.
- LPJ-GUESS의 식생 구조와 biomass는 사건 중 기본적으로 고정된 경계조건으로 사용한다.
- 사건 종료 후 외부 모듈이 계산한 토양수분 상태를 LPJ-GUESS에 다시 기록한다.

이 원칙은 Jia et al. (2026)의 PF-LPJG에서 ParFlow soil moisture가 LPJ-GUESS 내부 soil moisture를 overwrite하고, LPJ-GUESS가 하루 간격으로 ParFlow 상태를 읽는 published precedent와 일치한다. 다만 고운사에서 event-only takeover를 사용하는 것은 새로운 coupling이다.

## Why not full ParFlow first

PF-LPJG는 매우 강한 결합 선례지만 고운사 1차 구현에서 ParFlow를 필수 종속성으로 고정하지 않는다.

1. 고운사의 최우선 문제는 폭우에 따른 사면 침식과 토심 변화이며, 식생 demography 자체가 시간 단위로 계산될 필요는 없다.
2. full 3-D groundwater coupling은 구현 복잡도와 계산량이 크게 증가한다.
3. 먼저 event-scale hydrology + conservative state remapping으로 검증한 뒤, 측방 지하수와 water-table feedback이 결과에 지배적일 때 PF-LPJG형 상시 외부 수문 소유 방식으로 확장한다.

### Upgrade trigger to full external hydrology

다음 중 하나가 확인되면 PF-LPJG형 Route B를 재검토한다.

- lateral subsurface flow가 storm runoff/erosion을 지배
- water table depth가 식생 천이와 slope stability에 핵심
- LPJ-GUESS-RE 1-D vertical hydrology로 관측 토양수분 패턴을 재현하지 못함
- event takeover와 daily background hydrology 사이 상태 불연속이 검증오차의 주원인

## Event sequence

```text
1. LPJ-GUESS daily/pre-event state snapshot
2. vegetation state frozen for event-scale forcing
3. event hydrology substeps
4. interrill/rill erosion + deposition + other event geomorphology
5. soil-layer geometry update
6. conservative remap of water, C/N, live/dead roots, litter
7. updated state returned to LPJ-GUESS
8. daily/annual vegetation dynamics resume
```

산불이나 tree throw처럼 사건 자체가 즉시 식생을 파괴하는 경우에는 2와 6 사이에 explicit jump/mortality operator를 둔다.

## Non-negotiable coupling rules

1. `FineRootC`를 RLD 또는 root cohesion과 동일시하지 않는다.
2. `rootdist`는 토양층별 뿌리 비율 parameter이지 root biomass 자체가 아니다.
3. erosion으로 제거된 토양에 포함된 live roots를 먼저 물리적으로 제거한 뒤 surviving roots를 새 토양층에 remap한다. 단순 재정규화로 뿌리 질량을 보존해서는 안 된다.
4. water, soil C/N, mineral N, live roots, dead roots/litter는 토심 변화 시 가능한 한 mass-conservative overlap remapping을 사용한다.
5. standard LPJ-GUESS runoff는 event erosion forcing의 최종 runoff로 사용하지 않는다. event hydrology output이 그 역할을 가진다.
6. LPJ-GUESS patch를 곧바로 실제 GIS x-y cell과 동일시하지 않는다. 실제 spatial unit과 내부 patch/SEC 구조를 구분한다.

## Broad model search status

- HETEROFOR, iLand, ED2/EDv2, ECOTONE, LANDIS-II 등은 비교 참고로 유지한다.
- 이들 전체모델을 LPJ-GUESS와 다시 경쟁시키는 광범위 검색은 중단한다.
- 이후 새로운 모델 검색은 `현재 coupling에 치명적인 결손이 확인되었을 때 그 결손만 해결하는 기능 탐색`으로 제한한다.

## Primary references

- Verbruggen, W. et al. (2025). Implementing a process-based representation of soil water movement in a second-generation dynamic vegetation model: application to dryland ecosystems (LPJ-GUESS-RE v1.0). Geoscientific Model Development, 18, 6623-6645. https://doi.org/10.5194/gmd-18-6623-2025
- Jia, Z. et al. (2026). Advancing ecohydrological modelling: coupling LPJ-GUESS with ParFlow for integrated vegetation and surface-subsurface hydrology simulations. Geoscientific Model Development, 19, 1727-1747. https://doi.org/10.5194/gmd-19-1727-2026
- Stoebke, J. E. et al. (2026). Representing canopy structure dynamics within the LPJ-GUESS dynamic global vegetation model (revision 13221). Geoscientific Model Development, 19, 3595-3615. https://doi.org/10.5194/gmd-19-3595-2026

## Related project records

- `models/LPJ_GUESS_SPATIAL_COHORT_SYNTHESIS.md`
- `models/LPJ_GUESS_BRANCH_MERGE_AUDIT_2026.md`
- `decisions/2026-09-21_LPJGUESS_BIOMASS_COUPLING.md`
- `models/LPJ_GUESS_GEOMORPH_VARIABLE_INTERFACE.md`
