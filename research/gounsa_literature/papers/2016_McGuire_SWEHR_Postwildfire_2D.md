# 서지정보
McGuire et al. (2016). SWEHR 계열 postwildfire 2D shallow-water erosion model. 정확한 논문명/권호/DOI는 현재 채팅에서 완전 복구되지 않아 **원문 재검증 필요**.

# 이 논문을 찾은 이유
산불 후 환경에서 2D shallow-water와 morphodynamics를 함께 계산하는 모델을 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- postwildfire erosion

# 공간 구조
- 2D shallow-water 계열

# 적용 환경
- postwildfire hillslope/catchment

# 핵심 과정
- canopy interception
- infiltration
- 2D runoff
- Hairsine-Rose 계열 sediment/morphodynamics

# 식생 입력
- 주로 vegetation cover fraction
- quantitative root biomass 직접입력은 확인되지 않음

# 핵심 식
이번 세션에서 원식 전체는 복구되지 않았다. **원문 재검증 필요**.

# 파라미터와 단위
원문 재검증 필요.

# 원 논문의 구현 범위
산불 후 2D runoff-erosion-morphodynamics.

# 고운사에 직접 사용할 수 있는 부분
postfire 2D 모델이라는 점의 구조적 선례.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC/LitterC를 직접 연결하려면 **새로운 coupling**.

# 한계
vegetation effect가 cover 중심이므로 고운사의 strict quantitative-vegetation 조건을 충족하지 않는다.

# 최종 판정
**보조근거.** 산불 후 2D 적용 선례지만 최종 vegetation coupling 후보에서는 우선순위 낮음.
