# 서지정보

> Canonical file. 기존 `2012_Taylor_DGVMWeathering.md`의 초기 요약과 중복본의 상세 검토를 통합함.
Taylor, L. L., Banwart, S. A., Valdes, P. J., Leake, J. R., & Beerling, D. J. (2012). Evaluating the effects of terrestrial ecosystems, climate and carbon dioxide on weathering over geological time: a global-scale process-based approach. *Philosophical Transactions of the Royal Society B, 367*, 565-582. DOI: 10.1098/rstb.2011.0251.

# 이 논문을 찾은 이유
DGVM의 식생 생산성, PFT, 수문 상태를 process-based biological weathering model에 전달한 published architecture를 확인하기 위해 검토했다.

# 연구 유형
- coupled numerical model
- DGVM + climate + process-based weathering

# 공간 구조
- global grid
- 각 grid에서 soil weathering reaction calculation

# 적용 환경
- global silicate weathering
- basalt and granite
- plant and mycorrhizal functional types

# 핵심 과정
- DGVM NPP and PFT
- biological proton cycle
- nutrient uptake
- soil solution chemistry
- mineral dissolution
- hydrology

# 식생 입력
- NPP
- PFT distribution
- belowground C-N cycling
- fine-root nutrient demand
- mycorrhizal functional type

# 핵심 식
```
DGVM
 -> NPP / PFT / hydrology
 -> root + mycorrhizal nutrient uptake
 -> biological proton cycle
 -> soil pH / solution chemistry
 -> silicate dissolution
```

# 파라미터와 단위
- NPP and PFT state
- nutrient uptake stoichiometry
- mineral dissolution kinetics
- hydrologic corrections
- lithology

# 원 논문의 구현 범위
global-scale biological weathering을 dynamic vegetation and climate simulations와 연결한다.

# 고운사에 직접 사용할 수 있는 부분
정량 식생모델 상태가 weathering에 직접 forcing으로 들어가는 구조의 강한 선례다.

# 새로운 coupling이 필요한 부분
- SDGVM을 LPJ-GUESS로 교체
- sandstone mineralogy
- 100년 postfire transient implementation

# 한계
- global and geological-time purpose
- basalt/granite 중심
- local sandstone calibration 없음

# 최종 판정
- 보조 채택
- DGVM -> biological weathering coupling 근거

# 참고 링크 / DOI
https://doi.org/10.1098/rstb.2011.0251


## 중복 통합 기록
- 동일 DOI: `10.1098/rstb.2011.0251`
- 기존 canonical: `2012_Taylor_DGVMWeathering.md`
- 삭제한 중복본: `2012_Taylor_GlobalBiologicalWeathering.md`
- 기존 핵심 판정인 "DGVM NPP/PFT -> process-based weathering의 published precedent"를 유지하면서 상세 process chain을 보강함.


## 2026-09-21 mycorrhiza scope override

이 논문은 `DGVM -> process-based chemical weathering`이라는 상위 구조의 참고 선례로만 유지한다.

고운사에서 사용하지 않는 부분:
```
mycorrhizal functional type
root + mycorrhizal nutrient-uptake combined term
AM/EcM differentiation
```

고운사에서 참고 가능한 비균근 상위 구조:
- DGVM NPP/PFT/hydrology
- root nutrient demand
- soil solution chemistry
- mineral dissolution

균근 state는 모델 interface에 만들지 않는다.
