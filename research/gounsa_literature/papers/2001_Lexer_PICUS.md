# 서지정보
Lexer, M. J., & Hönninger, K. (2001). A modified 3D-patch model for spatially explicit simulation of vegetation composition in heterogeneous landscapes. Forest Ecology and Management, 144, 43-65. DOI: 10.1016/S0378-1127(00)00386-8

# 이 논문을 찾은 이유
고운사 산불 후 식생-지형 결합에서 10-30 m 이하 공간해상도와 명시적 종자분산을 가진 산림 천이모델 후보를 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- 산림 천이 / 개체목 기반 3D patch model

# 공간 구조
- 10 m x 10 m 수평 patch
- 5 m 수직 crown cell
- 주변 patch와 광환경 및 종자분산 상호작용을 명시적으로 계산

# 적용 환경
- 이질적인 산림 경관
- 중부유럽 산림
- 산지 경관 적용 지향

# 핵심 과정
- 개체목 생장
- 경쟁
- 종자분산
- 환경제약
- 장기 천이

# 식생 입력/상태
- 개체목 크기와 종 구성
- 3차원 수관 구조
- 토양수분 지수
- 생산량
- 본 논문/공개 설명에서 고운사에 필요한 fine-root biomass, dead-root pool, 정량 litter biomass 상태는 확인되지 않음

# 핵심 식
PICUS의 핵심은 개별 침식식이 아니라 10 m patch 배열에서 수관 광환경과 개체목 생장, 경쟁, 종자분산을 결합하는 구조다.

# 파라미터와 단위
- horizontal patch: 10 m x 10 m
- crown cell height: 5 m
- 기후 입력은 월 자료 기반

# 원 논문의 구현 범위
산림 조성과 장기 천이, 공간적 수관 경쟁을 모의한다.

# 고운사에 직접 사용할 수 있는 부분
- 10 m 수준의 명시적 공간구조
- 개체목 기반 산림 천이
- 공간적 종자분산

# 새로운 coupling이 필요한 부분
- 개체목 상태 -> fine/coarse root biomass
- root turnover -> dead-root pool
- litter mass -> 지형모델 표면보호
- 산불 후 즉시 상태변환
- 지형변화 -> 생장/정착 피드백

# 한계
고운사 지형모델이 요구하는 정량적 뿌리 및 litter pool이 핵심 상태량으로 확인되지 않았다. 공간해상도는 좋지만 지형결합용 생지화학 상태량이 부족하다.

# 최종 판정
- 보류
- 공간구조 비교후보로 강함
- 주 식생모델로는 root/litter 인터페이스 부족

# 참고 링크 / DOI
https://doi.org/10.1016/S0378-1127(00)00386-8
