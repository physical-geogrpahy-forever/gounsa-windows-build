# Ion, Marinescu, & Cruceanu (2024): vegetated-hillslope Saint-Venant / Hairsine-Rose erosion

## 서지정보
Ion, S., Marinescu, D., & Cruceanu, S.-G. (2024). *Water flow model on vegetated hillslopes with erosion*. arXiv:2408.12465. https://arxiv.org/abs/2408.12465

## 검색 목적
식생 영향이 물과 유사수지의 동일 2D 원본 코드에 동시 포함된 산림 경사지 연구 확인.

## 연구유형, 공간구조
수학적/수치방법론 2D porous/extended Saint-Venant + multiple-class Hairsine-Rose sediment model. Numerical experiments of vegetation distributions and soil erosion, flash floods, dams; not a verified field-calibrated postfire Korean steep forest erosion model.

## 핵심 프로세스 및 식생
Vegetation represented by spatial porosity and drag/resistance in fluid momentum. Multi-class sediment erosion and deposition described. **No positive verification native LAI-driven canopy interception, dynamic canopy storage, throughfall, explicit leaf-drop kinetic energy** from this abstract. Mathematical development should not be conflated with 2025 ASTERIX *Water Flow Module* published software which previously said sediment was future extension.

## 원본 검증 범위
Publication abstract + software provenance cross-check only. No actual full integrated erosion source archive validated, compile/run or soil mass/timestep verification. Cannot declare native software requirements passed merely because mathematical paper mentions 'accompanying software'.

## 고운사 coupling
Canopy LAI interception + direct vs leafdrip kinetic energy and soil production/LPJ dynamic state would be **new coupling** if implemented. Time-scale and mass conservation independently unverified.

## 최종 판정
**원본 일체형 엔진으로는 탈락.** Equation-level literature optional only. Independent code availability and primary vegetation canopy physics absent/unconfirmed.

## Sources
https://arxiv.org/abs/2408.12465
https://www.sciencedirect.com/science/article/pii/S1364815225000209
https://www.researchgate.net/publication/381652990_ASTERIX_Module_for_modelling_the_water_flow_on_vegetated_hillslopes
