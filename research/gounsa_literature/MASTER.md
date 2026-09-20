# Gounsa Literature Master

업데이트: 2026-09-21

이 문서는 전체 문헌검토의 살아 있는 통합본이다. 논문별 세부 내용은 `papers/`, 모델 계보는 `models/`, 확정 결정은 `decisions/`에 저장한다.

## 현재 고정 원칙

- COPLAS 최종모델 근거에서 제외
- MUSLE 최종 산지 유수침식식에서 제외
- quantitative vegetation state 우선
- genuine 2D 우선
- interrill/rill 또는 rainfall-driven/flow-driven 구분
- 기존 published equation 우선
- 논문에 없는 모델 간 연결은 반드시 새로운 coupling으로 명시
- 현장실험 상관식과 실제 수치모델을 구분
- vegetation cover를 root biomass 또는 RLD와 동일시하지 않음

## 현재 최우선 유수침식 조건

```text
genuine 2D
+ mountain/steep forest
+ quantitative vegetation state
+ interrill/rill or rainfall/flow separation
```

이 세션은 최종 유수침식 엔진을 확정하지 않았다. 아래 vertical profile, weathering, coarse fraction, fire spall 구조는 향후 선택되는 최종 erosion engine과 결합될 독립 구성요소다.

## 현재 고운사 통합구조

```text
Climate
  -> LPJ-GUESS vegetation and hydrology
  -> quantitative vegetation-to-geomorph coupling
  -> R / C-Cr / AB soil-regolith profile
  -> final 2D erosion and landscape-evolution engine
  -> elevation, soil depth, coarse fraction, sediment provenance update
  -> next vegetation and hydrology state
```

세부 결정: [2026-09-21_CURRENT_GOUNSA_ARCHITECTURE.md](decisions/2026-09-21_CURRENT_GOUNSA_ARCHITECTURE.md)

## 1. 토양과 풍화층의 기준구조

기존의 고정 단일 토심 구조 대신 다음을 기능적으로 분리한다.

```text
R -> C/Cr -> AB
```

- R: 비교적 신선한 기반암
- C/Cr: 풍화되었고 물과 뿌리가 접근할 수 있으나 상대적으로 비이동성인 기반물질
- AB: 물리적으로 이동 가능한 상부토양 또는 PDZ에 가까운 층

최소 상태:
```text
H_AB
H_C
z_R
W_AB
W_C
CF_surface
CF_AB
CF_C
```

고운사 현장관찰상 뿌리는 C/Cr까지 들어갈 수 있으므로
```text
Z_root > H_AB
```
를 허용한다.

근거:
- Yoo & Mudd (2008): PDZ와 CAZ의 기능적 분리
- Lapides et al. (2024): LPJ-GUESS에 weathered-bedrock water storage 추가
- Welivitiya et al. (2019): 수직 particle-size profile과 landform 동시진화
- van der Meij et al. (2020): 다층 profile에서 gravel, sand, silt, clay, water balance 결합

세부 결정: [2026-09-21_SOIL_REGOLITH_COARSE_FRAGMENT_ARCHITECTURE.md](decisions/2026-09-21_SOIL_REGOLITH_COARSE_FRAGMENT_ARCHITECTURE.md)

## 2. 풍화와 토양생산

두 경계를 분리한다.

```text
R -> C/Cr
C/Cr -> AB
```

### R -> C/Cr
Pelletier et al. (2013)의 depth-dependent production 구조를 장기 풍화전선의 근거로 사용한다.

원 논문의 기본형:
```text
P = P0 exp[-h cos(theta) / h0]
P0 = a exp(b EEMT)
```

고운사 제안형:
```text
P_R_to_C = P0(EEMT) exp[-(H_AB + H_C) cos(theta) / h0_R]
```

이 식은 Pelletier 원식을 고운사 두 층 구조로 확장한 새로운 coupling이다.

### C/Cr -> AB
R->C와 동일한 식을 중복사용하지 않는다. root fracture, tree throw, bioturbation 등 물리적 교란과정을 별도 검토한다.

Gabet & Mudd (2010)는 목본의 root fracture와 tree throw를 soil production에 명시적으로 연결한 핵심 모델근거다. FineRootC에 임의 계수를 곱해 그대로 이식하는 것은 원 논문 방식이 아니다.

