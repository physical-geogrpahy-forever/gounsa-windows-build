# LandscapeDNDC / PSIM

## 현재 판정
고운사 5개 고정 조건 중 **공간격자, 하층식생, 토양/뿌리, 지형수문, 시간해상도는 매우 강하고 자연천이만 약한 후보**이다. 최신 LandscapeDNDC 1.37은 과거 독립 cell framework보다 공간수문 기능도 강화됐다.

## 식생 표현
PSIM은 한 simulation unit 안에서 여러 vegetation cohort를 동시에 표현한다.
- 수종별/크기별 tree cohort
- tree regeneration cohort
- grass/herb ground-vegetation cohort
- cohort별 foliage, fine roots, living wood, reserves

개체목 x,y는 추적하지 않는다.

## 시간 구조
- PSIM 생리: sub-daily / hourly
- Farquhar photosynthesis + stomatal conductance
- cohort별 respiration, C/N allocation, senescence
- canopy 2-40 layers
- 사용자 정의 soil layers

## 뿌리와 litter
- fine-root biomass 명시
- fine-root distribution by soil layers
- root growth can account for bulk density and stone content
- fine-root senescence를 litter/soil organic matter로 전달
- MeTrx가 litter/SOM C/N cycling 담당
- 현재 공식 일별 구조 출력에는 10, 20, 40, 60, 80, 120, 150 cm 깊이별 root length density가 포함됨

## 하층식생
Grass/herbaceous vegetation도 cohort로 처리되며 tree cohort와 같은 photosynthesis, respiration, allocation, senescence framework를 사용할 수 있다.

Dirnböck et al. (2020) 산지 적용에서는 한 cell 최대 7 cohort:
- ground vegetation 1
- tree regeneration 2
- overstory tree 4

모든 cohort가 light, water, N 자원을 공유/경쟁했다.

## 공간 적용 선례
Dirnböck et al. (2020):
- European Alps, Kalkalpen National Park
- 약 158 km2
- 100 x 100 m actual grid
- 15,793 cells
- hourly simulation, 2000-2014
- LiDAR/vegetation 원자료 10 x 10 m를 100 m로 aggregate
- 당시 regional setup에서는 cells 간 lateral water/energy/matter exchange 없음

## 최신 공간수문: EcHy3D
LandscapeDNDC 1.37 framework는 Crabmeat의 synchronized many-cell domain을 이용하여 lateral connection을 지원한다.

`EcHy3D`는 실제 spatial cells와 neighborhood relation을 사용하며:
- soil/groundwater lateral flow: neighboring-cell hydraulic-head gradient
- surface runoff routing: topographic gradient
- optional river/channel storage and routing
- river-soil exchange
- NO3, NH4, DON, DOC, SO4 transport
을 계산한다.

각 setup cell은 x, y, z, dx, dy, dz, elevation, slope, aspect를 가진다.

따라서 최신 LandscapeDNDC는 단순한 independent-cell regional model로만 분류하면 안 된다. 다만 PSIM + EcHy3D + forest succession을 한 산지 연구에서 동시에 검증한 published application은 아직 별도 확인이 필요하다.

## 토양/WHC/토심
- soil layers individually defined
- field capacity/wilting point와 soil texture 기반 물수지 가능
- root growth를 bulk density와 stone content로 제한하는 옵션 존재
- EcHy/EcHy3D가 layered soil water와 groundwater를 처리
- 실제 soil depth를 cell/site 속성으로 줄 수 있음

## 천이/재생 감사
Dirnböck et al. (2020) 적용에서는 cohort 수가 초기화 후 고정되며 cohort merge/spawn을 하지 않았다. tree regeneration cohort도 초기 상태로 넣었다.

LandscapeDNDC 1.37 공식 site parameters에는:
- `succession_n_tree_init`: new trees planted during succession
- `succession_height_tree_init`: initial tree height during succession
- `succession_interval_s`: years for regrowth of young tree during succession
- `succession_interval_l`: generation time in years for succession
가 존재한다.

그러나 현재 공식 모델 설명에서 seed production, dispersal, germination, establishment filtering에 의해 새 woody cohort가 자율적으로 생성되는 BiomeE/FATES식 demographic succession은 확인하지 못했다. 파라미터 문구도 일정 세대/재생 간격에 정해진 수의 새 나무를 삽입하는 규칙 기반 regeneration에 가깝다.

따라서 현재 판정:
```
existing/regeneration cohorts의 생리와 경쟁: 강함
규칙 기반 young-tree insertion: 존재하는 것으로 보임
환경필터 기반 endogenous seed recruitment/succession: 미확인/약함
```

## 고운사 5조건 평가
1. 공간명시 cohort: O
2. 하층식생: O, 그러나 완전한 endogenous succession은 △
3. 토심 또는 WHC: O
4. 유역/지형: O, 산지 적용 + 최신 EcHy3D 공간수문
5. <=1 day: O, PSIM hourly

## 고운사 장점
1. cohort 기반이라 개체목보다 단순
2. hourly physiology라 storm-event 이후 빠른 환경변화 대응에 유리
3. grass/herb ground vegetation을 별도 cohort로 계산
4. fine-root biomass, vertical distribution, RLD 제공
5. detailed soil layers와 stone-content effect 지원
6. temperate mountain landscape published application 존재
7. 최신 framework에서 lateral groundwater/surface/river routing 가능
8. Windows/C++ 기반 실행과 HPC many-cell 구조

## 고운사 한계
1. 자연 종자생산-분산-정착 기반 woody succession이 약함
2. 2020 published mountain setup의 cohort 수 고정
3. PSIM + EcHy3D + dynamic succession을 동시에 검증한 산림사면 논문이 아직 확인되지 않음
4. dynamic erosion/deposition soil-depth update는 native geomorphic function이 아님
5. root exposure/burial와 storm mortality는 새로운 coupling 필요
6. ground vegetation cover가 일부 적용에서 overstory-cover empirical relation으로 조절됨

## 고운사 현재 역할
**A급 후보, 특히 시간단위 식생-토양 상호작용 엔진으로 강함.**

MEDFATE보다 hourly physiology와 root/soil detail이 강하고, 최신 EcHy3D로 spatial hydrology도 강화되었다. 하지만 100년 산불 후 초본-관목-교목 천이를 완전히 endogenous하게 맡기기에는 recruitment/demography가 아직 약하다.

## 핵심 근거
- Dirnböck et al. (2020), Landscape Ecology 35:483-499.
- LandscapeDNDC 1.37 PSIM documentation, 2026.
- LandscapeDNDC 1.37 EcHy3D documentation, 2026.
- LandscapeDNDC 1.37 Models Description / Users Guide, 2026.

## 링크
https://ldndc.imk-ifu.kit.edu/doxy/ldndc/doc/html/psim.html
https://ldndc.imk-ifu.kit.edu/doxy/ldndc/doc/html/ldndc_echy3d.html
https://pmc.ncbi.nlm.nih.gov/articles/PMC7045765/
