# 서지정보
Yoo, K., & Mudd, S. M. (2008). Toward process-based modeling of geochemical soil formation across diverse landforms: A new mathematical framework. *Geoderma, 146*(1-2), 248-260. DOI: 10.1016/j.geoderma.2008.05.029.

# 이 논문을 찾은 이유
고운사의:
```
mobile soil A/B
weathered but immobile C/Cr
fresh parent material
```
구조를 chemical weathering, weathering-front propagation, soil production, colluvial transport와 하나의 mass-balance framework로 연결할 수 있는 published 부모모델을 확인하기 위해 검토했다.

# 연구 유형
- mathematical process framework
- geochemical + geomorphic soil-formation model
- catena-scale mass balance

# 공간 구조
다양한 landform:
- eroding
- depositional
- level ground
- hillslope catena

soil domain을 두 핵심 영역으로 분해:

```
PDZ = physically disturbed zone
CAZ = chemically altered zone
```

PDZ:
- mobile / physically mixed soil

CAZ:
- physically undisturbed
- chemically altered parent material

# 적용 환경
- generic soil catenas
- diverse landforms

# 핵심 과정
- PDZ production
- weathering-front propagation
- mineral-specific dissolution
- elemental mass balance
- colloid translocation
- colluvial transport
- soil-bedrock boundary lowering

# 식생 입력
explicit vegetation model은 없다.

하지만 biological/chemical weathering terms를 later external forcing으로 연결할 수 있는 mass-balance skeleton이다.

# 핵심 구조

```
fresh parent material
 -> chemical weathering front
 -> CAZ
 -> physical conversion / incorporation
 -> PDZ
 -> colluvial transport
```

동시에:

```
mineral dissolution
precipitation
colloid translocation
solute loss
```

가 각 zone의 geochemistry를 갱신한다.

# 핵심 의미

## 1. mobile soil과 chemically weathered zone 분리
고운사에서:
```
H_AB
!=
Z_weathered
```
를 분리하는 강한 이론 근거.

## 2. chemical weathering과 boundary lowering 연결
chemical weathering은 단순 dissolved loss가 아니라 CAZ와 weathering-front evolution을 통해 soil-bedrock boundary lowering과 기능적으로 연결될 수 있다.

## 3. hillslope connectivity
soil catena에서 각 cell은 독립 box가 아니다.

```
upslope colluvial input
 -> local mineral inventory
 -> weathering
 -> downslope export
```

가 존재한다.

# 고운사에 직접 사용할 수 있는 부분

현재 상태를 다음처럼 재해석할 수 있다.

```
PDZ ~ mobile A/B soil
CAZ ~ C/Cr weathered regolith
fresh rock ~ sandstone parent material
```

따라서 장기적으로:

```
W_chem
 -> CAZ mineral transformation / mass loss

P_sand
 -> CAZ-to-PDZ physical/mobile conversion
```

처럼 역할을 나누는 architecture가 가능하다.

이는:
```
W_chem != P_sand
```
를 유지하면서도 둘을 하나의 mass-conserved profile model 안에서 연결할 수 있게 한다.

# 새로운 coupling이 필요한 부분
- LPJ-GUESS -> CAZ/PDZ chemical forcing
- Landlab/SWEHR -> PDZ transport
- sandstone-specific mineral kinetics
- fire spall/coarse fragments
- annual postfire transient

모두 new coupling이다.

# 한계
- vegetation dynamics 없음
- full 2D reactive transport 아님
- postfire 없음
- generic mineral/process framework
- current implementation code를 바로 사용할 production engine은 아님

# 최종 판정
- **핵심 채택: mobile-soil / chemically altered zone / weathering-front integration framework**
- 고운사 profile architecture의 강한 부모모델
- W_chem과 P_sand를 합치지 않으면서 연결하는 핵심 reference

# 참고 링크 / DOI
https://doi.org/10.1016/j.geoderma.2008.05.029
