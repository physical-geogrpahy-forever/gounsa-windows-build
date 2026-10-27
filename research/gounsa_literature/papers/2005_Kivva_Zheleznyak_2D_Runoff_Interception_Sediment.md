# 서지정보
Kivva, S., & Zheleznyak, M. (2005). Two-dimensional modeling of rainfall runoff and sediment transport in small catchment areas. *International Journal of Fluid Mechanics Research, 32*(6), 703–717. https://doi.org/10.1615/InterJFluidMechRes.v32.i6.50

# 검색 이유
원형 모델 내 수관차단, 2D Saint-Venant 지표유출 및 유사수송/퇴적을 동시에 명시한 독립 연구의 원본 공개여부 및 cm급 검증 사례 탐색.

# 연구 유형
소유역 지표유출/침식 수학모델 개발 및 Butenya 하천 유역 강우 홍수 관측 검증. 초록과 서지 원문을 확인했으며 논문 전체 본문은 공개 원문으로 확보하지 못했음.

# 공간구조
2차원 비정상 천수방정식과 보존형 암시적 1차 유한차분. 개방흐름 자유경계 모의. **논문 초록에는 계산 격자 크기 미기재**. 5cm/10cm 이하 실행 여부 확인 불가.

# 적용환경
소유역 및 강우유출에 따른 토양유실. Butenya 유역 검증.

# 핵심과정
식생 강우차단, 미세지형 함몰저류, 침투, 2D 지표유출, 토양의 세탈, 유사이동 및 재퇴적. 모형 초록에서 직접 명시한 구현 범위.

# 식생입력
식생 강우차단 존재가 초록에 제시되지만 LAI, 수관저류, 수관배수, leaf drip의 상세 식/매개변수는 원문 미확보로 확인되지 않음.

# 핵심식
2D unsteady shallow-water equations + infiltration equation + sediment transport equation. 입경별 이송능력 및 source-term 식의 상세 계수는 미확인.

# 파라미터와 단위
공간 격자 m 및 시간 s: 구체 수치 미확인. 재현 입력파일/코드 원본 미확보.

# 고운사 활용
수관차단+2D 수리+침식/재퇴적 일체 선행모델 개념 및 논문 근거. cm급 실행 가능성이나 LAI canopy dynamics 근거로 직접 사용 금지.

# 필요한 새로운 coupling
실제 저자의 2005 구현 전체코드와 LAI 구동 구조 및 cm 수치검증 없이는 고운사에 적용할 수 없음. 새로 보완해 원본이라고 부를 수 없음.

# 한계
10cm 이하 실증 논문 근거 없음, 다운로드 가능한 저자 원본코드 미확인. 논문 요약만 근거이며 작동 실험 수행하지 않음.

# 최종 판정
구조적으로 매우 관련성 높지만 **고운사의 공개 코드 + <=10cm 실증 조건 불충족**. 보조 선행연구로 보존.

# 확인한 출처
https://doi.org/10.1615/InterJFluidMechRes.v32.i6.50
https://www.researchgate.net/publication/239434788_Two-Dimensional_Modeling_of_Rainfall_Runoff_and_Sediment_Transport_in_Small_Catchment_Areas
