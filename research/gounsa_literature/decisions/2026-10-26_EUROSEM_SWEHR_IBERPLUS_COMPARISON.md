# 2026-10-26 EUROSEM, SWEHR, Iber+ 세 모형 원본 기능 및 고운사 적용 비교

## 핵심 판정
**고운사 초점: 밀생 억새 vs 떨어져 있는 참나무 맹아의 실제 patch position → canopy interception/direct throughfall/drip/stemflow → per-plant spatial infiltration/runoff → rainfall & flow detachment → deposition/size classes → armoring and soil depth → vegetation feedback.**

1. EUROSEM (Morgan et al. 1998) is the strongest of these three in physically distinguishing canopy rainfall pathways and drip kinetic energy, with Smith–Parlange infiltration, rock ROC/PAVE/ISTONE, event rill/interrill sediment. But 1D connected slope planes and channels, not genuine 2D shallow water; DT+LD+SF reaggregated as NR. Per-stem SF localization + cross-slope flow pathways absent, hence not adequate for the sparse oak-vs-dense tussock spatial sediment comparison as production engine.
2. SWEHR (McGuire et al. 2016) genuine 2D shallow-water, Green–Ampt, Hairsine–Rose original soil and loose sediment, size-specific raindrop and flow detachment, redeposition, slope/topography and debris-flow transition. 2016 article includes Rutter rainfall interception, but **public csdms-contrib/swehr C code used for latest simulations does not implement Rutter/per-stem stemflow out-of-box**. The latter was explicitly implemented in new spatial interface for recent validation. Original wildfire paper applied TLS, 37.5cm mesh, ≈40° hillslopes, and isolated raindrop vs flow detachment.
3. Iber+ (Cea et al. 2024) genuine 2D finite volume shallow-water + rainfall/flow driven original detachment + loose-layer redetachment + size-specific deposition, suspended and bedload, loose mass M_s,k and morphological Exner, GPU. Excellent candidate for production coupling SSSPAM/mARM persistent PSD/soil profile; **not a published full canopy-free TF/drip/SF or dynamic RLD/root erodibility model**.
4. **Primary prior decision retained:** Iber+ as best published event 2D multiclass erosion engine, SWEHR as source-modifiable postfire 2D benchmark/field mechanism exploration, EUROSEM as canopy, rock fragment and raindrop KE component reference. However practical execution readiness should not be mistaken for published scientific suitability: SWEHR tested 38 spatial-source cases; Iber+ not yet executed for comparable cases.
5. Open access Iber+ V3.2b executables for Windows/Linux and original four validation input datasets published https://doi.org/10.57745/UFEK4L. It is not established here that full GPU erosion source code is open or editable. It may need external forcing interface compatibility for separate rain-water and rain-impact terms; can use SWEHR code for coupling prototype then port after confirming Iber+ supported source injection.
6. All three lack **as originally published** a combined spatially explicit oak-rootstock vs M. sinensis rhizome/tussock per-stem SF + throughfall/drip energy + measured root and litter + coarse-fragment physics + dynamic vegetation. Never claim this coupled published model exists.

## Strict native/paper function comparison

| Process | EUROSEM (1998) | SWEHR (2016) | Iber+ (2024) |
|---|---|---|---|
| spatial surface water | 1D slope-plain/channel cascades, dynamic kinematic wave | genuine 2D SWE (finite volume) | genuine 2D SWE (finite volume/GPU) |
| vegetation interception | yes (INTERC) | original paper yes (Rutter); runnable public C not full canopy physics | no independently resolved canopy allocation in 2024 soil erosion paper |
| direct TF | native separate | throughfall coefficient in article; not distinct spatial term in QA C | external forcing required |
| leaf drip | native separate, drip impact KE empirical height | no complete leaf-drip KE demonstrated | no leaf-drip KE demonstrated |
| SF | native volumetric/shape-angle fraction, **recombined to total NR** | no per-stem SF | no per-stem SF |
| infiltration | Smith–Parlange (KINEROS lineage) | Green–Ampt | 2D rain f loss; depends on configured version/method |
| rill/interrill or rainfall/flow detachment | native, both | native, both | native, both |
| original sediment vs loose layer | no complete per-class dynamic original/deposited store state | Hairsine–Rose, yes | per-class dynamic Ms,k yes |
| particle sizes and shielding | limited bulk/transport-capacity emphasis | multiple size class, HR loose layer shielding | multigrain suspended+bedload, dynamic class grading and shielding |
| Exner/geomorphic update | rill/channel evolution in event but not arbitrary 2D raster Exner | 2D soil elevation update | dynamic Exner, 2D |
| field-specific stony rock infiltration/protection | ROC PAVE ISTONE original, **not dynamically weathering/spalling** | requires independent stony input | requires independent stony input |
| root RLD biomass / litter mass | no dynamic species root effects | no dynamic measured root inputs out-of-box | no dynamic measured root inputs out-of-box |
| steep mountainous/postfire | stony steep trials, not genuine 2D | San Gabriel Mountains burned steep approx 40°, measured TLS | vineyard plot; Alps Galabre 20km² run, note Alps original case **rainfall detachment only** |
| code status | 1998 Fortran77 source publicly available; native runs available | public original C source, recompiled locally by GitHub Actions | 2023 academic reproducibility Windows+Linux executables published, code-level customization not independently verified |

