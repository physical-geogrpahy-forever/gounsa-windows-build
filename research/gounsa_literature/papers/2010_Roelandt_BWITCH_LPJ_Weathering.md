# 서지정보
Roelandt, C., Goddéris, Y., Bonnet, M.-P., & Sondag, F. (2010). Coupled modeling of biospheric and chemical weathering processes at the continental scale. *Global Biogeochemical Cycles, 24*. DOI: 10.1029/2008GB003420.

# 이 논문을 찾은 이유
고운사에서 LPJ-GUESS의 식생 상태를 화학풍화에 명시적으로 연결할 published coupling이 존재하는지 확인하기 위해 검색했다. 특히 단순 runoff/temperature forcing을 넘어 식생의 호흡, 양분 흡수와 반환, PFT/NPP가 풍화에 들어가는 모델을 찾는 것이 목적이었다.

# 연구 유형
- 수치모델
- 동적식생모델과 반응수송 풍화모델 coupling

# 공간 구조
- 0.5도 격자 기반 continental application
- 각 격자에서 3개 수직층
  - L1 0-0.5 m
  - L2 0.5-1.5 m
  - L3 saprolite 1.5-6.5 m
- lateral geomorphic routing은 핵심이 아님

# 적용 환경
- Orinoco watershed
- tropical continental basin
- 비교선례로 temperate forest WITCH application을 계승

# 핵심 과정
- silicate mineral dissolution/precipitation
- soil/saprolite reactive transport
- hydrology and vertical drainage
- soil CO2 from belowground respiration
- cation uptake and return by vegetation
- PFT-dependent transpiration and rooting

# 식생 입력
- LPJ PFT distribution and fractional cover
- NPP
- living biomass and litter pools
- root-zone hydrology
- evapotranspiration
- belowground respiration
- biomass cation uptake
- aboveground litter return
- root litter return

# 핵심 식
B-WITCH는 LPJ-DGVM이 계산한 식생-수문-탄소 상태를 WITCH의 경계조건과 source/sink로 전달한다.

개념적 coupling:

```
LPJ
  PFT / NPP
  evapotranspiration
  soil water / drainage
  belowground respiration
  biomass turnover
        |
        v
B-interface
        |
        v
WITCH
  pCO2
  water content / flux
  cation uptake / return
  mineral dissolution / precipitation
        |
        v
chemical weathering flux
```

식생 양분 흡수는 NPP와 PFT cover에 비례하고, 층별 transpiration water use에 따라 L1/L2에 배분된다.

식물체가 고사하면:
- aboveground litter의 원소는 표층으로 반환
- root litter의 원소는 뿌리가 있던 층으로 반환

LPJ의 litter와 soil organic matter decomposition으로 계산된 belowground respiration이 soil CO2 생산률을 제공한다.

# 파라미터와 단위
원 논문의 풍화 reaction parameters는 WITCH 계보의 mineral-specific kinetics를 사용한다.
식생 coupling에서 필요한 상태:
- NPP
- PFT fractional cover
- layer water use
- runoff / drainage
- belowground respiration
- biomass elemental exchange

고운사 적용 시 실제 단위 mapping은 LPJ-GUESS 출력 정의와 함께 별도 구현표로 정리해야 한다.

# 원 논문의 구현 범위
원 논문은 LPJ를 1901-2002 기후로 먼저 구동한 후, 마지막 20년의 평균 수문, biomass exchange, belowground CO2를 WITCH forcing으로 사용했다. WITCH는 추가 구동하여 steady state dissolved flux를 계산했다.

따라서 published coupling은 명확하지만 산불 후 연별 succession을 그대로 추적하는 transient implementation은 아니다.

# 고운사에 직접 사용할 수 있는 부분
가장 중요한 published precedent:

```
dynamic vegetation model
 -> hydrology
 -> belowground respiration / soil CO2
 -> biomass nutrient uptake and return
 -> mechanistic chemical weathering model
```

특히 LPJ 계열을 직접 WITCH에 연결했다는 점에서 LPJ-GUESS와 가장 가까운 선례다.

고운사에서는 Hartmann의 단순 lithology/runoff/temperature forcing보다 식생 피드백을 더 완전하게 표현할 수 있는 핵심 계보로 사용한다.

# 새로운 coupling이 필요한 부분
고운사에서는 다음이 새 coupling이다.

```
LPJ-GUESS annual/daily transient states
 -> WITCH transient forcing
```

원 논문처럼 20년 평균 forcing을 쓰지 않고 산불 후 100년 동안 매년 또는 더 짧게 갱신하려면 새로운 coupling이다.

또한 WITCH dissolved weathering flux를 Landlab의 mobile-soil thickness production과 동일시하지 않는다.

# 한계
- 원 application은 tropical continental scale
- forcing은 20년 평균 후 steady-state WITCH
- mycorrhizal physiology와 explicit root exudates는 단순화
- published version에는 WITCH -> LPJ 양방향 feedback이 없음
- geomorphic bedrock-to-soil production thickness를 직접 출력하지 않음

# 최종 판정
- **채택: 고운사 식생-화학풍화 coupling의 핵심 published precedent**
- B-WITCH 전체를 그대로 복사하는 것이 아니라 coupling variables와 WITCH reaction framework를 고운사 transient 구조에 이식한다.
- LPJ-GUESS로 바꾸는 부분과 transient forcing은 새로운 coupling으로 명시한다.

# 참고 링크 / DOI
https://doi.org/10.1029/2008GB003420
