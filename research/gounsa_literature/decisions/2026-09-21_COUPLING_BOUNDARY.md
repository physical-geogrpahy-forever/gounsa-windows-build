# 결정: 기존 문헌식과 새로운 coupling의 경계

날짜: 2026-09-21

## 기존 문헌에서 직접 확인된 것

### WEPP
- live/dead root biomass -> interrill erodibility adjustment
- live/dead root biomass + buried residue -> rill erodibility adjustment
- interrill/rill process separation

### Mao et al. 2010
- distributed hydrology + WEPP erosion parameterization
- vegetation/root/residue states -> erodibility adjustment

### Gould et al. 2016
- VIC-WEPP lineage -> wildfire mountain watershed application

### PROMET/Waldmann
- dynamic vegetation -> layer root length density -> erosion resistance/root reinforcement

### ELM-Erosion
- PFT-specific root biomass -> erosion resistance

### Wu et al. 2020
- genuine 2D runoff/sediment
- explicit interrill/rill equations
- Ki/Kr/tau_c as erosion parameters
- no dynamic root biomass module

### Iber+ 2024
- genuine 2D finite-volume hydro-erosion
- rainfall-driven vs flow-driven detachment
- no dynamic root biomass module

## 반드시 새로운 coupling이라고 부를 것
다음은 이 채팅에서 reviewed papers 중 하나의 원래 구현으로 확인되지 않았다.

- LPJ-GUESS FineRootC -> WEPP root-mass variable
- LPJ-GUESS FineRootC -> Wu Ki/Kr
- LPJ-GUESS FineRootC -> Iber Kd
- LPJ-GUESS litter biomass -> Iber rainfall erodibility alpha_d
- PROMET RLD relation -> Wu/Iber
- McGuire rill output -> Wu rill mask
- thermal spall production -> Lamb dry-ravel storage/release

## 원칙
문헌식 자체는 가능한 한 원형을 유지한다.
단위변환은 허용하되, 변수의 생태학적 의미를 임의로 동일시하지 않는다.
