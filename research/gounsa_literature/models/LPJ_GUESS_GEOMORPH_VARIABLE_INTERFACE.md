# LPJ-GUESS -> Gounsa geomorphology variable interface

Updated: 2026-09-23
Status: CURRENT IMPLEMENTATION SPECIFICATION

## 1. Purpose

이 문서는 LPJ-GUESS를 고운사 식생 엔진으로 고정했을 때 외부 수문, 침식, 사면수송, 풍화 모듈과 실제로 어떤 상태량을 주고받을지를 정의한다.

핵심 원칙은 다음과 같다.

- vegetation cover 하나로 식생효과를 통합하지 않는다.
- PFT/cohort별 기관 탄소풀과 뿌리 분포를 가능한 한 보존한다.
- LPJ-GUESS 내부 상태와 표준 출력파일을 구분한다.
- 사건 후 토심 변화는 단순 parameter change가 아니라 state remapping 문제로 처리한다.
- 논문에 없는 변환은 모두 새로운 coupling으로 표시한다.

## 2. 확인된 LPJ-GUESS 상태 및 출력 구조

PEcAn의 현재 LPJ-GUESS interface는 binary state에서 PFT별 변수를 읽을 수 있으며, `biomass`를 다음 합으로 정의한다.

```text
cmass_leaf + cmass_root + cmass_sap + cmass_heart
```

PEcAn 문서는 state의 carbon mass 단위가 보통 `kg C m-2`라고 명시하고, above-ground wood target도 `kgC m-2`를 사용한다. 따라서 고운사 adapter에서는 내부 변수의 실제 단위를 branch별로 source/output module에서 다시 확인한 후 동일 단위를 명시적으로 보존한다.

표준 LPJ-GUESS output에서는 최소한 annual `cmass`, `anpp`, `lai`, `dens`, carbon pool 및 monthly `mnpp`, `mlai`, evapotranspiration, runoff, interception, soil water 관련 출력이 존재한다. 그러나 고운사 결합에는 standard aggregate output만으로 부족하므로 state reader 또는 custom output을 사용해 PFT/cohort 수준 상태를 직접 추출하는 것을 기본으로 한다.

## 3. LPJ-GUESS -> geomorphology 필수 변수

| 변수 | LPJ-GUESS 의미 | 공간/생물 수준 | 기본 시간성 | 추출 경로 | 고운사 사용 | 판정 |
|---|---|---|---|---|---|---|
| `cmass_root` | live fine-root C | individual/cohort/PFT state, 필요시 patch/gridcell 집계 | 지속 상태, allocation/turnover에 의해 갱신 | state/custom output | root mass, RLD/RSAD 변환, erosion resistance, root bioturbation | 필수 |
| `cmass_leaf` | leaf C | cohort/PFT | 지속 상태 | state/custom output | canopy biomass, litter source, fire mortality | 필수 |
| `cmass_sap` | sapwood C | tree cohort/PFT | 지속 상태 | state/custom output | woody biomass, allometry, tree-throw/CWD 후보 | 필수 |
| `cmass_heart` | heartwood C | tree cohort/PFT | 지속 상태 | state/custom output | woody biomass, allometry, tree-throw/CWD 후보 | 필수 |
| LAI | leaf area index | PFT/stand aggregate 가능 | daily state, annual/monthly output 가능 | `file_lai`, `file_mlai`, custom | interception, canopy shielding, radiation, understory diagnostics | 필수 |
| tree density | stems/area | cohort/PFT | demography에 의해 갱신 | `file_dens` 또는 state | tree throw event frequency, stand structure | 필수 |
| height | cohort tree height | tree cohort | 지속 state | state/custom output | canopy structure, tree throw geometry | 필수 |
| crown area | cohort/individual crown geometry | tree cohort | 지속 state | state/custom output | SEC canopy gap, interception geometry, tree fall footprint 후보 | 권장 |
| `rootdist[k]` | soil layer k의 root fraction parameter | PFT parameter | PFT parameter | instruction/PFT parameters | FineRootC의 초기 layer allocation | 필수 |
| `turnover_root` | annual fine-root turnover fraction | PFT parameter | 연 비율 | PFT parameter | dead-root input rate | 필수 |
| `turnover_leaf` | annual leaf turnover fraction | PFT parameter | 연 비율 | PFT parameter | litter production | 권장 |
| NPP | net primary production | PFT/stand | daily accumulation, annual/monthly output | `file_anpp`, `file_mnpp`, state/custom | growth diagnostic, weathering coupling 후보 | 권장 |
| litter C pools | dead plant material | pool/PFT dependence | 지속 state | state/carbon pool outputs | surface protection, OM transport, decomposition | 필수 |
| soil C/N pools | soil biogeochemistry | soil layer/pool | 지속 state | state/custom | erosion/deposition remapping | 필수 |
| mineral N | plant-available N | soil layer | 지속 state | state/custom | erosion/deposition remapping and post-event vegetation | 필수 |
| soil water | water by soil layer | soil layer | daily/subdaily hydrology | RE state/custom | pre-event initial condition, post-event feedback | 필수 |
| soil water potential | hydraulic state by layer | soil layer | RE solver state | RE state/custom | plant water stress and post-event remap | 권장 |
| FPC/PFT cover | canopy/vegetation cover summary | PFT/stand | output state | standard/custom output | diagnostics and canopy summary only | 보조 |

