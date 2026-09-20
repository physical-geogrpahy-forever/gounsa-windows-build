# PSEM_2D lineage

## 핵심 문헌
Nord & Esteves (2005). Water Resources Research 41. DOI 10.1029/2004WR003690.

## 고운사에서 검토한 이유
genuine 2D shallow-water and physically based rainfall/runoff erosion model without a fixed rill mask.

## 공간구조
- depth-averaged 2D Saint-Venant
- explicit finite difference
- natural nonplanar surfaces
- plot scale

## erosion processes
- rainfall detachment
- rainfall redetachment
- runoff detachment
- deposited-layer entrainment
- deposition
- suspended sediment conservation

## rill/interrill interpretation
The model does not need to prescribe rill/interrill classes in the Wu sense.
Microtopography + 2D hydraulics creates zones dominated by rainfall vs flow erosion.
Do not relabel this as an explicit rill/interrill classifier unless the paper itself does so.

## vegetation
No dynamic vegetation/root biomass/RLD module.

## 고운사에 쓸 수 있는 부분
- genuine 2D comparison engine
- rainfall vs flow erosion separation
- topography-flow feedback at plot scale

## 새로운 coupling
Any LPJ-GUESS/WEPP root or litter effects added to PSEM_2D erodibility parameters are **new coupling**.

## 최종 판정
**2D engine comparison candidate.**
