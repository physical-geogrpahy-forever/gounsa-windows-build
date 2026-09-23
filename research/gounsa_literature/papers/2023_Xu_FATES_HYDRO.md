# 서지정보
Xu, X., et al. (2023). Quantification of hydraulic trait control on plant hydrodynamics and risk of hydraulic failure within the Functionally Assembled Terrestrial Ecosystem Simulator (FATES-HYDRO V1.0). Geoscientific Model Development, 16, 6267–? . https://doi.org/10.5194/gmd-16-6267-2023

# 이 논문을 찾은 이유
고운사 식생엔진 후보인 FATES가 단순 root biomass만 제공하는지, 아니면 토층별 뿌리분포와 식물수리학을 짧은 시간간격으로 실제 계산하는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 개발
- cohort vegetation demography + plant hydraulics

# 공간 구조
- FATES demographic cohort / patch 구조
- host land model의 vertical soil layers와 연결
- FATES patch 자체는 내부 x-y 좌표가 없는 면적분율

# 적용 환경
- FATES site/ecosystem simulations
- 고운사에는 postfire cohort별 수분스트레스와 layer root uptake를 geomorph/hydrology state와 연결하는 선례로 중요

# 핵심 과정
- leaf, stem, transporting root, absorbing root hydraulic compartments
- rhizosphere-to-root-to-stem-to-leaf water flow
- organ water potential
- hydraulic conductance
- vulnerability / hydraulic failure risk
- fine-root biomass and specific root length
- soil-layer-specific root weighting

# 식생 입력
- cohort/PFT fine-root biomass
- specific root length
- root vertical distribution parameters
- leaf/stem/root hydraulic traits
- cohort size and carbon state

# 핵심식/구조
FATES-HYDRO는 water pathway를 대략 다음처럼 푼다.

```text
soil layer / rhizosphere
 -> absorbing root
 -> transporting root
 -> stem
 -> leaf
```

각 hydraulic compartment의 water potential과 conductance를 subdaily timestep에서 계산한다.

총 fine-root surface area는 fine-root biomass와 specific root length에 의해 결정되며, soil-layer conductance는 vertical root distribution과 layer root biomass weighting의 영향을 받는다.

# 파라미터와 단위
- plant/soil hydraulic calculation: 30 min class timestep
- organ compartments: leaf, stem, transporting root, absorbing root
- root spatial weighting: vertical soil-layer distribution

# 원 논문의 구현 범위
- FATES cohort physiology와 host soil hydrology를 연결
- host model이 infiltration, interlayer soil-water movement, drainage 등을 계산
- FATES-HYDRO가 cohort별 water uptake와 internal hydraulic state를 계산

# 고운사에 직접 사용할 수 있는 부분
1. cohort별 fine-root biomass
2. soil-layer별 root contribution
3. plant hydraulic stress at subdaily timestep
4. root litter/turnover와 기존 FATES demography 연결
5. 외부 hillslope hydrology가 제공하는 layer soil-water state를 실제 cohort physiology로 전달할 수 있는 구조

# 필요한 새로운 coupling
고운사에서는 erosion/deposition 후 다음을 새로 처리해야 한다.
- soil layer geometry change
- root biomass truncation/burial/remapping
- soil water/C/N conservative remapping
- geomorph grid와 host-model column 간 scale exchange

이 기능들은 FATES-HYDRO의 기존 기능이 아니다.

# 한계
1. root vertical architecture는 완전한 3-D root system이 아니라 parameterized layer distribution
2. internal FATES disturbance patches는 x-y 공간좌표가 없음
3. dynamic soil-depth change는 native process가 아님
4. FATES는 CTSM/ELM 등 host stack가 필요해 구현이 무거움

# 최종 판정
- **채택 후보 핵심 근거**
- FATES가 현재 후보 중 뿌리-수리학을 가장 세밀하게 표현하는 계열 중 하나임을 확인
- 고운사에서 root biomass/RLD-like geomorphic interface를 만들 때 강한 생리적 기반 제공

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-16-6267-2023
