# MEDFATE + medfateland

## 조사 목적
고운사 산불 후 100년 식생-지형 상호작용용 식생모델 후보. 공간명시 코호트, 교목/관목/초본, 뿌리와 토양층, 일 단위 이하 생리, 유역 수문 연결 여부를 검토한다.

## 모델 구조
- `medfate`: 임분 내부 식생을 cohort로 표현한다. tree, shrub, herb cohort를 입력할 수 있다.
- 임분 내부 식물 개체의 x-y 좌표는 명시하지 않는다.
- `medfateland`: 여러 임분/격자를 경관 및 유역 구조로 연결한다.
- `fordyn_land()`은 일별 growth/water balance를 호출하면서 장기 forest dynamics와 격자 간 seed dispersal을 결합한다.

## 시간 구조
- water balance와 plant growth/mortality: daily.
- 고급 transpiration/hydraulics는 sub-daily 계산을 포함한다.
- 장기 recruitment/resprouting/management는 `fordyn` 계층에서 처리한다.

## 식생과 천이
- tree, shrub, herb cohort 입력 가능.
- woody forest dynamics는 recruitment, growth, mortality, resprouting을 명시적으로 포함한다.
- seed bank와 seedling bank가 존재하며 환경필터를 거쳐 recruitment한다.
- herb cohort는 최근 버전에서 명시적 cohort로 들어가지만, 현재 reference book의 forest-dynamics 장은 recruitment/growth/mortality를 `woody plant cohorts` 중심으로 설명한다. 따라서 herb의 완전한 장기 demographic succession은 소스코드 수준 추가 확인이 필요하다.

## 뿌리 및 토양
- cohort마다 Z50, Z95, 선택적으로 Z100으로 fine-root 수직분포를 정의한다.
- multi-layer soil.
- root distribution과 각 soil layer의 water uptake가 연결된다.
- soil water model은 버전에 따라 bucket 또는 Richards 계열을 사용할 수 있다.

## 공간 수문
`medfateland`의 watershed simulation은 다음을 지원한다.
- overland surface flow from upslope cells
- lateral saturated soil flow/interflow between adjacent cells
- groundwater/baseflow between adjacent cells
- channel routing
- seed dispersal

기본 수문은 TETIS와 유사한 방식이며, 더 물리적인 distributed hydrology가 필요하면 SERGHEI와 결합할 수 있다.

## 코드
- R + compiled source를 포함하는 공개 패키지.
- medfate와 medfateland 모두 활발히 유지되고 있으며 2026년 문서가 존재한다.
- Mediterranean/Spain 중심 species parameterization이므로 고운사 수종에 대한 새 parameterization 필요.

## 고운사 장점
1. cohort 기반이라 개별목 모델보다 계산량을 억제할 수 있다.
2. tree-shrub-herb를 같은 임분 구조에서 표현 가능하다.
3. soil layers와 root depth가 직접 연결된다.
4. 유역 격자 사이 수문 연결과 seed dispersal이 이미 같은 프레임워크에 존재한다.
5. daily vegetation dynamics라 고운사 지형모델과 일 단위 coupling이 가능하다.
6. `soilDomains = none` 등 외부 bulk-soil-water 계산을 위한 인터페이스가 존재하여 외부 지형/수문 엔진과의 결합 가능성이 높다.

## 한계
- 임분 내부는 horizontal spatially implicit cohort.
- Mediterranean parameter set을 한국 온대림에 그대로 쓸 수 없다.
- herb cohort의 완전한 recruitment/mortality succession은 추가 코드 검증 필요.
- 지형 변화 자체를 내부에서 계산하지 않으므로 soil depth/elevation change는 외부 geomorphology coupling 필요.

## 현재 판정
**최우선 정밀검토 후보.**
현재 조사된 모델 중 사용자가 요구한 `cohort + tree/shrub/herb + root/soil layers + daily + watershed lateral hydrology + seed dispersal` 조합에 가장 가깝다.

## 핵심 자료
- De Cáceres et al. 2023, MEDFATE 2.9.3, GMD 16, 3165-3201.
- medfate 2026 reference book and package documentation.
- medfateland v3.0.0 2026 documentation.
