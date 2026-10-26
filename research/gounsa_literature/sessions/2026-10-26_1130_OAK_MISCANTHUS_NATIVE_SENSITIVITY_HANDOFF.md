# 고운사 원본 침식모형과 억새/참나무 맹아 시나리오 민감도 인계

## 금일 신규 작업
- EUROSEM original Fortran의 native INTERC 출력에 instrument-only CANOPY_QA를 추가하여 interception/free throughfall/leaf drip/stemflow를 별개 숫자로 검증함.
- SWEHR 기존 네이티브 C 기존 Hairsine-Rose 원본 및 Green-Ampt 시험값을 고정하는 경우와 Ks, roughness, a/ad/F 민감도를 별도로 총 50개 실행. 50/50 water+independent soil mass closure pass.
- EUROSEM original fixed F77 single plane test에서 cover/storage/shape/angle/height/pbase/fmin/manning/erod/spltex/slope 변수를 바꾸며 60개 실행. 59/60 native water pass, single SPLTEX 1 failed, sediment independent balance none.
- 참나무/억새 값은 모두 공개 원본의 *가상 식생구조 매개변수 가정*, Korean oak coppice/Miscanthus sinensis field observations 아님.
- original 10,20,30,40,50mm/h ×1h 전체 사례와 OAT 숫자는 native branch 스크립트 + GitHub Actions 아카이브 ZIP에 보존.
- 민감도 주요 결론: 같은 soil EUROSEM 30mm/h oak runoff 3.708 vs Miscanthus 3.491mm, original native SF 8.99 vs 5.16mm; SWEHR canopy-only exported sediment 0.004025 vs 0.003784 t/ha. 그러나 EUROSEM native SF 공간 위치가 지워지고, SWEHR는 유효강우 균일 forcing만 사용함. soil Ks/roughness 가정을 바꾸면 결과 방향이 뒤집혀 species soil-erosion rank 결론 불가능. EUROSEM net sediment 28.53 vs26.87 t/ha는 독립 sediment balance 미통과이므로 과학적 채택 불가.
- model primary decision Iber+ / SSSPAM 유지.
- 새 문헌: papers/2018_Holder_Miscanthus_CanopyPrecipitation.md. 추가 결정: decisions/2026-10-26_OAK_MISCANTHUS_NATIVE_MODEL_SENSITIVITY.md; MASTER, INDEX 갱신.
- 110 native cases summary + OAT https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40258842917
- raw native EUROSEM 60 cases https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40258483367
- raw native SWEHR 50 cases https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40258199435
- branch https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/swehr-water-sediment-closure-20261026/experiments/rainfall_10_50

## 잔여 우선순위
1. 고운사 drone+TLS 측정 수관/줄기 실측 및 토심, 거칠기, 뿌리, 암편별 Ks와 erodibility 자료 확보.
2. canopy SF spatial inflow weights must be grounded in measured stem-footprint, not arbitrary receiving area; drip kinetic energy forcing separately modeled.
3. original EUROSEM full sediment store, deposition and outflow mass integration not available; cannot use exported sediment value.
4. SWEHR 2D terrain and event hydrograph, mesh independence and transport kernel to be applied to LiDAR georeferenced grid.
