# EUROSEM 1998 원본과 2025년 LAI 확장: 식생 민감도 불변 결과에 대한 재현 및 코드 감사

작성: 2026-10-26. **사용자 문제제기:** 피복률/LAI 변화로 유사유출량 변화가 거의 없다는 이유로 버렸던 EUROSEM을 원본, 기존 입력/코드, 수치실험까지 재검증하여 **이전 시도가 잘못된 것인지** 구분한다. 이 기록은 기존 연구기록 및 새로운 원본 Fortran 전체실행에 기초한다.

## 핵심 재판정
1. **과거 729회 factorial 결과로 "원본 EUROSEM은 식생 효과가 본래 작다"라고 단정한 판단은 과도하다.** LAI는 본래 1998 원본 변수가 아니며 2025년 `LAI.PAR` 확장 포크였고, 피복률 포화, 잘못된 식생높이 단위, 수송능력식 설명 오류가 존재.
2. 실제 original `TheSoilman/EUROSEM` SHA `8652944da6e1e8436495aa0c08765e2399830dd7`, compiler compatibility+입력연결 초기화+관측용 쓰기, 2025년 기존 LAI 확장을 고정한 **24회 네이티브 전체 실행**과 **수관적하 식의 단 한 줄 진단 수정 원본 대 비교 24회**를 새로 완료했다. 심지어 식생높이를 150cm로 바꿔 KE_LD가 양수가 돼도 source-reported net erosion은 거의 불변이다. Native erosion result remains unattributed for physical validation: **independent sediment closure NOT performed**.
3. 원본 `KINET`+ `DRIPS`를 직접 대조하면 **수관적하 비율 `DRIPD/RAIN`을 2회 곱하는 계산**이 존재한다. 수정 포크 단 한 줄 A/B에서 internal leaf-drip detachment `DRDTIN`이 **2.65–28.12배** 커졌는데도 첫 요소 source-reported net erosion은 12쌍 전부 동일했다. 즉 이 원본 식 오류 **한 개만 고쳐서는 민감도 결핍이 해결되지 않음**.
4. 원본 간 `MCODE` 0 (Govers) ↔ 1 (Everaert) 바꾸면 고정 COVER=.5/height=150cm/EROD=.9에서 첫 요소 source-reported net 37,829.734kg ↔44,036.523kg, ~16.41% 차이. 즉 두 수송능력 알고리즘의 영향은 충분히 크다.
5. **고운사 주 엔진에 재선정하지 않는다**: 유사수지 미검증, 실제 완전 2D 유동/유사수송 아님, 1D 연결 사면요소/기부 수간유하우 평균화, root RLD/soil armour+Gounsa TLS rill representation 부재. 하지만 과거 식생 미민감도 **단독 이유**로 소스 프로세스 연구가 무가치하다고 버리는 결정은 정정한다. 역할은 원본 수관분배+잎에너지 독립 소스 검증용.

## 이전 729회 full factorial 정확한 원자료 복구 및 통계 재계산
사용자 Library 파일 `three_erosion_parameters_total_729_runs.csv` (106377 bytes, 729 rows×23 columns), `요인별_민감도_분석보고서.md` 원본을 직접 materialize한 후 pandas로 재집계.
- EROD factorial 243: rainfall10mm/h 총유사0, rain30 평균14.40973t/ha, rain50 평균83.85240t/ha.
- COVER 0.1/0.5/0.9 marginal rain30 = 14.42172 / 14.40374 / 14.40373t/ha; rain50 = 83.85269 /83.85225 /83.85225t/ha.
- LAI 1.0/2.5/4.0 rain30 marginal=15.29803/14.40108/13.53007t/ha; rain50=84.93897/83.85250/82.76573t/ha.
- EROD .1/.5/.9 marginal rain30/50 equal to six decimals; fixed 81 sample quadruples maximum difference across the three levels = 0.000005016t/ha.
- fixed LAI2.5, rain30, slope.3, EROD .5: cover0.1→0.5→0.9 free-throughfall=27→15→3mm, drip=1.067→6.185→11.303mm, stemflow=1.434→8.316→15.197mm, but net rain=29.501mm all and sediment outlet t/ha=12.982973→12.981208→12.981208.
- All source factorial plots are **synthetic**, not observed Miscanthus sinensis / oak sprouts Gounsa site. 729 full model exit0 and water max error 0.0376% do **not** establish independent eroded particle mass or finite soil stock.

