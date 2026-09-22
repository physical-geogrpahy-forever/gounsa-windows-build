# 서지정보
Brazhnik, K., & Shugart, H. H. (2016). SIBBORK: A new spatially-explicit gap model for boreal forest. Ecological Modelling, 320, 182-196. DOI: 10.1016/j.ecolmodel.2015.09.016

# 이 논문을 찾은 이유
실제 DEM 지형 위에 개별목을 명시적으로 놓는 산림모델이 고운사 식생-지형 피드백에 적합한지 확인했다.

# 연구 유형
- 수치모델
- 공간명시적 개체기반 gap model

# 공간 구조
- 실제 지형을 반영한 3차원 landscape
- 개별목 위치와 광환경을 명시적으로 계산

# 적용 환경
- 시베리아 boreal forest
- 복잡한 산지 지형 적용 사례 존재

# 핵심 과정
- 정착
- 생장
- 경쟁
- 스트레스
- 사망
- 공간적 광환경

# 식생 입력/상태
- tree biomass
- species composition
- 개별목 위치와 구조
- 유기물 forest-floor carbon pool은 추적하지 않음
- 고운사에 필요한 fine-root/dead-root/litter pool은 핵심 상태로 확인되지 않음

# 핵심 식
3차원 광추적과 gap dynamics를 실제 지형에 결합한다.

# 파라미터와 단위
원 논문 및 후속 연구는 plot 규모와 3차원 광환경에 초점을 둔다.

# 원 논문의 구현 범위
boreal forest의 장기 구조와 종조성을 실제 지형 위에서 모의한다.

# 고운사에 직접 사용할 수 있는 부분
- DEM 기반 공간구조
- 개별목 위치
- 산지 사면의 광환경 차이
- 산림 천이

# 새로운 coupling이 필요한 부분
- root biomass 및 root architecture
- litter/CWD 상태
- 산불 후 연료 및 지표유기물 변화
- 지형모델과의 토양두께/수문 피드백

# 한계
후속 설명에서 tree biomass는 모의하지만 organic forest floor carbon pool은 추적하지 않는다고 명시한다. 고운사 지형과정에 필요한 뿌리와 litter 인터페이스가 부족하다.

# 최종 판정
- 보조근거
- 공간적으로는 강하지만 주 식생모델로는 탈락에 가까움

# 참고 링크 / DOI
https://doi.org/10.1016/j.ecolmodel.2015.09.016
