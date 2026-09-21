# 서지정보
Quirk, J., Beerling, D. J., Banwart, S. A., Kakonyi, G., Romero-Gonzalez, M. E., & Leake, J. R. (2012). Evolution of trees and mycorrhizal fungi intensifies silicate mineral weathering. *Biology Letters, 8*(6), 1006-1011. DOI: 10.1098/rsbl.2012.0503.

# 이 논문을 찾은 이유
식생-풍화 coupling에서 tree roots만 볼 것이 아니라 mycorrhizal functional type이 weathering rate를 정량적으로 바꾸는지 확인하기 위해 검토했다.

# 연구 유형
- mature-tree field experiment
- mineral weathering experiment

# 공간 구조
- forest tree root/mycorrhizal zone
- mineral substrate bags / localized weathering interface

# 적용 환경
- mature tree lineages
- arbuscular mycorrhizal (AM)
- ectomycorrhizal (EM)
- basalt-bearing mineral substrate

# 핵심 과정
- fungal hyphal colonization
- mineral-surface trenching
- Ca release
- plant-fungal C allocation
- silicate weathering

# 식생 입력
- tree lineage
- mycorrhizal type
- root-associated fungi
- photosynthetic carbon supply to symbionts

# 핵심 결과
weatherable basalt에 대한 fungal colonization과 weathering intensity가:
- AM -> EM
- gymnosperm -> angiosperm
계열에서 달라졌다.

EM gymnosperm/angiosperm treatments에서는 AM gymnosperm보다 basalt Ca release가 약 2배 수준으로 높게 관측되었다.

# 파라미터와 단위
- mineral Ca release
- hyphal colonization
- mineral-surface alteration
- host/mycorrhizal functional type

# 원 논문의 구현 범위
mature trees와 mycorrhizal fungi가 mineral weathering을 어떻게 차별화하는지 field experiment로 정량 비교.

# 고운사에 직접 사용할 수 있는 부분
고운사 chemical-weathering interface에:

```
PFT/root state
+ mycorrhizal functional type
```

를 sensitivity dimension으로 남길 근거.

특히 pine/oak succession이 일어날 경우 AM/EM association 차이가 weathering chemistry를 바꿀 수 있다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS PFT를:
- AM
- EM
- mixed
기능형으로 mapping하고 weathering source/kinetics에 반영하는 것은 새로운 coupling이다.

# 한계
- basalt substrate
- weathering experiment, not full landscape model
- exact factor를 sandstone에 직접 전이할 수 없음

# 최종 판정
- **보조 채택: mycorrhizal functional type을 weathering sensitivity state로 유지**
- coefficient direct transfer는 금지

# 참고 링크 / DOI
https://doi.org/10.1098/rsbl.2012.0503


## 2026-09-21 mycorrhiza scope override

최신 결정 `decisions/2026-09-21_MYCORRHIZA_EXCLUSION.md`에 따라 이 논문의 균근 관련 기작은 **archive/reference only**이다.

현재 고운사 production 및 sensitivity에는 다음을 넣지 않는다.

```
mycorrhizal functional type
AM / EcM state
fungal hyphal weathering
fungal oxalate allocation
mycorrhizal weathering multiplier
```

이 논문은 식생-풍화 문헌계보를 보존하기 위한 참고자료로만 유지한다.
