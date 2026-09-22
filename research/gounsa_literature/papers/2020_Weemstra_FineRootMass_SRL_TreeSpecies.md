# 서지정보
Weemstra, M., et al. (2020). The role of fine-root mass, specific root length and life span in tree performance: A whole-tree exploration. *Functional Ecology*. https://doi.org/10.1111/1365-2435.13520

# 검토 이유
LANDIS-II NECN의 fine-root biomass를 erosion literature에서 사용하는 RLD로 변환할 수 있는 기존 tree-trait 자료가 있는지 확인하기 위해 검토했다.

# 핵심 물리량
여러 tree species에서 함께 측정:
- fine-root biomass [kg m^-3]
- specific root length, SRL [m g^-1]
- root length density, RLD [m m^-3]
- root tissue density
- mean root diameter

예시 수종에는 Quercus robur, Alnus glutinosa, Fagus sylvatica 등이 포함된다.

# 핵심 관계
단위일치 조건에서:
```
RLD = root mass density * SRL
```

이는 새로운 empirical erosion equation이 아니라 root mass를 root length로 바꾸는 trait-based unit transformation이다.

# LANDIS-II와의 관계
NECN이 주는 fine-root biomass를 soil-volume 기준 root mass density로 변환한 뒤, 종별 SRL을 사용하면 RLD를 계산할 수 있다.

# 한계
- NECN output 단위와 soil-volume normalization을 정확히 맞춰야 함
- species-specific SRL 필요
- Quercus robur 값을 Quercus mongolica에 그대로 이식하지 않음
- RLD 계산이 곧 erosion resistance 계산을 의미하지는 않음

# 판정
**FineRoot biomass -> RLD conversion의 강한 trait-based 근거.**
