# 서지정보
Hahm, W. J., Dralle, D. N., Sanders, M., Bryk, A. B., Fauria, K. E., Huang, M.-H., Hudson-Rasmussen, B., Nelson, M. D., Pedrazas, M. A., Schmidt, L., Whiting, J., Dietrich, W. E., & Rempe, D. M. (2022). Bedrock Vadose Zone Storage Dynamics Under Extreme Drought: Consequences for Plant Water Availability, Recharge, and Runoff. *Water Resources Research, 58*(4), e2021WR031781. DOI: 10.1029/2021WR031781.

# 이 논문을 찾은 이유
사면 식생이 weathered-bedrock water storage를 실제로 얼마나 소모하고, 그 feedback이 recharge/runoff를 어떻게 바꾸는지 확인하기 위해 검토했다.

# 연구 유형
- multiyear borehole field monitoring
- ecohydrology

# 공간 구조
- hillslope soil
- weathered bedrock vadose zone
- groundwater
- stream/spring runoff

# 적용 환경
- Rancho Venada, northern California Coast Range
- Mediterranean blue-oak savanna
- steeply dipping turbidites

# 핵심 과정
- rock-moisture storage
- root water uptake
- transpiration
- drought
- groundwater recharge
- runoff

# 식생 입력
- bedrock-rooted blue oaks
- transpiration
- tree water stress

# 핵심 결과
wet year:
```
647 mm precipitation
rock moisture replenished
~93 mm dry-season rock-moisture depletion
recharge + streamflow
```

drought years:
```
212 mm, 121 mm precipitation
winter rock-moisture gain ~54 mm, ~20 mm
```

storage가 완전히 회복되지 않아:
- tree water stress 증가
- sapflow 감소
- canopy dieback
- recharge/runoff 소실

즉:
```
vegetation water use
<-> bedrock vadose storage
<-> recharge/runoff
```
양방향 feedback이 실제 존재한다.

# 고운사에 직접 사용할 수 있는 부분
사면 풍화 hydrology에서 식생을 단순 water-loss scalar로 처리하기보다:

```
root-zone depth
rock-moisture storage capacity
annual recharge
seasonal withdrawal
```

을 분리할 근거다.

Chemical weathering 관점에서는 vegetation water uptake가:
- contact time
- drainage
- rock moisture
를 바꾸므로 W_chem에도 간접 피드백한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root water uptake를 C/Cr rock-moisture reservoir에 연결하는 것은 새로운 coupling이다.

# 한계
- chemical weathering 직접 측정 아님
- sedimentary mélange/turbidite site
- postfire 직접 없음

# 최종 판정
- **채택: vegetation-rock moisture-hillslope hydrology feedback**
- chemical-weathering hydrology interface의 핵심 보조근거

# 참고 링크 / DOI
https://doi.org/10.1029/2021WR031781
