# 서지정보
Gregory, J. M. (1982). *Soil Cover Prediction with Various Amounts and Types of Crop Residue*. Transactions of the ASAE, 25(5), 1333-1337. DOI: 10.13031/2013.33723.

# 이 논문을 찾은 이유
LPJ-GUESS가 제공할 수 있는 surface litter mass [kg m^-2]를 erosion model이 사용하는 actual surface-cover/shielding state로 변환하는 published quantitative bridge가 있는지 확인하기 위해 검토했다.

# 연구 유형
- theoretical/empirical residue-cover model
- field verification
- erosion model 자체는 아님

# 공간 구조
- surface residue layer
- plot/field scale

# 적용 환경
- agricultural crop residues
- 여러 residue type
- forest litter 직접 연구는 아님

# 핵심 과정
- dry residue mass
- projected/occupied soil-surface cover
- geometric saturation of surface cover with increasing mass

# 식생 입력
- surface residue dry mass per unit area
- residue-type-specific area-to-mass/calibration coefficient

# 핵심 식
Gregory derives the standard exponential mass-to-cover relationship:

```
C = 1 - exp(-b M)
```

where:
- `C`: fraction of soil surface covered [-]
- `M`: dry surface-residue mass per unit area
- `b`: residue-type-specific mass-to-cover coefficient with units reciprocal to `M`

The equation is saturating:
- low mass: cover rises approximately linearly
- high mass: additional mass produces progressively smaller cover gains
- `C -> 1` as mass becomes large

# 파라미터와 단위
The units of `b` depend on the mass-area unit used for `M`.
Do not transfer a coefficient without converting units.

Gregory measured coefficients for several crop-residue types and verified the equation against field data.

# 원 논문의 구현 범위
This paper solves only:
```
surface residue mass -> fractional surface cover
```
It does not provide a rainfall-detachability, rill-erodibility, or Hairsine-Rose equation.

# 고운사에 직접 사용할 수 있는 부분
This is a defensible intermediate state conversion:

```
LPJ-GUESS SurfaceLitter mass
 -> litter-specific surface cover C_lit
 -> erosion shielding/protection
```

This is preferable to pretending that litter mass is itself an intrinsic soil detachability.

# 새로운 coupling이 필요한 부분
Applying `C_lit` to SWEHR rainfall/flow erosion terms is a **new coupling** unless an erosion paper supplies the corresponding cover-response equation.

The coefficient `b` must not be borrowed from crop residue for Gounsa forest litter without calibration or forest-litter evidence.

# 한계
- agricultural residues
- residue geometry strongly controls `b`
- decomposition, packing and moisture can alter projected cover
- no postfire or forest-specific calibration

# 최종 판정
- **채택: surface litter/residue mass -> cover functional bridge**
- coefficient source for Gounsa must come from forest litter or local measurements
- not an erosion engine

# 참고 링크 / DOI
https://doi.org/10.13031/2013.33723
