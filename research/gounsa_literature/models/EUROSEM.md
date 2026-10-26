# EUROSEM lineage

## 고운사에서 검토한 이유
매립 석력과 surface armour가 infiltration, runoff, splash, rill/interrill erosion에 미치는 효과를 하나의 published erosion model에서 명시적으로 처리하는지 확인하기 위해 검토했다.

## 핵심 문헌
- Morgan et al. 1998, EUROSEM key paper
- Morgan et al. 1998, EUROSEM documentation and user guide
- Khaleghpanah et al. 2017, stony steep lands validation
- Jomaa et al. 2012, rock-fragment hydrology/erosion modeling comparison

## 공간 구조
- distributed event model
- cascading plane/channel elements
- interrill/rill explicit
- genuine 2D SWE 아님

## rock-fragment state
EUROSEM은 세 변수를 명시적으로 분리한다.

### ROC
`ROC` = soil volume 중 rock-fragment fraction.

기존 KINEROS infiltration formulation을 따라:
```
B_roc = B (1 - ROC)
```
으로 soil water-storage/saturation-deficit term을 조정한다.

### PAVE
`PAVE` = soil surface의 non-erodible/rock-fragment cover fraction.

raindrop detachment:
```
DET_pav = DET (1 - PAVE)
```

### ISTONE
surface position/sealing condition에 따라 PAVE가 saturated hydraulic conductivity를 증가 또는 감소시키도록 선택한다.

infiltration-reducing condition:
```
K_s,roc = K_s (1 - PAVE)
```

infiltration-enhancing condition:
```
K_s,roc = K_s (1 + PAVE)
```

중요: `embedded`라는 단어만으로 ISTONE 부호를 정하지 않는다.
- surface seal에 partially embedded된 fragments는 infiltration을 낮출 수 있음.
- high structural porosity/macroporosity 조건의 fully embedded/resting fragments는 infiltration을 높일 수 있음.
따라서 현장 surface seal/porosity 상태가 필요하다.

## 고운사에서 직접 쓸 수 있는 부분
- ROC, PAVE, ISTONE의 정의
- surface armour의 splash shielding
- stoniness와 infiltration/runoff를 같은 erosion model 안에서 연결한 published precedent
- steep stony hillslope 적용 선례

## 고운사에서 그대로 쓰기 어려운 부분
- full EUROSEM은 genuine 2D가 아님.
- rock-fragment state가 event 중 dynamic size-class armour로 진화하지 않음.
- high-volume embedded stone의 full unsaturated hydraulic conductivity curve에는 현대 GEM model이 더 적합함.

## 최종 판정
**부분 채택.**
- surface PAVE/shielding과 surface seal-position logic의 published source
- full production erosion engine으로는 사용하지 않음
- 고운사의 high embedded stoniness hydraulic property는 GEM/Naseri 계열을 우선

## 관련 파일
- ../papers/1998_Morgan_EUROSEM.md
- ../papers/2017_Khaleghpanah_EUROSEM_StonySteepLands.md
- ../papers/2012_Jomaa_RockFragmentHydrologyErosionModel.md


