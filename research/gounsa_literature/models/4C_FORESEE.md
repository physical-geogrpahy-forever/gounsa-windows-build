# 4C / FORESEE

## 현재 판정
유럽 온대림용 stand-scale process-based cohort model. tree cohort의 regeneration, fine root, litter, 다층 토양수분은 강하지만 하층식생은 generic ground vegetation이어서 고운사 산불 후 초본-관목 천이에는 제한적이다.

## 식생 표현
- species/age/dimension이 같은 나무를 tree cohort로 묶음
- cohort별 foliage, fine roots, sapwood, heartwood, phenology
- cohort 간 light, water, nutrient competition
- regeneration module이 새로운 tree cohort establishment 계산
- distance-independent, 수평 위치는 추적하지 않음

## 공간
- stand/patch scale
- 약 100 m2부터 수 ha까지 적용 가능
- native inter-patch seed dispersal/GIS landscape coupling은 핵심 기능이 아님

## 시간
- daily: soil water, phenology 등
- weekly: photosynthesis
- annual: C allocation, dimensional growth, mortality

## 뿌리와 litter
- cohort별 fine-root biomass
- rooting zone vertical layers
- 각 cohort water uptake는 토층별 fine-root share에 비례
- foliage/fine-root/sapwood senescence
- dead fine/coarse roots와 ground vegetation litter가 토층 organic matter pool로 전달

## 하층식생
- ground vegetation의 interception, transpiration, root/litter effect 존재
- 대표적으로 Calamagrostis arundinacea에 기반한 generic ground vegetation parameterization 사용
- 2020 model evaluation 논문도 ground vegetation growth가 아직 충분히 상세하지 않은 missing/weak process임을 지적

따라서 tree regeneration은 내장되어 있으나 species-rich herb/shrub succession model로 보아서는 안 된다.

## 고운사 장점
- 개체목보다 단순한 cohort structure
- 작은 stand/patch에 적용 가능
- tree regeneration 내장
- fine roots와 vertical root distribution
- litter/SOM C/N
- daily soil water

## 고운사 한계
- shrub/herb species demography 부족
- fire 이후 herb -> shrub -> tree replacement를 endogenous하게 표현하기 어려움
- physiology는 hourly가 아니라 daily/weekly
- native spatial landscape linkage 약함

## 판정
**B급 후보 / tree-cohort benchmark.**
MEDFATE보다 shrub/herb가 약하고 LandscapeDNDC보다 시간해상도가 낮다. 다만 tree regeneration + roots/litter를 갖춘 비교적 경량 cohort stand model의 좋은 선례다.

## 핵심 근거
Lasch-Born et al. (2020). Description and evaluation of the process-based forest model 4C v2.2 at four European forest sites. Geoscientific Model Development, 13, 5311-5343.
https://doi.org/10.5194/gmd-13-5311-2020
