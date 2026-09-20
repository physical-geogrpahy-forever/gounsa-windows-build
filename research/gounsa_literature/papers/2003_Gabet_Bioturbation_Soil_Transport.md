# Gabet, Reichman & Seabloom (2003)

# 서지정보
Gabet, E. J., Reichman, O. J., & Seabloom, E. W. (2003). The effects of bioturbation on soil processes and sediment transport. *Annual Review of Earth and Planetary Sciences, 31*, 249-273. https://doi.org/10.1146/annurev.earth.31.100901.141314

# 이 논문을 찾은 이유
사면확산을 leaf cover가 아니라 root mass, turnover, depth로 계산할 수 있는 식을 찾기 위해 검토했다.

# 연구 유형
- 리뷰 + mechanistic derivation

# 공간 구조
- hillslope sediment-flux formulation

# 적용 환경
- grassland, shrubland, forest

# 핵심 과정
- root growth/decay bioturbation
- hillslope sediment transport

# 식생 입력
- root mass per area
- annual root turnover
- root vertical distribution

# 핵심 식
채팅에서 `q_sx = x r tau / rho_r`와 root-depth distribution을 포함한 형태 `q_sx = -0.003 r tau /(rho_r ln beta_r) sin(theta) cos(theta)`를 검토했다. exact notation은 원문 재검증 필요.

# 파라미터와 단위
r: root mass per area, tau: turnover, rho_r: root tissue density, beta_r: root-distribution parameter, theta: slope.

# 원 논문의 구현 범위
뿌리 성장과 사망에 따른 토양변위를 sediment flux로 변환.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS FineRootC, root turnover, root-depth distribution을 사면수송에 연결할 핵심식.

# 새로운 coupling이 필요한 부분
LPJ-GUESS carbon mass를 dry root mass와 spatial root distribution으로 변환하는 것은 새로운 coupling.

# 한계
완성된 modern distributed LEM이 아니라 과정식/리뷰 성격.

# 최종 판정
- 채택
- root-growth/decay biogenic transport 핵심근거

# 참고 링크 / DOI
- https://doi.org/10.1146/annurev.earth.31.100901.141314
