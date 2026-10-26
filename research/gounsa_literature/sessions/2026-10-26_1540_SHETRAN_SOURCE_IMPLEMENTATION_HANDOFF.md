# SHETRAN 실제 구현 감사 인계 (2026-10-26)

## 핵심
SHETRAN 4.7.2.0 공개 원본 Fortran commit `cf9cd540add78ad3accbaf62b4199d2032887f6b` 수문/유사/식생 함수 호출경로를 순서대로 감사. **원본 실행/컴파일은 이 세션에서 하지 않음**, 위조된 모델실험 없음.

## 원본 함수 실체
- `driver/run_sim.f90` L272 ETSIM, L276 VSSIM, L295 OCSIM, L311 SYMAIN in this exact event-timestep order. All components alive in original code with BEXSY enabled.
- `evapotranspiration/ETmod.f90` ETSIM→ETIN→ET: per-class `CPLAI=PLAI*min(CLAI,1)`, dynamic `CSTORE` capacity CSTCAP and CK/CB drainage, canopy evaporation, `PNETTO` effective rain and `DRAINA` canopy discharge to soil.
- `sediment/SYmod.f90` SYMAIN: SYWAT gets `FCC`, effective free rain `LRAIN`, drip `DRAINA`, raindrop diameter, water depth, shear `TAUK`. SYOVER: `GMR` free rain momentum; `GMD` canopy drip momentum from XDRIP[m], DRDRIP[m], FDRIP; rainsplash erosion `DR=GKR*depthbuffer*(1-FCG-FCROCK)*(GMR+GMD)`; flow erosion `DF=GKF*(1-FCROCK)*max(0,tau/tauc-1)`; hillslope `GNU=(DR+DF)/RHOSO` if `DLS<DLSMAX`. FCG impacts rain only, rock impacts both; GKR/GKF soil type, not roots/biomass/RLD.
- `SYCOLM` mixes source erosion with sediment PSD/SOSDF, loose layer DLS/FBETA, mobile FDEL; 4-face transport capacity Yalin/Engelund-Hansen, `QSED` per size and neighbor face. `SYLINK` & `SYBED` channel sediment, `SYFINE` channel armouring. Soil surface `ZGRUND` passed `INTENT(IN)` so cannot develop rills/soil topographic surface lowering.
- `overland_channel/OCmod2.f90::OCQGRD` computes `Q=CONVM*sqrt(abs(∆z))/sqrt(L)`, Strickler/Manning diffusion wave on 2D grid; **not full SWE dynamic wave**. `OCmod::OCSIM` implicit matrix, neighbor 4-face `QOC`. Distinguish '2D spatial' from 'full 2D SWE'.
- `BALSED` sediment mass report **empty stub** in `SYmod.f90` L4668–69; original numeric sediment balance not demonstrated.
- No individual plant/tussock stemflow routing, dynamic vegetation root biomass to erodibility, fire sandstone spall weathering/fragment redistribution; original Wicks Bathurst (1996) SHESED explicitly states sheet flow without rilling. FCG/FCROCK source input fraction not direct biomass and root mechanics.
- `CSTCAP=0` CT1/CSTCAP division pre-guard, snow model branches DRAINA stale risks in source comments; model edge testing needed.
- Published original Cobres example `rundata_cob.txt` includes sediment yield input, sample XDRIP3m DRDRIP5mm FDRIP.5 7 grain classes, not site measurements. No attempt to execute or reparameterize.

## New permanent records
- `research/gounsa_literature/decisions/2026-10-26_SHETRAN_472_NATIVE_IMPLEMENTATION_CALLGRAPH_AUDIT.md` exact 11k source-based source-to-output process.
- `research/gounsa_literature/models/SHETRAN.md` current model ancestry + in-depth implementation audit and 2D diffusive wave correction.
- `research/gounsa_literature/MASTER.md` `INDEX.md` updated.
- Wicks&Bathurst 1996 original abstract https://www.sciencedirect.com/science/article/abs/pii/S0022169496800126
- Original source https://github.com/nclwater/Shetran/tree/cf9cd540add78ad3accbaf62b4199d2032887f6b

## Next steps
- If the original source is accepted as a hydrologic/sediment process candidate, **build and run original Cobres sediment-on example without source changes**, verify canopy storage/recession response and sediment independent mass conservation (native BALSED stub means source-ledger derived QA needed). Report failure with logs if build fails; do not invent outputs.
- Decide whether original 2D diffusive-wave without rills or morphodynamic feedback satisfies the Gounsa central event TLS objective. If not, compare against original openLISEM FullSWOF source that has full dynamic SWE, original canopy/leaf-drip/rock/grass erosion, with genuine Windows executable/source identity verification.
