# Stony-soil hydraulics: GEM / effective hydraulic-property lineage

## 고운사에서 검토한 이유
현장에서 매립 석력이 많으므로 rock-fragment volume을 임의 coefficient로 Ksat나 soil-water capacity에 곱하지 않고, published physically based model을 그대로 사용하기 위해 정리한다.

## 핵심 문헌
- Ma & Shao 2008: non-equilibrium dual-porosity infiltration model
- Naseri et al. 2020: General Effective Medium(GEM) hydraulic conductivity
- Naseri et al. 2023: measured stony-soil WRC/HCC and model evaluation
- Hlaváčiková et al. / related HYDRUS numerical stony-soil studies

## GEM
Naseri et al. 2020은 rock-fragment content, fragment conductivity, shape/orientation 및 background soil conductivity를 사용하여 stony soil의 effective hydraulic conductivity를 계산한다.

장점:
- saturated/unsaturated K(h)
- permeable/impermeable rock fragments 모두 가능
- fragment interaction 고려
- high volumetric rock-fragment content까지 목표로 개발
- mountainous and forested soils에 적합한 property model

따라서 고운사에서:
```
measured fine-earth K(h)
+ measured/estimated sandstone-fragment K(h)
+ volumetric RF fraction
+ fragment shape/orientation
 -> GEM
 -> effective K(h)
```
을 기본으로 한다.

## water retention
Naseri et al. 2023에서 porous RF까지 포함하는 volume-averaging relation:
```
theta_mix(h)
= (1-f) theta_soil(h)
+ f theta_rock(h)
```

RF water storage가 무시 가능한 경우:
```
theta_mix(h)
= (1-f) theta_soil(h)
```

고운사 사암은 RF 자체의 water retention을 가능하면 직접 측정하거나 sandstone-specific literature로 제약한다.

## Ma & Shao 2008
NDPM은 stone content, size, shape와 matrix-pore interaction을 infiltration process로 직접 다룬다.
고운사 production의 기본모델보다는 GEM 결과의 sensitivity/benchmark로 사용한다.

## 자의성 방지 원칙
다음과 같은 식을 새로 만들지 않는다.
```
K_eff = K_fine * arbitrary_factor(rock)
soil_water = soil_water * arbitrary_armour_factor
```

대신 existing published property model의 입력값을 현장에서 측정한다.

## erosion model과의 연결
GEM/Naseri output은 새로운 erosion coefficient가 아니라 동일 물리량인:
- K(h)
- Ksat
- theta(h)
를 hydrology/vegetation model에 전달한다.

모델 간 software coupling 자체는 새롭지만 **새로운 경험식을 만들지 않는다.**

## 최종 판정
- high embedded stoniness의 기본 hydraulic-property model: **GEM 채택**
- effective water-retention model: **Naseri et al. 2023 volume mixing 채택 후보**
- NDPM: sensitivity/benchmark
