# 서지정보
Ding, L., Fu, S., Liu, B., Yu, B., Zhang, G., & Zhao, H. (2020). *Effects of Pinus tabulaeformis litter cover on the sediment transport capacity of overland flow*. Soil and Tillage Research, 204, 104685. DOI: 10.1016/j.still.2020.104685.

# 이 논문을 찾은 이유
forest litter가 detachment뿐 아니라 sediment transport capacity를 직접 줄이는지, 그리고 litter accumulation amount에서 cover를 정량적으로 계산하는 기존 계보를 실제 pine litter 실험이 사용하는지 확인하기 위해 검토했다.

# 연구 유형
- laboratory flume experiment
- empirical transport-capacity equations

# 공간 구조
- flume/plot

# 적용 환경
- Pinus tabulaeformis needle litter
- overland flow on litter-covered slope

# 핵심 과정
- litter accumulation -> litter cover
- hydraulic resistance
- overland-flow sediment transport capacity

# 식생 입력
Litter cover treatments:
- 0%
- 5%
- 10%
- 20%
- 30%
- 50%
- 70%

The study explicitly notes that direct cover measurement is time-consuming and therefore litter cover is commonly calculated from litter accumulation amount, citing:
- Gregory 1982
- Pannkuk & Robichaud 2003
- Smets et al. 2008

# 핵심 식 / 결과
`T_c` decreases exponentially with litter cover.

Mean reduction in sediment transport capacity relative to bare conditions:
- 5% cover: about 32%
- 10%: 45%
- 20%: 56%
- 30%: 64%
- 50%: 75%
- 70%: 82%

The best practical predictors include:
- unit discharge
- slope gradient
- litter cover

The paper also finds unit stream power can predict transport capacity without an explicit litter-cover term, because the hydraulic effect of litter is partly expressed through the flow state.

# 파라미터와 단위
- sediment transport capacity `T_c`: kg m^-1 s^-1
- unit discharge
- slope gradient
- litter cover fraction/percent
- litter accumulation mass used to establish cover

# 원 논문의 구현 범위
This is not only a Manning-roughness study.
It establishes that exposed pine litter also changes the sediment-transport side of erosion.

# 고운사에 직접 사용할 수 있는 부분
Together with Gregory 1982 and Pannkuk & Robichaud 2003:

```
SurfaceLitter mass
 -> litter cover
 -> altered hydraulics
 -> lower transport capacity / detachment response
```

This supports a separate surface-litter state even if rainfall detachability and flow transport are represented by different terms.

# 새로운 coupling이 필요한 부분
LPJ-GUESS SurfaceLitC -> dry litter mass -> cover/geometry -> the 2D engine's hydraulic and sediment terms is a **new coupling**.

Do not automatically apply the empirical Pinus tabulaeformis transport-capacity coefficients to Gounsa.

# 한계
- numerical landscape model 아님
- one pine litter type
- controlled flume conditions
- transport-capacity response is not identical to rainfall detachability

# 최종 판정
- **채택: pine litter cover -> sediment-transport response evidence**
- important companion to the postfire Pannkuk & Robichaud litter bridge

# 참고 링크 / DOI
https://doi.org/10.1016/j.still.2020.104685