### Important distinction

`cmass_root`, `rootdist`, RLD, RSAD, root cohesion은 서로 다른 변수다.

```text
cmass_root = live fine-root carbon mass
rootdist[k] = PFT별 상대적 토양층 분포 parameter
RLD = root length / soil volume
RSAD = root surface area / soil volume
root cohesion = mechanical reinforcement parameter/result
```

어느 것도 자동으로 다른 것과 동일하지 않다.

## 4. FineRootC -> layer root mass

초기 또는 사건 직전의 가장 단순한 layer allocation은 다음과 같이 둘 수 있다.

```math
C_{r,k} = C_{r,total} f_{r,k}
```

여기서

- `C_r,total`: `cmass_root`
- `f_r,k`: 해당 PFT의 soil layer k root fraction

단, 얕은 토심에서 LPJ-GUESS-RE가 남는 root fraction을 최하부 soil layer에 압축하는 동작은 고운사에서 그대로 수용하지 않는다. 침식으로 실제 토양이 사라진 경우 사라진 체적에 있던 roots도 함께 제거해야 한다.

## 5. FineRootC -> RLD/RSAD

이 변환은 LPJ-GUESS native process가 아니며 새로운 coupling이다.

필요한 별도 PFT parameter:

- root carbon fraction `f_C`
- specific root length `SRL`, m root per kg dry root
- 필요시 specific root surface area `SRSA`

건조 root biomass:

```math
B_{r,k} = C_{r,k} / f_C
```

RLD:

```math
RLD_k = (B_{r,k} SRL) / V_{soil,k}
```

RSAD:

```math
RSAD_k = (B_{r,k} SRSA) / V_{soil,k}
```

고운사에서는 PFT별 `f_C`, `SRL`, `SRSA`를 별도 문헌/현장자료로 parameterize해야 한다. 이 단계가 확인되지 않은 상태에서 `cmass_root -> RLD`를 직접 비례식 하나로 확정하지 않는다.

## 6. Geomorphology -> LPJ-GUESS 필수 반환 변수

| 반환 상태 | 이유 | 처리 |
|---|---|---|
| elevation | 장기 지형변화와 기후/공간 forcing 갱신 | GIS state 갱신 |
| local soil depth | rooting volume와 soil water storage 변화 | RE soil geometry 갱신 |
| layer thicknesses | variable-depth soil column | 15-layer geometry 재구성 또는 mapping |
| bedrock depth/bottom boundary | shallow sandstone soil 하부경계 | bedrock BC 갱신 |
| water mass/content by layer | event 이후 실제 수문상태 | conservative remap 후 state overwrite |
| soil C by layer/pool | eroded/deposited OM 보존 | conservative remap |
| soil N/mineral N | nutrient loss/deposition 보존 | conservative remap |
| live root C by layer | soil removal에 따른 root truncation | conservative remap + mortality |
| dead root/litter | damaged/removed roots와 aboveground litter | detrital pools transfer |
| soil texture/coarse fragments | 침식/퇴적/암편공급으로 변할 경우 | hydrology/erodibility parameter 갱신 |
| slope/contributing-area diagnostics | external geomorph/hydrology forcing | GIS sidecar state, LPJ native state로 강제하지 않음 |

