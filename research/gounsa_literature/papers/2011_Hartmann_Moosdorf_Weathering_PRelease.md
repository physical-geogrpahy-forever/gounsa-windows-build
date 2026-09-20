# 서지정보
Hartmann, J., & Moosdorf, N. (2011). *Chemical weathering rates of silicate-dominated lithological classes and associated liberation rates of phosphorus on the Japanese Archipelago - Implications for global scale analysis*. Chemical Geology, 287(3-4), 125-157. DOI: 10.1016/j.chemgeo.2010.12.004.

# 이 논문을 찾은 이유
LPJ-GUESS-CNP P-weathering 식의 부모 모델에서 **전체 rock-weathering flux와 P-release가 원래 분리되어 있는지** 확인하기 위해 검토했다.

# 연구 유형
- empirical spatial weathering model
- 381 Japanese catchments
- lithology/runoff regression

# 공간 구조
- catchment / lithological class
- regional spatial extrapolation

# 적용 환경
- Japanese Archipelago
- silicate-dominated lithologies

# 핵심 과정
- chemical silicate rock weathering
- cation and dissolved-silica flux
- lithology dependence
- runoff dependence
- P liberation from weathering

# bulk weathering
The parent model first estimates bulk chemical silicate-rock weathering rate, reported as major cations plus dissolved silica flux:

```
CSRWR
[ t km^-2 yr^-1 ]
```

Lithology and runoff are the dominant predictors.

The reported mean for Japan is about:
```
25 t km^-2 yr^-1
```
with large spatial variation.

# phosphorus release
P release is then estimated assuming phosphorus is liberated proportionally to the bulk rock-mineral weathering rate, using lithology-specific P content.

Thus the original architecture is conceptually:

```
bulk chemical weathering
 -> multiply by lithology-specific relative P content
 -> P release
```

This is crucial for Gounsa.

# 고운사에 직접 사용할 수 있는 부분
If total chemical mass loss is needed, use the parent **bulk weathering relation** rather than trying to infer rock mass loss from LPJ-GUESS P flux after the fact.

The parent model provides:
```
lithology + runoff
 -> bulk chemical weathering flux
```

while P content is an additional nutrient-release conversion.

# 주의
LPJ-GUESS-CNP 2025 labels an intermediate term `F_CW` even though its Eq. A7 includes P content.

For Gounsa geomorphic mass balance, do not rely on variable naming alone.

Use the parent Hartmann weathering formulation explicitly and keep:
```
F_bulk
```
and:
```
F_P
```
as separate variables.

# 한계
- empirical catchment-scale weathering flux
- original training on Japan
- does not localize dissolution depth
- does not calculate weathering-front advance
- not a soil-thickness model

# 최종 판정
**핵심 채택: bulk chemical-weathering flux source behind the LPJ-GUESS P-weathering lineage.**

# 참고 링크 / DOI
https://doi.org/10.1016/j.chemgeo.2010.12.004
