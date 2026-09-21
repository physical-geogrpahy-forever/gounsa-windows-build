# 서지정보
Rombouts, T., Van Der Bauwhede, R., Campioli, M., Wallander, H., Sitters, J., & Verbruggen, E. (2026). Interactions between silicate weathering and ectomycorrhiza in severely acidified forests. *Communications Earth & Environment, 7*, 436. DOI: 10.1038/s43247-026-03592-y.

# 이 논문을 찾은 이유
최신 forest-weathering literature에서 ectomycorrhizal weathering의 합의 수준과 아직 해결되지 않은 scaling 문제를 확인하기 위해 검토했다.

# 연구 유형
- peer-reviewed perspective / synthesis

# 공간 구조
- hypha
- root zone
- forest stand
- landscape scaling discussion

# 적용 환경
- acidified forests
- ectomycorrhizal forest ecosystems
- enhanced silicate weathering context

# 핵심 과정
- EcM nutrient acquisition
- hyphal mineral penetration
- organic-acid secretion
- silicate dissolution
- soil acidification feedback
- base-cation supply
- forest nutrient cycling

# 식생 입력
- tree-EcM symbiosis
- photosynthetic C allocation
- EcM colonization/function
- forest acidification state

# 핵심 내용
논문은 EcM fungi가:
- mineral pores/fissures에 접근
- organic acids를 분비
- nutrient-bearing silicates를 weathering
할 수 있다는 evidence를 종합한다.

또한 plant-derived carbon allocation이 fungal weathering을 구동하는 핵심 energy pathway라고 정리한다.

# 파라미터와 단위
Perspective이므로 하나의 실행형 parameter set은 없다.

본문에서는 literature synthesis 차원에서 ecosystem별 weathering enhancement estimates를 논의하지만 고운사 coefficient로 사용하지 않는다.

# 원 논문의 구현 범위
forest silicate weathering와 EcM ecology의 current state와 knowledge gaps를 정리.

# 고운사에 직접 사용할 수 있는 부분
최신 관점에서 다음이 아직 핵심 gap임을 확인:
- fungal community-specific weathering
- mineral-specific response
- plot-to-landscape scaling
- forest type dependence

따라서 고운사에서 mycorrhiza를 hard-coded multiplier로 만들지 않고 advanced sensitivity state로 유지하는 현재 판정을 지지한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS PFT -> EcM functional state -> chemical-weathering source term은 새 coupling.

# 한계
- perspective
- enhanced weathering context가 큼
- original Gounsa-like postfire model은 아님

# 최종 판정
- **보조근거 / 최신 synthesis**
- mycorrhizal pathway 유지, coefficient 직접 사용 금지

# 참고 링크 / DOI
https://doi.org/10.1038/s43247-026-03592-y


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