## 2026-10-26 기존 식생 민감도 무반응 실험의 실제 오류와 재현: 판정 갱신
[2026-10-26 실제 729개 CSV 복구, 원본 Fortran 감사, 신규 24+24회 A/B 실행, 소스 플럭스 계측](../decisions/2026-10-26_EUROSEM_PREVIOUS_LOW_VEGETATION_SENSITIVITY_FORENSIC.md).
- 원본 `TheSoilman/EUROSEM` SHA `8652944da6e1e8436495aa0c08765e2399830dd7`. Original `INTERC` reads `COVER,DINT,SHAPE,PLANGLE,PLANTH,PBASE`; LAI variable was **added in 2025 experimental `patch_interception.py`**, not original.
- Added law `SKLAI=min(COVER,.046 LAI)`, `Smax=.20 LAI` mm: for LAI2.5, COVER .5 and .9 map to same capture coefficient .115 and same effective rain. 729 factorial 'COVER no effect' was partly mathematically baked into modified inputs.
- PLANTH original ASCII is **cm** and code divides by100, so past '3m' native `3` actually **3cm**. Internal leafdrip KE=0 for H<~0.138m; comparisons of measured-height plant interception were invalid. Rerun native 150cm returned positive KE and no sediment-change in this original benchmark; height error not sole cause.
- Original native `KINET` `DRIPKE=KE_LD*DRIPD/RAIN` then `DRIPS` `DMMSEC=RMMSEC*DRIPD/RAIN` => native leafdrip detachment scales as `(DRIPD/RAIN)^2`, unlike single-count rain partition. Source diagnostic one-line `DMMSEC=RMMSEC` A/B inflated *native internal* leafdrip splash 2.65–28.12x but did **not** affect source-reported first element net erosion at displayed precision (12 pairs).
- Source `MCODE=1` = Everaert, `0` = Govers. Fixed case MCODE switch changed first plane 37,829.734→44,036.523kg, +16.4%. Previous claim using Govers at MCODE1 invalid.
- Native `SED` `DTRC=DTRF*CEX+RDET` internal probe sampled `RDET≈3.1×10^-9`, `DTRF*CEX≈0.0016–0.00194` (5e5–6e5× greater), explaining why splash changes were dynamically swamped by transport-related source in sampled cells. The EROD=.9 additional instrumented cases output was incomplete, do not claim all-pass.
- Existing 729 original+LAI compiled runs and today's 48 complete native A/B/OAT runs are **not independent sediment mass closure or 2D site validation**. Native original EUROSEM is 1D connected plane/rill/channel geometry, despite many rainfall and plants processes. No true 2D LiDAR rill initiation, no localized stem-foot SF, no native quantitative root RLD coupling.
**Verdict**: restore as **valuable source-process benchmark** after correctly separating native code vs LAI fork; **continue EXCLUDE** as complete original Gounsa 2D source erosion engine, primarily for true2D and independent sediment QA gaps, not blanket 'vegetation has no effect'.

## 2026-10-26 저민감도 재감사: 과거 폐기 근거는 실험설정 오류가 포함됨

[EUROSEM 729회 전요인+원본 추적 및 28회 재시험 결정문](../decisions/2026-10-26_EUROSEM_729_LOW_VEGETATION_SENSITIVITY_ROOT_CAUSE_REAUDIT.md)을 최신 판단의 기준으로 적용할 것.

1. 2026-10-25 729회 자료 원문 CSV 직접 재분석: 3cm PLANTH로 leafdrip KE가 0이었고 **LAI는 native 원본 변수가 아니라 별도 `LAI.PAR` 실험 포크**에서 `Smax=Sleaf*LAI` + `k=min(COVER,kLAI*LAI)`로 추가한 상태변수였다. 이 포크의 LAI 민감도가 작다는 결과를 원본 canopy 또는 실제 고운사의 작은 식생효과로 해석하면 안 된다.
2. 원본 `eurseml.for::KINET` `DRIPKE`는 이미 `DRIPD/RAIN`을 곱함. `::DRIPS`에서 `DMMSEC=RMMSEC*DRIPD/RAIN`을 또 곱해 **drip source에 비율의 제곱**을 적용한다. Morgan et al. 1998 KE equation uses single weighted drip rainfall.
3. **2026-10-26 실제 original C/Fortran compile+run 20 cases** ([Actions](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40322591668)) confirmed original and *separately labelled corrected fork*: H3cm to H120cm, cover .1/.9, EROD .1/.9, MCODE Everaert1/Govers0. `DRIPKE>0` at H120cm, **reported sediment unchanged** when EROD or drip fraction corrected; 20/20 hydrological QA PASS, sediment independent ledger untested.
4. **Actual in-solver `SPLASH_DIAG` + `SED_SOURCE_DIAG`** [Actions](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40323173111): At L40 EROD0.1 to0.9 changes `RDET` ×9, drip-factor fix increases `RDET` about ×1.50, but flow `DTRF*CEX` and net `SUP` unchanged to reporting precision. Therefore engine **receives** KE source, but water-flow sediment transport capacity dominates this synthetic setup.
5. `eusedl.for::SED` line `DTRC=DTRF*CEX+PAVF*RDET(I)` mixes source commented m/s with flow-width `DTRF*CEX`; **apparent unit mismatch**, must derive before any correction. Separate *experimental fork* `RDET*TW` 8/8 native runs only changes exported output by ~0 to0.00021t/ha. [Actions](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40323570418). Changing source physics is never represented as original source behavior.
6. OLD 'EROD insensitivity proves splash physically irrelevant' **WITHDRAWN**. Formula-level errors and transport-dominated exact synthetic setting explain output. But still no independent EUROSEM sediment conservation, finite depth or 2D spatial stemflow/erosion map; **not restored as main 2D Gounsa engine**. Canopy rain balance and separate interrill/rill source equations can be process benchmarks after exact corrections.

