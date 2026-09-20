# 서지정보
Gould, G. K., Liu, M., Barber, M. E., Cherkauer, K. A., Robichaud, P. R., & Adam, J. C. (2016). *The effects of climate change and extreme wildfire events on runoff erosion over a mountain watershed*. Journal of Hydrology, 536, 74-91. DOI: 10.1016/j.jhydrol.2016.02.025.

# 이 논문을 찾은 이유
Mao et al.의 VIC-WEPP coupling이 실제 산불 산지에 적용된 선례인지 확인하기 위해 검토했다.

# 연구 유형
- coupled numerical model application
- wildfire/climate scenario modeling

# 공간 구조
- VIC large-scale hydrology + representative WEPP hillslopes
- genuine 2D shallow-water flow는 아님

# 적용 환경
- northern Rocky Mountains
- Salmon River Basin, Idaho
- elevation 약 304-3713 m
- wildfire mountain watershed

# 핵심 과정
- large-scale hydrology
- runoff erosion
- postfire parameterization
- representative hillslope WEPP erosion

# 식생 입력
VIC-WEPP/WEPP 계보를 통해 vegetation/soil erodibility adjustment를 사용한다. 이 채팅에서의 역할은 특히 산불 산지 적용 선례 확인이다.

# 핵심 식
개별 WEPP 식은 WEPP 모델 계보 파일과 Mao 2010 파일을 참조한다.

# 파라미터와 단위
논문별 postfire parameterization은 원문 표 기준으로 사용한다.

# 원 논문의 구현 범위
VIC-WEPP를 10,000 km2 이상 산악 유역의 기후변화와 wildfire erosion 평가에 적용.

# 고운사에 직접 사용할 수 있는 부분
- 산불 산지 + WEPP-based erosion coupling의 강한 published precedent
- mountain watershed 적용성 근거

# 새로운 coupling이 필요한 부분
VIC 대신 LPJ-GUESS/다른 hydrology를 쓰거나 genuine 2D engine으로 교체하면 **새로운 coupling**.

# 한계
- representative hillslope approach
- genuine 2D surface hydraulics 아님

# 최종 판정
**채택: 산불 산지 적용 선례.**

# 참고 링크 / DOI
10.1016/j.jhydrol.2016.02.025
