# 서지정보
Gabet, E. J., Reichman, O. J., & Seabloom, E. W. (2003). The effects of bioturbation on soil processes and sediment transport. 원문 서지 세부사항은 재검증 필요.

# 이 논문을 찾은 이유
피복률이 아니라 실제 root mass와 root turnover를 이용해 사면방향 토사이동을 계산하는 수치식이 있는지 확인하기 위해 검색했다.

# 연구 유형
- 수치모델 / 과정식

# 공간 구조
- 사면방향 flux 식
- 완전한 2D LEM은 아님

# 적용 환경
- 자연사면
- 식생형별 root depth distribution

# 핵심 과정
- biogenic hillslope transport
- root growth and decay에 의한 토양 변위

# 식생 입력
- root mass per unit area r [kg m^-2]
- annual root turnover tau [yr^-1]
- root density rho_r
- root depth-distribution parameter beta

# 핵심 식
채팅에서 복구된 핵심 형태:
q_sx = x r tau / rho_r
또한 root-depth distribution과 slope를 이용한 정리식이 제시된 것으로 검토했다.

# 파라미터와 단위
- r: kg m^-2
- tau: yr^-1
- rho_r: root tissue density
- beta: root depth distribution parameter
세부 계수는 원문 재검증 필요.

# 원 논문의 구현 범위
연간 root growth/decay cycle에 따른 biogenic sediment flux를 계산한다. 장기 지형발달모델 전체를 직접 제공하는 것은 아니다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS FineRootC를 root mass로 변환하고 연간 root turnover와 결합해 별도 q_bio 항을 구성하는 과정적 선례.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC/turnover -> Gabet식 q_bio -> 고운사 DEM 갱신은 새로운 coupling이다.

# 한계
- 토양 변위에 대한 강한 단순화 가정
- 고운사 100년 적용 시 계수와 root-depth parameter 재보정 필요
- background physical diffusion과 구분해야 함

# 최종 판정
- 보조근거
- 100년 strict-biomass biogenic transport 후보
- background diffusion 자체의 대체식으로는 채택하지 않음

# 참고 링크 / DOI
원문 DOI/정확한 서지는 원문 재검증 필요.