Original source https://github.com/TheSoilman/EUROSEM and customized diagnostic branch https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/swehr-water-sediment-closure-20261026/experiments/rainfall_10_50 .


### 2026-10-26 추가 원본 시간간격 수렴 시험
[실제 GNU Fortran 12회 실행](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40324676949)에서 H120cm, COVER.9, DINT1.5mm, EROD.9, 강우30mm/h 1시간, 100×145m 합성 단일 사면 조건으로 DELT=60,30,15s를 비교했다. Govers 순침식량 21.59255→21.68883→21.74793t/ha, Everaert 25.63028→25.72379→25.78255t/ha. 15s vs30s 차이 각 0.272%,0.228%; 12/12 수문 물수지 PASS. **이 조건에서 원본 계산은 시간간격 수렴 경향을 보임.** 독립 유사수지 미검증, 유한 토심 엄격 제한 미검증, 여전히 1D 연결 사면이므로 원본 2D 주 엔진 선정 안 됨. 결론 상세 [결정문](../decisions/2026-10-26_EUROSEM_729_LOW_VEGETATION_SENSITIVITY_ROOT_CAUSE_REAUDIT.md).


## 2026-10-26 원본 유사수지 24회 새 실험: 세류 0/12 통과

[고정밀 원본 유사수지 재검증](../decisions/2026-10-26_EUROSEM_1998_NATIVE_SEDIMENT_LEDGER_RILL_FAILURE.md). 원본 eplanel.for 873–924행은 inrlbal=sumqirr+sumdir+suspir, rillbal=stout+sumdrl+susprl-sedin 수지 계산을 이미 포함한다. 과거 보고에서 독립 유사수지 검증만 미완료였고 해당 원본 수지식이 없었던 것은 아니다.

**실제 24회**: RAIN30/50 mm/h, dt15/30/60초, rills off/on, Govers/Everaert 원본 Fortran source. 24회 수문 검사/원본 outlet Q×CT 재적분 통과, 독립 유사수지 tolerance 0.1% **9/24**만 통과. rills off 9/12, rills on 0/12.

**15초 결과** rills on whole slope sediment residual: R30 Govers −3.55178m³ (outlet 대비14.32%), R30 Everaert −5.74281m³ (21.48%), R50 Govers −21.05008m³ (16.99%), R50 Everaert −27.29938m³ (20.50%). 반면 rills off 네 경우 잔차 0.0037–0.0291%. 시간간격 줄여도 세류 잔차 해결되지 않음. [원본24회](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40326142263).

**세류간→세류 실제 유사 전달 재계측**: [24회](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40326648315). 15초 조건, interrill exported vs measured actual lateral into rill Govers30:11.80246 vs11.79962m³, Everaert30:18.96229 vs18.96267, Govers50:70.11043 vs70.10292, Everaert50:90.78222 vs90.78481. 대량 누락은 세류간-세류 연결점이 아니다. **세류 내부의 DLA/DRLNET/bed update 또는 미집계 저장량**을 추가 검사해야 함.

**현 상태의 EUROSEM 세류 포함 유사수지는 FAIL**, 세류 없는 1D 원본만 한정적 통과이고 고운사 2D 주 모델의 필수조건과 별개다. 실험적 LAI 보강과 수관적하 오류 수정 포크를 1998년 원본 기능으로 혼동 금지.
