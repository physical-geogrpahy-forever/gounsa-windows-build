# 서지정보
Li, X., Fu, S., Hu, Y., & Liu, B. (2022). Effects of rock fragment coverage on soil erosion: Differ among rock fragment sizes? *CATENA, 214*, 106248. https://doi.org/10.1016/j.catena.2022.106248

# 이 논문을 찾은 이유
큰 fire-spall이 작은 fragment로 바뀔 때 armour protection과 runoff/erosion이 어떻게 달라질지 입도 의존성을 확인하기 위해 검토했다.

# 연구 유형
- simulated-rainfall experiment

# 공간 구조
- erosion plot

# 적용 환경
- stony hillslope analogue

# 핵심 과정
- runoff
- sediment concentration
- soil loss
- rill erosion
- size-dependent shielding

# 식생 입력
- 없음

# 핵심 식
rock-fragment size 0.7-36 cm와 cover 15-60%를 조합했다.
12 cm 미만 fragment는 대체로 runoff와 soil loss를 줄였지만, 12 cm 이상에서는 runoff와 soil loss가 증가할 수 있었다.
작은 fragments는 같은 cover에서 더 많은 장애물을 만들고 flow-path tortuosity를 높여 유속을 늦추고 infiltration 시간을 늘리는 것으로 해석된다.

# 파라미터와 단위
- fragment size: 0.7, 1.1, 3.0, 5.5, 12.0, 18.8, 26.4, 36.0 cm
- cover: 15, 30, 45, 60%
- antecedent moisture: dry/wet runs

# 원 논문의 구현 범위
fragment cover의 erosion effect가 입도와 antecedent moisture에 따라 비선형적으로 달라짐을 정량화한다.

# 고운사에 직접 사용할 수 있는 부분
- armour는 cover만이 아니라 grain-size distribution을 가져야 한다.
- 큰 spall의 fragmentation이 무조건 armour를 약화시키는 것은 아니다.
- 작은 fragments가 제자리에 남아 있으면 오히려 shielding/hydraulic roughness가 강화될 수 있으므로 `fragmentation`과 `removal`을 분리해야 한다.

# 새로운 coupling이 필요한 부분
weathering/spall fragmentation에 따른 size-class transition과 size-class별 removal을 동적 armour 모듈에 넣는 것은 **새로운 coupling**이다.

# 한계
토양 및 실험경사가 고운사와 동일하지 않으며 fire-spall 자체를 생성하지 않는다.

# 최종 판정
- 핵심 채택
- size-class armour 구조의 핵심 근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2022.106248
