# LPJ-GUESS state adapter audit for Gounsa

Updated: 2026-09-23
Status: IMPLEMENTATION PATH CONFIRMED, BRANCH-SPECIFIC WORK REQUIRED

## 1. Question

고운사 coupling에서 LPJ-GUESS의 biomass, cohort geometry, litter, soil water, soil C/N을 읽고 지형사건 후 수정하여 다시 LPJ-GUESS에 돌려줄 수 있는가?

현재 결론은 **가능하다.** 다만 SEC + LPJ-GUESS-RE를 합친 최종 branch의 binary serialization schema를 adapter가 이해하도록 추가 작업이 필요하다.

## 2. Direct code evidence from PEcAn.LPJGUESS

PEcAnProject의 현재 LPJ-GUESS interface에는 restart/state를 읽고 쓰는 코드가 이미 존재한다.

Relevant files:

- `models/lpjguess/R/read_state.R`
- `models/lpjguess/R/write_state.R`
- `models/lpjguess/R/read_restart.LPJGUESS.R`
- `models/lpjguess/R/write_restart.LPJGUESS.R`
- `models/lpjguess/R/calculateGridcellVariablePerPFT.LPJGUESS.R`

Repository:
https://github.com/PecanProject/pecan

### Current reader architecture

`read_binary_LPJGUESS()` reads:

- `params.ins`
- `meta.bin`
- `0.state`
- package copies of LPJ-GUESS serialization definitions such as `guess.VERSION.cpp`, `guess.VERSION.h`, `parameters.VERSION.h`

It parses `serialize(ArchiveStream& arch)` declarations, reads the binary file, and returns:

```text
state
pos_list
siz_list
```

`pos_list` stores byte positions and `siz_list` stores binary element sizes. This means the code is not limited to a fixed hand-written table of every vegetation variable.

Important implementation limitations in the current reader comments/code:

- natural vegetation focus
- cohort mode focus
- state reader currently expects one LPJ-GUESS process for a state file
- model-version serialization definitions must match the executable that produced the restart

## 3. Confirmed vegetation state fields

PEcAn's LPJ-GUESS state code explicitly documents/read-writes individual/cohort fields including:

| State field | Meaning | Unit in code comments | Gounsa role |
|---|---|---|---|
| `cmass_leaf` | leaf C biomass | kgC m-2 modelled area | canopy/litter/fire |
| `cmass_root` | fine-root C biomass | kgC m-2 modelled area | root coupling |
| `cmass_sap` | sapwood C biomass | kgC m-2 | woody biomass/tree throw |
| `cmass_heart` | heartwood C biomass | kgC m-2 | woody biomass/tree throw |
| `fpc` | foliar projective cover | fraction | canopy diagnostic |
| `fpar` | absorbed PAR fraction | fraction | canopy/understory diagnostic |
| `densindiv` | individual density over patch | indiv m-2 | stand structure/tree throw |
| `anpp` | accumulated NPP | kgC m-2 yr-1 | growth/weathering diagnostic |
| `aet` | actual evapotranspiration | mm d-1 | water diagnostic |
| `height` | plant height | m | allometry/tree throw |
| `crownarea` | plant crown area | m2 | SEC/canopy geometry |
| `boleht` | bottom of crown height | m | canopy geometry |
| `lai` | cohort/individual patch-level LAI | dimensionless area ratio | interception/canopy |
| `age` | cohort/individual age | yr | demography |
| `intercep` | interception today on patch basis | model water unit | storm initial-state diagnostic |

This confirms that the Gounsa coupling does not have to reconstruct tree structure from total biomass alone.

## 4. Confirmed PFT/patch litter and water-stress fields

PEcAn state code also exposes patch-PFT fields including:

- `litter_leaf`, kgC m-2
- `litter_root`, kgC m-2
- `litter_sap`, kgC m-2
- `litter_heart`, kgC m-2
- nitrogen litter counterparts, kgN m-2
- `wscal`
- `phen`
- `nsapling`
- `gcbase_day`
- `wsupply`
- `fwuptake`
- `wstress_day`

This is important because high-level standard LPJ output is not the only route. The restart state already contains much of what the event coupling needs.

## 5. Confirmed soil biogeochemical state

Legacy/current PEcAn parsing code demonstrates restart fields for:

- soil water state
- runoff
- soil temperature
- fast/slow soil organic carbon pools
- 12 SOM pools with `cmass` in kgC m-2
- SOM `nmass` in kgN m-2
- available mineral nitrogen `nmass_avail` in kgN m-2
- daily decomposition and leaching-related states

Therefore an erosion/deposition operator can in principle remap not only soil depth and water but also soil C/N and mineral N.

## 6. Important version caveat: legacy soil schema != LPJ-GUESS-RE soil schema

The older hand-written PEcAn state reader shows two-layer soil arrays in places such as `Soil$wcont`. This must **not** be copied directly into the Gounsa implementation.

