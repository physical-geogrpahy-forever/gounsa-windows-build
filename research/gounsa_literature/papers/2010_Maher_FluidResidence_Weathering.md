# 서지정보
Maher, K. (2010). The dependence of chemical weathering rates on fluid residence time. *Earth and Planetary Science Letters, 294*(1-2), 101-110. DOI: 10.1016/j.epsl.2010.03.010.

# 이 논문을 찾은 이유
고운사 chemical weathering에서 식생 chemistry보다 hydrology와 water residence time이 더 큰 제어가 될 수 있는지 확인하고, WITCH/PROFILE/BioRT coupling의 필수 hydrologic state를 정하기 위해 검토했다.

# 연구 유형
- reactive-transport analysis
- field-data synthesis
- numerical modeling

# 공간 구조
- 1D soil/weathering profile
- flow path / equilibration length

# 적용 환경
- soils
- aquifers
- granitic weathering systems
- broad natural weathering datasets

# 핵심 과정
- advection
- mineral dissolution
- saturation-state approach
- secondary-mineral precipitation
- fluid residence time
- flow rate
- reaction affinity

# 식생 입력
직접 dynamic vegetation model 없음.

식생과 관련 가능한 forcing:
- soil CO2
- hydrologic flux
- soil structure / water residence time

# 핵심 식
mineral dissolution:

```
R_d
=
-k A (1-Q/K_eq)
```

또는 reaction affinity 형태:

```
R_d
=
-k A [1-exp(-DeltaG_r/RT)]
```

1D quasi-steady reactive transport:

```
0
=
-q dc/dz
+
R_d (1-c/c_eq)
```

where:
- q: percolation flux
- c: solute concentration
- c_eq: equilibrium concentration
- R_d: bulk weathering rate

# 핵심 결과
weathering rate variation은 material age보다:
- fluid residence time
- fluid flow rate
에 강하게 의존할 수 있다.

moderate residence-time range에서 transport-controlled weathering이 자연 weathering-rate variation을 잘 설명했다.

또한 intrinsic dissolution rate와 reactive surface area가 local reaction profile의 길이에는 중요하지만, system이 local-equilibrium limit에 도달하면 total export flux는 hydrologic flow에 의해 제한될 수 있다.

# 파라미터와 단위
- fluid residence time [time]
- percolation flux q [m yr^-1]
- mineral reactive surface area A [m2 m^-3]
- kinetic constant k [mol m^-2 s^-1]
- equilibrium state Q/K_eq
- porosity / volumetric water content

# 원 논문의 구현 범위
field/lab weathering rates를 reaction-transport timescale로 통합 해석한다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요하다.

고운사 chemical weathering에서는:

```
water residence time
flow-path depth
drainage
```

를 빠뜨리면 안 된다.

따라서 LPJ-GUESS의 runoff 총량만 W_chem에 넣는 Hartmann-only 접근은 공간/반응 측면에서 충분하지 않을 수 있다.

BioRT/Wen 2022 spatial sensitivity를 강화하는 근거다.

# 새로운 coupling이 필요한 부분
Landlab/SWEHR/LPJ-GUESS states에서:
- infiltration
- subsurface flow velocity
- residence time
를 만들고 RTM에 전달하는 것은 새로운 coupling이다.

# 한계
- granite 중심 데이터
- vegetation dynamics 직접 없음
- soil production thickness 직접 출력 아님

# 최종 판정
- **채택: chemical-weathering hydrologic control의 핵심 이론 근거**
- residence time을 production weathering interface의 필수 state 후보로 승격

# 참고 링크 / DOI
https://doi.org/10.1016/j.epsl.2010.03.010
