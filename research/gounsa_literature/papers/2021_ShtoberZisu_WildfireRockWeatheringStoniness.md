# 서지정보
Shtober-Zisu, N., & Wittenberg, L. (2021). Long-term effects of wildfire on rock weathering and soil stoniness in the Mediterranean landscapes. *Science of the Total Environment, 762*, 143125. https://doi.org/10.1016/j.scitotenv.2020.143125

# 이 논문을 찾은 이유
고운사 가설인 `큰 fire-spall -> postfire weathering/fragmentation -> 작은 석력 증가 -> 원래 spall의 소실`이 실제 장기 산불현장에서 관찰되는지 확인하기 위해 검토했다.

# 연구 유형
- 10-year postfire field study
- rock-weathering and soil-stoniness monitoring

# 공간 구조
- rock outcrop
- adjacent hillslope soil

# 적용 환경
- Mt. Carmel, Israel
- Mediterranean wildfire landscape
- chalk, limestone, dolomite

# 핵심 과정
- fire-induced exfoliation/spalling
- postfire weathering
- spall breakdown and pulverization
- rock-fragment enrichment
- surface stoniness change

# 식생 입력
- 직접 정량 식생변수 없음
- wildfire disturbance context

# 핵심 식
보편적인 weathering equation보다 10년 시간변화가 핵심이다.
대형산불의 thermal shock은 최대 약 20 cm 깊이까지 rock exfoliation을 만들었고, 10년 뒤 대부분의 flakes/spalls가 노두와 인접 토양에서 사라졌다.
남은 spalls/flakes는 파쇄 및 pulverization 되었으며, chalk에서는 >16 mm의 큰 gravel과 median 8-16 mm 입도가 관찰되어 큰 spall의 fragmentation을 시사했다.
burned chalk soil의 stoniness는 non-burned 23-39%에서 69-86%로 크게 증가했다.

# 파라미터와 단위
- time since fire: 10 years
- stoniness: %
- fragment size: mm
- weathering depth: up to ~20 cm

# 원 논문의 구현 범위
산불로 생성된 spall이 화재 직후 고정되어 남는 것이 아니라 이후 수년-10년 규모의 weathering으로 파쇄되고 형상과 토양 stoniness를 변화시키는 장기 연쇄를 직접 관찰한다.

# 고운사에 직접 사용할 수 있는 부분
- `fire spall -> large flakes/spalls -> postfire breakdown/pulverization -> smaller fragments`의 직접 장기 현장근거
- armour 상태는 fire 직후 초기조건으로 고정하지 않고 시간에 따라 입도와 형상이 변화해야 함
- fire-induced fragment supply가 fines removal과 별개로 surface stoniness를 증가시킬 수 있음

# 새로운 coupling이 필요한 부분
고운사 사암에서 size-class별 weathering transition rate와 fine-regolith production rate를 계산하는 것은 **새로운 coupling**이다.

# 한계
carbonate lithology이며 사암에 계수를 직접 이식할 수 없다. fragment가 작아진 뒤 실제 removal rate가 어떻게 바뀌는지는 별도 transport 문헌이 필요하다.

# 최종 판정
- 핵심 채택
- postfire spall weathering/fragmentation의 가장 직접적인 장기 현장근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.scitotenv.2020.143125
