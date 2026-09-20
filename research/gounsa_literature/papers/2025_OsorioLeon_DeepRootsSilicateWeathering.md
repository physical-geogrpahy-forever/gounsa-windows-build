# 서지정보
Osorio-Leon, J. J., et al. (2025). Deep Roots Supply Reactivity and Enhance Silicate Weathering in the Bedrock Vadose Zone. AGU Advances, 6(3), e2025AV001692. https://doi.org/10.1029/2025AV001692

# 이 논문을 찾은 이유
deep roots가 bedrock vadose zone의 chemical weathering을 정량적으로 얼마나 강화하는지 확인하기 위해 검토했다.

# 연구 유형
- 현장관측 + reactive-transport modeling

# 공간 구조
- 약 16 m bedrock vadose-zone profile

# 적용 환경
- forested Critical Zone
- weathered bedrock

# 핵심 과정
- deep-root respiration
- subsurface CO2
- silicate weathering
- solute production

# 식생 입력
- deep-root-associated CO2 production
- deep rhizosphere activity

# 핵심 식
상세 반응식은 원문 재검증 필요. 현재 채팅에서 확인된 정량 결과:
- deep rhizosphere activity가 BVZ weathering solute flux의 약 43 ± 3%
- deep-rhizosphere carbonic acid가 있는 경우 chemical weathering이 background 대비 약 1.8 ± 0.1배

# 파라미터와 단위
weathering solute flux, CO2 production, depth. 상세 단위 원문 재검증 필요.

# 원 논문의 구현 범위
깊은 뿌리의 생물호흡을 reactive transport에 넣어 관측된 bedrock-zone chemistry를 재현한다.

# 고운사에 직접 사용할 수 있는 부분
C/Cr 내 deep roots를 수분흡수뿐 아니라 chemical-weathering source로 처리할 강한 최신 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC(z)와 root respiration을 이 논문의 chemical-weathering modifier로 연결하는 것은 새로운 coupling이다.

# 한계
특정 parent material과 Critical Zone 조건의 정량배수를 고운사에 직접 적용하면 안 된다.

# 최종 판정
- 채택 후보의 화학풍화 핵심 근거

# 참고 링크 / DOI
https://doi.org/10.1029/2025AV001692
