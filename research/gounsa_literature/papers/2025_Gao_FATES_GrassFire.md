# 서지정보
Gao, X., Koven, C. D., Longo, M., Robbins, Z., Thornton, P., Hall, A., Levis, S., Rahimi, S., Xu, C., Kueppers, L. M., et al. (2025). California annual grass phenology and allometry influence ecosystem dynamics and fire regime in a vegetation demography model. New Phytologist, 245, 2480-2495. DOI: 10.1111/nph.20421

# 이 논문을 찾은 이유
FATES가 실제 grass PFT를 demographic cohort로 돌리고 fire/fuel feedback까지 계산하는지 확인하기 위해 검토했다.

# 연구 유형
- cohort-based vegetation demographic model application
- grassland/fire model evaluation

# 공간 구조
- cohort + time-since-disturbance patch
- patch는 통계적 면적이며 실제 x,y 위치가 없음

# 적용 환경
- California C3 annual grasslands

# 핵심 과정
- grass phenology
- size-dependent allocation/allometry
- competition for light, water, nutrients and space
- drought mortality
- fuel dynamics
- SPITFIRE-type fire behavior and vegetation-fire feedback

# 식생 입력
- grass live biomass
- leaf and fine-root carbon allocation
- storage carbon
- soil moisture
- litter and woody fuel pools

# 하층식생 의미
FATES가 tree-only model이 아니라 실제 grass PFT demographic dynamics를 계산할 수 있음을 보여준다. FATES의 표준 PFT 체계에는 shrubs와 grasses도 존재한다.

# litter/root
- fine-root pool 및 root turnover
- leaf litter and fine-root litter
- aboveground and belowground CWD
- live grass fuel

# 산불
SPITFIRE 계열을 이용해 fuel load, moisture, rate of spread, intensity와 fire effects를 계산한다.

# 고운사에 직접 사용할 수 있는 부분
- 산불 직후 초본 단계와 숲 회복을 하나의 demographic framework 안에서 처리할 잠재력
- root/litter/fuel 상태가 모두 존재
- subdaily host-land biophysics와 결합 가능

# 새로운 coupling이 필요한 부분
- 한국 온대림 grass/shrub/tree PFT calibration
- spatial geomorph raster와 host grid/column mapping
- geomorphic disturbance 직후 patch/cohort state update

# 한계
- FATES는 standalone light model이 아니라 CLM/CTSM 또는 ELM 같은 host land model과 결합하여 사용
- 내부 disturbance patch에는 x,y 위치가 없음
- grass parameterization은 아직 forest PFT보다 개발이 덜 성숙하다는 논문 자체의 지적

# 최종 판정
- 강한 후보
- 하층 초본, root/litter, fire, succession은 매우 강함
- 구현복잡도와 공간적 implicit patch가 고운사 적용의 주요 약점

# 참고 링크 / DOI
https://doi.org/10.1111/nph.20421
