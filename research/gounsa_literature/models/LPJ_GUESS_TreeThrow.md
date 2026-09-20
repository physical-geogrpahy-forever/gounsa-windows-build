# LPJ-GUESS -> tree throw / root-plate geomorphic interface

## 목적
LPJ-GUESS woody cohort states를 100년 고운사에서 실제 tree-throw events, pit-mound topography, sediment displacement and physical bedrock disturbance로 연결한다.

핵심 원칙:

```
tree mortality
!= tree throw

tree fall
!= uprooting

stem breakage
!= root-plate excavation
```

따라서 event chain을 분리한다.

---

# 1. two event pathways

## A. live/surviving trees: wind-driven overturning

Primary candidate:
```
ForestGALES / fgr
```

Inputs from LPJ-GUESS:
- DBH
- height
- woody cohort density
- species/PFT
- stand spacing/competition proxy
- rooting/soil state where compatible

External:
- local wind climate
- event wind/gust forcing
- topographic exposure

Output:
- critical wind speed for overturning
- critical wind speed for stem breakage
- event/annual risk

Only overturning creates a root-plate geomorphic event.

## B. fire-killed standing dead trees: delayed collapse

Primary lineage:
Gallaway et al. 2009.

```
F_T
=
1 - exp(-F dt)
```

This represents delayed toppling of standing dead trees.

Use:
```
fire mortality
 -> dead-standing cohort
 -> delayed toppling
 -> uprooting vs breakage
```

The Gallaway numerical `F` values are site-specific and not directly adopted.

Postfire `F` should ultimately depend on:
- dead-root mechanical integrity
- stem deterioration
- wind/snow disturbance if available

Any such dependence is a new coupling.

---

# 2. event count from cohort state

For a cell with cohort abundance `N` and annual/event uprooting probability `p`, a stochastic implementation may sample event count from an appropriate binomial/Poisson formulation.

This is implementation bookkeeping, not a claimed feature of LPJ-GUESS or ForestGALES.

If LPJ-GUESS cohort density represents fractional expected trees rather than explicit individuals, event sampling must preserve the correct cell-area expectation.

---

# 3. root-plate geometry hierarchy

## first priority: Korean calibration
Kim et al. 2014, Taehwa Experimental Forest:
- Larix kaempferi
- Pinus koraiensis
- actual typhoon-uprooted trees
- Korean granite forest
- root plate approximately oval/circular in plan
- half-ellipsoid in side view
- DBH more strongly related to root-plate properties than tree height

This is the preferred local geometry constraint.

Exact plotted regression coefficients must be transcribed from the original figures before coding if used.

## fallback: Gallaway 2009

```
V_RP
=
-5.74e-4 DBH
+
5.82e-3 DBH^2
```

with:
- `V_RP` [m3]
- DBH [cm]

Use only as:
- fallback allometry
- sensitivity prior
- cross-check

not a universal Korean coefficient.

Root-plate dimensions can also be estimated from Gallaway's DBH geometry relations.

---

# 4. sediment displacement

Greenwood et al. 2021 / Gabet lineage provides:

```
X_d
=
(W/2)(cos theta + sin theta)
+
(D/2)(sin theta - cos theta)
```

where:
- `W`: root-plate width
- `D`: root-plate depth
- `theta`: slope angle

This converts root-plate geometry and slope into event travel distance.

The local fraction of fine sediment contained in a root plate is site-specific.

Do not adopt Greenwood's 25% fine-sediment fraction without Gounsa evidence.

---

# 5. delayed root-plate release

Gallaway 2009 shows that root-plate sediment release is not necessarily instantaneous.

Root-plate volume remaining declines through time.

This matters because:
```
tree throw
 -> pit created immediately
 -> mound/root plate persists
 -> sediment gradually released
```

For Gounsa this interacts with:
- litter/CWD
- surface roughness
- SWEHR
- dry ravel

A persistent pit-mound/root-plate state is preferable to converting the whole event instantly into mobile sediment.

---

# 6. pit-mound topography

Doane 2021 provides the annual stochastic spatial roughness framework.

Each uprooting event should update:
- pit excavation
- mound deposition
- local DEM
- local soil thickness
- root-plate/mound storage state

Tree throw remains a discrete event process, not a diffusivity multiplier.

---

# 7. physical bedrock disturbance

Gabet & Mudd 2010 provides the architecture:

```
rootwad/pit geometry
 -> intersects soil-bedrock boundary
 -> bedrock volume disturbed
```

Important:
this is a geometric model, not a root-force versus rock-strength fracture model.

Therefore define an explicit:

```
f_fracture
```

or equivalent uncertainty/calibration factor if not all intersected C/Cr material is assumed to become detached regolith.

Do not claim mechanistic rock fracture without a separate mechanical model.

---

# 8. Korean susceptibility constraints

Park 2026 shows that in Korean Pinus densiflora for. erecta systems:
- slope
- DBH
- edge distance/exposure
- aspect
- surrounding vegetation structure

jointly control uprooting susceptibility.

Therefore:
```
p_uproot != f(DBH only)
```

This supports using mechanistic exposure/stand structure in ForestGALES rather than a DBH-only probability.

---

# 9. current complete chain

```
LPJ-GUESS woody cohorts
 DBH / height / density / mortality
             |
             +---------------------------+
             |                           |
             v                           v
       live-tree path              fire-killed path
       ForestGALES                 Gallaway delay
       wind CWS/risk               snag toppling
             |                           |
             +------------+--------------+
                          |
                          v
                 uprooting event?
                   /          \
                yes            no
                 |         stem break / CWD
                 v
          root-plate geometry
          Kim 2014 preferred
          Gallaway fallback
                 |
                 v
          pit-mound geometry
                 |
          +------+------+
          |             |
          v             v
   sediment travel   bedrock/C-Cr
   Greenwood         intersection
                     Gabet-Mudd
          |             |
          +------+------+
                 |
                 v
          DEM / soil-state update
```

---

# 10. what is now resolved

Resolved structurally:
- live-tree event probability model candidate
- postfire dead-tree delayed-toppling lineage
- DBH -> root-plate geometry lineage
- Korean root-plate calibration source
- event travel-distance equation
- pit/mound spatial architecture
- bedrock-intersection physical-weathering architecture

Still unresolved:
1. Korean species anchorage parameters for ForestGALES
2. exact Taehwa DBH-root-plate regression coefficients from figures
3. postfire dead-tree toppling-rate calibration
4. root-plate fine/coarse sediment fraction in Gounsa
5. bedrock fracture efficiency under rootwad intersection
6. availability/quality of local wind forcing
7. whether snow loading needs an explicit event pathway

## current judgment
The previous broad gap:
```
LPJ-GUESS woody cohort -> tree throw
```
is now mostly a **parameter calibration problem**, not a missing process architecture.
