# 서지정보
Tune, A. K., Druhan, J. L., Wang, J., Bennett, P. C., & Rempe, D. M. (2020). Carbon dioxide production in bedrock beneath soils substantially contributes to forest carbon cycling. *Journal of Geophysical Research: Biogeosciences, 125*(12), e2020JG005795. DOI: 10.1029/2020JG005795.

# 이 논문을 찾은 이유
균근을 제외한 상태에서 deep-root-associated respiration이 토양 아래 weathered bedrock에서 실제로 CO2 source를 만들고, 그 CO2가 water-rock interaction과 weathering에 기여할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- field monitoring
- gas + water sampling in fractured bedrock
- forest Critical Zone study

# 공간 구조
- thin soil
- weathered fractured bedrock
- 4-8 m deep CO2 production zone
- hillslope vadose zone

# 적용 환경
- Northern California old-growth forest
- thin soils <0.5 m
- deeply rooted forest
- fractured bedrock

# 핵심 과정
- below-soil carbon cycling
- bedrock-zone respiration
- CO2 production
- gas flux to soil
- CO2 dissolution in water
- DIC export
- potential carbonic-acid weathering

# 식생 입력
- deep rooting
- root-associated labile carbon
- root water use
- belowground carbon cycling

균근은 고운사 production에 사용하지 않는다.

# 핵심 결과
weathered bedrock 4-8 m depth에서 substantial CO2 production을 관측했다.

이 deep CO2 production은:
- land-surface CO2 efflux의 일부를 공급
- groundwater로 이동하는 DIC의 큰 부분에 기여
- 빠른 vadose-zone water transport 시 water에 용해되어 water-rock interaction을 촉진

할 수 있었다.

논문은 bedrock respiration이:
```
soil-only carbon box
```
로 설명되지 않는다고 결론낸다.

# 파라미터와 단위
- CO2 gas concentration/flux
- depth [m]
- water transport
- DIC flux
- bedrock moisture
- seasonal dynamics

# 원 논문의 구현 범위
deep forest rhizosphere가 soil 아래 fractured bedrock에서도 active carbon source임을 현장자료로 정량화한다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요한 non-mycorrhizal structural constraint.

```
root access depth
>
soil thickness
```

를 허용해야 한다.

그리고:
```
deep-root-associated C turnover
 -> bedrock CO2 source
 -> water chemistry / weathering potential
```
경로를 chemical-weathering interface에 남길 근거다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS에서:
- deep root biomass
- root turnover
- root respiration
을 bedrock-zone CO2 production profile로 바꾸는 것은 새 coupling이다.

# 한계
- CO2 production paper이며 mineral weathering flux 자체가 주 출력은 아님
- carbon source가 root respiration만인지 완전히 분리되지 않음
- site-specific bedrock/climate

# 최종 판정
- **채택: deep-root CO2 source의 핵심 현장근거**
- Osorio-Leon 2025 RTM의 선행 process evidence
- direct coefficient transfer 금지

# 참고 링크 / DOI
https://doi.org/10.1029/2020JG005795
