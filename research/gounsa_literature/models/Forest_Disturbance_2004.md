# Forest disturbance model lineage

## 핵심 기준 논문
Istanbulluoglu et al. (2004), Modeling of the interactions between forest vegetation, disturbances, and sediment yields.

## 왜 별도 계보로 보존하는가
고운사에서 산불 이후 모든 vegetation effect를 하나의 recovery factor로 묶지 않기 위한 핵심 published precedent다.

## 분리된 과정
- fire-induced water repellency
- understory surface roughness/protection
- overstory root cohesion
- gully erosion
- shallow landslide and debris-flow response

## 핵심 설계
`surface protection recovery != root-strength recovery`

## 고운사 적용
LPJ-GUESS에서 얻는 지상부와 root pools를 별도 경로로 geomorphic model에 전달한다.

## 새로운 coupling
LPJ-GUESS PFT별 biomass -> Manning roughness 또는 root cohesion 변환은 원 모델에 없으므로 새로운 coupling이다.

## 관련 논문
- ../papers/2004_Istanbulluoglu_ForestDisturbanceSediment.md
- ../papers/2019_Lehmann_STEP_TRAMM_RootDecayRegrowth.md

## 판정
- 산불 후 recovery architecture: 채택
