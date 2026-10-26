# 2026-10-26 빽빽한 억새 군락과 군데군데 참나무 맹아의 공간적 침식 비교 정정

## 확정 결정
**밀생 억새(Miscanthus sinensis)와 드문드문 분포한 산불 후 참나무 맹아(Quercus spp.)를 하나의 평균 vegetation COVER로 비교한 기존 모델실험은 연구문제를 제대로 테스트하지 못한다.** 초기의 공통 soil Ksat/rill detachment 및 동일 공간 균일강우로 계산된 약 1~6%의 유실량 차이는 실제 두 군락의 침식량이 비슷하다는 근거가 아니다. 숫자를 고운사 site soil-loss ranking으로 사용하는 것을 철회한다.

## 사용자의 실제 식생 상황
A dense grass case: 억새 포기들의 거의 연속적인 지표 초본층, 지하경+높은 fine root density under tussocks, dead/live culms, litter/standing dead vegetation, 작은 gap의 공간 분포. 억새 포기 사이는 더 적은 root density와 국소 경로일 수 있다.
B patchy oak case: 일부 기존 그루터기의 멀티-스템 맹아, 성숙 참나무림보다 작은 유효 수관, 낙엽층 복원이 진행 중일 수 있음, scattered rootstock islands, 노출 광물토와 표면 박리암편이 연결된 큰 interpatch flow paths를 형성할 가능성.
식생 유형을 고정 canopy cover 하나로 대체하거나 oak resprout의 오래된 지하부를 canopy cover나 new fine roots와 등치시키지 않는다.

## 관련 original 근거
- Mayor et al. (2008) WRR DOI 10.1029/2007WR006367: 유사한 식생 비율에서도 노출토양의 패치 규모, 연결성과 미세지형에 따라 runoff/sediment yield 차이. 6 plots와 3 catchments로 Flowlength 검증.
- Crompton et al. (2023) GRL DOI 10.1029/2022GL101801: 2D Saint Venant + tracer 실험에서 높은 patch infiltrability는 흐름을 포착하지만 높은 roughness는 흐름을 패치 바깥으로 돌릴 수도 있음. flow run-on vs run-around의 결과는 spatial arrangement가 결정.
- Crompton et al. (2023) Catena DOI 10.1016/j.catena.2023.107322: structural connectivity와 functional runoff connectivity 차이는 rainfall intensity, duration, permeability에 좌우됨.
- Gregory et al. (2018) BioEnergy Research DOI 10.1007/s12155-018-9903-6: M. sinensis 포기 내부와 사이의 뿌리밀도 이질성 현장자료, 단 산불 후 새 군락 자체의 보정값은 아님.
- Kim et al. (2020) Forests DOI 10.3390/f11050515: 산불 후 참나무는 기존 stump/rootstock에서 맹아 발생하는 유산 상태가 존재.
위 사례들은 주로 semi-arid 기후 및 농경지이므로 정확한 숫자를 고운사 site parameter로 이식하지 않는다.

## 모델 구조의 필수 정정
- EUROSEM 원본은 canopy free TF, leaf drip, SF는 계산하지만 합산해서 1D plane net rain을 받으므로, **밀생 억새의 runoff-pathway 차단 및 산발 참나무 사이 bare connected channel을 입력하는 방식이 없음**.
- SWEHR 공개 QA 원본 3×51 / 0.25m grid(0.75m 너비)는 Gounsa 드론/TLS로 관측할 수 있는 수 m 규모의 포기/그루터기 배열을 표현하기에 부적합하며, uniform net input으로 운용한 기존 실행에는 spatial oak/grass structure가 존재하지 않음.
- 임의로 Ks, Manning, F를 oak/grass 각각 하나씩 주는 방식은 서로 다른 물리과정의 임의 보정을 만드는 것이므로 종특성의 검증이 아님.
- 본 생산 2D engine은 기존 결정의 Iber+를 유지하되 불투수/투수 표면, root/litter/fragment 및 canopy/stem locations를 공간 상태로 결합한 **새로운 coupling**이 필요하다.
- 10,20,30,40,50mm/h 1h 검증은 물수지와 입경별 원토양 박리/재박리/퇴적/토사유출 질량수지 모두 통과해야 한다. Pathway connectivity metrics themselves are not erosion or runoff models.

## 최소 공간형 입력
공통 기반: georeferenced high-resolution TLS/Drone DTM and 2D flow-relevant microtopography, observed sediment roughness, embedded/surface spall rock position, soil depth/PSD, texture, K(h), initial theta.
Oak: mapped living/dead rootstock centres, sprout stem diameter/count and inclination, crown projection, species, leaf-on/leaf-off, litter and old/new root profile, stem-base hydraulic properties.
Miscanthus: detected tussock polygons, culm density and angles, leaf height/LAI, live/dead aboveground biomass and litter, within-tussock vs gap fine root profile, rhizome positions and soil hydraulic properties.
Rainfall pathway: rainfall -> canopy storage/evaporation -> direct TF, leaf drip KE, oak per-stump SF or Miscanthus per-tussock SF -> spatial local infiltration/runon/runaround -> 2D runoff -> size-specific detachment/deposition/erosion and sediment export.
Litter shielding and root detachment effects are distinct. Surface coarse fragment armouring and infiltration can act oppositely and should not be included through arbitrary fixed multipliers.

## 최소 비교실험
1. **실제 배치 비교**: dense grass map vs scattered stump oak map, own observed vegetation traits, common underlying topographic geomorphic boundary conditions (or explicitly matched plots/paired observations).
2. **공간배치만 비교**: same vegetation area and same total traits, contrast contiguous dense-like distribution vs patchy scattered distribution; isolate source connectivity.
3. **형질만 비교**: fix spatial map, swap measured oak/grass effective hydraulic and drop-energy/root trait fields to isolate species physiology/structure, recognising biologically implausible combinations are counterfactual sensitivity not prediction.
4. **변수/교란 비교**: same realized bare-pathway map with/without litter, fine-roots, live culms, and stemflow localization, rooting extent, initial moisture, 5 intensity cases.
Outcomes: actual bare-connected flowlength, runoff initiation/connectivity map, sediment source/sink maps, gross detachment, redeposition, delivered yield t/ha/event, soil-depth changes, water/solid mass budget.

## 정량적 예측의 적절한 수준
정성 가설: 억새가 실제로 조밀하게 사면을 연속적으로 피복하고, 참나무 맹아가 군데군데 있으며 그 사이 벌거숭이 토양이 연결되어 있고 다른 soil factors comparable하면, **참나무 사면이 더 큰 지표유출 연속성과 유실량을 보일 가능성이 높다**.
단정 불가: 억새 포기 사이 지속 유출, 억새 내부 고사, 토양 발수성, stem-run-around, oak litter remnant, rock armour, macropore Ks 및 강우강도의 비선형 상호작용에 따라 비율과 방향은 달라질 수 있다.
Do not use old EUROSEM ~26–160t/ha 'net erosion' as site yield; independent sediment mass closure not passed.
