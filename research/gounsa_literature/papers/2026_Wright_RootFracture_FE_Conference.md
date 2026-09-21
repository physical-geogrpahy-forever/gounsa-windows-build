# 서지정보
Wright, C., Ramsdale, E., McKay Fletcher, D., Williams, K., Le Houx, J., & Ruiz, S. (2026). Understanding root biomechanics in high-strength environments: assessing the feasibility of penetration and fracture FE models with SRXCT. *EGU General Assembly 2026*, EGU26-7232. DOI: 10.5194/egusphere-egu26-7232.

# 이 논문을 찾은 이유
고강도 매질에서 root pressure와 crack propagation을 finite-element model로 직접 다룬 최신 연구가 production 수준까지 발전했는지 확인하기 위해 검토했다.

# 연구 유형
- 학회초록
- finite-element numerical model
- SRXCT 실험 연계
- preliminary research

# 공간 구조
- root tip / crack scale
- experimental and field-scale boundary conditions

# 적용 환경
- high-strength soil / surrogate solid media
- mechanically harsh rooting environment

# 핵심 과정
- direct root penetration
- root pressure
- crack propagation
- local softening by exudation
- successive fracture and growth

# 식생 입력
- exerted root pressure
- root growth
- exudation-related local softening

# 핵심 식
공개 초록에서 완전한 constitutive equation은 제시되지 않는다.

개념 구조:

```
root pressure
 + local softening by exudation
 -> crack propagation
 -> overcoming direct penetration limit
 -> further root growth
```

# 파라미터와 단위
초록 수준에서 상세 parameter table은 제공되지 않는다.

# 원 논문의 구현 범위
FE model과 SRXCT 관측을 결합해 고강도 환경에서 direct penetration과 crack propagation 가능성을 평가한다.

# 고운사에 직접 사용할 수 있는 부분
living root가 단순 압입 한계를 crack propagation으로 우회할 수 있다는 최신 mechanics 방향성을 보여준다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root state를 pressure/fracture mechanics로 바꾸고, 사암 균열의 fragment detachment 및 연간 soil production으로 환산하는 것은 전부 새로운 coupling이다.

# 한계
- peer-reviewed journal article이 아니라 2026 EGU conference abstract
- constitutive details와 full validation 부족
- sandstone-specific production rate 없음
- landscape-scale implementation 없음

# 최종 판정
- **보류 / 최신 mechanics 보조근거**
- production baseline에는 사용하지 않는다.
- 후속 journal paper가 나오면 재검토 우선순위가 높다.

# 참고 링크 / DOI
https://doi.org/10.5194/egusphere-egu26-7232
