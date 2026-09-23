# 서지정보
Verbruggen, W., et al. (2025). LPJ-GUESS-RE v1.0: a process-based Richards-equation soil hydrology implementation in LPJ-GUESS. Geoscientific Model Development, 18, 6623–? . https://doi.org/10.5194/gmd-18-6623-2025

# 이 논문을 찾은 이유
고운사 식생-지형 결합에서 외부 지형모델이 바꾸는 토심과 토층 구조를 식생모델의 수분스트레스와 뿌리흡수에 반영할 수 있는지 확인하기 위해 검토했다. 특히 기존 LPJ-GUESS bucket hydrology보다 물리적인 다층 토양수문과 얕은 기반암 경계를 제공하는지 확인했다.

# 연구 유형
- 수치모델 개발
- LPJ-GUESS 토양수문 모듈 확장

# 공간 구조
- 수평적으로는 기존 LPJ-GUESS site/grid 구조
- 토양수문은 1-D vertical Richards equation
- 15개 토양층
- 사용자가 토층 두께를 설정할 수 있어 총 토심을 조정 가능

# 적용 환경
- 다양한 기후/토양 조건의 LPJ-GUESS site simulations
- 고운사에는 얕은 산림토양과 기반암 경계 표현 관점에서 중요

# 핵심 과정
- Richards equation 기반 불포화/포화 수분 이동
- 토양수분포텐셜
- hydraulic conductivity
- root water uptake sink
- free-drainage / bedrock / aquifer lower boundary
- adaptive subdaily numerical integration

# 식생 입력
- LPJ-GUESS PFT/cohort vegetation state
- root distribution and water demand
- transpiration-driven root uptake

# 핵심식/구조
토양수분은 다층 Richards equation으로 풀며 root water uptake가 sink term으로 들어간다. 수치적분은 LPJ-GUESS의 일별 ecosystem step 내부에서 adaptive subdaily timestep으로 수행된다.

중요한 구조:
```text
daily LPJ-GUESS ecosystem step
 -> adaptive subdaily Richards solver
 -> layer soil-water potential/conductivity
 -> root uptake sink
 -> daily vegetation water stress and carbon response
```

# 파라미터와 단위
- soil layers: 15
- layer thickness: configurable
- lower boundary: free drainage / bedrock / aquifer options
- solver: adaptive subdaily integration, Boost odeint Cash–Karp 계열

# 원 논문의 구현 범위
- 기존 LPJ-GUESS의 단순 토양수분 구조를 process-based vertical hydrology로 교체
- lateral hillslope routing은 포함하지 않음
- erosion/deposition에 따른 run-time soil-layer geometry 변화는 포함하지 않음

# 코드/branch 의미
공개 코드는 LPJ-GUESS 4.1.1 revision 10118 기반이다. 저자들은 새 수문코드가 다른 LPJ-GUESS branch로 비교적 쉽게 이전될 수 있도록 구성되었다고 설명한다.

이는 고운사에서 2026 SEC/PPA branch와의 결합 가능성을 높이는 근거지만, 실제 병합이 이미 검증되었다는 뜻은 아니다.

# 고운사에 직접 사용할 수 있는 부분
1. 얕은 토심과 기반암 경계의 명시적 표현
2. layer-wise soil-water state
3. 물리 기반 root-water uptake
4. 일별 vegetation loop 안의 subdaily soil response
5. 외부 geomorph model이 바꾼 soil profile을 받아들이기 좋은 layer architecture

# 필요한 새로운 coupling
고운사에서 erosion/deposition으로 토양층 두께가 바뀌면 다음 상태를 보존적으로 재배분해야 한다.
- soil water
- soil C/N pools
- root fractions / root biomass
- hydraulic properties

또한 실제 사면의 측방수문은 PF-LPJG, LPJ-DH 또는 별도 hydrology engine과 결합해야 한다.

`SEC/PPA + RE + external lateral hydrology`는 현재 published single implementation이 아니며 새로운 code merge/coupling이다.

# 한계
1. 1-D vertical hydrology
2. root vertical architecture는 여전히 비교적 단순하고 정적 parameterization에 의존
3. run-time geomorphic soil-depth remapping 없음
4. 계산비용은 default hydrology보다 증가하며 aquifer boundary 조건은 특히 비쌀 수 있음
5. SEC/PPA와 동일 revision이 아님

# 최종 판정
- **채택 후보 핵심 근거**
- LPJ-GUESS 계열에서 criterion 3의 soil-depth / multilayer hydrology 측면을 가장 강하게 보완
- SEC/PPA와의 병합 가능성은 높아 보이나 실제 source-level diff audit 필요

# 참고 링크 / DOI
- https://doi.org/10.5194/gmd-18-6623-2025
- Code archive: https://doi.org/10.5281/zenodo.15024130