### 한국 analogue
Byun et al. (2015)은 대관령에서 토양생산률의 토양두께 의존성을 정량화했다. 현재 채팅에서 복구된 함수는
```text
P_s = (54 ± 1) exp[-(0.0068 ± 0.0026) h]
```
이며 P_s는 m Myr^-1, h는 cm로 해석했다. 고운사 직접계수가 아니라 한국 산지의 크기차수 제약으로만 사용한다.

## 3. LPJ-GUESS와 C/Cr 수분

Lapides et al. (2024)은 LPJ-GUESS에서 상부 soil water storage와 하부 weathered-bedrock rock-moisture storage를 분리하는 직접 선례다.

고운사에서는 최소한
```text
W_AB
W_C
```
를 분리하는 방향을 채택한다.

dynamic H_AB와 H_C에 따라 storage capacity를 바꾸는 기능, coarse fraction을 storage/infiltration에 반영하는 기능, 셀 간 same-day run-on은 Lapides 원 논문에 없는 새로운 coupling이다.

모델 메모: [LPJ_GUESS_BedrockHydrology.md](models/LPJ_GUESS_BedrockHydrology.md)

## 4. coarse fraction과 수직 토양조성

표면 석력만 하나의 고정값으로 두지 않는다.

최소:
```text
CF_surface
CF_AB
CF_C
```

가능하면 비율 대신 질량상태를 직접 추적한다.
```text
M_fine
M_coarse
CF = M_coarse / (M_coarse + M_fine)
```

첫 구현에서는
```text
fine < 2 mm
coarse > 2 mm
```
의 두 그룹으로 시작하는 것이 가장 단순하다.

변화경로:
- 세립질 선택적 침식 -> CF_surface 증가
- C/Cr 노출 -> surface composition이 C/Cr 조성에 접근
- coarse deposition -> CF_surface 변화
- coarse export -> CF_surface 감소 가능
- fire spall generation -> 신규 coarse material 추가

SSSPAM과 HydroLorica 계열은 이런 vertical composition을 상태변수로 추적할 수 있다는 구조적 선례다. 전체 모델을 이식하는 것이 아니라 profile-state 구조를 차용한다.

LORICA 계보: [LORICA_HydroLorica_ChronoLorica.md](models/LORICA_HydroLorica_ChronoLorica.md)

## 5. fire spall

fire spall은 기존 coarse fragment나 C/Cr와 동일한 상태로 합치지 않는다.

최소:
```text
M_spall
```

가능하면:
```text
M_spall_mobile
M_spall_stable
```

### 생성
Buckman et al. (2021)은 spall thickness, affected area, rock mass를 정량화했다.

고운사 사건단위 제안식:
```text
Delta M_sp = rho_r A_exposed d_sp f_sp
```
이것은 Buckman의 thickness × affected area를 질량보존 형태로 재구성한 새로운 coupling이다.

### 이동
Pala et al. (2025)은 산불 후 debris-flow deposit에서 형태적으로 spall로 판정된 암편이 1.3–36.6%를 차지한 사례를 보고했다. 그러나 일부는 syn-flow fragmentation일 가능성이 있어 완전한 provenance 판별은 아니다.

### 잔류와 armour
Shtober-Zisu et al. (2018)은 일부 spall이 장기간 재와 세립질 물질을 포획할 수 있음을 보여준다.

Nyssen et al. (2001)과 Zavala et al. (2010)은 fire-spall 연구는 아니지만 일반 surface rock fragments가 soil loss를 낮출 수 있다는 직접 조작실험 근거를 제공한다.

따라서 spall에는 상반된 두 효과가 있다.
```text
new coarse sediment supply -> total mobile sediment 증가 가능
stable surface cover -> fine-soil erosion 감소 가능
```

세부 결정: [2026-09-21_FIRE_SPALL_AND_ARMOUR_DECISION.md](decisions/2026-09-21_FIRE_SPALL_AND_ARMOUR_DECISION.md)

## 6. fire spall의 현재 문헌공백

현재 확인한 문헌 범위에서는 산불피해 사면에서 spall을 유지한 처리와 제거한 처리를 직접 비교해 runoff와 fine-soil loss 변화를 정량화한 연구를 찾지 못했다.

따라서
```text
fire spall -> soil loss 몇 % 증가 또는 감소
```
라는 보편계수는 현재 없다.

고운사에서 자연 spall 유지구, 제거구, 가능하면 고정구를 비교해 runoff, <2 mm soil loss, coarse export를 분리 측정하는 현장실험이 높은 가치가 있다.

