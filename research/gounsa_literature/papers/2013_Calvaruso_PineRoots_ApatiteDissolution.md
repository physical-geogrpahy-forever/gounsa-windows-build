# 서지정보
Calvaruso, C., Turpault, M.-P., Frey-Klett, P., Uroz, S., Pierret, M.-C., Tosheva, Z., & Kies, A. (2013). Increase of apatite dissolution rate by Scots pine roots associated or not with *Burkholderia glathei* PML1(12)Rp in open-system flow microcosms. *Geochimica et Cosmochimica Acta, 106*, 287-306. DOI: 10.1016/j.gca.2012.12.014.

# 이 논문을 찾은 이유
균근 없이 living tree roots 자체가 mineral dissolution을 정량적으로 증가시킬 수 있는 직접 실험 근거를 찾기 위해 검토했다.

# 연구 유형
- controlled open-system flow microcosm
- tree-root mineral-weathering experiment
- mass-balance experiment

# 공간 구조
- Scots pine seedling roots
- apatite grains
- continuous flow-through microcosm

# 적용 환경
- forest nutrient acquisition analogue
- apatite
- Scots pine

# 핵심 과정
- root proton release
- root organic-acid release
- apatite dissolution
- nutrient uptake
- element export

일부 treatment는 mineral-weathering bacterium을 포함하지만, **root-only treatment도 별도로 존재**한다.

균근은 본 실험의 production 근거로 사용하지 않는다.

# 식생 입력
- living Scots pine roots
- root rhizosphere chemistry
- nutrient uptake

# 핵심 결과
Scots pine roots는 bacterial inoculation 유무와 관계없이 abiotic control에 비해 apatite에서 여러 원소의 release를 크게 증가시켰다.

reported weathering-budget result:
- Ca, P 및 여러 trace elements release가 control 대비 factor >10 수준으로 증가

SEM에서도 root contact zone의 apatite dissolution 흔적을 확인했다.

Roots/rhizosphere에서:
- protons
- gluconate
- oxalate
- acetate
- lactate
등의 weathering agents가 확인되었다.

# 파라미터와 단위
- open-system water flux
- outlet Ca/P/trace-element fluxes
- organic-acid concentrations
- pH
- apatite dissolution rate

고운사에 factor >10을 그대로 적용하지 않는다.

# 원 논문의 구현 범위
living tree root presence가 apatite dissolution과 element mobilization을 얼마나 변화시키는지 flow-through mass balance로 정량화.

# 고운사에 직접 사용할 수 있는 부분
매우 중요한 non-mycorrhizal root-weathering evidence.

```
living tree roots
 -> proton / organic-acid release
 -> mineral dissolution
```

경로가 실제 forest-tree root에서 존재함을 보여준다.

이는 균근 없이도 root chemistry를 chemical-weathering interface에 남길 근거다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root state / nutrient demand를:
- proton source
- organic-acid source
로 변환하는 것은 새 coupling이다.

# 한계
- apatite는 sandstone bulk silicate와 반응성이 다름
- seedling microcosm
- annual landscape W_chem coefficient로 직접 변환 불가
- bacterial interaction treatment가 함께 존재하나 root-only evidence를 분리해서 사용해야 함

# 최종 판정
- **채택: non-mycorrhizal living-root chemical-weathering 핵심 실험근거**
- root chemistry pathway 유지 근거
- coefficient direct transfer 금지

# 참고 링크 / DOI
https://doi.org/10.1016/j.gca.2012.12.014
