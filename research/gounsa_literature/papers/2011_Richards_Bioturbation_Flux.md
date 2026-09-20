# 서지정보
Richards, P. J., Hohenthal, J. M., & Humphreys, G. S. (2011). *Bioturbation on a south-east Australian hillslope: estimating contributions to soil flux*. Earth Surface Processes and Landforms, 36(9), 1240-1253. DOI: 10.1002/esp.2149.

# 이 논문을 찾은 이유
LPJ-GUESS와 explicit tree-throw/root-growth modules가 계산하지 않는 soil-fauna bioturbation이 residual background flux에서 무시 가능한지 확인하기 위해 검토했다.

# 연구 유형
- direct field soil-flux measurement
- wildfire-affected hillslope

# 적용 환경
- southeast Australia
- postfire hillslope

# 핵심 과정
- ant mounding
- vertebrate scraping
- tree throw
- direct biogenic downslope transport

# 정량 결과
Mean direct flux contributions included approximately:
- vertebrate scraping: 57.0 +/- 89.4 g m^-1 yr^-1
- ant mounding: 36.4 +/- 66.0 g m^-1 yr^-1

Tree throw is individually large but can be less important where events are rare.

The paper estimates tree throw would dominate mid-slope biotic flux only if frequency reaches roughly:
```
2-3 events ha^-1 yr^-1
```

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS does not simulate ants, burrowing fauna or all small-scale soil churning.

Therefore:
```
explicit roots + explicit tree throw
```
does **not** imply:
```
all biogenic creep is resolved
```

A nonzero residual background term remains physically defensible.

# 새로운 coupling이 필요한 부분
No attempt should be made to transfer Australian fauna flux values directly to Gounsa.

They are evidence for an omitted process class, not Gounsa coefficients.

# 한계
- large uncertainty
- Australian fauna/community
- postfire landscape
- flux partly controlled by spatial ecological distribution rather than slope alone

# 최종 판정
**채택 as evidence that residual bioturbation remains after explicit tree throw/root-growth modules.**

# 참고 링크 / DOI
https://doi.org/10.1002/esp.2149
