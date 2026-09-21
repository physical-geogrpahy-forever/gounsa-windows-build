# 서지정보
Uhlemann, S., Peruzzo, L., Chou, C., Williams, K. H., Wielandt, S., Wang, C., Falco, N., Wu, Y., Carr, B., Meldrum, P., Chambers, J., & Dafflon, B. (2024). Variations in Bedrock and Vegetation Cover Modulate Subsurface Water Flow Dynamics of a Mountainous Hillslope. *Water Resources Research, 60*(2), e2023WR036137. DOI: 10.1029/2023WR036137.

# 이 논문을 찾은 이유
산지 사면에서 bedrock structure와 vegetation cover가 subsurface flow path를 동시에 어떻게 바꾸는지 확인하여, 식생이 weathering에 화학적 forcing뿐 아니라 hydrologic pathway를 통해 작용하는 직접 evidence를 확보하기 위해 검토했다.

# 연구 유형
- hillslope field hydrology
- electrical resistivity tomography
- soil moisture/temperature monitoring
- simplified hydrological modeling
- particle tracking

# 공간 구조
- steep upper hillslope with shallow bedrock
- gentler lower hillslope with colluvium
- tree-covered upper section
- grass/veratrum lower section

# 적용 환경
- snow-dominated mountainous watershed
- East River watershed, Rocky Mountains

# 핵심 과정
- shallow lateral flow
- vertical preferential flow
- fractures
- root-associated recharge
- colluvial groundwater recharge
- snowmelt
- vegetation shading
- bedrock-dependent flow structure

# 식생 입력
- conifer locations/cover
- grass and herbaceous cover
- tree-associated root zones

dynamic vegetation model은 아니다.

# 핵심 결과
Steep, shallow-bedrock section:
```
thin soil
 -> mainly shallow lateral flow
```

하지만:
```
tree locations
 -> more vertical flow
 -> likely fracture + root preferential flow
 -> deeper rock-moisture recharge
```

Lower colluvial section:
```
vertical flow
+ upstream-driven groundwater dynamics
```
가 우세했다.

Tree-covered shallow-bedrock zones showed deeper moisture recharge signatures than nearby unvegetated areas.

# 고운사에 직접 사용할 수 있는 부분
매우 중요하다.

```
vegetation
 -> root/fracture preferential flow
 -> deeper water delivery
 -> weathering opportunity
```

를 별도 hydrologic pathway로 둘 강한 근거.

또:
```
upper steep slope
!= always deeper drainage
```

because shallow lateral flow can dominate unless fractures/roots create vertical bypass.

따라서:
- slope
- vegetation
- fracture state
를 독립 state로 유지해야 한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root distribution을:
- preferential vertical-flow probability
- fracture-access sensitivity
로 연결하는 것은 NEW COUPLING이다.

# 한계
- chemical weathering rate 직접 측정 아님
- root effect와 fracture effect 완전 분리 불가
- conifer/grass mountain system
- sandstone-specific 아님

# 최종 판정
- **핵심 채택: vegetation + fracture controlled hillslope flow-path evidence**
- root-controlled deep flow pathway를 weathering hydrology에 추가
- direct weathering coefficient source 아님

# 참고 링크 / DOI
https://doi.org/10.1029/2023WR036137
