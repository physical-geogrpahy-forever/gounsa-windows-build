# 2026-10-28 OpenLISEM 원본 7.5.2 복구 가능성 재감사

## 확정 결론
**지금 시점에서 원본 OpenLISEM 7.5.2는 고운사 유수침식 주모델 NO-GO 유지.** 소스의 일부 결함은 단위수정 가능하나 2D 강우/유수침식의 안정적 복구는 증명하지 못했다. 코드에 기능 존재와 수치/물리 검증 성공은 다르다. 고운사 요구한 5~10cm 완성 모델로 추천하지 않는다.

## 기존 원본 실제 Windows 12회 실행
- Github Actions https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304135775 : 5m, 100x100m, slope25%, 20mm/h for1h +10min drain, native 2D open boundary, SHA256 recorded f8a5722ed0b370f32fb3dae5c55465427abe75b1155b50bf12aa5516d6b4ca79 .
- Oak scheme1 exported sediment (kg/ha) at dt5,10,20s: 0.005993, 123.037727, 832.588686.
- Oak scheme3 (kg/ha): 0.030954,28.707586,268.530307.
- Miscanthus scheme1: 0.004050,0.007095,238.256810; scheme3:0.018893,0.044177,88.121322.
- Aggregate water/sediment ledger can close but not imply per-cell physical available soil mass or timestep convergence. Native Oak dt20s cell erosion 5982.901t/ha vs 25cm assumed soil supply3375t/ha. Earlier extra dt1/2s action40304815539 and 2m action40303685346 timed out, no new stable fine-mesh results.

## Native source direct verification
- Official v7.5.2 and current main_C versions of erosion/lisErosionAux.cpp have identical SHA 019a31f7233352c9347407906b9f641e27e60582. Also erosion/lisSWOF2DSediment.cpp is identical SHA683eb85b59da4a74b95363374efb223c094e933b. Changing branch does not fix these flaws.
- GetSV sediment diameter measured in micrometers. At diameter >=100um, code incorrectly uses dm = d/1000.0 and sqrt(1 + X - 1) grouping. Standalone g++ C++17 compiled reproduction from source expression with gravity9.81, calibration1 gave 50um0.002248125m/s, 99.9um0.0089745239925m/s, 100um1.2722617655181m/s, 100.1um1.2728977374481m/s. This is a deterministic physical jump, but not established as sole cause of exported sediment variability. Native alternate option tested before and also failed.
- In model/lisDataInit.cpp, SwitchUseMaterialDepth is false. In erosion/lisSWOF2DSediment.cpp SedimentSSContinuous, DetachMaterial call commented out and some concentration cap commented out. Hydrological soil depth is not inherently erosion finite sediment stock. Re-enabling without proper deposited-layer and soil mass ledger is not a valid trivial patch.
- flow/lisSWOF2DopenMUSCL.cpp actual flow timestep controls inside findSmallestCFLdt: qMax(TimestepfloodMin,dt_req_min), possible CFL violation when floor exceeds stability requirement. Actual 5cm native CFL has NOT been measured, so classify this as a potential issue.
- SWOFSedimentAdvection loops with OpenMP pragma and in a scatter pattern updates tma/tmb/tmc/tmd neighbor cell map buffers by += without explicit atomics or reduction. Possible data race if cells concurrently target same buffer; requires threads1 vs multi reproduction. Do not report confirmed runtime race.
- Outgoing sediment dss calculated from dt, velocity, concentration; coded separate outgoing reduction is not explicit min(available sediment), with related cap commented. Sediment positivity/finite mass not validated.

## What would be needed if one attempts a separate scientific fork
1) Pin source SHA and Windows executable, exact matching runfile and grids. Correct/test settling term as a single A/B change, do not modify physical parameter to mask failures.
2) Isolate threads1 vs multiple threads; test 2D conservative sediment advection; inspect hydrodynamic internal CFL behavior, not only external timestep.
3) Implement/verify finite original soil mass + mobile deposited sediment separately, water/sediment/bed mass and elevation, no mass creation by recurring redetachment.
4) Re-run native baseline and 5/10cm for water and sediment export, local deposition and DoD, input canopy ON/OFF under otherwise identical conditions; convergence tolerance and positivity must be met. Until full test, a fork is a modified model, NOT the original independently validated model.
5) Given the user's strong preference for published ready-to-use physical model and repeated failure, **do not make OpenLISEM fork rescue mainline** before demonstrable independent numerical and field validation.

## Provenance
- https://github.com/vjetten/openlisem/tree/v7.5.2
- https://github.com/vjetten/openlisem/tree/main_C
- https://github.com/vjetten/openlisem/blob/v7.5.2/erosion/lisErosionAux.cpp
- https://github.com/vjetten/openlisem/blob/v7.5.2/erosion/lisSWOF2DSediment.cpp
- https://github.com/vjetten/openlisem/blob/v7.5.2/flow/lisSWOF2DopenMUSCL.cpp
- Previous project decision: 2026-10-27_OPENLISEM_752_SOURCE_NATIVE_REAUDIT_NO_GO.md
