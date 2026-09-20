# WEPP model lineage

## 고운사에서 검토한 이유
interrill과 rill을 분리하면서 live/dead root biomass, residue 등 quantitative vegetation state를 soil erodibility에 직접 반영하는 published model lineage를 찾기 위해 검토했다.

## 공간구조
- 기본 hillslope profile은 1D
- watershed extension은 representative hillslopes/channel network
- genuine 2D surface-flow engine은 아님

## 핵심 erosion structure
Interrill:
```
D_i = K_i,adj × rainfall/runoff terms
```

Rill detachment capacity:
```
D_c = K_r (τ - τ_c)
```

Net rill detachment:
```
D_f = D_c (1 - G/T_c)
```

## root/residue effects confirmed in this chat

Cropland-style adjustment:
```
CKidr = exp(-0.56 * dr)
CKilr = exp(-0.56 * lr)

CKrbr = exp(-0.4 * br)
CKrdr = exp(-2.2 * dr)
CKrlr = exp(-3.5 * lr)
```

- `lr`: live root mass
- `dr`: dead root mass
- `br`: buried residue mass

Important:
- root biomass directly modifies `K_i` and `K_r`
- this chat did **not** verify an equivalent direct root multiplier on `τ_c`
- do not invent biomass-dependent `τ_c` without separate literature support

Rangeland lineage:
- surface 0.1 m live + dead root biomass (`ROOT10`) is used in baseline rill-erodibility-related parameterization
- do not automatically equate rangeland ROOT10 relations with dynamic LPJ-GUESS FineRootC without a documented conversion

## vegetation pools
WEPP plant/residue components distinguish:
- above-ground biomass
- live root biomass
- dead root biomass
- root depth
- LAI
- canopy
- standing residue
- flat residue
- buried residue
- coarse fragments

## key papers/files
- Alberts et al. 1995, WEPP Soil Component
- Arnold et al. 1995, Plant Growth Component
- Stott et al. 1995, Residue Component
- Foster et al. 1995, Hillslope Erosion Component
- Lee et al. 2022
- Mao et al. 2010
- Gould et al. 2016

## 고운사에 쓸 수 있는 부분
- quantitative root biomass -> `K_i/K_r` adjustment
- live/dead root separation
- residue pools
- interrill/rill process separation

## 새로운 coupling
LPJ-GUESS FineRootC/LitterC를 WEPP variables로 변환하거나 Wu/Iber 등 genuine 2D engine에 전달하는 것은 **새로운 coupling**이다.

## 최종 판정
**핵심 채택 lineage: quantitative vegetation -> erosion resistance.**
2D hydraulics engine은 별도 필요.
