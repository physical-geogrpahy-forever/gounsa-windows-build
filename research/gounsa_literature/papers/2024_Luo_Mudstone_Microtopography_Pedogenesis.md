# 서지정보
Luo, B., Li, J., Tang, J., Wei, C., Zhong, S., et al. (2024). Microtopography effects on pedogenesis in the mudstone-derived soils of the hilly mountainous regions. *Scientific Reports, 14*, 11998. DOI: 10.1038/s41598-024-62540-y.

# 이 논문을 찾은 이유
동아시아의 퇴적암 산지에서 summit-to-toeslope 위치가 water/material redistribution, chemical weathering, soil thickness를 어떻게 바꾸는지 확인하기 위해 검토했다.

# 연구 유형
- hillslope toposequence field study
- soil geochemistry/mineralogy
- pedogenesis analysis

# 공간 구조
soil profiles at:
- summit
- shoulder
- backslope
- footslope
- toeslope

# 적용 환경
- Sichuan Basin, China
- hilly mountainous region
- lacustrine mudstone parent material
- subtropical monsoon climate
- forest and cultivated landscapes in regional setting

# 핵심 과정
- surface runoff
- clay/material redistribution
- water redistribution
- chemical weathering
- soil profile development
- erosion/deposition
- slope-position control

# 식생 입력
dynamic vegetation model은 없다.

Study landscape includes forest/cropland and soil-organism effects are discussed, but vegetation type is not the primary controlled variable.

따라서 vegetation coefficient source가 아니라 East Asian sedimentary hillslope constraint다.

# 핵심 결과
downslope:
```
summit -> shoulder -> backslope -> footslope -> toeslope
```
방향으로 soil thickness가 증가하고 profile configuration이:
```
A-C -> A-B-C
```
로 발달했다.

Summit/shoulder:
- gravity/surface erosion removes weathered material
- fresh rock exposed
- soil development relatively weak

Footslope/toeslope:
- water and weathered materials accumulate
- contact time increases
- chemical weathering and pedogenesis stronger

그러나 saturation/poor aeration은 일부 mineral/weathering 및 organic-matter decomposition을 제한할 수 있으므로 downslope effect도 단순 단조법칙은 아니다.

# 고운사에 직접 사용할 수 있는 부분
동아시아 퇴적암 산지에서:

```
hillslope position
 -> erosion/deposition
 -> water retention/contact time
 -> chemical weathering
 -> profile development
```

의 직접 field evidence.

고운사에서는 topographic position을 단순 categorical multiplier로 쓰지 않고:
- erosion/deposition
- convergence/wetness
- residence time
를 state로 계산하는 근거가 된다.

# 새로운 coupling이 필요한 부분
Landlab/SWEHR flow and sediment state를:
- water residence
- mineral residence
- soil-profile state
로 전달하는 것은 NEW COUPLING이다.

# 한계
- mudstone, not sandstone
- cultivation influence at some lower-slope profiles
- dynamic vegetation model 없음
- rate law보다 weathering extent/pedogenesis 비교

# 최종 판정
- **채택: East Asian sedimentary-hillslope toposequence weathering constraint**
- slope-position effect를 hydrology/transport intermediates로 구현할 근거
- coefficient source는 아님

# 참고 링크 / DOI
https://doi.org/10.1038/s41598-024-62540-y
