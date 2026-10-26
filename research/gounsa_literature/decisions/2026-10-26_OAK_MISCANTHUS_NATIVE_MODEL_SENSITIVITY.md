# 2026-10-26 고운사 참나무 맹아형 대 억새형: 원본 EUROSEM/SWEHR 식생-수문-침식 민감도

## 핵심 판정
원본 물리 모형을 실제 실행하여 가상 식생구조 변화가 관측량을 바꾸는 것은 확인했다. **이는 참나무 맹아와 억새의 실제 침식량 크기 및 우열을 검증했다는 뜻이 아니다.**
- SWEHR: 50/50 민감도 시나리오 물수지, 독립적인 원토양 박리-퇴적층-부유사-경계배출 유사수지 통과.
- EUROSEM: 59/60 수문 물수지 통과. 1개(SPLTEX=1 OAT) 실패. **독립 유사수지 검증 0/60**.
- EUROSEM native INTERC 수관차단/직접 수관통과우/수관적하/수간유하 분배는 실제 원본 Fortran 호출 결과다.
- SWEHR는 original solver에 유효강우를 균일하게 공급한 것일 뿐, SF 지점 집중과 수관적하 KE를 연결하지 못했다. 정확히 이 **공간적 coupling 부재** 때문에 두 식생의 지표침식 차이를 실제 연구결론으로 확정 불가.
- 2026-09-22 production primary engine Iber+ 선택을 SWEHR/EUROSEM으로 재변경하지 않는다.

## 실행 및 산출물
- Native EUR Fortran src sha 8652944da6e1e8436495aa0c08765e2399830dd7, SWEHR native C sha 4e6f783f335ac6dc1c116ef0d516c2f3d1b911e2.
- SWEHR 실행: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40258199435
- EUROSEM 실행: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40258483367
- 결합 감사를 통한 실제 결과표/OAT: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40258842917
- 브랜치: `swehr-water-sediment-closure-20261026`, `experiments/rainfall_10_50/run_species_sensitivity.py`, `analyze_native_ensembles.py`, `species_sensitivity_native.yml`, `analyze_native_species.yml`.
- 시험 조건: 1시간 강우 10,20,30,40,50mm/h; EUROSEM 14500m² 원본 시험사면(100m×145m, SIR=0.85), SWEHR 3×51격자, dx0.25m(9.5625m²). 서로 다른 지형/면적이므로 절대 t/ha 결과 모형 간 직접 교차검증 안됨.

## 입력(현장 실측값 아님!)
공통 native EUROSEM original default: FMIN=5mm/h, Manning n=0.188, EROD=0.9 g/J, SPLTEX=2, SIR=0.85, original DERO=5m(얕은 고운사 토심이 아님), PBASE=0.05.
- 참나무 맹아형 *가정*: canopy COVER=0.55, DINT=1.5mm, SHAPE=2(활엽), PLANGLE=55°, PLANTH=2.5m.
- 억새형 *가정*: COVER=0.75, DINT=1.5mm, SHAPE=1(가느다란 잎), PLANGLE=75°, PLANTH=1.2m.
- EUROSEM hydraulic surface extra *arbitrary exploratory*, neither measured: oak FMIN10mm/h, Manning n0.14, EROD0.7, SPLTEX1.6; miscanthus FMIN7mm/h, n0.24, EROD0.65, SPLTEX1.5. Root biomass or RLD were **not** actually input, nor were their quantitative published functional relationships included. Soil contrast is a sensitivity perturbation only; not evidence oak roots better.
- SWEHR same-conditions Ksat=2e-6m/s, Manning n0.1, `a=ad=0.25`, `F=0.004`. Native SWEHR cannot take original EUROSEM partition in spatial 2D; only total uniform `P-I` applied over event, with `I=COVER×DINT×(1-exp(-P_mm))` reconstructed from published EUROSEM canopy storage relation.
- SWEHR hypothetical plant-soil additional: oak Ks=4e-6, roughness0.13, a0.18/ad0.22/F0.003; miscanthus Ks2e-6, roughness0.2, a0.12/ad0.17/F0.0025. These ratios have not been derived from measured stems, litter, macropore or root biomass. They should **not** be adopted as production parameters.

## EUROSEM native canopy partition at 30mm/h
| output mm | Oak assumed | Miscanthus assumed |
|---|---:|---:|
| Incident rainfall | 30 | 30 |
| Initial event canopy storage | 0.825 | 1.125 |
| Direct free throughfall | 13.500 | 7.500 |
| Leaf drip | 6.685788 | 16.216140 |
| Stemflow | 8.989212 | 5.158865 |
| Ground net rainfall (TF+drip+SF) | 29.175 | 28.875 |

Native interception ledger closure exact to 1e-6mm; genuine original INTERC source instrumentation, no novel canopy equation replacing process.
CRITICAL limitation: original EUROSEM shape2+55° results in oak stemflow 30% of rain. This is much higher than some observed oak/coppice field examples, so not a species-specific realistic point estimate. Angle/shape OAT shows runoff and sediment summaries unchanged even when stemflow versus drip changes, because mass is routed back into an areal rainfall field rather than spatial stem-base inlet. This is a structural deficiency for the user's stated main question, not proof that stemflow location cannot matter.

