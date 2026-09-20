# 서지정보
Kim, J., Ivanov, V. Y., & Katopodes, N. D. (2013). *Modeling erosion and sedimentation coupled with hydrological and overland flow processes at the watershed scale*. Water Resources Research, 49, 5134-5154. DOI: 10.1002/wrcr.20373.

# 이 논문을 찾은 이유
genuine 2D Saint-Venant hydrodynamics와 Hairsine-Rose rainfall/flow erosion, multi-size sediment, original/deposited soil layers를 유역 규모에서 결합한 published model이 고운사 엔진에 더 적합한지 확인하기 위해 검토했다.

# 연구 유형
- physically based 2D erosion and sediment numerical model
- catchment-scale integrated hydrologic/hydrodynamic model

# 공간 구조
- genuine 2D Saint-Venant equations
- unstructured multiple-resolution triangular mesh
- finite volume
- Roe approximate Riemann solver
- coupled tRIBS-OFM hydrology/overland flow

# 적용 환경
- Lucky Hills watershed, southeastern Arizona
- semiarid catchment
- rainfall-event simulations
- forest/postfire application 아님

# 핵심 과정
- rainfall-driven detachment/redetachment
- overland-flow entrainment/reentrainment
- size-selective sediment transport
- deposition
- original-soil layer
- deposited loose-soil layer
- deposited-layer shielding
- bed/morphology evolution
- infiltration/runoff coupling

# 식생 입력
The model includes vegetation-mediated sensitivity cases but does not directly use root biomass in erosion resistance.

Vegetation analysis used mean annual above-ground biomass to vary:
- saturated hydraulic conductivity
- Manning roughness

The biomass effect on roughness was mediated through a biomass-to-cover relationship.

# 핵심 식
For each sediment class i, the 2D Hairsine-Rose equations track:
- suspended concentration c_i
- deposited mass M_i
- rainfall detachment/redetachment
- flow entrainment/reentrainment
- deposition

Rainfall detachment uses original/deposited-soil detachability parameters.

Flow entrainment is based on excess stream power:
```
Omega - Omega_cr
```
with effective-energy fraction and specific entrainment energy.

A shielding factor H increases as deposited sediment mass accumulates and protects original soil.

# 파라미터와 단위
- deposited mass M_i: mass area^-1
- rainfall detachability a0/ad: mass volume^-1
- critical stream power Omega_cr
- specific entrainment energy J
- settling velocity v_i
- sediment classes and original-soil fractions

# 원 논문의 구현 범위
2D hydrology, surface hydraulics, rainfall erosion, overland-flow erosion, multi-size sediment transport and deposition are solved in a single finite-volume framework and applied to a real watershed.

# 고운사에 직접 사용할 수 있는 부분
Strong engine candidate because it already contains:
```
2D SWE
+ rainfall detachment
+ flow entrainment
+ original soil
+ loose/deposited layer
+ multigrain sediment
+ morphology
```

The original/deposited layer distinction is especially relevant to postfire loose surface material, ash/fines and newly deposited sediment.

# 새로운 coupling이 필요한 부분
LPJ-GUESS roots/litter modifying H-R detachability, critical stream power, or soil-layer resistance is **new coupling**.

# 한계
- root biomass/RLD not used directly in erosion resistance
- vegetation sensitivity used above-ground biomass indirectly through Ksat/roughness and cover
- semiarid watershed, not steep forest/postfire validation
- computational implementation/source availability needs checking before selecting as production engine

# 최종 판정
- **top-tier 2D engine candidate**
- must be compared directly with Iber+ and postfire Ouyang/McGuire Hairsine-Rose lineage
- arguably more natural than Iber+ for representing intact versus loose/deposited soil

# 참고 링크 / DOI
https://doi.org/10.1002/wrcr.20373
