# 서지정보
Bai, Y., Zhang, J., Zhang, S., Koju, U. A., Yao, F., & Igbawua, T. (2017). *Using precipitation, vertical root distribution, and satellite-retrieved vegetation information to parameterize water stress in a Penman-Monteith approach to evapotranspiration modeling under Mediterranean climate*. Journal of Advances in Modeling Earth Systems, 9, 168-192. DOI: 10.1002/2016MS000702.

# 이 논문을 찾은 이유
root biomass/RootC를 토심별로 배분하는 vertical root distribution 후보를 확인하기 위해 검토했다.

# 연구 유형
- 수문/ET 모델
- erosion model 아님

# 공간 구조
- ET/water-stress parameterization

# 적용 환경
- Mediterranean climate

# 핵심 과정
- evapotranspiration
- soil-water stress
- vertical root distribution

# 식생 입력
- vertical root distribution
- satellite vegetation information

# 핵심 식
대표 구조:
```
Y = β^d
```
형태로 토심별 누적 root fraction을 계산한다.

# 파라미터와 단위
- β: root-distribution parameter
- d: depth
정확한 정의/단위는 원문 notation을 따른다.

# 원 논문의 구현 범위
vertical root distribution을 ET water-stress 계산에 사용한다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS가 필요한 토심별 root distribution을 충분히 제공하지 않을 때 보조 근거가 될 수 있다.

# 새로운 coupling이 필요한 부분
erosion Ki/Kr 또는 root cohesion에 연결하면 **새로운 coupling**.

# 한계
erosion model이 아니다. LPJ-GUESS 자체 root distribution이 충분하면 필요성이 낮다.

# 최종 판정
**보조근거.**

# 참고 링크 / DOI
10.1002/2016MS000702
