# DHSVM-Doten 산림 수관차단과 지표유수침식 완전 공개 C 소스 발견 및 원본 경로 심층감사 (2026-10-27)

## 최초 발견과 중요한 과거 판정 정정
2026-10-27 고운사 문헌조사에서 이전 [Doten 2006 canonical](../papers/2006_Doten_DHSVM_Mountain_Forest_Sediment.md)은 공식 `pnnl/DHSVM-PNNL`를 살펴본 후 "확장 침식소스가 공개되어 있는지 미확인"으로 기록됐다. **그것은 조사 미진에 따른 불완전한 판단이었다.** 별도 공개 GitHub [`jhamman/DHSVM`](https://github.com/jhamman/DHSVM) master는 **실제 침식/유사수송이 들어 있는 하나의 구형 C 모델 전체 소스**를 제공한다.
원문 **Doten et al. (2006)**, *Water Resources Research* 42 W04417, DOI https://doi.org/10.1029/2004WR003829 . 메인 `makefile` blob `d3aea1b578d5b07dc5c2e6241c29eefac551f904`에서 `InterceptionStorage.o`, `MassEnergyBalance.o`, `InitSedTables.o`, `RouteSurface.o`, `RouteChannelSediment.o`, `CalcBagnold.o`, `InitSedMap.o`, `MainDHSVM.o` **모두 OBJS로 링크**. 각 소스가 텍스트로 존재하고 헤더/빌드 포함됨. **This corrects only source existence**; it does NOT validate native execution, 2006-paper same revision, canopy benchmark or cm-scale feasibility.

## 파일별 공개 C blob and exact lines
| `jhamman/DHSVM` root file | Git blob SHA | 중요한 원본 |
|---|---|---|
| `makefile` | `d3aea1b578d5b07dc5c2e6241c29eefac551f904` | 전체 sediment-related C obj included, legacy gcc/FLEX/X11 make |
| `MainDHSVM.c` | `ac436ba3f124305cb5d570c40c2473573e831c2d` | L245–274 Sediment initialization and SedMap, L319 SedimentFlag, L370–75 cell VegType input into MassEnergyBalance, L431–35 RouteSurface, L400–412 ChannelSed |
| `InitNewMonth.c` | source read; SHA from GitHub `fetch_file` obtainable | L114–116 `VType[i].LAI[j]=LAIMonthly[j][month-1]; VType[i].MaxInt[j]=LAI[j]*Fract[j]*LAI_WATER_MULTIPLIER` |
| `MassEnergyBalance.c` | `f68123522c94e3b964c3376b34044747bc707077` | L117–20 coefficient arrays, L211–26 rainfall momentum, L270–74 `InterceptionStorage` called with plant canopy; L277–79 no-veg input momentum |
| `InterceptionStorage.c` | `d026c1abb57248fb38ac0b24e76f495fa496285c` | L46–53 canopy interception bucket; L55–65 momentum contribution from canopy drip and direct throughfall |
| `RouteSurface.c` | `12616f71e9715801aaa1b1c7517129fc8e75b40e` | L259–344 detachment/transport equation; L392–405 weighted fixed downslope routing |
| `RouteChannelSediment.c` | `46dac1ca188dcae469f7e6a60d7f97a47bce81bb` | channel fractions sediment storage, L128–280 capacity/settling/routing |
| `InitSedTables.c` | original file read | KIndex and soil d50, cohesion and root coherence as configured sediment tables |
| `data.h` | `99512d92d0f151013afc012034bf1ba23f7e3513` | VEGTABLE LAI, canopy MaxInt, Fract, Height, SEDPIX output Erosion, MomentSq |
| `settings.h` | `f0ac93d23fb678637d32b809bd2b6d2b15a55ac1` | eight (directional) neighbor sediment definitions |

### Physical active path (same source)
1. `InitNewMonth.c L114–116`: monthly **LAI→Smax native** (`LAI×Fract×LAI_WATER_MULTIPLIER`).
2. `MainDHSVM.c` loops real grid cells and calls `MassEnergyBalance` with `&VType[VegMap[y][x].Veg-1]`. `MassEnergyBalance.c L270–274`: `InterceptionStorage` consumes `MaxInt,Fract,IntRain,RainFall` and outputs `MomentSq`.
3. `InterceptionStorage.c L46–53`: canopy S(t) buckets intercept/deduct precipitation; L55–65 `MomentSq` computes kinetic impact **from modeled leafdrip + directly throughfall** (using vegetation height dependent `LD_FallVelocity` and `MS_Rainfall`).
4. `RouteSurface.c`: `PrecipMap[y][x].MomentSq` used in `DR` drop-induced detachment and `streampower`, `TC`, `floweff` determine flow-induced entrainment, final sediment concentration `SedOut` with settling + cap. `SedMap.Erosion` and channel sediment inputs computed; `RouteChannelSediment` handles river fractions, settling, deposition.
5. `MainDHSVM.c L319` `SedimentFlag` must switch `SurfaceErosion` ON; `RouteSurface.c::SedimentFlag L595–599` explicitly **forces kinematic routing on when erosion on**.
**Thus canopy-water/drip-rain impact + hillslope sediment code is indeed a single publicly readable compiled-code lineage**. Do not repeat old claim "Doten erosion code never appeared in GitHub".

## Serious source defects exactly as printed: unacceptable before field use
### A. Rain splash forcibly zero for native bare cells
`RouteSurface.c L284–295`:
```c
if (VType->OverStory == TRUE) {
    if (VType->UnderStory == FALSE) DR = KIndex*Fw*MomentSq;
    if (VType->UnderStory == TRUE) DR = KIndex*Fw*(1-VType->Fract[1])*MomentSq;
}
else if (VType->UnderStory == TRUE)
    DR = KIndex*Fw*(1-VType->Fract[0])*MomentSq;
else
    DR = 0.;
```
**For vegetation class with no overstory or understory, `DR=0` even with positive rainfall momentum.** `MassEnergyBalance.c L277–279` explicitly sets `MomentSq=MS_Rainfall` if **no vegetation**, so the hydrological input contains direct raindrop impact but the sediment code **then nulls bare-soil raindrop detachment**. Directly contradicts Gounsa bare vs grass/oak splash comparison. Static source-level fact, not independently native run.

### B. Drop detachment conditioned on existing strong overland flow
`RouteSurface.c L259–273`: all erosion computations including `DR` nested under `sedoutflow>0`, then under `h>0.001 [m]` **AND** `streampower>SETTLECRIT`. `constants.h` declares `SETTLECRIT 0.004` stream-power threshold. Thus impact-driven raindrop detachment **will be zero / not counted whenever water depth ≤1mm or stream power ≤0.004**, even for heavy rain on unponded soil. Its raindrop term is not independent from hydraulic transport condition. `DR` is not computed separately and stored if not mobilized. One could distinguish detachment-vs-delivery in model design, but **code does not represent splash and temporary deposited soil inventory** in those low-flow cells. Very significant for physical Gounsa bare plot.

### C. Per-cell vegetation identity appears omitted in splash erosivity
`RouteSurface.c` function receives `VEGTABLE *VType` and `VEGPIX **VegMap`. In same function L127–148, **correctly references** `VType[VegMap[y][x].Veg-1].ImpervFrac`. But L284–292 sediment `DR` explicitly references **`VType->OverStory`, `VType->UnderStory`, `VType->Fract`** without `VegMap[y][x].Veg` indexing. In C, `VType->` equals **`VType[0].`**, thus **every cell's raindrop detachment branch is based on the first vegetation class**, NOT each cell's mapped vegetation type. This affects Gounsa mixed patch comparisons even if hydrology uses correct cell `VType[...] `. The source's semantic issue can be proven without runtime, but exact relative sediment change needs native QA.

### D. Rain KE empirical intensity range selection inconsistent
`MassEnergyBalance.c L215–220`: `if(RainfallIntensity > 10.) MS_Index=0; else if(RainfallIntensity >=10. && RainfallIntensity<100.) MS_Index= floor(...); else MS_Index=3`. **Middle condition is reachable only at exactly 10mm/h**, not the whole intended 10–100mm/h band; all user's 10–50mm/h values >10 select coefficient `alpha[0],beta[0]`. Arrays at L117–120 include four calibrated empirical pairs; this is code-level branching defect, regardless of whether 10 or 100 was intended. No source patch was made.

### E. Genuine XY 2D inertial flow absent and dynamic soil stock not constrained
`RouteSurface.c L392–405` redistributes downhill via nonnegative `TopoMap[y][x].Dir[n]/TotalDir` flow fractions, **not independent signed x/y face SWE momentum**; L169–177 and `SedimentFlag L595–99` force `kinematic` during active sediment. It cannot model spontaneous multi-sided free bidirectional inflow/outflow or hydrodynamic reverse flow of deposition patches.
`SedMap[y][x].Erosion` accumulates soil-depth-change diagnostic L330–331, but no actual `TopoMap[y][x].Dem` recomputation in viewed `RouteSurface` section and original paper explicitly states **unlimited sediment available** (Doten §2.2, paragraph [15]). This **is NOT a finite-depth topographic Exner solver** at 5cm. Claims about basin-wide water/sediment mass balance stability require an end-to-end compiled test.

## Published physical & numerical evidence
Original [Doten et al.(2006)](../papers/2006_Doten_DHSVM_Mountain_Forest_Sediment.md) full Wiley open paper §3: **Rainy Creek 49,085 cells at 30m**, 3-hour forcing/hydrologic timestep; surface erosion at **same 30m resolution** despite finer DEM for **mass wasting** (not for canopy-driven surface sediment). Mean slope26°, range0–66°. Forest overstory/understory and LAI fire sensitivity experiment published. **Native 5–10cm soil erosion calculation NO**.
- Original paper's own Section 2.2 paragraph [15] explicitly assumes *unlimited sediment available for detachment*.
- Source `jhamman/DHSVM` has a makefile with legacy X11/Flex and root src, but **no original published Rainy Creek run config or dataset in root**; no exact 2006 article source commit tag. Source `makefile` 2006-10-12 comment **postdates paper's first publication Apr 2006**, so do not falsely assert binary exactly identical to original 2006 printed calculations.
- GitHub full repo is readable but no explicit root LICENSE file in inspected tree; repository public visibility is not proof of GPL/reuse license. Terms must be clarified before adaptation.
- **No native compile/run performed** this audit. Direct files+makefile+calls verified; incorrect conditionals are source-level proofs, not quantitative validated run diagnostics.

## Gounsa strict verdict
| Gate | Status |
|---|---|
| Real published mountainous forest canopy+drop/sheet erosion concept | **YES**, Doten 2006 |
| Same public C source has canopy to `MomentSq` to surface sediment and channel | **YES**, archived variant `jhamman/DHSVM` (not exact paper build) |
| LAI→canopy max water storage code actually connected | **YES**, `InitNewMonth` + `InterceptionStorage` |
| Bare rainfall splash and grid-specific grass/oak physics correct | **FAIL in inspected source: DR=0 on bare; VType[0] for all cells** |
| Raindrop detach whenever rainfall falls even without runoff | **FAIL** gated h>1mm and stream power |
| Free x/y dynamic SWE flow and sediment | **FAIL**, topographic direction / kinematic |
| Published 5/10cm native | **FAIL**, actual30m at 3h |
| Stable fully compiled original executable / accurate local DoD | **NOT TESTED**; no published high-res benchmark or matching 2006 field source |
**Decision: NEW POSITIVE original-code discovery corrects historical source-negative, but operational Gounsa strict FULL NO-GO.** This is substantially stronger archival evidence than simply looking at a paper abstract: author-era code had original canopy impact and sediment code but its exact executable has scientifically fatal bare and mixed vegetation branch conditions. Do not feed this user a broken published model as a 5cm ready solution.

## Source links
- https://github.com/jhamman/DHSVM
- https://github.com/jhamman/DHSVM/blob/master/makefile
- https://github.com/jhamman/DHSVM/blob/master/InitNewMonth.c
- https://github.com/jhamman/DHSVM/blob/master/MassEnergyBalance.c
- https://github.com/jhamman/DHSVM/blob/master/InterceptionStorage.c
- https://github.com/jhamman/DHSVM/blob/master/RouteSurface.c
- https://github.com/jhamman/DHSVM/blob/master/RouteChannelSediment.c
- https://doi.org/10.1029/2004WR003829
