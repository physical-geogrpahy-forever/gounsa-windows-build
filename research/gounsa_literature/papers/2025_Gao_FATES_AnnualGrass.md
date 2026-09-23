# 서지정보
Gao, X., Koven, C. D., Longo, M., Robbins, Z., Thornton, P., Hall, A., Levis, S., Rahimi, S., Xu, C., & Kueppers, L. M. (2025). California annual grass phenology and allometry influence ecosystem dynamics and fire regime in a vegetation demography model. New Phytologist, 245(6), 2480–2495. https://doi.org/10.1111/nph.20421

# 이 논문을 찾은 이유
FATES의 grass PFT가 단순한 prescribed ground cover인지, 아니면 실제 demographic recruitment, growth, mortality, competition을 수행하는지 확인하여 고운사의 explicit understory criterion을 재평가하기 위해 검토했다.

# 연구 유형
- 수치모델 적용 및 parameterization
- CLM-FATES vegetation demography + fire

# 공간 구조
- FATES patch/cohort structure
- site simulation과 California regional grid simulation
- patch는 disturbance history 기반 spatially implicit unit

# 적용 환경
- California Mediterranean annual grasslands
- fire-prone ecosystem

# 핵심 과정
- grass PFT cohort demography
- recruitment from seed
- allometric growth
- light/space/water competition
- drought-deciduous phenology
- drought mortality
- recurrent recruitment
- SPITFIRE fuel/fire feedback

# 식생 입력
- C3 annual grass PFT traits
- grass allometry
- leaf physiology
- phenology and mortality traits
- soil-water state

# 핵심식/구조
FATES는 size-dependent cohort growth, mortality and resource competition을 계산한다. 본 연구에서는 drought-deciduous phenology와 drought-driven mortality를 이용해 annual grass population과 seasonal biomass를 재현했다.

특히 논문은 recurrent recruitment를 명시적으로 언급하며, plant mortality 이후 seed로부터 새로운 recruit가 생성될 수 있음을 보여준다.

# 파라미터와 단위
- daily mean temperature and soil-water state affect phenology
- regional evaluation 2000–2020 fire regime
- model spinup from bare ground

# 원 논문의 구현 범위
California annual grassland의 구조, 생산성, phenology, fire를 FATES로 모의한다. Forest understory application 자체는 아니다.

# 고운사에 직접 사용할 수 있는 부분
- grass가 FATES에서 실제 demographic PFT로 작동한다는 직접 근거
- bare ground -> recruitment -> growth -> mortality -> litter/fire feedback 구조
- 산불 후 초기 초본단계 표현 가능성

# 새로운 coupling이 필요한 부분
- 한국 온대 초본/관목 PFT parameterization
- forest tree/shrub/grass 동시 postfire succession validation
- fine mapped hillslope coupling은 ELM-ParFlow-FATES 계보와 결합해 검증해야 함

# 한계
- grass-specific allometry/phenology parameterization이 아직 woody PFT보다 덜 성숙함
- 저자들도 grass process가 기존 tree-focused demographic models보다 덜 개발됐음을 지적함
- current detailed Tree Recruitment Scheme은 tree seedling dynamics에 더 특화됨
- grass fire mortality는 직접적인 fire-kill보다는 aboveground biomass loss 및 carbon starvation 경로로 주로 반영됨

# 최종 판정
- **채택: FATES criterion 2를 상향하는 핵심 근거**
- FATES grass는 prescribed cover가 아니라 실제 recruitment/growth/mortality를 갖는 demographic vegetation임
- 다만 forest understory grass/shrub의 parameterization과 postfire 동시 검증은 추가 필요

# 참고 링크 / DOI
https://doi.org/10.1111/nph.20421
