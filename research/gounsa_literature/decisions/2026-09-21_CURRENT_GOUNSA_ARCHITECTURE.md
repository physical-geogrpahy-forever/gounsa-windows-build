# 결정: 현재 고운사 통합모델 구조

날짜: 2026-09-21

## 목적
식생, 수문, 토양과 풍화층, 침식과 퇴적, 지형이 상호작용하는 Eco-Geo-Hydro 모델을 구축한다.

## 현재 고정 구조
- 식생과 생태수문: LPJ-GUESS 계열
- vertical profile: R, C/Cr, AB 분리
- root-accessible depth와 mobile soil thickness 분리
- coarse fraction과 fire spall 상태 추적
- 최종 유수침식 엔진은 아직 확정하지 않음

## 최종 유수침식 엔진 조건
SYSTEM.md의 기준을 유지한다.
```text
genuine 2D
mountain/steep forest
quantitative vegetation state
interrill/rill 또는 rainfall/flow separation
```
COPLAS와 MUSLE는 최종근거에서 제외한다.

## vertical profile
```text
R -> C/Cr -> AB
```
- R: 비교적 신선한 기반암
- C/Cr: 풍화된 기반물질
- AB: 물리적으로 이동 가능한 상부토양

고운사에서는 뿌리가 C/Cr까지 접근할 수 있으므로 Z_root > H_AB를 허용한다.

## hydrology
상부토양과 풍화층의 수분저장을 분리하는 방향을 유지한다.
```text
W_AB
W_C
```
Lapides et al. (2024)이 직접적인 LPJ-GUESS 선례다.

## weathering
R->C/Cr와 C/Cr->AB를 서로 다른 경계과정으로 처리한다. Pelletier 계열은 전자, root fracture와 tree throw 등은 후자의 후보근거다.

## coarse fraction
최소한 CF_surface, CF_AB, CF_C를 구분하고 가능하면 fine/coarse mass 자체를 추적한다.

## fire spall
별도 provenance의 coarse reservoir로 두고 생성, 이동, 잔류/armour를 분리한다.

## 식생과 지형
COPLAS의 site-normalized biomass 식은 사용하지 않는다.
- canopy: LAI -> vegetation cover/FPC -> geomorphic protection
- root: absolute quantitative root state -> erodibility
- litter: litter mass 또는 cover -> flow resistance

논문에 없는 연결은 새로운 coupling으로 표시한다.

## 질량보존
weathering, soil production, erosion, deposition, spall generation과 transport는 mass transfer로 처리한다.

## 시간척도
- 일 또는 사건: 식생, 수문, 유출, 침식, 퇴적물 이동
- 연 또는 geomorphic step: 풍화전선과 soil-profile development
- 장기: landscape evolution

## 미해결 핵심
- 최종 genuine-2D mountain erosion engine
- root -> erodibility 최종식
- litter -> flow resistance 최종식
- C/Cr->AB 생산률
- coarse-fraction hydrology
- fire-spall entrainment와 armour 함수
