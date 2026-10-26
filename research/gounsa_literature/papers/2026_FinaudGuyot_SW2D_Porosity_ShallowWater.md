# 2026 SW2D porosity-based free-surface-flow model

## 서지정보
Finaud-Guyot, P., Guinot, V., Rousseau, A., Bugeau, L., Steinstraesser, J. G. C., & Delenne, C. (2026). The SW2D software for porosity-based shallow water simulations. *Environmental Modelling & Software*, 107190 (published online 8 October 2026). https://doi.org/10.1016/j.envsoft.2026.107190

## 검색 이유
2026년 새 발표된 공개 2D 식생/강우유출 해석 소스가 원본 유수침식 및 sediment transport까지 포함하는지 선별.

## 연구 유형 / 공간구조
Fully documented open-source finite-volume 2D shallow water on unstructured arbitrary polygonal grids, multiple (five) hyperbolic porous shallow-water formulations. Source and sample data on authors' GitLab. Rainfall, infiltration, wind stress forcings.

## 적용 환경
Floods and distributed free-surface flow, porosity caused by structures/vegetation. Peer-reviewed 2026 hydrodynamics method and analytic cases; detailed mountainous erodible burned forest and native leafdrip splash validation not established.

## 핵심과정/식생
Porosity and friction act on 2D water fluxes. LAI-driven canopy water storage, canopy throughfall, leafdrip KE, separately modeled raindrop detach, flow detachment, two-dimensional sediment conservation and bed evolution **not part of the published paper's declared functionality or highlights**. Absence is currently based on publication model module scope, not a complete examination of every GitLab repository source file.

## 고운사 적합성 / 새 coupling
Water flow and numerical verification might serve independent SWE solver science; native original 2D soil erosion and biological interception missing/unverified. Adding any rain/drip/erosion modules is new implementation, not original model.

## 최종 판정
**Main original integrated Gounsa erosion engine 탈락**, because no positive verification native sediment detachment/advection and canopy LAI. No build or rainfall erosion test performed.

## Reference
https://www.sciencedirect.com/science/article/pii/S1364815226003373
