# 서지정보
Zanchi, G., Yu, L., Akselsson, C., Bishop, K., Köhler, S., Olofsson, J., & Belyazid, S. (2021). Simulation of water and chemical transport of chloride from the forest ecosystem to the stream. Environmental Modelling & Software, 138, 104984. https://doi.org/10.1016/j.envsoft.2021.104984

# 이 논문을 찾은 이유
고운사 식생 엔진 후보 중 실제 산림사면에서 일 단위 측방 수문과 식생-토양 상태를 함께 계산하는 계열이 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- ForSAFE의 2D hillslope 확장 및 실제 산림사면 검증

# 공간 구조
- 산림 사면 transect의 연결된 공간 단위
- lateral soil-water and chemical transport
- saturated/unsaturated zone 구분
- 논문은 이를 ForSAFE-2D로 명명

# 적용 환경
- 북스웨덴 산림사면
- forest-to-stream hydrology and chemistry

# 핵심 과정
- tree growth와 forest biogeochemistry를 포함하는 ForSAFE
- soil water storage
- lateral water flow
- saturated/unsaturated soil water
- chloride transport
- stream discharge

# 식생 입력
- ForSAFE의 stand-level tree growth 및 nutrient uptake
- litter decomposition
- soil and tree hydrology
- 이 논문 자체는 age/size cohort demography를 도입하지 않는다.

# 핵심 식
본 검토의 핵심은 개별 식보다 공간 및 시간 결합 구조이다. ForSAFE-2D는 기존 ForSAFE에 lateral water and chemical element transport를 추가한다.

# 파라미터와 단위
- 일 단위 수문 및 chloride transport 검증
- soil properties와 model parameterization은 supplementary material에서 제공
- 정확한 매개변수는 고운사 적용 시 원문 및 보충자료 재확인 필요

# 원 논문의 구현 범위
- forest hillslope에서 water storage와 forest-to-stream discharge를 일 단위로 모의
- lateral water and chemical flows 구현
- 실제 hillslope measurements와 비교
- source/software는 Fortran 계열

# 고운사에 직접 사용할 수 있는 부분
- 기준 4의 강한 직접 선례: 실제 forest hillslope lateral hydrology
- 기준 5 충족: daily hydrology
- 외부 또는 내부 토양수분 상태가 식생/biogeochemistry와 연결되는 forest-process architecture 참고

# 새로운 coupling이 필요한 부분
- 침식 및 퇴적으로 soil layer geometry가 바뀌는 경우의 water/C/N/root state remapping
- 고운사 geomorphic engine과 event-time state exchange
- age/size cohort vegetation 구조를 추가하려면 별도 vegetation engine 또는 새로운 coupling 필요

# 한계
- 핵심 식생 구조는 demographic age/size cohort가 아니다.
- hillslope hydrology는 강하지만 고운사 기준 1의 spatial cohort vegetation engine 요구를 충족하지 않는다.
- 극한강우에 따른 지형변화를 직접 계산하지 않는다.

# 최종 판정
- 보조근거
- 실제 산림사면 일 단위 수문과 식생-토양 결합의 강한 선례
- strict vegetation-engine 후보로는 cohort 구조 부족 때문에 탈락

# 참고 링크 / DOI
- https://doi.org/10.1016/j.envsoft.2021.104984
