# 서지정보
Naseri, M., Iden, S. C., & Durner, W. (2022). Effective hydraulic properties of 3D virtual stony soils identified by inverse modeling. *SOIL, 8*, 99-112. https://doi.org/10.5194/soil-8-99-2022

# 이 논문을 찾은 이유
GEM 등 scaling relation 대신 3D Richards simulation으로 stony soil의 effective WRC/HCC를 계산한 published path가 있는지, 그리고 어떤 scaling model이 그 결과와 맞는지 확인하기 위해 검토했다.

# 연구 유형
- 3D virtual numerical experiment
- HYDRUS 2D/3D
- inverse modeling

# 공간 구조
- 3D soil volume with embedded impermeable spherical RF
- 1D effective-property inverse representation

# 적용 환경
- sandy loam virtual stony soil
- RF volume fraction 11-37%

# 핵심 과정
- variably saturated water flow
- evaporation
- unit-gradient flow
- effective WRC
- effective HCC

# 식생 입력
- 없음

# 핵심 식
3D Richards equation simulation으로 heterogeneous flow를 생성한 뒤, homogeneous 1D model의 effective hydraulic properties를 inverse modeling으로 식별한다.

# 파라미터와 단위
- RF volumetric fraction f: 11-37%
- WRC parameters
- HCC parameters
- matric potential
- water content
- hydraulic conductivity

# 원 논문의 구현 범위
WRC는 impermeable RF 조건에서 단순 volume scaling도 비교적 잘 맞았으나, HCC는 f만으로 단순 scaling할 수 없었다.
Novák, Maxwell, GEM 등의 conductivity scaling이 예측을 개선했고 이 virtual spherical-RF experiment에서는 Maxwell이 가장 잘 맞았다.

# 고운사에 직접 사용할 수 있는 부분
- 고운사의 embedded RF geometry를 explicit 3D hydraulic model로 계산하고 effective WRC/HCC를 도출하는 published architecture
- 현장 effective property 측정이 어려울 때 GEM 하나에 의존하지 않는 benchmark
- Richards-equation hydrology와 reduced effective-property model 사이의 연결근거

# 새로운 coupling이 필요한 부분
고운사 실제 fragment shapes, sandstone permeability, root macropores를 3D domain에 반영하는 것은 site-specific parameterization이다.

# 한계
- impermeable spherical RF
- f 최대 37%
- 실제 산림토양의 macropore/contact-gap heterogeneity는 단순화

# 최종 판정
- 핵심 채택 후보
- high embedded-stoniness hydraulic-property estimation의 geometry-explicit 대안

# 참고 링크 / DOI
https://doi.org/10.5194/soil-8-99-2022
