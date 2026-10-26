# Ion, Marinescu, & Cruceanu (2025) ASTERIX

## 서지정보
Ion, S., Marinescu, D., & Cruceanu, S.-G. (2025). ASTERIX: Module for modeling the water flow on vegetated hillslopes. *Environmental Modelling & Software, 186*, 106336. https://doi.org/10.1016/j.envsoft.2025.106336

## 이 논문을 검색한 이유
물리 기반 식생 2D Saint-Venant 천수방정식과 Hairsine-Rose 침식이 배포된 단일 원본 모형으로 구현됐는지 확인.

## 연구 유형, 공간 구조, 적용환경
원본 동료심사 2D vegetation-porosity-dependent shallow-water flow numerics, finite-volume, hexagonal raster, 2025 공개 C source. Laboratory and catchment-scale water-flow applications; 실제 고운사 산림 가파른 사면의 침식 관측 검증 아님.

## 모델에서 실제 구현된 것
Vegetation spatial porosity/friction affects 2D Saint-Venant momentum and water depth, numerical flow tests; source code of *water flow module* publicly described. Crucially the original 2024 ASTERIX author preprint's **Future Extensions** section explicitly says native infiltration/interception are **not yet considered** and a separate Hairsine–Rose **erosion and sedimentation module was in preparation**. 2025 original journal article still presents a water-flow module, with no published proof that canopy LAI interception and sediment solver have been released integrated.

## 식생 입력
Porosity / physical vegetation density, friction/plant roughness; **NOT LAI-dependent canopy water-storage/throughfall or raindrop/leafdrop KE** in evidenced original code. Vegetation porosity != overstory LAI or fine root biomass/RLD. Soil cover and direct hit require separate equations not in this release.

## 핵심 식/모수
Extended porous Saint-Venant water depth h [m] and velocity (u,v) [m/s], porosity theta [-] and vegetation/friction coefficients. No original rain versus leafdrip detachment coefficients or erosion output confirmed. Do not reconstruct sediment module from a separate 2024 theoretical article and present as native original ASTERIX.

## 고운사 적용과 한계 및 최종 판정
**탈락** as complete original forest-canopy+2D rain/flow erosion engine: no native interception and erosion in demonstrable 2024/2025 flow release. Separate 2024 Ion et al. paper on Hairsine-Rose erosion equation does not prove production integration into downloadable 2025 ASTERIX binary/source. No build/bench test done, fail at source functionality screen.

## References
- Primary 2025: https://www.sciencedirect.com/science/article/pii/S1364815225000209
- Primary 2024 preprint with unambiguous 'Future Extensions': https://www.researchgate.net/publication/381652990_ASTERIX_Module_for_modelling_the_water_flow_on_vegetated_hillslopes
- Separate 2024 mathematical sediment paper: https://arxiv.org/abs/2408.12465
- Published code URL given in author paper: http://www.ima.ro/software/ASTERIX_flow_2D.tar.xz (not retrieved or built).
