# 서지정보
Alberts, E. E., Nearing, M. A., Weltz, M. A., Risse, L. M., Pierson, F. B., Zhang, X. C., Laflen, J. M., & Simanton, J. R. (1995). Chapter 7. Soil Component. In D. C. Flanagan & M. A. Nearing (Eds.), *USDA-Water Erosion Prediction Project Hillslope Profile and Watershed Model Documentation*. NSERL Report No. 10.

# 이 논문을 찾은 이유
WEPP의 interrill erodibility Ki, rill erodibility Kr, critical shear stress와 live/dead root, buried residue, coarse fragments의 관계를 원문에서 확인하기 위해 검토했다.

# 연구 유형
- 공식 수치모델 문서

# 공간 구조
- WEPP hillslope profile
- 기본 routing은 1D

# 적용 환경
- cropland
- rangeland

# 핵심 과정
- interrill erodibility
- rill erodibility
- critical shear stress
- infiltration
- random roughness
- coarse fragments

# 식생 입력
- live root biomass
- dead root biomass
- buried residue
- canopy
- ground cover
- rangeland ROOT10

# 핵심 식
채팅에서 직접 확인한 daily adjustment 구조:

```
Ki = Kib(CKican)(CKigc)(CKidr)(CKilr)(CKisc)(CKisl)(CKift)
Kr = Krb(CKrbr)(CKrdr)(CKrlr)(CKrsc)(CKrft)
τc = τcb(Cτrr)(Cτsc)(Cτft)
```

Lee et al. (2022)와 Chapter 7을 함께 확인한 cropland root adjustment:
```
CKidr = exp(-0.56 dr)
CKilr = exp(-0.56 lr)
CKrdr = exp(-2.2 dr)
CKrlr = exp(-3.5 lr)
```

# 파라미터와 단위
- Ki: kg s m^-4 계열
- Kr: s m^-1
- τc: Pa
- root mass: kg m^-2

# 원 논문의 구현 범위
WEPP soil state와 시간가변 erodibility parameter를 계산한다.

# 고운사에 직접 사용할 수 있는 부분
root biomass가 interrill/rill erodibility에 직접 작용하는 published model structure의 핵심 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC/dead-root/litter를 WEPP 변수에 전달하고, 이를 genuine 2D engine에서 갱신하는 것은 새로운 coupling이다.

# 한계
- cropland root coefficients의 forest transferability는 독립 검증되지 않음
- rangeland interrill은 cover 중심
- WEPP routing 자체는 genuine 2D가 아님

# 최종 판정
- 채택: root-dependent Ki/Kr 구조 근거
- 미채택: 최종 2D erosion engine
