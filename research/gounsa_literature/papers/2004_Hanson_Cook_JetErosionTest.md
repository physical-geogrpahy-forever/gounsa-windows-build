# 서지정보
Hanson, G. J., & Cook, K. R. (2004). Apparatus, test procedures, and analytical methods to measure soil erodibility in situ. *Applied Engineering in Agriculture, 20*(4), 455-462. https://doi.org/10.13031/2013.16492

# 이 논문을 찾은 이유
Iber+의 flow-driven detachability와 critical shear stress를 soil-loss 결과에 맞춰 보정하지 않고, 현장에서 독립적으로 측정할 방법을 찾기 위해 검토했다.

# 연구 유형
- in situ erosion test methodology
- submerged jet erosion test
- physically based parameter estimation

# 공간 구조
- point/core scale
- in situ soil surface

# 적용 환경
- cohesive and semi-cohesive soils
- channels, streambanks, spillways, embankments 등

# 핵심 과정
- excess-shear erosion
- critical shear stress
- erodibility coefficient

# 식생 입력
- 기본 방법은 식생상태를 직접 모델링하지 않음
- 뿌리를 포함한 undisturbed sample에도 후속 연구에서 적용 가능

# 핵심 식
일반 excess shear relation:
```
epsilon_r = k_d (tau - tau_c)^a
```
통상 a=1로 사용.

- epsilon_r: erosion rate [m s^-1]
- k_d: volumetric erodibility coefficient [m^3 N^-1 s^-1]
- tau: applied boundary shear stress [Pa]
- tau_c: critical shear stress [Pa]

JET scour-depth time series와 jet hydraulics에서 tau_c와 k_d를 추정한다.

# 파라미터와 단위
- tau_c [Pa]
- k_d [m^3 N^-1 s^-1]
- soil bulk density [kg m^-3]
- soil moisture
- jet head/nozzle geometry

# Iber+와의 직접 연결
Iber+ original-soil flow detachment:
```
D_fdd = K_d max(tau-tau_s,0)
```
여기서 K_d 단위는 kg N^-1 s^-1.

JET k_d는 m^3 N^-1 s^-1이므로 measured dry/bulk soil density rho_b로:
```
K_d,Iber = rho_b k_d,JET
```
가 된다.

이는 empirical fitting이 아니라 erosion-volume rate를 erosion-mass rate로 바꾸는 차원변환이다.

```
tau_s,Iber = tau_c,JET
```
도 동일 physical threshold로 직접 대응한다.

# 고운사에 직접 사용할 수 있는 부분
- K_d와 tau_s의 independent field measurement
- 현장 root/litter treatment별 parameter 측정
- output calibration을 피하는 핵심 방법

# 새로운 coupling이 필요한 부분
LPJ-GUESS state에서 JET parameter의 temporal interpolation을 만드는 것은 별도 문제이다.
가능하면 root-state class별 independent measurement table을 사용한다.

# 한계
JET scale과 hillslope rill scale 사이 scale effect가 존재할 수 있으므로 flume cross-check 권장.

# 최종 판정
- **Iber+ K_d / tau_s의 최우선 독립 측정법**

# 참고 링크 / DOI
https://doi.org/10.13031/2013.16492
