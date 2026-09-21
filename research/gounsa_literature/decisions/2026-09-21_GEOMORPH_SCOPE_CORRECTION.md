# 결정: 고운사 100년 기본 지형과정 범위 축소

날짜: 2026-09-21

## 사용자 범위 확인

현재 고운사 100년 기본모델에서는 다음을 **기본 구현범위에서 제외**한다.

```
tree throw / uprooting
shallow landslide
```

이 둘은 문헌 아카이브에는 보존하되 production core에는 넣지 않는다.

필요성이 이후 현장자료나 민감도 분석으로 확인될 때만 optional module로 재검토한다.

## 현재 기본 지형과정

```
1. water erosion
2. hillslope diffusion / creep
3. root-growth/decay biogenic transport
4. postfire dry ravel
5. soil/regolith weathering and production
6. fire spall / coarse-fragment supply
```

## 사면수송 기본식

```
q_hill
=
q_bg
+
q_rootgrowth
+
q_dryravel
```

Baseline background creep:

```
q_bg
=
-K_bg H_* [1-exp(-H_active/H_*)] grad(z)
```

Landlab `DepthDependentDiffuser`를 사용한다.

얕은 토양에서는:

```
q_bg
approx
-K_bg H_active grad(z)
```

Root-growth/decay transport:
- Gabet et al. 2003
- LPJ-GUESS native root state/turnover

Postfire dry ravel:
- Lamb lineage
- Roering & Gerber / Jackson & Roering supporting evidence

## 풍화 기본구조

Tree throw/rootwad physical production을 production core에서 제외한다.

따라서:

```
P_total
=
P_chem_front
+
P_root_mech_if_supported
+
P_other_phys_if_supported
```

현재 1차 구현은:
- Hartmann/LPJ-GUESS chemical-weathering forcing
- DynSoil/MErSiM or Braun-type chemical front production candidate
- mobile-soil mass balance after Yoo/Brosens

Gabet & Mudd 2010 rootwad/tree-throw architecture는 참고문헌으로 유지하되 기본 production term으로 사용하지 않는다.

## shallow landslide

현재는 제외.

따라서:
- root cohesion for landslide
- factor of safety
- failure probability
- landslide event routing

을 현재 구현 우선순위에서 제거한다.

## 이유

연구 목표는 100년 산불 후 식생-지형 피드백이며, 현재 현장/자료 조건에서 uprooting과 shallow landslide를 넣으면:
- 파라미터 수가 크게 늘고
- 불확실성이 커지며
- 핵심 과정인 유수침식, creep, root turnover, dry ravel, weathering 해석을 흐릴 수 있다.

## 최종 판정

```
tree throw / uprooting = archive only, production baseline excluded
shallow landslide      = archive only, production baseline excluded
```

이 결정은 이후 MASTER와 short-timescale architecture의 현재 상태를 덮어쓴다.


## implementation scaffold

Weathering/creep production implementation is now anchored to Landlab:

```
Landlab
 + custom shallow-sandstone production Mode A/B
 + DepthDependentDiffuser
 + separate Gabet root-growth flux
 + separate dry-ravel flux
```

Tree throw/uprooting and shallow landslide remain archive-only and must not be reintroduced by later model-lineage files unless the scope decision is explicitly reopened.
