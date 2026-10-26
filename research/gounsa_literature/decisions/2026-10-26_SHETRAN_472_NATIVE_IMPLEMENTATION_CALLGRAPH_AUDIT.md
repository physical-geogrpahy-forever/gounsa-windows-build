# SHETRAN 4.7.2 소스 구현의 실제 연결과 기능 한계 감사 (2026-10-26)

## 조사 방식과 판정 수준
사용자 요구에 따라 **확인 가능한 완전 공개 원본만** 조사. 이번에는 신규 기능 구현/입력 매개변수 조작/모델 실행 없이 오직 원본 Fortran source를 line-by-line source trace. 원본 repository `nclwater/Shetran` GPL-3.0, pinned commit `cf9cd540add78ad3accbaf62b4199d2032887f6b`, project version 4.7.2.0. 원본 실제 함수 존재, 실행 중 경로 존재, 참고문헌 기능을 구분한다. 원본 Cobres/Aire 유사 활성 설정 제공되지만 **본 세션에서 원본 native 빌드, 예제 실행, 원본/외부 수지검증을 한 적 없음**.

## 본 실행의 정확한 함수 호출 순서
`src/driver/run_sim.f90` lines 251–346:
1. `ETSIM` (L272) → `ETIN` → `ET` per land element: vegetation time-state, canopy CSTORE, gross precipitation, evap, DRAIN, PNETTO and DRAINA output.
2. `VSSIM` (L276) per element: unsaturated/groundwater infiltration physics and `PNETTO` forcing; `VSmod.f90` L4399 soil-column net input.
3. `OCSIM` (L295) actual horizontal finite-difference flow (surface + channel); `src/overland_channel/OCmod.f90` L2238 `OCQDQ`, implicit block-row solve, L2375–78 outputs 4-faced signed `QOC`, `HRF`.
4. If `BEXSY` sediment flag is enabled and time condition true, `SYMAIN` (L311) receives `CLAI,PLAI,DRAINA,HRF,PNETTO,QOC,ZGRUND` from hydrological components. No sediment routing if BEXSY off.
5. `src/sediment/SYmod.f90` `SYMAIN`: `SYWAT` L3464 → `SYOVER` L3469 → optional channel-bank `SYBKER`, sediment per timestep and within NEPS sediment substeps `SYCOLM` L3586 or `SYLINK` L3564, then `SYBED` for channels L3635. Sediment multi-size mass routed to adjacent 4-faced elements; outflows scattered to neighbours L3608.
6. `BALWAT` for water L342; `BALSED` L345 is a **genuinely empty subroutine** `SYmod.f90` L4668–69. Numeric sediment mass closure is not independently validated by built-in BALSED.

## 1. Time-dependent canopy storage, NOT constant canopy-loss factor
`src/evapotranspiration/ETmod.f90` `ETIN` L795–817:
- plant/element canopy fraction `CPLAI = min(CLAI(N),1)*PLAI(N)`, `N=NVC(IEL)`; vegetation state can be time-varying via input breakpoints, unlike fixed crop coefficient.
- Rain `precip_m_per_s` is m/s, `DTUZ` s.
`ET` L451–531:
- incident not on canopy [mm/timestep] = `PNET0 = P*1000*(1-CPLAI)*DTUZ`;
- canopy interception evaporation = `PE*CPLAI*DTUZ` (scaled by wetness if storage below capacity);
- canopy net inflow [mm/s] `Q=CPLAI*(P*1000-PE)`;
- existing canopy water `CSTOLD=CSTORE(IEL)` [mm] and capacity `CSTCAP(N)` [mm].
- If stored water exceeds `CSTCAP`, drain via original logarithmic exact-solution branch involving `CK(N)` [mm/s], `CB(N)` [1/mm], `DTUZ`, and Q. Else fill store, evaporate from canopy, excess above capacity drains.
- water ledger in each element `DRAIN=CSTOLD + supplied P*DTUZ - canopy evap - CSTORE_new` (details depend branch).
- soil-reaching `PNET = (PNET0 + DRAIN)/DTUZ` [mm/s]; `ETIN` L814–18 writes `PNETTO=PNET/1000`, `DRAINA=DRAIN/(1000*DTUZ)` [m/s]. The two components are **hydrological rain input** and **canopy-drained component** in the original code; `DRAINA` is not per-stem stemflow.
- No independent per-stem water source/stem storage/trunk partition demonstrated. When stored below capacity after rainfall, water remains in canopy to evaporate; do NOT claim it must all drain after rain.
- Code caveats: `F1=MIN(CT1/CSTCAP,ONE)` evaluated before zero-capacity guard and legacy branch logarithms presume valid nonzero CB. Also comments warn snowmelt branch can leave DRAIN and PNET stale; requires unit tests.

