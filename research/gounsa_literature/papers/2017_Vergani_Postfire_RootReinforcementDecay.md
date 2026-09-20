# 서지정보
Vergani, C., Werlen, M., Conedera, M., Cohen, D., & Schwarz, M. (2017). *Investigation of root reinforcement decay after a forest fire in a Scots pine (Pinus sylvestris) protection forest*. Forest Ecology and Management, 400, 339-352. DOI: 10.1016/j.foreco.2017.06.005.

# 이 논문을 찾은 이유
산불 후 죽은 woody/fine-root system의 mechanical integrity가 수년 동안 어떻게 감소하는지 정량적 시간척도를 확보하여 postfire dead-root persistence model을 제약하기 위해 검토했다.

# 연구 유형
- postfire field root-distribution measurement
- root pullout/mechanical testing
- Root Bundle Model analysis

# 적용 환경
- stand-replacing forest fire
- Scots pine protection forest
- Switzerland
- 4 years postfire

# 핵심 과정
- root mechanical-property decay
- root reinforcement loss
- natural-regeneration recovery

# 핵심 결과
- 4 years after fire, root reinforcement was lower by a factor of about 3.6 relative to the healthy reference stand
- most of the loss was attributed to degradation of root mechanical properties
- reported decay coefficient for the model: c = 0.27, compared with c = 0.11 in a timber-harvest spruce study
- natural regeneration at 4 years contributed little compensation
- model projection indicated the old burned-stand root protection approached zero by around 10 years

# 고운사에 직접 사용할 수 있는 부분
This paper constrains the **timescale of mechanical legacy decay** after stand-replacing fire.

It supports a state such as:
```
DeadRoot quantity
x MechanicalIntegrity(age)
```
rather than assuming dead-root biomass alone determines protection.

# 새로운 coupling이 필요한 부분
The root-reinforcement metric is for slope stability, not Hairsine-Rose surface erosion.

Therefore:
- c = 0.27 must not be copied directly into SWEHR J
- factor 3.6 at four years is a sensitivity/timescale constraint only

# 한계
- Scots pine
- slope-stability root reinforcement, not direct rill/interrill erosion
- root diameter spectrum differs from erosion-active very fine roots

# 최종 판정
- **보조근거: postfire mechanical-integrity decay timescale**
- do not directly parameterize water-erosion resistance from the slope-stability coefficient

# 참고 링크 / DOI
https://doi.org/10.1016/j.foreco.2017.06.005
