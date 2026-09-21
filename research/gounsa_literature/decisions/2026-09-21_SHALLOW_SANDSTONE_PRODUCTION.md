# 결정: 고운사 shallow-soil sandstone production regime

날짜: 2026-09-21

## 사용자 조건
고운사 parent material은 sandstone이고, mobile soil은 얕다.

따라서 thick-soil shielding regime보다 **thin-soil production regime**가 핵심이다.

---

## 1. 기존 exponential baseline의 한계

기존 baseline:

```
P_sand(h)
=
P0_sand exp(-h/gamma_sand)
```

은 sandstone에서 soil production이 soil thickness와 함께 감소하는 1차 근사로 유용하다.

그러나 Oregon Coast Range sandstone 자료는 very thin soil / exposed bedrock에서 단순한 monotonic exponential 관계가 항상 성립하지 않을 수 있음을 보여준다.

Heimsath et al. 2001 자체는 inverse exponential fit을 제시했지만, 후속 synthesis에서는:
- 약 15-30 cm soil에서 빠른 production
- 약 15 cm보다 얕은 구간에서 production이 다시 낮아질 가능성
- exposed or nearly exposed bedrock가 오히려 덜 weathered/resistant할 수 있음

이 보고되었다.

즉:

```
h -> 0
=> P -> P0 maximum
```

을 고운사에 무조건 적용하지 않는다.

---

## 2. shallow sandstone baseline

고운사의 현재 얕은 토양조건에서는 다음 두 시나리오를 반드시 함께 돌린다.

### Scenario A: monotonic exponential

```
P_A(h)
=
P0 exp(-h/gamma)
```

Evans et al. 2021의 sandstone fits를 이용한 standard sensitivity.

이 시나리오는:
- simple
- long-term sandstone literature와 직접 비교 가능
- h가 얕으면 P가 P0에 가까워짐

### Scenario B: thin-soil hump / suppression

Oregon sandstone evidence를 반영하여:
- very thin soil / exposed bedrock에서 production이 peak보다 낮을 수 있음
- peak는 약 15-30 cm 부근에 존재할 수 있음

따라서 production hard-lock 전까지:
```
P_B(h)
```
는 zero-depth maximum을 강제하지 않는 humped sensitivity function으로 둔다.

정확한 함수형과 계수는 local sandstone/soil-depth evidence 없이 새로 invent하지 않는다.

초기 sensitivity에서는 published thin-soil envelope를 사용해:
- h < about 0.15 m: lower-than-peak production
- h about 0.15-0.30 m: potential peak-production zone
- h > peak depth: exponential-like decline

을 비교한다.

---

## 3. 100-year implication

Because current soil is shallow:

```
P_sand
```

can be near the upper sandstone production envelope.

Therefore century-scale production is **not negligible by default**.

Sandstone analogue rates imply order-of-magnitude:
```
several mm to a few cm / 100 yr
```
depending on:
- soil thickness
- sandstone matrix/cementation
- whether the site lies below, near, or above the thin-soil production peak

This is large enough to compare explicitly with:
- water erosion
- dry ravel
- creep
- fire-spall supply

---

## 4. creep implication of shallow soil

Residual creep baseline:

```
q_bg
=
-D*_bg H_active grad(z)
```

Because `H_active` is shallow:

```
H_active small
=> q_bg small
```

all else equal.

This is desirable because the model cannot transport more mobile soil than exists.

Root-growth/decay transport must also be capped by available mobile-soil mass.

Thus shallow soil strengthens the need for:
- soil-availability caps
- strict mass conservation
- no constant-D transport that ignores soil thickness

---

## 5. production versus erosion feedback

In a shallow-soil system:

```
erosion lowers h
 -> may increase production if on descending thick-soil limb
```

but if erosion pushes the site into an extremely thin / exposed-bedrock regime:

```
further thinning
 -> may not keep increasing production
```

because the Oregon sandstone lineage permits a humped response.

Therefore fire/erosion feedback should not be coded as:

```
less soil always => faster production
```

without testing the humped alternative.

---

## 6. current production rule

Do not hard-lock a single zero-depth `P0` extrapolation.

Production implementation must expose at least two switchable modes:

```
mode = exponential
mode = shallow-hump sensitivity
```

until:
1. actual Gounsa soil-depth distribution
2. exact sandstone petrography/cementation
3. local/regional production constraints

are available.

---

## 7. current priority

Given:
```
sandstone + shallow soil
```

the next weathering priority is no longer deep-regolith mineral-age modeling.

Priority becomes:
1. actual H_AB distribution
2. shallow sandstone production regime
3. P0/gamma or hump constraints
4. fire-spall supply
5. compare 100-year production against erosion/export

DynSoil/MErSiM remains optional.

## 최종 판정
**고운사는 shallow-soil sandstone regime으로 취급한다.**

The monotonic Evans exponential remains one required sensitivity case, but very shallow soil must also be tested against a humped/zero-depth-suppressed production scenario based on the Oregon sandstone literature.


---

## 8. simple 100-year magnitude check

Using the site-specific Evans et al. 2021 `P0,gamma` pairs and the exponential sensitivity mode:

For shallow soils of about:
```
H_AB = 0.05-0.30 m
```

the corresponding 100-year production is approximately:

- Comer: about 7.2-7.6 mm / 100 yr
- Hilton: about 15.7-17.2 mm / 100 yr
- Rufford: about 6.2-6.9 mm / 100 yr
- Woburn: about 18.8-25.7 mm / 100 yr

These are **analogue sensitivity values only**, not Gounsa predictions.

The key implication is:

```
shallow sandstone production
can readily be O(1 cm / 100 yr)
```

and therefore should not be omitted before comparing it against erosion/export.

Oregon sandstone thin-soil evidence further suggests:
- < about 15 cm: rates around 0.15 mm yr^-1 in the reviewed synthesis
- about 15-30 cm: roughly 0.25-0.35 mm yr^-1 in some pits

equivalent to order:
```
15-35 mm / 100 yr
```

under a simple constant-rate comparison.

Because these values come from different sandstone systems and long-term cosmogenic averages, they define a sensitivity envelope rather than an annual transient forecast.