## 7. 식생과 지형 coupling

COPLAS의 site-normalized biomass 식은 최종근거에서 제외한다.

COPLAS에서 확인한 문제:
- normalized biomass 1은 생태학적 포화상태가 아님
- site mean/std에 의존
- leaf가 total diffusion을 바꾸어 splash와 creep이 함께 변화
- big-leaf 구조
- LPJ-GUESS pool과 정의 불일치

결정: [2026-09-21_COPLAS_EXCLUSION_AND_REPLACEMENT.md](decisions/2026-09-21_COPLAS_EXCLUSION_AND_REPLACEMENT.md)

### canopy
Istanbulluoglu & Bras (2005)의 실제 vegetation cover fraction 기반 관계를 우선 참고한다.
```text
K_d = K_b exp(-alpha V)
```

LPJ-GUESS LAI에서 V 또는 FPC를 계산하는 연결은 새로운 coupling이다.

### root
FineRootC를 COPLAS 방식으로 정규화해 바로 erodibility에 넣지 않는다. absolute root biomass, root density, RLD, root cohesion 등 실제 침식저항과 직접 연결되는 published relation을 우선 조사한다.

### litter
SurfaceLitC의 site normalization을 사용하지 않는다. litter mass 또는 litter cover와 flow resistance의 정량관계를 별도 문헌에서 찾는다.

## 8. 질량보존 원칙

다음 모든 과정은 명시적인 mass transfer로 처리한다.
```text
R -> C/Cr
C/Cr -> AB
AB erosion
deposition
spall generation
spall transport
```

임의의 mass scale을 넣어 DEM 변화만 맞추는 방식을 허용하지 않는다.

## 9. 시간척도

일 또는 사건:
- LPJ-GUESS vegetation and hydrology
- runoff and run-on
- infiltration
- erosion and sediment transport
- disturbance-related surface update

연 또는 geomorphic step:
- weathering-front movement
- C/Cr->AB soil production
- profile composition update

장기:
- landscape evolution
- drainage reorganization
- soil-regolith coevolution

2025년 이후 1년 규모 검증에서는 자연 풍화전선 이동보다 vegetation recovery, runoff, fine-soil loss, coarse-fragment mobility, surface armour가 중요하다.

## 10. 고운사 현장자료에 대한 주의

현재 대화에서 사용된 고운사 조사값 중 평균 soil depth 21.6 cm, surface gravel ratio 48%, bedrock exposure 28%가 보고되었으나 이 수치가 prefire map, postfire field measurement, 또는 결합자료 중 무엇인지 명확히 분리되지 않았다. 따라서 이를 prefire initial condition이라고 단정하지 않는다.

현재 상부 20 cm가 석력 위주라는 현장관찰 역시 산불 이후 20 cm의 fine soil이 전부 제거되었다는 증거가 아니다. 가능한 상태는 기존 skeletal soil, selective fine loss, C/Cr exposure, fire spall addition, coarse export의 결합이다.

## 11. unresolved gaps

1. genuine-2D mountain erosion engine 최종선정
2. quantitative root state -> erodibility relation
3. litter mass/cover -> flow resistance relation
4. C/Cr->AB production law와 parameter
5. coarse fraction -> hydrology relation
6. fire-spall mobile/stable fraction
7. fire-spall entrainment threshold
8. surface armour function
9. 고운사 초기 vertical CF(z)
10. pedogenic A/B/C와 geomorphic PDZ/CAZ의 operational mapping

## 12. 이번 세션 핵심 APA 참고문헌

Buckman, S., Morris, R. H., & Bourman, R. P. (2021). Fire-induced rock spalling as a mechanism of weathering responsible for flared slope and inselberg development. *Nature Communications, 12*, 2150. https://doi.org/10.1038/s41467-021-22451-2

Byun, J., Heimsath, A. M., Seong, Y. B., & Lee, S. Y. (2015). Erosion of a high-altitude, low-relief area on the Korean Peninsula: Implications for its development processes and evolution. *Earth Surface Processes and Landforms, 40*(13), 1730–1745. https://doi.org/10.1002/esp.3749

Gabet, E. J., & Mudd, S. M. (2010). Bedrock erosion by root fracture and tree throw: A coupled biogeomorphic model to explore the humped soil production function and the persistence of hillslope soils. *Journal of Geophysical Research: Earth Surface, 115*, F04005. https://doi.org/10.1029/2009JF001526

