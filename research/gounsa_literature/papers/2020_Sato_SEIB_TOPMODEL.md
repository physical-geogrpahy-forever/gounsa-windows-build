# 서지정보
Sato, H., Kobayashi, H., Beer, C., & Fedorov, A. (2020). Simulating interactions between topography, permafrost, and vegetation in Siberian larch forest. Environmental Research Letters, 15, 095006. DOI: 10.1088/1748-9326/ab9be4

# 이 논문을 찾은 이유
LiDAR 기반 세밀 지형과 식생모델을 연결할 때 SEIB-DGVM 계보 안에 지형->수문->식생 피드백의 published precedent가 존재하는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 coupling
- SEIB-DGVM + NOAH-LSM + TOPMODEL 계열 지형수문 보정

# 공간 구조
- 대규모 grid 내부의 elevation heterogeneity를 elevation classes와 CTI로 표현
- genuine 2D lateral hydrology는 아님
- within-grid topographic redistribution parameterization

# 적용 환경
- 동시베리아 낙엽송림
- 영구동토
- 건조 및 과습 스트레스
- 반복 산불이 존재하는 boreal forest context

# 핵심 과정
- topographic index
- soil-water redistribution
- drought stress
- over-wet mortality
- vegetation-thermohydrology feedback
- SEIB individual-tree dynamics

# 식생 입력
- SEIB tree state
- LAI
- biomass
- tree abundance
- soil moisture and soil temperature feedback

# 핵심 식
TOPMODEL 계열 combined topographic index와 elevation heterogeneity를 이용해 한 grid 내부 토양수분 재분배를 모의하고, 각 지형등급의 수분상태를 식생 생존과 연결한다.

# 파라미터와 단위
- elevation
- elevation standard deviation
- CTI
- soil moisture
- soil temperature
- model exchange variables are updated daily in the SEIB-NOAH lineage

# 원 논문의 구현 범위
대규모 동시베리아 격자에서 subgrid topography가 토양수분 및 낙엽송 생존에 미치는 효과를 모의한다.

# 고운사에 직접 사용할 수 있는 부분
- topography -> hydrology -> vegetation의 published SEIB coupling precedent
- 사면 위치 및 습윤도 차이를 식생 회복에 되먹임하는 구조
- SEIB를 지형상태와 완전히 독립적인 point model로만 볼 필요가 없다는 근거

# 새로운 coupling이 필요한 부분
- LiDAR DEM의 실제 lateral flow와 CTI를 1-5 m 지형격자에서 계산
- event-scale geomorph hydrology와 SEIB soil moisture state 연결
- geomorphic soil depth 변화가 NOAH/SEIB soil layers에 미치는 영향

# 한계
TOPMODEL 방식은 LiDAR-scale 2D 수문해석 자체가 아니다. CTI 기반 subgrid redistribution이므로 고운사 유수침식 모델의 수문을 대체할 수 없다.

# 최종 판정
- 채택: topography-vegetation coupling precedent
- 주 수문/침식 엔진으로는 사용하지 않음

# 참고 링크 / DOI
https://doi.org/10.1088/1748-9326/ab9be4
