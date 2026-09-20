# 결정: 고운사 과정별 모듈을 분리한다

날짜: 2026-09-21

## 원칙
식생효과를 단일 vegetation coefficient로 합치지 않는다.

## 현재 production baseline

포함:
```
water erosion
hillslope residual creep
root-growth/decay transport
postfire dry ravel
soil/regolith weathering and production
fire spall / coarse-fragment supply
```

제외:
```
tree throw / uprooting
shallow landslide
```

제외 항목의 문헌은 archive-only로 유지한다.

## 유수침식
```
LPJ-GUESS
 -> root/litter states
 -> erosion-resistance interface
 -> 2D rainfall/runoff erosion engine
```

Rainfall-driven과 flow-driven 침식을 분리한다.

## hillslope transport

```
q_hill
=
q_bg
+
q_rootgrowth
+
q_dryravel
```

### residual background creep
```
q_bg
=
-D*_bg H_active grad(z)
```

Furbish 2009 계보를 baseline으로 한다.

### root-growth/decay transport
Gabet et al. 2003:

```
q_sx
=
-[0.003 r tau / (rho_r log(beta))]
sin(theta) cos(theta)
```

LPJ-GUESS native root state/turnover를 사용한다.

### postfire dry ravel
Lamb 계열을 별도 disturbance pathway로 유지한다.

## weathering/regolith

다음 두 과정을 구분한다.

```
chemical dissolved mass loss
!=
bedrock-to-regolith front advance
```

### mobile A/B soil
Yoo 2007 / Brosens 2020 mass balance.

### C/Cr regolith
DynSoil/MErSiM-style transient state를 우선 후보로 둔다.

Hartmann/LPJ-GUESS-CNP는 daily chemical-weathering forcing 역할이다.

## fire spall
Spall fragment production은 dry ravel과 다른 source process이다.

현재 별도의 quantitative production equation이 필요한 unresolved gap이다.

## coarse fragments
- prefire fragments
- fines removal로 노출된 fragments
- fire-spall fragments

을 구분하며:
- mobile loose supply
- armour effect

도 분리한다.

## excluded modules
tree throw/uprooting과 shallow landslide는 현재 구현하지 않는다.

향후 현장자료나 민감도 분석에서 필요성이 명확해질 때만 optional module로 재검토한다.

## 최종 판정
현재 고운사 production architecture는:

```
LPJ-GUESS
 + SWEHR
 + Furbish residual creep
 + Gabet root-growth transport
 + Lamb dry ravel
 + Hartmann/DynSoil-style weathering-regolith balance
 + fire-spall/coarse-fragment module
```

이다.