## Original published equations essential
EUROSEM:
`NR=DT+LD+SF=R-Icstor` (aggregate total before single-plane infiltration); `KE(LD)=15.8 sqrt(PH) - 5.87` J m^-2 mm^-1; PH metres inside energy formula, PLANTH input centimetres. Original manuscript equation from Morgan et al. (1998) and original manual.
SWEHR:
`e_k = (1-H) p_k a R` schematic rain-detachment (flow-depth damping omitted), plus flow entrainment governed by fraction of stream power F and specific entrainment energy J. Wet-front infiltration Green–Ampt. Original paper has Rutter canopy storage, but C source lacks drop/stem split.
Iber+:
`∂_t h+∂_x q_x+∂_y q_y=r-f` and per-class sediment `∂_t(h C_k)+∇·(q C_k)= detachment_orig+redetach_loose-deposition`; per-class loose layer `M_s,k`, Exner z_b, sediment positivity and wet-dry mass conservation. Explicitly note that r appears in both surface-water and rainfall-driven detachment; **feeding SF as r without separately reducing raindrop erosion is physically inaccurate**.
These are equation sketches, not complete original formulations.

## Prior actual executions and independent validation
- EUROSEM: previous 60 native canopy/erosion param cases, 59/60 native water balance pass, one SPLTEX=1 test fail, **no independently checked original sediment mass budget**. Earlier PLANTH metre/cm mistake was explicitly corrected. Earlier soil-loss values 26–160t/ha cannot be accepted as realistic Gounsa output.
- SWEHR: original C native plus new spatial vegetation forcing and modified initial/boundary QA, **38/38 strict water+original soil/deposited/suspended+boundary layer mass conservation pass**. 13×25 grid, dx 0.5m, synthetic 81.25m² slope, density mask grass 94.77% vs oak 9.23%. P=30mm/h×1h exported sediment 0.000542655 vs 0.002290642t/ha respectively (oak ~4.22x); a modeling response to **arbitrarily hypothetical Ks/roughness/erodibility** and spatial mask, not site prediction. Equal-40%-vegetation layout controls produced 0.001285687 and 0.001459800 t/ha. 10–50 all intensities archived.
- Iber+: 2024 original publication validated laboratory and vineyard data plus Alps and debris-flood, but **no locally reproduced native Iber+ Gounsa-like 10–50 mm/h 38-run setup or independent code-ledger check**. Do not claim numerical comparison among 3 models accomplished.
- Github SWEHR results https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/spatial-vegetation-runoff-erosion-20261026/experiments/rainfall_10_50/spatial_patch_experiments/verified_20261026/summary.csv

## Species-specific project implications and clear division of work
- Drone/TLS actual separate stump coordinates and coppice geometry, tussock polygons/patch gaps, bare microtopographic connectivity, surface spalled fragment footprint, litter/surface biomass, root length density/soil depth.
- External canopy module resolves leaf/stem storage, evaporation, separate `Q_DTF(x,y), Q_drip(x,y), Q_stem,j(t)`, KE of direct throughfall and drips at actual effective drop height.
- **Never feed stemflow into rainfall-impact source simply as extra rainfall.** Inflow water `p_water` and impact energy/raindrop rainfall equivalent `p_impact` must remain independently supplied while conserving water.
- First implement/input/validate on transparent SWEHR source, compare every separate water/solid ledger, 2D runoff connectivity and grid convergence. If Iber+ supports or can be extended with separately controlled water source and droplet erosion forcing, port source and compare fixed DEM, rain and PSD; then use Iber+ production event engine.
- Long-term: Iber+ original soil erosion and Ms,k transfer once only to SSSPAM/mARM depth-dependent rock fragmentation/armour; do not count redetachment as original soil depletion. LPJ-GUESS independently yields roots/leaves/litter PFT/cohort.
- No permanent choice of an unverified engine swap; Iber+ first choice with an explicit practical software accessibility dependency.

## Source documents
Morgan et al. (1998), ESP&L 23, 527–544 https://doi.org/10.1002/(SICI)1096-9837(199806)23:6%3C527::AID-ESP868%3E3.0.CO;2-5
EUROSEM code/manual overview https://wp.lancs.ac.uk/sustainable-soils/eurosem/
McGuire et al. (2016), JGR Earth Surface 121, 2211–2237 https://doi.org/10.1002/2016JF003867
SWEHR public C source https://github.com/csdms-contrib/swehr
Cea et al. (2024), Environmental Modelling & Software 179, 106098 https://doi.org/10.1016/j.envsoft.2024.106098
Iber+ V3.2b original validation executable https://doi.org/10.57745/UFEK4L
