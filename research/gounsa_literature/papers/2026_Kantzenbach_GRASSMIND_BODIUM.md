# 서지정보
Kantzenbach, M., König, S., Reitz, T., Schädler, M., & Taubert, F. (2026). Synergizing grassland and soil system model expertise by coupling GRASSMIND (v2.0) and BODIUM (v1.2). EGUsphere [preprint]. https://doi.org/10.5194/egusphere-2026-1713

Discussion started 4 May 2026.

# 이 논문을 찾은 이유
FORMIND codebase에 포함된 `grassmindEnabled`가 고운사에서 요구하는 explicit herbaceous succession의 실질적 해결책이 될 수 있는지, 그리고 herbaceous model이 외부 soil model과 state exchange 가능한지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 coupling
- individual/process-based grassland model + systemic soil model
- FINAM coupling framework

# 공간 구조
- GRASSMIND: patch-based individual herbaceous community model
- BODIUM: soil-system model
- 본 연구는 grassland/soil coupling이며 forest understory simulation은 아님

# 적용 환경
- European managed grassland / GCEF experimental context
- multi-year field data calibration and validation

# 핵심 과정
- individual herbaceous plant growth
- interspecific competition
- vertical light competition
- crowding mortality
- soil-water limitation
- soil resource dynamics
- model coupling through FINAM

# 식생 입력
- herbaceous individuals/species
- shoot/height/leaf states
- roots and soil-water demand
- seed/recruitment processes in GRASSMIND lineage

# 핵심 식
본 논문의 핵심은 GRASSMIND 내부의 단순 soil-water representation을 BODIUM의 soil system state로 교체/연결하는 component coupling이다.

개념:
```text
BODIUM soil water/resource state
 -> GRASSMIND herbaceous physiology/growth/competition
 -> vegetation demand/state
 -> coupled soil feedback
```

# 파라미터와 단위
GRASSMIND v2.0은 daily weather forcing과 herbaceous individual/process parameters를 사용한다.
논문은 soil-water coupling이 standalone GRASSMIND보다 관측 soil-water response를 더 신뢰성 있게 만든다고 보고한다.

# 원 논문의 구현 범위
- GRASSMIND v2.0 + BODIUM v1.2
- FINAM을 통한 independent model component coupling
- grassland field data를 이용한 parameterization/calibration/validation

# 매우 중요한 FORMIND 관련 확인
Code/data availability에서 저자들은 본 연구에 사용한 **GRASSMIND v2.0이 forest model FORMIND에 integrated되어 있고 FORMIND의 license/publication policy를 따른다**고 명시한다.

그러나 이것은 다음을 증명하지 않는다.
```text
FORMIND trees + GRASSMIND herbs
simultaneously in one forest patch
```

실제로 UFZ LISA 설명은 FORMIND를 forest component, GRASSMIND를 grassland component로 별도로 나열한다.

따라서 고운사 criterion 2에 대해:
- herbaceous demographic engine 자체는 존재
- FORMIND forest understory로 native concurrent integration되었다는 증거는 아직 없음

# 고운사에 직접 사용할 수 있는 부분
1. herbaceous individual/process model의 soil-state coupling precedent
2. daily herbaceous competition과 soil-water response
3. FINAM을 사용해 vegetation model의 native soil representation을 전문 soil model과 연결하는 구조
4. 향후 FORMIND tree component와 herbaceous component를 같은 landscape framework에 연결할 수 있다는 기술적 근거

# 새로운 coupling이 필요한 부분
- forest canopy FORMIND와 GRASSMIND를 동일 forest cell/patch에 동시에 계산하는 vertical competition interface
- tree canopy shading -> herb light climate
- tree and herb roots -> shared layer water competition
- tree/herb litter and fire interactions
- erosion/deposition에 따른 soil layer geometry remapping

이러한 동시 forest-strata coupling은 현재 확인 범위에서 published native feature가 아니므로 반드시 **새로운 coupling**으로 표시한다.

# 한계
1. grassland 연구이지 forest understory 연구가 아니다.
2. FORMIND codebase integration이 simultaneous forest+grass simulation을 의미하지 않는다.
3. GRASSMIND v2.0 code는 FORMIND licensing/publication policy 아래 request 기반이며, 독립 GRASSMIND v3.0은 개발 중이다.
4. 고운사 온대 산림 하층종 parameterization이 필요하다.

# 최종 판정
- **채택: criterion 2를 보완할 수 있는 herbaceous engine 및 soil-coupling precedent**
- 그러나 FORMIND의 native forest understory 충족 근거로는 아직 보류

# 참고 링크 / DOI
https://doi.org/10.5194/egusphere-2026-1713
Coupling code archive: https://doi.org/10.5281/zenodo.19204558
