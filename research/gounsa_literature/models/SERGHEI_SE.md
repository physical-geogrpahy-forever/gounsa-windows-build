# SERGHEI-SE lineage

## 핵심 문헌
- Martínez-Aranda et al. (2025 preprint), *SERGHEI-SE: An Open-Source High-Performance-Computing Model for Soil Erosion and Sediment Transport Processes in Catchments*
- Braga, Martínez-Aranda & García-Navarro (2026), Water 18(15), 1870, DOI 10.3390/w18151870

## 고운사에서 검토한 이유
latest open-source high-performance genuine 2D catchment-scale erosion framework.

## 공간구조
- 2D shallow-water equations
- 2D solid transport
- finite volume
- bed evolution
- HPC/high-resolution catchment computation

## vegetation
2025 model description uses a vegetation/land-management/bedrock modification factor, including Sentinel-2-derived inputs in the demonstrated setup.
Dynamic root biomass/RLD is not a core state variable.

2026 evaluation likewise does not solve the quantitative vegetation-state gap.

## 강점
- genuine 2D
- conservation-oriented finite-volume formulation
- catchment-scale HPC
- explicit surface evolution

## 한계
- quantitative root/litter state missing
- root recovery after wildfire not represented mechanistically

## 고운사에 쓸 수 있는 부분
Modern 2D-engine comparison and implementation architecture.

## 새로운 coupling
LPJ-GUESS root/litter states linked to erosion parameters are **new coupling**.

## 최종 판정
**2D-engine comparison candidate.**
