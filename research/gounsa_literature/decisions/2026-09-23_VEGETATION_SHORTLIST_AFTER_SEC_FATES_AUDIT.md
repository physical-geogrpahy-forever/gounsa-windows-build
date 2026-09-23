# Vegetation shortlist after SEC, FATES grass and FORMIND source audits

Date: 2026-09-23

## 목적
고운사 postfire vegetation-geomorphology model의 식생엔진 후보를 다음 다섯 조건으로 다시 정리한다.

1. 실제 geographic/terrain unit과 연결 가능한 spatial cohort 또는 합리적으로 단순화된 individual/cohort hybrid
2. 초본, 관목, 교목 하층식생과 succession을 매우 명시적으로 고려
3. native dynamic soil depth가 아니라 **external soil/terrain state와 coupling 가능**할 것
4. hillslope/catchment/topography 적용 선례
5. physiology/ecohydrology timestep <= 1 day, preferably hourly/subhourly

---

# 핵심 결정 1: 아직 다섯 조건을 완벽히 만족하는 single ready-made published model은 확인되지 않음

검색을 넓힌 뒤에도 다음 trade-off가 유지된다.

- actual fine spatial forest models는 herb/shrub succession이 약한 경우가 많음
- rich succession models는 annual/monthly timestep인 경우가 많음
- fast demographic land models는 internal patches가 statistical인 경우가 많음
- terrain hydrology가 강한 models는 vegetation demography가 약한 경우가 많음

따라서 최종 선택은 `ready-made completeness`와 `coupling burden` 사이의 비교가 된다.

---

# 핵심 결정 2: LPJ-GUESS는 strongest development lineage로 승격

2026 SEC/PPA revision 13221로 인해 LPJ-GUESS의 기존 약점이었던 canopy spatiality와 recruitment-layer representation이 크게 개선되었다.

현재 LPJ-GUESS ecosystem에는 서로 다른 published branches로 다음 기능이 존재한다.

## SEC/PPA revision 13221
- age/size tree cohorts
- cohort crown area and persistent local gaps in SEC
- recruitment layer
- forest-floor herbaceous light environment
- shrubs/grasses coexist with tree PFTs in LPJ-GUESS ecology
- daily ecological/physiological processes

## LPJ-DH / LPJG-WHyMe-TFM
- actual 50 m Stordalen catchment
- DEM-derived lateral water routing
- tree/shrub/grass vegetation

## PF-LPJG 2026
- hourly ParFlow
- daily LPJ-GUESS
- ParFlow soil moisture overwrites LPJ state daily
- vegetation P-ET returned to hydrology
- 3-D surface/subsurface water flow

## LPJ-GUESS-RE
- 1-D Richards equation
- variable layer thickness / total soil depth
- bedrock/aquifer boundaries
- subdaily adaptive numerical solution

These are **not one published codebase**. Combining them is a new coupling/code merge.

### Important simplification
If Gounsa uses ParFlow or another external terrain/soil hydrology model, **LPJ-GUESS-RE does not have to be merged into the production code**.

PF-LPJG already demonstrates:
- external hydrology replacing internal LPJ soil-water/runoff
- variable soil-layer alignment
- layer-specific soil properties
- daily overwrite of LPJ soil moisture
- MPI-based synchronous exchange

Therefore the practical path can be reduced to:

```text
latest LPJ-GUESS SEC/PPA ecology
+
PF-LPJG-style external hydrology/state exchange
```

LPJ-GUESS-RE then serves as:
- alternative if LPJ itself must solve vertical soil water
- reference implementation for variable soil layer depth and Richards physics

This materially reduces integration burden.

---

# 핵심 결정 3: FATES criterion 2 is stronger than previously assessed

Gao et al. (2025) demonstrates that FATES grass is not prescribed ground cover.

FATES grass PFTs can:
- recruit repeatedly from seed
- grow as demographic vegetation
- compete for resources
- undergo phenology and drought mortality
- change biomass/fuel/litter state
- interact with SPITFIRE

Current FATES parameter infrastructure includes:
- tree PFTs
- shrub PFTs
- grass PFTs
- PFT-specific seed banks

