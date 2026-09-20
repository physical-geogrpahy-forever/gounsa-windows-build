# 결정: 고운사 residual background creep

날짜: 2026-09-21

## 질문
root-growth transport, tree throw, dry ravel, landslide를 명시적으로 계산한 뒤 background creep를 어떻게 처리할 것인가?

## 결정

```
D_bg = 0
```
은 기본안으로 채택하지 않는다.

또한 자연산림에서 보정된 total diffusivity를 그대로 사용하지 않는다.

Baseline:

```
q_bg
=
-D*_bg H_active grad(z)
```

where:
- `D*_bg` is a residual local-creep coefficient [L T^-1]
- `H_active` is active mobile-soil thickness
- `q_bg` is volumetric flux per contour width

## 근거

### Furbish et al. 2009
Soil flux is consistent with a depth-slope functional form.

The diffusion-like coefficient includes active-soil thickness and particle-activation properties.

### Furbish & Haff 2010
Local slow bulk creep and long-distance intermittent surface motions should be distinguished.

### Doane et al. 2021
Tree throw explains only about 11-18% of total volumetric hillslope flux at the studied temperate forest.

### Sonoda & Kurashige 2017
Six-year weathered-granite forest monitoring in Japan directly observed wet-dry residual strain accumulating into net creep.

### Richards et al. 2011
Faunal bioturbation contributes measurable downslope flux not represented by LPJ-GUESS.

### Deshpande et al. 2021
Granular creep can persist even without imposed disturbances.

## process partition

```
q_hill
=
q_bg
+
q_rootgrowth
+
q_dryravel
```

Tree throw/uprooting and shallow landslide are outside the current production baseline.

`q_bg` contains only unresolved/local processes such as:
- wetting-drying
- weak freeze-thaw
- fauna
- micro-scale granular rearrangement
- unresolved shallow bioturbation

## parameter rule

Richardson 2019 total `D` compilation is **not** the direct source of `D*_bg`.

It can only provide:
- broad plausibility bounds
- upper-envelope sanity check

Preferred:
1. local calibration
2. process-budget residual
3. sensitivity range if data unavailable

## freeze-thaw
If Gounsa freeze-thaw proves important, promote Anderson 2002 frost creep into an explicit module rather than inflating `D*_bg`.

## postfire
No arbitrary fire multiplier for `D*_bg`.

Fire effects are already represented by:
- changing `H_active`
- dry ravel
- root dynamics

Additional time variation in `D*_bg` requires separate evidence.

## numerical timestep
Evaluate on annual geomorphic state, with internal substeps if stability requires.

## final
**Residual depth-dependent creep is retained.**

This replaces the previous provisional:
```
q_bg = -D_bg S
```
with a soil-thickness-aware form and avoids both:
- zeroing legitimate creep
- double counting total natural diffusivity.
