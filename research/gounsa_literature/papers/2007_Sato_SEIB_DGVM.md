# 서지정보
Sato, H., Itoh, A., & Kohyama, T. (2007). SEIB-DGVM: A new Dynamic Global Vegetation Model using a spatially explicit individual-based approach. Ecological Modelling, 200(3-4), 279-307. DOI: 10.1016/j.ecolmodel.2006.09.006

# 이 논문을 찾은 이유
LPJ-GUESS의 patch 내부 공간 비명시성 문제를 피하면서 일 단위 생리, 개체목 경쟁, 뿌리와 litter 상태를 제공할 수 있는 식생모델인지 검토했다.

# 연구 유형
- 수치모델
- 공간명시적 개체기반 DGVM

# 공간 구조
- 기본 virtual forest 30 m x 30 m
- 내부 1 m x 1 m simulation cell
- 개별목의 위치, 수관 경쟁, 주변목 영향을 명시적으로 계산
- 각 기후 grid box에 하나의 sample plot을 배치하는 구조

# 적용 환경
- 다양한 생물군계
- 지역 및 전지구 식생동태
- 후속 연구에서 시베리아 산불 후 천이 적용

# 핵심 과정
- 광합성 및 호흡
- 탄소배분
- 개체목 정착
- 생장
- 경쟁
- 사망
- 초본과 목본 공존
- litter turnover
- wildfire disturbance

# 식생 입력/상태
- leaf biomass
- trunk biomass
- fine-root biomass
- grass biomass
- litter pools
- LAI
- 개별목 위치와 크기

# 핵심 식
개별목을 3차원적으로 배치하고 각 개체의 광환경과 탄소수지를 계산한다. 생리과정은 일 단위, 줄기생장은 월 단위, 정착/사망/교란은 연 단위로 갱신되는 계보로 발전했다.

# 파라미터와 단위
- virtual forest: 30 m x 30 m
- internal cell: 1 m x 1 m
- physiology: daily
- trunk growth: monthly
- vegetation dynamics/disturbance: annual

# 원 논문의 구현 범위
각 grid box 내부의 30 m 가상림에서 개체목 공간경쟁과 생지화학 과정을 결합한다.

# 고운사에 직접 사용할 수 있는 부분
- 30 m 셀 크기와 잘 맞는 virtual forest
- 1 m 내부 개체목 공간구조
- fine-root biomass
- litter
- 일 단위 생리
- 산불 후 천이 표현 가능

# 새로운 coupling이 필요한 부분
- 고운사 유역의 각 30 m 셀을 독립 virtual forest로 배치
- 셀 사이 종자 이동과 식생 확산을 지형격자에 맞게 연결
- 지형모델의 soil depth/moisture 변화를 각 plot에 전달
- SEIB root/litter 상태를 erosion/root mechanics 입력으로 변환

# 한계
공개 기본 배포판은 단일 virtual forest point simulation이다. 다중 plot 계산 코드는 있으나, 표준 공개 구조가 30 m 유역 셀 사이의 실제 종자 이동과 상호작용을 제공한다고 볼 근거는 없다. 따라서 LPJ-GUESS의 '셀 간 독립성' 문제를 완전히 해결하지 않는다.

# 최종 판정
- 강한 보류 후보
- 셀 내부 공간구조는 현재 검토 후보 중 최고 수준
- 유역 셀 간 연결성이 핵심 미검증점

# 참고 링크 / DOI
https://doi.org/10.1016/j.ecolmodel.2006.09.006
https://seib-dgvm.com/en/?page_id=40
