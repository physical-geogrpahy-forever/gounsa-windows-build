# 2026-10-27 original DHSVM (Doten 2006) recovered in independent GitHub C source — strict final gate

## 이 조사의 가장 중요한 확정 성과
기존 사용자 고운사 문헌의 'Doten(2006) 침식 소스코드가 공식 PNNL 배포판에 없다'는 기록은 사실이었지만 **모든 공개판에 없다는 확대해석은 잘못**이었다. `https://github.com/jhamman/DHSVM` root master에 **실제로 동일 프로그램으로 빌드되는** 유수침식 C code가 있다.
- makefile `InterceptionStorage.o`, `MassEnergyBalance.o`, `RouteSurface.o`, `RouteChannelSediment.o`, `CalcBagnold.o`, `InitSedMap.o`, `InitSedTables.o` 및 `MainDHSVM.o`를 동일 `DHSVM` 실행프로그램에 묶는 명시적 target.
- `InitNewMonth.c` monthly LAI→capacity Smax; `MassEnergyBalance.c` canopy interception and leafdrip/direct rain momentum; `InterceptionStorage.c` active S(t) and `MomentSq`; `RouteSurface.c` rain+flow sediment and transport; `RouteChannelSediment.c` river loads. **This is a genuine single-codebase forest canopy plus sediment ancestor**. This changes 'code absent' to '**code present, not native verified stable**', not the Gounsa candidate decision.

## Critical native defects discovered
1. `RouteSurface.c L284–295`: absent OverStory/UnderStory → `DR=0` always, despite `MassEnergyBalance.c` has direct-rain `MomentSq` without vegetation.
2. `RouteSurface.c L261–273`: `DR` only inside `sedoutflow>0`, water-depth >0.001m and stream power >0.004. This suppresses physically independent rainfall detachment under low-runoff conditions.
3. `RouteSurface.c L284–292` uses **`VType->` == `VType[0]`** not mapped `VType[VegMap[y][x].Veg-1]`, even though L127–147 correctly indexes vegetation class. Hence bare/grass/oak **mixed patch canopy erosivity does not follow per-cell class** in inspected source.
4. `MassEnergyBalance.c L215–220` rainfall branch **`if(I>10) index0; else if(10≤I<100) ...`**, making intended middle 10–100mm/h coefficient branch unreachable except at exactly I=10. This is a code branch flaw in rain moment.
5. `RouteSurface.c L392–405` `TopoMap.Dir/TotalDir` positive downslope direction routing, `SedimentFlag L595–599` explicitly sets `Routing=TRUE` kinematic when erosion active. Free XY SWE + sediment no.
6. Original Doten 2006 article peer-reviewed simulation **30m grid 49,085 cells, 3-hour hydrological timestep**, runoff erosion at hydrological scale not high-resolution mass wasting; assumes unlimited detachment supply. No published 5–10cm native flow/erosion; exact paper binary SHA and complete inputs not archived in code repo.

## Full review references
- [new model original-code audit](../models/DHSVM_Doten_2006_Original_Open_C_Sediment_Canopy_Execution_Path_2026.md) file by blob SHA and line.
- [canonical Doten paper corrected](../papers/2006_Doten_DHSVM_Mountain_Forest_Sediment.md).
- https://github.com/jhamman/DHSVM
- https://doi.org/10.1029/2004WR003829 original Wiley text §2, §3.
- `pnnl/DHSVM-PNNL` remains separate current release tree lacking above solver; **must never conflate it with recovered historical jhamman code**.

## User's strict decision
| mandatory criterion | judgement |
|---|---|
| Published peer-reviewed forest and LAI/canopy water impact soil erosion | PASS concept Doten 2006 |
| In one publicly inspectable C source code compiled canopy→drip momentum→sediment | **PASS native connected code**, actual full build not done |
| Soil source correct for bare grass oak spatial patch | **FAIL source-level** |
| Independently positive rain splash in low runoff and vegetation-specific energy | **FAIL source-level** |
| Real free X/Y 2D SWE and sediment | **FAIL kinematic network** |
| Published actual 0.05/0.10m computational trial | **FAIL original 30m** |
| Numerical water+sediment mass and timestep stability at 5cm | **UNKNOWN / NOT RUN** |
| Released source exact 2006 paper build & native dataset | **UNCERTAIN** |
**Strict rejection for operational Gounsa 5–10cm original remains.** But previously unseen *full original forest canopy + sediment code lineage* found and this factual correction preserved. Do not propose a hand-patched branch as another established published model. Source-level bugs provide reproducible reasons to reject before resource-heavy runtime tests.

## Next decision if user prioritizes short-term deliverable
No verified existing all-condition main model this session. If user changes strict full-SWE/5cm or source code requirements intentionally, archived **real code** DHSVM is a documented forest benchmark, yet after the above source defects it must not be promoted as scientifically valid canopy-on/off unmodified simulation. A different physically based engine that was actually published and tested at 5cm would still be necessary.
