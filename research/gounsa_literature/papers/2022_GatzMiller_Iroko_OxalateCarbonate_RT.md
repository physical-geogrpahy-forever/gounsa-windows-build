# 서지정보
Gatz-Miller, H. S., Gérard, F., Verrecchia, E. P., Su, D., & Mayer, K. U. (2022). Reactive transport modelling the oxalate-carbonate pathway of the Iroko tree; Investigation of calcium and carbon sinks and sources. *Geoderma, 410*, 115665. DOI: 10.1016/j.geoderma.2021.115665.

# 이 논문을 찾은 이유
tree-root system, litter-derived oxalate, mineral weathering, solute uptake, soil chemistry를 하나의 mass-balanced reactive transport model로 연결한 사례를 찾기 위해 검토했다.

# 연구 유형
- 1D reactive transport model
- sensitivity analysis
- plant-soil geochemical coupling

# 공간 구조
- 1D vertical soil/root zone
- reactive transport column

# 적용 환경
- Iroko tree oxalate-carbonate pathway
- carbonate-free parent material
- tree rhizosphere

# 핵심 과정
- oxalate production/oxidation
- root water uptake
- root solute uptake
- mineral weathering
- Ca transport
- calcite precipitation
- pH evolution
- carbon sequestration

# 식생 입력
- root distribution / root extent
- root water uptake
- solute uptake
- litter / calcium-oxalate return pathway

# 핵심 식
개념적 구조:

```
tree/root system
 -> water and solute uptake
 -> litter / oxalate input
 -> microbial oxalate oxidation
 -> pH change
 -> mineral weathering
 -> Ca release
 -> calcite precipitation
```

model is constrained by Ca mass balance.

# 파라미터와 단위
- root uptake rates
- mineral weathering kinetics
- oxalate input/oxidation
- Ca transport
- pH / aqueous speciation
- precipitation reactions

# 원 논문의 구현 범위
tree-mediated geochemical pathway를 1D reactive transport로 직접 계산한다.

# 고운사에 직접 사용할 수 있는 부분
다음 점이 중요하다.

```
root system geometry / uptake
 + organic input
 + mineral weathering
 + nutrient/solute mass balance
```
가 하나의 RTM에서 동작 가능하다는 published precedent.

LPJ-GUESS root distribution과 nutrient uptake를 weathering chemistry에 연결할 구조적 근거가 된다.

# 새로운 coupling이 필요한 부분
- Iroko-specific oxalate pathway를 고운사 forest chemistry로 바꾸는 것은 새 coupling
- LPJ-GUESS PFT/root state를 root uptake geometry로 전달하는 것도 새 coupling

# 한계
- tropical Iroko-specific pathway
- carbonate precipitation이 핵심 목적
- sandstone soil production 직접 모델이 아님

# 최종 판정
- **보조 채택: root geometry + uptake + weathering + mass balance coupling 선례**
- 2023 2D 후속연구와 함께 root-architecture weathering 역할 검증에 사용

# 참고 링크 / DOI
https://doi.org/10.1016/j.geoderma.2021.115665
