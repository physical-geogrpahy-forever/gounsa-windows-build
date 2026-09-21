# LORICA

## 모델 성격
Raster-based soil-landscape evolution model.
LAPSUS landscape evolution + MILESD soil formation lineage.

## 핵심 구조
- DEM surface evolution
- multiple soil layers per grid cell
- lateral erosion/deposition and creep
- vertical pedogenic processes
- physical/chemical weathering
- armouring
- particle-size selective transport
- vegetation protection feedback

## 핵심 feedback
soil development -> texture/profile -> erosion susceptibility
erosion/deposition -> mineral/soil redistribution -> profile/weathering
weathering/pedogenesis -> soil state -> landscape process rates

## 고운사에서의 장점
- soil profile와 DEM을 같은 spatial framework에서 함께 진화
- erosion/deposition과 chemical weathering을 연결
- mineral residence/fresh-material redistribution interface 설계에 유용

## vegetation 관련 한계
- dynamic forest ecosystem model 아님
- vegetation은 주로 erosion protection feedback
- root biomass/RLD/respiration/root water uptake/nutrient cycling 없음

## 고운사 역할
Geomorphic-weathering coupling의 spatial precedent로 사용.
ForSAFE 또는 LPJ-GUESS 계열의 vegetation-weathering process와 결합하면 NEW COUPLING.

## 최종 판정
- 강한 보조 채택
- 역할: soil-landscape-weathering spatial coevolution reference