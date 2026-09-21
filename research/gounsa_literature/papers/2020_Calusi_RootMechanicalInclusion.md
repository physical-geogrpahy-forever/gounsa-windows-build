# 서지정보
Calusi, B., et al. (2020). Plant root penetration and growth as a mechanical inclusion problem. *International Journal of Non-Linear Mechanics, 120*, 103344. DOI: 10.1016/j.ijnonlinmec.2019.103344.

# 이 논문을 찾은 이유
tree throw와 무관하게 살아 있는 뿌리 성장 자체가 주변 고강도 매질을 기계적으로 변형하거나 파괴하는 정량 수치식이 존재하는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- continuum mechanics
- 실험자료와 비교

# 공간 구조
- 단일 뿌리를 원통형 inclusion으로 표현
- 뿌리-주변 매질 접촉 문제

# 적용 환경
- artificial soil
- real soil
- maize primary root

# 핵심 과정
- root axial/radial growth
- root-soil mechanical stress
- penetration resistance
- fracture-regrowth cycle

# 식생 입력
- root growth state
- root geometry
- growth-pressure response

# 핵심 식
뿌리를 탄성 원통, 주변 토양을 homogeneous elastic fracturable matrix로 두어 접촉응력을 계산하고 root-growth equation과 coupling한다.

고강도 매질에서 axial pressure가 임계값에 도달하면 root growth가 정지하고, fracture-regrowth cycle을 허용하는 수치구조를 사용한다.

개념 구조:

```
root growth
 -> contact stress
 -> matrix resistance / failure threshold
 -> fracture-regrowth response
 -> continued root elongation
```

# 파라미터와 단위
- root / matrix elastic properties
- root radius and elongation
- axial contact stress
- matrix penetration/failure resistance

정확한 parameter mapping은 원 논문의 mechanics formulation을 따라야 한다.

# 원 논문의 구현 범위
Zea mays primary root가 인공토와 실제 토양을 침투할 때의 mechanical interaction을 설명하고 실험결과와 비교한다.

# 고운사에 직접 사용할 수 있는 부분
다음 구조가 물리적으로 가능한 numerical precedent임을 보여준다.

```
root growth
 -> mechanical stress
 -> surrounding matrix failure
```

따라서 living-root biomechanical weathering을 무조건 0으로 놓아야 한다는 뜻은 아니다.

# 새로운 coupling이 필요한 부분
고운사에서는:
- LPJ-GUESS root state / radial growth
- sandstone fracture geometry
- sandstone tensile/fracture properties
를 연결해야 한다.

이는 완전한 새로운 coupling이다.

# 한계
- bedrock/sandstone 검증이 아님
- maize root와 soil matrix 대상
- landscape-scale annual rock-production flux를 출력하지 않음
- fractured sandstone의 joint propagation, fragment detachment, regolith production으로 바로 변환할 수 없음

# 최종 판정
- **보조근거 / mechanics precedent**
- production root-weathering law로 직접 채택하지 않음
- 향후 site-specific sandstone root-fracture sensitivity를 만들 때 mechanics 후보

# 참고 링크 / DOI
https://doi.org/10.1016/j.ijnonlinmec.2019.103344
