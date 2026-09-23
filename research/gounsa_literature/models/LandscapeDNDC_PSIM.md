# LandscapeDNDC / PSIM

## 현재 판정
고운사 식생모델 후보군에서 새로 확인된 **강한 process-cohort 후보**. 특히 시간해상도, 산지 적용, 하층식생, fine root, 토양층 표현이 매우 강하다. 반면 자연천이와 공간 종자분산은 MEDFATE/BiomeE/LANDIS-II보다 약하다.

## 식생 표현
PSIM은 한 simulation unit 안에서 여러 vegetation cohort를 동시에 표현한다.
- 수종별/크기별 tree cohort
- tree regeneration cohort
- grass/herb ground-vegetation cohort
- cohort별 foliage, fine roots, living wood, reserves 등

개체목 좌표는 필요하지 않는다.

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

## 하층식생
grass/herbaceous vegetation도 cohort로 처리되며 tree cohort와 원칙적으로 같은 photosynthesis, respiration, allocation, senescence framework를 이용한다.

Dirnböck et al. 2020 산지 적용에서는 한 cell 최대 7 cohort:
- ground vegetation 1
- tree regeneration 2
- overstory tree 4

모든 cohort가 light, water, N을 경쟁했다.

## 공간 적용 선례
Dirnböck et al. 2020:
- European Alps, Kalkalpen National Park
- 약 158 km2
- 100 x 100 m actual grid
- 15,793 cells
- hourly simulation, 2000-2014
- LiDAR/vegetation data 원자료 10 x 10 m를 100 m로 aggregate
- regional application에서 cells는 서로 독립, lateral water/energy/matter exchange 없음

현재 LandscapeDNDC framework 자체는 many-cell simultaneous simulation과 일부 lateral connection kernel(EcHy 3D 등)을 지원한다.

## 천이/재생 감사
주의: Dirnböck et al. 적용에서는 cohort 수가 초기화 후 **고정**되며 cohort merge/spawn을 하지 않았다. tree regeneration cohort도 초기 상태로 넣었다.

현재 공식 site parameters에는:
- `succession_n_tree_init`
- `succession_height_tree_init`
- `succession_interval_s`
- `succession_interval_l`
가 존재한다.

그러나 문서 표현이 `new trees planted during succession`, `generation time`, `regrowth` 수준이므로 이것을 자연 종자생산-분산-발아-정착 기반의 완전한 endogenous succession으로 간주하지 않는다. 실제 자연천이 알고리즘은 추가 source-level 검증이 필요하다.

## 고운사 장점
1. cohort 기반이라 개체목보다 단순
2. hourly physiology라 storm-event 이후 빠른 환경변화에 대응하기 좋음
3. grass/herb ground vegetation을 별도 cohort로 계산
4. fine-root biomass와 vertical distribution 제공
5. detailed soil layers와 stone-content effect 지원
6. temperate mountain landscape의 실제 published application 존재
7. Windows 64-bit binary 배포가 현재 유지됨

## 고운사 한계
1. published spatial application의 cohort 수가 고정
2. native seed dispersal/동적 cohort creation이 충분히 검증되지 않음
3. 2020 regional setup은 cell 간 lateral exchange 없음
4. dynamic erosion/deposition soil-depth update는 native geomorphic function이 아님
5. fire-spread/postfire succession의 완성도는 별도 확인 필요
6. ground vegetation cover가 일부 적용에서 overstory-cover empirical relation으로 조절됨

## 고운사 현재 역할
**A급 추가후보.**
MEDFATE보다 hourly physiology가 강하고, 산지 temperate precedent가 직접적이다. 하지만 100년 postfire succession을 단일 모델로 맡기기에는 demographic succession 검증이 부족하다.

가장 유망한 역할은:
```
actual GIS cell
 -> PSIM hourly tree/regeneration/herb physiology
 -> fine roots / water / N / litter
 -> geomorph event coupling
```
이며, 완전한 seed-driven succession까지 요구할 경우 추가 검증 또는 새로운 coupling이 필요하다.

## 핵심 근거
- Dirnböck et al. (2020), Landscape Ecology 35:483-499. Substantial understory contribution to the C sink of a European temperate mountain forest landscape.
- LandscapeDNDC official PSIM documentation, accessed 2026-09-23.
- LandscapeDNDC current users guide/site parameter documentation, 2026.

## 링크
https://ldndc.imk-ifu.kit.edu/doxy/ldndc/doc/html/psim.html
https://pmc.ncbi.nlm.nih.gov/articles/PMC7045765/
