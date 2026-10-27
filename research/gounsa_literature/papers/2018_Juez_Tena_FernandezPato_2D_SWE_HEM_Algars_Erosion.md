# 서지정보

Juez, C., Tena, A., Fernández-Pato, J., Batalla, R. J., & García-Navarro, P. (2018). Application of a distributed 2D overland flow model for rainfall/runoff and erosion simulation in a Mediterranean watershed. *Cuadernos de Investigación Geográfica, 44*(2), 615–640. https://doi.org/10.18172/cig.3320

# 이 논문을 찾은 이유

OpenLISEM 외에 타 저자들이 실제 원본 단일 연구에서 2D full dynamic wave + infiltration + event soil erosion and sediment transport 결합한 사례의 격자 크기 및 수관차단, 국지 퇴적, 공개 코드 여부 확인.

# 연구 유형

Peer-reviewed applied 2D numerical paper; publisher open full 26-page PDF and p.2 screenshot checked. https://publicaciones.unirioja.es/ojs/index.php/cig/article/download/3320/3092/7481

# 공간 구조

**Full 2D dynamic shallow-water equations** on unstructured triangular finite-volume mesh, coupled per-cell SCS hydrological loss and 2D extended Hillslope Erosion Model (HEM). Actual main catchment calculation mesh **158000 triangles over about 419km2, minimum cell AREA 150m2 and max 600m2**, article §4.1 p.14 L1474–1484. Triangle area 150m2 is NOT 5–10cm length. Calibration toy/SCM mesh 200 cells each 66000–200000m2.

# 적용환경

River Algars catchment northeastern Spain, two rainstorm events, outlet water hydrograph and suspended sediment concentrations calibrated. Original catchment ~405km2 upstream designated confluence versus 419km2 numerical catchment shape; avoid conflating exact boundaries.

# 핵심 과정

2D full SWE X and Y dynamic wave, SCS infiltration; HEM locally predicts source and 2D sediment concentration. **Sediment deposition affecting channel topography explicitly NOT included** (original §4.3, PDF p20 L1616–1620). No actual within-storm net depositional DEM correction.

# 식생 입력

Land use roughness and SCS classes but NO confirmed physically active LAI canopy storage, throughfall or leafdrip energy. Article full text find 'interception' returned zero.

# 핵심 식

2D momentum/continuity and 2D HEM parameter source. Published HEM calibrated parameter alternative examples Ki=0.0007kg/m3, Kr=0.004m-1, B=0.001kg m^-8/3s^-1 for event1. Site tuned, not forest-specific. Authors report among calibrated parameter sets event1 sediment volume error 2% but sediment peak ~30% versus event2 volume ~12% and peak ~40% (§4.3), NOT independent validation.

# 파라미터와 단위

Main mesh area 150–600m2, 158k cells. Single full run approximately 24h on Intel i7-4770 3.40GHz 32GB RAM; simplified calibration 30s/SCM run (original p14–16). No actual <=0.1m grid use.

# 원 논문의 구현 범위

Actual original published full 2D hydraulic storm erosion model but source equation does not calculate depositional change in DEM; 5–10cm and canopy are not present.

# 고운사에 사용할 수 있는 부분

Published full 2D dynamic-wave storm and sediment concentration comparison and calibration protocol, not ready-made 5cm local soil erosion model.

# 새로운 coupling

Adding canopy drip and Exner sediment deposition would constitute user-disallowed new model modification, not published 2018 same software.

# 한계

Exact executable source public Git SHA not linked by publisher. 2017 IAHR prior https://www.iahr.org/library/infor?pid=19571 speaks of future RiverFlow2D integration, but cannot assert 2018 original equals some commercial Hydronia code without evidence.

# 최종 판정

**Rejected Gounsa single native cm model**: genuine 2D SWE YES; <=10cm actual mesh NO; explicit LAI canopy NO; local deposition NO; matching source availability not verified.

# 참고 링크

https://doi.org/10.18172/cig.3320

https://publicaciones.unirioja.es/ojs/index.php/cig/article/download/3320/3092/7481