# VED vegetation erosion dynamics model

## 핵심 논문
- Wang et al. (2024). Modeling soil erosion dynamic processes along hillslopes with vegetation impact across different land uses on the Loess Plateau of China. CATENA 243, 108202.

## 모델 구조
hillslope erosion dynamics에서 soil detachment capacity와 sediment transport capacity를 모두 vegetation effect와 함께 계산한다.

## 식생형 차이
woodland, grassland, farmland가 서로 다른 vegetation-decay response를 보였으며, 현재 채팅에서 woodland > grassland > farmland 순의 effect가 확인되었다.

## 고운사에서의 역할
- 목본과 초본에 동일한 erosion coefficient를 적용하면 안 된다는 수치모델 선례
- detachment와 transport capacity에 식생효과를 별도로 넣는 구조적 후보

## 한계
원래 vegetation 입력이 biomass보다 cover 중심이다.
LPJ-GUESS RootC/AGB/PFT를 VED coefficient로 바꾸는 것은 **새로운 coupling**이다.

## 판정
보조근거. 최종 engine으로 확정하지 않음.
