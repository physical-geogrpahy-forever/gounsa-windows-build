# 서지정보
Erlandsson, M., Oelkers, E. H., Bishop, K., Sverdrup, H., Belyazid, S., Ledesma, J. L. J., & Köhler, S. J. (2016). Spatial and temporal variations of base cation release from chemical weathering on a hillslope scale. *Chemical Geology, 441*, 1-13. DOI: 10.1016/j.chemgeo.2016.08.008.

# 이 논문을 찾은 이유
산림 사면에서 weathering release가 unsaturated, saturated, riparian zones 사이에서 어떻게 공간적으로 분배되는지, PROFILE 계열을 hillslope scale로 확장한 실제 사례를 확인하기 위해 검토했다.

# 연구 유형
- integrated catchment/hillslope model
- mineral-dissolution modeling
- long-term soil-water monitoring

# 공간 구조
- unsaturated soil zone
- saturated zone
- organic-rich near-stream/riparian zone
- hillslope-to-stream continuum

# 적용 환경
- boreal forested hillslope
- Northern Sweden

# 핵심 과정
- mineral dissolution
- base-cation release
- pH control
- dissolved Al effects
- DOC effects
- soil temperature
- soil moisture/hydrology
- hillslope solute export

# 식생 입력
dynamic vegetation model은 없음.

Forest influence는:
- DOC
- soil chemistry
- hydrologic state
- organic-rich riparian zone
등에 내재되어 있다.

균근 state는 고운사에서 사용하지 않는다.

# 핵심 모델
세 mineral dissolution formulations 비교:
- PROFILE
- Transition-State Theory
- Palandri & Kharaka kinetic database

In-situ dissolution is calculated as function of:
```
pH
Al
DOC
temperature
hydrologic zone
```

# 핵심 결과
- organic-rich near-stream zone이 total base-cation release에 상당한 기여
- unsaturated and saturated zones가 전체 release에 대략 비슷한 규모로 기여
- dissolution law 선택에 따라 hillslope spatial release pattern이 달라짐
- 일부 mass-balance methods는 Na/K release를 과대평가할 수 있음

# 고운사에 직접 사용할 수 있는 부분
매우 중요하다.

```
weathering
!= root-zone-only process
```

사면에서:
- unsaturated
- saturated
- downslope/riparian-like accumulation zones
의 화학환경 차이를 고려할 필요가 있다.

고운사에 명시적 riparian zone이 없더라도:
```
topographic convergence
 -> wetter / DOC-rich zones
 -> altered weathering chemistry
```
를 sensitivity로 다룰 근거가 된다.

또 WITCH/PROFILE production 후보가 hillslope-scale spatial extension이 가능함을 보여준다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS + terrain hydrology로:
- pH
- DOC
- saturation state
- wetness/convergence
를 공급하는 것은 새로운 coupling.

# 한계
- boreal forest
- base-cation release 중심
- topography evolution 없음
- dynamic forest succession 없음

# 최종 판정
- **채택: forested-hillslope spatial chemical-weathering model 핵심 precedent**
- PROFILE의 spatial extension 근거
- BioRT와 함께 hillslope chemistry engine 비교대상

# 참고 링크 / DOI
https://doi.org/10.1016/j.chemgeo.2016.08.008