## 2. Canopy-adjusted raindrop physics before splash erosion
`SYmod.f90` `SYWAT` L4413–4499:
- compute `FCC(N)=PLAI(N)*min(CLAI(N),1)` ground fraction sheltered by canopy.
- assign `DRAINA(i)` from hydrology and `PNETTO(i)`.
- Effective direct rain intensity `LRAIN = max(PNETTO-DRAINA,0)/(1-FCC)` if FCC<1.
- Effective raindrop diameter (meters) `DRDROP=max(1e-4, DRDRIP(N)*DRAINA/PNETTO, 0.01935*PNETTO^0.182)` if PNETTO>0. The ratio mixes effective drop size, not literal geometric drop distribution; requires physical verification.
- `SYWAT` also reads 4-face `QOC`, water level `HRF`, terrain `ZGRUND`, derives cell water depth `DWAT1=max(HRF-ZGRUND,0)` and representative shear `TAUK`.
- Having `LRAIN` vs `DRAINA` separate explicitly distinguishes canopy through/drain vs free direct rain for impact calculation. `DRAINA` is all canopy drainage as leaf/drip assumption, not spatial per-tree stemflow.

## 3. Actual original hillslope detachment law
`SYmod.f90` `SYOVER` L3658–3806:
- Vegetation species/type `NVC(IEL)` selects `XDRIP[N]` drip height [m], `DRDRIP[N]` drop diameter [m], `FDRIP[N]` drip-water fraction [0..1]; original input `SY24` sets these arrays.
- Drip momentum coefficient `TGMD=πρw²g*c*(1-exp(-2*XDRIP/c))*DRDRIP³*FDRIP/6`, with `c=ADD(ISCD)+DRDRIP*BDD(ISCD)` from legacy source; group classes switch by XDRIP and DRDRIP.
- Free rainfall momentum `GMR=(1-FCC)*AD(ISGMR)*LRAIN**BD(ISGMR)`, piecewise intensity coefficient `AD/BD`.
- Leafdrip momentum `GMD=TGMD*DRAINA`.
- Splash detachment `DR = GKR_soil*exp[-max(0,h/DRDROP-1)]*(1-FCG-FCROCK)*(GMR+GMD)`.
- Flow detachment `DF= GKF_soil*(1-FCROCK)*max(0,tau-tau_c)/tau_c` from `SYCRIT`, where tau from 2D water and tau_c from soil median diameter and clay or Shields.
- Source soil erosion depth `GNU=(DR+DF)/RHOSO` if loose sediment layer `DLS<DLSMAX`; if DLS>=threshold, sets GNU=0 **step-function absolute soil protection**, not smooth Hairsine–Rose shielding.
- **Very important: FCG reduces splash DR but is ABSENT in direct flow detachment DF. FCROCK reduces both DR and DF.** Therefore dense tussock ground cover cannot mechanically reduce flow detachment via same FCG term; it may change water hydraulics/other vegetation pathways but no direct DF_FCG in source.
- `FCG` and `FCROCK` are 2D land-element fractions entered from SY41/SY42 in `SYREAD` and `SYmod` `SYERR2` tests `FCG<=1-FCROCK`. They do not represent direct live root biomass or rock weathering. `GKR` and `GKF` keyed to **soil class**, not RLD or litter mass.
- This is a momentum-based raindrop+leaf-drip detachment model, **NOT an independently verified leaf-drip kinetic-energy law**, and differs from openLISEM `KE_LD` model and EUROSEM KE law.

## 4. Hydrology and sediment transport
- `OCmod.f90 OCSIM` L2206 onward uses block-tridiagonal implicit water-surface solve and face discharges `QOC(iel,1:4)`; dynamic shallow-water SWE inertia solver not identified. **Spatial 2D grid routing ≠ necessarily 2D full dynamic SWE**.
- `VSmod.f90 VSSIM` L4261/4399 includes unsaturated/groundwater infiltration (3D water architecture); no claim site Ks known from code.
- `SYCOLM` L1139–1296 receives sediment erosion source `GNU`, creates `DDLS=FETA*GNU*DTSY`, with `NSED` particle classes, `SOSDF` original soil grain fractions and loose layer `DLS,FBETA,PLS`; adds incoming flux, calculates available sediment and `SYOVTR` transport capacity or `FPCRIT` concentration cap; emits outflow `QSED` and updates loose sediment and moving particle concentration `FDEL`. Overland transport capacity can be Yalin or Engelund-Hansen (`ISGSED=0/1`). These capacity laws were derived for noncohesive channels and their applicability to shallow forest hillslopes uncertain (comment at top `SYmod`).
- `SYMAIN` scatters multi-class `QSED` across adjacent cells/faces by `ICMREF`. Channel `SYLINK`, `SYBED` and fine particle `SYFINE` allow channel bed layering and armouring. Channel armour ≠ time-varying postfire sandstone spall armour on hillslope.

