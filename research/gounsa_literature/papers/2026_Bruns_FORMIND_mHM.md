# 서지정보
Bruns, N., Huth, A., Thober, S., & Fischer, S. M. (2026). Combining an individual-based dynamic vegetation model with a distributive hydrologic model to improve coupled water-carbon modelling. EGUsphere [preprint]. https://doi.org/10.5194/egusphere-2026-4918

Discussion started 31 August 2026. Under review for Geoscientific Model Development.

# 이 논문을 찾은 이유
고운사 vegetation engine 조건 3과 4의 핵심인 `forest demography <-> distributed catchment hydrology`가 실제 published coupling으로 구현된 최신 사례가 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 coupling
- individual/cohort forest model + distributed hydrologic model
- catchment-scale application

# 공간 구조
- FORMIND: spatial forest patches / cohorts or individual trees
- mHM: distributed grid hydrology
- Selke river catchment, Central Germany
- stand-scale vegetation process와 catchment discharge를 결합

# 적용 환경
- Central Germany Selke river catchment
- mixed deciduous catchment
- 약 40% forest cover
- temperate forest

# 핵심 과정
- dynamic forest structure
- GPP
- transpiration / evapotranspiration partitioning
- soil-water availability
- catchment runoff/discharge
- vegetation-water feedback

# 식생 입력
- FORMIND tree/cohort state
- forest structure
- LAI/production state
- soil-water limitation supplied through coupled hydrology

# 핵심 식
이 논문의 핵심은 단일 새로운 식보다 two-way model coupling이다.

개념:
```text
mHM distributed soil-water / hydrologic state
 -> FORMIND water limitation / GPP / transpiration
 -> vegetation-dependent ET/transpiration
 -> mHM catchment water balance and discharge
```

# 파라미터와 단위
논문 초록/현재 공개정보에서 직접 확인된 주요 평가량:
- transpiration fraction Et/ET
- standalone mHM: 약 0.50
- coupled FORMIND-mHM: 약 0.73
- catchment discharge at gauges
- forest GPP

# 원 논문의 구현 범위
Selke catchment에서 standalone mHM과 FORMIND-mHM을 비교하고, dynamic forest-water feedback이 discharge 및 ET partitioning에 미치는 영향을 평가했다.

주요 결과:
- discharge performance는 standalone mHM과 대체로 비슷
- ET partitioning은 크게 변함
- Et/ET가 0.50에서 0.73으로 증가해 관측범위에 더 가까워짐
- 모든 gauge에서 seasonal GPP-discharge relation이 나타남

# 고운사에 직접 사용할 수 있는 부분
1. distributed hydrology와 dynamic forest model의 direct published coupling precedent
2. 토양수분을 vegetation physiology/growth의 외부 state로 넘기는 기준 3A의 강한 근거
3. forest structure가 다시 transpiration과 catchment water balance에 feedback하는 양방향 구조
4. 독일 온대 mixed deciduous catchment라는 환경적 유사성
5. FINAM을 통한 component-wise coupling precedent

# 새로운 coupling이 필요한 부분
- 고운사 erosion/deposition에 따른 dynamic soil-layer thickness
- water/C/N/root state의 conservative remapping
- DEM, slope, connectivity의 event-driven 갱신
- root exposure/burial
- 고운사 geomorph grid와 FORMIND/mHM grid 사이 scaling
- herbaceous forest understory가 필요할 경우 GRASSMIND와의 동시 forest integration

# 한계
1. 현재 논문은 2026년 8월 공개된 preprint이며 peer-review 중이다.
2. 연구의 핵심은 forest-water coupling이며 geomorphic erosion/deposition은 없다.
3. FORMIND native forest vegetation은 woody succession 중심이다.
4. forest herbaceous understory demographic succession은 본 논문에서 핵심적으로 다루지 않는다.
5. 고운사처럼 storm-driven soil geometry change를 처리하지 않는다.

# 최종 판정
- **채택: criterion 3/4의 핵심 최신 coupling precedent**
- FORMIND를 조건부 top-tier vegetation candidate로 올리는 직접적인 근거
- 다만 criterion 2 herbaceous understory gap은 별도 검증 필요

# 참고 링크 / DOI
https://doi.org/10.5194/egusphere-2026-4918
Model code/software is linked from the preprint to Zenodo record 21904998.
