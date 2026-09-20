# 서지정보
McGuire, L. A., et al. (2013). *Controls on the spacing and geometry of rill networks on hillslopes: Rain splash detachment, initial hillslope roughness, and the competition between fluvial and colluvial transport*. Journal of Geophysical Research: Earth Surface, 118, 241-256. DOI: 10.1002/jgrf.20028.

# 이 논문을 찾은 이유
실제 2D rill network가 지형-유동-침식 피드백으로 자발적으로 발생하는 모델을 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- morphodynamic rill-network model

# 공간 구조
- genuine 2D
- microtopography 기반
- branching/merging/incision 발생

# 적용 환경
- 실험적 hillslope scale
- 원래 격자 약 15 mm 수준으로 고운사 산지 규모와 큰 스케일 차이

# 핵심 과정
- shallow surface flow
- rain-splash damaged layer
- fluvial erosion/deposition
- storm-time diffusive transport
- DEM update
- emergent rill network

# 식생 입력
- 사실상 없음

# 핵심 식
대표 지형갱신식:
```
∂z/∂t = β∇²z + (D-E)/(1-φ)
```

# 파라미터와 단위
세부 단위는 원문 표 재확인 필요.

# 원 논문의 구현 범위
미세지형에서 erosion-flow-topography feedback으로 rill network를 자발적으로 생성한다.

# 고운사에 직접 사용할 수 있는 부분
- emergent rill-network 물리의 강한 선례
- rill 위치를 처음부터 고정하지 않아도 되는 접근의 근거

# 새로운 coupling이 필요한 부분
- McGuire erosion equation을 Wu/WEPP 식으로 교체하면 **새로운 coupling**
- McGuire를 단순 rill-mask generator로 쓰는 절차 역시 원 논문에 정의되지 않았으므로 **새로운 coupling**

# 한계
- 식생모듈 없음
- 스케일 차이 큼
- storm-time `β∇²z`는 Pelletier 계열 장기 creep/bioturbation과 동일 과정이 아님

# 최종 판정
**보조근거/고급 rill-network 후보.** 고운사 본체에 그대로 이식하기보다 rill emergence의 검증·비교계보로 유지.
