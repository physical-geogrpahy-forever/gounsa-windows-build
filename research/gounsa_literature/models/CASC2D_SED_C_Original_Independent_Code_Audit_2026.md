# CASC2D-SED 2D 산지 침식 단일엔진 실제 C source audit (2026-10-27)

## 원본의 계보와 실재성
- Johnson et al.(2000) [DOI](https://doi.org/10.1111/j.1752-1688.2000.tb04246.x), CSU model introduction and [July 2003 CASC2D-SED v1.0 reference manual](https://www.engr.colostate.edu/~pierre/ce_old/Projects/CASC2D-SED%20Web%20site%20082506/Download_files/CASC2D-SED-Reference-Manual.pdf).
- CSU 공식 모델 사이트: https://www.engr.colostate.edu/~pierre/ce_old/Projects/CASC2D-SED%20Web%20site%20082506/CASC2D-SED-Home.htm , download route `CASC2D-SED-Download.htm`. CSU 페이지는 source+manual+input/output examples 제공을 명시하나 이 세션에서는 legacy download URL은 HTTP403으로 직접 접속 불가.
- **실제 소스 확보** (archival GitHub copy): https://github.com/wy7980/CASC2D-SED . `readme.md` Git blob `2b8e59269f6eb857b7431d5dc1679022adfdd6cc`는 CSU download page를 원출처로 기재하고, CentOS6.2 GCC4.4.7 makefile, 변수 `rint`→`wrint`로 재선언 컴파일 충돌을 고쳤다고 명시. 그러므로 원 CSU 배포바이트와 **완전히 같은 소스가 아님**. 공개 GPL 등 라이선스는 GitHub repo의 별도 실제 LICENSE 확인 후 단정. 본 세션에서는 native make/실행 없음.

## 1. canopy 경로: 원본 동적 수관차단 없음
- `ReadControlFile.c` blob `1cfa6b1cc7c9fa9c3976b4b519a2a04776ebfba4`: L74–85 landuse Manning `pman[i]`, **initial retained mm `retention[i]`**, USLE-C `cfactor[i]`, USLE-P `pfactor[i]` read.
- `InitializeVars.c` blob `62ee0fde3545aa58c68e5c671044085efdfb53e6` L19: `ret[j][k] = retention[iman[j][k]] / 1000` initial.
- `rain.c` blob `14de283e0a80865bfb7ea65bd90322e90cedac57` L57–60: rain intensity converted (inches/hour) to m/s then `if (ret !=0) intercept(j,k)`.
- `intercept.c` blob `90fb9817f1679755150351cb642fd97562b3e9b4`: **22 line full file** `if (wrint*dt >= ret) {wrint-=ret/dt; ret=0} else {ret-=wrint*dt; wrint=0}`. **No LAI, no canopy water state C(t) with Smax, no time-dependent drainage D(t), no leafdrop throughfall KE**. This code represents **initial land-use interception capacity exhausted** not the physically complete Rutter or Gash model.
- `OvrlDepth.c` L87–91 uses only interception-reduced rainfall for water addition. There is no differentiated soil-reaching water vs rainfall impact KE source.

## 2. true XY 2D but diffusive and only a **single open outlet**
- `OvrlRout.c` blob `4ab95cda944580ee9f077fd562d725c08ab6b107`, L14–34 loops all active grid cells and two unique edges (east and south), `ovrl` exchanges signed water quantity between each adjacent pair.
- `sf=(e_i-e_j)/w -(h_j-h_i)/w`, `dqq=sign(sf)*w*sqrt(abs(sf))/ManningN * (h_upstream-stordepth)^1.667`; (dqov_i-=dqq), (dqov_j+=dqq); flow may reverse depending head gradient. **Interior flow is not D8**. However this is diffusive-wave, not full nonlinear inertial two-momentum SWEs.
- `RoutOutlet.c` under one `jout,kout`, `qoutov` discharge calculated only at that cell, `h[jout][kout]-=qoutov*dt/(w*w)`, channel likewise; no 4-sides all-boundaries free outflow. `OvrlRout` skips missing/outside grid, so no other boundary loss automatically. This directly **fails original Gounsa request freely outflow all edges** (unmodified code).
- `RoutSedOut.c` dispatches sediment export only via the same `jout,kout`.

## 3. native flow erosion and settling; not independent rain splash
- `RoutSedOvrl.c` blob `560dbfbd310ee66cd8f895e424e64e1f27cd1836`: `RoutSedOvrl(dqq,sf,from,to)` only called when `OvrlRout` has nonzero `dqq`. Particle groups sand/silt/clay. Suspended sediment transported, predeposited sediment reentrained, parent material scoured up to remaining transport capacity, `Settling.c` settles by terminal speed and flow depth.
- `Fcts_sed.c` blob `c6816f74e4bb103c0f0450a2ead5f9ae32bff019`: `KRcap(KRcoeff, discharge, width, sf,...)` uses q^2.035, slope^1.66, USLE-C, USLE-K, USLE-P, width, dt. Thus **USLE land-cover factor is not LAI-driven physical interception or mechanistic sediment root resistance**.
- There is **no independent splash detachment source where rain>0 but q=0 in the verified event flow path**. Thus rainsplash+overland detach simultaneously as separate native mechanisms FAIL.
- `InitializeVars.c` initializes `ssoil` of all size fractions to 0; `TransferSed` subtracts eroded parent material fraction from `ssoil`; code does not use positive preloaded finite erodible soil stock to bound erosion in verified path. Negative `ssoil` may be diagnostic cumulative net soil loss, not guaranteed physical stock. Soil depth constraint would be a new modification.

## 4. Actual peer-reviewed resolution and follow-up
- [Johnson et al.(2000)](../papers/2000_Johnson_Julien_Molnar_Watson_CASC2D_SED.md) Goodwin Creek runoff peaks/timing ±20%, sediment rates -50 to +200% observational case, broad error, not 5–10cm.
- [Rojas et al.(2008)](../papers/2008_Rojas_Velleux_Julien_Johnson_CASC2D_SED_GridScale.md): **30–330m model computational grids**, typical 30/90m results. 5–10cm precedent missing.
- [Wei & Kinouchi(2014)](../papers/2014_Wei_Kinouchi_CASC2D_Forested_Interception.md) Japanese forest CASC2D modified `Smax(mm)=0.935+0.498LAI-0.00575LAI²` from existing empirical canopy study. This is **different modified hydrologic research implementation**, not automatically the released `wy7980` sediment executable; its 5–10cm erosion run and code not found. Claiming original `intercept.c` uses LAI would be FALSE.
- [Jiang et al.(2025) AHMS-SED](../papers/2025_Jiang_Parteli_Shao_AHMS_SED_20km_Original_Code.md) new 20km Yellow River sediment model, [actual published code/Zenodo v1](https://zenodo.org/records/14494932), plus [Github](https://github.com/JiangCong1990/AHMS-SED) README. Regionally routed modified CASC2D-SED, not sub10cm free XY sediment model.

## GO/NO-GO
| Hard gate | CASC2D-SED archived C source |
|---|---|
| Source available | YES, archived modified copy (file/Makefile) |
| Native xy internal flow | YES, *diffusive-wave*, bidirectional |
| 2D sediment and deposition | YES, flow-based sand/silt/clay |
| Native LAI canopy storage/drainage throughfall | NO, static initial retention only |
| Direct rainsplash separately from flow erosion | NO in inspected active execution |
| All four open boundaries | NO, one `jout,kout` |
| Peer-reviewed <=0.1m computation | NOT FOUND, explicit 2008 30–330m |
| cm-scale numerical convergence, soil stock | NOT TESTED, finite depth not encoded in verified path |

**Strict user Gounsa original single engine: NO-GO.** Original full academic model and actual source existence is real, but cannot merge Jetten, Wei(2014), or AHMS sediment into a single preexisting published matching engine. Any expansion must be declared a new fork and independently tested. **Do not suggest Casc2D as replacement for Classic OpenLISEM just because model source exists.**

## Source links
https://github.com/wy7980/CASC2D-SED/blob/master/intercept.c
https://github.com/wy7980/CASC2D-SED/blob/master/OvrlRout.c
https://github.com/wy7980/CASC2D-SED/blob/master/RoutOutlet.c
https://github.com/wy7980/CASC2D-SED/blob/master/RoutSedOvrl.c
https://github.com/wy7980/CASC2D-SED/blob/master/Fcts_sed.c
https://github.com/wy7980/CASC2D-SED/blob/master/ReadControlFile.c
https://github.com/wy7980/CASC2D-SED/blob/master/InitializeVars.c
https://github.com/wy7980/CASC2D-SED/blob/master/Makefile
