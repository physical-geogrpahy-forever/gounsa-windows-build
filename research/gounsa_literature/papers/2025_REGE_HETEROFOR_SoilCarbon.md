# 서지정보
REGE+ project final report (2025). Forest regeneration under climate and environmental changes. BRAIN-be 2.0 / Belgian Science Policy. HETEROFOR soil organic carbon module section.

# 이 논문을 찾은 이유
산불 이후 dead root, CWD, litter가 지형과정에 중요하므로 최신 HETEROFOR 계보가 고사유기물 pool을 실제로 분리하는지 확인했다.

# 연구 유형
- 연구과제 최종보고서
- 모델개발 보고

# 공간 구조
- HETEROFOR stand/tree framework
- soil horizons
- organic matter pools

# 적용 환경
- 온대 산림

# 핵심 과정
HETEROFOR soil carbon module에서:
- aboveground standing deadwood (snags)
- aboveground lying deadwood
- belowground deadwood
- aboveground decaying litter
- belowground decaying litter
- active/stable soil carbon
을 구분한다.

# 식생 입력
- dead woody biomass
- leaf litter
- fine-root litter
- belowground woody mortality

# 핵심 식
cohort-based litter/deadwood decomposition and transfer into active/stable carbon pools. 세부 parameterization은 보고서의 soil carbon section과 도식에 제시된다.

# 파라미터와 단위
- carbon pools and decomposition rates
- depth-dependent soil carbon pools

# 원 논문의 구현 범위
고사목과 litter의 지상/지하 탄소동태를 HETEROFOR에 추가한다.

# 고운사에 직접 사용할 수 있는 부분
- 산불 후 CWD와 belowground deadwood 상태를 분리할 모델 골격
- fine-root litter와 woody-root death를 별도 지형효과로 연결할 가능성
- litter/CWD 장기감쇠

# 새로운 coupling이 필요한 부분
- fire severity로 생성되는 각 dead pool의 초기량
- dead-root pool -> erosion resistance decay
- CWD -> sediment storage/connectivity
- litter mass -> rainfall detachment protection

# 한계
peer-reviewed model-description paper가 아니라 프로젝트 보고서이다. fire combustion 자체를 계산하는 모듈 근거는 아니다.

# 최종 판정
- 보조근거
- 최신 HETEROFOR dead-organic-state 기능 확인에 중요

# 참고 링크
https://www.belspo.be/belspo/brain2-be/projects/FinalReports/REGE_FinRep.pdf