LPJ-GUESS-RE has:

- adjustable soil layer thickness
- 15-layer default structure
- layer-specific `theta`
- layer-specific `psi`
- layer-specific hydraulic conductivity
- Richards-equation state
- free-drainage, bedrock or aquifer lower boundary

Hence the final Gounsa adapter must be generated/validated against the actual SEC + RE source branch and its serialization order.

## 7. Writer capability

PEcAn `write_state.R` provides two useful patterns.

### Fixed-schema in-place writer

`write_binary_LPJGUESS()`:

1. copies the original `0.state`
2. uses stored byte positions and element sizes
3. seeks to each position
4. overwrites the updated state value
5. atomically replaces the state file

This is suitable when state structure and cohort count do not change.

### Flexible writer

`write_binary_LPJGUESS_flexible()` is explicitly documented as:

> Write LPJ-GUESS binary state allowing cohort count changes

It rebuilds the state stream when the number of individuals/cohorts changes.

This is important for fire mortality, recruitment, tree loss or other events that may alter cohort count.

## 8. Recommended Gounsa implementation strategy

Do not start by modifying core LPJ-GUESS vegetation equations.

Create a separate adapter layer:

```text
LPJ restart/state
   |
   v
Gounsa State Adapter
   |
   +-- export vegetation state
   +-- export soil state
   |
   v
storm hydro-geomorph model
   |
   v
conservative remap operator
   |
   +-- update soil geometry
   +-- update water
   +-- update soil C/N
   +-- truncate/remap live roots
   +-- update dead roots/litter
   +-- apply explicit vegetation mortality if needed
   |
   v
LPJ restart writer
   |
   v
LPJ-GUESS resumes
```

PEcAn is best treated as an implementation precedent and possibly reusable parser/writer code, not as a requirement that the full PEcAn workflow be adopted.

## 9. First synthetic test

Before coupling any real rainfall model, implement this deterministic test.

### Initial state

- a single LPJ vegetation unit
- known soil depth
- known layer water mass
- known soil C/N
- known `cmass_root`

### Artificial event

```text
remove top 0.10 m soil
```

### Expected checks

1. new total soil depth decreases exactly 0.10 m
2. water removed from the lost volume is accounted as export or event flux
3. soil C and N in lost material are accounted
4. root C in removed material is lost/transferred, not renormalized back into the surviving soil
5. surviving state is written to a restart file
6. LPJ-GUESS can restart successfully
7. no negative state variables
8. C, N and water mass-balance residuals are machine/rounding scale apart from declared exports

Only after this passes should the real storm erosion model be connected.

## 10. Second synthetic test

```text
deposit 0.05 m sediment
```

Need test two conceptual options separately:

- new sediment begins with no live roots and specified water/C/N
- burial mortality is imposed on roots/seedlings according to an explicit rule

Do not automatically extend existing root distribution into newly deposited sediment at the instant of deposition.

## 11. Branch-lock requirement

Before production coding, record exact:

- LPJ-GUESS base revision
- SEC revision/source
- LPJ-GUESS-RE revision/source
- merge commit
- serialization schema version

Any restart adapter must reject a state file produced by an unknown/incompatible schema rather than silently reading incorrect byte positions.

## 12. Current verdict

**The restart-state coupling path is technically credible and already has strong software precedent.**

The main unresolved engineering problem is not whether LPJ-GUESS exposes enough vegetation state. It does. The real work is:

1. merge/choose SEC + RE branch cleanly
2. add RE layer state to the adapter schema
3. implement conservative soil-layer remapping
4. verify restart round-trip

This substantially lowers the need to search for another vegetation model.

## Sources

- PEcAnProject/pecan, `models/lpjguess/R/read_state.R`, accessed 2026-09-23.
- PEcAnProject/pecan, `models/lpjguess/R/write_state.R`, accessed 2026-09-23.
- PEcAnProject/pecan, `models/lpjguess/R/write_restart.LPJGUESS.R`, accessed 2026-09-23.
- PEcAnProject/pecan, LPJ-GUESS state documentation and per-PFT calculation utilities, accessed 2026-09-23.
- Verbruggen et al. (2025), https://doi.org/10.5194/gmd-18-6623-2025
- Jia et al. (2026), https://doi.org/10.5194/gmd-19-1727-2026
- Stoebke et al. (2026), https://doi.org/10.5194/gmd-19-3595-2026

## Related project records

- `decisions/2026-09-23_LPJ_GUESS_BASELINE_LOCK.md`
- `models/LPJ_GUESS_GEOMORPH_VARIABLE_INTERFACE.md`
- `models/LPJ_GUESS_SPATIAL_COHORT_SYNTHESIS.md`
- `models/LPJ_GUESS_BRANCH_MERGE_AUDIT_2026.md`
