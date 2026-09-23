# 서지정보
Tang, J., Miller, P. A., Crill, P. M., Olin, S., & Pilesjö, P. (2015). Investigating the influence of two different flow routing algorithms on soil–water–vegetation interactions using the dynamic ecosystem model LPJ-GUESS. Ecohydrology, 8, 570–583. https://doi.org/10.1002/eco.1526

# 이 논문을 찾은 이유
2014 LPJ-DH가 단일-flow routing에 한정된 일회성 개발인지, 이후 더 realistic한 multi-flow routing으로 확장되어 vegetation-carbon feedback까지 검증됐는지 확인하기 위해 검토했다.

# 연구 유형
- dynamic ecosystem model hydrological-routing comparison
- arctic-enabled LPJ-GUESS / LPJ-DH lineage

# 공간 구조
- DEM-based distributed catchment routing
- single-flow algorithm과 triangular form-based multiple-flow algorithm 비교
- grid-cell water connectivity가 vegetation and carbon estimates에 미치는 영향을 평가

# 적용 환경
- northern peatland catchment
- permafrost와 peatland hydrology 포함
- flat/low terrain의 flow partition 문제가 중요한 환경

# 핵심 과정
- topographic flow accumulation and redistribution
- soil-water state feedback to LPJ-GUESS vegetation
- vegetation and carbon flux response
- multiple-flow scheme이 flat areas와 convergent flow를 더 현실적으로 표현

# 식생 및 cohort
- LPJ-GUESS dynamic vegetation structure를 사용
- 기존 LPJ-DH 계보의 cohort competition, establishment, growth and mortality framework 유지

# 시간 구조
- LPJ-GUESS ecological/water-balance daily framework
- routing과 long-term outputs를 연결

# 고운사에 직접 사용할 수 있는 부분
- 산지/유역에서 D8-style single routing만 쓰지 않고 multiple-flow water redistribution을 vegetation model과 결합한 precedent
- 지형유도 수분재분배가 carbon/vegetation 결과를 변화시킨다는 검증

# 새로운 coupling이 필요한 부분
- 고운사 true 2D geomorph hydrology와 LPJ-GUESS state exchange
- dynamic soil-depth remapping

# 한계
- peatland/permafrost target
- modern code availability가 제한적
- physically based 3D groundwater model보다는 routing abstraction이 단순

# 최종 판정
- LPJ-DH 계보의 강한 보조근거
- 고운사에서 single-flow만을 고집하지 않고 terrain-driven multi-direction water redistribution을 고려해야 한다는 근거
