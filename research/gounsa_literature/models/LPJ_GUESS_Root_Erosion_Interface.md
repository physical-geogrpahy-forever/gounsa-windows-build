# LPJ-GUESS root-state -> water-erosion interface

## 목적

고운사에서 LPJ-GUESS가 자체 계산한 quantitative root state를 SWEHR/Hairsine-Rose erosion resistance에 전달하는 인터페이스를 정의한다.

**Production 원칙:** RLD, root length, layer distribution 등 LPJ-GUESS가 계산해 제공할 수 있는 root quantity는 외부 문헌값으로 재구성하지 않고 LPJ-GUESS 출력을 그대로 사용한다.

이 문서는 다음을 명확히 분리한다.

1. LPJ-GUESS 내부 상태량의 **단위/기하 변환**
2. root trait parameterization
3. 토층별 root distribution
4. erosion-active depth selection
5. RLD -> erosion resistance의 **새로운 coupling**

---

## 1. 출발 상태: fine-root carbon

LPJ-GUESS lineage에서 fine-root C biomass는 ground-area basis의 carbon stock으로 표현된다.

대표 단위:

```
C_root,p [kg C m^-2 ground]
```

Dantas de Paula et al. (2025) LPJ-GUESS-NTD implementation explicitly uses:
```
C_root [kg C m^-2]
```

주의:
고운사 export variable `FineRootC`가 정확히 이 의미/단위를 갖는지는 실제 output definition에서 최종 확인한다.

If the simulation state is read at cohort/patch level, patch weighting must be done once and correctly.
Do not multiply by vegetation cover/FPC again if the exported C stock is already per ground area.

---

## 2. production에서는 LPJ-GUESS 계산값을 우선한다

Dantas de Paula et al. (2025) implements:

```
SRL_C [m root kg C^-1]
```

and fine-root C biomass in LPJ-GUESS.

아래 관계는 LPJ-GUESS 출력 단위를 감사하거나 RLD가 직접 출력되지 않는 경우에만 사용하는 **fallback/accounting relation**이다.

Therefore root length per ground area is:

```
L_A,p
= C_root,p * SRL_C,p
```

Units:

```
(kg C m^-2 ground)
*
(m root kg C^-1)

= m root m^-2 ground
```

This avoids an unnecessary assumed:
```
root carbon -> dry root mass
```
conversion.

### if observational SRL is dry-mass based

Many field studies report:

```
SRL_DM [m root kg dry root^-1]
```

Then a documented root carbon fraction `f_C,root` is required:

```
C_root = f_C,root * M_root,dry
```

so:

```
SRL_C
= SRL_DM / f_C,root
```

Do not assume `f_C,root` without a source.

---

## 3. vertical root fraction from LPJ-GUESS

Current LPJ-GUESS multi-layer hydrology uses:
- 15 soil layers
- default thickness 0.1 m per layer
- PFT-specific root fraction by layer

The standard cumulative root distribution is:

```
RD_cumul(z)
= 1 - beta_root^z
```

For layer i:

```
f_p,i
= RD_cumul(z_bottom,i)
- RD_cumul(z_top,i)
```

with bottom-layer remainder treatment as in LPJ-GUESS.

### implementation rule

Prefer:
```
actual LPJ-GUESS root fraction array
```
over externally reconstructing the Jackson equation.

This prevents:
- depth-unit mistakes
- mismatch with modified soil-layer thickness
- mismatch with the exact PFT setup

---

## 4. exact FineRootC -> layer RLD equation

For PFT p and soil layer i:

```
RLD_p,i
=
C_root,p
* SRL_C,p
* f_p,i
/ Dz_i
```

where:
- `C_root,p`: fine-root C [kg C m^-2 ground]
- `SRL_C,p`: [m root kg C^-1]
- `f_p,i`: fraction of PFT fine roots in layer i [-]
- `Dz_i`: layer thickness [m]

Units:

```
kg C m^-2
* m kg C^-1
/ m

= m root m^-3 soil
```

Gyssels RLD convention uses km root m^-3 soil:

```
RLD_km,p,i
=
RLD_p,i / 1000
```

### multi-PFT cell

If PFT root-C stocks are already expressed per total ground area:

```
RLD_i
=
sum_p RLD_p,i
```

If they are patch/cohort-area states instead, first perform the LPJ-GUESS-consistent patch/gridcell aggregation.

Do not multiply an already area-normalized PFT root stock by FPC again.

---

## 5. Korean forest constraint

Huh et al. (2025), Mt. Taehwa, Korea, directly compared:
- Korean pine
- deciduous oak forest

Fine roots:
```
diameter < 2 mm
```

Main results:
- pine mean fine-root diameter about 0.986 mm
- oak about 0.619 mm
- oak SRL about 3x pine over 0-30 cm
- oak SRL almost 5x pine in 0-10 cm
- total 0-30 cm fine-root biomass similar:
  - pine about 265 g m^-2
  - oak about 269 g m^-2
- but vertical distribution was very different
- oak fine roots strongly concentrated at 0-10 cm
- pine was much more uniform over 0-30 cm

