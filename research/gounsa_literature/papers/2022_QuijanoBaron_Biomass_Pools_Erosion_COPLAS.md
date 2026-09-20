# Quijano-Baron et al. (2022) — COPLAS biomass-pool erosion framework

# 서지정보
Quijano-Baron, J., Saco, P. M., & Rodriguez, J. F. (2022). Modelling the effects of above and belowground biomass pools on erosion dynamics. *Catena, 213*, 106123. https://doi.org/10.1016/j.catena.2022.106123

# 이 논문을 찾은 이유
LPJ-GUESS의 leaf, root, litter, wood, soil-carbon pool을 서로 다른 침식 메커니즘에 연결할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- SIBERIA 기반 raster/distributed LEM
- flow direction은 steepest downslope direction 기반

# 적용 환경
- 호주 tropical woodland savanna
- 일 단위, 100년 가상실험

# 핵심 과정
- fluvial sediment transport
- diffusive transport에 rain splash와 creep을 함께 포함
- hydrology
- dynamic biomass pools

# 식생 입력
- root biomass
- leaf biomass
- litter biomass
- wood biomass
- soil carbon
- big-leaf vegetation

# 핵심 식
- `q_s = beta q^m S^n`
- `q_d = D S`
- root biomass는 normalized 값으로 soil erodibility `beta`를 낮춘다.
- leaf biomass는 `D = Dmax - alpha Lhat` 형태로 diffusion coefficient를 낮춘다.
- litter biomass는 Manning roughness `n = nbare + nref Lithat^w`를 높인다.
- soil carbon은 water-retention capacity를 수정한다.

# 파라미터와 단위
- root, leaf, litter, soil carbon은 site mean/std로 정규화한 0-1 값
- `alpha=0.5`를 Istanbulluoglu & Bras에서 가져왔다고 원문에 서술
- `w=1`은 상세정보 부족으로 가정

# 원 논문의 구현 범위
Hydrology, vegetation, biomass pools, SIBERIA landform evolution을 일 단위로 순차결합한다.

# 고운사에 직접 사용할 수 있는 부분
기관별 biomass pool의 계절적 비동기성과 각 pool이 서로 다른 지형과정에 작용한다는 개념적 구조.

# 새로운 coupling이 필요한 부분
- LPJ-GUESS PFT/cohort를 유지하면서 absolute biomass 또는 root traits를 사용하는 변환
- leaf effect를 splash와 creep으로 분리하는 결합
- living wood를 tree throw, root fracture, CWD로 연결하는 결합

# 한계
- big-leaf 접근이라 understory와 overstory를 구분하지 못함
- wood pool은 살아 있는 동안 직접 geomorphic effect가 없음
- site-normalized biomass로 절대 식생량 비교가 어려움
- leaf가 total diffusion 전체를 낮춰 creep까지 억제

# 최종 판정
- 탈락
- COPLAS는 고운사 최종모델 근거에서 제외한다. biomass-pool 분리 철학만 보조 개념으로 보존한다.

# 참고 링크 / DOI
- https://doi.org/10.1016/j.catena.2022.106123

# 복구 메모
- 업로드된 원문을 현재 채팅에서 직접 확인했다.
