# 서지정보
Zhang, G.-H., Tang, K.-M., Ren, Z.-P., & Zhang, X.-C. (2013). Impact of grass root mass density on soil detachment capacity by concentrated flow on steep slopes. *Transactions of the ASABE, 56*(3), 927-934. https://doi.org/10.13031/trans.56.9566

# 이 논문을 찾은 이유
뿌리량이 Iber+의 flow detachability K_d와 critical shear stress tau_s 중 어느 항을 주로 변화시키는지 확인하기 위해 검토했다.

# 연구 유형
- laboratory flume experiment
- undisturbed rooted soil cores

# 공간 구조
- concentrated-flow/rill scale

# 적용 환경
- steep slopes 17.4-42.3%
- switchgrass rooted soils

# 핵심 과정
- soil detachment capacity
- rill erodibility
- critical shear stress
- root mass density

# 식생 입력
- root mass density: 0.25-17.98 kg m^-3

# 핵심 식
WEPP excess shear form:
```
D_c = K_r (tau - tau_c)
```

각 root-density group에서 D_c와 tau의 회귀:
- slope = K_r
- x-intercept = tau_c

보고된 root effect:
```
K_r = 0.410 exp(-2.018 RD)
```
(원문 단위/표기 사용 시 재검증)

핵심은 root mass density 증가에 따라 rill erodibility가 크게 감소했다는 점이다.

# 핵심 결과
- rooted soil mean detachment capacity는 control의 약 1/4
- live roots가 erodibility를 최대 약 78% 감소
- K_r는 root mass density와 exponential decrease
- tau_c는 root density와 일관된 유의 관계가 없었음

# Iber+에 대한 의미
Iber+:
```
D_fdd = K_d (tau-tau_s)
```
는 WEPP-type excess shear form과 동일한 구조 및 동일 dimension을 가진다.

따라서 뿌리 효과는 우선:
- **K_d 변화에 배치**
- tau_s는 뿌리량으로 임의 조정하지 않음
이 문헌과 부합한다.

# 고운사에 직접 사용할 수 있는 부분
- root effect를 K_d에 두고 tau_s에는 독립 측정값을 쓰는 근거
- steep-slope concentrated-flow experimental protocol

# 새로운 coupling이 필요한 부분
switchgrass regression coefficient를 고운사 참나무/초본에 그대로 이식하지 않는다.
LPJ FineRootC -> K_d는 고운사 root trait 또는 independent detachment tests로 제약한다.

# 최종 판정
- **root effect의 primary target = flow detachability K_d**
- tau_s root multiplier는 기본적으로 사용하지 않음

# 참고 링크 / DOI
https://doi.org/10.13031/trans.56.9566