Therefore FATES criterion 2 is **STRONG**.

Nuance:
- the detailed environmentally sensitive Tree Recruitment Scheme with explicit forest-floor seedling emergence/mortality is tree-focused
- grass/shrub demographic parameterization remains less mature than tree demography
- a published Korean/temperate full herb -> shrub -> tree postfire validation was not identified

FATES remains the strongest **ready mechanistic demographic cohort + explicit hillslope hydrology** precedent because ELM-FATES + ParFlow already exists.

Its main weakness is criterion 1 spatial interpretation:
- host grid/column is real x-y
- internal disturbance patches are spatially implicit area fractions

---

# 핵심 결정 4: FORMIND-mHM criterion 2 is now resolved downward

FORMIND itself is stronger than initially assumed:
- actual quadratic patches
- default cohort mode can aggregate same-type/same-size trees
- explicit woody seed/recruitment/gap succession
- daily GPP/water
- mHM distributed catchment coupling in 2026

However current source uses a type-dependent compile-time process branch of the form:

```cpp
if constexpr (isGrass<PlantWithTraitsType>) {
    // grass path
} else {
    // non-grass forest path
}
```

Therefore GRASSMIND being integrated into the FORMIND codebase does **not** demonstrate simultaneous tree cohorts + herbaceous demographic understory in one forest patch.

FORMIND-mHM is consequently:
- criterion 1: STRONG
- criterion 2: PARTIAL; woody strong, herb forest understory not native/proven
- criterion 3: VERY STRONG
- criterion 4: VERY STRONG
- criterion 5: STRONG

It remains a very strong secondary/conditional candidate but does not displace LPJ-GUESS, MEDFATE or FATES under the current criterion 2.

---

# Updated shortlist

| lineage | 1 spatial cohort | 2 understory succession | 3 external soil-terrain coupling | 4 terrain/catchment | 5 <= daily | role |
|---|---|---|---|---|---|---|
| **LPJ-GUESS SEC + PF-style coupling** | STRONG-PARTIAL: SEC cohort gaps inside real geographic cells | STRONG: tree/shrub/grass, recruitment layer, herb floor-light response | VERY STRONG by PF-LPJG precedent | VERY STRONG by LPJ-DH/PF-LPJG | daily ecology + hourly external hydro | **strongest development lineage; new code merge required** |
| **ELM-ParFlow-FATES** | PARTIAL: real host grid, statistical internal patches | **STRONG** tree/shrub/grass demography | **VERY STRONG** direct coupling | **VERY STRONG** 3-D hillslope precedent | half-hourly + daily demography | **strongest ready mechanistic coupled precedent** |
| **MEDFATE 5.x + medfateland 3.0** | **STRONG** actual geographic cells and cohorts | STRONG-PARTIAL: tree/shrub recruitment strong, herb recruitment incomplete | **VERY STRONG** external soil-domain option and state continuation | **VERY STRONG** connected watershed | daily, optional subdaily physiology | **easiest prototype / lowest coupling burden** |
| **FORMIND-mHM** | **STRONG** actual patches + cohort mode | PARTIAL: woody strong, same-patch herb demographic layer not proven | **VERY STRONG** | **VERY STRONG** | daily | strong secondary candidate |
| FireBGCv2 | STRONG hybrid | STRONG-PARTIAL guild understory | MODERATE | STRONG mountain catchment | daily | secondary benchmark |
| LandscapeDNDC/PSIM | STRONG landscape cohorts | PARTIAL, natural regeneration gap | STRONG | STRONG mountain | hourly | hourly benchmark |
| LM4.1 PPA | cohort STRONG, GIS spatiality partial | PARTIAL-STRONG tree/grass, shrub weak | STRONG | PARTIAL characteristic hillslope | 30 min + daily | demographic land comparator |
| LPJmL-FIT | 10 m individual/tree patch but terrain connectivity partial | STRONG-PARTIAL tree/grass, shrub weak | MODERATE | WEAK-PARTIAL | daily | secondary |
| ED2 | cohort STRONG, internal patches statistical | tree/grass strong; shrub/postfire understory less direct | STRONG local hydrology | PARTIAL basin applications, no equivalent fine lateral hillslope precedent found | subhourly | below FATES for Gounsa |
| FATE-HD | STRONG geographic age-PFG cohorts | **EXCELLENT** herb/shrub/tree | WEAK | STRONG mountain landscape | **FAIL annual** | criterion-2 benchmark only |
| ORCHIDEE-CAN-NHA | tree size cohorts | **WEAK** independent understory | STRONG | WEAK-PARTIAL | 30 min + daily | reject strict shortlist |

