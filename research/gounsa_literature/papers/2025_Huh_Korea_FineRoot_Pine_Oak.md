# 서지정보
Huh, W., Lee, M., Kim, S., Byeon, S., Kim, T. K., Hong, J., Park, C., Won, G., Kim, E., et al., & Kim, H. S. (2025). *Contrasting spatio-temporal variation of fine root dynamics in nearby evergreen korean pine and deciduous oak forests*. Plant and Soil, 514, 2045-2066. DOI: 10.1007/s11104-025-07502-7.

# 이 논문을 찾은 이유
고운사 LPJ-GUESS의 FineRootC -> RLD 변환에는 한국 온대산림의 conifer/broadleaf fine-root SRL, diameter, biomass depth distribution과 turnover가 필요하므로, 국내 산림에서 직접 측정한 가장 가까운 자료로 검토했다.

# 연구 유형
- field fine-root ecology
- sequential soil coring
- minirhizotron monitoring

# 공간 구조
- three replicated 20 x 20 m plots per forest type
- soil depth classes 0-10, 10-20, 20-30 cm
- repeated root observations over 2021-2022

# 적용 환경
- Mt. Taehwa, Seoul National University Forest, central Korea
- evergreen Korean pine stand dominated by Pinus koraiensis
- deciduous oak stand dominated by Quercus aliena / Q. variabilis
- loamy/granitic temperate forest setting

# 핵심 과정
- fine-root biomass
- fine-root length
- SRL
- root diameter
- depth distribution
- production
- mortality
- turnover / longevity

# 식생 입력 / 측정
Fine roots:
```
diameter < 2 mm
```

Soil cores were separated into:
```
0-10 cm
10-20 cm
20-30 cm
```

SRL was measured conventionally as:
```
SRL_dry = root length / root dry mass
```

# 핵심 결과
Across the whole 0-30 cm profile:
- Korean pine fine roots had a larger mean diameter, about 0.986 mm
- oak fine roots had a smaller mean diameter, about 0.619 mm
- oak SRL was about three times the Korean-pine SRL across the profile
- in the 0-10 cm layer, oak SRL was almost five times the Korean-pine value

Root biomass:
- Korean pine: about 265 g m^-2 in 0-30 cm
- oak: about 269 g m^-2 in 0-30 cm
- despite similar total biomass, depth allocation differed strongly
- oak very-fine roots and total fine-root biomass were concentrated much more strongly in 0-10 cm
- Korean pine fine-root biomass/morphology was comparatively uniform over 0-30 cm

Turnover:
- Korean pine fine roots had faster turnover and shorter lifespan
- oak roots had slower turnover and longer lifespan

This is directly important after fire because the same total FineRootC does **not** imply the same surface RLD or persistence for conifer and broadleaf PFTs.

# 파라미터와 단위
- SRL in the field paper: root length per dry mass
- LPJ-GUESS-NTD Dantas implementation can instead use SRL per kg C

Therefore direct numerical use requires either:
1. convert measured dry-mass SRL to carbon-based SRL using a documented root C fraction, or
2. calibrate/derive `SRL_C` directly from paired root C and length data.

Do not silently identify dry-root mass with carbon mass.

# 고운사에 직접 사용할 수 있는 부분
This is a high-priority local constraint for PFT-specific root traits.

At minimum, distinguish:
```
evergreen conifer PFT
!=
deciduous broadleaf/oak PFT
```

The observed Korean forest result supports:
- lower surface SRL for pine than oak
- stronger 0-10 cm concentration for oak
- different root turnover dynamics

These local ratios are more relevant to Gounsa than tropical LPJ-GUESS-NTD SRL ranges.

# erosion-active depth implication
The study shows that the upper 0-10 cm is a biologically distinct fine-root layer in Korean forest soils.

For the first Gounsa implementation, the LPJ-GUESS top 10-cm root fraction is therefore the most defensible **available model layer** for a surface-erosion RLD state.

However, this does not mean erosion mechanically samples the entire 10 cm equally. A shallower active-depth sensitivity (e.g. upper part of the top layer) should be tested if field/root or erosion data justify it.

# 새로운 coupling이 필요한 부분
- species/stand observations -> Gounsa PFT-level SRL parameter
- dry-mass SRL -> carbon-based SRL if needed
- postfire mortality -> live/dead root states
- layer RLD -> SWEHR JSMASK

# 한계
- Korean pine rather than Pinus densiflora
- oak stand is mixed Q. aliena / Q. variabilis
- no erosion experiment
- data quantify 0-30 cm, not roots in the upper millimetres/centimetres specifically

# 최종 판정
- **핵심 채택: Korean temperate-forest PFT-specific SRL/depth/turnover constraint**
- high priority for Gounsa FineRootC -> RLD parameterization

# 참고 링크 / DOI
https://doi.org/10.1007/s11104-025-07502-7
