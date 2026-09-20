# 결정: 100년 고운사 풍화와 사면수송의 시간척도 및 모델 구조

날짜: 2026-09-21

## 질문
토양/레골리스 풍화와 사면확산에 Pelletier 2013을 사용할 것인가, 더 짧은 시간간격의 published models를 사용할 것인가?

## 결정
**Pelletier 2013을 두 과정의 주 모델로 사용하지 않는다.**

100년 고운사에서는 multi-rate modular architecture를 채택한다.

---

## 1. 풍화/토양생산

### chemical hydroclimatic weathering
**LPJ-GUESS-CNP 2025를 1차 driver로 채택.**

이유:
- LPJ-GUESS 내부 구현
- patch별 daily weathering
- daily soil temperature
- prognostic runoff
- vegetation structure가 hydrology를 통해 weathering에 영향

구조:
```
LPJ-GUESS
 -> runoff + soil temperature
 -> daily chemical weathering
 -> annual accumulated weathering flux
 -> [NEW COUPLING] regolith mass/thickness change
```

### woody mechanical weathering
**Gabet & Mudd 2010 annual model lineage를 채택.**

```
LPJ-GUESS woody cohort/root state
 -> root fracture
 -> physical bedrock erosion
 -> soil/regolith production
```

Original paper uses annual timestep.

### comparison/validation
- REWTCrunch 2022: root-induced reactive transport
- SoilGen 2022: daily-hydrology soil-profile chemical weathering
- SSSPAM: physical weathering/profile/armour
- Pelletier 2013: long-term structural benchmark

---

## 2. 사면수송

단일 biomass-dependent diffusivity를 사용하지 않는다.

```
q_hill
=
q_bg
+
q_rootgrowth
+
q_treethrow
+
q_dryravel
```

### q_bg
First implementation:
```
q_bg = -D_bg S
```
as a **residual background creep** term.

Reason:
- explicit tree throw is separate
- explicit root-growth transport is separate
- postfire dry ravel is separate
- shallow landslide is separate
- therefore a natural-landscape total diffusivity would double count processes

### nonlinear sensitivity
Roering 2001:
```
q
=
-K grad(z)
/
[1-(|grad(z)|/S_c)^2]
```
is retained as a steep-slope sensitivity/alternative.

Do not use a field-calibrated total `K` unchanged while adding tree throw/root growth/landslides separately.

### q_rootgrowth
**Gabet et al. 2003**, annual root turnover.

Use LPJ-GUESS native root state/turnover.

### q_treethrow
**Doane et al. 2021**, annual stochastic event process.

Supporting actual annual model precedent:
CSDMS TreeThrow.

### q_dryravel
Lamb 2011 postfire disturbance/storage pathway, already separately adopted.

### shallow landslide
separate discrete module, not hidden inside nonlinear diffusion.

---

## 3. 왜 Pelletier를 내리는가

Pelletier 2013:
- geologic-time-scale model objective
- fixed/prescribed EEMT across individual runs
- reported topographic states after 10 Myr
- small numerical timestep only because of explicit-solver stability

Thus:
```
small dt in code
!=
annual ecological calibration
```

Direct:
```
LPJ-GUESS biomass(t)
 -> Pelletier diffusivity(t)
```
is not treated as an existing published annual coupling.

---

## 4. 왜 HydroLorica를 본체로 쓰지 않는가
HydroLorica has daily/monthly/yearly hydrology, but its own paper explicitly warns that its annually changing simplified vegetation type should not be used to study annual-to-decadal systems.

Thus it is an architecture reference only.

---

## 5. SSSPAM 판정
SSSPAM demonstrates:
- 100-year LEM application
- physical weathering
- diffusion
- armour
- subsurface soil-profile evolution

But it lacks dynamic forest/root states and overlaps SWEHR erosion/surface-sediment state.

Therefore:
**comparison + possible future coarse-fragment/armour source, not primary core.**

---

## 6. temporal coupling

### daily
- LPJ-GUESS hydrology and chemical-weathering driver

### rainfall event
- SWEHR water erosion

### annual
- accumulated chemical-weathering bookkeeping
- root-growth/decay bioturbation
- woody mechanical weathering
- tree throw
- background creep
- soil/regolith/DEM update

### disturbance event
- wildfire
- dry ravel
- shallow landslide
- major windthrow if modeled

---

## 7. unresolved items

1. LPJ-GUESS-CNP chemical-weathering flux -> geomorphic regolith mass/thickness conversion
2. Gounsa lithology parameters for chemical weathering
3. LPJ-GUESS woody cohorts -> root-fracture/rootwad geometry
4. residual background creep `D_bg` calibration without double counting
5. tree-throw event geometry/rate from LPJ-GUESS cohort state
6. whether Roering nonlinear residual materially improves the 100-year result
7. weathering significance over only 100 years: quantify before adding unnecessary complexity
8. coarse-fragment/armour state reconciliation with SWEHR

---

## 8. final current architecture

```
LPJ-GUESS
  |
  +-- daily runoff + Tsoil
  |      -> chemical weathering
  |
  +-- annual root state/turnover
  |      -> Gabet root-growth transport
  |
  +-- annual woody cohorts/mortality
  |      -> Gabet-Mudd mechanical weathering
  |      -> Doane tree throw
  |
  +-- background
  |      -> residual creep
  |
fire
  +-- dry ravel
  +-- spall [separate]
  |
slope failure
  +-- shallow landslide [separate]
```

## 최종 판정
**100년 고운사에서는 Pelletier보다 process-specific daily/annual models를 우선한다.**

Pelletier는 장기 consistency benchmark로 유지한다.


---

## 2차 감사

이 결정은 유지되며 다음 파일에서 근거 서지와 역할을 재감사했다:

`decisions/2026-09-21_WEATHERING_HILLSLOPE_SECOND_PASS_AUDIT.md`

2차 감사의 주요 보정:
- LPJ-GUESS-CNP는 full soil-production engine이 아니라 daily chemical-weathering/P-release forcing
- Gabet et al. 2021 DOI 10.1029/2020JF005858의 기존 biomass-transport 해석 철회
- Pelletier et al. 2018 DOI 10.1002/esp.4306의 기존 biomass-diffusivity 해석 철회
- Kirwan & Shugart 2008을 AGU abstract로 재분류
- Roering & Gerber 2005, Jackson & Roering 2009를 postfire dry-ravel/root-decay process-separation 근거로 강화

최종 아키텍처 자체는 변경되지 않는다.
