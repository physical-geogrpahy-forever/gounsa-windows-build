# 2026-10-26 SWEHR 원 논문 수관저류/차폐 및 코드 감사 인계

## 새 확인
McGuire et al. (2016) §3.5 Eq24–26 Rutter 수관 C(t), Tc, D(C), S,Kc,gc, evaporation neglected due to storm scale.
**독립적인** canopy rainfall splash shielding §3.2 Eq3–4 multiplies rainfall detachment and redetachment by `((1−Cv)+TcCv)`, representing rain reaching bed without first contacting canopy. Do not confuse with water storage/loss.
Additional pre-existing code dampening: deposited-sediment shield H (original soil), wet flow depth h0/h_vertical exponential b for rainsplash, depth-dependent Manning friction. Vegetation-dependent Manning n(Cv), litter, RLD NOT explicitly modeled.
Original published Nov/Dec severe burn hydrology neglect canopy interception §3.8; synthetic 20×5m study §4.3 varied Cv0.05–0.95, ks2–11mm/h and used Tc=.35, S2.2mm, Kc5e-5mm/s, gc3.9mm^-1. About ≥5fold smaller splash-only sediment volume over cover range at fixed Ks; flow-only ≤2fold, mixed process sensitive to both.
**Direct source proof:** original CSDMS `SWEHR.c` github.com/csdms-contrib/swehr, L814 R=RAIN[rind]; L1331 H sediment layer shield, L1338/L1343 E1/E2 use R times masks with NO ((1−Cv)+TcCv) factor; L1348–1352 wet-depth damping implemented; L1360 `SF` is friction slope (not stemflow); L1427 U1+=dtR with no Rutter. No Rutter/Cv/Tc/Kc/gc storage function. Only 7 files in original repo, no canopy module.
Published Rutter 1975 original separately predicts throughfall/stemflow and trunk evaporation; 2016 adaptation and public C do not implement per-trunk separate fluxes. Reference Rutter 1972 and Rutter 1975.
Caution prior 38 SWEHR synthetic spatial experiments `QA_WFACTOR` and `QA_DFACTOR` included static interception/plant stemflow hypothetical map, but not Rutter dynamic reservoir or separate original direct high KE shielding; treating retained water as permanently lost under E=0 is not correct after rain stops.
## GitHub saved
- papers/1972_Rutter_CanopyRainfallInterception.md
- papers/1975_Rutter_ThroughfallStemflowInterception.md
- papers/2016_McGuire_SWEHR_Postwildfire_2D.md updated (canonical full study)
- models/SWEHR.md (new)
- decisions/2026-10-26_SWEHR_RUTTER_CANOPY_SHIELDING_SOURCE_AUDIT.md
- MASTER.md, INDEX.md 393 papers / 59 models / 32 decisions updated
## Next scientifically required
1. Code 1975 Rutter reservoirs (or equivalently original 2016 simplified C) separate from no rainfall: canopy C, stem Cstem, 0–60min intense and poststorm dry-down, no evaporation (for reproducing McGuire 2016) versus evaporation enabled scenario if needs long model.
2. Rain water `Pwater=DTF+Drip+SF`, raindrop energy/impact `Pimpact = incident direct fraction + drip effective KE` with **no double application of Cv/Tc shielding** when the throughfall is already split by canopy; spatial nearest trunk and tussock stemflow locations with conservative mass ledger.
3. Litter/root, Ks, Manning roughness, coarse fragments distinct from Cv. Root quantity cannot be inferred from projected cover.
4. 10,20,30,40,50 mm/h 1h rain and recession coupled canopy/surface water and soil sediments independently closed. No new tests performed in this source audit.
## Source evidence
- Full paper https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016JF003867
- original code https://github.com/csdms-contrib/swehr/blob/master/SWEHR.c
- 1975 original https://www.britishecologicalsociety.org/applied-ecology-resources/document/19751918683/
