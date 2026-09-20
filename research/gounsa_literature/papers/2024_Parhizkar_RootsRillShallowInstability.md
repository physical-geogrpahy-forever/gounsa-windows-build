# 서지정보
Parhizkar, M., Lucas-Borja, M. E., & Zema, D. A. (2024). Plant roots reduce rill detachment and shallow instability in forest topsoils. Rhizosphere, 31, 100921. https://doi.org/10.1016/j.rhisph.2024.100921

# 이 논문을 찾은 이유
상층 교목과 하층 초본의 경쟁이 erosion resistance에 어떤 문제를 만들 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- 현장/실험

# 공간 구조
- forest topsoil plot/sample

# 적용 환경
- forest canopy 아래 토양

# 핵심 과정
- rill detachment
- shallow instability
- tree-grass competition

# 식생 입력
- tree roots
- grass cover suppression
- root total length
- root mass density
- specific root length

# 핵심 식
현재 채팅에서 확인한 정량결과:
tree canopy 아래 soil detachment capacity가 bare soil보다 약 41% 낮았고 aggregate stability는 약 83% 높았다. Dc와 root total length, RMD, SRL 사이 음의 관계가 보고되었다.

# 파라미터와 단위
root length, RMD, SRL, Dc. 정확한 단위와 회귀식은 원문 재검증 필요.

# 원 논문의 구현 범위
tree canopy 아래에서 tree-grass competition과 root system이 rill detachment 및 shallow stability에 미치는 영향을 평가한다.

# 고운사에 직접 사용할 수 있는 부분
상층 교목 biomass가 많다고 하층 지표보호를 자동으로 대리할 수 없다는 근거. LPJ-GUESS understory suppression을 보존할 이유가 된다.

# 새로운 coupling이 필요한 부분
tree cohort와 herb cohort의 경쟁결과를 cell-scale erodibility로 연결하는 것은 새로운 coupling이다.

# 한계
수치지형모델 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.rhisph.2024.100921
