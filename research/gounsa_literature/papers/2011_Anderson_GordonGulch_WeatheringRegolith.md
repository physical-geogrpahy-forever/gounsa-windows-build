# 서지정보
Anderson, S. P., Anderson, R. S., Hinckley, E.-L. S., Kelly, P., & Blum, A. (2011). Exploring weathering and regolith transport controls on Critical Zone development with models and natural experiments. *Applied Geochemistry, 26*, S3-S5. DOI: 10.1016/j.apgeochem.2011.03.014.

# 이 논문을 찾은 이유
사면방향에 따른 미기후와 식생 차이가 weathering front, saprolite, mobile regolith에 서로 다르게 나타나는지 확인하기 위해 검토했다.

# 연구 유형
- natural experiment
- simple numerical modeling
- Critical Zone field synthesis

# 공간 구조
- opposing north- and south-facing hillslopes
- weathering front
- saprolite
- mobile regolith
- hillslope transport

# 적용 환경
- Gordon Gulch, Boulder Creek Critical Zone Observatory
- Colorado Front Range
- forested montane hillslopes
- aspect-driven microclimate contrast

# 핵심 과정
- weathering-front advance
- mobile-regolith production
- hillslope sediment transport
- slope-aspect climate forcing
- regolith-profile evolution

# 식생 입력
dynamic vegetation model은 아니다.

Aspect contrast에는:
- denser lodgepole-pine vegetation on cooler/wetter north-facing slopes
- sparser ponderosa/grass vegetation on warmer/drier south-facing slopes
같은 vegetation/environment contrast가 포함된다.

따라서 vegetation을 climate/aspect와 완전히 분리한 인과실험은 아니다.

# 핵심 결과
north-facing slopes에서:
- weathering front가 더 깊음
- saprolite가 더 strongly decayed

south-facing slopes보다 Critical Zone architecture가 더 발달했다.

논문은 weathering-front advance, mobile-regolith production, regolith transport의 simple numerical models로 이 차이를 해석한다.

핵심 구조:

```
aspect
 -> radiation / temperature / moisture
 -> vegetation + hydrologic contrast
 -> weathering-front advance
 -> saprolite state
 -> mobile-regolith production
 -> surface transport
```

# 파라미터와 단위
이 짧은 paper의 model coefficients를 고운사에 직접 복사하지 않는다.

Relevant states:
- weathering-front depth [m]
- mobile-regolith thickness [m]
- soil-production rate
- sediment-transport rate
- aspect-dependent climatic forcing

# 원 논문의 구현 범위
Critical Zone profile evolution을 weathering-front advance + soil production + surface transport로 분해한 simple numerical experiment.

# 고운사에 직접 사용할 수 있는 부분
중요한 구분:

```
weathering front depth
!=
mobile soil thickness
```

식생/미기후 차이가 deep weathered rock에는 강하게 나타나더라도 mobile soil thickness 또는 sediment transport가 같은 방식으로 반응한다고 가정하면 안 된다.

고운사에서는:
- C/Cr weathering-front state
- mobile A/B soil H
를 분리할 근거가 된다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation/hydrology state를 weathering-front velocity에 연결하는 것은 새로운 coupling이다.

# 한계
- short synthesis paper
- aspect, climate, vegetation effects가 공변
- 직접적인 FineRootC-to-weathering equation 없음
- sandstone-specific 아님

# 최종 판정
- **채택: aspect-driven hillslope Critical Zone architecture 핵심 precedent**
- weathering front와 mobile soil을 분리할 강한 근거
- vegetation multiplier source가 아님

# 참고 링크 / DOI
https://doi.org/10.1016/j.apgeochem.2011.03.014
