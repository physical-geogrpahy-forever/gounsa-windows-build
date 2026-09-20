# 서지정보
Dantas de Paula, M., Forrest, M., Warlind, D., Darela Filho, J. P., Fleischer, K., Rammig, A., & Hickler, T. (2025). *Including the phosphorus cycle into the LPJ-GUESS dynamic global vegetation model (v4.1, r10994) – global patterns and temporal trends of N and P primary production limitation*. Geoscientific Model Development, 18, 2249-2274. DOI: 10.5194/gmd-18-2249-2025.

# 이 논문을 찾은 이유
고운사의 100년 식생-지형 모델에서 Pelletier식 장기 weathering proxy 대신, LPJ-GUESS 자체 상태와 더 짧은 시간간격으로 직접 연결되는 chemical-weathering implementation이 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- LPJ-GUESS v4.1 확장
- phosphorus-cycle / chemical-weathering implementation

# 공간 구조
- LPJ-GUESS gridcell
- replicate patch
- 15-layer mineral-soil hydrology
- weathering calculation itself is patch based

# 적용 환경
- global terrestrial ecosystems
- lithology-dependent chemical weathering

# 핵심 과정
- carbonate/silicate chemical weathering
- P liberation
- runoff dependence
- soil-temperature dependence
- soil shielding
- vegetation-hydrology-weathering feedback

# 식생 입력
weathering 식에 biomass가 직접 곱해지는 구조는 아니다.

그러나 LPJ-GUESS가 계산하는 vegetation structure가 runoff를 변화시키고, 그 prognostic runoff가 weathering 식에 직접 들어간다.

따라서 원 논문 자체에:
```
vegetation
 -> LPJ-GUESS hydrology/runoff
 -> chemical weathering
```
의 동적 연결이 존재한다.

# 시간간격
**Daily weathering rates are calculated for each simulated patch.**

사용 상태:
- daily prognostic soil temperature
- LPJ-GUESS prognostic runoff

따라서 Pelletier 2013의 geologic-timescale vegetation-weathering relation보다 고운사 100년 simulation의 forcing timescale에 훨씬 가깝다.

# 핵심 식

P weathering:
```
F_PW
=
F_CW,i(lithology, runoff)
* F_T(temperature)
* F_s,i(lithology)
```

Chemical-weathering/P-liberation term:
```
F_CW,i
=
(b_carbonate + b_silicate)_i
* p_i
* q
```

where:
- `q`: prognostic runoff of each simulated LPJ-GUESS patch [mm yr^-1 basis in the empirical weathering formulation]
- `p_i`: lithology-specific P content
- `b_carbonate`, `b_silicate`: lithology-specific weathering parameters

Temperature factor:
```
F_T
=
exp[
  -(Ea_i/R)
  * (1/T - 1/T0)
]
```

with:
```
T0 = 284.15 K
```

The paper also applies a lithology-dependent soil-shielding factor `F_s,i`.

# 파라미터와 단위
- `F_PW`: P-weathering/liberation flux
- `F_CW,i`: reported in t km^-2 yr^-1 in the Appendix formulation
- `q`: runoff
- `T`: daily prognostic soil temperature [K]
- lithology and shielding parameters from Hartmann-Moosdorf / Hartmann et al. lineage

Exact conversion from P liberation to total rock/regolith mass must not be inferred from `p_i` without returning to the parent CWM formulation.

# 원 논문의 구현 범위
This is an **actual LPJ-GUESS implementation**, not an external conceptual coupling.

It dynamically links:
```
LPJ-GUESS runoff + temperature + lithology
 -> daily chemical weathering
 -> soil P supply
 -> vegetation nutrient limitation
```

# 고운사에 직접 사용할 수 있는 부분
Strong candidate for the **hydroclimatic chemical-weathering driver**.

Advantages over Pelletier 2013:
1. already inside LPJ-GUESS
2. daily update
3. vegetation affects runoff
4. temperature and lithology explicit
5. no need to infer annual weathering from EEMT/AGB alone

# 새로운 coupling이 필요한 부분
This paper computes nutrient-release/chemical-weathering flux, not geomorphic regolith-thickness production.

Therefore:
```
chemical weathering mass / mineral alteration
 -> C/Cr or soil/regolith thickness change
```
is a **new coupling** unless a validated solid-volume/mass-balance relation is adopted.

Also, direct deep-root respiration enhancement from Osorio-Leon et al. 2025 is not part of this LPJ-GUESS-CNP weathering equation.

# 한계
- designed for P cycle, not landscape evolution
- global lithology parameterization may need local lithology replacement
- does not explicitly fracture bedrock by roots
- does not itself update DEM or regolith thickness
- daily weathering calculation does not mean daily measurable geomorphic lowering; rates can be accumulated to annual mass balance

# 최종 판정
**채택: 100년 고운사 chemical-weathering forcing의 1차 후보.**

Pelletier 2013보다 시간척도와 LPJ-GUESS coupling 면에서 우선한다.

Geomorphic thickness production still requires a separate mass/volume conversion and mechanical-weathering module.

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-18-2249-2025
