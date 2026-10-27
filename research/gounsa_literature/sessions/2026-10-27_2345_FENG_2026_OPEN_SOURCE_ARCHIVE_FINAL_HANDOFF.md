# 2026-10-27 23:45 마지막 독립 코드/논문 재검증 인계

## 사용자 역할 및 원칙
OpenLISEM 코드 수치오류 복구·5cm/10cm 원본 실행은 다른 Work가 담당. 이 세션은 동일모델 미입증 논문/코드를 엄격히 구분하면서 새 공개모델을 조사. 시작 시 SYSTEM, MASTER, INDEX, 기존 SERGHEI_SE/Braga2026 원본 판정 등 읽음.

## 진짜 신규 2026 학술자료
- Feng, Tan, Xu, Li, Bisht (2026) [WRR DOI10.1029/2025WR042040](https://doi.org/10.1029/2025WR042040). Wiley full methods/Results/Availability inspected; first published 2026-05-11.
- Actual ELM land surface (runoff + raindrop and runoff erosion) + TELEMAC-2D SWE + GAIA multiclass sediment and Exner, 2026 author-modified GAIA to accept ELM hourly area sediment mass sources. Published combined/linked framework, **not single original software**.
- Shared JIGSAW Delaunay unstructured grid 442277 triangular cells, min30m, secondary90m, outer1000m. Source ELM hourly, TELEMAC smaller internal time step, 2017 Harvey Houston 1336km². 16 USGS gauge water level median R²0.83 and KGE0.78. This is not 5cm rainfall canopy simulation.
- **[Zenodo revised source release v2](https://zenodo.org/records/18331808) DOI10.5281/zenodo.18331808**, `Data_Scripts_Harvey_Sediment_v2.zip` 8.2GB MD5 efdf94753cd7f29cd8476bf71abb9ff6. Contents list says src/ modified TELEMAC/GAIA source, Data/ simulated outputs and USGS, Scripts/ analysis/figure, shpfiles/ GIS. Real public deposited revised source metadata YES, but ZIP 8.2GB **not downloaded, source inside not read, compile/run not performed**.
- Canonical paper [here](../papers/2026_Feng_Tan_Xu_Li_Bisht_ELM_TELEMAC_GAIA_Harvey_Sediment.md); [strict decision](../decisions/2026-10-27_LAST_CHANCE_2026_FENG_ELM_TELEMAC_GAIA_30M_SOURCE_VS_SINGLE_NATIVE_GATE.md).

## Already indexed 2026 benchmark check: not newly counted
- Braga et al.(2026), DOI10.3390/w18151870, previously indexed [canonical](../papers/2026_Braga_SERGHEI_SE_Finite_Volume_Evaluation.md). Genuine 2D finite-volume sediment and Exner; **5mm erodible dam-break** test is not rainfall. Actual rainfall hillslope/V-catchment **1m**, vegetation canopy water interception and leaf drip future work. No change to strict Gounsa exclusion.
- Classic LISEM full canopy/sediment original remains under numerics Work; prior 12-run erosion failure not overturned. No native simulations in this session.

## Archive
- New paper Feng2026, decision, MASTER summary, INDEX 509 Papers and 110 Decisions at final update; model count unchanged. This handoff.

## Final decision
No verified publicly published native same-engine 5–10cm *forest LAI canopy water and leafdrop impact* + free xy 2D sediment rain/flow erosion/deposition + real event mass&time convergence. Feng provides real 2026 research code archive but 3-model 30m not applicable. No adoption. Publication process, code existence, and native numerical acceptance must remain separate.
