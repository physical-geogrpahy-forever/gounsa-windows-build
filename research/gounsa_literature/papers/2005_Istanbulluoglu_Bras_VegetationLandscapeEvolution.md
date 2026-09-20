# 서지정보
Istanbulluoglu, E., & Bras, R. L. (2005). Vegetation-modulated landscape evolution: Effects of vegetation on landscape processes, drainage density, and topography. *Journal of Geophysical Research: Earth Surface, 110*(F2), F02012. https://doi.org/10.1029/2004JF000249

# 이 논문을 찾은 이유
식생피복을 지형과정에 직접 연결한 published landscape evolution model을 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- landscape evolution model

# 공간 구조
- distributed landscape evolution

# 적용 환경
- 식생이 존재하는 산지와 반건조 landscape

# 핵심 과정
- fluvial erosion
- hillslope diffusion
- vegetation disturbance and recovery

# 식생 입력
- vegetation cover fraction V

# 핵심 식
```text
K_d = K_b exp(-alpha V)
```
V는 0에서 1 사이의 식생피복률이다.

# 파라미터와 단위
- V: 무차원
- K_d, K_b: 지형확산계수
- alpha: 감쇠계수

# 원 논문의 구현 범위
식생피복 변화가 사면수송과 유수과정을 조절하고 장기 지형발달에 피드백한다.

# 고운사에 직접 사용할 수 있는 부분
COPLAS의 지역별 biomass 정규화 대신 실제 식생피복률을 사용하는 구조적 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS의 LAI를 식생피복률 V로 변환해 이 식에 넣는 것은 새로운 coupling이다. 후보 변환식은 `V = 1 - exp(-k LAI)`이며 k는 별도 검증이 필요하다.

# 한계
V는 LeafC나 LAI 자체와 동일하지 않으며 PFT와 상층, 하층 구조를 직접 제공하지 않는다.

# 최종 판정
- 보조근거로 채택
- LAI에서 V로의 연결은 새로운 coupling

# 참고 링크 / DOI
https://doi.org/10.1029/2004JF000249