## 2025년 LAI 확장이 COVER 응답을 제거한 기계적 이유
Historical GitHub experiment branch `eurosem-single-model-lai-20261025`, source `eurosem_lai_1998/patch_interception.py`: the original `INTERC` routine was modified conditionally when `LAI.PAR` exists:
`SCAP = max(0, SLEAF*LAI)`
`SKLAI = min(COVER, KLAI*LAI)`
`VEGSTO = SCAP*(1-exp(-SKLAI * cumulative_rain / SCAP))`.
Example `SLEAF=.20mm/LAI`, `KLAI=.046/LAI`. At LAI 2.5 `SCAP=.5mm`, `SKLAI=.115`; COVER=.5 and COVER=.9 both saturate `SKLAI=.115`, identical intercepted depth, identical total ground rainfall, despite dramatically different free TF, leaf drip, SF. Thus an inference "COVER had no physically important effect" conflates near identical boundary effective rainfall and actively disabled canopy impact energy.

## Native source coding audit (before any fix)
Official original https://github.com/TheSoilman/EUROSEM pinned sha as above:
- `emainl.for` lines ~957–962 reads `PLANTH` in **centimetres** and divides by 100: earlier plantheight 3, 2.5,1.2 originally **3cm,2.5cm,1.2cm**, not metres. `KINET` `KE_LD=max(15.8 sqrt(H_m)-5.87,0)`, threshold ~0.138m, suppressing leafdrop impact in original 729 test. This error was previously discovered in `decisions/2026-10-26_OAK_MISCANTHUS_REAUDIT.md` and confirmed specifically here.
- `eurseml.for` `KINET`: `DRIPKE=KE_LD*DRIPD/RAIN`; `DRIPS`: `DMMSEC=RMMSEC*DRIPD/RAIN` and `DRDTIN=DRIPKE*DMMSEC*DAMPF*(1-RWR)*EROD`: thus drip factor is squared, as a source-level candidate error relative to a singly partitioned rain kinetic-energy flux. Direct rainfall `RAINKE=KE_direct*TFALL/RAIN` multiplied by full `RMMSEC`, only one ratio.
- `eurseml.for` `INTERC` original `VEGSTO=COVER*DINT*(1-exp(-Pcum))`; 2025 injection changed this. Under both versions stemflow is converted back to mean areal `rain` in flow, not localized stem-footprint.
- `eplanel.for` `MCODE=1` branch is **Everaert** (Bagnold effective stream power), `MCODE=0` is **Govers** (unit stream power); earlier test.par ended `MCODE=1`. Published retrospective that said all 729 tests use Govers must be corrected.
- `eusedl.for` `SED...` `CALL CAPAC`, `CALL DRIPS`, then `DTRF=CGU*TW`, `DTRC=DTRF*CEX+RDET`; `SUP=DTRC-CT*DTRF`; model can be transport-capacity limited; need numerical internal term ratio rather than infer 'inoperative splash'.

## Actual reproduced native end-to-end 24 cases
[Actions run 40319063481](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40319063481), branch `eurosem-forensic-audit-20261026`, workflow `eurosem-forensic-20261026.yml`, script `eurosem_lai_1998/forensic_native_20261026.py`.
- 24/24 run return0, original source hash `8652944...`; original F77 body flow and sediment unchanged, existing 2025 `LAI.PAR` fork and gfortran legacy init/format fixes applied. Same rain30mm/h LAI2.5, three cover, heights 3/150cm, EROD .1/.9g/J, MCODE0/1.
- COVER=.5, EROD=.1, MCODE0, 3cm -> internal height .03m, DRIPKE0, reported first plane net 37,829.730kg; 150cm -> height1.5m, DRIPKE2.779253, **same** 37,829.730kg.
- COVER=.5 H150cm EROD .9 MCODE0 first net 37,829.734kg; MCODE1 first net 44,036.523kg. MCODE dominates.
- Water error in these scenarios ~0.0046%, good only hydrology.

## Native A/B of suspected doubled drip ratio: 12 matched pairs
[Actions run 40319799767](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40319799767), script `eurosem_lai_1998/forensic_drip_single_fraction_20261026.py`.
Compiled **1998 original DRIPS** plus instrument-only writes against **one-line diagnostic (not original!)** `DMMSEC=RMMSEC` instead of `DMMSEC=RMMSEC*DRIPD/RAIN`. 3 COVER ×2 EROD×2 MCODE=12 pairs, total24 native runs. All returned0 and 8 internally logged splash samples per run:
- COVER0.1 EROD.9 MCODE1 `DRDTIN` mean original0.0000650307 -> modified0.0018286844 (×28.12).
- COVER0.5 same original0.0021856320 -> modified0.0106015837 (×4.851).
- COVER0.9 same original0.0072999685 -> modified0.0193749844 (×2.654).
- First plane reported net erosion kg **identical at printed .001kg precision in all matched pairs**, even though modified internal leaf splash increased strongly. More restrictive earlier instrument yielded 0 samples, corrected in commit b246e1 and **successful repeat** confirms actual samples.
- Therefore doubled drip factor alone does NOT explain the full model's near-zero vegetation sensitivity and should not be silently patched as solution. No native original 'bug fixed' scientific validation was claimed.

