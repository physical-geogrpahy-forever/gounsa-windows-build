# 서지정보
Stott, D. E., Alberts, E. E., & Weltz, M. A. (1995). *Residue Decomposition and Management*. In D. C. Flanagan & M. A. Nearing (Eds.), USDA-Water Erosion Prediction Project: Hillslope Profile and Watershed Model Documentation. NSERL Report No. 10, Chapter 9.

# 이 문서를 찾은 이유
산불 후 litter/dead-root/residue pool을 erosion resistance와 연결할 때 WEPP가 어떤 residue pools를 분리하고, surface residue mass를 실제 surface cover로 어떻게 변환하는지 확인하기 위해 검토했다.

# 연구 유형
- official technical model documentation

# 핵심 과정
- residue decomposition
- standing/flat/buried residue
- dead roots
- management effects
- surface coarse fragments handled separately in WEPP system
- flat-residue mass -> surface cover

# 식생 입력
- standing residue
- flat residue
- buried residue
- dead root biomass

# 핵심 식

WEPP Chapter 9 uses the Gregory-type exponential relation for flat residue cover:

```
C_rf = 1 - exp(-c_f M_f)
```

where:
- `C_rf`: fraction of soil covered by flat residue [-]
- `M_f`: flat residue biomass per unit area
- `c_f`: residue-specific mass-to-cover coefficient

This is a saturating quantitative mass-to-cover conversion.

The decomposition component separately tracks standing, flat, buried residue and dead roots rather than collapsing all detritus into one cover variable.

# 파라미터와 단위
- `M_f`: surface/flat residue dry mass per area
- `c_f`: reciprocal mass-area units consistent with `M_f`
- original WEPP units must be preserved or explicitly converted

# 원 문서의 구현 범위
WEPP provides:
```
residue mass/state
 -> surface cover
 -> erosion-related surface protection
```

It does not imply that all forest litter has the same mass-to-cover coefficient as crop residue.

# 고운사에 직접 사용할 수 있는 부분
The important transferable architecture is:

```
SurfaceLitter mass
 -> litter-type-specific surface cover
 -> erosion shielding
```

This supports keeping LPJ-GUESS litter in quantitative mass units while deriving a separate physically interpretable cover state for rainfall-impact protection.

# 새로운 coupling이 필요한 부분
LPJ-GUESS litter carbon -> dry litter mass -> forest litter cover is a **new coupling** unless the carbon-to-dry-mass and litter-type coefficient are explicitly documented.

Using that cover inside SWEHR is another new coupling.

# 한계
- agricultural-management heritage
- crop-residue coefficient values are not automatically transferable to forest litter
- surface position, morphology and decomposition state matter

# 최종 판정
**core residue-pool and mass-to-cover source.**

# 관련 보완문헌
- Gregory 1982: theoretical/empirical mass-to-cover equation
- Pannkuk & Robichaud 2003: direct postfire conifer-needle mass-to-cover and erosion-response calibration
