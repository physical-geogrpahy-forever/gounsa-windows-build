# 2026-10-27 23:02 고운사 독립 비LISEM: SEIMS CMake→rain/flow sediment→canopy→unit rigorous audit

## User priorities
OpenLISEM is assigned to parallel Work and excluded. Seek another published, actually same-version downloadable source engine at actual native 0.05–0.10m, X/Y free SWE, LAI canopy water storage and soil-reaching drop energy, separate rain/runoff detachment and local sediment/deposition. User explicitly says **코드 철저히 확인**, so no model name-list-only answers.

## Source fully inspected
`lreis2415/SEIMS` branch `dev` (not exact 2019 paper git SHA): dynamic erosion CMake `SPLASHERO_PARK` and `KinWavSed_OL` both included, plugin APIs outputs `D_DETSplash` and inputs `D_DETSplash` + `D_QOverland`. In `KinWavSed_OL::GetSedimentInFlow`, native sediment inventory gets `Dsp + Df` then concentration beyond transport cap deposited, while `OverlandflowSedRouting` uses fixed `flowInIndex` network (not free XY 2D). `SPLASHERO_PARK::Execute` gets `VAR_NEPR` canopy net rain, multiplied by USLE C, no active leafdrip kinetic energy input (api comment). `PI_SVSC` interception uses seasonal max/min storage, no native LAI parameter. Internal storm `PI_MCS` has source-level undefined `m_P` and `data` inside STORM_MODE conditional branch; alternatives exist so no global compile verdict.

## New quantitative source concern
`KinWavSed_OL.cpp` `m_WH` is mm via L263/266/395/400, `m_V` Manning m/s; `GetTransportCapacity` L299 multiplies `m_V*m_WH*60` and labels q m²/min, without /1000. This shifts q 1000× and conditional threshold 0.046. Independent C++17 compiled sample v0.1m/s depth5mm slope0.2 K0.3 eco1/eco2=1: raw q30, unit-corrected q0.03, capacity 1.76504521624 vs0.339683110243; branch high vs low. Units 1000x not universal total sediment error factor. Full native SEIMS package not built or executed. 
- [Full model audit](../models/SEIMS_2026_Storm_Source_Callgraph_Canopy_And_Sediment_Unit_Audit.md)
- [Decision](../decisions/2026-10-27_SEIMS_STORM_SOURCE_BUILDTARGET_LAI_AND_TRANSPORT_Q_UNITS_NOGO.md)
- [C++ isolated probe](../code_audits/SEIMS_TransportCapacity_UnitProbe.cpp)
- [Probe result](../code_audits/SEIMS_TransportCapacity_UnitProbe_Output.txt)
- Existing canonical `models/SEIMS.md` should reference expanded audit.
- Update INDEX (add 1 model, 1 decision; code audit directory excluded from model index).
- Update MASTER top summary and count.

## Decision
No all-pass engine found; SEIMS robustly NO-GO due directed routing, canopy drip energetics absent, no real 5cm trial, plus native source q units risk. Distinguish actual executable plugin CMake from selected workbench configuration and checked formulas from observed native QA.
