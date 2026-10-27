# 2026-10-27 SEIMS storm original source audit, quantitative isolation test and adopted-model decision

## Scope
The user requested **further published original model research with thorough actual code inspection**, independently from other Work's OpenLISEM source repair. Original source [lreis2415/SEIMS `dev`](https://github.com/lreis2415/SEIMS/tree/dev), original framework reference Zhu et al. (2019), DOI10.1016/j.envsoft.2019.104526. Existing [SEIMS model](../models/SEIMS.md) already rejected on the basis of kinematic sediment routing, but that early record DID NOT trace the storm CMake targets to outputs or check storm canopy module compiling and numerical transport units. This audit provides genuinely new evidence rather than a duplicate model name.

## Code path actually inspected
[Full source/blob audit](../models/SEIMS_2026_Storm_Source_Callgraph_Canopy_And_Sediment_Unit_Audit.md): 
- `erosion/CMakeLists.txt` includes `SPLASHERO_PARK`, `KinWavSed_OL`, each has `ADD_LIBRARY SHARED` in respective CMake.
- `erosion/SPLASHERO_PARK/api.cpp` input `VAR_NEPR` [mm], output `D_DETSplash` [kg], leaf drainage metadata **commented out**.
- `SplashEro_Park.cpp:173–191` rainy detachment formula via `NEPR`, `USLE-C`, `USLE-K`, wet-surface shielding. Does not model leafdrip kinetic energy.
- `KinWavSed_OL/api.cpp` takes `D_DETSplash`, `FLOWIN_INDEX`, `ROUTING_LAYERS`, and `D_QOverland`. `KinWavSed_OL.cpp:318–341` `m_Sed_kg += Dsp + Df`, checks transport capacity and deposits excess. `OverlandflowSedRouting:493–496` sediment imports from `flowInID` network. Thus **source+flow erosion and deposition do exist as connected native module functions**, but **the sediment solver is directed kinematic topology, not free signed X/Y SWE**. Original source includes no per-cell active soil depth to limit extraction and no dynamic DEM update in the verified functions.
- `hydrology/PI_SVSC/Interception_SVSC.cpp` seasonal cap `Smax(day)`, net rain output, **no LAI read in active interface and no canopy-drip KE**. SEIMS may reduce actual reaching rain for splash but must not call this measured LAI canopy-drip erosion. Source storm mode excludes ET from this module.

## Newly identified build and numerical concerns
### PI_MCS under STORM_MODE expected compile failure (source-level, not full build)
- `PI_MCS/Interception_MCS.h` member `m_pcp` exists but `m_P` absent; `Interception_MCS.cpp:132` references `m_P` only under `#ifdef STORM_MODE`.
- `Interception_MCS.cpp:64 and 75` `SetValue(... value)` assigns `m_hilldt=data` (undeclared name in that method).
- Both `PI_MCS` and `PI_SVSC` are distinct CMake built targets. So **only assert source-level PI_MCS storm branch compile blockers**, not entire SEIMS binary cannot run. Developer compiler defines/build flags in actual user workflows not exercised.

### Strong dimension inconsistency in KinWavSed_OL
- `KinWavSed_OL.cpp:263–279` Manning `m_V` [m/s] using `m_WH /1000` (mm to m).
- `WaterVolumeCalc:395–403` repeats `m_WH/1000` depth conversion.
- But `GetTransportCapacity:299` sets `q=m_V*m_WH*60`, and comment declares q area discharge [m²/min]. **Must divide depth by 1000 for unit-consistent area flux**, otherwise native q numeric ×1000 relative SI intended. Branch is selected using q=0.046, so code may shift mathematical regime and magnitude.
- Independently compiled C++17 isolated test [source](../code_audits/SEIMS_TransportCapacity_UnitProbe.cpp), [output](../code_audits/SEIMS_TransportCapacity_UnitProbe_Output.txt) uses example v=0.1 m/s, depth=5mm, slope=0.2, K=0.3, eco1=eco2=1; native q30 vs qSI0.03, branches HIGH q² vs LOW sqrt(q); capacity1.765045 vs0.339683 (5.196x). **NOT original SEIMS full build or field-result error ratio**; only source formula sensitivity.

## Hard gates
| User must-have | Same released SEIMS source |
|---|---|
| Public C++ source and actual storm erosion CMake target | **YES** |
| Rainfall+overland separate source and sediment capacity deposition | **YES, module path inspected** |
| LAI → canopy dynamic storage+throughfall and drop-energy in soil erosion | **NO, Net rain only and USLE C** |
| Fully independent X/Y SWE + sediment flux at each cell face | **NO, FLOWIN_INDEX network** |
| Exact published true 5cm/10cm vegetation+sediment native | **NO precedent found** |
| Proven native sediment mass/time/soil finite stock stability | **NOT TESTED**, suspect transport unit inconsistency |
| Exact 2019 paper solver = inspected 2026 dev branch | **NOT ESTABLISHED** |

**Strictly reject SEIMS as user's operational high-res original.** Retain as evidence that *real modules* can be compiled and linked but sub-process provenance and units require audits. Do not present this as a way to rescue the other Work's OpenLISEM, or as a replacement without a published native all-condition benchmark.

## No fictional completion
No complete SEIMS build, no source patch, no water+sediment simulation, no 5cm observed DoD. Exact source read and one self-contained isolated compiled C++ calculation actually performed.

## URL
https://github.com/lreis2415/SEIMS/blob/dev/seims/src/seims_main/modules/erosion/KinWavSed_OL/KinWavSed_OL.cpp
https://github.com/lreis2415/SEIMS/blob/dev/seims/src/seims_main/modules/hydrology/PI_MCS/Interception_MCS.cpp
https://github.com/lreis2415/SEIMS/blob/dev/seims/src/seims_main/modules/hydrology/PI_SVSC/Interception_SVSC.cpp
