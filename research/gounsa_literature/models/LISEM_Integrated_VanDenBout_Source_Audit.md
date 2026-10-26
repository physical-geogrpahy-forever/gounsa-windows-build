# LISEM Integrated Spatial Earth Modeller: 독립 C++/OpenCL 계보의 실제 수관 및 유사 침식 소스 감사

작성일 2026-10-26. **주의: 이 저장소는 OpenLISEM Classic 7.5.2 `vjetten/openlisem`와 다른 프로젝트**. Classic 7.5.2 실제 Windows 수치비수렴을 이 프로젝트에 그대로 전가하지도 않고, 이 프로젝트의 홈페이지 소개만으로 전자는 복구됐다고 주장하지도 않는다.

## 공개 출처
- Source: https://github.com/bastianvandenbout/LISEM/tree/6a5ef17d87bab4227d48673c95c12c61462114dd
- LISEM 0.2.x multi-hazard project; same author's overview https://lisemmodel.com/docs/about/ ; author research https://doi.org/10.5281/zenodo.7414954
- Repo API advertises MIT because root LICENSE begins `MIT License Copyright (c) 2017 Can Güney Aksakalli`, while repository also contains `licence.txt` GNU GPL v3 and developer website says GPLv3. **Whole-software licence must NOT be inferred to be MIT from repository metadata alone.** Treat model as distributed under publisher GPL3 until clarified.
- This inspection did not download/run compiled executable and cannot claim computational stability.

## Actual matching program modules read
- `lisem/model/kernels/model_sediment.cl` explicit rain impact (L348–422), flow detachment/deposition (L424–465), four-neighbor sediment flux (L470–519), original code provided.
- `GetSV` in this file L52–65 has the *parentheses corrected* relative to the v7.5.2 Classic default: `10*(sqrt(1+0.01*1.65*g*dm^3)-1)/dm`, distinct from Classic bug `10*sqrt(1+X-1)/dm`. That does NOT prove native convergent sediment balance, and is not reason to rehabilitate Classic.
- `modelruninit.cpp` L432–446 reads `SMAX Canopy` raster into `SMAX_CANOPY`.
- `model_hydrology.cl::hydrology` ~L289 `store_canopy=SCANOPY`, L302 `Smaxc=SMAX_CANOPY`, but L310 `h=h+store_canopy`, L326 `h=h+rain`, L397 `write_imagef(SCANOPYN,...,0)`. The observed `Smaxc` is read but **is not used** to limit/store rainfall in this hydrology kernel; no canopy water-budget LAI driven interception appears in inspected model hydrology kernel.
- `model_evapotranspiration.cl` L169 `//float LAI = ndvi * 4.0;` **commented out**, L192 `write_imagef(SCANOPYN,...,0)` too. NDVI is not native LAI-linked dynamic canopy store.
- `model_sediment.cl` L381–386 `directrain=(1-vegcover)*rain_m`, `throughfall=vegcover*rain_m`, with `KE_LD` from plant height; this partition does not consume actual canopy drainage or dynamic canopy storage, and relies on `vegcover` rather than LAI. Subtracting interception does not appear in this expression itself. **The model being capable of leaf-drip-like splash does not prove actual throughfall from a working water store.**

## Numerical code concern requiring any future source-level requalification
In `model_sediment.cl` ~L507–510 `qfsout = qfsout +z_x1 < -1000? sflux_x1 : 0` etc. Without parentheses a C-style ternary operator's precedence makes this evaluate a comparison with `qfsout+z_x1`, not `qfsout += (z_x1<-1000 ? sflux_x1 : 0)`. This is a **plausible report-flux bug from source reading**, not an experimentally confirmed water/sediment mass residual. Worth isolating only if the missing canopy test were ever resolved.

## What passes vs fails
- Complete readable erosion/hydrology source in unique GitHub codebase: YES.
- Genuine 2D surface water and 2D XY sediment flux functions: source shows 4-neighbor flux and hydro solvers; exact hydrodynamics full finite-volume consistency not revalidated.
- Native quantitative canopy water storage / LAI→throughfall used in erosion flux: **FAIL native code evidence**: stored canopy inputs ignored/reset in reviewed kernels, `throughfall` in sediment is proportional to `vegcover × rain`.
- Steep mountains case original lineage has Dominica landslide/flood studies; native *this version* observed Gounsa forest splash/sediment not verified.
- Stable timestep erosion transport/finite soil stock: **NOT TESTED**.

## 사용자 원칙 적용 최종 판정
**Discard for Gounsa complete native integrated engine** before time-expensive OpenCL build. This is due to missing *active* LAI canopy storage/throughfall/leaf drip link, not due to Classic 7.5.2 benchmark contamination. Scientific hydrodynamics / soil transport components can be cited only with these caveats. Never present as tested stable.

## Sources
https://github.com/bastianvandenbout/LISEM
https://lisemmodel.com/docs/about/
https://doi.org/10.5281/zenodo.7414954
