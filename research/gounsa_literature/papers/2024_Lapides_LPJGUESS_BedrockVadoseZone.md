# 서지정보
Lapides, D. A., Hahm, W. J., Forrest, M., Rempe, D. M., Hickler, T., & Dralle, D. N. (2024). Inclusion of bedrock vadose zone in dynamic global vegetation models is key for simulating vegetation structure and function. *Biogeosciences, 21*, 1801–1826. https://doi.org/10.5194/bg-21-1801-2024

# 이 논문을 찾은 이유
고운사에서 실제 뿌리가 A+B 토양층 아래의 C/Cr 풍화층까지 들어가는 현장관찰을 LPJ-GUESS 수문구조에 반영할 수 있는 직접 선례를 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- LPJ-GUESS hydrology modification

# 공간 구조
- 각 grid cell은 1-D 수직 column
- 상부 토양층과 하부 weathered bedrock water storage를 분리
- lateral flow는 원 모델 내부에 없음

# 적용 환경
- Northern California Coast Ranges 상세사례
- 미국 전역 적용
- 얕은 토양과 풍화기반암 수분이 중요한 산림 및 savanna

# 핵심 과정
- soil water storage
- weathered-bedrock rock moisture
- root water uptake
- transpiration
- overland flow
- percolation
- baseflow

# 식생 입력
- LPJ-GUESS PFT
- root distribution
- LAI와 식생생리
- plant water demand

# 핵심 식
원 LPJ-GUESS의 고정 50 cm와 100 cm 두 층 구조를 수정해, 상부는 soil storage capacity, 하부는 rock-moisture storage capacity로 정의한다.

주요 수정:
- 더 깊은 plant-accessible storage 반영
- upper layer field-capacity overflow를 deeper soil/weathered bedrock로 전달
- 상부에서 하부로의 물 이동을 보다 물리적인 수리전도도 제약으로 처리
- 하부 weathered bedrock excess water를 baseflow로 처리

# 파라미터와 단위
- soil storage capacity: water depth
- rock moisture storage capacity: water depth
- Ksat: length time^-1
- root distribution: fraction
세부 site parameter는 원문 재검증 필요.

# 원 논문의 구현 범위
식물이 전형적인 토양깊이보다 더 깊은 풍화기반암의 물을 사용할 수 있도록 LPJ-GUESS를 확장한다.

# 고운사에 직접 사용할 수 있는 부분
고운사에서
```text
root-accessible depth > mobile soil thickness
```
를 허용하는 가장 직접적인 LPJ-GUESS 선례.

고운사에서는 최소한
```text
W_AB
W_C
```
처럼 상부토양과 C/Cr의 수분저장고를 분리하는 구조를 검토할 수 있다.

# 새로운 coupling이 필요한 부분
- 고운사에서 H_AB, H_C가 지형과정에 따라 동적으로 변할 때 LPJ-GUESS storage capacity를 매 timestep 갱신
- run-on을 하류셀에 같은 날 재주입
- coarse fraction이 storage capacity에 미치는 영향
이들은 원 논문에 없는 새로운 coupling이다.

# 한계
- 풍화기반암 수분은 구현하지만 weathering front 자체를 동적으로 이동시키지 않음
- pedogenesis와 coarse fraction을 동적으로 생성하지 않음
- 각 LPJ-GUESS cell은 기본적으로 lateral flow가 없는 1-D column

# 최종 판정
- C/Cr 수분저장과 root-accessible depth 구조의 핵심 근거로 채택
- 동적 지형결합은 새로운 coupling으로 명시

# 참고 링크 / DOI
https://doi.org/10.5194/bg-21-1801-2024
