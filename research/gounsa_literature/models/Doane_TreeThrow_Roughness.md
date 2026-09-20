# Doane tree-throw / hillslope-roughness lineage

## 핵심 논문
- Doane et al. (2021). Topographic roughness on forested hillslopes: A theoretical approach for quantifying hillslope sediment flux from tree throw.
- Doane et al. (2023). Hillslope roughness reveals forest sensitivity to extreme winds.
- Doane et al. (2024). Topographic roughness as an emergent property of geomorphic processes and events.

## 모델 계보
2021: tree throw contribution to hillslope sediment flux를 topographic roughness로 정량화.
2023: tree-throw frequency를 extreme-wind sensitivity와 연결.
2024: stochastic roughening events와 creep-like smoothing의 경쟁으로 roughness를 일반화.

## 고운사에서의 역할
사면확산을 하나의 biomass-modified D로 처리하지 않고
q_hill = q_creep + q_tree_throw
로 분해할 근거.

## LPJ-GUESS 연결
DBH, cohort density, mortality, disturbance forcing을 tree-throw event rate로 연결할 수 있으나 이는 원 논문 기능이 아니다.

## 새로운 coupling
LPJ-GUESS woody cohort -> uprooting/tree-throw probability -> sediment flux는 **새로운 coupling**이다.

## 판정
tree-throw 모듈의 핵심 계보.
