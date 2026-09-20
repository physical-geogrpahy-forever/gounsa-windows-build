# LAPSUS model lineage

## 범위
고운사 문헌검토에서 LAPSUS와 vegetation-density coupling을 정리한다.

## 기본 구조
Baartman et al. (2018) 검토에서 다음 구조를 확인했다.

- transport capacity: `C = gamma Q^m Lambda^n`
- detachment capacity: `D = K Q Lambda`
- sedimentation capacity: `T = P Q Lambda`

vegetation density V가 K, P, infiltration에 영향을 준다.

## vegetation state
- absolute vegetation density, g m-2
- dynamic growth, mortality, dispersal

## 고운사에 사용할 수 있는 부분
- absolute vegetation density를 사용하는 선례
- detachment와 deposition parameter를 분리하는 구조

## 제한
Baartman et al. (2018)의 5/20 g m-2 breakpoint와 매우 강한 K/P scaling은 연구설정 의존적이다. 고운사에 직접 이식하지 않는다.

## 새로운 coupling
LPJ-GUESS PFT별 biomass에서 K/P를 산정하는 식을 만들 경우 새로운 coupling이다.

## 관련 논문
- ../papers/2018_Baartman_LAPSUSVegetationPatterning.md

## 판정
- 구조 참고
- 직접 파라미터 이식은 탈락