## 5. Strong missing requirements/limitations
- **NO automatic rill incision**; Wicks & Bathurst (1996) SHESED paper expressly `sheet overland flow (without rilling)` DOI 10.1016/S0022-1694(96)80012-6.
- **NO morphodynamic feedback for hillslope elevation**: `SYMAIN` formal argument `ZGRUND(NEL)` is **INTENT(IN)**, while `GNU` is output and `DLS,FBETA,FDEL` are state updates; hence no lowering of overland land-surface topography on each erosion event, no topographic routing updates/rill incision in the current original sediment module. Channel `ARBDEP` changes but do not interpret this as hillside DEM Exner evolution.
- **NO original spatial per-stump stemflow or tussock funnel concentration**; original `DRAINA` is undifferentiated canopy drainage; hydrology expects PNETTO in each land cell.
- **NO root RLD to erodibility link**: `RDF` exists for evapotranspiration soil water uptake `ETmod` but `SYOVER` gets no RDF/root; GKR/GKF by soil class.
- **NO plant dynamic litter canopy floor biomass→FCG** unless external map/time forcing inputs supplied; `FCG` is user-assigned cover fraction. `FCROCK` static non-erodible land fraction, no spalling/weathering.
- **NO built-in sediment mass balance**: `BALSED` L4668–69 is stub, although water `BALWAT` called. `SYBC` time varying sediment boundary is also stub, per source header `SYmod`.
- Hourly/intense steep slope 10–50mm/h combined source/transport site predictions never run or calibrated here. Original example `examples/Cobres/model/rundata_cob.txt` points to `input_cob_syd.txt`, which has 7-grain/vegetation `XDRIP=3.0m,DRDRIP=.005m,FDRIP=.5,FCG=.3,FCROCK=0`; these are generic original example values not gounsa oak/grasses.
- Current SHETRAN source includes under-the-hood documented hazards ET zero canopy capacity `F1=CT1/CSTCAP` before guard, snowpack can retain stale DRAINA; should be tested before claims of numerical stability.
- No compiled native SHETRAN executable from this environment, no source edits, no results/benchmarks from current audit.

## Grounded primary sources
- https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/driver/run_sim.f90#L251-L346
- https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/evapotranspiration/ETmod.f90#L451-L531
- https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/evapotranspiration/ETmod.f90#L790-L819
- https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/sediment/SYmod.f90#L3463-L3500
- https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/sediment/SYmod.f90#L3658-L3806
- https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/sediment/SYmod.f90#L4413-L4520
- https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/sediment/SYmod.f90#L1139-L1296
- https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/sediment/SYmod.f90#L4660-L4672
- https://github.com/nclwater/Shetran/tree/cf9cd540add78ad3accbaf62b4199d2032887f6b/examples/Cobres/model
- https://www.sciencedirect.com/science/article/abs/pii/S0022169496800126

## 6. 정확한 2차원 지표유동 방식 (OCQGRD 추가 확인)
`src/overland_channel/OCmod2.f90` `OCQGRD` L909–1064: grid-to-grid shared face surface flux uses signed water-level head difference `DZ=ZI(1)-ZI(0)`, higher-side water depth `HM=ZI(HI)-ZGI(HI)`, flow-path length `L=LI(0)+LI(1)`, width-weighted Strickler `STRW`. It evaluates hydraulic conveyance `CONVM` through `CONVEYAN` and calculates `Q(LO)=CONVM*sqrt(abs(DZ))/sqrt(L)`, `Q(HI)=-Q(LO)`. Away from smoothing `CONVM≈K*W*h^(5/3)`. This is physically a **Manning–Strickler gradient-based diffusive-wave hydraulic face law**, computed on 2D planar grid; it is **not a full two-momentum-equation 2D Shallow Water Equations solver**. It supports four-face spatial flow paths but lacks resolved inertia/hydraulic shock on steep rough microtopography. Original `OCSIM` solves water depths implicitly by block-tridiagonal matrix with `OCQGRD` Jacobian. Proper comparison: SHETRAN = 2D spatial diffusive-wave surface hydrology plus fully coupled subsurface, whereas SWEHR and openLISEM full SWOF modes = true 2D dynamic SWE; **do not equate them just because both use raster cells**.
Original code: https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/overland_channel/OCmod2.f90#L909-L1064