Istanbulluoglu, E., & Bras, R. L. (2005). Vegetation-modulated landscape evolution: Effects of vegetation on landscape processes, drainage density, and topography. *Journal of Geophysical Research: Earth Surface, 110*(F2), F02012. https://doi.org/10.1029/2004JF000249

Lapides, D. A., Hahm, W. J., Forrest, M., Rempe, D. M., Hickler, T., & Dralle, D. N. (2024). Inclusion of bedrock vadose zone in dynamic global vegetation models is key for simulating vegetation structure and function. *Biogeosciences, 21*, 1801–1826. https://doi.org/10.5194/bg-21-1801-2024

Nyssen, J., Haile, M., Poesen, J., Deckers, J., & Moeyersons, J. (2001). Removal of rock fragments and its effect on soil loss and crop yield, Tigray, Ethiopia. *Soil Use and Management, 17*(3), 179–187. https://doi.org/10.1111/j.1475-2743.2001.tb00025.x

Pala, C., Melis, M. T., Pioli, L., Sarro, R., Loddo, S., Cinus, S., & Brunetti, M. T. (2025). Sediment generation through thermal spalling during the 2021 Montiferru Planargia wildfire and its contribution to postfire debris flows. *Scientific Reports, 15*, 30918. https://doi.org/10.1038/s41598-025-15527-2

Pawlik, Ł., Phillips, J. D., & Šamonil, P. (2016). Roots, rock, and regolith: Biomechanical and biochemical weathering by trees and its impact on hillslopes—A critical literature review. *Earth-Science Reviews, 159*, 142–159. https://doi.org/10.1016/j.earscirev.2016.06.002

Pelletier, J. D., et al. (2013). Coevolution of nonlinear trends in vegetation, soils, and topography with elevation and slope aspect. *Journal of Geophysical Research: Earth Surface, 118*, 741–758. https://doi.org/10.1002/jgrf.20046

Quijano-Baron, J., Saco, P. M., & Rodriguez, J. F. (2022). Modelling the effects of above and belowground biomass pools on erosion dynamics. *Catena, 213*, 106123. https://doi.org/10.1016/j.catena.2022.106123

Shtober-Zisu, N., Brook, A., Kopel, D., Roberts, D., Ichoku, C., & Wittenberg, L. (2018). Fire induced rock spalls as long-term traps for ash. *Catena, 162*, 88–99. https://doi.org/10.1016/j.catena.2017.11.021

van der Meij, W. M., Temme, A. J. A. M., Wallinga, J., & Sommer, M. (2020). Modeling soil and landscape evolution – the effect of rainfall and land-use change on soil and landscape patterns. *SOIL, 6*, 337–358. https://doi.org/10.5194/soil-6-337-2020

van der Meij, W. M., Temme, A. J. A. M., Binnie, S. A., & Reimann, T. (2023). ChronoLorica: Introduction of a soil–landscape evolution model combined with geochronometers. *Geochronology, 5*, 241–261. https://doi.org/10.5194/gchron-5-241-2023

Welivitiya, W. D. D. P., Willgoose, G. R., & Hancock, G. R. (2019). A coupled soilscape–landform evolution model: Model formulation and initial results. *Earth Surface Dynamics, 7*, 591–607. https://doi.org/10.5194/esurf-7-591-2019

Yoo, K., & Mudd, S. M. (2008). Toward process-based modeling of geochemical soil formation across diverse landforms: A new mathematical framework. *Geoderma, 146*(1–2), 248–260. https://doi.org/10.1016/j.geoderma.2008.05.029

Zavala, L. M., Jordán, A., Bellinfante, N., & Gil, J. (2010). Relationships between rock fragment cover and soil hydrological response in a Mediterranean environment. *Soil Science and Plant Nutrition, 56*(1), 95–104. https://doi.org/10.1111/j.1747-0765.2009.00429.x

박경, 임주훈, 이영근. (2009). *대형산불피해지의 지표지질 변화*. 국립산림과학원 연구보고 09-06. 국립산림과학원.

김만일, 추창오. (2023). 산불 영향에 따른 토층의 광물학적 특성 변화에 관한 연구. *지질공학, 33*(1), 69–83. https://doi.org/10.9720/KSEG.2023.1.069
