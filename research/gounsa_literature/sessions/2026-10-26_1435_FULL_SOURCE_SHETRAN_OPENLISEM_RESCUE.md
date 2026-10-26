# 2026-10-26 SWEHR 대체 가능한 공개 원본모형 확보 인계

## 핵심 사용자 지시
저자의 미공개 2016 SWEHR 코드를 받을 것이라는 가정을 버리고, **실제 전체 오픈소스에 수관차단, 수관적하, 빗방울 및 유수박리, 공간유사수송이 구현된 다른 원본 모델** 조사. 설명/모형명만 보고 가능 판정 금지. SHETRAN/openLISEM 확인.

## 가장 큰 새 결과: SHETRAN 원본 구현
- official GPL-3 repo https://github.com/nclwater/Shetran (`nclwater/Shetran-public`은 binary only로 다른 곳). GNU/Linux and Windows original Fortran source `src/`, project version 4.7.2.0 and `external/tarballs/` full HDF5/zlib-ng/stdlib sources shipped, plus reproducible sediment and canopy examples.
- `ETmod.f90` lines 450–529: actual canopy `CSTORE(IEL), CSTCAP(N), CK(N), CB(N)` Rutter-style time varying canopy water, drains to `DRAINA(IEL)`, not heuristic canopy cap.
- `SYmod.f90` `SYWAT` lines 4472–4499: canopy sheltering `FCC`, `DRAINA`, direct rain `LRAIN`.
- `SYOVER` lines 3766–3806: real canopy drip-fall height `XDRIP`, drop size `DRDRIP`, drip fraction `FDRIP`, separate rainfall and drip momentum GMR/GMD, independent raindrop detachment and flow shear detachment, suppression by ground close vegetation `FCG` and surface stone `FCROCK`, rain impact buffer `DWAT1/DRDROP`, loose layer `DLSMAX`.
- Original sediment-on Cobres example `examples/Cobres/model/rundata_cob.txt` item 17 -> `input_cob_syd.txt` has `SY24 XDRIP,DRDRIP,FDRIP`, `SY41 FCG`, `SY42 FCROCK`, seven sediment size classes. Original Aire SYD example also exists. **Example presence, not executed**.
- **Caveats:** published Wicks & Bathurst 1996 SHESED simulates sheet without rilling. No original automatic incising rills, measured root RLD->erodibility coupling, individual SF, rock weathering. **`SYmod.f90/BALSED` is empty stub** in inspected 2026 source; independent sediment mass QA not turnkey; code compilation/actual output NOT tested here. Windows original documented VS2026+Intel ifx2026.1, Linux gfortran16.1/CMake, tarball dependencies shipped, no DNS for container git clone. Do not call 'pass'.
- Papers canonical new `papers/1996_Wicks_Bathurst_SHESED.md`, `papers/2000_Ewen_Parkin_OConnell_SHETRAN.md`; lineage `models/SHETRAN.md`.

## Other fully open original: classic openLISEM
- official GPLv3 https://github.com/vjetten/openlisem/tree/main_C
- `hydro/lisInterception.cpp` cell_Interception: real canopy + litter storage and `RainNet`, leaf drainage `LeafDrain`.
- `erosion/lisErosionSplash.cpp`: free direct rainfall `directrain`, canopy `throughfall`, leafdrip KE from actual PlantHeight and direct KE, `(1-StoneFraction)`, `(1-GrassFraction)`, wet-depth buffering, 2D `SSFlood`.
- `erosion/lisSWOF2DSediment.cpp` with 2D SWE FullSWOF sediment detachment, advection, deposition and classes. Same source fully public.
- Previous Linux Qt6/QWT repository failure **unresolved**, source/exe v7.5.2 full version identity **not verified**. Source availability is not runtime success. `models/OpenLISEM.md` updated.

## Other candidates filtered
- `pnnl/DHSVM-PNNL` public canopy `InterceptionStorage.c`, official `DHSVM/sourcecode/` has no sediment/erosion source despite Doten 2006 separate published erosion code. Exclude as verified combined erosion source.
- `TanZiTT/GEOtopSed` repo includes original GEOtop water/vegetation C and Libraries but no identifiable sediment module; 2016 GEOtopSed paper reports separate SourceForge erosion code. No full source-aligned proof for this GitHub archive. Exclude for now.
- `storm-fsv-cvut/smoderp2d` full GPL Python runoff source, but explicit canopy-drip KE plus sediment source terms not source-confirmed. Not accepted strict original.
- earlier `nclwater/Shetran-public` binary-only historical repo is separate from now full `nclwater/Shetran`, do not confuse.

## GitHub saved
`research/gounsa_literature/models/SHETRAN.md`
`research/gounsa_literature/models/OpenLISEM.md` updated
`research/gounsa_literature/papers/1996_Wicks_Bathurst_SHESED.md`
`research/gounsa_literature/papers/2000_Ewen_Parkin_OConnell_SHETRAN.md`
`research/gounsa_literature/decisions/2026-10-26_FULL_OPEN_SOURCE_NATIVE_2D_VEGETATION_EROSION_MODELS.md`
INDEX papers395, models60, decisions36; MASTER updated.

## Next work must be original-native
1. Use published original `SHETRAN` Fortran unmodified, clone under branch pinned full SHA, compile with actual repository documented supported toolchain (and available original deps), run **Cobres existing example with sediment on**, report exact original input, output and exit code, not changed vegetation indices.
2. Compare original native at multiple rainfall intensities ONLY after unmodified reference case reproduces; **explicitly note release's BALSED stub** and independently reconcile saved sediment stores/flux if possible.
3. If compiling fails, record actual failure; do not substitute fabricated SWEHR-like model.
4. openLISEM Windows original event with released binaries as alternative, but exact matching source version first.
