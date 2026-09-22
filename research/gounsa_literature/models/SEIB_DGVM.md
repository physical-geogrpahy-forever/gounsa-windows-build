# SEIB-DGVM model lineage

## 목적
30 m x 30 m virtual forest 내부를 1 m 격자로 나누고 individual trees의 공간경쟁과 생지화학 과정을 결합하는 spatially explicit individual-based DGVM.

## 기본 구조
Sato et al. 2007.
- virtual forest: 30 m x 30 m
- internal simulation cells: 1 m x 1 m
- individual woody PFTs plus grasses
- individual spatial competition

후속 계보에서:
- physical/physiological processes: daily
- trunk growth: monthly
- establishment, mortality, disturbance including wildfire: annual
- fine-root and litter turnover represented
- root/leaf/trunk carbon pools expanded in later variants
- SPITFIRE variant available

## 공개 코드 상태
2026-06 updated official download page:
- latest listed version 3.21
- base distribution is a single virtual-forest point simulation
- multi-plot / regional calculation information exists in code>mpi
- plot size can be changed in configuration

## 고운사 장점
1. 30 m geomorph grid와 virtual forest 기본 크기가 정확히 맞음.
2. 내부 1 m 공간에서 개체목 경쟁을 명시적으로 계산.
3. LPJ-GUESS보다 within-cell horizontal heterogeneity가 훨씬 현실적.
4. daily physiology, fine-root biomass, litter, wildfire와 post-disturbance succession을 함께 보유.

## 고운사 핵심 문제
'30 m virtual forest가 공간명시적'이라는 말은 각 30 m plot 내부의 개체 위치가 명시적이라는 뜻이다.

공개 point version 자체가 고운사 4454개 30 m cell 사이의:
- seed exchange
- migration
- lateral ecological interaction
을 자동 제공한다고 볼 수 없다.

따라서 LPJ-GUESS의 landscape-scale cell independence 문제와 다른 형태의 공간단절이 남는다.

## 필요한 새 coupling
- multiple 30 m plots on catchment raster
- explicit inter-plot seed dispersal
- geomorphic soil depth/moisture feedback
- root/litter -> erosion/root mechanics interface

## 판정
강한 2순위 후보.
셀 내부 식생구조는 매우 뛰어나지만 catchment-wide spatial succession을 새로 연결해야 한다.

## 관련 논문
- papers/2007_Sato_SEIB_DGVM.md
