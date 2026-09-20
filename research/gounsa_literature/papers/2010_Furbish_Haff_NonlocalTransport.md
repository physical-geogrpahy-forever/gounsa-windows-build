# 서지정보
Furbish, D. J., & Haff, P. K. (2010). *From divots to swales: Hillslope sediment transport across divers length scales*. Journal of Geophysical Research: Earth Surface, 115, F03001. DOI: 10.1029/2009JF001576.

# 이 논문을 찾은 이유
고운사 사면수송을 하나의 diffusion coefficient로 합치는 대신, slow local bulk creep와 long-travel intermittent surface processes를 분리하는 것이 이론적으로 타당한지 확인하기 위해 검토했다.

# 연구 유형
- nonlocal probabilistic transport theory
- field-profile comparison

# 핵심 구분
The paper explicitly separates:

```
slow bulk soil behavior
from small-scale bioturbation / dilation
```

and:

```
intermittent surface motions
with longer travel distances
```

Examples of the latter include:
- dry ravel
- soil slips
- tree throw
- animal excavation
- fire-related surface release

# 핵심 의미
A local diffusion-like law can be reasonable for small particle motions associated with:
- wetting-drying
- freeze-thaw
- small-scale bioturbation

but long-distance intermittent motions become nonlocal, especially on steep slopes.

# 고운사에 직접 사용할 수 있는 부분
This supplies the theoretical basis for the chosen modular architecture:

```
q_hill
=
q_local_bg
+
q_rootgrowth
+
q_treethrow
+
q_dryravel
+
separate landslide events
```

Do not force all terms into one `D`.

# relation to postfire
The paper specifically discusses material temporarily stored behind vegetation or in mounds being remobilized after fire/death as a slope-dependent intermittent process.

This supports keeping postfire dry ravel separate from local background creep.

# 한계
- general transport theory
- does not give Gounsa-specific rates
- parameterization of each displacement kernel remains process-specific

# 최종 판정
**핵심 구조근거: local residual creep and nonlocal disturbance transport must be separated.**

# 참고 링크 / DOI
https://doi.org/10.1029/2009JF001576
