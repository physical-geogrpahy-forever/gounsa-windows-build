# 서지정보
Dantas de Paula, M., Reichert, T., Lugli, L. F., McGale, E., Pierick, K., Darela-Filho, J. P., Langan, L., Homeier, J., Rammig, A., & Hickler, T. (2025). *The fungal collaboration gradient drives root trait distribution and ecosystem processes in a tropical montane forest*. Biogeosciences, 22, 2707-2732. DOI: 10.5194/bg-22-2707-2025.

# 이 논문을 찾은 이유
LPJ-GUESS FineRootC를 RLD로 바꾸기 위해 필요한 specific root length (SRL)를 LPJ-GUESS 자체에서 quantitative root trait로 구현한 published precedent가 있는지 확인하기 위해 검토했다.

# 연구 유형
- LPJ-GUESS-NTD model development
- trait-based dynamic vegetation modelling
- field-informed fine-root parameterization

# 공간 구조
- individual/cohort vegetation in LPJ-GUESS-NTD
- tropical montane forest sites

# 적용 환경
- Ecuadorian tropical montane forest
- 직접적인 고운사 온대산림 calibration은 아님

# 핵심 과정
- fine-root biomass
- specific root length
- fine-root diameter
- fine-root absorptive surface area
- mycorrhizal nutrient acquisition
- individual trait variation

# 식생 입력 / 상태
The study adds SRL as an individual fine-root trait in LPJ-GUESS-NTD.

Fine roots are defined as roots with diameter <2 mm in the reference field data.

# 핵심 식
The published model calculates fine-root surface area as:

```
A_root
= SRL * d_root * pi * C_root
```

with:
- `SRL`: m root per kg C
- `d_root`: fine-root diameter [m]
- `C_root`: fine-root carbon biomass [kg C m^-2]

The key implication for Gounsa is even simpler: because SRL is expressed per unit **root carbon**, total fine-root length per unit ground area follows directly as:

```
L_A
= SRL_C * C_root
```

where:
- `L_A`: root length per ground area [m root m^-2 ground]
- `SRL_C`: specific root length [m root kg C^-1]
- `C_root`: fine-root C [kg C m^-2 ground]

Thus no arbitrary root-carbon-to-dry-mass fraction is necessary if SRL is parameterized in this carbon-based unit.

# 파라미터와 단위
Use a clearly defined carbon-based SRL:

```
SRL_C [m root kg C^-1]
```

Do not mix it silently with the conventional observational SRL often reported per gram of dry root mass.

If observational dry-mass SRL is used instead, a root carbon fraction conversion becomes necessary and must be separately documented.

# 원 논문의 구현 범위
LPJ-GUESS-NTD directly represents:
```
fine-root C
+ SRL
+ root diameter
-> fine-root length/surface traits
```

This is the strongest LPJ-GUESS-internal precedent found for converting a quantitative fine-root carbon pool into a root-length quantity.

# 고운사에 직접 사용할 수 있는 부분
For each PFT/cohort p:
```
L_A,p = C_root,p * SRL_C,p
```

Combined with LPJ-GUESS layer fraction `f_p,i` and layer thickness `Dz_i`:

```
RLD_p,i
= C_root,p * SRL_C,p * f_p,i / Dz_i
```

Units:
```
(kg C m^-2) * (m kg C^-1) / m
= m m^-3
```

For Gyssels-style units:
```
RLD_km,p,i
= RLD_p,i / 1000
```

# 새로운 coupling이 필요한 부분
- assigning SRL_C to the actual Gounsa PFTs/species
- deciding patch/gridcell aggregation
- deciding the erosion-active near-surface depth
- feeding the resulting RLD into SWEHR `JSMASK`

The algebraic unit conversion itself is not an empirical erosion model, but the erosion coupling remains new.

# 한계
- tropical montane forest trait ranges cannot be copied directly to Korean temperate PFTs
- LPJ-GUESS-NTD variant, not necessarily the exact Gounsa code branch
- SRL and diameter vary among species and with mycorrhizal strategy

# 최종 판정
- **핵심 채택: LPJ-GUESS fine-root C -> root-length bridge**
- resolves the dimensional conversion at the functional-form level
- remaining problem is Gounsa-specific SRL parameterization and surface-depth weighting

# 참고 링크 / DOI
https://doi.org/10.5194/bg-22-2707-2025
