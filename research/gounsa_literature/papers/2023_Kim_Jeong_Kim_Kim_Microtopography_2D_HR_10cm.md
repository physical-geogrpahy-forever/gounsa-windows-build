# Kim et al. (2023) — Genuine 10 cm 2D computational mesh, SWE-HR erosion/deposition

## 서지정보
Kim, S., Jeong, M., Kim, J., & Kim, D.-H. (2023). Effects of Soil Particle Size on Relationship Between Mound-Puddle Type Microtopography Roughness and Soil Erosion Rate on a Hillslope Basin: Hairsine–Rose Model Analysis. *Water Resources Research, 59*(3), e2022WR033879. https://doi.org/10.1029/2022WR033879

## 연구 유형·검색 이유
동료심사 2D 수치모형 사례. 사용자의 5–10cm 고해상도 **실제 계산격자**가 수문과 침식·퇴적에 관해 출판된 사례인지 검증. UAV 관측 해상도와 계산 격자 및 1D vs 2D 구분 필요.

## 공간구조 및 사례
§2.2.6: 10m wide ×21m long real-microtopography-informed 2D basin; **41,380 triangular cells, 21,000 nodes, node spacing 0.1m =10cm**. This is numerical simulation spacing, not DEM observation alone. Additional 1D basin 4,816 triangular cells, 3,013 nodes, **node spacing 0.01m =1cm**, but this fine simulation is *1D*; do not advertise it as genuine 1cm 2D. The 2D basin average slope0.03 (3%), not steep high-gradient forest. Zero infiltration by assumption (impervious); boundary one downstream zero-gradient, other edges walls. No all-four free outflow.

## Core processes and native model provenance
§2.1 uses *tRIBS-FEaST* coupled dynamic-wave 2D shallow-water with true x/y accelerations, inertia and pressure, and Hairsine–Rose independent rainfall impact detachment / runoff entrainment, size-selective advected suspended load, settling and deposited layer shielding. Original Kim/Ivanov/Katopodes (2013) core DOI10.1002/wrcr.20373. Spatially complex mound/puddle features change soil erosion trends depending on settling particle diameters even under similar outlet runoff hydrographs.
§2.2.4 soil distribution seven classes for 2D with settling velocities2.1,6.8,20,38,75,160,300mm/s. No explicit fully dynamic canopy interception active in this study.

## Vegetation, limits
§2.2.5 says explicitly **all test basins uniformly bare soil** and vegetation effect **not considered**. No LAI canopy Smax/time-dependence, no throughfall/stemflow or canopy leaf drip KE in these numerical experiments. 2D simulation is 10cm and not 5cm; 1cm is merely 1D. Original tRIBS's public GitHub base can simulate Rutter interception but authors' complete FEaST 2D HR published extension EXACT executable source still unavailable in audited original tRIBS repository. 2023 article Data Availability indicates 2D bathymetry data from Frei et al.(2010) on request, not release of 2023 model solver. Source identified? **NO.** Built/runtime replicated in Gounsa? **NO.**

## Useful new scientifically grounded result
Published genuine 10cm 2D finite volume shallow water + rainfall and runoff soil erosion/deposition in microtopography; spatial microtopography can control sign/magnitude of grain size effects. This is a strong *resolution and geomorphic-process* benchmark, not an accessible full canopy model. Avoid promoting this as forest 10cm canopy study.
Parameter units h[m], x/y 0.1m, settling velocity[mm/s], rainfall intensity rain excess [original paper equations HTML image-backed].

## Final Gounsa verdict
**PASS published 10cm genuine 2D HR erosion+deposition study (bare and gentle slope). FAIL simultaneous vegetation interception, source reproducibility, steep Gounsa ecology/5cm/full four-sided flux.** Research precedent only.

Sources: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022WR033879 ; https://doi.org/10.1002/wrcr.20373 .
