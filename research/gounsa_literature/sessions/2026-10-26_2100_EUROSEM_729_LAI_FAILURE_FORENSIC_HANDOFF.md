# 고운사 EUROSEM 1998 이전 식생 민감도 무반응 729회 forensic 2026-10-26 인계

## 사용자 지시
“차이 적어서 버린 모델이라도 가져와 철저히 뜯어봐서 이전 시도가 잘못된 게 아닌지 확인” → 2025년 EUROSEM 729개 full factorial actual CSV와 exact input/code provenance 복구 후 동일 Fortran full native 24+24 비교와 내부 소스 플럭스 계측.

## 오늘 실제 복구/발견
- Library `three_erosion_parameters_total_729_runs.csv` 729×23 columns, `요인별_민감도_분석보고서.md` 파일 materialize; 243 EROD factorial rain30 cover0.1/0.5/0.9 marginal sediment 14.42172/14.40374/14.40373t/ha; rain50 83.85269/83.85225/83.85225.
- Historical GitHub `eurosem-single-model-lai-20261025/eurosem_lai_1998/patch_interception.py` custom LAI.FOR branch: `SCAP=.20*LAI`, `SKLAI=min(COVER,.046*LAI)`; for LAI2.5 COVER 0.5/.9 identical k=.115, effective rain equal.
- Native 1998 input `PLANTH` centimetres not m; old 3 used as 3cm and zero leafdrip energy (threshold ~13.8cm). Previous 2026-10-26 readjustment was found in `decisions/2026-10-26_OAK_MISCANTHUS_REAUDIT.md`, now verified pertinent to factorial.
- `MCODE=1` 1998 original test.par is Everaert, `MCODE=0` Govers; old test summaries had incorrect labels.
- `KINET` and `DRIPS`: `DRIPKE=KE_LD*(DRIPD/RAIN)`; `DMMSEC=RMMSEC*(DRIPD/RAIN)`; `DRDTIN=DRIPKE*DMMSEC*...` => fraction² in leaf-drip source. Original-paper equivalence not assumed, candidate code inconsistency.
- Real new GNU Fortran original source SHA 8652944da6e1e8436495aa0c08765e2399830dd7 **24/24 executed** in new branch `eurosem-forensic-audit-20261026`, flow/sediment unchanged except previous LAI.PAR fork and observation-only WRITE. COVER(.1,.5,.9), H3/150cm, EROD(.1,.9), MCODE(0,1). Plant H correct increased leaf KE 0→2.779 at C=.5, but first-element source reported net ~37,830kg unchanged; EROD×9 hardly alters; MCODE0 vs1 +16.4%. [actions 40319063481](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40319063481).
- 12 original vs diagnostic 1-line `DMMSEC=RMMSEC` source pairs 24/24 executed; 8 splash sample observations each show actual leafdrop source rises ×28.12(C.1), ×4.85(C.5), ×2.65(C.9), first-element reported net same to output .001kg. Modified fork is NOT original. [actions 40319799767](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40319799767).
- New `eusedl.for` observation WRITE at `SUP=DTRC-CT*DTRF` shows actual native EROD=.1 MCODE0/1 8 sample mean `RDET=3.10e-9`, `DTRF*CEX=.0015925/.0019420`, ratio 5.13×10^5 / 6.26×10^5. EROD=.9 instrumented two cases incomplete (4 samples, no first plane net output) despite program rc0; **do not use** for claimed success or source magnitude. [actions 40320553800](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40320553800).
- 729 cases independently closed only WATER, **NO sediment full ledger**, no validation of 2D site soil erosion (EUROSEM still 1D cascaded element).

## Canonical writing completed this session
- decision: `decisions/2026-10-26_EUROSEM_PREVIOUS_LOW_VEGETATION_SENSITIVITY_FORENSIC.md`
- model: `models/EUROSEM.md` appended
- old re-audit `decisions/2026-10-26_OAK_MISCANTHUS_REAUDIT.md` appended cross-reference
- `MASTER.md` top new corrected model decision
- New Github experimental branch `eurosem-forensic-audit-20261026`; scripts `eurosem_lai_1998/forensic_native_20261026.py`, `forensic_drip_single_fraction_20261026.py`, `forensic_capacity_flux_20261026.py`; 3 workflows; all native successful complete runs archived as Actions artifacts.

## Scientific conclusion
**Wrong previous test interpretation** → past small slope/plant/LAI effect is not evidence of useless EUROSEM canopy source; exact modified input k saturation and height centimeters flaw, native doubled drop partition discovered. In the investigated 30mm/h sample, actual sediment output still insensitive because transport-capacity related source dominates rain-source in probed cells. However no independent sediment closure, unreal site conditions/DERO=5m, 1D not true2D and no spatial stem SF, **do not promote as full Gounsa engine**. Valuable canopy/drip/rain source **as a component subject to correction and validation**, not a completed production model.

## Next true blockers
1. Instrumented EROD=.9 flux probe incomplete; diagnose (native nonzero EXIT? static file absent) if using source-level contribution beyond .1; do not silently count.
2. Actually compute independent eroded soil vs transported out boundary sediment mass ledger, check 1D bed storage and finite soil depth.
3. If aiming full Gounsa: source-verifiable genuine2D SWE 2D sediment stable QA separately; any new EUROSEM coupled interface is **new** not original model.
