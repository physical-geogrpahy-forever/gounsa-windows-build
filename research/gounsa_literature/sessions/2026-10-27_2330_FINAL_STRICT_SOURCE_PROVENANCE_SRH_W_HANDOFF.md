# 2026-10-27 고운사 "마지막" 요청 인계: SRH-W 2009 학술논문 대 2007 공개 hydro-only 판본

## 작업
- 사용자: 기존 작업 품질 불만, 원본 코드 철저 확인을 최종 요구. OpenLISEM 수정은 다른 Work에게 맡긴 역할 분리 유지.
- `SYSTEM.md`, `MASTER.md`, `INDEX.md`, 최신 `decisions`, 실제 과거 서지와 공개 소스 감사 중복 확인. 이전에 검토한 Doten DHSVM, Wflow.jl, SWAT+, SPHY-MMF, tRIBS-FEaST, LISEM, HydroSed2D, Le2015 FullSWOF-HR 등 재등재 없이 비교.
- 새 DOI/서지 [Lai (2009)](../papers/2009_Lai_SRH_W_HybridMesh_2D_Watershed_Erosion.md), DOI10.1061/(ASCE)1084-0699(2009)14:1(15), 2D hybrid-mesh FV watershed flow+erosion paper found at ASCE publisher.
- [2007 SRH-W v1.1 U.S. Bureau of Reclamation official manual](https://www.usbr.gov/tsc/techreferences/computer%20software/models/srh2d/downloads/SRH-W%20v1.1%20User%20Manual%20June2007.pdf) indexed §1.3 states **only flow and runoff; erosion and sediment not yet released**. Manual also describes land-use interception **depth** and Green-Ampt, not observed dynamic LAI leaf-drip. The PDF is 11.8MB and web.open rejected (tool size), so quote is supported by exact indexed excerpt not entire visual PDF. 2009 paper possible future extension is real but corresponding source, 5cm mesh, forest canopy unknown.
- U.S. Bureau modern [SRH-2D 3.3.1](https://www.usbr.gov/tsc/techreferences/computer%20software/models/srh2d/index.html) river sediment downloadable EXE, but is not exact 2009 modified SRH-W source. Do not treat modern river program as 2009 2D watershed rainfall-interception source.
- Extra GitHub repository discovery [Daishubinghydraulic/Shallow-water-equations-with-Hairsine-Rose-soil-erosion-equations](https://github.com/Daishubinghydraulic/Shallow-water-equations-with-Hairsine-Rose-soil-erosion-equations) `README.md` blob `1ffff75bfe2426bf1d9a3ba8bfe99c4892bcc5fe`: original VBA Excel hill-slope roll-wave model, paper merely **submitted**, no peer-reviewed DOI confirmed, full XY/canopy source not verified. Unqualified, so no duplicate paper file.
- Search of exact FullSWOF-HR study source and Hairsine-Rose code returns no exact 2015 modified solver; hydrodynamic baseline only. Prior independent source audit remains binding.
- NO numerical sim, compile, new native benchmark in this session. Source search, paper versions and actual code audit archival; do not claim running success.

## GitHub changed
- new [Lai 2009 paper](../papers/2009_Lai_SRH_W_HybridMesh_2D_Watershed_Erosion.md)
- new [final decision](../decisions/2026-10-27_FINAL_STRICT_ORIGINAL_SINGLE_MODEL_SOURCE_GATE_SRH_W_AND_RECENT.md)
- [MASTER.md](../MASTER.md) strict conclusion
- [INDEX.md](../INDEX.md) updated at time: Papers508; Models110; Decisions108; concurrent work may increase further
- this handoff

## Practical Gounsa decision
No FULL matching **published 5–10cm native free source, LAI canopy time dynamics, unconstrained four-side true XY 2D water+rain/flow sediment/deposition with mass&mesh numerical stability** software independently verified. This does not prove mathematically impossible. Current only conditional research-engine route is Classic LISEM line being numerically repaired/checked by separate Work; **past native failure not erased**. Without Work successful test, do not announce adopted. Do not invent patched integrated "existing" model.

## Binding minimum test
(a) identical article executable and source commit; (b) tested dx 0.1m,0.05m and known p=10/30/50mmh 6h; (c) canopy ON vs OFF mass and leaf drip KE path; (d) all-edge free 2D x/y; (e) positive h/c, finite soil mass, two sediment terms active and local erosion/deposition; (f) dt/mesh convergence and simultaneous water+sediment closure. If any not met: non-candidate.
