# 서지정보
Gérard, F., Blitz-Frayret, C., Hinsinger, P., & Pagès, L. (2017). Modelling the interactions between root system architecture, root functions and reactive transport processes in soil. Plant and Soil, 413, 161-180.
DOI: 10.1007/s11104-016-3092-x

# 이 논문을 찾은 이유
식생의 뿌리를 단순 biomass multiplier가 아니라 공간적으로 분포한 root state로 reactive transport와 실제 결합한 numerical model을 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- root system architecture + multicomponent reactive transport coupling

# 공간 구조
- 2D soil domain
- x 75 cells, z 100 cells
- 총 7500 control volumes
- y-direction thickness 1.5 m
- 80 d simulation
- hillslope routing은 아님

# 적용 환경
- alkaline soil rhizosphere
- hydroxyapatite에서 P 획득 사례
- 산림사면 아님

# 핵심 과정
- ArchiSimple root system architecture
- MIN3P reactive transport
- dynamic spatial root surface density
- P and Ca uptake
- root-induced pH change
- mineral dissolution
- solute transport
- geochemical equilibrium/kinetics

# 식생 입력
- explicit root architecture
- root surface density per control volume
- nutrient uptake
- root growth updated during simulation

# 핵심 식
ArchiSimple의 root segments를 각 MIN3P control volume의 root surface density로 변환해 chemical source/sink에 전달한다.

ArchiSimple RSA(t) -> root surface density(x,z,t) -> uptake and rhizosphere pH -> MIN3P chemistry -> mineral dissolution / nutrient availability

# 파라미터와 단위
- root surface density: m2 root surface per m3 bulk soil
- 75 x 100 control volumes
- simulation: 80 d
- maximum reactive-transport timestep: 1 d

# 원 논문의 구현 범위
- Fortran-C++ sequential coupling
- spatially explicit roots와 multicomponent reactive transport를 실제 결합
- hydroxyapatite dissolution과 P acquisition 계산
- root-induced pH change가 mineral-derived nutrient acquisition에 미치는 영향 분석

# 고운사에 직접 사용할 수 있는 부분
1. LPJ-GUESS root state를 chemistry에 넘길 때 단일 biomass factor보다 depth/spatial distribution을 사용하는 선례.
2. root uptake와 rhizosphere chemistry를 mineral reaction에 연결하는 실제 implemented model.
3. grid cell별 root source/sink interface 설계 참고.

# 새로운 coupling이 필요한 부분
- LPJ-GUESS FineRootC/RLD -> root surface density 변환은 NEW COUPLING.
- forest PFT root architecture를 ArchiSimple crop architecture로 직접 대체할 수 없음.
- hillslope shallow/deep/lateral hydrology와 연결하려면 별도 coupling 필요.

# 한계
- 산림사면 모델 아님.
- 지형진화 없음.
- rhizosphere scale, 80 d.
- 해당 application에서는 water uptake feedback을 핵심으로 사용하지 않았음.
- hydroxyapatite/P 결과를 sandstone total weathering coefficient로 일반화할 수 없음.

# 최종 판정
- 채택
- 역할: root-state -> reactive transport/mineral reaction interface의 mechanistic model precedent.

# 참고 링크 / DOI
- https://doi.org/10.1007/s11104-016-3092-x