# 서지정보
Crompton, O., Katul, G., Lapides, D., & Thompson, S. (2023). Hydrologic connectivity and patch-to-hillslope scale relations in dryland ecosystems. *Geophysical Research Letters, 50*(10), e2022GL101801. https://doi.org/10.1029/2022GL101801

# 이 논문을 검색한 이유
동일한 비율의 식생이더라도 패치의 실제 공간배치, 표면거칠기와 침투능 차이로 물이 식생 안으로 들어가는지 아니면 식생을 우회하는지 검증하기 위해서다.

# 연구 유형
원본 출판 2D Saint-Venant 수리모형에 의한 가상 패치 지형실험. Hairsine–Rose/침식-퇴적 독립 보존 모형 자체는 아님.

# 공간 구조
2D 천수방정식, patchy vegetation vs bare soil, tracer advected flow paths, flow connectivity inside hillslope와 outlet connectivity 비교.

# 적용환경
반건조 식생패치 사면; 고운사 억새와 참나무 맹아 식생에 대한 직접 현장보정이 아님.

# 핵심 과정
식생패치의 높은 침투성은 유출수를 받아들여 run-on 경로를 촉진하지만, 식생의 높은 거칠기는 물을 식생 바깥으로 우회시켜 연결된 노출토양 경로를 형성할 수 있음. 출구연결성과 사면 유출손실 간 관계를 모델실험으로 검토함.

# 식생 입력
공간적 식생 점유, patch-specific hydraulic conductivity and surface resistance; 줄기별 SF/TF는 없음.

# 핵심 식 및 단위
2D Saint-Venant mass/momentum conservation; 출구까지 tracer 경로 길이 vs 식생패치 유입 길이. 2D 식생의 물리적 장애물 및 soil K는 각각 다르게 공급.

# 고운사에 직접 사용할 수 있는 부분
밀생 억새와 군데군데 참나무 맹아의 실제 vegetation map을 original 2D finite volume infiltration/runoff engine에 분포형 parameter field로 넣어야 한다는 근거. 수관 차이만 주고 spatial runoff source connectivity를 없애면 원래 질문을 풀 수 없음.

# 새로운 coupling
Per-stem oak SF/per-tussock Miscanthus SF and throughfall/drip KE, root/litter/fragment fields, patch-resolved erosion/sediment 2D mass balance. 해당 논문에 이 전체과정이 기존 구현됐다고 주장 금지.

# 한계
반건조지 model, 유사수지 부재, site species 근거 미포함. 연결성과 토사유출의 단순 단조관계를 모든 침투-거칠기 조합에 적용 금지.

# 최종 판정
공간적 수문연결성 구현 근거 핵심 채택.

# 참고 링크
https://research.fs.usda.gov/treesearch/66866
