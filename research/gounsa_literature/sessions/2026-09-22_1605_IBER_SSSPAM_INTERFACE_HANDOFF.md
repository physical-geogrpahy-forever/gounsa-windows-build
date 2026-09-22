# 2026-09-22 Iber-SSSPAM exact interface handoff

## 사용자 요구
- 고운사에는 매립 석력이 많음.
- 모델은 기존 published model을 가져와야 함.
- arbitrary empirical relation과 output-fit calibration을 피하는 것이 최우선.

## 이번 세션에서 확정된 변경
Primary event erosion engine:
- OpenLISEM -> **Iber+ 2024**로 변경.

이유:
- OpenLISEM current source에서 material-depth evolution disabled
- multiclass controls/UI 일부 inactive/commented
- Iber+는 published active multiclass mass-conservation model

OpenLISEM+SWATRE는 hydrology benchmark/postfire comparison으로 유지.

## Iber+ event state
Original soil:
- g_k
- D_rdd,k
- D_fdd,k

Loose layer:
- M_s,k [kg m^-2]
- f_k
- D_rdrd,k
- D_fdrd,k
- D_dep,k

Persistent original-soil depletion:
```
E_orig,i,k
=
A_i ∫(D_rdd,i,k + D_fdd,i,k) dt
```

Loose-layer redetachment:
```
E_redet,i,k
=
A_i ∫(D_rdrd,i,k + D_fdrd,i,k) dt
```

E_redet must NOT be subtracted from deep profile again.

Event-end persistent surface state:
- M_s,k(end)
- f_k(end)
- z_b(end)

Iber relation:
```
l_d,k = M_s,k / (rho_s phi)
```

## SSSPAM/mARM role
Use:
- depth-resolved embedded PSD
- vertical resupply
- weathering transition
- inter-event profile restructuring

Do not use:
- SSSPAM calibrated fluvial erosion equation
- duplicate event erosion/deposition
- duplicate DEM change

## surface-layer mismatch
Iber+ loose layer has variable thickness.
SSSPAM armour/profile discretisation differs.

Current non-arbitrary policy:
- authoritative surface mass = Iber+ M_s,k
- authoritative deeper profile = SSSPAM/mARM
- exchange only by mass conservation and existing SSSPAM vertical-resupply rule
- no fitted exchange coefficient

## parameter policy
Do not tune to observed soil loss.

Prefer:
1. direct field measurement
2. independent rainfall/flume experiment
3. published physical transformation
4. literature-constrained uncertainty range

Especially:
- Ksat
- porosity
- initial saturation
- soil depth
- suction
- g_k
- initial M_s,k
- M_s,cr
- rainfall detachability
- flow detachability
- critical shear stress

## new literature files
- 2024_Cea_IberPlus_MulticlassErosion.md
- 2022_SanzRamos_IberV3_Manual.md
- 1991_Hairsine_Rose_RainfallDetachmentDeposition.md
- 1992_Hairsine_Rose_SheetFlow.md
- 1992_Hairsine_Rose_RillFlow.md

## decision
- 2026-09-22_IBER_SSSPAM_EVENT_PROFILE_INTERFACE.md

## current architecture
```
LPJ-GUESS
 -> measured/independently constrained soil state
 -> Iber+ 2024 event 2D multiclass erosion
 -> E_orig,k / M_s,k(end) / z_b(end)
 -> SSSPAM/mARM embedded profile + weathering
 -> next-event g_k / soil depth / profile
```

## remaining unresolved points
1. exact independent measurement protocol for Iber M_s,cr at Gounsa
2. independent determination of Iber alpha_d,k, K_d,k, tau_s under root/litter states
3. LPJ FineRootC -> measured detachment resistance without fitted cross-model coefficient
4. SurfaceLitC -> event litter protection
5. fire severity -> fire-spall initial PSD
6. exact event/inter-event software state-file format
