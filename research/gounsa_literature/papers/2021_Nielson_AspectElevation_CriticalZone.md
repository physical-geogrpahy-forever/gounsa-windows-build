# 서지정보
Nielson, T., Bradford, J., Holbrook, W. S., & Seyfried, M. (2021). The Effect of Aspect and Elevation on Critical Zone Architecture in the Reynolds Creek Critical Zone Observatory: A Seismic Refraction Study. *Frontiers in Water, 3*, 670524. DOI: 10.3389/frwa.2021.670524.

# 이 논문을 찾은 이유
산지에서 slope aspect, snow/water delivery, vegetation density와 weathering-zone depth가 어떻게 연결되는지 독립적인 geophysical field site로 확인하기 위해 검토했다.

# 연구 유형
- seismic refraction field study
- paired hillslope natural experiment

# 공간 구조
- north/south-facing hillslopes
- 300 m elevation gradient
- soil to weathered/fresh bedrock

# 적용 환경
- Reynolds Creek Critical Zone Observatory, Idaho
- snow-dominated mountain watershed

# 핵심 과정
- snow accumulation
- meltwater pulse
- subsurface water penetration
- soil moisture
- bedrock weathering depth
- vegetation density

# 식생 입력
dynamic vegetation model 없음.

Observed:
- denser vegetation on wetter/cooler north-facing slopes
- vegetation may contribute to soil retention or biological weathering

# 핵심 결과
north-facing slopes:
- more persistent snowpack
- deeper water delivery
- commonly deeper weathering

weathering-zone thickness also increased with decreasing elevation, interpreted in relation to higher soil moisture.

저자들은 primary interpretation으로:
```
snowpack / moisture delivery
 -> deeper weathering
```
을 제시하지만, denser vegetation contribution을 caveat로 남긴다.

# 고운사에 직접 사용할 수 있는 부분
식생효과와 hydrologic effect를 분리해서 모델링해야 한다는 근거.

```
vegetation state
 -> ET / soil retention / root effects

water delivery
 -> weathering depth
```

를 한 multiplier로 합치지 않는다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS + site hydrology로 water delivery and vegetation effects를 separately resolve하는 것은 새로운 coupling.

# 한계
- granite-like mountain CZ, not Gounsa sandstone
- no process vegetation model
- seismic weathering depth, not annual production flux

# 최종 판정
- **보조 채택: aspect-hydrology-vegetation weathering-depth constraint**
- current aspect itself is not a weathering coefficient

# 참고 링크 / DOI
https://doi.org/10.3389/frwa.2021.670524
