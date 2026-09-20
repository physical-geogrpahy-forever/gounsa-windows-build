# 서지정보
Saco, P. M., & Moreno-de las Heras, M. (2013). Ecogeomorphic coevolution of semiarid hillslopes: Emergence of banded and striped vegetation patterns through interaction of biotic and abiotic processes. *Water Resources Research, 49*(1), 115-126. https://doi.org/10.1029/2012WR012001

# 이 논문을 찾은 이유
SIBERIA의 fluvial sediment transport parameter에 식생 biomass density가 직접 들어가는 published precedent를 확인하고, COPLAS식 지역내 정규화 없이 절대 biomass를 쓸 수 있는지 검토하기 위해 확인했다.

# 연구 유형
- 수치모델
- coupled vegetation-landform evolution model

# 공간 구조
- distributed hillslope
- runoff routing과 SIBERIA landform evolution coupling
- 2D hillslope grid

# 적용 환경
- 반건조 사면
- patterned vegetation

# 핵심 과정
- runoff-runon
- fluvial sediment transport
- diffusive transport
- plant growth
- topographic evolution

# 식생 입력
- plant biomass density P, g m-2

# 핵심 식
지형수지:

```
dz/dt = -(div qs + div qd) + U
```

fluvial sediment transport:

```
qs = beta1 * q^m1 * S^n1
```

식생에 따른 erodibility-related parameter:

```
beta1 = betab * (1 - betav * P)
```

단, minimum erodibility `beta_min`을 둔다.

diffusive transport:

```
qd = D * S
```

이 논문에서는 biomass가 diffusion coefficient D에 직접 들어가지 않는다.

# 파라미터와 단위
- P: g m-2
- betav: biomass 1 g m-2당 erodibility 감소효과에 대응
- D: m2 time-1 계열
- q, S, m1, n1: SIBERIA fluvial transport variables

# 원 논문의 구현 범위
absolute biomass density와 evolving topography를 직접 결합하며, biomass가 infiltration과 fluvial erodibility에 영향을 준다.

# 고운사에 직접 사용할 수 있는 부분
- 지역별 B/Bmax 정규화 없이 절대 biomass를 geomorphic coefficient에 넣는 선례
- direct biomass-erodibility sensitivity model
- 식생-지형 양방향 feedback의 단순 비교구조

# 새로운 coupling이 필요한 부분
LPJ-GUESS의 PFT별 biomass 또는 FineRootC를 각각 다른 `beta_v,i`로 연결하는 것은 원 논문에 없는 `새로운 coupling`이다.

# 한계
- PFT 차이를 직접 표현하지 않는다
- 반건조 vegetation model이므로 고운사 산림에 계수를 직접 이식할 수 없다
- genuine 2D 산지 집중류 최종 엔진을 단독으로 충족하는 모델은 아니다

# 최종 판정
- 보조근거
- direct biomass sensitivity 비교모델

# 참고 링크 / DOI
https://doi.org/10.1029/2012WR012001

## 2026-09-21 현재 채팅 최종 보정
- 이 논문의 biomass-erodibility 관계는 유용한 직접 biomass 선례이지만, **유출 라우팅은 SIBERIA 계열의 steepest-descent/D8 단일유향 구조**이므로 HighLand의 분산 지표유출과 동일시하지 않는다.
- 고운사에서는 Saco의 라우팅을 채택하지 않는다. biomass가 erodibility를 낮추는 개념만 보조근거로 사용한다.
- 면상침식과 집중류침식을 하나의 fluvial term으로 합치는 구조도 고운사 최종안에는 쓰지 않는다.
