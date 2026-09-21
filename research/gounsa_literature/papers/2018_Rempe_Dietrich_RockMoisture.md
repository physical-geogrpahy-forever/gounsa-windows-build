# 서지정보
Rempe, D. M., & Dietrich, W. E. (2018). Direct observations of rock moisture, a hidden component of the hydrologic cycle. *Proceedings of the National Academy of Sciences, 115*(11), 2664-2669. DOI: 10.1073/pnas.1800141115.

# 이 논문을 찾은 이유
얕은 토양 아래의 weathered-bedrock water storage가 사면 식생과 hydrology를 실제로 지배하는지 확인하고, 고운사에서 H_AB와 root-access depth / hydrologic depth를 분리할 근거를 강화하기 위해 검토했다.

# 연구 유형
- multiyear hillslope field monitoring
- neutron-probe rock-moisture observations
- Critical Zone hydrology

# 공간 구조
- full forested hillslope
- thin soil
- saprolite
- weathered fractured bedrock
- water table
- fresh bedrock

# 적용 환경
- Rivendell hillslope, northern California
- seasonally dry old-growth forest
- argillaceous/fractured bedrock

# 핵심 과정
- infiltration
- rock-moisture storage
- deep vadose-zone water
- tree transpiration
- groundwater recharge
- streamflow partitioning

# 식생 입력
- deep-rooted forest
- seasonal tree water uptake

dynamic vegetation model은 아니다.

# 핵심 결과
Rock moisture는:
```
soil base
to
groundwater table
```
사이의 unsaturated weathered bedrock에 저장된다.

Seasonal cycle:
```
wet season:
rain -> rock moisture recharge

dry season:
trees -> rock moisture withdrawal
```

연간 강수의 최대 약 27%가 seasonal rock moisture로 저장될 수 있었다.

중요:
```
weathered-bedrock moisture
!=
soil moisture
```

그리고 weathered-bedrock distribution은 soil thickness와 독립적인 깊은 landscape state다.

# 고운사에 직접 사용할 수 있는 부분
고운사에서 다음을 분리할 강한 근거:
```
H_AB
Z_root
Z_weathered
rock moisture
soil moisture
```

즉:
```
Z_root > H_AB
```
를 허용한다.

Deep-root water uptake는 다시:
- transpiration
- drainage
- CO2/weathering
에 영향을 줄 수 있다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS에 bedrock-vadose reservoir를 추가하거나 외부 hydrology state로 전달하는 것은 새로운 coupling이다.

# 한계
- direct chemical-weathering-rate paper는 아님
- specific wet forest / lithology
- fire disturbance 없음

# 최종 판정
- **채택: rock-moisture / deep-root hillslope hydrology 핵심 field precedent**
- chemical weathering에는 hydrologic forcing source로 사용
- weathering coefficient source가 아님

# 참고 링크 / DOI
https://doi.org/10.1073/pnas.1800141115
