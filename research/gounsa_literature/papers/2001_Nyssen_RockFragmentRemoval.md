# 서지정보
Nyssen, J., Haile, M., Poesen, J., Deckers, J., & Moeyersons, J. (2001). Removal of rock fragments and its effect on soil loss and crop yield, Tigray, Ethiopia. *Soil Use and Management, 17*(3), 179–187. https://doi.org/10.1111/j.1475-2743.2001.tb00025.x

# 이 논문을 찾은 이유
고운사에서 표면 석력과 fire spall이 세립질 토양유실을 억제하는 armour 역할을 할 수 있는지 직접적인 현장 조작실험 근거를 찾기 위해 검토했다.

# 연구 유형
- 현장실험
- 농경지 runoff plot 조작실험

# 공간 구조
- 5 m × 6 m runoff plot 12개
- 분포형 수치모델 아님

# 적용 환경
- 에티오피아 북부 Tigray 고지
- Vertic Cambisol
- 평균 경사 0.125 m m^-1
- 경작지

# 핵심 과정
- 표면 석력피복
- 수식침식
- 토양유실
- 토양수분 보전

# 식생 입력
- 작물 재배조건
- 식생량을 지형과정의 정량 입력으로 사용한 연구는 아님

# 핵심 식
수치모델 식을 제안한 연구가 아니라 석력 제거 처리에 따른 토양유실 변화를 측정한 현장실험이다.

현재 채팅에서 확인한 1999년 처리 결과:
- 거의 전부 제거: 약 27.4 kg m^-1 yr^-1
- 절반 제거: 약 19.6 kg m^-1 yr^-1
- 대조구: 약 8.7 kg m^-1 yr^-1

정확한 표 번호와 단위 정의는 원문 표 재검증 권장.

# 파라미터와 단위
- surface rock fragment cover: %
- soil loss: kg m^-1 yr^-1로 현재 채팅에서 확인
- plot size: 5 m × 6 m

# 원 논문의 구현 범위
표면 석력 제거 정도를 인위적으로 조절해 토양유실의 변화를 직접 측정한다.

# 고운사에 직접 사용할 수 있는 부분
표면 석력이 세립질 토양유실을 억제할 수 있다는 직접 현장조작 근거. 고운사에서 fire spall이 표면에 잔류할 경우 sediment supply 증가와 반대로 armour 효과를 낼 수 있다는 가설의 근거가 된다.

# 새로운 coupling이 필요한 부분
고운사 모델에서 surface coarse fraction 또는 spall cover를 fine-soil erodibility에 연결하는 함수는 원 논문에 없다. 이를 수치모델에 넣는 것은 새로운 coupling이다.

# 한계
- 농경지이며 산불 후 산림사면이 아님
- fire spall 연구가 아님
- 석력의 크기, 배치, 매몰 정도가 고운사와 다를 수 있음
- 현장실험 결과를 그대로 고운사 계수로 사용하면 안 됨

# 최종 판정
- 보조근거로 채택
- fire spall 자체의 효과를 정량화한 연구는 아님

# 참고 링크 / DOI
https://doi.org/10.1111/j.1475-2743.2001.tb00025.x
