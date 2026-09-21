# 서지정보
Perez-Fodich, A., & Derry, L. A. (2019). Organic acids and high soil CO2 drive intense chemical weathering of Hawaiian basalts: Insights from reactive transport models. *Geochimica et Cosmochimica Acta, 249*, 173-198. DOI: 10.1016/j.gca.2019.01.027.

# 이 논문을 찾은 이유
식생이 chemical weathering에 미치는 두 핵심 경로인:
- soil/root respiration CO2
- low-molecular-weight organic acids
를 multicomponent reactive transport에서 분리해 정량 평가한 사례를 찾기 위해 검토했다.

# 연구 유형
- multicomponent reactive transport 수치모델
- chronosequence data comparison

# 공간 구조
- 1D porous-media weathering profile
- 약 1 m initial basalt column

# 적용 환경
- Hawaiian tropical forest soil chronosequence
- basalt parent material

# 핵심 과정
- variably saturated flow
- soil CO2 forcing
- oxalate/citrate organic ligands
- mineral dissolution
- secondary mineral precipitation
- Fe, Al, Si, Ca, Mg mobilization

# 식생 입력
식생 자체를 동적으로 모의하지 않는다.

biological forcing:
- elevated soil pCO2 as respiration proxy
- continuous low-molecular-weight organic-acid input

# 핵심 식
세 단계 scenario를 비교한다.

```
M1: infiltration + atmospheric CO2

M2:
M1
+ elevated soil CO2

M3:
M2
+ oxalate / citrate ligands
```

모델에서 elevated soil CO2는 pH를 낮추고 Mg/Ca leaching을 강화한다.

organic ligands는 Al과 Fe complexation을 통해 secondary phases의 dissolution 및 elemental export를 크게 바꾸며 observed mass depletion pattern을 더 잘 재현한다.

# 파라미터와 단위
원 논문 sensitivity에서:
- soil CO2: atmospheric 대비 약 10배 forcing
- oxalate/citrate: 10^-4 M 수준의 continuous input scenario
- mineral-specific kinetic/thermodynamic parameters
- partial saturation / hydrologic flow

이 값들을 고운사에 직접 적용하지 않는다.

# 원 논문의 구현 범위
biologically generated acidity와 organic ligands가 reaction front 및 element loss를 어떻게 바꾸는지 수치적으로 검증한다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS에서:
- root/SOM respiration -> soil CO2
- root/litter activity -> organic ligands
를 서로 다른 weathering pathways로 유지해야 한다는 강한 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS respiration 및 organic-C pools를 실제 pCO2와 ligand concentration으로 변환하는 것은 새로운 coupling이다.

# 한계
- basalt, tropical forest
- 10^4 yr chronosequence
- forcing values를 고운사 사암에 직접 전이할 수 없음

# 최종 판정
- **채택: soil CO2 + organic-ligand chemical-weathering mechanism의 핵심 근거**
- coefficient source가 아니라 process-architecture source

# 참고 링크 / DOI
https://doi.org/10.1016/j.gca.2019.01.027
