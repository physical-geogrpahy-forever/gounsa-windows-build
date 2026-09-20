# 서지정보
Hartmann, J., Moosdorf, N., Lauerwald, R., Hinderer, M., & West, A. J. (2014). *Global chemical weathering and associated P-release - The role of lithology, temperature and soil properties*. Chemical Geology, 363, 145-163. DOI: 10.1016/j.chemgeo.2013.10.025.

# 이 논문을 찾은 이유
LPJ-GUESS-CNP의 chemical-weathering forcing이 실제로 어떤 bulk-weathering, temperature, soil-shielding 계보에서 왔는지 확인하고, Gounsa에서 nutrient P flux와 geomorphic chemical mass loss를 분리하기 위해 검토했다.

# 연구 유형
- global empirical chemical-weathering model
- lithology/runoff/temperature/soil-shielding synthesis

# 공간 구조
- global grid / lithological class

# 적용 환경
- global land surface
- multiple rock classes

# 핵심 과정
- lithology-specific bulk chemical weathering
- temperature adjustment
- runoff control
- soil shielding
- associated P release

# 핵심 구조
The 2014 model extends the earlier Hartmann-Moosdorf weathering approach by adding:
- lithology-specific temperature sensitivity
- soil shielding for strongly depleted/thick surface materials
- global spatial application

The conceptual chain is:

```
lithology + runoff
 -> bulk chemical weathering

bulk chemical weathering
 x temperature factor
 x soil-shielding factor
 -> climate/soil-adjusted weathering flux

adjusted bulk weathering
 x lithology-specific P content
 -> P release
```

# 고운사에 직접 사용할 수 있는 부분
Use this lineage to define a **bulk dissolved chemical mass-loss flux** separately from nutrient P release.

In a Gounsa implementation define explicitly:
```
F_bulk_chem
```
and:
```
F_P_release
```
instead of reusing an ambiguous variable name.

# LPJ-GUESS relation
Dantas de Paula et al. 2025 directly adopts this model family for P weathering and applies daily LPJ-GUESS soil temperature and prognostic runoff.

Therefore the climate forcing can be taken from LPJ-GUESS while the geomorphic mass balance should use the parent bulk-weathering quantity.

# 한계
- empirical/global
- no explicit reaction-front depth
- no direct regolith-thickness production
- soil shielding is categorical/parameterized rather than a fully evolving local profile

# 최종 판정
**채택: temperature and soil-shielding extension of the bulk weathering forcing.**

Use for dissolved chemical loss, not as the bedrock-to-regolith production law.

# 참고 링크 / DOI
https://doi.org/10.1016/j.chemgeo.2013.10.025