---

# Implementation implication for Gounsa

The three strongest practical routes now have distinct philosophies.

## Route A: LPJ-GUESS latest ecology + external hydrology
Best if the priority is:
- cohort rather than individual trees
- explicit tree/shrub/grass competition
- gap/recruitment dynamics
- ability to keep a relatively lightweight vegetation engine
- use an external geomorphic/hydrologic engine for terrain feedback

Main work:
- port PF-LPJG-style coupler/state exchange onto latest SEC branch
- preserve current SEC canopy/recruitment code
- map external soil layers/water state into LPJ root and soil state
- add event-driven conservative remapping for erosion/deposition

## Route B: ELM-ParFlow-FATES
Best if the priority is:
- maximum process completeness already demonstrated
- subdaily plant-soil-atmosphere exchange
- full demographic tree/shrub/grass ecology
- 3-D hillslope hydrology

Main cost:
- heavy model stack
- internal patches not literal geomorphic pixels
- substantial setup/HPC burden

## Route C: MEDFATE + medfateland
Best if the priority is:
- rapid implementable prototype
- actual GIS cells
- daily state editing
- R/terra/sf compatibility
- native watershed lateral flow and seed dispersal

Main work:
- herb recruitment/succession extension if early postfire herbs must be endogenous
- soil-layer state remapping after erosion/deposition
- Korean species parameters

---

# Software merge risk: current preliminary assessment

PF-LPJG paper identifies its main LPJ-side changes as:
1. soil layer discretization
2. layer-specific texture inputs
3. external soil-moisture overwrite
4. MPI coupler inserted in `framework.cpp`

SEC paper identifies its scientific changes around:
- cohort crown-area geometry
- canopy fPAR/light calculation
- persistent gaps
- light-dependent establishment/recruitment
- cohort canopy organization

These functional areas are largely different, which is encouraging.

However exact source conflicts cannot yet be claimed to be low because:
- PF-LPJG is based on LPJ-GUESS v4.0.1
- LPJ-GUESS-RE is based on v4.1.1 r10118
- SEC/PPA paper uses revision 13221
- the SEC archive has had restricted-version history and an exact source diff against PF-LPJG has not yet been completed

Therefore current engineering verdict:

**conceptual merge compatibility = high**

**actual code-merge difficulty = unresolved, likely moderate rather than trivial**

The preferable strategy is to port the comparatively narrow PF coupling interface forward into the latest SEC code, rather than back-port SEC into the old PF-LPJG v4.0.1 tree.

---

# Next research priority
1. identify exact LPJ source files touched by SEC/PPA and compare against PF-LPJG modifications
2. test whether latest LPJ branch can accept external variable-depth soil water without RE
3. quantify 10, 25 and 50 m runtime for SEC with reduced replicate patch count
4. verify Korean temperate shrub/herb PFT parameterization pathways
5. compare required custom coding between LPJ route and MEDFATE herb-recruitment extension
6. preserve FATES as the process-complete benchmark

## Related files
- `models/LPJ_GUESS_SPATIAL_COHORT_SYNTHESIS.md`
- `models/FATES.md`
- `models/MEDFATE_MEDFATELAND.md`
- `models/FORMIND_mHM_GRASSMIND.md`
- `papers/2026_Stoebke_LPJGUESS_CanopyStructure.md`
- `papers/2025_Gao_FATES_AnnualGrass.md`
- `papers/2022_Fang_FATES_ParFlow_Topography.md`
