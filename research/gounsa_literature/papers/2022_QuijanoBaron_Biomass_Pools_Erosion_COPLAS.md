# 서지정보
Quijano-Baron, J., Saco, P. M., & Rodriguez, J. F. (2022). Modelling the effects of above and belowground biomass pools on erosion dynamics. *Catena, 213*, 106123. https://doi.org/10.1016/j.catena.2022.106123

# 이 논문을 찾은 이유
leaf, root, litter, wood, soil carbon을 서로 다른 침식 메커니즘에 연결하는 수치모델을 검토하고 고운사 적용 가능성을 평가하기 위해 읽었다.

# 연구 유형
- 수치모델

# 공간 구조
- SIBERIA 기반 raster/distributed LEM
- steepest downslope direction 기반 routing
- 일 단위 순차결합

# 적용 환경
- 호주 Howard Springs tropical woodland savanna

# 핵심 과정
- fluvial sediment transport
- diffusive transport
- hydrology
- biomass pools
- erosion/deposition

# 식생 입력
- leaf biomass
- root biomass
- litter biomass
- wood biomass
- soil carbon
- LAI
- big-leaf vegetation

# 핵심 식
```text
q_s = beta q^m S^n
q_d = D S
D = Dmax - alpha Lhat
n = nbare + nref Lithat^w
```

Root 정규화:
```text
Rhat = ((R - Rmean) / Rstd) / 5 + 0.5
```
leaf, litter, soil carbon도 같은 방식의 site-specific 정규화를 사용한다.

# 파라미터와 단위
- normalized biomass pools: 0–1
- alpha = 0.5
- litter exponent w = 1
- Dmax와 최대 erodibility는 보정

# 원 논문의 구현 범위
Hydrology, vegetation, biomass pools, SIBERIA landform evolution을 일 단위로 순차결합한다.

# 고운사에 직접 사용할 수 있는 부분
최종식이 아니라 기관별 biomass pool이 서로 다른 지형과정에 작용할 수 있다는 개념만 참고한다.

# 새로운 coupling이 필요한 부분
COPLAS 식을 직접 사용하지 않고 고운사에서는
- LPJ-GUESS LAI에서 실제 vegetation cover 또는 FPC 계산
- root biomass 또는 root traits에서 soil erodibility 계산
- litter mass 또는 litter cover에서 Manning n 계산
- splash와 creep 분리
등의 새로운 coupling이 필요하다.

# 한계
- site mean/std 정규화라 다른 지역으로 parameter transfer가 어려움
- Lhat = 1은 생태학적 포화상태가 아님
- leaf가 total diffusion을 조절해 splash와 creep이 함께 변함
- big-leaf 접근이라 understory와 overstory를 구분하지 못함
- LPJ-GUESS 변수와 biomass-pool 정의가 완전히 동일하지 않음

# 최종 판정
- 탈락
- SYSTEM 규칙에 따라 COPLAS는 고운사 최종모델 근거에서 제외
- biomass pool 분리 철학만 역사적 참고로 보존

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2022.106123
