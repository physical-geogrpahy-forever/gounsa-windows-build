# 서지정보
Maggioli, L., Rodríguez-Caballero, E., Cantón, Y., Rodríguez-Lozano, B., & Chamizo, S. (2022). Design Optimization of Biocrust-Plant Spatial Configuration for Dry Ecosystem Restoration Using Water Redistribution and Erosion Models. *Frontiers in Ecology and Evolution*, 10, 765148. https://doi.org/10.3389/fevo.2022.765148

# 이 논문을 찾은 이유
고운사의 필수조건 10cm 이하 + LiDAR DTM + LAI 관련 수관저류 + 강우사상별 지표유출 + 침식모의를 하나의 published model에서 결합한 실증사례를 검증하기 위해. 2026-10-27의 'cm급 수관차단/침식 선례 미확인'이라는 기존 결론을 직접 반박한다.

# 연구 유형
스페인 건조지역 사면 현장 TLS 변화관측(2014-07 및 2015-12) + 이벤트 LISEM 매개변수 보정 및 침식량 비교 + 가상 식생패치/biocrust 분포 시나리오. 원문 전체 HTML 본문을 직접 검토.

# 공간 구조
25m×15m = 약375m² 실험사면. 현장 TLS 5cm DTM, **LISEM 계산도 5cm 격자**, 강우사상 내부 **1초 시간간격**. 논문 명시: 유출은 **kinematic-wave routing**이며 이것만으로 full 2D SWE/4방향 자유유출 구현을 입증하지 않음. 격자맵의 2D 공간분포와 2D 유체 수치해석을 엄격히 구분.

# 적용 환경
남부 스페인 알메리아 석회암 채석 훼손사면. 자생식생은 주로 거친 포기 형태의 alpha grass (Macrochloa tenacissima)와 관목; bare soil, vegetation, biocrust 패치. 고운사의 억새(Miscanthus)와 **종이 다르므로 동일 매개변수 직접 전용 불가**.

# 핵심 과정
강우사상별 수관저류 관련 LAI, 침투(Green-Ampt), 비피복/식생/생물토양피막 별도 침투특성, kinematic-wave 지표 유출, LISEM 침식 및 유사 이동, 식생 패치별 runoff source/sink. 18개 유출발생 강우사상을 개별 모의, 18개월 총 지형변화(DoD)로 침식 총량 비교.

# 식생 입력
TLS 5cm 셀의 식생점/전체점 비율로 식생 피복 파악, LAI는 실제 잎점 직접 광학역산 아닌 **피복도에서 경험식으로 추정**해 모델 수관 수분저장능력 계산. 식생높이 TLS 수직 범위, 보호 피복/식생 패치 25×25cm 및 50×50cm, 뿌리 기여 토양점착력과 거칠기 변화. LAI와 canopy interception parameter의 구현체/버전별 상세 원본 경로 **논문에 기재되지 않음**; 모델 기재는 LISEM, 특정 OpenLISEM 실행 버전 태그가 아님.

# 핵심 식
LAI vs cover: Ramírez et al. (2007) 계열 경험식 사용; 원문 수식이 HTML에서 이미지 처리되어 정확 계수 전체 미전사, LAI 계산의 명시된 1.99 계수만 확인. Green-Ampt 침투. 흐름은 kinematic wave. 심층 SWEs나 자동 DEM 업데이트가 이 논문 5cm 실험에서 입증된 건 아님.

# 파라미터와 단위
DTM/input 0.05m, event timestep 1s; 원강우 5분 강우계; 가상 강우강도 15, 55mm/h 각30분; 식생 군집 0.25×0.25m/0.50×0.50m. 초기 토양 3cm biocrust 및 아래 3–30cm 층 설정. 원문 보고 18개 강우사상 총 침식예측 3.55t, 총 침식량 비교 오차 RMSE 17.79%(논문의 성능표현). 정확 DOF/오차식은 본문 표 정의 이상으로 해석하지 않음.

# 원 논문의 구현 범위
**5cm+수관차단 LAI 추정+침투/유출+침식의 실증 일체는 참**. 실험 결과의 검증은 18개월 전체 침식량에 대한 사후 TLS와 비교이고 5cm 격자별 국지 침식·퇴적 및 18회 각 이벤트 후 DoD 검증은 아님. 5cm 계산 시간간격 수렴/유사질량수지는 본문에서 미확인.

# 고운사에 직접 사용할 수 있는 부분
초고해상도 TLS의 지형/식생점 분류, LAI 및 식생높이 산출, 사면 식생 패치 2차원 구성, 단일모델 사상별 유출-침식의 유력한 **직접 선행연구**. 현재 고운사 SHETRAN 주모델만 고집하는 근거를 해제하되 별도의 LISEM 소스버전 안정성 감사 필요.

# 새로운 coupling이 필요한 부분
원본 분포형 routing이 4면 수리학적 2D 흐름인지 검증, 현장 수관 적하/수관저류 매개변수와 지표 식생/암편 및 부피밀도 현장 입력 제약, 원본 버전 고정과 time/dx convergence, cm급 DoD 격자별 비교.

# 한계
Maggioli(2022)의 버전과 OpenLISEM 7.5.2는 같다고 주장 불가. 기존 7.5.2 원본 고운사 2D 5m 유사수송 대규모 시간간격 비수렴 NO-GO는 그대로 유지. kinematic wave가 네방향 자유유출의 genuine 2D hydrodynamics을 만족한다고 말할 수 없음.

# 최종 판정
**채택: 핵심 published 5cm 연구 선례. 주모델 코드 선정은 보류(원본 실행버전 미확인, 수리학 2D와 7.5.2 수치결함 미해결).**

# 참고 링크 / DOI
https://doi.org/10.3389/fevo.2022.765148
https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.765148/full

## 2026-10-27 개발 계보 확인
원문 https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.765148/full 의 `Model Selection` 절은 모델을 `LISEM (Limburg Soil Erosion Model)`로 표기하고 `Jetten and De Roo 2001` 및 초기 LISEM 연구를 인용하며 **kinematic-wave routing**을 설명한다. 따라서 **고전 LISEM / OpenLISEM classic 계열** 사용 가능성이 높다. 하지만 **어떤 classic 실행 버전**(200x LISEM, 201x OpenLISEM 등)인지는 원문 미기재이므로, 실제 `v7.5.2` 또는 신형 `LISEM v0.x`를 썼다고 단정 불가.
