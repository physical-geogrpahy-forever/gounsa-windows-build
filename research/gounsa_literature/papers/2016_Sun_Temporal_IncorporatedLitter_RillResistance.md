# 서지정보
Sun, L., Zhang, G.-H., Luan, L.-L., & Liu, F. (2016). *Temporal variation in soil resistance to flowing water erosion for soil incorporated with plant litters in the Loess Plateau of China*. CATENA, 145, 239-245. DOI: 10.1016/j.catena.2016.06.016.

# 이 논문을 찾은 이유
incorporated litter의 erosion resistance effect가 시간에 따라 분해/토양안정화와 함께 변하는지 확인하기 위해 검토했다.

# 연구 유형
- field-sampled hydraulic-flume experiment
- temporal parameterization study
- numerical model 자체는 아님

# 공간 구조
- topsoil samples from field plots
- repeated flow-scour experiments

# 적용 환경
- Loess Plateau
- black locust, sea buckthorn, green bristle grass litter incorporation

# 핵심 과정
- rill erodibility
- critical shear stress
- soil consolidation
- litter decomposition

# 식생 입력
- incorporated litter
- litter mass density
- litter decomposition state

# 핵심 식
Key temporal results:
- `K_r` decreased significantly over time as an exponential function
- fitted `tau_c` increased exponentially with time
- `K_r` could be estimated by soil bulk density, water-stable aggregates, and litter mass density, R2 about 0.92

Mean Kr:
- control about 0.27 s m^-1
- litter treatments about 0.20-0.22 s m^-1

# 파라미터와 단위
- Kr: s m^-1
- tau_c: Pa
- litter mass density and soil-structure variables
Exact temporal regression coefficients require full-paper verification.

# 원 논문의 구현 범위
Shows that litter effects on erosion resistance are **time-dependent**, not a static multiplier.

# 고운사에 직접 사용할 수 있는 부분
Postfire recovery can distinguish:
```
litter amount
+ litter decomposition/soil consolidation time
 -> Kr(t), tau_c(t)
```

This is relevant to 100-year postfire simulation where litter pools and soil structure evolve.

# 새로운 coupling이 필요한 부분
LPJ-GUESS litter turnover/decomposition to these experimental variables is a **new coupling**.

# 한계
- no 2D model
- Loess soils
- mixed effects of litter and evolving soil structure

# 최종 판정
- **채택: temporal litter-resistance evidence**
- supports dynamic rather than fixed litter protection

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2016.06.016
