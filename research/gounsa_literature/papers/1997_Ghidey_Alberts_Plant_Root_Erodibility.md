# 서지정보
Ghidey, F., & Alberts, E. E. (1997). *Plant root effects on soil erodibility, splash detachment, soil strength, and aggregate stability*. Transactions of the ASAE, 40(1), 129-135. DOI: 10.13031/2013.21257.

# 이 논문을 찾은 이유
interrill erodibility가 cover가 아니라 root mass 또는 root length density와 직접 관계하는 실험근거를 확인하기 위해 검토했다.

# 연구 유형
- laboratory rainfall-simulation experiment
- empirical erosion/root relation
- 수치모델 논문 아님

# 공간 구조
- laboratory soil samples/plots

# 적용 환경
- Mexico silt loam
- crop treatments: alfalfa, Canada bluegrass, corn, soybean

# 핵심 과정
- interrill erosion
- splash detachment
- soil strength
- aggregate stability

# 식생 입력
- dead root mass/density
- root length density

# 핵심 식
이 채팅에서 Gyssels review를 통해 확인한 대표 relation:
```
K_i = 3.55 exp(-0.71 RD)
K_i = 3.62 exp(-0.029 RLD)
```
해당 계수/단위는 원 논문 조건을 그대로 확인하여 사용할 것.

# 파라미터와 단위
- RD: root density
- RLD: root length density
정확한 units는 original tables/equations 기준.

# 원 논문의 구현 범위
root quantities와 interrill erodibility의 empirical relationship.

# 고운사에 직접 사용할 수 있는 부분
WEPP/PROMET 계열 root-effect parameterization이 물리적/실험적으로 근거를 가진다는 보조증거.

# 새로운 coupling이 필요한 부분
이 회귀식을 고운사 numerical model에 직접 삽입하면 **새로운 model coupling/parameterization**이다.

# 한계
- 농경 실험
- numerical-model implementation 아님
- 산림 산지 검증 아님

# 최종 판정
**보조근거 בלבד: empirical root-interrill relationship.** 최종 모델 자체로 사용하지 않는다.

# 참고 링크 / DOI
10.13031/2013.21257
