# 서지정보
Gabet, E. J., Reichman, O. J., & Seabloom, E. W. (2003). The effects of bioturbation on soil processes and sediment transport. *Annual Review of Earth and Planetary Sciences, 31*, 249-273.

# 이 논문을 찾은 이유
root growth and decay가 사면수송 flux에 직접 들어가는 published equation을 찾기 위해 검토했다.

# 연구 유형
- 리뷰 / 기계론적 수식 정리

# 공간 구조
- hillslope flux formulation

# 적용 환경
- 초지
- 관목지
- 산림

# 핵심 과정
- root-growth bioturbation
- hillslope sediment transport

# 식생 입력
- root mass
- root turnover
- root-depth distribution

# 핵심 식
`q_sx = x r tau / rho_r`; 뿌리깊이 분포를 포함한 형태로 `q_sx`를 slope와 root distribution parameter의 함수로 표현.

# 파라미터와 단위
`r`: root mass/area, `tau`: annual turnover, `rho_r`: root tissue density.

# 원 논문의 구현 범위
식생형별 root mass, turnover, depth 차이로 biogenic flux를 계산한다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS FineRootC, root turnover, rooting profile을 직접 연결하기 가장 좋은 사면수송식 후보.

# 새로운 coupling이 필요한 부분
LPJ-GUESS 탄소단위를 root mass/area로 변환하는 부분은 새로운 coupling.

# 한계
독립적인 전체 LEM이라기보다 과정식/리뷰 성격.

# 최종 판정
- 채택 후보

# 참고 링크 / DOI
https://doi.org/10.1146/annurev.earth.31.100901.141314
