# 서지정보
Jiang, C., Parteli, E. J. R., & Shao, Y. (2025). A model for regional-scale water erosion and sediment transport and its application to the Yellow River Basin. *Journal of Advances in Modeling Earth Systems*, 17(5), e2024MS004593. https://doi.org/10.1029/2024MS004593

# 이 논문을 검색한 이유
CASC2D-SED 원본 계보가 최신 학술모델로 개선되어 동일 공개 소스로 canopy+erosion 2D, cm mesh 요건을 갖추었는지 확인.

# 연구 유형
AHMS-SED = atmospheric and hydrological model (AHMS including Noah-MP and WRF) + modified CASC2D-SED sediment module; hydrology/sediment observed basin scale validation.

# 공간 구조 및 해상도
황하 유역 1979–1987년 20km 격자, 월별 배출량 관측과 비교. **저자의 논문은 원래 CASC2D-SED의 2D diffusive solver 그대로 5–10cm 실행하는 것이 아님**. Routing network regional subgrid framework로 수정되었음을 Zenodo 저자 설명에서 명시.

# 적용환경
황하 유역 광역 침식, 다년 (1979–1987) 유사유출량, 토양 훼손/관개 영향.

# 핵심과정
runoff intensity sensitivity, supplied-sediment, modified CASC2D-SED sediment cap, gully area index, regional sediment advection/routing.

# 식생입력
Noah-MP land surface vegetation coupling 가능하지만 해당 20km 통합의 실제 canopy-to-leafdrip 5cm overland soil detachment feedback module은 확인하지 못함. 같은 이름의 parent model interception이 native cm canopy로 확장됐다고 해석 금지.

# 핵심식
CASC2D-SED 수정에 따른 threshold and sediment supply plus regional transport (세부 수식은 원문 2.3절과 appendix 참고). 공개된 논문 본문 검증 범위 내 수식 텍스트만: runoff-driven transport capacity corrected with land-use and gully factors. 정확식의 계수 전사는 생략.

# 파라미터와 단위
20km grid, years 1979–1987, outlet mKGE .90 and NSE .81 for monthly sediment flux. outlet validation not 5cm per-cell DoD verification.

# 원 논문의 구현 범위
기존 CASC2D-SED를 AHMS regional hydrologic model에 결합한 **새 모델**. 황하 강우 강도/양 및 관개 민감도 분석.

# 실제 공개 코드
- Official author GitHub https://github.com/JiangCong1990/AHMS-SED
- Zenodo https://doi.org/10.5281/zenodo.14494932 ; archive `JiangCong1990/AHMS-SED-AHMS-SED_v1.0.zip`, 28.9 MB, deposited 2024-12-15. README describes regional modified sediment model; 출처 publication DOI와 일치.
- 이번 세션에서 README/GitHub source presence and Zenodo listing 확인, **native compile/run 및 모든 코드 커널 정적 검증은 수행하지 않음**.

# 고운사에 직접 사용할 수 있는 부분
CASC2D-SED 입경별 토사이송 후속 개발과 regional sediment source availability 모델 구현의 후속 문헌.

# 새로운 coupling이 필요한 부분
Full xy 2D small-plot source routing, high-res DEM, native leafdrip impact + dynamic interception + finite soil stock 검증을 일방적으로 주장 불가.

# 한계
발표 격자 크기 20km, 단일 산림 6시간 사건과 다른 문제. 두 오픈소스 lineage를 identical original이라고 보지 말 것.

# 최종 판정
**공개 코드 존재 PASS, 5–10cm 고운사 원본 주모델 NO-GO(20km 지역 통합 목적).**

# 참고 링크 / DOI
https://doi.org/10.1029/2024MS004593
https://github.com/JiangCong1990/AHMS-SED
https://zenodo.org/records/14494932
