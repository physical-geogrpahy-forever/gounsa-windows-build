# SCION-FLORA model lineage

## 핵심 논문
- Gurung et al. (2024). Geographic range of plants drives long-term climate change. Nature Communications 15, 1805.

## 모델 구조
SCION의 deep-time carbon-weathering framework에 FLORA dynamic vegetation productivity를 결합한다.

## 핵심 coupling
현재 채팅에서 복구된 구조:
f_biota = 0.0005 * NPP + f_minbiota * RCO2^r
f_minbiota = 0.32

## 고운사에서의 역할
DGVM NPP를 chemical-weathering modifier로 직접 쓰는 최근 published precedent.

## 한계
deep-time global model이다. 고운사 soil-production thickness 계수로 직접 이식 금지.

## 새로운 coupling
LPJ-GUESS NPP를 고운사 R->C 또는 C/Cr weathering rate에 연결하는 것은 **새로운 coupling**이다.

## 판정
보조근거.
