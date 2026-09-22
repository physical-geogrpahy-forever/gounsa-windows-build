# 서지정보
Sato, H., & Sumida, A. (2025). Crown structure and competitive interactions in mixed forests: Insights from an individual-based model. Ecological Research, 40(5). DOI: 10.1111/1440-1703.12562

# 이 논문을 찾은 이유
고운사와 유사한 냉온대 침엽수-활엽수 혼효림에서 SEIB-DGVM이 세밀한 공간구조로 실제 적용되고 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- individual-based cold-temperate forest dynamics

# 공간 구조
- 100 m x 100 m spatially explicit virtual forest
- individual trees
- crown geometry and competition

# 적용 환경
- 냉온대 침엽수-활엽수 혼효림

# 핵심 과정
- establishment
- growth
- mortality
- crown competition
- species/PFT differences in allometry and allocation

# 식생 입력
- individual tree DBH
- crown dimensions
- trunk
- crown
- fine roots

# 핵심 식
2023 modifications include empirical allometry and allocation rules for cold-temperate woody PFTs. 2025 work further evaluates crown structure and competition.

# 파라미터와 단위
- virtual forest: 100 m x 100 m
- internal individual-tree spatial representation

# 원 논문의 구현 범위
냉온대 혼효림 구조와 경쟁을 개별목 수준에서 재현한다.

# 고운사에 직접 사용할 수 있는 부분
- 고운사의 온대 산림과 기후생태적 거리가 열대 TROLL보다 작음
- 30 m를 넘는 virtual forest area도 사용 가능함을 보여줌
- LiDAR-derived crown structure와 직접 비교 가능한 상태량

# 새로운 coupling이 필요한 부분
- 한국 수종/PFT parameterization
- 산불 후 초기조건
- root architecture
- litter surface redistribution
- LiDAR tree segmentation -> SEIB initialization

# 한계
fine roots are represented as formless entities; detailed horizontal root geometry is absent.

# 최종 판정
- 채택: SEIB cold-temperate applicability의 핵심 근거

# 참고 링크 / DOI
https://doi.org/10.1111/1440-1703.12562
