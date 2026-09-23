# Martínez-de la Torre et al. (2020) — JULES groundwater / hillslope

## 서지정보
Martínez-de la Torre, A., Blyth, E. M., Weedon, G. P., et al. (2020). Towards the representation of groundwater in the Joint UK Land Environment Simulator. *Hydrological Processes*. https://doi.org/10.1002/hyp.13767

## 이 논문을 검색한 이유
JULES가 실제/이상화 지형에서 fine-grid hillslope groundwater redistribution을 처리할 수 있는지, 즉 고운사 criterion 3과 4의 공간해상도 잠재력을 확인하기 위해 검토했다.

## 연구 유형
land-surface hydrology development and groundwater benchmarking.

## 공간구조
중요한 idealised experiment:
- V-shaped catchment
- 10 m horizontal grid
- 약 110 m wide, 100 m long domain
- explicit hillslope slopes and river/channel geometry
- 5 m soil column

## 핵심과정
- saturated/unsaturated water storage
- groundwater
- lateral redistribution / outlet discharge benchmarking
- fine-grid hydrologic response

## 고운사 의미
JULES hydrologic core가 1 km grid에만 제한된 것은 아니다.
10 m idealised hillslope simulation precedent가 있어 10–50 m vegetation/hydrology benchmark를 시도할 기술적 근거가 있다.

## 중요한 구분
이 논문은 JULES-RED demographic vegetation을 함께 돌린 연구가 아니다.
따라서 10 m JULES hydrology와 daily JULES-RED demography를 합친 고운사 setup은 새로운 integration/benchmark이다.

## 최종 판정
**criterion 3/4의 fine-scale hydrology precedent로 유지.**
