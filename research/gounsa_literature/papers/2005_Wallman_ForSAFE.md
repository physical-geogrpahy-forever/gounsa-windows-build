# 서지정보
Wallman, P., Svensson, M. G. E., Sverdrup, H., & Belyazid, S. (2005). ForSAFE—an integrated process-oriented forest model for long-term sustainability assessments. *Forest Ecology and Management, 207*(1-2), 19-36. DOI: 10.1016/j.foreco.2004.10.016.

# 이 논문을 찾은 이유
산림 식생성장, litter decomposition, hydrology, soil chemistry, mineral weathering이 하나의 published model에서 동적으로 feedback하는 사례를 확인하기 위해 검토했다.

# 연구 유형
- integrated process-oriented forest ecosystem model

# 공간 구조
- forest stand / layered soil profile

# 적용 환경
- forest ecosystem
- long-term forestry sustainability

# 핵심 과정
ForSAFE는 다음 계보를 결합한다.
- PnET tree growth
- DECOMP soil organic matter decomposition
- PULSE hydrology
- SAFE/PROFILE soil chemistry and weathering

# 식생 입력
- tree growth
- biomass allocation
- nutrient uptake
- litterfall
- decomposition
- transpiration / hydrology

# 핵심 식
구조적 coupling:

```
tree growth
 <-> nutrient availability / uptake
 -> litterfall
 -> decomposition / soil chemistry
 -> weathering environment
 -> nutrient supply
 -> tree growth
```

# 파라미터와 단위
각 submodel의 process parameters 사용. Weathering은 PROFILE 계보의 mineral-specific kinetics를 사용한다.

# 원 논문의 구현 범위
vegetation과 soil을 dynamic feedback으로 결합하는 forest ecosystem model.

# 고운사에 직접 사용할 수 있는 부분
식생이 chemical weathering에 들어가는 경로를:
- hydrology
- litter decomposition
- nutrient uptake
- soil chemistry
로 명시적으로 분리하는 강한 산림 선례.

# 새로운 coupling이 필요한 부분
PnET 대신 LPJ-GUESS를 사용하고 SAFE/PROFILE 또는 WITCH chemistry에 연결하는 것은 새로운 coupling이다.

# 한계
- 자체 tree-growth model이 있으므로 LPJ-GUESS와 그대로 중복 사용하면 안 됨
- geomorphic soil production / 2D landform change model이 아님

# 최종 판정
- 보조 채택
- 산림 vegetation-weathering feedback architecture의 핵심 비교모델

# 참고 링크 / DOI
https://doi.org/10.1016/j.foreco.2004.10.016
