# 2026-10-26 실제 공개 원본 소스코드 안에서 수관과 침식 기능을 모두 확인한 대체모형 감사

## 사용자 결정 요구
**임의의 식생 계수를 덧붙이거나 미공개 저자 코드를 요청해 얻을 수 있다고 가정하지 않는다.** GPL 등으로 전체 개발 소스와 실행 입출력 예제가 공개되었으며 실제 원본 코드 안에 식생 수문/박리저감이 있는 모델만 채택 후보. 2D overland + rainfall impact + separate flow detachment + leaf drip/canopy + ground/rock shield + mountain prior. 미구현은 미구현이라고 표시. 실제 compile/run하지 않으면 통과했다고 주장 금지.

## 최초 감사 결론
- **SHETRAN original** [nclwater/Shetran](https://github.com/nclwater/Shetran) 2026 current original Fortran/CMake project v4.7.2.0, GPL-3.0. Contains full `src/evapotranspiration/ETmod.f90`, `src/sediment/SYmod.f90`, `src/overland_channel/OCmod*.f90`, input sediment examples Cobres/Aire and archives of third-party dependencies under `external/tarballs/` (HDF5, zlib-ng, Fortran stdlib). EVALUATION SOURCE VERIFIED, compiler and numerical mass balance NOT YET TESTED.
- **Classic openLISEM original** [vjetten/openlisem](https://github.com/vjetten/openlisem/tree/main_C) GPLv3, code functions confirmed `hydro/lisInterception.cpp`, `erosion/lisErosionSplash.cpp`, `erosion/lisErosion.cpp`, `erosion/lisSWOF2DSediment.cpp`; 2D FullSWOF dynamic flow, direct rain/leafdrip KE, canopy interception and litter, grass/rock/no splash, separate flow detachment. Build needs Qt6 and dependencies; previously Linux environment setup failed. User has earlier provided native Windows 7.5.2 installer, but availability/behavior of that executable and source-identical version NOT locally validated. Do NOT pretend earlier OpenLISEM compile issue solved.
- **SWEHR V1 2017** C fully available and compiled untouched but original McGuire 2016 vegetation Rutter and canopy direct splash shielding not included, thus cannot meet need out of box.
- **DHSVM PNNL official** [pnnl/DHSVM-PNNL](https://github.com/pnnl/DHSVM-PNNL) forest canopy source exists (`InterceptionStorage.c`), but current `DHSVM/sourcecode` complete tree contains NO detachment/sediment modelling source despite Doten 2006 separate derived erosion model publication, so NO native-source verified combined model.
- **GEOtopSed** [TanZiTT/GEOtopSed](https://github.com/TanZiTT/GEOtopSed) GitHub file tree includes `GEOtop/` standard physical water and energy source and libraries but NO named sediment erosion/source/transport module; four major C files inspected `geotop.c`, `water.balance.c`, `vegetation.c`, `output.c` contained NO explicit erosion/sediment physics key functions. Its 2016 published sediment model and SourceForge version may not match this GitHub archive: excluded from 'full verified' until original erosion source is found and linked. 
- **SMODERP2D** GPL3 full Python source [storm-fsv-cvut/smoderp2d](https://github.com/storm-fsv-cvut/smoderp2d) distributed event 2D sheet/rill hydrology in water-resources management but initial inspected tree lacks separately identifiable raindrop detachment + sediment advection module and canopy/drip physics. Not accepted under strict all-process criteria from repo name/descriptions.

## SHETRAN rigorous source evidence
- `ETmod.f90` near lines 451–529: `CSTORE(IEL)` canopy store and `CSTCAP(N)`, `CK(N)`, `CB(N)`, dynamic updates `DRAIN`, `DRAINA(IEL)=DRAIN/(1000*DTUZ)` lines 817 and original vegetated evaporation. This is real canopy water reservoir, NOT fixed fraction.
- `SYmod.f90` subroutine `SYWAT` near lines 4475–4499: canopy sheltered `FCC=PLAI*MIN(CLAI,1)`, rainfall from canopy `DRAINA`, computes raindrop diameter `DRDROP` and direct rainfall `LRAIN`.
- `SYmod.f90` subroutine `SYOVER` near lines 3766–3805 implements \(GMR=(1-FCC)a LRAIN^b\), \(GMD=TGMD\,DRAINA\), \(TGMD=\pi\rho_w^2 g c (1-\exp(-2XDRIP/c))DRDRIP^3FDRIP/6\). \(DR=GKR\exp[-\max(0, DWAT1/DRDROP-1)] (1-FCG-FCROCK)(GMR+GMD)\); \(DF=GKF (1-FCROCK)\max(0,\tau-\tau_c)/\tau_c\). `DLS>=DLSMAX` suppresses underlying soil detachment. Soil properties and vegetation independent.
- Original 2D 4-face finite-difference routing in SHETRAN surface OC `QOC(iel,face)`, spatially distributed land cells not D8 1D only, plus 3D subsurface.
- Wicks & Bathurst 1996 SHESED original abstract explicitly states **sheet overland flow WITHOUT rilling**. Do NOT claim automatic rill initiation and incision. Individual stemflow concentrated per-stump/crown spatial map not separately identified. Root quantity/root length density to soil erodibility not automatically modeled. `FCROCK` is rock-exposed fraction and NOT rock production/weathering/rock movement.
- Numerical ledger caveat: `SUBROUTINE BALSED` in `SYmod.f90` lines 4668–4669 is empty; no full independent sediment closure done. Does not rule out correct native sediment flux, but disqualifies uncritical mass-balance accuracy claims.
- Example `examples/Cobres/model/rundata_cob.txt` enumerates sediment input line 17 `input_cob_syd.txt`. `SY24` input 3.0m fall, .005m drip diameter, .5 drip fraction for generic vegetation; not Gounsa-specific. `SY41` FCG, `SY42` FCROCK; 7 sizes.
- `COMPILING.md`: Windows ifx 2026 and VS 2026; Linux gfortran 16.1 (or Intel ifx), CMake, fypp, HDF5 and zlib-ng/stdlib source tarballs all present in external/tarballs. **No native compilation or experiment run performed** and tool DNS GitHub access blocked in container; no invented success.

## OpenLISEM source specifics and current limitation
- `hydro/lisInterception.cpp` lines 43–73: canopy `Cover, LAI, CanopyStorage, CStor, LeafDrain, RainNet` present. Computes `CS=Smax(1-exp(-canopen RainCumInt/Smax))`, `canopen=1-exp(-0.45*LAI)`, `RainNet=Cv*LeafDrain+(1-Cv)*Rain`. Separate litter interception.
- `erosion/lisErosionSplash.cpp` lines 59–114: `directrain=(1-Lc)(1-Cv)Rainc`, `KE_LD=max(15.3sqrt(PlantHeight)-5.87,0)` (height units internal map must be checked), `throughfall=(1-Lc)Cv*LeafDrain`, `DetLD1/2 + DetDT1/2`, `(1-StoneFraction)` and `(1-GrassFraction)` suppression. Splash delivered to `SSFlood` under 2D dynamic.
- `erosion/lisSWOF2DSediment.cpp`: `SWOFSediment`, original 2D SWOF sediment advection, suspension, bedload, deposition, `SedimentDetachmentSS`.
- OpenLISEM official repository source code `main_C` more recent README 7.5.0 series; `openLisemSetup_7.5.2.exe` from previous chat is not shown to be identically compiled from inspected `main_C` revision. Prior Linux Qt6/QWT dependency failure remains. Avoid recommending pointless retry of unavailable Qt packages.

## Compare against strict priorities
| User constraint | SHETRAN | openLISEM | published SWEHR 1.0 |
|--|--|--|--|
| full original source | YES | YES | YES |
| ready example config with sediment input | YES (Cobres/Aire) | manuals and open official examples yes but site default not inspected | sample default had no Rutter |
| real canopy storage original code | YES, dynamic C | YES, storage model | NO |
| direct vs drip splash original code | YES, height/diameter | YES, height/KE | NO separated per canopy |
| rain and flow detachment | YES | YES | YES |
| independent ground cover/rock surface shielding | YES | YES | waterdepth and loose sediment only |
| genuine 2D spatial overland domain | yes horizontal 4-face finite differences, NOT 2D SWE full dynamic-wave | YES FullSWOF 2D SWE mode | YES 2D SWE |
| rills automatically incised | NO, original sheet without rilling | NOT demonstrated that rills 'automatically' form; 2D flow concentration spatially varies | original plot channels possible but vegetation absent |
| individual plant SF mapped | NOT verified | NOT verified | NO |
| measured root RLD coupled natively | NO | NO | NO |
| surface spall rock evolution | NO | NO | NO |
| code compiled & example run locally in this task | NO | NO; prior build fail | original no modifications compiled previously |

## Research implementation decision
Two genuinely source-verified candidates: **(1) SHETRAN primary new alternative to test first on full original Cobres sediment case** (strongest documented canopy-drip + soil and rock processes as native original, no request to authors), **(2) openLISEM as second serious native-source option** (explicit 2D dynamic SWE, has original canopy+drip+litter+rock). No native performance or mass-closure score until real run. Not automatically replace previous SWEHR or Iber decision with unverified results: move SHETRAN to FIRST execution priority and openLISEM to second if original input/computation needed. Distinguish original model from any newly proposed canopy+stem source.

## Bibliography
Wicks & Bathurst 1996 J Hydrol, doi:10.1016/S0022-1694(96)80012-6.
Ewen, Parkin & O'Connell 2000 J Hydrologic Eng DOI 10.1061/(ASCE)1084-0699(2000)5:3(250).
SHETRAN current repo https://github.com/nclwater/Shetran
Classic openLISEM current repo https://github.com/vjetten/openlisem/tree/main_C
openLISEM wiki https://github-wiki-see.page/m/vjetten/openlisem/wiki
DHSVM official https://github.com/pnnl/DHSVM-PNNL
GEOtopSed archive https://github.com/TanZiTT/GEOtopSed
SMODERP 2D https://github.com/storm-fsv-cvut/smoderp2d
