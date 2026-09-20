# 서지정보
Gabet, E. J., Reichman, O. J., & Seabloom, E. W. (2003). *The effects of bioturbation on soil processes and sediment transport*. Annual Review of Earth and Planetary Sciences, 31, 249-273. DOI: 10.1146/annurev.earth.31.100901.141314.

# 이 논문을 찾은 이유
피복률이 아니라 실제 root mass, root turnover, root-depth distribution을 이용해 biogenic hillslope sediment flux를 계산하는 published process equation을 찾기 위해 검토했다.

# 연구 유형
- 리뷰
- 기계론적 과정식 정리

# 공간 구조
- hillslope flux formulation
- 완전한 2D LEM은 아님

# 적용 환경
- 초지
- 관목지
- 산림
- 자연사면

# 핵심 과정
- root-growth bioturbation
- root growth and decay에 의한 토양 변위
- hillslope sediment transport

# 식생 입력
- root mass per unit area r [kg m^-2]
- annual root turnover tau [yr^-1]
- root tissue density rho_r
- root-depth distribution parameter beta

# 핵심 식
채팅에서 복구된 핵심 형태:
```
q_sx = x r tau / rho_r
```
또한 root-depth distribution과 slope를 포함한 형태로 flux를 정리한다.

# 파라미터와 단위
- r: root mass per unit area [kg m^-2]
- tau: annual root turnover [yr^-1]
- rho_r: root tissue density
- beta: root-depth distribution parameter

세부 계수는 원문 기준으로 확인한다.

# 원 논문의 구현 범위
연간 root growth/decay cycle에 따른 biogenic sediment flux를 계산하는 과정식을 정리한다. 독립적인 전체 LEM은 아니다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS FineRootC를 root mass로 변환하고 연간 root turnover 및 rooting profile과 결합해 별도 `q_bio` 항을 구성하는 가장 직접적인 문헌 근거 중 하나다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC/turnover -> Gabet식 q_bio -> 고운사 DEM 갱신은 새로운 coupling이다.

# 한계
- root-induced transport를 단순화한 process formulation
- 고운사 100년 적용 시 root-depth parameter 및 단위변환 확인 필요
- background physical diffusion과 분리해야 함

# 최종 판정
- 채택 후보
- 100년 strict-biomass biogenic transport 핵심근거
- background diffusion 자체의 대체식으로는 사용하지 않음

# 참고 링크 / DOI
https://doi.org/10.1146/annurev.earth.31.100901.141314
