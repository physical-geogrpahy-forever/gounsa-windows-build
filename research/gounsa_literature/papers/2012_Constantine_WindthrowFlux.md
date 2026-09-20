# 서지정보
Constantine, J. A., Schelhaas, M.-J., Gabet, E., & Mudd, S. M. (2012). Limits of windthrow-driven hillslope sediment flux due to varying storm frequency and intensity. *Geomorphology, 175-176*, 66-73.

# 이 논문을 찾은 이유
forest succession과 동적 나무크기 분포를 windthrow sediment flux에 연결한 모델을 찾기 위해 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- forest-gap / hillslope coupling

# 적용 환경
- 산림

# 핵심 과정
- windthrow sediment flux

# 식생 입력
- tree size distribution
- tree population
- storm-dependent throw probability

# 핵심 식
tree population, size, storm intensity를 통해 throw flux를 계산한다. 단일 단순식보다 population model 구조가 핵심이다.

# 파라미터와 단위
DBH/size, density, storm frequency/intensity, root-plate/displaced volume.

# 원 논문의 구현 범위
ForGEM forest-gap model과 windthrow flux 결합.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS woody cohort DBH/height/density를 활용할 구조적 선례.

# 새로운 coupling이 필요한 부분
LPJ-GUESS cohort를 원 모델의 tree-population 변수에 매핑하면 새로운 coupling.

# 한계
산불 후 dead wood/CWD와 root-growth creep는 별도.

# 최종 판정
- 채택 구조의 핵심 참고

# 참고 링크 / DOI
https://doi.org/10.1016/j.geomorph.2012.06.022
