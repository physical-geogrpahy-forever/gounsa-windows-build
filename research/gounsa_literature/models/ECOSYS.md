# ecosys model lineage

## 현재 판정
고운사 5조건에서 새로 중요해진 process-rich 비교후보.

핵심 장점은 식생을 단순 피복률로 다루지 않고 여러 plant population/PFT가 다층 수관과 다층 토양에서 빛, 물, N, P를 경쟁하며, 같은 계산영역 안에서 2D/3D 지표수·토양수 이동까지 계산할 수 있다는 점이다.

그러나 LPJ-GUESS/FATES처럼 age/size demographic cohort를 명시적으로 이동시키는 모델은 아니다. 따라서 1번은 완전 충족이 아니라 PARTIAL로 판정한다.

## 고운사 5조건

| 기준 | 판정 | 근거 |
|---|---|---|
| 1. 공간명시 cohort 구조 | PARTIAL | 실제 row-column-layer 공간은 명시적이고 여러 plant population이 경쟁하지만 age/size cohort 구조는 아님 |
| 2. 하층식생 + 천이 | STRONG/PARTIAL | tree, shrub, graminoid, moss/lichen 등 여러 PFT의 다층 경쟁과 조성변화는 강함. 산불 연구에서 seedbed/seedling regeneration과 postfire composition change가 보고됨. 다만 소스에서 독립적인 seed dispersal→new age cohort 생성 구조는 아직 확인하지 못함 |
| 3. 토양-지형모델 coupling 가능 | STRONG | 임의의 토양층, 토양수분, 뿌리분포, 토양 깊이, hydraulic state가 식생 생리에 직접 feedback. 외부 지형 변화의 soil state를 다시 매핑하기 좋은 상태변수 구조 |
| 4. 유역/지형 선례 | STRONG | Seward Peninsula Kougarok hillslope에서 연결 사면 수문과 토심 구배를 직접 모의 |
| 5. <=1 day | STRONG | 일반적으로 hourly, 일부 수치과정은 convergence에 따라 더 짧은 timestep |

## 식생 구조
공식 ecosys 설명은 식물 활동을 다음 세 수준에서 계산한다고 설명한다.
- organ
- population
- community

여러 plant populations가 동시에 존재할 수 있으며 각 population은 다층 수관과 다층 뿌리 상태를 갖는다.

고위도 적용에서 실제로 함께 표현된 PFT 예:
- evergreen tree
- deciduous tree
- evergreen shrub
- deciduous shrub
- heath
- C3 grass / graminoid
- moss
- lichen

각 PFT의 잎면적과 뿌리길이 분포는 prognostic하게 변화하고, 수관층의 광경쟁과 토양층의 물·영양염 경쟁에 직접 들어간다.

## 코드 수준 population audit, 2026-09-23
공개 GitHub 코드 `jinyun1tang/ECOSYS`의 `startq.f`에는 다음이 명시된다.

```text
PPI, PPX = initial,current population (m-2)
```

초기화 시:

```text
PPI = PPZ
PPX = PPI
PP = PPX * cell area
```

`PP`는 이후 root length, water/nutrient uptake 및 plant output 계산에 직접 사용된다.

중요한 제한:
- 현재 코드 검색에서는 `PP` population을 자연 seed dispersal 또는 age/size recruitment로 새로 생성하는 명확한 demographic routine을 확인하지 못했다.
- 따라서 ecosys의 population을 LPJ-GUESS의 age cohort와 동일시하면 안 된다.
- ecosys는 **공간명시 plant-population process model**로 분류하는 편이 정확하다.

## 하층식생과 조성변화
Mekonnen et al. 2018의 Arctic tundra 적용:
- deciduous shrub
- evergreen shrub
- graminoid
- nonvascular vegetation
을 동시에 경쟁시켰다.

온난화에 따른 nutrient cycling과 광경쟁 변화만으로 PFT 상대 우점도가 크게 바뀌었다.

2024 DOE/NGEE Arctic 산불 연구 자료에서는 ecosys 산불 모의가 다음을 바꾸는 것으로 설명된다.
- surface vegetation
- soil organic carbon
- seedbed quality
- seedling regeneration
- soil moisture
- PFT competition

즉 postfire shrub-herb competition 및 조성변화 자체는 명시적으로 다룬다.

다만 현재 확인 범위에서 이것이 독립적인 종자확산-발아-연령 cohort 생성 알고리즘인지, 기존 PFT population의 regeneration/growth 상태변화인지 명확히 분리되지 않았다. 이 부분은 계속 코드 감사가 필요하다.

## 2D/3D 공간과 수문
공식 model functions 문서:
- 모든 flux equation은 row-column-layer cell matrix에서 3D로 풀 수 있음
- 1D, 2D, 3D 도메인 사용 가능
- cell별 soil properties를 다르게 줄 수 있음
- water, heat, C, N, P 및 solute transport가 cell 사이에서 계산됨

따라서 실제 지형격자에서 soil depth와 hydraulic property를 공간적으로 다르게 두고, 연결 수문을 계산할 수 있다는 점이 핵심이다.

## 핵심 지형 선례: Mekonnen et al. 2021
Kougarok Hillslope, Seward Peninsula, Alaska.

