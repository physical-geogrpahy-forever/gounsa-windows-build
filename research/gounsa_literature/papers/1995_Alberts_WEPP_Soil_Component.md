# 서지정보
Alberts, E. E., Nearing, M. A., Weltz, M. A., Risse, L. M., Pierson, F. B., Zhang, X. C., Laflen, J. M., & Simanton, J. R. (1995). *Soil Component*. In D. C. Flanagan & M. A. Nearing (Eds.), USDA-Water Erosion Prediction Project: Hillslope Profile and Watershed Model Documentation. NSERL Report No. 10, Chapter 7.

# 이 문서를 찾은 이유
WEPP의 Ki, Kr, tau_c가 실제로 어떻게 정의되고 vegetation/root/residue 상태로 조정되는지 원 공식문서에서 확인하기 위해 검토했다.

# 연구 유형
- official technical model documentation

# 공간 구조
- WEPP hillslope/watershed parameterization

# 적용 환경
- cropland
- rangeland
- multiple WEPP field-study soils

# 핵심 과정
- interrill erodibility Ki
- rill erodibility Kr
- critical shear stress tau_c
- temporal soil/management adjustment
- coarse fragments

# 식생 입력
- live root biomass
- dead root biomass
- buried residue
- ground/canopy effects
- rangeland ROOT10 lineage

# 핵심 식
이 채팅에서 원문 확인한 root multipliers:
```
CKidr = exp(-0.56 * dr)
CKilr = exp(-0.56 * lr)

CKrbr = exp(-0.4 * br)
CKrdr = exp(-2.2 * dr)
CKrlr = exp(-3.5 * lr)
```

# 파라미터와 단위
WEPP Chapter 7 original units must be preserved in implementation.
Do not silently substitute LPJ-GUESS carbon units.

# 원 문서의 구현 범위
soil erodibility, temporal adjustment, rangeland/cropland equations, coarse-fragment effects.

# 고운사에 직접 사용할 수 있는 부분
quantitative roots/residue -> Ki/Kr parameterization.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC/dead-root pools -> WEPP root mass is **new coupling** unless conversion is explicitly documented.

# 한계
WEPP hydraulics itself is not genuine 2D.

# 최종 판정
**핵심 채택 technical source.**
