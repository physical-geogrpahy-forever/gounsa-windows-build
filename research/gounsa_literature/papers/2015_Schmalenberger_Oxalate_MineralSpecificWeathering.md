# 서지정보
Schmalenberger, A., Duran, A. L., Bray, A. W., Bridge, J., Bonneville, S., Benning, L. G., Romero-Gonzalez, M. E., Leake, J. R., & Banwart, S. A. (2015). Oxalate secretion by ectomycorrhizal Paxillus involutus is mineral-specific and controls calcium weathering from minerals. *Scientific Reports, 5*, 12187. DOI: 10.1038/srep12187.

# 이 논문을 찾은 이유
mycorrhizal weathering에서 organic-acid secretion이 일정한 plant trait인지, 아니면 mineral composition에 따라 식물이 반응적으로 조절하는지 확인하기 위해 검토했다.

# 연구 유형
- controlled mycorrhizal microcosm experiment
- 14C tracing
- mineral-specific weathering analysis

# 공간 구조
- tree root / ectomycorrhizal hypha / mineral grain interface

# 적용 환경
- Pinus sylvestris
- Paxillus involutus
- multiple rock/mineral substrates

# 핵심 과정
- photosynthate allocation
- fungal oxalate secretion
- proton acidity
- mineral-specific Ca dissolution
- nutrient acquisition

# 식생 입력
- plant photoassimilate
- ectomycorrhizal fungal activity
- mineral-specific fungal response

# 핵심 결과
Paxillus involutus는 모든 광물에 같은 양의 oxalate를 분비하지 않았다.

```
mineral composition / nutrient content
 -> fungal C allocation / oxalate secretion
 -> Ca weathering
```

경로가 확인되었다.

weathered Ca accumulation은 mineral type에 따라 크게 달랐다.

# 파라미터와 단위
- 14C allocation
- oxalate secretion
- hyphal surface acidity
- weathered Ca
- mineral composition

# 원 논문의 구현 범위
tree-mycorrhiza system이 nutrient-bearing minerals를 선택적으로 weathering하는지를 실험적으로 정량화.

# 고운사에 직접 사용할 수 있는 부분
root exudation 또는 mycorrhizal ligand source를:

```
constant fraction of root C
```

로만 둘 경우 중요한 feedback을 놓칠 수 있음을 보여준다.

가능한 고급 coupling:
```
nutrient demand
+ local mineralogy
 -> exudation / ligand allocation
```

# 새로운 coupling이 필요한 부분
LPJ-GUESS-CNP nutrient limitation과 sandstone mineralogy를 fungal/exudate allocation에 연결하는 것은 새로운 coupling.

# 한계
- specific EcM fungus and pine
- microcosm
- sandstone directly tested하지 않음
- landscape-scale coefficient 없음

# 최종 판정
- **보조 채택: mineral-specific exudation feedback의 핵심 근거**
- first production에서는 sensitivity/advanced option

# 참고 링크 / DOI
https://doi.org/10.1038/srep12187
