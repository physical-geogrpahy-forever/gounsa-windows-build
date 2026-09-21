# 서지정보
Pedrazas, M. A., Hahm, W. J., Huang, M.-H., Dralle, D. N., Nelson, M. D., Breunig, R. E., Fauria, K. E., Bryk, A. B., Dietrich, W. E., & Rempe, D. M. (2021). The relationship between topography, bedrock weathering, and water storage across a sequence of ridges and valleys. *Journal of Geophysical Research: Earth Surface, 126*(4), e2020JF005848. DOI: 10.1029/2020JF005848.

# 이 논문을 찾은 이유
hillslope length/relief가 weathering-front depth와 rock-moisture storage를 실제 ridge-valley sequence에서 어떻게 조직하는지 확인하기 위해 검토했다.

# 연구 유형
- deep drilling
- downhole logging
- geochemistry
- porosity characterization
- neutron-probe moisture monitoring

# 공간 구조
- multiple ridges and valleys
- ridge to channel
- shallow and deep weathering fronts

# 적용 환경
- Northern California Coast Ranges
- mountainous forested sedimentary terrain

# 핵심 과정
- ridge-valley spacing
- fracturing
- oxidation/weathering fronts
- bedrock water storage
- seasonal moisture dynamics
- erosion-weathering feedback

# 식생 입력
forested setting이며 dynamic vegetation model은 아니다.

Root-zone relevance는 weathered-bedrock moisture storage를 통해 해석한다.

# 핵심 결과
두 개의 weathering fronts를 확인.

Shallow front:
```
~7 m below ridge
```
에서 pervasive fracturing and oxidation extent와 대응.

Deeper front:
- similar-spacing ridges: 약 11 m
- ridge-valley spacing이 거의 2배인 ridge: 약 17.5 m

즉:
```
hillslope length / relief
 -> deeper weathered structure
```
가 관측된다.

Seasonally dynamic moisture storage depth는 shallow weathering front와 대체로 일치했다.

Under channels, the two fronts converge near the surface.

# 고운사에 직접 사용할 수 있는 부분
Ferrier & Perron 2020의:
```
hillslope length matters
```
를 field data로 강화한다.

또:
```
weathered depth
 -> rock-moisture storage
 -> vegetation water access
```
reverse feedback을 지지한다.

따라서 divide-channel distance와 local relief를 inherited Z_weathered prior에 활용할 가능성이 있다.

# 새로운 coupling이 필요한 부분
DEM-based hillslope length/relief를:
- initial Z_weathered prior
- rock-moisture storage capacity
로 연결하는 것은 NEW COUPLING이다.

# 한계
- site-specific sedimentary terrain
- direct vegetation manipulation 없음
- long-term inherited weathering structure
- annual production law 없음

# 최종 판정
- **핵심 채택: hillslope length-weathering depth-water storage field constraint**
- inherited profile initialization과 rock-moisture capacity 설계에 유용
- coefficient direct transfer 금지

# 참고 링크 / DOI
https://doi.org/10.1029/2020JF005848
