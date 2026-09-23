# 2026-09-23 vegetation shortlist update

이 문서는 `2026-09-23_STRICT_SPATIAL_COHORT_FIVE_CRITERIA.md` 이후의 추가 검토를 반영하며, 겹치는 항목에서는 이 문서를 최신 판정으로 우선한다.

## 사용자 고정 5조건
1. geographic cell/terrain unit에 연결 가능한 cohort 또는 간소화된 individual/cohort hybrid
2. herb/grass/shrub understory와 succession이 매우 명시적
3. native dynamic soil depth 자체보다 external soil/hydrology/geomorph state와 연결 가능성이 중요
4. catchment/hillslope/topography precedent
5. physiology/ecohydrology <= 1 day, preferably hourly/subhourly; demographic schedule은 별도 기록

## 이번 라운드의 중요 변경

### FATES 상승
FATES source audit에서 `mortality_disturbance_fraction=0`을 이용하면 ordinary cohort mortality는 유지하면서 mortality-driven disturbance patch creation을 억제할 수 있음을 확인했다.

Recruitment/seedbank는 patch fission과 별도 demographic process이다.

따라서 고운사처럼 이미 관측된 wildfire를 초기조건으로 넣고 이후 100년 recovery를 보는 구성에서는:
```text
1 GIS vegetation cell
 -> 1 host column
 -> approximately 1 persistent FATES patch
 -> multiple tree/shrub/grass cohorts
```
로 운용할 수 있다.

이는 native FATES의 spatially implicit internal patches 문제를 완전히 없애지는 않지만, 고운사의 cell-level geomorph coupling에서는 practical limitation을 크게 줄인다.

FATES의 grass는 prescribed cover가 아니다. 2025 annual-grass application에서 bare-ground recruitment, growth, drought mortality and fire/fuel feedback을 수행했다.

### JULES-RED 신규 top-tier 진입
Current JULES v8.1 contains RED as an official selectable demographic model.

RED has:
- PFT-specific mass classes
- reproduction allocation and seedling recruitment
- tree/shrub/grass competition hierarchy
- original experiment: 10 tree mass classes, 8 shrub classes, 1 grass class
- explicit bare-soil grass -> shrub -> tree succession demonstration

JULES provides:
- usually 30-60 min land-surface timestep
- dynamic vegetation call period permitted down to 1 day
- layered soil water and root-zone stress
- time-varying prescribed `sthuf` soil wetness by soil layer
- restart state including soil moisture and water table
- TOPMODEL and subdaily river routing catchment precedent
- root carbon and root litter by PFT

Main limitations:
- RED competition is simplified to seedling gap availability and a tree > shrub > grass hierarchy rather than multilayer PPA canopy competition
- grass is one mass class in the published configuration
- standard `dzsoil_io` layer thickness is domain-wide, so dynamic/spatial soil geometry is custom
- standard root output is PFT-total rather than demographic mass-class-specific

### ED2 downgrade
Current canonical ED2 source has temperate C3 grass and multiple temperate/conifer tree PFTs but **no canonical shrub PFT / no `is_shrub` machinery**.

Therefore ED2 is now a strong comparator, not a top-tier fit for explicit herb -> shrub -> tree postfire succession.

### FORMIND-mHM remains conditional but below shortlist
FORMIND has actual patches, default tree cohort aggregation, daily water/GPP and a direct mHM catchment coupling.

However current FORMIND/GRASSMIND implementation separates grass and non-grass template paths; shared codebase does not demonstrate concurrent forest tree + herbaceous understory demography in one patch.

### CABLE-POP reject
CABLE physiology is subdaily and POP has woody cohorts, but POP demography is annual and woody-focused. No explicit herb/shrub/tree succession comparable to the top candidates.

---

# Current serious shortlist

| lineage | spatial cohort interpretation | understory succession | soil/geomorph interface | topography/catchment | timestep | main unresolved issue |
|---|---|---|---|---|---|---|
| **FATES + ELM/ParFlow** | geographic host cell + demographic size cohorts; persistent-single-patch config reduces implicit-patch problem | **very strong** tree/shrub/grass recruitment and competition | **very strong 3A**, 3B custom | **direct 3-D hillslope precedent** | half-hourly biophysics, daily demography | heavy software stack; no cohort x-y positions |
| **LPJ-GUESS SEC/PPA + PF-LPJG-style coupling** | geographic cells + tree cohorts with within-patch crown/gap structure | **very strong** tree/shrub/grass; SEC adds explicit woody understory/forest-floor light | **very strong 3A** if PF-style external hydrology used; 3B custom | LPJ-DH 50 m catchment + PF-LPJG 3-D hydrology precedents | daily LPJ coupling, hourly external hydro; structural demography slower | requires merging newer SEC branch with older PF coupling branch |
| **JULES-RED** | geographic grid + mass cohorts; no internal x-y | **strong** grass/shrub/tree succession, but simplified gap hierarchy | **strong 3A** via prescribed layer soil water/restart; 3B custom | strong JULES TOPMODEL/river-routing lineage | 30-60 min LSM, dynamic vegetation call can be daily | simplified understory light; spatial soil-layer geometry fixed by default |
| **MEDFATE + medfateland** | actual GIS cells + tree/shrub/herb cohorts | **strong-partial**: tree/shrub recruitment complete; herb recruitment loop missing | **very strong and easiest** | direct connected watershed implementation | daily growth/water, subdaily hydraulics | endogenous herb recruitment/succession gap |

## Important: do not collapse the LPJ-GUESS branches into a published single model
The following are separate developments:
- LPJ-DH 50 m catchment routing
- PF-LPJG ParFlow coupling
- LPJ-GUESS-RE multilayer Richards soil
- SEC/PPA canopy cohort revision

Combining SEC/PPA with PF-LPJG-style hydrology is a **new code merge/coupling**, not an already published model.

## Biological 0-20 yr postfire comparison
If explicit early succession is weighted most heavily:

### FATES
- strongest complete demographic pathway among ready systems
- tree/shrub/grass PFTs
- seed bank/recruitment
- actual grass demographic application
- daily vegetation dynamics

### LPJ-GUESS SEC/PPA
- tree age cohorts + shrub/grass PFTs
- improved forest-floor light and persistent canopy gaps
- biologically strong, but exact latest branch + external hydrology combination must be built

### JULES-RED
- remarkably direct grass -> shrub -> tree succession demonstration
- woody mass classes computationally parsimonious
- simpler competition: seedling gap hierarchy rather than detailed canopy strata

### MEDFATE
- physiologically and spatially excellent
- tree/shrub succession strong
- existing herb cohorts grow and compete, but endogenous herb recruitment loop remains incomplete

## Current research priority
Do not return to broad model-name collection unless a candidate has a plausible chance to beat these four.

Next checks:
1. FATES computational and initialization feasibility at 25-50 m Gounsa vegetation cells
2. LPJ SEC/PPA + PF coupling source-merge feasibility and Korean PFT parameterization
3. JULES-RED suitability of simplified gap hierarchy for Korean postfire herb/shrub transition and mass-class-specific root reconstruction
4. MEDFATE minimal extension needed for herb seed/recruitment
5. identical coupling interface specification for all four so they can be compared by implementation burden and scientific completeness

## Supporting model files
- `models/FATES.md`
- `models/LPJ_GUESS_SPATIAL_COHORT_SYNTHESIS.md`
- `models/JULES_RED.md`
- `models/MEDFATE_MEDFATELAND.md`
- `models/ED2_EDv3.md`
- `models/FORMIND_mHM_GRASSMIND.md`
- `models/CABLE_POP.md`