- coupled transect ecosys
- 실제 crest → midslope → lower-slope 위치
- 서로 다른 soil depth와 drainage
- shrub, graminoid, nonvascular PFT 동시 모의
- PFT biomass 관측과 모델의 일치: R2 약 0.89
- 잘 배수되고 얕은 능선에서는 water stress로 shrub biomass가 제한
- 중사면에서는 적정 수분과 N 공급이 shrub 성장을 강화
- 하부사면에서는 포화/저산소 조건이 식생을 제한

이는 고운사에서 요구하는

```text
terrain position
 -> soil water / drainage / soil depth
 -> root water and nutrient uptake
 -> PFT competition / biomass
```

의 직접적인 published precedent다.

## 시간 구조
최근 ecosys 적용은 일반적으로 hourly land/ecosystem calculations를 사용한다.
공식 설명은 seconds-to-decades 범위를 지원한다고 밝힌다.

따라서 폭우나 지형변화 직후의 토양수분 상태를 하루보다 짧은 간격으로 식생 생리에 반영할 수 있다는 점은 LPJ-DH보다 유리하다.

## 토심 변화 coupling
토심 변화가 ecosys 자체 geomorph process로 내장된 것은 아니다.
그러나 모델은 토양층별로 다음 상태를 갖는다.
- water / ice
- temperature
- C/N/P
- gases / solutes
- root length and uptake
- hydraulic properties

따라서 고운사 geomorph engine이 erosion/deposition으로 layer thickness를 바꾸면 다음의 새로운 coupling이 필요하다.

```text
geomorph event
 -> new layer thickness / surface elevation
 -> conservative remap of water, C, N, P and solutes
 -> truncate/bury/remap root profiles
 -> resume hourly ecosys
```

이 작업은 새 coupling이지만, soil-water-storage 하나만 가진 단순 vegetation model보다 상태 연결은 훨씬 물리적으로 명시적이다.

## fire
ecosys는 fire impact studies에 실제 사용되었다.
최근 tundra fire applications에서 fire가 surface vegetation, soil thermal state, active-layer depth, nutrient cycling, seedbed quality 및 vegetation composition을 바꾸는 것으로 모의됐다.

고운사에 중요한 점은 fire 자체보다도 fire 이후 soil moisture 변화가 shrub establishment/competitiveness와 herbaceous competition을 바꾸는 구조다.

## 장점
1. 실제 2D/3D 연결 공간
2. hourly 이하의 짧은 timestep
3. tree/shrub/herb/nonvascular PFT 동시 경쟁
4. 다층 수관 + 다층 뿌리
5. 토양수분, 영양염, 저산소, 동결융해와 식생의 양방향 feedback
6. hillslope topography 적용 선례
7. soil depth와 hydraulic heterogeneity를 직접 줄 수 있음
8. 공개 Fortran source가 존재함

## 중요한 한계
1. age/size cohort demography가 아니다.
2. 개별목 구조가 없다.
3. 자연 seed dispersal→recruitment→new age cohort가 코드상 어느 수준까지 내생적인지 아직 불확실하다.
4. 숲의 수목 size structure/stand structure를 LPJ-GUESS, FATES, FORMIND처럼 직접 재현하는 목적에는 약하다.
5. 고운사 온대 산림 수종/PFT parameterization이 필요하다.
6. dynamic erosion/deposition 후 soil/root state remapping은 새 coupling이다.

## 현재 역할
**상위 비교후보로 유지.**

특히 조건 3, 4, 5와 하층식생의 생리적 경쟁은 현재 조사한 모델 중 매우 강하다.

그러나 사용자가 요구한 1번 `cohort structure`를 엄격하게 적용하면 LPJ-GUESS/FATES보다 아래에 둬야 한다.

따라서 ecosys를 최종 vegetation engine으로 바로 채택하기보다 다음 역할이 적절하다.

```text
LPJ-GUESS/FATES = demographic-cohort benchmark
ecosys           = fine-time-step hillslope plant-soil competition benchmark
MEDFATE          = implementation-friendly spatial cohort comparator
LandscapeDNDC    = hourly mountain forest benchmark
```

## 다음 검증
1. ecosys plant population density가 natural mortality/recruitment로 바뀌는 코드 경로를 추가 감사
2. fire 이후 seedling regeneration 구현식 확인
3. forest tree age/size structure를 별도로 표현할 수 있는지 확인
4. soil-layer geometry를 restart 중 변경할 수 있는지 확인
5. 고운사 규모의 2D grid 계산비용 확인

## 핵심 참고문헌
- Grant, R. F. ecosys model development papers and official Ecosys Modelling Project documentation.
- Mekonnen, Z. A., Riley, W. J., Grant, R. F., et al. (2018). Accelerated Nutrient Cycling and Increased Light Competition Will Lead to 21st Century Shrub Expansion in North American Arctic Tundra. Journal of Geophysical Research: Biogeosciences. https://doi.org/10.1029/2017JG004319
- Mekonnen, Z. A., Riley, W. J., Grant, R. F., et al. (2021). Topographical Controls on Hillslope-Scale Hydrology Drive Shrub Distributions on the Seward Peninsula, Alaska. Journal of Geophysical Research: Biogeosciences, 126. https://doi.org/10.1029/2020JG005823
- DOE ESS / NGEE Arctic fire application materials, 2024.
- Public source code: https://github.com/jinyun1tang/ECOSYS