## Numerical interpretation and unresolved checks
- Gross interrill detachment and first-plane source-reported net do NOT equal sediment mass flux across physically defined final catchment boundary, and simulated erosion has **no independent sediment ledger** in archival QA.
- A source-term-only option may have very small effect under strong transport-capacity control or per-cell finite soil recirculation. To demonstrate dominance, instrument and quantitatively contrast `RDET`, `DTRF*CEX`, `DTRC`, `CT`, `SUP` in `eusedl.for`; new native workflow sourceflux probe [run 40320553800](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40320553800) initiated, results to append if successful. Do not label transport limitation conclusively proven before positive native diagnostics.
- Finite available 5m `DERO` in test data is not the shallow postfire soil at Gounsa; no observed Ksat, plant LAI, root biomass, wettability/stone layers, TLS calibration.
- Original EUROSEM has 1D cascading planes/channels, not genuine 2D lateral hydrodynamic and sediment conservation, and native canopy partition collapses stem-footprint SF location to areal means.

## Final decision and publication trust
- **Retract** unqualified rejection rationale "COVER/LAI low response means EUROSEM canopy physics are insignificant." It was incorrectly extrapolated from a flawed experimental fork and unit interpretation, *and* corrected native inputs still show surprising small sediment response deserving process investigation. 
- **Do not reinstate** EUROSEM as Gounsa main source engine because standalone full 2D requirement fails, original dynamics produce no independently verified sediment conservation, no spatial species root feedback. 
- **Potential use:** historical published plant capture, throughfall, leafdrip, stemflow formulas only after dimensional/source/manual discrepancy verification; process-level scientific reference, not validated absolute t/ha.
- Any future diagnostic modified sediment code has to be called a new experimental fork.

## Additional native source-to-capacity probe: completed
[Actions run 40320553800](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40320553800), `eurosem_lai_1998/forensic_capacity_flux_20261026.py`. Recreated 24 original experiment cards; instrumented `eusedl.for` just after native `SUP(I)=DTRC-CT(I)*DTRF`, to observe at the active first interrill grid point 8 actual solver steps. No physics edits. Four cases EROD .1/.9 × MCODE0/1:
- **Successful fully complete cases at EROD .1**: native sample means `RDET` 3.10297877875e-9 (both MCODE), `DTRF*CEX` 0.0015925075 (Govers) and 0.00194201 (Everaert). Ratio **513,216x** and **625,857x** respectively, computed from the two means. Thus in these sampled time/space cells, the effective equilibrium transport-capacity source contribution completely dwarfs rain-source `RDET`. More plausibly than 'grass has no effect', this particular test was grossly **transport-capacity controlled** or encoded a physically unusual huge source. This is *not* the whole spatiotemporal integrated source mass ratio, nor proven physically sound.
- These original code samples produced concentrations around 0.05996/0.07373 and transport capacities about 0.06150/0.075 (model units), and original net first plane 37829.73 / 44036.52kg as reproduced.
- **EROD .9 instrumented cases: incomplete**. Although subprocess exit0, only four samples and no source-reported first-plane net erosion found, so treat these instrumented cases as **INCOMPLETE**, NOT as confirming the .9 ratio. The previous 24-case original end-to-end test `40319063481` did return full outputs at EROD .9, but this particular diagnostic code may perturb legacy Fortran execution; source-level instrumentation is not itself a guarantee of identical uninstrumented behavior. Do not merge partial EROD .9 source probe into model success claims.

**Consolidated cause attribution:** (A) 2025 LAI extension capped COVER dependence; (B) 3cm PLANTH effectively suppressed leafdrip KE; (C) original DRIPKE×DMMSEC uses squared fraction; (D) **in the tested original benchmark**, sampled native capacity equilibrium source was >5e5× raindrop source and outlet reported sediment was overwhelmingly insensitive to EROD and height. The combined source and original run evidence justifies that prior low sensitivity **was not a valid plant-erosion-process falsification**. Whether a different slope/soil/rain intensity or measured site yields different physical sensitivity remains unverified. No independent sediment ledger and no true 2D model, so Gounsa main engine rejection stands.
