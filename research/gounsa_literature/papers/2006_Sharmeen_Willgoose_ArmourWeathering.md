# 서지정보
Sharmeen, S., & Willgoose, G. R. (2006). The interaction between armouring and particle weathering for eroding landscapes. *Earth Surface Processes and Landforms, 31*(10), 1195-1210. https://doi.org/10.1002/esp.1397

# 이 논문을 찾은 이유
고운사의 `large spall -> weathering/fragmentation -> armour change -> erosion change`를 이미 구현한 기존 수치모델이 있는지 확인하기 위해 검토했다.

# 연구 유형
- ARMOUR extension
- process-based numerical experiment

# 공간 구조
- 1D hillslope

# 적용 환경
- armour-forming eroding surfaces
- published particle-weathering mechanisms

# 핵심 과정
- armour formation
- particle weathering
- daughter particle-size distribution
- size-selective transport
- weathering-limited / transport-limited erosion

# 식생 입력
- 없음

# 핵심 식/구조
ARMOUR에 particle-weathering mechanism을 결합하여 parent particle이 daughter-size classes로 분해되는 과정과 그 결과의 erosion/armour 변화를 동시에 계산한다.

중요 결과:
- 동일한 크기 daughter particles 생성: erosion 증가, armour 감소 가능
- 매우 작은 spall-like daughters 생성: erosion 증가와 armour 증가가 동시에 가능
- fine-to-coarse 범위의 daughters 생성: armour가 깨져도 transport capacity 소비 때문에 erosion이 오히려 감소할 수 있음

# 파라미터와 단위
- parent/daughter size distribution
- weathering rate
- transport/entrainment parameters
- runoff forcing

# 원 논문의 구현 범위
weathering이 armour를 단순 약화시킨다는 가정을 거부하고, weathering geometry와 transport capacity의 상호작용으로 결과를 계산한다.

# 고운사에 직접 사용할 수 있는 부분
- 사용자가 처음 제안한 `spall weathering -> armour weakening`을 더 엄밀한 기존모델 구조로 대체
- `fragmentation != armour loss`를 수치적으로 처리 가능
- weathering-limited와 transport-limited regime 구분

# 새로운 coupling이 필요한 부분
fire severity가 초기 fire-spall PSD를 만드는 단계와 vegetation/hydrology coupling은 별도이다.

# 한계
- 1D
- weathering parameters는 lithology-specific calibration 필요

# 최종 판정
- **armour-weathering 상호작용의 핵심 채택모델**

# 참고 링크 / DOI
https://doi.org/10.1002/esp.1397
