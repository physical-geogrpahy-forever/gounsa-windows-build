# 서지정보
Cohen, S., Willgoose, G., & Hancock, G. (2009). The mARM spatially distributed soil evolution model: A computationally efficient modeling framework and analysis of hillslope soil surface organization. *Journal of Geophysical Research: Earth Surface, 114*, F03001. https://doi.org/10.1029/2008JF001214

# 이 논문을 찾은 이유
ARMOUR의 물리적 armour-weathering 과정을 장기/공간분포 모델로 계산할 수 있는 효율적 기존 구현을 찾기 위해 검토했다.

# 연구 유형
- state-space numerical model
- ARMOUR reduction/generalisation

# 공간 구조
- spatially distributed landscape
- surface armour layer + subsurface supply

# 적용 환경
- stony hillslope / mine-spoil grading lineage

# 핵심 과정
- selective erosion
- armour formation
- physical weathering
- soil grading evolution

# 식생 입력
- 없음

# 핵심 식
soil grading vector `g_t`를 입도 class별 상태벡터로 두고:
```
g_(t+1) = A g_t
```
형태의 state-space transition matrix로 erosion/weathering에 따른 grading 변화를 계산한다.

# 파라미터와 단위
- size classes
- erosion transition matrix
- weathering transition matrix
- surface layer mass/depth

# 원 논문의 구현 범위
계산비용이 큰 ARMOUR를 state-space matrix로 근사하여 large spatial/long-term simulation이 가능하게 했다.

# 고운사에 직접 사용할 수 있는 부분
- armour와 weathering을 입도별 질량보존 transition으로 계산
- custom scalar armour coefficient 대신 state vector 사용
- 100년 반복사건 계산에 적합한 효율성

# 새로운 coupling이 필요한 부분
2D hydraulic erosion amount를 mARM transition에 전달하면 software coupling이다.

# 한계
surface 중심이며 full vertical soil profile은 후속 mARM3D가 필요.

# 최종 판정
- 핵심 채택 계보

# 참고 링크 / DOI
https://doi.org/10.1029/2008JF001214
