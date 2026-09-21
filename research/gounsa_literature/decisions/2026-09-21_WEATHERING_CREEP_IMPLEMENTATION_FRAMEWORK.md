# 결정: 고운사 풍화 및 사면 creep 구현 프레임워크

날짜: 2026-09-21

## 질문
Pelletier 2013을 수정해서 100년 고운사 모델을 구현할 것인가, 아니면 더 짧은 시간간격에 적합한 modular numerical framework를 사용할 것인가?

## 결정
**Landlab을 풍화/creep 수치 구현 scaffold로 우선 채택한다.**

Pelletier 2013은 장기 구조 비교용으로만 유지한다.

---

## 1. 이유

Landlab은:
- open-source Python
- MIT license
- 2D gridded landscape framework
- modular process components
- custom component 추가 가능
- short numerical timestep / internal substepping 가능

현재 고운사에 필요한 두 과정이 이미 독립 component 형태로 존재한다.

### soil production
```
ExponentialWeatherer
```

기본식:
```
P
=
P0 exp(-H/Hd)
```

### depth-dependent creep
```
DepthDependentDiffuser
```

```
q_bg
=
-K H_* (1-exp(-H/H_*)) grad(z)
```

For shallow soil:
```
H << H_*
```

```
q_bg
approx
-K H grad(z)
```

This matches the selected shallow-soil residual-creep concept.

---

## 2. important Gounsa modification

Do not use Landlab default production law as the only weathering law.

Gounsa is:
```
sandstone + shallow soil
```

Therefore implementation must support:

### mode A
```
P_A(h)
=
P0 exp(-h/gamma)
```

### mode B
shallow-soil humped / zero-depth-suppressed production sensitivity.

The second mode must be a custom component or custom production function.

Do not invent final hump parameters before local/regional evidence.

---

## 3. hillslope transport

Production baseline:

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
Landlab DepthDependentDiffuser.

### q_rootgrowth
Gabet et al. 2003 explicit root-growth/decay flux from LPJ-GUESS native root state.

Do not put vegetation into `K` again.

### q_dryravel
separate postfire process.

Tree throw/uprooting and shallow landslide remain outside current scope.

---

## 4. steep slope option

If linear slope dependence proves insufficient:

```
DepthDependentTaylorDiffuser
```

can be tested.

It supports:
- depth dependence
- nonlinear slope response
- critical slope
- dynamic timestepping

But it is sensitivity-only because strong nonlinear near-critical transport may overlap with dry-ravel/nonlocal steep-slope processes.

---

## 5. numerical timestep

Outer geomorphic clock can remain annual.

Internally:
```
annual process state
 -> stable substeps
 -> annual mass-conserved state
```

This avoids treating 1 year as the explicit numerical timestep when stability requires shorter dt.

---

## 6. mobile-soil mass conservation

Required shared state:
```
soil__depth
bedrock__elevation
topographic__elevation
```

All flux components must satisfy:
```
exported mobile soil
<=
available mobile soil
```

No negative soil depth.

Chemical dissolved loss must be added separately to mobile-soil mass balance.

---

## 7. software status

Landlab is:
- public source repository
- actively available as Python package
- MIT licensed
- designed for component-level modification and coupling

Thus it is much more practical for Gounsa than modifying a bundled geologic-timescale Pelletier model.

---

## final
**Implementation framework: Landlab.**

Process equations:
- sandstone production: Gounsa custom mode A/B
- residual creep: DepthDependentDiffuser
- root growth: Gabet 2003 separate flux
- dry ravel: separate
- chemical dissolved weathering: LPJ-GUESS/Hartmann separate mass-loss term

Pelletier remains comparison only.
