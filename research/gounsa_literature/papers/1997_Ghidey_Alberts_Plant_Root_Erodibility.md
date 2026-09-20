# 서지정보
Ghidey, F., & Alberts, E. E. (1997). *Plant root effects on soil erodibility, splash detachment, soil strength, and aggregate stability*. Transactions of the ASAE, 40(1), 129-135. DOI: 10.13031/2013.21257.

# 이 논문을 찾은 이유
산불 후 죽은 fine roots를 즉시 erosion resistance에서 제거해도 되는지, dead-root mass/length가 실제 interrill erodibility와 soil strength에 어떤 정량 효과를 갖는지 확인하기 위해 검토했다.

# 연구 유형
- laboratory rainfall-simulation experiment
- empirical erosion/root relation
- numerical-model implementation 아님

# 공간 구조
- 1 m x 0.3 m soil boxes
- 4% slope
- rainfall simulation

# 적용 환경
- Mexico silt loam
- crop-derived dead roots
- alfalfa, Canada bluegrass, corn, soybean

# 핵심 과정
- interrill erosion
- rainfall detachment
- soil strength
- aggregate stability
- dead-root physical legacy

# 식생 입력
- dead root mass in 0-0.15 m soil
- dead root length in 0-0.15 m soil

Observed ranges included approximately:
- dead root mass: 0.092-0.495 kg m^-2
- dead root length: 2.364-12.289 km m^-2

# 핵심 식

Interrill erodibility versus dead root mass:
```
K_i = 3.55 exp(-0.71 RTM)
```

where:
- `RTM`: dead root mass [kg m^-2]
- coefficient reported for the study's `K_i` scaling

Interrill erodibility versus dead root length:
```
K_i = 3.62 exp(-0.029 RTL)
```

where:
- `RTL`: dead root length [km m^-2]

Reported fit:
- root-mass relation: R2 = 0.63 using individual plots
- root-length relation: R2 = 0.59 using individual plots
- treatment means produced stronger relationships

# 핵심 결과
- dead roots did not materially alter runoff
- soil loss and sediment concentration decreased as dead root mass/length increased
- interrill erodibility decreased exponentially
- soil shear strength increased with dead root abundance
- aggregate stability increased
- splash detachment itself did not show a significant crop/root effect

This distinction is important:
```
dead roots
 -> soil erodibility / binding effect
but not necessarily
 -> raindrop splash shielding
```

# 고운사에 직접 사용할 수 있는 부분
A postfire dead-root pool must not automatically be set to zero erosion protection immediately after root mortality.

This paper supports:
```
dead-root state
 -> persistent soil-resistance effect
 -> decay with root decomposition
```

It also supports keeping litter/rainfall shielding separate from root-soil binding.

# 새로운 coupling이 필요한 부분
Transferring this agricultural interrill relationship directly to SWEHR `J` or `ASMASK` would be a new coupling and is not justified as a universal coefficient.

For high-gradient forest concentrated flow, use this primarily as:
- evidence for dead-root persistence
- validation bound
- interrill/dead-root sensitivity reference

# 한계
- agricultural soil and crop roots
- 4% slope
- dead roots were inherited from cropping systems, not wildfire-killed forest roots
- not a rill/concentrated-flow forest experiment

# 최종 판정
**채택: direct quantitative evidence that dead roots retain erosion-resistance effects.**

Do not use the raw coefficients as universal Gounsa parameters.

# 참고 링크 / DOI
https://doi.org/10.13031/2013.21257
