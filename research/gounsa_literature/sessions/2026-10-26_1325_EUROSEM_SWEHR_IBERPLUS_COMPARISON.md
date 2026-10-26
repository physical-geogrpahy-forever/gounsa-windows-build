# 2026-10-26 EUROSEM, SWEHR, Iber+ source-based comparison handoff

## Verified original research
- Morgan et al. (1998), EUROSEM ESP&L, DOI 10.1002/(SICI)1096-9837(199806)23:6<527::AID-ESP868>3.0.CO;2-5: canopy direct throughfall, leaf drip, stemflow and drip kinetic energy + connected plane/channel erosion. Original runoff input NR=DT+LD+SF averages away stem concentration. Original Fortran 77 downloadable at Lancaster Sustainable Soils EUROSEM web site.
- McGuire et al. (2016), DOI 10.1002/2016JF003867, 2D finite-volume postfire hydrodynamics, Green–Ampt, Rutter canopy in published paper, HR original/deposited multiclass sediment and TLS validation on California 40° steep fire scar. Public SWEHR C source `csdms-contrib/swehr` used for 38 native spatial 2D cases has NO direct distributed Rutter and per-stem SF physical model without new interface.
- Cea et al. (2024), DOI 10.1016/j.envsoft.2024.106098, original Iber+ GPU 2D finite-volume SWE, multiclass bedload+suspended, rainfall/flow detachment, deposition, loose layer shielding and Exner. 20 km² Galabre Alps **only rainfall detachment, not combined** in that published basin experiment. 60×2.2m hillslope/vineyard and lab/river test coverage. Public 2023 Iber+ V3.2b reproducibility Windows/Linux executables DOI 10.57745/UFEK4L; editable complete source not yet independently confirmed.
- EUROSEM complete canopy source has limitation for localized SF infiltration; Iber+ rainfall impact and water source must be separated so SF is not counted as raindrop. No original triple model combines full site-needed stem+drip root and armour.
- Previous EUROSEM 59/60 native water QA, independent sediment QA NOT passed/tested. SWEHR 38/38 native water+independent sediment ledger QA passed in **synthetic** 13×25-cell spatial forcing setup, 10-50 mm/h, soil parameters imaginary, no real site model. Iber+ never run site-matched current tests. No physically fair 3-model numerical t/ha comparison available.
- Canonical 2026-09-22 Iber+ event engine + SSSPAM/mARM long-term armour/profile stays current. SWEHR transparent C research testbed, EUROSEM canopy and stoniness process benchmark. Do not double-run different sediment models and add same soil loss; no false scalar cover=roots.

## Newly saved
- decisions/2026-10-26_EUROSEM_SWEHR_IBERPLUS_COMPARISON.md
- INDEX.md and MASTER.md updated

## Next work
1. Check Iber+ V3.2b executive input schemas and supported rainfall maps / separate drop impact parameter controls in original test cases; confirm erosion module is correct version.
2. Use identical synthetic dense grass/sparse oak maps, 10-50 mm/h, matched runoff and rainfall split; run Iber+ and SWEHR independently with independent water and class sediment QA and error rates.
3. Per-plant spatial canopy from direct observations, root / litter mass with calibrated published relationships; distinguish surface armour and embedded coarse fragments and site hydraulic functions.
4. Actual Gounsa drone/TLS and georeferenced vegetation data needed for site-level prediction and mesh convergence.
