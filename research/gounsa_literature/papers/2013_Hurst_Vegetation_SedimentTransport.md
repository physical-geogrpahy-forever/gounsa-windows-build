# 서지정보
Hurst et al. (2013). JGR Earth Surface. DOI: 10.1002/jgrf.20049. 정확한 논문명과 전체 저자목록은 원문 재검증 필요.

# 이 논문을 찾은 이유
2010년대 이후 산림 식생량 또는 AGB와 hillslope sediment transport coefficient D의 관계를 검토하기 위해 찾았다.

# 연구 유형
- 지형계측 + 모델/역산 해석
- 단순 현장실험만은 아님

# 공간 구조
- 산림 사면의 hillslope transport 해석
- 세부 수치격자 구조는 원문 재검증 필요

# 적용 환경
- 산림 산지

# 핵심 과정
- hillslope diffusion / colluvial transport
- biogenic transport

# 식생 입력
- AGB 대리변수
- canopy-height 계열 정보

# 핵심 식
현재 채팅에서 확정한 핵심은 sediment transport coefficient D가 aboveground biomass와 연계될 수 있는지를 검정했다는 점이다. 보편적인 biomass-D 식을 확정한 논문으로 취급하지 않는다.

# 파라미터와 단위
- D: hillslope transport coefficient
- AGB 관련 변수
- 정확한 식과 단위는 원문 재검증 필요

# 원 논문의 구현 범위
산림에서 식생량과 hillslope transport efficiency의 공간적 관계를 검토.

# 고운사에 직접 사용할 수 있는 부분
biomass가 hillslope transport에 영향을 줄 수 있다는 2010년대 산림 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS의 연간 biomass를 D에 직접 연결하는 것은 원 논문에 없는 새로운 coupling.

# 한계
공간적 AGB-D 관계를 100년 시간변화식으로 그대로 전환할 수 없음.

# 최종 판정
- 보조근거
- 고운사 100년 Kd 식의 직접 채택 근거는 아님

# 참고 링크 / DOI
https://doi.org/10.1002/jgrf.20049