## 7. Conservative soil-layer remapping

토심이 바뀌면 기존 layer index와 새 layer index를 단순 일대일 대응시키지 않는다.

old layer `i`와 new layer `j`의 깊이구간 겹침을 `L_ij`라 할 때, 면적당 extensive state `M_i`는 1차 근사에서 다음처럼 remap한다.

```math
M'_j = sum_i M_i (L_ij / Delta z_i) + S_j
```

여기서 `S_j`는 deposition 또는 외부 source다.

이 방식을 우선 적용할 extensive states:

- water mass
- soil organic C/N
- mineral N
- live root C
- dead root C

토양이 erosion으로 완전히 제거된 부분은 overlap이 0이므로 그 체적의 root와 soil pools도 자동으로 surviving column에서 사라진다. 제거된 질량은 sediment/export 또는 detrital routing으로 별도 회계한다.

### Why this matters

다음 처리는 금지한다.

```text
soil depth decreases
 -> remaining root fractions simply renormalized to sum 1
 -> total root biomass unchanged
```

이렇게 하면 침식으로 soil과 roots가 사라졌는데도 root biomass가 보존되는 비물리적 결과가 생긴다.

## 8. Event coupling clock

### LPJ clock

- photosynthesis, respiration, phenology, water/carbon fluxes: 주로 daily process
- allocation, establishment, mortality 등 demographic/growth processes: 주요 갱신이 annual scale

### Geomorph clock

- storm hydrology와 rill/interrill erosion: event 내부 sub-daily timestep
- 실제 timestep은 선택한 hydro-erosion engine의 CFL/solver 조건에 맡긴다.

### Synchronization

```text
start of day / pre-event
  -> export LPJ vegetation and soil state
storm begins
  -> freeze ordinary vegetation growth
  -> external hydrology owns event water state
  -> hydro-erosion and geomorphology
storm ends
  -> remap soil geometry + water + C/N + roots
  -> overwrite/update LPJ state
LPJ resumes
```

식생이 6시간 동안 성장하도록 만들 필요는 없다. 단, fire mortality, uprooting, burial, erosion-induced root loss처럼 사건 자체가 식생을 즉시 바꾸는 과정은 별도의 event operator로 처리한다.

## 9. Water-state ownership

### Phase 1 baseline

```text
non-event: LPJ-GUESS-RE owns vertical soil hydrology
event: external hydro-geomorph engine owns hydrological state
post-event: external state is remapped into LPJ-GUESS
```

### Phase 2 if needed

측방 지하수와 water table이 핵심으로 확인되면 PF-LPJG와 같이 외부 hydrology가 항상 water state를 소유하고 LPJ-GUESS 내부 soil moisture를 overwrite하는 구조로 확장한다.

Jia et al. (2026)은 ParFlow soil moisture가 LPJ-GUESS internal soil moisture를 overwrite하고, LPJ-GUESS가 ParFlow output을 24 timesteps, 즉 하루마다 읽는 구조를 구현했다. 이는 고운사 coupling의 가장 직접적인 published architectural precedent다.

## 10. SEC spatial interpretation

Stoebke et al. (2026)의 SEC는 cohort의 aggregated crown area에 patch 내부 위치를 부여하여 tree mortality로 생긴 canopy gap이 유지되도록 한다. 이는 하층식생과 재생을 표현하는 데 유리하다.

그러나 다음을 구분한다.

```text
SEC position inside LPJ patch != absolute GIS x-y coordinate
```

따라서 권장 계층은 다음과 같다.

```text
real GIS vegetation unit / hillslope element
   -> one LPJ-GUESS site/stand representation
      -> internal patches
         -> SEC canopy positions and cohorts
```

