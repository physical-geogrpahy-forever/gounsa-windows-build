# 결정: SWEHR 원논문의 수관차단 및 강우충격 저감의 공개 코드 누락 확인

## 결정 요약
원논문에 **(A) Rutter canopy storage/throughfall/drainage and (B) canopy mechanical shielding of raindrop detachment**가 **따로 존재**한다. 논문만 보고 현재 재현된 공개 `SWEHR.c`에 이미 두 과정이 있다고 주장하지 않는다. 본 연구에서 SWEHR 우선 활용 시 두 과정 모두 분리해서 새로 구현해야 하며, 원래 source Hairsine-Rose E[1], E[2]와 water source U[1]가 동일한 R을 사용하는 것을 구분해야 한다.

## 원논문 직접 검증
- McGuire et al. (2016), §3.5 Eq24–26: Rutter et al. 1972,1975 기반 시간별 canopy stored depth C, direct throughfall Tc, drainage D based Kc/gc/S. Short storm scale E ignored. Ground net rain corrected using canopy reservoir.
- §3.2 Eq3–4: separate rainfall-impact shield **f_s=(1-Cv)+Tc Cv**. Physical meaning = original raindrops reaching ground without contact canopy. Not the same as soil-reached rain volume after dripping.
- §3.2 Eq5–7: flow-depth-based reduction in effective rainsplash detachment, and deposit shielding by prior detached sediment. **Neither is vegetation litter/root attenuation**.
- §3.3 and Discussion §5: vegetation effect on Manning roughness noted but not implemented as dynamic Cv–n in original paper.
- §3.8 says severe burn removes vegetation so interception NOT used in modelled November and December storms.
- §4.3: synthetic 20×5m, 25° hill, two rain tests. `Cv` 0.05–0.95, Ks2–11mm/h, Rutter Tc0.35, S2.2mm, Kc=5e-5mm/s and gc3.9mm^-1. At constant Ks raindrop-only sediment ~5x decrease across cover, flow-only less than ~2x; mixed processes similarly sensitive to Cv and Ks. **These are synthetic recovery model results, not site vegetation species observation or original released C confirmation.**
- Rutter et al. 1975 original model elaborated to calculate stemflow and throughfall separately; 2016 SWEHR paper's simplified C,D,Tc does **not** demonstrate a separate per-tree SF spatial supply implementation.

## Native C source facts
`https://github.com/csdms-contrib/swehr/blob/master/SWEHR.c`
- no `Cv`, `Tc`, `Rutter`, canopy `C`, trunk storage `S_t`, canopy D, Kc and gc source keywords or functions.
- L814 `R=RAIN[rind]`.
- L1331–1333 `H=min(1,TOTM/mtstar)`: existing loose deposited sediment shielding, not vegetation.
- L1338 and L1343 `E[1]`/`E[2]` rainfall detachment `...×R` but without `f_s`.
- L1348–1352 `pow(h0/h_vertical,b)` wet-depth rainfall impact attenuation IS implemented.
- L1356–1360 variable `SF` stores Manning friction slope, not stemflow. Roughness depth-dependent but not computed from biomass/vegetation cover.
- L1427 `U[1]+=dt*R`, the same original R for water supply; no Rutter canopy loss applied.
- L1450 Green–Ampt Ks infiltration built in, default example `KS=0`.
- Previous source-modified spatial interface `QA_WFACTOR`/`QA_DFACTOR` separate ground supply vs rainsplash, still no dynamic Rutter storage/drainage nor leaf-drip impact energy; canopy storage fixed .8mm maximum hypothetical, not Rutter.

## Implementation tests that must be passed
1. Canopy micro-module stand-alone pulse (10, 20,30,40,50mm/h) and ceased-rain drainage: gross P − evap − surface-input = change in C and stem storage, integrated over time. No deletion of temporary canopy water under E=0.
2. Identical ground water supply with varying high-energy direct-throughfall/drop energy to isolate **mechanical shielding** from runoff; no double multiplication `f_s` if already applying direct high-energy rain fraction.
3. Same rain-impact input with changing water source to isolate **Rutter interception hydrology** from splash; ensure flux and sediment budget.
4. Spatial stemflow to tussock/stump; leaf drip KE separate; avoid using `SF` friction slope as variable name for stemflow to prevent confusion.
5. Real Gounsa root/litter and rock fragmentation not replaced by Cv; use measured spatial Ksat and a/ad/J.
6. Downstream 2D native mass ledger and mesh sensitivity run before claiming simulated site differences.

## Why this matters
Earlier dense grass 94.77% vs sparse oak 9.23% local hydrology simulation has *some hypothetical canopy storage / drip budget accounting* but not original Rutter and original canopy impact shielding. Its 4.2× site-like difference is not the full vegetation shielding response of the McGuire 2016 model. Do not infer 'SWEHR has no separate vegetation shielding in the paper' or 'current source includes fully implemented Rutter'.

## Source grade
[A] original paper full HTML §3.2, §3.5, §4.3 and discussion: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016JF003867
[A] original GitHub source single C: https://github.com/csdms-contrib/swehr/blob/master/SWEHR.c
[A abstract] Rutter 1975: https://www.britishecologicalsociety.org/applied-ecology-resources/document/19751918683/
[A abstract] Rutter 1972: https://www.sciencedirect.com/science/article/pii/0002157171900343
