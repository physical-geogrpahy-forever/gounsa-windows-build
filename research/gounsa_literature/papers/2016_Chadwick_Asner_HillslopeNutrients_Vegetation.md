# 서지정보
Chadwick, K. D., & Asner, G. P. (2016). Tropical soil nutrient distributions determined by biotic and hillslope processes. *Biogeochemistry, 127*(2-3), 273-289. DOI: 10.1007/s10533-015-0179-z.

# 이 논문을 찾은 이유
사면 침식/풍화가 공급한 rock-derived nutrients가 vegetation에 의해 다시 보유되고, 이 양분분포가 다시 forest carbon dynamics에 영향을 줄 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- hillslope field toposequence study
- soil geochemistry
- ecosystem nutrient cycling

# 공간 구조
- 16 hillslopes
- contrasting hillslope morphology
- toposequences
- surface to 1 m soil

# 적용 환경
- lowland Peruvian Amazon
- terra firme tropical forest
- strongly weathered soils

# 핵심 과정
- hillslope erosion and rejuvenation
- rock-derived nutrient distribution
- biological nutrient retention
- vertical nutrient recycling
- potential forest carbon response

# 식생 입력
- existing tropical forest ecosystem
- biotic nutrient uptake/recycling
- no dynamic vegetation model

# 핵심 결과
Ca와 P는 subsurface보다 surface soil에서 덜 depleted되었다.

Exchangeable Ca와 Mg도 surface soil에 강하게 농축되어 있었다.

해석:
```
hillslope erosion / rejuvenation
 -> rock-derived nutrient resupply
 -> biological uptake and surface retention
 -> nutrient spatial pattern
 -> possible forest C dynamics
```

특히 Ca는 ecosystem 내에서 강하게 cycling되는 것으로 해석된다.

# 고운사에 직접 사용할 수 있는 부분
현재 new coupling:
```
weathering nutrient release
 -> LPJ-GUESS-CNP
 -> vegetation recovery
```
를 지지하는 hillslope-level field evidence.

또 nutrient state는 local weathering flux만이 아니라:
- erosion/rejuvenation
- downslope redistribution
- biological retention
의 결과라는 점이 중요하다.

# 새로운 coupling이 필요한 부분
SWEHR/Landlab physical redistribution과 chemical nutrient pools를 같은 spatial mass balance에서 연결해야 한다.

# 한계
- tropical Amazon
- mature ecosystem
- fire recovery 직접 없음
- weathering rate numerical model 아님

# 최종 판정
- **채택: hillslope geomorphology -> nutrient -> vegetation feedback 핵심 constraint**
- nutrient return을 local-only box로 두지 않을 필요성을 제기

# 참고 링크 / DOI
https://doi.org/10.1007/s10533-015-0179-z
