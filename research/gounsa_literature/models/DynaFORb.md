# DynaFORb

업데이트: 2026-09-23

# 목적
DynaFORb는 온대림 하층식생 community를 process-based 방식으로 계산하기 위해 Landuyt et al. (2024)이 제안한 trait-based model이다.

고운사에서의 관심은 forest models가 대개 단순화하는 grasses, herbs, ferns, dwarf shrubs 등의 하층식생을 full individual plants 없이 계산할 수 있는가이다.

# representation
- individual plants를 직접 추적하지 않음
- species-specific cover를 기본 상태량으로 사용
- cohort-based modelling에서 영감을 받은 cover-based community representation
- plant organs and vegetation height layers를 배열로 표현
- 권장 plot scale 약 0.01–1 m2

따라서 실제 landscape cohort engine보다는 **understorey submodel**에 가깝다.

# 핵심 과정
- daily phenology
- cover -> aboveground biomass allometry
- vertical light competition
- daily gross photosynthesis
- growth and maintenance carbon demand
- temperature effects
- interspecific performance comparison
- predicted annual relative cover change

# 시간구조
DynaFORb는 두 시간해상도를 분명히 구분해야 한다.

```text
daily:
 light
 phenology
 biomass proxy
 photosynthesis
 respiration/carbon demand
 competition/performance

annual:
 community cover change / main structural state
```

따라서 criterion 5는 partial이다. 하루마다 physiology-like performance는 바뀌지만 폭우 직후 community structure가 daily recruitment/mortality로 바뀌는 모델은 아니다.

# soil/water
현재 버전의 가장 큰 고운사 한계다.

논문은 water and nutrient competition을 아직 포함하지 않는다고 명시한다.
현재 performance는 mainly light, secondarily temperature에 의해 결정된다.

따라서 현재 native interface에는 다음이 없다.
- soil layer water content
- matric potential
- water table
- root water uptake
- lateral hydrology
- changing soil depth

# succession / recruitment
DynaFORb는 understorey composition and cover response를 다루지만 FATES와 같은 seed-bank demographic recruitment engine은 아니다.
현재 논문 validation도 one-year performance vs observed relative cover change 중심이며 장기 community trajectory 자체의 검증은 아직 제한적이다.

# strict five criteria
| criterion | 판정 |
|---|---|
| 1 spatial cohort/hybrid | WEAK-PARTIAL: cohort-inspired cover model, no geographic x-y cohort engine |
| 2 explicit understorey succession | STRONG-PARTIAL: species-specific herbs/ferns/dwarf shrubs, but recruitment demography limited |
| 3 soil-state coupling | FAIL currently |
| 4 terrain/catchment precedent | FAIL |
| 5 <=daily | PARTIAL: daily internal performance, annual cover update |

# 고운사 역할
production engine이 아니라 다음 용도의 benchmark다.

1. temperate forest herbaceous functional-trait parameterization
2. low-cost understorey competition structure
3. MEDFATE에서 herb recruitment/community dynamics를 추가할 때 참고
4. LPJ/FATES의 generic grass PFT보다 species-rich temperate understorey를 세분화할 때 참고

# current top tier와의 관계
- MEDFATE: water/soil/catchment는 훨씬 강하나 herb recruitment가 약함. DynaFORb biology를 참고해 보완할 여지가 있음.
- LPJ-GUESS: forest and soil-water framework가 훨씬 강함. DynaFORb는 herb biology reference.
- FATES: demographic completeness가 훨씬 강함. DynaFORb는 temperate species-level understorey performance reference.

# 최종 판정
**understorey biology benchmark. production shortlist 미진입.**

다시 검토할 조건:
- water/nutrient competition extension
- daily cover/recruitment dynamics
- overstorey model direct coupling
- landscape/catchment implementation

# 관련 문헌
- `papers/2024_Landuyt_DynaFORb.md`
