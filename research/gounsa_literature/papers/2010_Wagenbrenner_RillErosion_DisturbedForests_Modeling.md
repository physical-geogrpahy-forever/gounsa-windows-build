# 서지정보
Wagenbrenner, J. W., Robichaud, P. R., & Elliot, W. J. (2010). *Rill erosion in natural and disturbed forests: 2. Modeling approaches*. Water Resources Research, 46, W10507. DOI: 10.1029/2009WR008315.

# 이 논문을 찾은 이유
고운사처럼 급경사 산림과 산불 교란 조건에서 WEPP/Foster 계열 rill detachment 식의 `Kr`, `tau_c`, transport-limited/source-limited 가정이 실제로 성립하는지 확인하기 위해 검토했다.

# 연구 유형
- 현장 simulated-runoff 실험
- rill erosion model parameterization / model comparison
- 독립적인 2D 수치모델은 아님

# 공간 구조
- 4 m rill plots
- steep forest hillslopes
- 1D concentrated-flow/rill parameterization

# 적용 환경
- natural forest
- low soil burn severity
- high soil burn severity
- logging skid trails
- northwestern United States
- slope classes approximately 18-69%

# 핵심 과정
- rill detachment capacity
- sediment transport capacity
- source-limited vs transport-limited erosion
- shear stress, stream power, unit stream power, unit-length shear force

# 식생 입력
root biomass 직접입력 없음.
disturbance state와 ground/duff cover가 실험조건으로 반영됨.

# 핵심 식
WEPP/Foster rill detachment:
```
D_c = K_r (tau_s - tau_c)
```

Foster-Meyer detachment/transport feedback을 함께 검토한다.

# 파라미터와 단위
- `K_r`: s m^-1
- `tau_c`: Pa
- `D_c`: kg m^-2 s^-1
- transport capacity `T_c`: kg s^-1

원문에서 shear-stress-based `K_r`:
- natural forest: 1.5e-6 s m^-1
- high soil burn severity: 2.0e-4 s m^-1
- skid trail: 1.7e-3 s m^-1

즉 disturbance에 따라 수 orders of magnitude 변한다.

# 원 논문의 구현 범위
66 simulated-runoff experiments의 rill erosion을 네 hydraulic predictor로 분석하고 forest disturbance class별 rill erodibility를 추정한다.

중요한 결과:
- 모든 disturbance class에서 sediment flux가 transport capacity보다 매우 낮음
- transport ratio 최대 약 0.53%
- steep forest rill erosion은 명확히 **detachment/source limited**
- 동일 inflow 내에서도 `K_r`가 초기에서 steady state로 감소
- 따라서 `K_r`를 시간불변 상수로 두는 것도 문제될 수 있음

# 고운사에 직접 사용할 수 있는 부분
1. 급경사 산불 산림에서 shear-excess/Foster 계열 rill detachment를 쓰는 직접 근거
2. burned forest에서 `K_r`가 disturbance severity에 따라 크게 달라진다는 calibration/validation range
3. 고운사에서는 concentrated-flow erosion이 transport capacity보다 detachment resistance에 더 민감할 수 있다는 근거
4. static `K_r` 대신 vegetation/soil recovery에 따라 time-varying erodibility를 둘 필요성

# 새로운 coupling이 필요한 부분
LPJ-GUESS root/litter state로 `K_r(t,x)`를 계산하는 것은 본 논문에 없다. 이를 연결하면 새로운 coupling이다.

# 한계
- root biomass/RLD 직접식 없음
- 2D solver 아님
- simulated clear-water inflow rill experiments
- natural/low-severity class에서 shear-stress regression slope가 비물리적 음수인 경우가 있어 단일 hydraulic predictor의 한계를 보여줌

# 최종 판정
- **채택: steep disturbed/postfire forest rill calibration and validation benchmark**
- 2D 엔진 후보는 아님
- 고운사 concentrated-flow/rill 식의 산림 적합성을 뒷받침하는 핵심 근거

# 참고 링크 / DOI
https://doi.org/10.1029/2009WR008315
