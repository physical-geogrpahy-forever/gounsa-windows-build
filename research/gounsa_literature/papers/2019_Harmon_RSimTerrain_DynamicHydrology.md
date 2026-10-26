# 서지정보
Harmon, B. A., Mitasova, H., Petrasova, A., & Petras, V. (2019). r.sim.terrain 1.0: A landscape evolution model with dynamic hydrology. *Geoscientific Model Development, 12*, 2837–2854. https://doi.org/10.5194/gmd-12-2837-2019

# 이 논문을 찾은 이유
2D 격자형 유수침식과 현장 DEM 지형변화 및 rill 발달을 동시에 다루는 전체 공개 원본을 다시 조사.

# 연구 유형
과정 기반 공간분포 유수 및 유사 수치모형과 지형발달 연구; 현장 LiDAR와 비교한 사례.

# 공간 구조
GRASS GIS Python addon `r.sim.terrain`에서 `r.sim.water` 및 `r.sim.sediment` (SIMWE)의 2차원 stochastic path-sampling / Green function Monte Carlo 수치해법을 이용. 대안으로 RUSLE3D/USPED 제공. **SIMWE의 2D stochastic flow를 완전한 2D finite-volume SWE와 혼동하지 않는다.**

# 적용환경 / 검증 방법
미국 Fort Bragg의 Patterson Branch 소유역. 면적 약 450 m² 상세지형, LiDAR 기반 다년 DEM과 동적 침식/퇴적 지형분석 비교. Rills, ephemeral gullies, channel incision/widening, aggradation 등 fine-scale morphology 구현 논문 주장. 모델성능의 정량 절대오차를 확인하지 않은 상태에서 현장 검증 PASS라고 주장하지 않는다.

# 원본 구현 과정
- 2D surface runoff `r.sim.water`와 유사 이송/침식/퇴적 `r.sim.sediment` 모델 실행
- `r.sim.terrain`에서 강우사상 마다 침식/퇴적에 따른 raster DEM 갱신
- 동적 runoff, shallow overland flow, transport-limited/detachment-limited condition
- 시간 및 격자 해상도 영향을 처리하며 multiple walkers stochastic solution

# 식생 입력
`c_factor`, `mannings`, `detachment`, `transport`, `runoff` 등 **raster land-cover/coefficient**. 원본 문헌 및 최신 명령어 옵션에서 **LAI 기반 canopy interception, CStore, throughfall and leafdrip energetics**는 확인되지 않았다. 지표 피복률이 LAI-driven canopy hydrology와 같지 않다.

# 핵심식, 매개변수, 단위
`r.sim.sediment` manual: `water_depth` [m], `detachment_coeff` [s m^-1], `transport_coeff` [s], `shear_stress` [Pa], `man` Manning surface roughness. `r.sim.terrain` precipitation intensity [mm h^-1], DEM [m], erosion elevation change [m], walkers simulation particles [-]. Dimensional and coefficient correctness must be confirmed from primary manual before using.

# 원래 코드 범위, 고운사 적용
Public GPL2 GRASS addon https://github.com/baharmon/landscape_evolution, GRASS manuals and example GIS dataset publicly downloadable. The native 2D erosion/DEM updating and LiDAR small-catchment paradigm is extremely relevant as **geomorphological benchmarking**. But dynamic vegetation LAI canopy water storage and plant-height-dependent leafdrip/throughfall is absent/unproven, and separate explicit rainfall impact versus runoff-driven detachment source not shown as native distinct functions. No original numerical convergence/finite stock or source exact-version compile run carried out here.

# 최종 판정
**고운사 세 조건을 모두 충족한 단일 원본에서 제외.** High-value secondary 2D erosion/rill/topographic feedback comparison; could be used as an independent geomorphic benchmark only. Do not solve missing canopy by changing C factor and calling it physically endogenous interception.

# Sources
https://gmd.copernicus.org/articles/12/2837/2019/gmd-12-2837-2019.html
https://grass.osgeo.org/grass-stable/manuals/r.sim.sediment.html
https://grass.osgeo.org/grass-stable/manuals/addons/r.sim.terrain.html
https://github.com/baharmon/landscape_evolution
