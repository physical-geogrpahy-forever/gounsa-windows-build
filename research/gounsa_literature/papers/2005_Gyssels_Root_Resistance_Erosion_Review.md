# 서지정보
Gyssels, G., Poesen, J., Bochet, E., & Li, Y. (2005). *Impact of plant roots on the resistance of soils to erosion by water: a review*. Progress in Physical Geography, 29(2), 189-217. DOI: 10.1191/0309133305pp443ra.

# 이 논문을 찾은 이유
root mass density/RLD가 splash, interrill, rill erosion에 미치는 영향의 공통식을 정리하고 process별 root effectiveness 차이를 확인하기 위해 검토했다.

# 연구 유형
- review/meta-synthesis
- 수치모델 논문 아님

# 공간 구조
다수 실험연구 종합.

# 적용 환경
다양한 vegetation/soil studies; 고운사 산림을 직접 검증한 단일 모델은 아님.

# 핵심 과정
- splash
- interrill erosion
- rill erosion
- ephemeral gully erosion

# 식생 입력
- root density
- root length density
- root mass

# 핵심 식
Review synthesis:
```
SEP = exp(-b RP)
```
- SEP: soil erosion parameter relative to root-free/bare condition
- RP: root parameter such as root density or RLD
- b: root-effectiveness coefficient

Review average b values:
- splash: approximately 0
- interrill: 0.1195 for root density [kg m^-3], 0.0022 for RLD [km m^-3]
- rill: 0.5930 for root density, 0.0460 for RLD

# 파라미터와 단위
Use units exactly as defined by the review when applying the reported b values.

# 원 논문의 구현 범위
existing experimental evidence synthesis; not a standalone erosion simulator.

# 고운사에 직접 사용할 수 있는 부분
- roots matter more strongly for concentrated/rill erosion than splash
- supports separate vegetation controls for interrill vs rill
- provides empirical ranges/checks for sensitivity analysis

# 새로운 coupling이 필요한 부분
SEP relation inserted into a 2D erosion engine is **new coupling** unless directly implemented by a cited model.

# 한계
- review coefficients combine heterogeneous experiments
- not a mountain-forest numerical-model validation
- should not replace WEPP/PROMET/ELM-Erosion model implementations

# 최종 판정
**채택 as empirical synthesis/check, not final model.**

# 참고 링크 / DOI
10.1191/0309133305pp443ra