지형모델이 1-5 m cell을 사용하더라도 모든 geomorph cell마다 독립 LPJ-GUESS simulation을 강제하지 않는다. vegetation unit의 적절한 해상도는 계산량과 topographic heterogeneity를 함께 보고 별도 확정한다.

## 11. Standard output vs coupling state

### Standard output으로 충분한 것

- LAI trend
- total/PFT biomass diagnostics
- annual/monthly NPP
- density
- ecosystem C balance
- AET/interception/runoff diagnostics

### state/custom output이 필요한 것

- `cmass_root`, `cmass_leaf`, `cmass_sap`, `cmass_heart`의 cohort/PFT 수준 값
- height/crown area
- layer-specific live root mass
- RE layer water state/potential
- soil C/N/mineral N by layer for conservative remapping
- event 후 직접 state overwrite에 필요한 variables

## 12. Adapter implementation priorities

1. LPJ-GUESS branch/version을 고정한다.
2. binary state reader로 `cmass_*`, density, cohort geometry를 round-trip read/write할 수 있는지 시험한다.
3. RE soil layer geometry와 water state의 read/write 위치를 확인한다.
4. 단순 `soil depth -10 cm` synthetic test를 만든다.
5. water, soil C/N, root C mass balance를 전후 비교한다.
6. 그 뒤에 hydro-erosion engine을 연결한다.

가장 먼저 만들어야 할 검증은 복잡한 폭우 실험이 아니라 `토심만 인위적으로 줄였을 때 모든 state가 질량보존적으로 remap되는가`이다.

## 13. Unresolved parameters, not unresolved model choice

앞으로 필요한 검색은 전체 식생모델이 아니라 다음 parameter/coupling에 한정한다.

- Korean temperate forest PFT별 `SRL`, `SRSA`, root carbon fraction
- live/dead fine-root turnover after fire
- biomass/RLD -> `Ki`, `Kr` 변환의 최종식
- tree cohort -> tree throw probability and displaced soil volume
- litter/CWD -> surface shielding and sediment interaction
- NPP/root respiration/biomass -> weathering/soil production coupling
- shallow sandstone soil의 hydraulic parameters and coarse-fragment effects

## 14. References

- Smith, B. et al. (2001). Dynamic vegetation modelling: representing plant functional types and individual population dynamics in an ecosystem model. Journal of Vegetation Science.
- LPJ-GUESS Reference Manual, v4-era documentation. Standard annual/monthly outputs and PFT parameters including `rootdist`, `turnover_root`, `turnover_leaf`, `sla`, `ltor_max`.
- Verbruggen, W. et al. (2025). Implementing a process-based representation of soil water movement in a second-generation dynamic vegetation model: application to dryland ecosystems (LPJ-GUESS-RE v1.0). Geoscientific Model Development, 18, 6623-6645. https://doi.org/10.5194/gmd-18-6623-2025
- Jia, Z. et al. (2026). Advancing ecohydrological modelling: coupling LPJ-GUESS with ParFlow for integrated vegetation and surface-subsurface hydrology simulations. Geoscientific Model Development, 19, 1727-1747. https://doi.org/10.5194/gmd-19-1727-2026
- Stoebke, J. E. et al. (2026). Representing canopy structure dynamics within the LPJ-GUESS dynamic global vegetation model (revision 13221). Geoscientific Model Development, 19, 3595-3615. https://doi.org/10.5194/gmd-19-3595-2026
- PEcAn.LPJGUESS package documentation, functions `readStateBinary.LPJGUESS`, `calculateGridcellVariablePerPFT`, `updateState.LPJGUESS`, `write_restart.LPJGUESS`. Accessed 2026-09-23.

## 15. Related project records

- `decisions/2026-09-23_LPJ_GUESS_BASELINE_LOCK.md`
- `decisions/2026-09-21_LPJGUESS_BIOMASS_COUPLING.md`
- `models/LPJ_GUESS_SPATIAL_COHORT_SYNTHESIS.md`
- `models/LPJ_GUESS_BRANCH_MERGE_AUDIT_2026.md`
