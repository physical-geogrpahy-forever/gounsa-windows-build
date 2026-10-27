# 2026-10-27 23:55 독립 비LISEM 문헌조사: Aksoy2020, WASH123D, Qu-Duffy2007 PIHM

## 이번 세션의 작업 범위
사용자의 고운사 프로젝트. Original OpenLISEM 원본수치 오류는 별도 Work가 담당, 본 세션은 **새로운 실제 published non-LISEM 단일 5~10cm 산림 수관저류와 자유 XY SWE 강우 및 유수침식+퇴적** 소스 찾기. `SYSTEM.md`, `MASTER.md`, `INDEX.md` (직전501 papers/105 models/103 decisions) 최신 읽은 후 DOI/제1저자로 중복 검색하고 시작.

## 새 논문 3건, 새로운 model source audits 2건
1. [Aksoy et al (2020)](../papers/2020_Aksoy_Gedikli_Yilmaz_2D_Rill_Interrill_Lab_Validation.md) *J Hydrology 581 124391*, DOI10.1016/j.jhydrol.2019.124391. **2D rainfall-runoff + sediment coupled original** experimentally validated in bare sand flume with pre-existing longitudinal rill, X and Y slope5–20%, rainfall45–105mm/h; native gridwidth and full-SWE momentum cannot be confirmed without restricted Methods and no source found. Canopy absent in published validation. Not a 5cm forest canopy engine.
2. [Yeh et al (1998) WASH12D/WASH123D](../papers/1998_Yeh_Cheng_WASH123D_2D_Overland_Sediment_TechReport.md), USACE CHL-98-19, original preliminary WASH12D abstract includes **2D overland+sediment**, selectable kinematic/diffusive/**dynamic-wave**. [Code audit](../models/WASH123D_1998_2D_Flow_Sediment_Source_Availability_Audit.md): [official CSDMS listing](https://csdms.colorado.edu/wiki/Model:WASH123D) **says 'As code' but Source web URL blank and indexed 'Source code not available'**. GitHub WASH12D/123D original source search no match. LAI/throughfall/leafdrip and published 5cm run not proven, refuse recommendation.
3. [Qu & Duffy (2007)](../papers/2007_Qu_Duffy_PIHM_Canopy_ODE_FVM_Watershed.md) WRR 43 W08419 DOI10.1029/2006WR005752. Original paper §3.2.1 canopy storage h_v balance, original current public source [PSUmodeling/MM-PIHM](https://github.com/PSUmodeling/MM-PIHM) MIT [source audit](../models/PIHM_MM_PIHM_2007_LAI_Canopy_Source_And_PIHMSed_Lineage_Audit.md): `src/is_sm_et.c` blob `3a178dd207c69abe520fd7aa766c0c32ff7b11f7` line86 `intcp_max = lc.cmcfactr * lai * lc.shdfac`, `src/read_lai.c` external dynamic `LAI_TS`, canopy evaporation water balance active. But native repo target builds `pihm`, `flux-pihm`, `flux-pihm-bgc` no sediment; `src/transpt/` four files all solute, not soil erosion. Shale Hills historical PIHMSed regolith and tree-throw development is DIFFERENT research, no publicly matched 5cm integrated event erosion binary. Fail strict user.
4. [Decision](../decisions/2026-10-27_2355_NEW_AKSOY_WASH123D_PIHM_STRICT_PUBLISHED_SOURCE_SCREEN.md) records all criteria and unchanged NO-GO.

## Archive actions committed
Three new papers, two new model audits, one new decision, this handoff. `INDEX.md` updated with **Papers504 Models107 Decisions104** as of audit (contains .gitkeep); ensure `MASTER.md` summary present.
GitHub direct connector used to access model C source and repo trees. Web used for original DOI and official CSDMS metadata. **No numerical simulation, compilation or cm-scale original-code run** conducted in this research turn.

## Scientific takeaways
- **PIHM canopy LAI actively implemented**; code-public/real parameter path proven, but current source does not include original rill sediment solver. Distinguish related PIHMSed geological transport.
- **WASH123D 2D sediment feature is described**; code download and canopy input unknown despite 'as code' field; explicitly CSDMS 'source code not available'.
- **Aksoy2020** is new direct dual-slope bare interrill/rill sediment validation original, but actual 5cm and canopy not provided.

## Next target (strict)
Only paper that *actually ran* 5cm or10cm TWO-DIMENSIONAL lateral SWE with dynamic LAI interception/leafdrip energy and local sediment, where matching FULL open original source or binary/exact dataset is available. No unpreceded SHETRAN scale-up or returning assigned OpenLISEM Work code. Avoid filling archive with unrelated generic field obs. Multi-source coupling is NOT a published single model.

## Session handoff correction after more primary article access
Elsevier publicly indexed Aksoy 2020 Introduction/Section snippets at https://www.sciencedirect.com/science/article/pii/S0022169419311266 reveal model's hydrologic predecessor is derived from 2D control volume **but explicitly solves only longitudinal flow**, and 2020 reduction in dimension is deliberate; therefore do NOT say 2020 published an unconstrained fully XY SWE 2D test. Original experiment flume physical 6.50m×1.36m×0.17m, D50 0.45mm medium sand /0.15mm fine sand. Rain/flow erosion both mentioned, but canopy/actual grid/source not. Canonical paper and latest decision were appended with this strict clarification. At 2026-10-27 record close, no new runnable all-pass solver.
