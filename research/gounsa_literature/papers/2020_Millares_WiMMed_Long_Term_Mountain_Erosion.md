# 서지정보
Millares, A., Herrero, J., & Bermúdez, M. (2020). *Long-term modeling of soil loss and fluvial transport processes in a mountainous semi-arid basin, southern Spain*. Conference paper, River Flow 2020, 10th Conference on Fluvial Hydraulics. 세부 proceedings pagination/DOI는 **원문 재검증 필요**.

# 이 논문을 찾은 이유
WiMMed/HEMINGS 계보가 실제 mountainous semi-arid basin에서 장기 soil loss와 fluvial transport를 계산하는지 확인하기 위해 검토했다.

# 연구 유형
- distributed numerical model application
- conference paper

# 공간 구조
- WiMMed physically based distributed model
- erosion module integrated from Millares et al. (2019)
- flow routing은 genuine 2D SWE가 아니라 distributed/D8 계열로 판정

# 적용 환경
- Mediterranean high mountain
- Guadalfeo basin, southern Spain

# 핵심 과정
- hydrology
- hillslope erosion
- fluvial sediment transport
- long-term sedimentation

# 식생 입력
vegetation map/soil map 등을 사용하지만 strict root biomass/RLD dynamic input은 이 채팅에서 확인되지 않았다.

# 핵심 식
Millares et al. (2019) erosion module을 WiMMed에 통합하는 구조.

# 파라미터와 단위
원문 재검증 필요.

# 원 논문의 구현 범위
reservoir sedimentation monitoring으로 장기 erosion/transport를 calibration-validation.

# 고운사에 직접 사용할 수 있는 부분
- 산악 유역에서 장기 distributed erosion/sediment transport를 수행한 선례
- HEMINGS/WiMMed 계보의 산지 적용성 근거

# 새로운 coupling이 필요한 부분
LPJ-GUESS biomass와 erodibility를 직접 연결하거나 genuine 2D solver로 교체하면 **새로운 coupling**.

# 한계
strict genuine 2D + quantitative vegetation 조건 미충족.

# 최종 판정
**보조근거.** 산악 적용성은 강하지만 최종 2D 엔진으로는 보류.
