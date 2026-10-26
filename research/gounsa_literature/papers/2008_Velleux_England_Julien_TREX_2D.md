# Velleux, England & Julien (2008): TREX

## 서지정보
Velleux, M. L., England, J. F., Jr., & Julien, P. Y. (2008). TREX: Spatially distributed model to assess watershed contaminant transport and fate. *Science of the Total Environment, 404*(1), 113–128. https://doi.org/10.1016/j.scitotenv.2008.05.053

## 이 논문을 검색한 이유
OpenLISEM 폐기 이후 genuine 2D rain-runoff-erosion original source with example sediment tests and mountain forest application precedent.

## 연구유형과 공간구조
Event-scale **2D overland flow** over watershed DEM cells; 1D stream channels; interception/infiltration and sediments in overland/channel. Based on CASC2D (diffusive wave overland), published original TREX implementation as spatial model. Crucial: inspect original code before claiming exact full 2D dynamic SWE or numerical stability.

## 적용환경
Colorado State University TREX program has published experimental/watershed hydro/erosion cases and source + sediment transport example links. Official research page lists Japanese Fukushima Dai-ichi affected **forested** catchment adaptation by Wei et al. (2017) and **South Korea Naesung Stream** erosion source risk by Ji et al. (2014). These are modified TREX / different environments and are NOT a postfire Gounsa native-model validation.

## 핵심 과정
2D precipitation runoff overland, interception/surface depression, Green-Ampt infiltration, surface erosion/deposition, sediment advection and dispersion and bed elevation adjustment, particle-size classes, channels. Soil/flow erosion mechanics based on physical hydraulic properties; does NOT demonstrate separate leaf-drip kinetic energy in available overview.

## 식생 입력 및 정량성
Official descriptions explicitly state **interception and surface storage simulated as equivalent water depths**. This is NOT proof of LAI-driven canopy store, throughfall timing, dynamic interception evaporation and distinct leafdrip splash. No RLD/fine roots or litter mass-to-erodibility original function verified. Therefore fails user's most important vegetation-state criterion until executable source inspection proves otherwise.

## 수학/단위
Core 2D overland water depth continuity `∂h/∂t + ∂qx/∂x + ∂qy/∂y = effective rainfall - infiltration +/- lateral terms`. h [m], q [m2/s], rainfall/infiltration [m/s]. Original sediment and interception equations must be extracted from code/manual; do NOT invent published formulas from high-level overview.

## 완전한 소스 / 예제 입수 확인
Colorado State University original [TREX-Home](https://www.engr.colostate.edu/~pierre/ce_old/Projects/TREX%20Web%20Pages/TREX-Home.html) **lists** Source Code and Hydrology/Sediment Transport ZIP examples; the source ZIP bytes and matching version are **not yet downloaded/verified** in this session (web open returned 403). The publication documentation states C99 181 *.c + 10 header files as research-era code; availability currently uncertain. A superficial claim 'source exists online' is not successful access/compilation.

## 필요한 새로운 coupling
LPJ-GUESS-derived LAI and canopy storage/throughfall to TREX rain interface would be an **explicitly new coupling** unless native dynamic code emerges after source audit. Do not add unverified vegetation empirical coefficients.

## 한계 / 최종 판정
**Secondary original-source retrieval candidate, NOT currently a verified fully matching engine.** Strong genuine 2D+erosion+real watershed pedigree, but incomplete quantitative canopy native proof, old official source link possibly inaccessible, no native numerical run/pass. If current source unreachable or LAI canopy non-native, do not spend indefinite time repairing.

## Sources
https://www.engr.colostate.edu/~pierre/ce_old/Projects/TREX%20Web%20Pages/TREX-Overview.html
https://www.engr.colostate.edu/~pierre/ce_old/Projects/TREX%20Web%20Pages/TREX-Research.html
https://pubmed.ncbi.nlm.nih.gov/18649925/
