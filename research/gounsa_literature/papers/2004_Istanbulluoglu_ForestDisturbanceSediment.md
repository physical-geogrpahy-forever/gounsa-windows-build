# 서지정보
Istanbulluoglu, E., Tarboton, D. G., Pack, R. T., & Luce, C. H. (2004). Modeling of the interactions between forest vegetation, disturbances, and sediment yields. *Journal of Geophysical Research: Earth Surface, 109*, F01009. https://doi.org/10.1029/2003JF000041

# 이 논문을 찾은 이유
산불 이후 산림 식생이 유수침식, gully erosion, shallow landslide, debris flow에 어떻게 연결되는지 실제 수치모델로 확인하기 위해 검토했다. 특히 overstory와 understory가 서로 다른 지형기능을 갖는 모델을 찾는 목적이 있었다.

# 연구 유형
- 수치모델
- 장기 산림 교란-침식 결합모델

# 공간 구조
- DEM grid 기반 distributed model
- 연 단위 vegetation/disturbance update
- 수문 및 침식사건은 확률적 극한사건으로 구동

# 적용 환경
- 산지
- 산림
- 산불 후
- 벌채 후
- Idaho Batholith

# 핵심 과정
- hillslope diffusion
- gully erosion
- shallow landslide
- debris flow
- soil production
- wildfire disturbance
- fire-induced water repellency

# 식생 입력
- understory biomass
- ground cover
- vegetation roughness
- overstory root cohesion
- disturbance-induced vegetation loss

# 핵심 식
유효전단응력 roughness partition은 기존 기록에서 다음 구조로 복구되었다.

```
f_s = (n_s / n_t)^1.5
```

기존 root cohesion의 감소는 지수형 decay로 표현하고, 새 식생의 root strength는 sigmoid recovery로 별도 계산한다. understory biomass는 ground cover로 변환되고, ground cover는 Manning roughness로 연결된다.

핵심 설계는 다음이다.

```
surface protection recovery != root-strength recovery
```

# 파라미터와 단위
- root cohesion: kPa
- understory biomass: 질량 면적 단위
- Manning roughness: 무차원
- 회복 및 decay 계수: 시간함수 파라미터
- mature root cohesion 등 연구지점별 수치는 Idaho 조건에 맞춘 값이므로 고운사에 직접 이식하지 않는다.

# 원 논문의 구현 범위
산불과 벌채가 water repellency, surface roughness, root cohesion을 서로 다르게 변화시키고, 그 결과 gully erosion과 mass wasting의 빈도 및 규모가 달라지는 구조를 구현한다.

# 고운사에 직접 사용할 수 있는 부분
- 산불 후 surface effect와 root effect를 별도 시간척도로 처리하는 설계
- understory surface resistance와 overstory root cohesion을 분리하는 구조
- 산불 직후 accelerated erosion period 개념
- 단일 vegetation factor로 모든 과정을 동시에 조절하지 않는 근거

# 새로운 coupling이 필요한 부분
LPJ-GUESS의 PFT별 biomass pools를 이 논문의 roughness 및 root-strength 변수로 직접 전달하는 연결은 원 논문에 없다. 고운사에서는 반드시 `새로운 coupling`으로 표기한다.

# 한계
- Idaho의 산림 및 기후 조건에 맞춘 파라미터
- LPJ-GUESS와 직접 결합된 모델이 아님
- 원 논문의 단순 식생회복식을 고운사에 그대로 복사하면 안 됨
- 하층 biomass를 최종적으로 cover/roughness로 매핑하므로 LPJ-GUESS canopy state와 지표 ground cover를 혼동하면 안 됨

# 최종 판정
- 채택
- 역할: 산불 후 surface recovery와 root recovery의 분리 근거

# 참고 링크 / DOI
https://doi.org/10.1029/2003JF000041
