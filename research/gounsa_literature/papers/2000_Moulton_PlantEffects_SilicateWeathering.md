# 서지정보
Moulton, K. L., West, A. J., & Berner, R. A. (2000). Solute flux and mineral mass balance approaches to the quantification of plant effects on silicate weathering. *American Journal of Science, 300*(7), 539-570. DOI: 10.2475/ajs.300.7.539.

# 이 논문을 찾은 이유
사면기울기, 미기후, lithology 차이를 가능한 한 줄인 상태에서 trees 자체가 silicate weathering을 얼마나 변화시킬 수 있는지 정량 field evidence를 확인하기 위해 검토했다.

# 연구 유형
- paired catchment/landscape field comparison
- solute-flux mass balance
- mineral mass balance
- vegetation vs barren comparison

# 공간 구조
- adjacent basaltic areas
- bare to tree-covered landscape comparison
- catchment drainage / soil weathering products

# 적용 환경
- western Iceland
- basalt
- barren areas with partial moss/lichen cover
- tree-populated areas

# 핵심 과정
- silicate dissolution
- Ca/Mg release
- cation uptake by growing trees
- stream solute export
- plagioclase weathering
- pyroxene weathering
- vegetation-mediated weathering

# 식생 입력
- tree presence
- tree biomass / cation uptake
- birch vs conifer comparison

Dynamic vegetation model은 아니다.

# 실험 설계의 강점
저자들은 plant effect를 분리하기 위해:
- microclimate
- slope
- lithology
차이를 최소화하도록 인접 site를 선택했다.

따라서 단순 aspect/erosion 공변보다 식생 effect를 비교적 직접적으로 본 자료다.

# 핵심 결과
solute-flux approach:
```
vegetated Ca + Mg weathering release
~4 x barren
```

mineral mass balance:
```
plagioclase weathering
~2 x

pyroxene weathering
~10 x
```
vegetated vs bare difference가 보고되었다.

또 biomass-normalized weathering flux가 birch에서 conifer보다 높았다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요한 positive vegetation-effect field evidence:

```
vascular plants
 -> increased mineral weathering
```

그러나 이것을:
```
W_chem *= 4
```
또는:
```
P_sand *= 4
```
로 고운사에 적용하지 않는다.

이 연구는 basalt/mineral-specific response이고 modern process pathways를 직접 분해하지 않는다.

고운사에서는 root respiration, hydrology, nutrient uptake/return, optional DOC/ligand pathways로 그 식생효과를 process-wise 구현한다.

# 다른 문헌과의 관계
Moulton 2000의 strong positive plant effect는:
- Larsen 2023: erosion can dominate vegetation signal
- Oeser 2020: NPP increase need not increase weathering
- Donaldson 2026: inherited weathering can mask current vegetation differences
와 모순이라기보다 환경별 limiting process가 다름을 보여준다.

따라서:
```
vegetation effect
= context dependent
```
가 최종 결론이다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS quantitative vegetation state를 Moulton field enhancement factor에 직접 연결하는 것은 unsupported NEW COUPLING이므로 하지 않는다.

# 한계
- basalt
- Iceland climate
- tree vs barren endmember
- current Gounsa postfire forest recovery와 다름
- hillslope transport dynamics 직접 없음
- mineral-specific factors transferable하지 않음

# 최종 판정
- **핵심 보조 채택: isolated positive vascular-plant weathering evidence**
- process sign/possibility evidence only
- numerical multiplier source로 사용 금지

# 참고 링크 / DOI
https://doi.org/10.2475/ajs.300.7.539
