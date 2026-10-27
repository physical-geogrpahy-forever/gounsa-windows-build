# 2026-10-27 고운사 비LISEM 후속: 한국 산림 수관침식 관측 2009, 참나무 관측 2016, Wflow native 2026 단위오류 검증

## 출발과 목표
기존 `SYSTEM.md`, `MASTER.md`, `INDEX.md` 494 papers /103 models/99 decisions, 이전 비LISEM 감사, 모델 Wflow/SWEHR/PSEM2D/RillGrow/CAESAR reviews 확인 후 신규 DOI 우선 찾음. **OpenLISEM 원본 코드 디버깅은 사용자 Work에 맡겨 본 세션에서 다루지 않음**. 본 조사는 '실제 발표된 5–10cm 자유 XY+canopy+rain/flow erosion+deposition+source'만 합격으로 하며 현장침식 5cm 퇴적층을 모델 5cm cell로 둔갑 금지.

## 새로운 국내 야외실험 2009
Kim, Yang, Kim & Onda (2009), *Hydrological Research Letters 3*,36–40, DOI10.3178/hrl.3.36. 경기도 안성 0.45×0.40m **six soil loss plot** in slopes 10,20,30deg under canopy/open; banded gneiss surface ~4% fines/76% sand/20% gravel. Observed canopy soil loss lower than open; strong relation to maximum 3h rainfall intensity and storm total; canopy throughfall reaches saturation-like relation and erosion initiation changes. Publisher J-STAGE article verified; indexed article full text for plot info. **Observation, not 2D computational grid; no model code**. [Canonical](../papers/2009_Kim_Yang_Kim_Onda_Korean_Forest_Canopy_Interrill_Erosion.md).

## 새로운 참나무/낙엽 2016 현장연구, 재사용 가능한 수관우량 자료까지 확인
Thompson, Davis & Oliphant (2016), *ESPL 41*:1018–1026, DOI10.1002/esp.3881. University-hosted original 9p PDF read and web PDF screenshots p2 and p6 checked. Eight paired California Quercus agrifolia and Eucalyptus globulus plots 1.5m² under undisturbed canopy, oak mean slope21.4deg vs eucalyptus19.1deg; oak mean litter layer **5cm**, eucalyptus **10cm** (these are litter thickness NOT computing grid). 2006/07 eucalyptus runoff greater, soil repellency effects; heavy Jan2008 oak plots **more sediment** than eucalyptus (ANOVA p0.019, Wilcoxon p0.0325) and litter-depth difference hypothesized. Storm totals Jan2008 approx 450mm, daily max123mm, collection buckets overflowed → large-event water runoff uncertain. No forest fire treatment in original field.
**Actual reusable raw-derived observational data discovered**: [iGISc/iGIScData data/tidy_eucoak.rda](https://github.com/iGISc/iGIScData/blob/master/data/tidy_eucoak.rda), documentation `man/tidy_eucoak.Rd` with **180 rows ×12 variables**, includes oak/eucalyptus, event rain mm and subcanopy rainfall, runoff volume L, soil repellency, slope/aspect. **It does NOT list sediment mass nor cellwise DoD**, so suitable for basic rainfall partition + plot runoff comparisons, NOT direct erosion-validation or 5cm simulation. Source trace via connected GitHub. [Canonical](../papers/2016_Thompson_Davis_Oliphant_Oak_Eucalyptus_Litter_Soil_Erosion_Field.md).

## New high-impact actual released source version audit Wflow Julia
Previously canonical [Wflow_Sediment.md](../models/Wflow_Sediment.md) contains full native LAI canopy+ EUROSEM leafdrip/direct rain detachment + ANSWERS runoff erosion but directed-graph sediment routing, therefore **no genuine independently directed 2D XY local sediment transport**.
**New GitHub upstream merged commit actually inspected**:
- [Deltares/Wflow.jl PR 939](https://github.com/Deltares/Wflow.jl/pull/939), merged 2026-06-15 commit `b9de064dda8027dfd5567af1b5ccef8c35d0c869`, included in [v1.0.3 2026-06-23 release](https://github.com/Deltares/Wflow.jl/releases/tag/v1.0.3), exact tagged target `44f15035073cb011ae26a57620882de9a16dd041`.
- `erosion_process.jl` **erroneous prepatch `KE=(rddir*kedir+rdleaf*keleaf)*0.001`** changed to **`KE=(rddir*kedir+rdleaf*keleaf)`**: rainfall depth [mm] × drop KE [J m^-2 mm^-1] already is [J m^-2]. Explicit wrong prepatch multiplier reduced one term 1000×.
- `rainfall_erosion.jl`: `waterlevel_mm=waterlevel[i]*1000` before canopy-related EUROSEM splash shield `exp(-φh)`: original h measured [m] while original equation assumes [mm] and φ[mm^-1]. Without conversion, shielding vastly underrepresented. Therefore two patches act in **opposite directions** and Gounsa plot forecast ratio cannot be inferred by a single 1000 factor.
- Upstream changed test `test/run_sediment.jl` single-cell rainfall erosion **0.01232301374083337 → 12.323013740833371**; test mean rainfall erosion **0.0014726364432116048 → 1.433891239693397**; total soil erosion mean **0.010083427210107495 → 1.4425020304602927**. Exact **upstream regression assertions only**, not native Gounsa model re-run. Never claim public model has no bug now, only these known bugs fixed.
- v1.0.3+ recommended for any *secondary* Wflow EUROSEM comparison, not as main model. Source is complete, but 5cm event free-X/Y sediment native paper unproven and network transport is hard fail.

## Search model status
New papers 2009 and 2016 are scientifically useful **field observation**, not independent new model engines. Original Gounsa all-in-one 5–10cm 2D source **still no proven PASS**, despite historical source bug fixes. This cannot license user-unwanted model coupling or extrapolate existing non-5cm solver. OpenLISEM left for parallel Work.

## Specific new insight for model experiments
When canopy interception ON/OFF is compared, hold litter thickness, soil repellency, infiltration, surface cohesion/roughness fixed to isolate canopy-only effect; then do second factorial varying litter and soil. **Observed oak sediment can be greater even with interception** if litter/soil differs, so simplistic canopy→erosion monotonic assumption should be tested, not presupposed.

## Native checks conducted
Original Wflow merged GitHub PR diff and field dataset package docs inspected via connected GitHub; forest 2016 9p PDF screenshot inspected. No native erosion solver compiled or simulation executed in this session. For user requirement 'actual previously used 5–10cm single published model', findings remain partial.