## EUROSEM hydrological sensitivity, same soil, hypothetical canopy change
| R mm/h | Oak runoff mm | Miscanthus runoff mm | Oak reported net soil erosion t/ha (NOT independently conserved) | Miscanthus net t/ha (NOT independently conserved) |
|--:|--:|--:|--:|--:|
|10|0|0|0|0|
|20|0|0|0|0|
|30|3.70813|3.49095|28.53297|26.87483|
|40|12.04206|11.77425|91.31517|89.32207|
|50|21.30961|21.02557|159.369|157.3097|

Native runoff changes modestly (~5.9% at 30 mm/h) under canopy-only assumptions; sediment numbers are explicitly **unverified output** and have no physical validation as event exported sediment yield. 50mm/h >150t/ha is outside a credible Gounsa inference without erosion depth constraints, sediment flux, observed erosion and bulk density.

## SWEHR true water and independent sediment closure under homogeneous net rain
| R mm/h | Oak runoff mm | Miscanthus runoff mm | Oak exported sediment t/ha | Miscanthus exported sediment t/ha |
|--:|--:|--:|--:|--:|
|10|0.1991863|0.0822334|0.000000615|0.000000251|
|20|8.884832|8.603182|0.00028937|0.00026104|
|30|18.43071|18.14136|0.00402466|0.00378437|
|40|28.13230|27.84000|0.02107582|0.02024102|
|50|37.90527|37.61137|0.06434977|0.06257729|

SWEHR last column is integrated signed boundary sediment export and total-erosion/loose-layer conservation was independently tested. 30mm/h: under fixed soil, grass hypothetical profile gives ~6% less boundary export. This is caused by **assumed event interception only** (0.3mm difference), not SF localization, root structure, or rainfall drop KE. Thus it does NOT prove 6% lower erosion under grass in Gounsa.

## Additional hypothetical soil differences: direction NOT robust
EUROSEM 30mm/h net erosions: oak hypothetical 0.00749 t/ha vs grass 4.58 t/ha (unverified sediment flux); SWEHR 30mm/h export: oak 0.0003378 vs grass 0.0005570 t/ha, i.e. reversed from canopy-only ordering. At 50mm/h SWEHR exports oak 0.01367 vs grass 0.00622 t/ha, reversing *again*. Consequently the species rank is **not identifiable from these hypothetical inputs**. Report mechanism sensitivity and confidence, not ecological causation.

## 30mm/h OAT true model sensitivity
- EUROSEM original: `FMIN` 3→20 mm/h: runoff 0~8.447mm and reported net erosion 0~64.56t/ha. `COVER` 0→0.9: runoff 3.328~4.325mm and reported net 25.63~33.23t/ha; `DINT` 0.5→3mm runoff 3.114~4.116mm; `PBASE` 0→0.1 runoff 3.212~4.186mm. Other plant SHAPE/PLANGLE/PLANTH runs changed native component rain partition but NOT final runoff/sediment in this one-plane test.
- EUROSEM `S` OAT changed main plane slope .3→.85 but runoff/sediment unchanged because original source sets `s(j)=sir(j)` in non-rill test; `SIR` stays .85. **Do not claim slope-independent physics.** Likewise EROD/SPLTEX changes had little/no numerical effect in this test configuration, not universally in all EUROSEM erosion dynamics; SPLTEX=1 OAT failed.
- SWEHR original: `Ks` 0→8e-6 m/s varied runoff ≈0→27.47mm, sediment export ≈0→0.01752t/ha; `F` .001→.01 varied export .000559→.01869t/ha; Manning .05→.3 export .000480→.00854t/ha; `a` .05→1 export .00330→.00673t/ha; `ad` .05→1 nearly unchanged; changing event canopy loss 0→4mm changed runoff 15.38→19.23mm and sediment export .00200→.00475t/ha.
- Both engines: canopy/shape comparison is less diagnostic of sediment export than hydraulic soil response and surface erodibility, **given the chosen non-spatial canopy coupling and benchmark conditions**.

## External evidence, not site calibration
Holder et al. 2018 DOI 10.1111/gcbb.12503: UK 6ha Miscanthus × giganteus event/annual field measurements 776mm gross, 455mm TF, 133mm SF, 188mm interception across period; 24% interception and 17.1% SF observed over many events, not 1h extreme rainfall. This is another Miscanthus species and different soil and slope. See papers/2018_Holder_Miscanthus_CanopyPrecipitation.md. Deciduous oak forest understorey field observations and evergreen oak coppice intercept/SF from different climates give very wide event ratios; no direct Gounsa M. sinensis or oak-resprout biomass/stand geometry measured here.

## Remaining prerequisites
1. Derive each plot's hourly canopy storage/canopy partition from terrestrial LiDAR and paired TF/SF field measurements. Measure per-stem (oak sprouts and Miscanthus culms) stem diameter, stem count and leaf angle for physically spatial SF.
2. Per-cell 2D ground precipitation including SF localization plus leaf-drip KE; per-cell mass conservative supply, explicit new coupling; separate local macropore Ks and pre-fire hydrophobicity and actual soil water contents.
3. Keep root biomass or RLD and litter mass as independent vegetation states; **never equate canopy COVER to those states**.
4. Use the actual Gounsa 2D LiDAR terrain, shallow stony soil depth and particle-size profile (not EUROSEM demo SIR=.85, max erosion depth 5m, nor SWEHR 9.56m² artificial DEM).
5. Confirm computed annual/event comparison and independent sediment boundary flux in EUROSEM, then compare to TLS bed changes and sediment trap rates.
6. Do not change primary selected Gounsa Iber+ event erosion solver due to diagnostic experiment without a separate decision.
