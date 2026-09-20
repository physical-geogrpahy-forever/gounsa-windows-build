# 서지정보
Jackson, M., & Roering, J. J. (2009). *Post-fire geomorphic response in steep, forested landscapes: Oregon Coast Range, USA*. Quaternary Science Reviews, 28(11-12), 1131-1146. DOI: 10.1016/j.quascirev.2008.05.003.

# 이 논문을 찾은 이유
고운사처럼 급경사 산림 산불 후 어떤 사면과정이 실제로 우세하며, dry ravel과 shallow-landslide/root-strength decay를 background diffusion에서 분리해야 하는지 현장근거로 확인하기 위해 검토했다.

# 연구 유형
- postfire field study
- topographic/geomorphic analysis
- root-strength temporal observations

# 공간 구조
- three wildfire sites
- steep dissected forest hillslopes

# 적용 환경
- Oregon Coast Range
- fires in 1999, 2002, 2003

# 핵심 과정
- dry ravel
- root-strength decay
- landslide/debris-flow susceptibility
- hydrophobicity/infiltration
- channel sediment delivery

# 식생 입력
No dynamic vegetation model.

Observed postfire vegetation/root condition provides temporal process constraints.

# 핵심 결과
- strong soil hydrophobicity existed but discontinuities allowed rapid infiltration, so runoff erosion was not dominant at the study sites
- significant dry-ravel transport occurred at all sites
- at Sulphur Creek, fire-driven dry-ravel accumulation corresponded to slope-averaged lowering of about 2.5 mm
- Holocene-scale interpretation suggested fire could contribute roughly 10-20% of total denudation in steep dissected terrain
- root strength declined faster than expected from timber-harvest analogues

# 고운사에 직접 사용할 수 있는 부분
The paper strongly supports process separation:

```
postfire dry ravel
+
root-strength decay / landslide susceptibility
```

rather than treating all fire response as an increase in one diffusion coefficient.

It is also a caution that hydrophobicity does not automatically imply dominant overland-flow erosion where preferential/discontinuous infiltration remains strong.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root mortality/recovery -> landslide and dry-ravel states is a new coupling.

# 한계
- Oregon sedimentary terrain
- process dominance may differ in Gounsa
- not a numerical vegetation model

# 최종 판정
**핵심 postfire process-separation evidence.**

Use to justify:
- separate dry-ravel module
- separate root-decay/landslide module
- no universal postfire diffusivity multiplier

# 참고 링크 / DOI
https://doi.org/10.1016/j.quascirev.2008.05.003