Therefore:

```
same FineRootC
!= same RLD
```

and:

```
same total RLD
!= same surface RLD
```

for conifer and broadleaf PFTs.

This supports the need for PFT-specific root traits, but **고운사 production coupling에서는 이 값을 외부에서 따로 추정하지 않는다. LPJ-GUESS가 계산한 PFT별 root state를 사용한다.**

---

## 6. erosion-active depth

Surface/rill erosion is controlled mainly by roots in near-surface soil.

The current LPJ-GUESS top layer is 0-10 cm, and the Korean Huh et al. study also resolves a distinct 0-10 cm fine-root layer.

Therefore baseline implementation should first compute:

```
RLD_0_10cm
```

from the LPJ top layer.

However:
- concentrated-flow detachment can act over a shallower active depth than 10 cm
- root density varies within 0-10 cm
- rill incision can deepen during an event

Thus the top 10-cm RLD is an **available model-layer state**, not a claim that every root across 10 cm contributes equally.

Recommended sensitivity architecture:

```
baseline:
RLD_eff = RLD_0_10cm

alternative:
RLD_eff = depth-weighted RLD over active erosion depth
```

Do not invent a 0-5 cm split unless supported by field data or a defensible vertical interpolation.

---

## 7. live versus dead roots after fire

The baseline equation above describes root length associated with a quantitative root-C state.

Postfire erosion needs at least:

```
RLD_live
RLD_dead
```

because dead roots can retain mechanical effects for some time after vegetation mortality.

LPJ-GUESS mortality/turnover and the separate dead-root state must therefore be coupled to a decay/persistence model before production hard-lock.

Do not set:
```
fire mortality -> root resistance = 0 immediately
```
unless supported by the selected root-decay literature.

---

## 8. RLD -> SWEHR J coupling

Gyssels et al. (2005):

```
SEP_root
= exp(-b RLD)
```

For the review-average rill relation with RLD in km m^-3:

```
b = 0.0460
```

SWEHR original-soil flow entrainment:

```
E_flow ∝ 1/J
```

Therefore the current Gounsa baseline **new coupling** is:

```
J_eff
=
J_bare / SEP_root

=
J_bare
* exp(b RLD_eff)
```

Important:
- not a published single model
- review-average `b` is an initial prior/sensitivity value
- PFT/local calibration preferred
- do not duplicate the same root protection in both `J` and `UC`

---

## 9. coupling chain

Current baseline:

```
LPJ-GUESS
 FineRootC_p
      |
      +--> SRL_C,p
      |
      +--> root fraction f_p,i
      |
      v
 RLD_p,i
      |
      +--> sum/area aggregation
      |
      v
 RLD_eff, surface
      |
      +--> SEP_root
      |
      v
 JSMASK_eff
      |
      v
 SWEHR flow entrainment
```

---

## 10. what is now resolved

### resolved at functional-form/unit level

```
FineRootC
 -> root length
 -> layer RLD
```

Equation:

```
RLD_p,i
=
C_root,p
* SRL_C,p
* f_p,i
/ Dz_i
```

No arbitrary carbon-to-dry-mass factor is required if `SRL_C` is used.

### still unresolved / calibration required

1. 어떤 LPJ-GUESS root output을 coupling variable로 export할지 확인: RLD가 직접 있으면 그것을 최우선 사용
2. surface erosion에 사용할 erosion-active depth weighting
3. postfire live/dead root persistence와 dead-root mechanical integrity
4. local/calibrated `b` in RLD -> erosion reduction
5. `J_bare` calibration

---

## 11. final current judgment

The previous gap:

```
FineRootC -> RLD
```

should no longer be described as lacking an equation.

It is now:

```
LPJ-GUESS native root-state output을 사용
+ output/interface mapping 확인 필요
+ depth/mechanical weighting unresolved
```

This is a major reduction in the vegetation-coupling uncertainty.

## 핵심 근거

- Dantas de Paula et al. 2025, LPJ-GUESS-NTD SRL implementation
- Zhou et al. 2024, current LPJ-GUESS 15-layer hydrology/root fractions
- Verbruggen et al. 2025, LPJ-GUESS root distribution equation
- Huh et al. 2025, Korean conifer/broadleaf fine-root SRL/depth/turnover
- Gyssels et al. 2005, RLD relative erosion synthesis


---

## 2026-09-21 project correction: no external SRL parameterization

사용자 프로젝트 설계에 따라 PFT별 SRL/RLD는 LPJ-GUESS가 계산한다.

따라서 production workflow는:

```text
LPJ-GUESS native root calculation
 -> export RLD/root-length/layer state
 -> unit and spatial-basis check only
 -> erosion-active root state
 -> SWEHR JSMASK coupling
```

으로 수정한다.

`FineRootC * SRL_C * f / Dz` 식은 LPJ-GUESS output audit 또는 RLD 미출력 시의 진단/호환용 관계로 보존하지만, 외부에서 PFT별 `SRL_C`를 정해 production RLD를 재계산하는 것이 기본안은 아니다.
