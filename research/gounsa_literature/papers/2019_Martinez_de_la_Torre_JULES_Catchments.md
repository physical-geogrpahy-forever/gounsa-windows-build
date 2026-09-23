# Martínez-de la Torre et al. (2019) — JULES catchment hydrology

## 서지정보
Martínez-de la Torre, A., Blyth, E. M., Robinson, E. L., et al. (2019). Using observed river flow data to improve the hydrological functioning of the JULES land surface model (vn4.3) used for regional coupled modelling in Great Britain (UKC2). *Geoscientific Model Development*, 12, 765–784. https://doi.org/10.5194/gmd-12-765-2019

## 이 논문을 검색한 이유
JULES-RED 후보의 criterion 4, 즉 실제 유역/지형 적용 전례를 검증하기 위해 검토했다.

## 연구 유형
- distributed land-surface hydrology
- catchment calibration/evaluation

## 적용환경
Great Britain의 13개 유역.

## 공간구조
- distributed 1 km x 1 km JULES grid
- DEM-derived flow direction and flow accumulation
- TOPMODEL topographic-index inputs
- topographic index는 더 세밀한 DEM에서 계산 후 model grid에 집계

## 핵심과정
- surface runoff
- subsurface runoff
- saturation/baseflow
- TOPMODEL water-table response
- river routing

## 시간
River Flow Model routing은 JULES model timestep마다 계산되어 subdaily로 작동한다.

## 고운사에 사용할 수 있는 부분
JULES는 point-column 또는 ESM coarse tile만 가능한 모델이 아니다.
실제 geographic catchment grid에서 distributed water balance와 routing을 수행한 전례가 있다.

따라서 JULES-RED를 fine vegetation grid에 적용하는 구상은 model architecture와 충돌하지 않는다.

## 필요한 새로운 coupling
- 10–50 m vegetation grid benchmark
- RED demographic state와 catchment setup의 직접 결합 검증
- geomorphic DEM/soil-depth state exchange

## 한계
- published application은 1 km로 고운사보다 매우 거침
- vegetation demography RED가 이 논문의 중심이 아님
- erosion/deposition process 없음

## 최종 판정
**Criterion 4 direct lineage precedent.**
Fine-scale JULES-RED catchment validation은 별도 필요.
