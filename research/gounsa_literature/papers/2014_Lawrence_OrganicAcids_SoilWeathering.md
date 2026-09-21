# 서지정보
Lawrence, C. R., Harden, J. W., & Maher, K. (2014). Modeling the influence of organic acids on soil weathering. *Geochimica et Cosmochimica Acta, 139*, 487-507. DOI: 10.1016/j.gca.2014.05.003.

# 이 논문을 찾은 이유
LPJ-GUESS의 root/litter-derived organic inputs를 chemical weathering에 넣을 때, organic acid가 weathering을 항상 증가시키는지 아니면 secondary mineral precipitation, complexation, decomposition 때문에 장기 net effect가 달라질 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- reactive transport 수치모델
- soil pedogenesis / chemical weathering model

# 공간 구조
- 1D soil profile
- chronosequence-scale soil development

# 적용 환경
- Santa Cruz, California marine-terrace soil chronosequence
- 자연 토양 풍화

# 핵심 과정
- organic acid input
- organic acid transport
- organic acid decomposition
- organic-metal aqueous complexation
- mineral surface complexation
- primary mineral dissolution
- secondary mineral precipitation
- weathering-front evolution

# 식생 입력
원 모델은 식생모델을 직접 결합하지 않는다.

식생 관련 source term:
- low-molecular-weight organic acids
- root/microbial exudate analogue
- plant-material decomposition-derived organics

# 핵심 식
논문은 multicomponent reactive transport network에 oxalate를 추가하여 다음 경로를 분리한다.

```
organic-acid input
 -> transport / decomposition
 -> aqueous metal complexation
 -> mineral surface reactions
 -> mineral dissolution / precipitation
 -> profile-scale weathering
```

핵심 결과:
- near-surface mineral dissolution은 organic acid로 빨라질 수 있음
- 그러나 profile 전체의 장기 net chemical weathering은 오히려 감소할 수 있음
- kaolinite precipitation과 oxalate decomposition이 weathering-front evolution에 중요

# 파라미터와 단위
- oxalic-acid concentration
- organic-acid decomposition rate
- mineral kinetic constants
- aqueous complexation constants
- surface-complexation parameters
- fluid flux
- secondary-mineral precipitation parameters

# 원 논문의 구현 범위
organic carbon cycling이 soil weathering과 pedogenesis를 어떻게 바꾸는지 profile scale에서 reactive transport로 계산한다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요하다.

```
root/litter organic inputs
!=
simple positive weathering multiplier
```

를 수치모델로 보여준다.

고운사에서는 LPJ-GUESS root/litter/SOM state를:
- organic-acid or DOC source
- decomposition
- complexation
경로로 WITCH/PROFILE 또는 다른 RTM에 전달해야 한다는 근거가 된다.

# 새로운 coupling이 필요한 부분
```
LPJ-GUESS litter/root state
 -> LMW organic-acid source
```
는 새로운 coupling이다.

또한 soil-profile weathering flux를 sandstone boundary lowering 또는 mobile-soil production으로 바꾸는 것도 별도 coupling이다.

# 한계
- vegetation dynamics를 직접 모의하지 않음
- sandstone-specific parameterization 아님
- 장기 profile model이며 postfire annual succession을 직접 검증하지 않음

# 최종 판정
- **채택: organic-acid weathering의 핵심 process constraint**
- vegetation effect의 부호를 단일 양의 multiplier로 두지 않는 핵심 근거
- B-WITCH/REWTCrunch 보강 논문

# 참고 링크 / DOI
https://doi.org/10.1016/j.gca.2014.05.003
