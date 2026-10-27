# 2026-10-27 CASC2D-SED CSU 공개 원본 C 확보와 2000/2008/2014/2025 버전 분리: 고운사 주모델 NO-GO

## 결정
OpenLISEM 7.5.2 수정/네이티브 재실행은 Work에 맡기고, 별도 발표 모델을 찾음. 새로 발견한 **비-OpenLISEM CASC2D-SED 전체 C 소스 보존본** `https://github.com/wy7980/CASC2D-SED`를 직접 검사. 심층 감사 [models/CASC2D-SED](../models/CASC2D_SED_C_Original_Independent_Code_Audit_2026.md).

**실제 출처 확보 = yes; 필수 LAI 동적 canopy + splash + unrestricted four boundaries + <=10cm published executable = NO; 고운사 원본 단일 주엔진 선정 보류.**

## 새로 추가한 3개 논문
1. [Johnson et al.(2000)](../papers/2000_Johnson_Julien_Molnar_Watson_CASC2D_SED.md), DOI10.1111/j.1752-1688.2000.tb04246.x. 2D diffusive wave, Green-Ampt, sand/silt/clay sediment transport, net erosion and deposition, Goodwin Creek test; reported peak discharge/time ±20%, sediment rates error -50% to 200% (journal abstract). Genuine 2D **diffusive-wave**, not dynamic SWE.
2. [Rojas et al.(2008)](../papers/2008_Rojas_Velleux_Julien_Johnson_CASC2D_SED_GridScale.md), DOI10.1061/(ASCE)1084-0699(2008)13:9(793). **Actual published 30m–330m** sensitivity, 30m/90m acceptable, not 5cm, coarser 150m bad sediment distribution.
3. [Jiang et al.(2025)](../papers/2025_Jiang_Parteli_Shao_AHMS_SED_20km_Original_Code.md), DOI10.1029/2024MS004593. Modified CASC2D-SED + AHMS regional Yellow River **20km**; [2024-12-15 Zenodo source archive](https://zenodo.org/records/14494932), [GitHub author repo](https://github.com/JiangCong1990/AHMS-SED). Regional subgrid routing modified, not exact original code and not sub10cm physical runoff erosion test.

## Source audit finding exactly in code
- `readme.md` in `wy7980` attributes original to [CSU legacy downloads](https://www.engr.colostate.edu/~pierre/ce_old/Projects/CASC2D-SED%20Web%20site%20082506/CASC2D-SED-Download.htm). Clone fixes compile symbol `rint`→`wrint`; not byte-identical published original. CSU legacy website original link directly HTTP403 but GitHub file contents successfully read through connector; no run done.
- `ReadControlFile.c` `retention` per land-use mm, `InitializeVars.c` `ret=retention/1000`, `intercept.c` 22 lines simply subtracts `min(rain*dt,ret)` and sets storage remaining. **LAI dynamic canopy storage/drainage/drop kinetic energy absent**. Rain subsequently added directly to `OvrlDepth`.
- `OvrlRout.c` signed `sf=(DEM_i-DEM_j)/w-(h_j-h_i)/w`, `dqq=sign(sf)*w*sqrt(abs(sf))/n * (h-upstream storage)^1.667`, pairwise exchange on right/down edges giving interior x/y **both directions**. This is real 2D **diffusive wave**, not directed graph/D8.
- `RoutOutlet.c` `qoutov` calculation exclusively at single `jout,kout`, `RoutSedOut.c` same; outside/missing neighbors skipped. **Can't exit freely through all four boundaries as supplied user requirement**.
- `Fcts_sed.c::KRcap` sediment transport capacity ∝ slope^1.66 × unit-discharge^2.035 × USLE C/K/P. `RoutSedOvrl.c` dispatch only with nonzero `dqq`, sand/silt/clay suspended/deposited/parent soil, settles later `Settling.c`, net erosion `SedStats.c`. **Independent rainfall splash detachment where no flow = absent** in verified model execution path.
- `InitializeVars.c` `ssoil=0`, `TransferSed` deducts parent soil eroded mass, not a positive finite erodible soil depth store proven to prevent physically excessive incision. Numerical time/mesh convergence at 5cm not tested.

## Relation to already known 2014 Wei & Kinouchi
- Existing [2014 forested CASC2D](../papers/2014_Wei_Kinouchi_CASC2D_Forested_Interception.md) DOI10.2208/jscejhe.70.I_157 derives LAI-linked max canopy storage from forest catchment rainfall-runoff modeling. This is a **modified 2014 forest hydrology version** whose source is NOT identified with recovered 2003 CSU CASC2D-SED C code. Paper did not perform 5cm native canopy and sediment grid test.
- User requested an existing published **single version**: can't simply add Wei's LAI function into C model and claim it is published CASC2D-SED, or add current AHMS-SED 20km routing and claim cm-scale.

## What was excluded rather than newly recommended
- 2026 Braga et al. SERGHEI-SE, 2025 Hinsberger Yörük HydroAS-2D, 2026 Finaud-Guyot SW2D already in INDEX; no duplicate paper created. HydroAS requires proprietary code and did not use splash, 25cm finest. SW2D hydraulics only. CASC2D-SED is a **different source lineage from previously excluded TREX** but descendant functional limitations overlap.
- Explicit major unmet goal: published 5–10cm + quantitative LAI canopy water storage/throughfall, direct impact and flow detachment, genuine free XY 2D all edges, sediment conservation+deposition, same original executable source.

## New decision
Original CASC2D-SED is an **excellent publicly available comparison implementation of 2D diffusive-wave sediment**, but **does not qualify for Gounsa original unmodified main engine**. The basic academic model is not being denigrated; the explicit research requirements cannot be fulfilled by the deposited source.

Further research should prioritize entirely new SAME-VERSION published sub10cm canopy/sediment executable, and not reintroduce sources already screened NO-GO without a materially different version.

## Source URLs
https://github.com/wy7980/CASC2D-SED
https://github.com/wy7980/CASC2D-SED/blob/master/intercept.c
https://github.com/wy7980/CASC2D-SED/blob/master/OvrlRout.c
https://github.com/wy7980/CASC2D-SED/blob/master/RoutOutlet.c
https://github.com/wy7980/CASC2D-SED/blob/master/RoutSedOvrl.c
https://github.com/wy7980/CASC2D-SED/blob/master/Fcts_sed.c
https://doi.org/10.1111/j.1752-1688.2000.tb04246.x
https://doi.org/10.1061/(ASCE)1084-0699(2008)13:9(793)
https://doi.org/10.1029/2024MS004593
https://zenodo.org/records/14494932
