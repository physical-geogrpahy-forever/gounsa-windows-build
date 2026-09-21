# 서지정보
Brantley, S. L., Eissenstat, D. M., Marshall, J. A., Godsey, S. E., Balogh-Brunstad, Z., Karwan, D. L., Papuga, S. A., Roering, J., Dawson, T. E., Evaristo, J., Chadwick, O., McDonnell, J. J., & Weathers, K. C. (2017). Reviews and syntheses: on the roles trees play in building and plumbing the critical zone. *Biogeosciences, 14*, 5115-5142. DOI: 10.5194/bg-14-5115-2017.

# 이 논문을 찾은 이유
사면 풍화와 식생을 결합할 때 뿌리와 나무가:
- regolith architecture
- water movement
- soil/bedrock permeability
- downslope solute flux
를 어떻게 함께 바꾸는지 Critical Zone 관점에서 정리하기 위해 검토했다.

# 연구 유형
- interdisciplinary review / synthesis
- testable hypotheses

# 공간 구조
- tree/root zone
- hillslope
- catchment Critical Zone
- soil to weathered bedrock continuum

# 적용 환경
- multiple Critical Zone Observatories
- forested hillslopes

# 핵심 과정
Trees as builders:
- root penetration
- regolith disturbance
- porosity/permeability changes
- weathering-zone architecture

Trees as plumbers:
- water uptake
- root-depth targeting
- hydraulic redistribution
- preferential flow
- perched/saturated zones near roots
- lateral hillslope flow
- stream chemistry effects

# 식생 입력
- tree/root distribution
- functional rooting depth
- water uptake
- nutrient foraging
- root-created permeability structure

균근 관련 가설도 원 논문에는 있지만, **고운사에서는 최신 scope decision에 따라 해당 항을 사용하지 않는다.**

# 핵심 구조
고운사와 가장 관련된 부분:

```
topography / bedrock structure
 -> root-zone accessibility
 -> root distribution
 -> permeability / macropores
 -> infiltration and lateral flow
 -> water residence and stream chemistry
 -> weathering environment
```

또한 trees above valley floor도 rooting-zone permeability를 변화시켜 intermittent saturation과 downslope water movement를 통해 stream chemistry에 영향을 줄 수 있다고 제안한다.

# 파라미터와 단위
review paper이므로 single parameter set 없음.

# 원 논문의 구현 범위
실행형 numerical model이 아니라 Critical Zone process hypotheses를 통합.

# 고운사에 직접 사용할 수 있는 부분
고운사에서 식생효과를:
```
root respiration only
```
로 축약해서는 안 된다는 구조적 근거.

최소한:
- root distribution
- root water uptake
- infiltration/permeability effect
- lateral flow
- residence time
을 weathering hydrology에 연결할 필요가 있다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root distribution을 Landlab/BioRT permeability 또는 preferential-flow state로 변환하면 새로운 coupling이다.

첫 production에서 full dynamic permeability coupling을 반드시 넣을 필요는 없지만, sensitivity 우선순위가 높다.

# 한계
- review/hypothesis paper
- quantitative rate law 없음
- heterogeneous sites
- mycorrhiza hypotheses는 Gounsa에서 제외

# 최종 판정
- **채택: forest-hillslope Critical Zone plumbing architecture의 핵심 review**
- root-controlled hydrology/weathering coupling의 구조적 근거
- coefficient source 아님

# 참고 링크 / DOI
https://doi.org/10.5194/bg-14-5115-2017
