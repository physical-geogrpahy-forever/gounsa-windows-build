# 2026-10-26 EUROSEM 원본 유사수지 핵심 진전 인계

## 사용자 의도
기존 LAI/COVER 민감도 작아 탈락시킨 EUROSEM 1998 원본과 2026-10-25 실험 포크의 입력 및 계산 오류를 다시 감사한 다음, 원본 세류/세류간 침식 유사수지 보존을 정밀 검증. 연결 문제 때문에 분할 진행함. 사용자 필수조건은 LAI 등의 정량 식생 상태로 실제 수관저류/수관통과/적하를 변환하고 직접 지표유출에 의한 침식, 산지/급경사지, 진정한 2D 구조, 안정성이다.

## 이전 채팅에서 이미 한 일
- 729회 LIBRARY CSV 원자료 직접 재분석 및 원래 LAI patch code 복구. 원본 1998 LAI parameter native 부재, past LAI.PAR experimental extension and H3cm leafdrip KE suppression identified.
- Original `eurseml.for` duplicated DRIPD/RAIN factor in kinetic vs DRIPS. Original and fork run actual 20 +8 comparisons, in-source RDET increased 9× when EROD ×9 but delivered sediment unchanged. Transport dominated test.
- Original Fortran 12 dt (15/30/60sec) water QA: nonrilled 1D reported net erosion converges within about 0.3% for finer pair.
- Full original source audit decision at `decisions/2026-10-26_EUROSEM_729_LOW_VEGETATION_SENSITIVITY_ROOT_CAUSE_REAUDIT.md`.

## THIS turn essential new experimental findings
1. Rediscovered `TheSoilman/EUROSEM/eplanel.for` L873–924 native sediment balances: `inrlbal=sumqirr+sumdir+suspir`; `rillbal=stout+sumdrl+susprl-sedin`. Explicit sources/soil stock and suspension states exist but field flux ledger unvalidated. Earlier summary 'original has no sediment budget' inaccurate.
2. NEW observed-step high precision Fortran diagnostics and independent boundary `∑0.5(Qnow*Cnow+Qprev*Cprev)dt` check. 24 native runs, 30/50mmh,dt60/30/15s, MCODE0/1, rills off/on. [native GitHub run 40326142263](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40326142263). 24/24 model execution and hydro QA PASS. 24/24 independently computed outlet integrated sediment matches original `SEDTOT/rho/1000` to <0.00003% relative. **Original sediment budget <0.1%: no-rills 9/12 PASS, rills 0/12 PASS**.
3. 15-sec most decisive results for rill-on **combined full-slope physical budget** (in m3, relative to outlet): rain30 Govers outlet24.79910 residual−3.55178=14.32%, Everaert outlet26.74136 residual−5.74281=21.48%; rain50 Govers outlet123.92093 residual−21.05008=16.99%, Everaert outlet133.16624 residual−27.29938=20.50%. At 15sec no-rills all four have <0.03% relative residual.
4. 24 additional original code cases logged `QLRAV,CLAT,XL,DEPNO,DT` passed to native `eusedl::SEDCOM` after interrill, and Python independently integrated rill lateral sediment in. [native run 40326648315](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40326648315). 15sec rills interrill export vs rill admitted: 30 Govers11.80246 vs11.79962, 30 Everaert18.96229 vs18.96267, 50 Govers70.11043 vs70.10292, 50 Everaert90.78222 vs90.78481 m3. These match near 0.003%-0.024%. **NOT an upstream interrill-rill transfer leak**; likely inside rill phase DLA/DRLNET/bed morphology or untracked store/balance accounting.
5. "Workflow succeeded" here refers actual 24 native Fortran runs; physically rilled cases fail stated conservation criterion. Do not conflate process exit with mass QA.

## Saved canonical files
- New `decisions/2026-10-26_EUROSEM_1998_NATIVE_SEDIMENT_LEDGER_RILL_FAILURE.md` -- exact data and code correspondence.
- Updated `models/EUROSEM.md`, `MASTER.md`, `decisions/2026-10-26_EUROSEM_729_LOW_VEGETATION_SENSITIVITY_ROOT_CAUSE_REAUDIT.md`.
- Source diagnostic branch `swehr-water-sediment-closure-20261026`, `experiments/rainfall_10_50/verify_eurosem_reaudit_20261026.py`, `run_eurosem_sediment_ledger_20261026.py`, `.github/workflows/eurosem_original_sediment_mass_ledger_20261026.yml`.
- Exact raw output and machine-readable CSV/JSON from GitHub Actions run artifacts at 40326142263 and 40326648315. Sandbox paths **must not be inferred** from those artifact names.

## Recommendation for next concrete source audit
Inspect `eusedl.for::SEDCOM` LCH=1 `DLA` calculation and `eplanel.for::RILLWI` rill-profile evolution, and if needed instrument *each timestep's* actual rill bed original solid volume change and entire suspended sediment concentration/storage; isolate missing/unrecorded store vs source term nonconservation. Do not fix rill balancing with an empirical subtraction. If valid fix found, label patched fork, rerun 24-case same mass+dt verification; model still genuine 1D not required 2D. Given user '의심이 되면 버려', do not promote EUROSEM to original working rilled Gounsa model.
