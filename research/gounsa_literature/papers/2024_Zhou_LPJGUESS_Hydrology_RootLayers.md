# 서지정보
Zhou, H., Tang, J., Olin, S., & Miller, P. A. (2024). *A comprehensive evaluation of hydrological processes in a second-generation dynamic vegetation model*. Hydrological Processes, 38(4), e15152. DOI: 10.1002/hyp.15152.

# 이 논문을 찾은 이유
고운사 coupling에서 LPJ-GUESS fine-root C를 토층별 RLD로 변환하려면 현재 LPJ-GUESS의 soil-layer 구조와 PFT별 root fraction이 어떻게 정의되는지 확인해야 하므로 검토했다.

# 연구 유형
- LPJ-GUESS model evaluation / hydrology description
- global hydrological validation

# 공간 구조
- gridcell
- replicate patches
- PFT/cohort vegetation
- 15 soil layers

# 적용 환경
- global terrestrial ecosystems

# 핵심 과정
- carbon allocation
- root water uptake
- soil water balance
- PFT-specific vertical root distribution

# 식생 입력 / 상태
LPJ-GUESS annual NPP is allocated to:
- leaves
- sapwood
- fine roots

The model represents root uptake using PFT-specific fractions of roots in each soil layer.

# 핵심 구현 확인
The current multi-layer LPJ-GUESS configuration described in the paper uses:

```
15 soil layers
x 0.1 m per layer
= 1.5 m mineral-soil profile
```

Plant water uptake is partitioned according to:
```
PFT-specific root fraction in each layer
```

These root fractions are parameterized following Jackson et al. (1996).

Therefore the current model already provides the vertical weighting needed to distribute total fine-root C among soil layers.

# 고운사에 직접 사용할 수 있는 부분

If total fine-root carbon for PFT p is:
```
C_root,p [kg C m^-2 ground]
```

and LPJ-GUESS layer root fraction is:
```
f_p,i [-]
```

then the carbon assigned to layer i can be represented as:
```
C_root,p,i = C_root,p * f_p,i
```

provided the supplied `C_root,p` is already normalized per ground area for the same patch/gridcell basis.

This is a bookkeeping/unit conversion, not a new empirical erosion law.

# 새로운 coupling이 필요한 부분
- FineRootC output definition and patch/gridcell normalization must be checked in the actual Gounsa LPJ-GUESS build.
- Converting layer root C to root length using SRL and then feeding erosion resistance is part of the Gounsa coupling.
- Do not multiply by FPC/cover again if the exported root C is already ground-area normalized.

# 한계
- root architecture is prescribed rather than dynamically responding to erosion
- current root fractions describe the entire fine-root pool, not specifically the subset mechanically active in the top few centimetres
- the 1.5 m profile may not include deeper roots relevant to other geomorphic processes; for surface erosion, the near-surface fraction is the relevant part

# 최종 판정
- **채택: current LPJ-GUESS soil-layer/root-fraction source**
- key source for FineRootC -> layer-specific RLD conversion

# 참고 링크 / DOI
https://doi.org/10.1002/hyp.15152
