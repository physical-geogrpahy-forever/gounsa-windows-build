# 서지정보
Roering, J. J., & Gerber, M. (2005). *Fire and the evolution of steep, soil-mantled landscapes*. Geology, 33(5), 349-352. DOI: 10.1130/G21260.1.

# 이 논문을 찾은 이유
산불 후 급경사 산림에서 background creep와 구분되는 dry-ravel transport가 실제로 얼마나 커지고 nonlinear transport law의 slope sensitivity가 어떻게 변하는지 확인하기 위해 검토했다.

# 연구 유형
- field observation
- high-resolution topographic analysis
- physically based transport-model calibration

# 공간 구조
- steep soil-mantled hillslopes
- high-resolution topography
- slope-dependent sediment flux

# 적용 환경
- Oregon Coast Range
- recent wildfire
- steep forested terrain

# 핵심 과정
- postfire dry ravel
- nonlinear hillslope transport
- vegetation/litter removal
- local bedrock exposure
- valley infilling

# 식생 입력
Dynamic biomass model 없음.

Fire is represented as an abrupt change in surface roughness/transport state after vegetation and litter combustion.

# 핵심 식 / 파라미터 해석
The calibrated postfire transport follows a nonlinear slope-dependent flux law.

Key reported threshold:
```
S_c,postfire = 1.03
```

compared with a previously estimated long-term value:
```
S_c,long-term = 1.27
```

The lower postfire critical gradient is interpreted as reduced surface roughness following vegetation combustion.

The paper reports postfire erosion rates about six times the long-term mean for its study setting.

# 시간척도
The spatial simulations represent the immediate/first-year postfire state.

The authors explicitly note that ecological and geomorphic effects may persist several years, but the model is not a dynamic annual vegetation-recovery model.

# 고운사에 직접 사용할 수 있는 부분
Strong evidence that:

```
postfire dry ravel
!=
background creep
```

and that fire can change the effective slope threshold/roughness controlling granular transport.

This supports retaining Lamb/postfire dry-ravel as a separate disturbance pathway instead of modifying the long-term background diffusion coefficient permanently.

# 새로운 coupling이 필요한 부분
LPJ-GUESS recovery state -> postfire `S_c` or transport coefficient recovery would be a new coupling.

Do not infer such a time function from this paper alone.

# 한계
- Oregon Coast Range
- immediate postfire focus
- no LPJ-GUESS-like vegetation dynamics
- dry ravel and background creep are not fully separable in a single calibrated nonlinear coefficient

# 최종 판정
**채택 보조근거 for postfire dry-ravel state.**

Not the baseline background-creep law.

# 참고 링크 / DOI
https://doi.org/10.1130/G21260.1
