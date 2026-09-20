# 서지정보
Kim, M.-S., Kim, Y.-S., Min, H.-G., Kim, J.-G., & Koo, N. (2017). *Pine Forest Soil Characteristics and Major Soil Impact Factors for Natural Regeneration*. Korean Journal of Soil Science and Fertilizer, 50(3), 179-186. DOI: 10.7745/KJSSF.2017.50.3.179.

# 이 논문을 찾은 이유
고운사 산림에서 중요한 국내 소나무 Pinus densiflora의 SRL에 대한 한국 자료를 확보하여 LPJ-GUESS conifer root-trait parameterization의 local constraint로 사용할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- Korean forest-soil survey
- controlled seedling exposure/growth experiment

# 공간 구조
- soils collected from 23 Korean pine forests
- 10-day seedling growth experiment

# 적용 환경
- Pinus densiflora
- Korean forest soils from 23 locations

# 핵심 과정
- root elongation
- root dry mass
- specific root length
- soil pH / exchangeable Al controls

# 식생 입력 / 측정
SRL was defined as:
```
SRL = root length / root dry mass
```

Unit:
```
mm mg^-1
```
which is numerically equivalent to:
```
m g^-1
```

# 핵심 결과
Across the 23 forest-soil treatments, seedling SRL ranged from:
```
0.3198 to 0.7915 mm mg^-1
```

Soil pH had a positive effect on SRL, whereas exchangeable Al had a negative influence.

# 고운사에 직접 사용할 수 있는 부분
This is direct Korean Pinus densiflora evidence that SRL is not a fixed universal trait and can vary with soil chemistry.

It is useful as:
- local species evidence
- environmental sensitivity evidence
- a lower-level constraint when designing conifer SRL sensitivity ranges

# 새로운 coupling이 필요한 부분
The measured seedling dry-mass SRL cannot be inserted directly into LPJ-GUESS `SRL_C` without:
- root carbon fraction conversion
- consideration of seedling versus mature-tree fine roots

# 한계
- seedlings, not mature forest trees
- only 10 days of growth after germination
- total young-root system rather than standardized mature absorptive fine-root orders
- therefore the numerical range should **not** be adopted as the production PFT parameter

# 최종 판정
- **보조근거: Korean Pinus densiflora SRL/environmental sensitivity**
- do not use the raw seedling range as mature-forest calibration

# 참고 링크 / DOI
https://doi.org/10.7745/KJSSF.2017.50.3.179
