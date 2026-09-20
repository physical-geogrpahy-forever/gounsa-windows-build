# 서지정보
Anderson, R. S. (2002). *Modeling the tor-dotted crests, bedrock edges, and parabolic profiles of high alpine surfaces of the Wind River Range, Wyoming*. Geomorphology, 46(1-2), 35-58. DOI: 10.1016/S0169-555X(02)00053-3.

# 이 논문을 찾은 이유
residual background creep를 단순 상수 diffusivity로만 둘 필요가 있는지, freeze-thaw를 실제 기후와 active regolith depth에 연결한 process-specific model이 있는지 확인하기 위해 검토했다.

# 연구 유형
- process-based numerical hillslope model
- frost creep + regolith production

# 공간 구조
- hillslope profile
- evolving regolith thickness and topography

# 적용 환경
- high alpine periglacial surface
- Wind River Range, Wyoming

# 핵심 과정
- frost penetration
- frost heave / settling
- frost-driven soil creep
- regolith production
- depth limitation of transport

# 핵심 구조
The model assumes frost creep dominates transport.

Transport efficiency:
- scales with local slope
- scales with frost-event frequency
- depends on frost penetration depth
- is curtailed when available regolith is thinner than potential frost penetration

Thus:
```
freeze-thaw forcing
+ active regolith depth
+ slope
 -> creep transport
```

rather than a climate-independent constant D.

# process equation structure
Displacement from a frost event is largest near the surface and decreases with depth, reaching zero at the frost-penetration depth.

Long-term flux integrates:
- displacement per event
- probability distribution of frost depths
- event frequency

The exact numerical implementation should be taken from the original equations before coding.

# 고운사에 직접 사용할 수 있는 부분
If freeze-thaw is shown to be an important annual process at Gounsa, this is a defensible optional explicit module driven by:
- temperature/frost-event frequency
- active soil/regolith thickness
- slope

It is preferable to hiding a strong frost-creep contribution inside an unexplained D.

# 새로운 coupling이 필요한 부분
LPJ-GUESS soil temperature -> frost penetration/event-frequency interface is a new coupling unless the exact required frost state is already available.

# 한계
- alpine/periglacial environment
- process intensity may be much larger than Gounsa
- no dynamic vegetation
- not a generic temperate-forest creep coefficient

# 최종 판정
**optional explicit abiotic-creep module.**

Do not adopt its alpine coefficients without demonstrating Gounsa freeze-thaw significance.

# 참고 링크 / DOI
https://doi.org/10.1016/S0169-555X(02)00053-3
