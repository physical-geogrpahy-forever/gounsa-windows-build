# 서지정보
Kim, D., Ahn, B., Kim, M. P., & Im, S. (2014). *Morphological Characteristics Analysis of Root Plate in Wind-Uprooted Trees*. Journal of Korean Society of Forest Science, 103(2), 248-257. DOI: 10.14578/jkfs.2014.103.2.248.

# 이 논문을 찾은 이유
Gallaway 2009의 Canadian DBH-root-plate 관계를 그대로 사용하지 않고, 한국 산림에서 DBH와 실제 uprooted root-plate geometry의 지역 자료를 확보하기 위해 검토했다.

# 연구 유형
- post-typhoon field survey
- root-plate morphology/allometry

# 공간 구조
- 서울대학교 태화산학술림
- 태풍으로 실제 전도된 개체 측정

# 적용 환경
- Korean temperate forest
- granite parent material
- Larix kaempferi 77개체
- Pinus koraiensis 24개체
- 2012 Typhoon Bolaven windthrow

# 핵심 과정
- wind uprooting
- root-plate geometry
- DBH-root-system allometry
- uprooting-direction root asymmetry

# 측정 상태
조사한 root plate는 평면에서 타원/원형, 측면에서 반타원체에 가까웠다.

평균 DBH:
- Larix kaempferi: 약 24.2 cm
- Pinus koraiensis: 약 28.1 cm

평균 root-plate depth:
- Larix: 약 0.74 m
- Pinus koraiensis: 약 0.69 m

평균 root-plate height:
- Larix: 약 1.55 m
- Pinus koraiensis: 약 1.71 m

평균 root-plate width:
- Larix: 약 2.23 m
- Pinus koraiensis: 약 2.42 m

# DBH 관계
DBH는 tree height보다 belowground root-plate properties와 더 강한 상관을 보였다.

보고된 상관 예:
- Larix DBH-root plate height: r 약 0.635
- Larix DBH-root plate width: r 약 0.645
- Larix DBH-root surface area: r 약 0.525
- Pinus koraiensis DBH-root plate height: r 약 0.453
- Pinus koraiensis DBH-root surface area: r 약 0.531

논문은 유의한 지상부-지하부 변수에 대해 simple linear relationships를 도출했다.

정확한 Figure 9/10 회귀계수는 현재 텍스트 소스에서 안전하게 전사되지 않았으므로, coding 전에 원 Figure를 직접 확인한다.

# 방향성
전도방향 쪽 root plate에서:
- root number
- root surface area

가 반대방향보다 더 컸다.

따라서 root plate를 완전 대칭구조로 보는 것은 단순화다.

# 고운사에 직접 사용할 수 있는 부분
고운사 tree-throw geometry의 **국내 최우선 지역 calibration 자료**.

우선순위:
```
한국 local allometry
>
Gallaway Canadian allometry
>
generic rootwad geometry
```

특히 LPJ-GUESS가 제공하는 DBH를 root-plate width/depth/volume로 변환할 때 local species calibration의 기준이 된다.

# 새로운 coupling
```
LPJ-GUESS DBH
 -> Kim et al. root-plate geometry
 -> pit/mound event
```
결합은 새로운 coupling이다.

# 한계
- 낙엽송과 잣나무
- 고운사의 실제 우점종 전체를 포함하지 않음
- 이미 전도된 나무만 측정했으므로 uprooting probability model은 아님
- DBH-root plate 관계의 설명력이 완전하지 않음

# 최종 판정
**핵심 채택: 고운사 tree-throw root-plate geometry의 국내 지역 보정근거.**

전도 확률은 ForestGALES/Gallaway 등 별도 모델이 필요하다.

# 참고 링크 / DOI
https://doi.org/10.14578/jkfs.2014.103.2.248
