# REWTCrunch model lineage

## 핵심 논문
- Roque-Malo, Druhan & Kumar (2022). REWTCrunch: A modeling framework for vegetation induced reactive zone processes in the Critical Zone. JGR Biogeosciences 127, e2021JG006562.

## 모델 구조
multilayer canopy/root ecohydrology, root exudation, reactive transport를 결합한다.

## 핵심 coupling
RootBiomass(z,t) -> RootExudation -> microbial/chemical reactions -> mineral dissolution.

## 고운사에서의 역할
LPJ-GUESS FineRootC의 수직분포를 C/Cr chemical weathering에 연결할 가장 직접적인 process-model 선례 중 하나.

## 한계
geomorphic LEM이 아니며 mineral dissolution flux를 soil/regolith thickness production으로 직접 출력하지 않는다.

## 새로운 coupling
mineral dissolution을 R->C 또는 C/Cr->AB mass production으로 변환하는 것은 **새로운 coupling**이다.

## 판정
화학풍화 보조모듈 채택 후보.
