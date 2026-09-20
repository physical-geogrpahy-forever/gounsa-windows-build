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
q_dryravel
```

### q_bg
Production baseline:
```
q_bg = -D*_bg H_active grad(z)
```
Furbish 2009의 active-soil-depth dependent residual creep를 사용한다.

Reason:
- root-growth transport is explicit
- postfire dry ravel is explicit
- tree throw/uprooting and shallow landslide are excluded from current baseline
- therefore natural-landscape total diffusivity는 residual coefficient로 직접 사용할 수 없다

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

Do not use a field-calibrated total `K` unchanged while adding explicit root-growth and dry-ravel terms.

### q_rootgrowth
**Gabet et al. 2003**, annual root turnover.

Use LPJ-GUESS native root state/turnover.

### tree throw / uprooting
Current production baseline에서 제외한다.
Doane/Gallaway/Constantine 계보는 future optional reference로만 보존한다.

### q_dryravel
Lamb 2011 postfire disturbance/storage pathway, already separately adopted.

### shallow landslide
Current production baseline에서 제외한다.

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
- regolith-front production
- root-growth/decay bioturbation
- residual background creep
- soil/regolith/DEM update

### disturbance event
- wildfire
- dry ravel
- fire spall

---

## 7. unresolved items

1. Gounsa lithology and weathering-front parameters
2. 100-year magnitude of chemical front advance and dissolved mass loss
3. residual background creep `D*_bg` calibration
4. exact LPJ-GUESS root-state/unit mapping into Gabet 2003
5. whether Roering nonlinear residual materially improves the 100-year result
6. fire-spall production equation
7. coarse-fragment/armour state reconciliation with SWEHR

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


---

## 3차 범위 수정

최신 범위 결정:
`decisions/2026-09-21_GEOMORPH_SCOPE_CORRECTION.md`

현재 production baseline에서:
- tree throw / uprooting 제외
- shallow landslide 제외

따라서 현재 핵심은:
```
water erosion
+ residual creep
+ root-growth/decay transport
+ dry ravel
+ weathering/regolith production
+ fire spall/coarse fragments
```

이다.


---

## 4차 정리: 현재 production scope

최신 범위에서는:
```
tree throw / uprooting = 제외
shallow landslide      = 제외
```

사면수송은 다음 세 항만 사용한다.

```
q_hill
=
q_bg
+
q_rootgrowth
+
q_dryravel
```

### q_bg
```
q_bg
=
-D*_bg H_active grad(z)
```

### q_rootgrowth
Gabet et al. 2003 exact equation:

```
q_sx
=
-[0.003 r tau / (rho_r log(beta))]
sin(theta) cos(theta)
```

LPJ-GUESS native fine-root state, turnover and root-depth distribution을 사용한다.

### q_dryravel
Lamb lineage.

풍화는:
```
Hartmann/LPJ-GUESS chemical forcing
+ Yoo/Brosens mobile-soil mass balance
+ DynSoil/MErSiM-style regolith front
```
로 정리한다.

Gabet & Mudd 2010 rootwad/tree-throw physical weathering은 archive-only다.
