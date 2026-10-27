# 서지정보
Rojas, R., Velleux, M., Julien, P. Y., & Johnson, B. E. (2008). Grid scale effects on watershed soil erosion models. *Journal of Hydrologic Engineering*, 13(9), 793–802. https://doi.org/10.1061/(ASCE)1084-0699(2008)13:9(793)

# 이 논문을 검색한 이유
CASC2D-SED의 **실제 발표된 격자해상도와 격자 민감도**를 확인하여 5–10cm 주장에 선례가 있는지 판단.

# 연구 유형
Goodwin Creek 실측자료로 soil erosion grid effects 해상도 민감도 및 3개 강우사상 보정/검증. ASCE 저널 초록 기준.

# 공간구조
2D diffusive-wave CASC2D-SED, 모의 raster 해상도 **30m–330m**, 원래 30m에서 parameterization and calibration. 5–10cm 구동 논문 아님.

# 적용환경
Goodwin Creek 실험유역 Mississippi, 세 강우사상.

# 핵심과정
원본 2D overland flow, runoff-sediment flux calibration, grid aggregation effect on flow slope/channel topology/sediment source/delivery.

# 식생입력
CASC2D-SED land-use C/P and fixed interception by landuse; 본 논문에서 LAI-driven canopy storage/leafdrop KE의 native field test 증거 없음.

# 핵심식
본 세션에서는 abstract만 확인. 식과 파라미터 전체 본문을 확인하지 않았으므로 임의 수식 미전사.

# 파라미터와 단위
Raster cell 30m–330m. Three rainfall events. Reported sediment yield within ±50% field observation for published configuration.

# 원 논문의 구현 범위
30m, 90m에서 Goodwin Creek sediment/flow reasonably simulated; grid >150m에서 sediment delivery ratio artefacts. 논문은 coarse-to-medium watershed raster study, sub10cm proof 아님.

# 고운사에 직접 사용할 수 있는 부분
Grid dependence 검증이 모델선정 시 필수라는 별도의 peer-reviewed precedent.

# 새로운 coupling이 필요한 부분
CASC2D original을 5–10cm로 확대하고 LAI canopy and unrestricted 4-edge flow/raindrop impact를 추가하면 미검증 새 engineering. 학술적으로 기존 실증이라고 기술 불가.

# 한계
실험 유역은 고운사 작은 산림경사와 환경/scale 크게 다름. 논문 전문 수식과 실행판은 이번 연구에서 별도 확인되지 않음.

# 최종 판정
**보조근거**, 5–10cm 실행 근거로는 부적합.

# 참고 링크 / DOI
https://doi.org/10.1061/(ASCE)1084-0699(2008)13:9(793)
https://ascelibrary.org/doi/10.1061/(ASCE)1084-0699(2008)13:9(793)
