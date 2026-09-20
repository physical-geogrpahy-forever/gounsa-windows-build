# 결정: strict 2D + 산지 + quantitative vegetation + process separation

날짜: 2026-09-21

## 결정 내용
현재 이 채팅에서 검토한 범위에서는 다음 네 조건을 모두 만족하는 **단일 published model은 확인되지 않았다**.

```
1. genuine 2D surface flow / sediment routing
2. mountain or steep forest/postfire applicability
3. root biomass, RLD, live/dead root mass, litter biomass 등 quantitative vegetation state
4. interrill/rill 또는 rainfall-driven/flow-driven process separation
```

## 확인된 두 모델군

### A. genuine 2D engine
- Wu et al. 2020
- PSEM_2D
- Iber+ 2024
- McGuire rill-network lineage
- OpenLISEM
- SERGHEI-SE

공통 약점:
dynamic root biomass/RLD 직접연결이 없거나, root cohesion이 external/cover-weighted state이다.

### B. quantitative vegetation -> erosion resistance
- WEPP
- Mao et al. 2010 VIC-WEPP
- Gould et al. 2016 wildfire mountain application
- PROMET/Waldmann
- ELM-Erosion
- DANSAT/ANSWERS-2000 lineage

공통 약점:
genuine 2D hillslope surface hydraulics를 해결하지 않는다.

## 의미
고운사에서 최종적으로 두 모델군을 결합하면 그것은 기존 단일 published model이 아니라 **새로운 coupling**이다.

## 현재 역할 구분
- 2D hydraulics/erosion skeleton: Wu, Iber+, PSEM_2D, SERGHEI-SE 등에서 평가
- quantitative vegetation bridge: WEPP, Mao, PROMET, ELM-Erosion 등에서 평가

## 재검토 금지
이미 끝난 “Wu vs WEPP 중 하나를 고르는 문제”로 되돌아가지 않는다.
두 계보의 역할은 다르다.
