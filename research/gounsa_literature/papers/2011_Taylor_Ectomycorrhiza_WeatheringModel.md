# 서지정보
Taylor, L. L., Banwart, S., Leake, J. R., & Beerling, D. J. (2011). Modeling the evolutionary rise of ectomycorrhiza on sub-surface weathering environments and the geochemical carbon cycle. *American Journal of Science, 311*, 369-403. DOI: 10.2475/05.2011.01.

# 이 논문을 찾은 이유
뿌리와 균근의 양분 흡수 및 탄소 배분을 mineral weathering kinetics에 직접 연결한 정량 process model이 있는지 확인하기 위해 검토했다.

# 연구 유형
- process-based 수치모델
- biological weathering model

# 공간 구조
- mycorrhizosphere와 bulk soil을 분리한 토양 반응 구조

# 적용 환경
- silicate mineral weathering
- plant and mycorrhizal functional types

# 핵심 과정
- fine-root and mycorrhizal nutrient uptake
- biological proton cycle
- organic-acid exudation
- decomposition and nutrient return
- soil pH
- mineral dissolution

# 식생 입력
- NPP
- fine-root activity
- nutrient uptake
- mycorrhizal functional type
- organic matter return

# 핵심 식
핵심은 biological proton cycle이다.

```
NPP
 -> root / mycorrhizal nutrient uptake
 -> proton and base-cation balance
 -> mycorrhizosphere pH
 -> mineral dissolution kinetics
```

EM fungi의 organic-acid exudation도 별도 weathering mechanism으로 포함한다.

# 파라미터와 단위
- nutrient uptake stoichiometry
- biomass elemental composition
- proton balance
- organic ligand concentration
- mineral-specific dissolution kinetics

# 원 논문의 구현 범위
식물과 균근 기능형이 silicate weathering 환경을 어떻게 바꾸는지를 process model로 계산한다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS의 NPP, fine-root state, nutrient uptake, litter/decomposition을 chemical-weathering proton balance에 연결할 수 있다는 근거다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS PFT를 실제 고운사 수종의 mycorrhizal functional type과 연결하는 것은 새로운 coupling이다.

# 한계
- geological carbon-cycle 목적
- sandstone-specific parameterization 아님
- 산불 후 annual calibration이 아님

# 최종 판정
- 보조 채택
- direct vegetation-to-chemical-weathering mechanism의 강한 근거
- production에서는 B-WITCH/REWTCrunch와 함께 사용 수준을 결정

# 참고 링크 / DOI
https://doi.org/10.2475/05.2011.01


## 2026-09-21 mycorrhiza scope override

이 논문의 mycorrhizal-specific mechanism은 current Gounsa production/sensitivity에서 사용하지 않는다.

Archive/reference only:
- mycorrhizal functional type
- fungal nutrient uptake term
- fungal organic-acid term
- mycorrhizosphere-specific parameterization

필요하면 이 논문에서 일반적인 biological proton-cycle 개념만 역사적 참고로 본다. Production equation 또는 parameter source로 사용하지 않는다.
