# 결정: 고운사 residual background creep

날짜: 2026-09-21

## 질문
root-growth/decay transport와 postfire dry ravel을 별도 계산한 뒤 background creep를 어떻게 처리할 것인가?

현재 production baseline에서는:
- tree throw / uprooting 제외
- shallow landslide 제외

## 결정

```
D_bg = 0
```
은 기본안으로 채택하지 않는다.

또한 자연산림에서 보정된 total diffusivity를 그대로 사용하지 않는다.

최종 baseline은 Johnstone & Hilley 계열의 soil-depth-limited flux를 Landlab `DepthDependentDiffuser` 형태로 구현한다.

```
q_bg
=
-K_bg H_* [1-exp(-H_active/H_*)] grad(z)
```

where:
- `K_bg`: residual local-creep transport coefficient [L T^-1]
- `H_*`: transport decay depth [L]
- `H_active`: active mobile-soil thickness [L]
- `q_bg`: volumetric sediment flux per contour width [L2 T^-1]

얕은 토양에서:

```
H_active << H_*
```

이면:

```
q_bg
approx
-K_bg H_active grad(z)
```

가 된다.

즉 기존:

```
q_bg = -D*_bg H_active grad(z)
```

은 **shallow-soil approximation**으로만 유지한다.

---

## 근거

### Johnstone & Hilley 2015
soil-mantled hillslope transport가 mobile-soil thickness에 의해 제한되는 depth-dependent 구조를 제공한다.

Landlab의 `DepthDependentDiffuser`가 이 계보를 실용적인 수치 component로 구현한다.

### Furbish et al. 2009
vertically integrated creep flux의 depth-slope dependence를 지지한다.

### Furbish & Haff 2010
local slow bulk creep와 intermittent/nonlocal transport를 분리해야 함을 보인다.

### Sonoda & Kurashige 2017
일본 풍화화강암 산림에서 wetting-drying에 의한 residual deformation이 반복되어 net creep가 되는 현장근거를 제공한다.

### Richards et al. 2011
soil fauna 등의 bioturbation도 LPJ-GUESS가 직접 계산하지 않는 residual flux source가 될 수 있다.

### Deshpande et al. 2021
외부 disturbance가 없어도 granular creep가 지속될 수 있음을 보여준다.

---

## process partition

현재 production hillslope transport:

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
local residual creep only.

포함 가능한 미해상 과정:
- wetting-drying
- weak freeze-thaw
- fauna
- micro-scale granular rearrangement
- unresolved shallow bioturbation

### q_rootgrowth
Gabet et al. 2003.

LPJ-GUESS native root state/turnover를 사용한다.

### q_dryravel
postfire dry-ravel lineage를 별도 사용한다.

### excluded
- tree throw / uprooting
- shallow landslide

---

## parameter rule

Richardson 2019 total `D` compilation은 **직접 `K_bg` source가 아니다.**

그 값은:
- broad plausibility bounds
- upper-envelope sanity check

에만 사용한다.

Preferred calibration hierarchy:
1. local creep/topographic data
2. process-budget residual
3. sensitivity range

---

## postfire

`K_bg`에 arbitrary fire multiplier를 곱하지 않는다.

산불효과는 우선:
- `H_active` 감소
- `q_rootgrowth` 변화
- `q_dryravel` pulse

로 명시적으로 전달한다.

따라서 얕은 토양이 되면:

```
H_active -> 0
```

에 따라:

```
q_bg -> 0
```

이 자동으로 보장된다.

---

## steep slopes

급경사에서 linear slope dependence가 부족한지 확인할 때만:

```
DepthDependentTaylorDiffuser
```

를 sensitivity case로 사용한다.

이 component는:
- depth dependence
- nonlinear slope response
- critical slope
- dynamic internal timestep

을 제공한다.

하지만 dry ravel을 이미 별도로 계산하므로 near-critical transport를 기본값으로 넣으면 중복될 수 있다.

따라서 production baseline은 `DepthDependentDiffuser`다.

---

## numerical timestep

Outer geomorphic state는 annual update로 유지할 수 있다.

다만 Landlab diffusion solver는 stability가 요구하면 shorter internal substeps를 사용한다.

```
annual forcing/state
 -> internally stable diffusion substeps
 -> annual conserved output
```

---

## final

**Production baseline:**

```
q_bg
=
-K_bg H_* [1-exp(-H_active/H_*)] grad(z)
```

**Shallow-soil approximation:**

```
q_bg
approx
-K_bg H_active grad(z)
```

고운사의:
```
sandstone + shallow soil
```
조건에서 soil availability가 creep를 자동 제한한다.

Tree throw/uprooting과 shallow landslide는 현재 production baseline에 포함하지 않는다.
