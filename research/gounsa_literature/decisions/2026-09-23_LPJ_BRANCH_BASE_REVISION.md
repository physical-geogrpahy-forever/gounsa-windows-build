# Decision: LPJ-GUESS implementation base revision

Date: 2026-09-23
Status: PROVISIONAL IMPLEMENTATION BASE, TO BE LOCKED AFTER BUILD/REGRESSION TEST

## Decision

고운사 LPJ-GUESS 결합버전은 **SEC 논문의 LPJ-GUESS revision 13221을 소스 기준선으로 두고, LPJ-GUESS-RE의 Richards-equation soil hydrology를 그 위로 forward-port하는 방향**으로 진행한다.

즉 다음 방식이다.

```text
LPJ-GUESS SEC revision 13221
        |
        +-- keep SEC canopy / cohort-light modifications
        |
        +-- port LPJ-GUESS-RE soil-water changes
        |      - Richards equation
        |      - configurable layer thickness
        |      - variable total soil depth
        |      - bedrock / free drainage / aquifer BC
        |
        +-- add Gounsa state adapter
               - vegetation export
               - event hydro-geomorph takeover
               - conservative soil/root/C/N remapping
               - restart write-back
```

## Why SEC r13221 is the better base than RE r10118

### 1. RE v1.0 is based on an older LPJ-GUESS revision

The archived LPJ-GUESS-RE v1.0 code is based on LPJ-GUESS v4.1.1 revision 10118.

The Zenodo archive itself states that, unless reproducing the RE paper exactly, users should use the latest LPJ-GUESS release as a basis in order to obtain newer developments and bug fixes.

### 2. SEC is newer and directly addresses the Gounsa vegetation problem

Stoebke et al. (2026) explicitly identifies the model as LPJ-GUESS revision 13221 and adds the spatially-explicit canopy (SEC) scheme.

For Gounsa, SEC is directly valuable because it preserves canopy gaps and improves the representation of forest-floor light, understory vegetation and regeneration after tree mortality/disturbance.

### 3. The RE authors explicitly state that the hydrology code is portable

Verbruggen et al. (2025) state that the new model code is relatively simple and easy to transfer to other LPJ-GUESS branches. They also foresee merging RE with other LPJ-GUESS developments.

Therefore the technically cleaner direction is:

```text
newer vegetation/canopy branch
 <- port relatively self-contained RE hydrology
```

rather than:

```text
older RE branch r10118
 <- backport all later SEC/canopy changes
```

## Important qualification

This is an **engineering decision for the Gounsa model**, not a published LPJ-GUESS release.

The following combined model does not currently have a published single-version citation:

```text
SEC r13221 + LPJ-GUESS-RE + Gounsa geomorph coupling
```

It must always be described as a custom merged/coupled branch with separate citations for SEC and RE.

## Merge-risk expectation

Previous branch audit judged SEC + RE as low-to-moderate conflict because:

- SEC primarily changes canopy geometry, light competition and establishment-related structures.
- RE primarily changes soil hydrology, soil layer geometry and lower boundary conditions.

However, overlap can still occur through:

- soil-layer constants and root uptake
- water-stress state
- serialized `Soil` state
- instruction-file parameters
- output modules
- build-time constants

Therefore `low-to-moderate conflict` is a hypothesis to test, not a guarantee.

## Required gate before final branch lock

Revision 13221 remains the provisional base until all of the following pass.

1. SEC r13221 reproduces its reference/basic test without RE changes.
2. RE hydrology can be ported and compiled without disabling SEC.
3. Default/free-drainage simulation runs through spinup and transient phases.
4. Shallow-soil + bedrock test runs without water mass-balance failure.
5. SEC gap/regeneration behaviour remains active after RE port.
6. restart serialize/read/write round trip works for the merged `Soil` and vegetation state.
7. synthetic 0.10 m erosion remap conserves declared water, C and N mass.
8. no silent mismatch exists between adapter serialization schema and executable revision.

After these tests, the exact merge commit SHA becomes the permanent Gounsa LPJ-GUESS baseline.

## RE computational implication

Verbruggen et al. report from experience that RE hydrology is roughly five times slower than the default LPJ-GUESS hydrology, with still larger cost for the aquifer boundary condition.

For Gounsa this supports:

- use `bedrock` rather than `aquifer` as the first shallow-soil baseline
- avoid full groundwater complexity unless field evidence requires it
- keep event hydrology external rather than attempting to resolve all storm geomorphology inside LPJ-GUESS

## Source versions

### SEC

- Stoebke et al. (2026)
- LPJ-GUESS revision: 13221
- code archive: Zenodo DOI 10.5281/zenodo.18133363
- role: canopy structure, persistent gaps, understory light, regeneration

### LPJ-GUESS-RE

- Verbruggen et al. (2025)
- archived basis: LPJ-GUESS v4.1.1 revision 10118
- RE archive: Zenodo DOI 10.5281/zenodo.15024130
- role: Richards-equation vertical soil-water movement, configurable layers, variable soil depth, bedrock/free-drainage/aquifer bottom BC

## Final current statement

**Implementation base: SEC r13221.**

**Hydrology strategy: forward-port LPJ-GUESS-RE onto that base.**

**Final production revision: not yet locked until compile, regression, restart and mass-balance tests pass.**

## Related records

- `decisions/2026-09-23_LPJ_GUESS_BASELINE_LOCK.md`
- `models/LPJ_GUESS_BRANCH_MERGE_AUDIT_2026.md`
- `models/LPJ_GUESS_STATE_ADAPTER_AUDIT_2026.md`
- `models/LPJ_GUESS_GEOMORPH_VARIABLE_INTERFACE.md`
- `papers/2025_Verbruggen_LPJ_GUESS_RE.md`
- `papers/2026_Stoebke_LPJ_GUESS_SEC.md`
