# Residual background creep model lineage

## 목적
고운사에서 다음을 이미 별도 계산한 뒤에도 남는 continuous/local hillslope transport를 정의한다.

- root growth/decay transport
- postfire dry ravel
- SWEHR water erosion

현재 production baseline에서 tree throw/uprooting과 shallow landslide는 제외되어 있다. 따라서 residual calibration에서도 이 둘을 현재 explicit flux로 빼지 않는다.

질문:
```
남은 q_bg를 0으로 둘 것인가?
상수 diffusivity로 둘 것인가?
active-soil depth를 포함한 process-aware law를 쓸 것인가?
```

## 핵심 결론

```
q_bg != 0
```
을 baseline으로 한다.

그러나:
```
q_bg != natural-landscape total diffusivity
```
이다.

Preferred baseline:

```
q_bg
=
-D*_bg H_active grad(z)
```

with optional geometric correction from Furbish et al. 2009.

- `D*_bg`: residual local-creep coefficient [L T^-1]
- `H_active`: active mobile-soil thickness [L]
- `q_bg`: volumetric flux per contour width [L2 T^-1]

## 1. why H_active is required

Furbish et al. 2009 derives a statistical/kinematic transport structure in which vertically integrated soil flux is proportional to the product:

```
active soil thickness
x
surface slope
```

The diffusion-like coefficient is not a primitive constant but contains:
- active thickness
- particle size
- excess porosity
- particle-activation frequency

For Gounsa this matters because fire/erosion can strongly reduce A/B mobile-soil thickness.

The depth-dependent form guarantees:
```
H_active -> 0
=> q_bg -> 0
```

This is preferable to a constant total `D` that continues transporting soil even when little mobile soil remains.

## 2. why q_bg is not zero

### Doane et al. 2021
On temperate forested hillslopes in southern Indiana:
- tree throw contributed only about 11-18% of total volumetric hillslope flux
- remaining flux was attributed to creep-like processes

The creep-like class includes:
- freeze-thaw
- wetting-drying
- smaller bioturbation

Thus explicit tree throw alone does not close the transport budget.

### Sonoda & Kurashige 2017
Six-year monitoring on a weathered-granite forest slope in Japan showed:

```
drying -> downslope deformation
wetting -> partial reverse deformation
incomplete recovery -> residual strain
repetition -> net annual creep
```

This is a strong East Asian forest analogue showing hydrologic deformation can create net creep independent of tree throw.

### Richards et al. 2011
Ant mounding and vertebrate scraping generated measurable downslope flux on a postfire Australian hillslope.

LPJ-GUESS does not calculate all soil-fauna activity.

### Deshpande et al. 2021
Laboratory granular slopes creep even without imposed disturbances, although the rate slows with structural relaxation.

External disturbances can rejuvenate creep.

This supports a nonzero irreducible granular residual in principle.

## 3. local versus nonlocal separation

Furbish & Haff 2010 distinguishes:

### local / bulk
- wetting-drying
- freeze-thaw
- small bioturbation
- slow granular rearrangement

### intermittent / nonlocal
- dry ravel
- soil slips
- tree throw
- long animal excavation moves
- fire-related release

Gounsa follows this separation.

Thus:

```
q_bg
= local residual creep only
```

while:
```
q_treethrow
q_rootgrowth
q_dryravel
landslide
```
remain separate.

## 4. freeze-thaw

Anderson 2002 provides an explicit frost-creep alternative:

```
temperature history
 -> frost-event frequency/depth
 -> depth-dependent displacement
 -> creep flux
```

This should only be activated if Gounsa temperature/soil-freezing analysis shows frost creep is material.

Do not hide a demonstrably strong freeze-thaw process in `D*_bg` if an explicit process module is needed.

## 5. climate/vegetation constraints

Richardson et al. 2019 compiled effective `D` values across global sites.

General range spans roughly:
```
10^-5 to 10^-1 m2 yr^-1
```
across very different settings.

But this `D` is an effective **total** coefficient.

It may already contain:
- roots
- fauna
- tree throw
- freeze-thaw
- wet-dry creep

Therefore it is only:
- a plausibility envelope
- a sensitivity bound

not a direct `D_bg` value.

Do not use:
```
LPJ-GUESS biomass
 -> Richardson total D
```
as the Gounsa residual law.

## 6. calibration strategy

Preferred hierarchy:

### A. direct local calibration if data become available
Fit `D*_bg` to:
- repeat microtopography
- creep markers/strain
- pit-mound smoothing
- tracer displacement

after excluding known discrete events.

### B. process-budget residual
If a total hillslope flux estimate exists:

```
q_bg,obs
=
q_total,obs
-
q_rootgrowth
-
q_dryravel
-
q_other_explicit
```

then fit:

```
D*_bg
=
-q_bg,obs
/
(H_active grad(z))
```

This is conceptually clean but observationally demanding.

### C. sensitivity prior
If no local calibration exists:
- use a broad physically plausible range
- constrain against Richardson global total-D values as an **upper envelope**
- ensure residual + explicit process flux does not exceed plausible total transport

## 7. time stepping

The constitutive flux can be evaluated on the annual geomorphic step:

```
annual H_active
+ annual topography
 -> q_bg
 -> divergence
 -> annual elevation/soil redistribution
```

Do not use a one-year explicit timestep blindly if numerical diffusion stability requires substepping.

If necessary:
- hold annual process parameters fixed
- substep the diffusion solver internally

This is analogous to hourly rainfall forcing with sub-hourly SWEHR integration.

## 8. postfire behavior

Do not impose an arbitrary postfire multiplier on `D*_bg`.

Postfire changes enter naturally through:
- `H_active`
- separate dry-ravel term
- separate root-growth term
- separate tree throw
- separate landslide

Wetting-drying or freeze-thaw residual coefficients should become time-dependent only if a published/local calibration supports that relationship.

## 9. steep slopes

Furbish 2009 local creep is strongest as a model for local/small-displacement transport.

On steep slopes, long-distance motions become increasingly nonlocal.

Therefore:
- keep `q_bg` as the local residual
- let dry ravel and any future explicitly activated nonlocal modules carry long-distance motion
- use Roering nonlinear total transport only as a sensitivity comparison, not automatically in addition

## current judgment

**Production baseline:**
```
q_bg = -D*_bg H_active grad(z)
```

**D*_bg is nonzero but residual/calibrated.**

Do not:
- set it equal to total forest diffusivity
- make it a simple biomass multiplier
- add a postfire multiplier without evidence
- use it to hide discrete mass-wasting processes

## 핵심 근거
- Furbish et al. 2009
- Furbish & Haff 2010
- Doane et al. 2021
- Sonoda & Kurashige 2017
- Richards et al. 2011
- Pawlik & Šamonil 2018
- Richardson et al. 2019
- Deshpande et al. 2021
- Anderson 2002


## shallow-soil project constraint

Gounsa currently has shallow mobile soil.

Therefore:
```
q_bg = -D*_bg H_active grad(z)
```
is especially appropriate because transport capacity collapses as `H_active` becomes small.

All annual creep updates must impose:
```
exported mobile-soil volume
<=
available mobile-soil volume
```

The Gabet root-growth/decay flux is an explicit separate term and must not be reabsorbed into calibration of `D*_bg`.

Current production hillslope flux:
```
q_hill
=
q_bg
+
q_rootgrowth
+
q_dryravel
```

Tree throw/uprooting and shallow landslide are outside the current production scope.
