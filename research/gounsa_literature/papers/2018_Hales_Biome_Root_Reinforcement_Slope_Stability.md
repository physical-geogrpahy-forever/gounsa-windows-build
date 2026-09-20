# 서지정보
Hales, T. C. (2018). *Modelling biome-scale root reinforcement and slope stability*. Earth Surface Processes and Landforms, 43(10), 2157-2166. DOI: 10.1002/esp.4381.

# 이 논문을 찾은 이유
LPJ-GUESS의 root biomass를 shallow-landslide mechanics의 root reinforcement로 연결할 때 필요한 biome-scale mechanistic bridge를 찾기 위해 검토했다.

# 연구 유형
- mechanistic root-reinforcement/slope-stability model

# 공간 구조
- biome/hillslope parameterization
- slope stability mechanics

# 적용 환경
- vegetated slopes across biomes
- mountain shallow-landslide relevance

# 핵심 과정
- root distribution
- root tensile/material properties
- root reinforcement
- slope stability

# 식생 입력
- root distributions
- root material strength/properties
- vegetation/biome-dependent root traits

# 핵심 식
이 세션에서 exact full equation set은 저장하지 않았으므로 원문을 직접 참조한다. 핵심 pathway:
```
root biomass / root distribution
-> root geometric and mechanical traits
-> root reinforcement
-> slope stability
```

# 파라미터와 단위
root cohesion/reinforcement and root-distribution/material-property parameters. exact units는 원문 기준.

# 원 논문의 구현 범위
biome-scale root reinforcement의 magnitude와 variability를 slope stability에 연결한다.

# 고운사에 직접 사용할 수 있는 부분
```
LPJ-GUESS FineRootC
-> root distribution / architecture
-> c_r
-> factor of safety
```
의 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC에서 실제 root diameter distribution, RAR, tensile strength를 생성하는 구체적 conversion은 **새로운 coupling 또는 별도 문헌식 필요**.

# 한계
유수침식 Ki/Kr와 shallow-landslide root cohesion을 동일 parameter로 취급해서는 안 된다.

# 최종 판정
**채택: shallow-landslide root-reinforcement bridge.**

# 참고 링크 / DOI
10.1002/esp.4381
